#!/usr/bin/env python3
"""Audit kênh YouTube đối thủ qua YouTube Data API v3 (chỉ dùng thư viện chuẩn).

Dùng:
    export YOUTUBE_API_KEY=...            # hoặc đặt trong .env
    python3 shared/automation/youtube_channel_audit.py \
        --channels projects/01-youtube-ai-finance/research/competitors/channels.txt \
        --out projects/01-youtube-ai-finance/data/processed/channel-audit

channels.txt: mỗi dòng một kênh — @handle, URL kênh, hoặc channel ID (UC...). Dòng bắt đầu bằng # bị bỏ qua.

Đầu ra (trong thư mục --out, gắn ngày):
    YYYY-MM-DD-channels.csv  — số liệu kênh: sub, view, số video, ngày tạo, tần suất đăng, view trung vị 30 video gần nhất…
    YYYY-MM-DD-videos.csv    — các video gần nhất của từng kênh: tiêu đề, ngày đăng, thời lượng, view, like, comment,
                               hệ số outlier (view / trung vị view của kênh)

Quota: mỗi kênh tốn khoảng 3–5 đơn vị (channels.list + playlistItems.list + videos.list); mặc định 10.000 đơn vị/ngày.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import re
import statistics
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://www.googleapis.com/youtube/v3/"


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip())


def call(endpoint: str, key: str, **params) -> dict:
    params["key"] = key
    url = API + endpoint + "?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as err:
        detail = err.read().decode("utf-8", "replace")[:300]
        raise SystemExit(f"Lỗi API {err.code} tại {endpoint}: {detail}")


def parse_channel_ref(ref: str) -> dict:
    ref = ref.strip()
    m = re.search(r"(UC[\w-]{22})", ref)
    if m:
        return {"id": m.group(1)}
    m = re.search(r"@([\w.\-]+)", ref)
    if m:
        return {"forHandle": "@" + m.group(1)}
    return {"forHandle": "@" + ref}


def iso_duration_seconds(value: str) -> int:
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", value or "")
    if not m:
        return 0
    d, h, mi, s = (int(x or 0) for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + s


def audit_channel(ref: str, key: str, max_videos: int) -> tuple[dict, list[dict]]:
    data = call("channels", key, part="snippet,statistics,contentDetails", **parse_channel_ref(ref))
    if not data.get("items"):
        print(f"  ! Không tìm thấy kênh: {ref}", file=sys.stderr)
        return {}, []
    ch = data["items"][0]
    uploads = ch["contentDetails"]["relatedPlaylists"]["uploads"]

    video_ids: list[str] = []
    page = None
    while len(video_ids) < max_videos:
        params = {"part": "contentDetails", "playlistId": uploads, "maxResults": 50}
        if page:
            params["pageToken"] = page
        items = call("playlistItems", key, **params)
        video_ids += [it["contentDetails"]["videoId"] for it in items.get("items", [])]
        page = items.get("nextPageToken")
        if not page:
            break
    video_ids = video_ids[:max_videos]

    videos: list[dict] = []
    for i in range(0, len(video_ids), 50):
        batch = call("videos", key, part="snippet,statistics,contentDetails", id=",".join(video_ids[i:i + 50]))
        for v in batch.get("items", []):
            stats = v.get("statistics", {})
            secs = iso_duration_seconds(v["contentDetails"].get("duration", ""))
            videos.append({
                "channel": ch["snippet"]["title"],
                "video_id": v["id"],
                "url": f"https://www.youtube.com/watch?v={v['id']}",
                "title": v["snippet"]["title"],
                "published": v["snippet"]["publishedAt"][:10],
                "duration_sec": secs,
                "is_short_guess": secs <= 180,
                "views": int(stats.get("viewCount", 0)),
                "likes": int(stats.get("likeCount", 0)),
                "comments": int(stats.get("commentCount", 0)),
            })

    long_views = [v["views"] for v in videos if not v["is_short_guess"]] or [v["views"] for v in videos] or [0]
    median_views = statistics.median(long_views)
    for v in videos:
        v["outlier_x"] = round(v["views"] / median_views, 2) if median_views else 0

    dates = sorted(dt.date.fromisoformat(v["published"]) for v in videos)
    span_days = max((dates[-1] - dates[0]).days, 1) if len(dates) > 1 else 0
    st = ch["statistics"]
    summary = {
        "channel": ch["snippet"]["title"],
        "channel_id": ch["id"],
        "handle": ch["snippet"].get("customUrl", ""),
        "country": ch["snippet"].get("country", ""),
        "created": ch["snippet"]["publishedAt"][:10],
        "subscribers": int(st.get("subscriberCount", 0)),
        "total_views": int(st.get("viewCount", 0)),
        "video_count": int(st.get("videoCount", 0)),
        "sampled_videos": len(videos),
        "uploads_per_week": round(len(videos) / span_days * 7, 2) if span_days else "",
        "shorts_share": round(sum(v["is_short_guess"] for v in videos) / len(videos), 2) if videos else "",
        "median_views_long": int(median_views),
        "median_duration_min_long": round(statistics.median(
            [v["duration_sec"] for v in videos if not v["is_short_guess"]] or [0]) / 60, 1),
        "last_upload": dates[-1].isoformat() if dates else "",
    }
    return summary, videos


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--channels", required=True, help="File danh sách kênh (mỗi dòng một kênh)")
    parser.add_argument("--out", required=True, help="Thư mục ghi CSV")
    parser.add_argument("--max-videos", type=int, default=50, help="Số video gần nhất lấy mỗi kênh (mặc định 50)")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    load_dotenv(root / ".env")
    key = os.environ.get("YOUTUBE_API_KEY")
    if not key:
        raise SystemExit("Thiếu YOUTUBE_API_KEY (đặt trong .env hoặc biến môi trường).")

    refs = [line.strip() for line in Path(args.channels).read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.strip().startswith("#")]
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    today = dt.date.today().isoformat()

    summaries, all_videos = [], []
    for ref in refs:
        print(f"→ {ref}")
        summary, videos = audit_channel(ref, key, args.max_videos)
        if summary:
            summaries.append(summary)
            all_videos += videos

    write_csv(out / f"{today}-channels.csv", summaries)
    write_csv(out / f"{today}-videos.csv", sorted(all_videos, key=lambda v: -v["outlier_x"]))
    print(f"Xong: {len(summaries)} kênh, {len(all_videos)} video → {out}")


if __name__ == "__main__":
    main()
