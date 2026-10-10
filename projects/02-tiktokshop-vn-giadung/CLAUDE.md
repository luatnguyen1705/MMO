# TikTok Shop VN · Gia dụng — bối cảnh cho Claude

Luật chung ở `/CLAUDE.md`. File này bổ sung luật riêng của dự án.

## Bối cảnh
- Thị trường Việt Nam, nội dung tiếng Việt. Affiliate TikTok Shop (không tự bán hàng).
- Ngành gia dụng: đồ bếp, dọn dẹp, lưu trữ, tiện ích nhà cửa — giá thấp/vừa, dễ demo, mua theo cảm hứng.
- Kiến thức nền tảng: `shared/knowledge/platforms/tiktok.md`.

## Phạm vi dữ liệu
Chỉ đọc/ghi trong thư mục này. Video tải về để ở `data/raw/` (không commit); chỉ commit metadata trong log.

## Luật riêng
- **Không reup nguyên trạng.** TikTok hạn chế phân phối/không cho gắn giỏ với nội dung không nguyên bản
  và có thể xử phạt tài khoản. Mỗi video phải được biên tập đáng kể: hook mới, cắt ghép lại, giọng/phụ đề Việt,
  thêm cảnh hoặc góc nhìn riêng; xoá watermark/logo/chữ Trung của nguồn. Ghi lại link nguồn trong log.
- Sản phẩm trong video phải **đúng** sản phẩm được gắn giỏ (cùng mẫu, cùng tính năng) — không quảng cáo sai.
- Không nói quá công dụng; tránh ngành hàng hạn chế. Tuân thủ quy tắc cộng đồng & chính sách TikTok Shop VN.
- Livestream phải có người thật/tương tác thật — không dùng live phát lại video giả live `[CẦN XÁC MINH chính sách hiện hành]`.

## Tool bên ngoài (dự kiến)
| Tool | Dùng cho | Trạng thái |
|------|----------|-----------|
| TikTok Shop Affiliate Center / Creator Center | Tìm sản phẩm, lấy link, xin mẫu, xem hoa hồng | Chưa setup |
| Kalodata / FastMoss / tool data VN | Số liệu sản phẩm & video bán chạy | Chưa chọn |
| Douyin / Xiaohongshu / 1688 / Taobao | Nguồn video | Chưa setup |
| Tool tải video không watermark | Tải nguồn | Chưa chọn |
| CapCut | Biên tập, phụ đề, giọng AI tiếng Việt | Chưa setup |
| Claude | Dịch/viết lời Việt, hook, caption | Sẵn sàng |
