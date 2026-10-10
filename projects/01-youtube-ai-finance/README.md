# YouTube AI tài chính

> Phase: **0 · Nghiên cứu** · Cập nhật: 2026-10-10

## Mục tiêu
- Xây kênh YouTube chủ đề tài chính, sản xuất bằng AI (faceless), quy trình tự động kết hợp tool bên ngoài.
- Đạt điều kiện YPP, rồi mở thêm nguồn thu: affiliate (app đầu tư, sách, tool), sponsor, sản phẩm số.

## KPI (đề xuất — chốt sau Phase 0)
| Chỉ số | Mục tiêu 30 ngày | Mục tiêu 90 ngày | Hiện tại |
|--------|------------------|------------------|----------|
| Số video đã đăng | 12 | 40 | 0 |
| Subscriber | 300 | 1.000 | 0 |
| Giờ xem (watch hours) | 500 | 4.000 | 0 |
| CTR thumbnail | ≥ 4% | ≥ 6% | — |
| Giờ công / video | ≤ 3h | ≤ 1h | — |

## Lộ trình
- [ ] Phase 0 — Chọn ngôn ngữ/thị trường, ngách con, đối thủ, format ([RESEARCH-PLAN](research/RESEARCH-PLAN.md))
- [ ] Phase 1 — Test thủ công 10–15 video, 2–3 format
- [ ] Phase 2 — Chuẩn hoá: kịch bản → voice → dựng → thumbnail → upload thành skill
- [ ] Phase 3 — Pipeline bán tự động (người duyệt kịch bản + thumbnail)
- [ ] Phase 4 — Tự động & nhân rộng (thêm kênh/ngôn ngữ)

## Pipeline mục tiêu
```
Ý tưởng (trend, tin tức, từ khoá) → Kịch bản (Claude) → Kiểm tra số liệu & pháp lý
→ Giọng đọc (ElevenLabs…) → Hình ảnh (stock, chart, AI image) → Dựng (CapCut/ffmpeg/Remotion)
→ Thumbnail + tiêu đề (Canva) → Upload & lên lịch (YouTube API) → Theo dõi số liệu → Cập nhật skill
```

## Skill của dự án
| Skill | Mục đích | Mức |
|-------|----------|-----|
| [yt-finance-topic](.claude/skills/yt-finance-topic/SKILL.md) | Tìm & chấm điểm chủ đề video | L0 (nháp) |
| [yt-finance-script](.claude/skills/yt-finance-script/SKILL.md) | Viết kịch bản video tài chính | L0 (nháp) |

## Link nhanh
- Kế hoạch nghiên cứu: [research/RESEARCH-PLAN.md](research/RESEARCH-PLAN.md)
- Test: [experiments/INDEX.md](experiments/INDEX.md)
- Nhật ký: [ops/JOURNAL.md](ops/JOURNAL.md) · Quyết định: [ops/DECISIONS.md](ops/DECISIONS.md)
