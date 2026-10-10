---
name: yt-finance-script
description: Viết kịch bản video YouTube tài chính (dự án 01) từ một chủ đề đã chọn — hook, cấu trúc giữ chân, gợi ý hình ảnh từng đoạn, disclaimer. Dùng khi sản xuất video mới.
---

# yt-finance-script — Viết kịch bản

**Mức tự động hoá:** L0 (bản nháp — chỉnh lại sau lần chạy thật đầu tiên) · **Phạm vi:** dự án 01

## Input
- Chủ đề + tiêu đề đã chọn (từ `yt-finance-topic`), độ dài mục tiêu, ngôn ngữ.

## Các bước
1. Nghiên cứu nhanh: 3–5 nguồn uy tín, ghi số liệu + nguồn + ngày vào cuối kịch bản.
2. Dàn ý: Hook (0–15s, hứa hẹn rõ ràng khớp tiêu đề) → bối cảnh → 3–5 ý chính, mỗi ý có "open loop" → kết luận → CTA.
3. Viết lời đọc tự nhiên (câu ngắn, ~140–160 từ/phút tiếng Anh; ~180–200 từ/phút tiếng Việt `[CẦN XÁC MINH theo giọng đã chọn]`).
4. Cột gợi ý hình ảnh cho từng đoạn (stock / chart / AI image / text overlay).
5. Kiểm tra: không lời khuyên đầu tư cụ thể, có disclaimer, số liệu khớp nguồn, có góc nhìn riêng (không chỉ tóm tắt tin).
6. Lưu `content/scripts/YYYY-MM-DD-<slug>.md`.

## Output
- `content/scripts/YYYY-MM-DD-<slug>.md` gồm: tiêu đề, mô tả, tag, kịch bản 2 cột (lời đọc | hình ảnh), nguồn.

## Checklist chất lượng
- [ ] Hook khớp tiêu đề/thumbnail
- [ ] Mọi số liệu có nguồn
- [ ] Có disclaimer, không YMYL vi phạm
- [ ] Có ít nhất 1 phân tích/góc nhìn riêng

## Bài học
- (chưa có)

## Changelog
- 2026-10-10 — Tạo bản nháp.
