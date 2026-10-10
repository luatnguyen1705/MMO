---
name: tts-product-hunting
description: Săn sản phẩm gia dụng đáng làm affiliate trên TikTok Shop Việt Nam (dự án 02) — lọc theo doanh số, hoa hồng, xu hướng, độ dễ tìm video nguồn. Dùng khi cần danh sách sản phẩm mới cho tuần hoặc thay sản phẩm hết hot.
---

# tts-product-hunting — Săn sản phẩm

**Mức tự động hoá:** L0 (bản nháp — chỉnh lại sau lần chạy thật đầu tiên) · **Phạm vi:** dự án 02

## Input
- Ngách con, số sản phẩm cần (mặc định 20), khoảng giá ưu tiên.

## Các bước
1. Lấy danh sách ứng viên: Affiliate Center (lọc gia dụng, sắp theo doanh số/hoa hồng), tool data (sản phẩm tăng trưởng 7 ngày),
   video affiliate đang viral trong ngách.
2. Với mỗi sản phẩm ghi: tên, link, giá, % hoa hồng, đơn 7/30 ngày, số creator đang bán, rating shop, có mẫu miễn phí không.
3. Chấm điểm (1–5): nhu cầu/tăng trưởng · hoa hồng tuyệt đối/đơn · mức cạnh tranh creator (ngược) ·
   "demo được trong 3 giây" (hiệu ứng thị giác) · dễ tìm video nguồn TQ · uy tín shop.
4. Chọn top → lưu `research/market/YYYY-MM-DD-products.md`; sản phẩm được chọn chuyển sang `source-cn-video`.

## Hướng tự động hoá
- Export định kỳ từ tool data → script chấm điểm → danh sách duyệt mỗi sáng.

## Bài học
- (chưa có)

## Changelog
- 2026-10-10 — Tạo bản nháp.
