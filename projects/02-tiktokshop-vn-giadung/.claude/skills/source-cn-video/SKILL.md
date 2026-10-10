---
name: source-cn-video
description: Tìm video nguồn Trung Quốc (Douyin, Xiaohongshu, 1688, Taobao) cho một sản phẩm gia dụng và biên tập/Việt hoá thành video affiliate TikTok nguyên bản (dự án 02). Dùng khi sản xuất video cho sản phẩm đã chọn.
---

# source-cn-video — Từ video gốc TQ đến video Việt nguyên bản

**Mức tự động hoá:** L0 (bản nháp — chỉnh lại sau lần chạy thật đầu tiên) · **Phạm vi:** dự án 02

## Input
- Sản phẩm đã chọn (link TikTok Shop + ảnh), từ `tts-product-hunting`.

## Các bước
1. **Từ khoá tiếng Trung**: dịch tên + công dụng sản phẩm sang tiếng Trung (2–4 biến thể), tìm trên Douyin/Xiaohongshu;
   tìm bằng ảnh trên 1688/Taobao để lấy video người bán.
2. Chọn 2–5 clip nguồn có cảnh demo rõ; xác nhận **cùng mẫu** với sản phẩm gắn giỏ.
3. Tải bản không watermark → `data/raw/<san-pham>/`. Ghi link nguồn vào log.
4. **Biên tập lại** (bắt buộc đủ các ý): hook 1–3s mới (vấn đề/kết quả) · ghép từ nhiều clip, đổi thứ tự/nhịp ·
   xoá chữ/logo Trung · phụ đề + giọng Việt (lời do Claude viết theo insight người mua VN) · CTA giỏ hàng.
5. Viết caption + hashtag; đăng; gắn sản phẩm. Ghi vào `content/published/LOG.md` (kèm biến thể hook/format nếu đang test).

## Checklist chất lượng
- [ ] Không còn watermark/chữ Trung
- [ ] Sản phẩm trong video khớp sản phẩm gắn giỏ
- [ ] Hook mới, không giữ nguyên dựng gốc
- [ ] Không nói quá công dụng

## Hướng tự động hoá
- Script: dịch từ khoá → tìm & tải hàng loạt → template CapCut/ffmpeg cho phụ đề + TTS → người duyệt → đăng.

## Bài học
- (chưa có)

## Changelog
- 2026-10-10 — Tạo bản nháp.
