# YouTube AI tài chính

> Phase: **0 · Nghiên cứu (gần xong)** · Cập nhật: 2026-10-10 · Kênh: **tiếng Việt**

## Mục tiêu
- Xây kênh YouTube **tiếng Việt** chủ đề tài chính, sản xuất bằng AI (faceless), quy trình tự động kết hợp tool bên ngoài.
- Định vị đề xuất: **"Kinh tế Việt kể bằng dữ liệu"** (xem [báo cáo nghiên cứu](research/reports/Kênh%20YouTube%20AI%20tài%20chính%20Việt.md)).
- 6 tháng đầu là giai đoạn **xây tài sản + kiểm chứng format**, chưa phải giai đoạn kiếm tiền (RPM VN ~0,2–0,5 USD/1.000 view).
- Đạt điều kiện YPP, rồi mở thêm nguồn thu: affiliate (app đầu tư, sách, tool), sponsor, sản phẩm số.

## KPI (kịch bản cơ sở — ước tính, hiệu chỉnh sau 4–6 tuần)
| Chỉ số | Mục tiêu 3 tháng | Mục tiêu 6 tháng | Hiện tại |
|--------|------------------|------------------|----------|
| Video dài đã đăng | 45–50 | ~96 | 0 |
| View tích luỹ | ~34.000 | ~189.000 | 0 |
| Subscriber | 350–500 | 1.000–2.000 | 0 |
| Giờ xem | ~2.000 | ≥ 4.000 (YPP) | 0 |
| CTR / AVD | ≥ 4% / ≥ 35% | giữ hoặc tăng | — |
| Kiếm tiền | — | YPP duyệt + 1 affiliate tài chính đo được chuyển đổi | — |

Cảnh báo sớm: tháng 3 mà ≤ 10.000 view hoặc ≤ 100 sub → xem lại chủ đề/thumbnail trước khi tăng sản lượng.

## Lộ trình
- [x] Phase 0 — Chọn ngôn ngữ (VN), ngách con, format ([báo cáo](research/reports/Kênh%20YouTube%20AI%20tài%20chính%20Việt.md)) — [audit đối thủ](research/competitors/SUMMARY.md) xong 2026-10-10
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
| [youtube-channel-setup](../../.claude/skills/youtube-channel-setup/SKILL.md) (chung) | Setup tài khoản/AdSense/thuế chuẩn | L1 |
| [competitor-research](../../.claude/skills/competitor-research/SKILL.md) (chung) | Audit đối thủ bằng YouTube Data API | L2 |

## Link nhanh
- **Báo cáo nghiên cứu:** [research/reports/](research/reports/) · ghi chú gốc: [research/research_notes/](research/research_notes/)
- Kế hoạch nghiên cứu: [research/RESEARCH-PLAN.md](research/RESEARCH-PLAN.md)
- Test: [experiments/INDEX.md](experiments/INDEX.md)
- Nhật ký: [ops/JOURNAL.md](ops/JOURNAL.md) · Quyết định: [ops/DECISIONS.md](ops/DECISIONS.md)
