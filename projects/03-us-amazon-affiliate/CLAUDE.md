# Social US · Amazon Affiliate — bối cảnh cho Claude

Luật chung ở `/CLAUDE.md`. File này bổ sung luật riêng của dự án.

## Bối cảnh
- Đối tượng: người mua ở Mỹ. Nội dung tiếng Anh tự nhiên (giọng Mỹ).
- Chủ dự án ở Việt Nam: mọi phương án phải đánh giá rào cản tài khoản, IP, xác minh, thanh toán, thuế (W-8BEN).
- Kiến thức nền tảng: `shared/knowledge/platforms/amazon-associates.md`, `pinterest.md`, `youtube.md`, `tiktok.md`.

## Phạm vi dữ liệu
Chỉ đọc/ghi trong thư mục này.

## Luật riêng
- Mọi nội dung có link phải qua skill `amazon-compliance-check` trước khi đăng (hoặc trước khi pipeline đăng tự động).
- Luôn có disclosure rõ ràng (FTC + Amazon). Không đặt link Amazon trong email/PDF/ebook/offline.
- Không hiển thị giá cố định trừ khi lấy qua API chính thức và có thời điểm cập nhật.
- Không dùng ảnh sản phẩm Amazon ngoài cách Amazon cho phép; ưu tiên ảnh/video tự tạo hoặc có giấy phép.
- Không spam: giới hạn tần suất đăng theo từng nền tảng; không mua bán tài khoản, không thao túng tương tác.
- Đăng hàng loạt ≠ nội dung kém: mỗi bài phải có giá trị thật (so sánh, giải quyết vấn đề, gợi ý theo nhu cầu).

## Tool bên ngoài (dự kiến)
| Tool | Dùng cho | Trạng thái |
|------|----------|-----------|
| Amazon Associates (US) | Link affiliate, báo cáo | Chưa đăng ký |
| Amazon Creators API / PA-API | Dữ liệu sản phẩm, giá | Cần đủ doanh số để mở `[CẦN XÁC MINH]` |
| Canva (đã kết nối MCP) | Pin, ảnh, video ngắn | Đã kết nối |
| Claude | Ý tưởng, copy, so sánh sản phẩm | Sẵn sàng |
| Tailwind / Buffer / Publer / API nền tảng | Lên lịch đăng | Chưa chọn |
| n8n / Make | Điều phối pipeline | Chưa chọn |
