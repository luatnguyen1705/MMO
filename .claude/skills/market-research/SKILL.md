---
name: market-research
description: Nghiên cứu thị trường/nền tảng/xu hướng để quyết định đánh vào đâu — so sánh nền tảng, đánh giá ngách, nhu cầu, cạnh tranh, rào cản (chính sách, vị trí địa lý, thanh toán). Dùng trước khi chọn hướng cho dự án hoặc khi cần so sánh lựa chọn.
---

# market-research — Chọn sân chơi

**Mức tự động hoá:** L1 · **Phạm vi:** dùng chung

## Input
- Câu hỏi nghiên cứu (lấy từ `projects/<p>/research/RESEARCH-PLAN.md`), ràng buộc của chủ dự án
  (đang ở Việt Nam, ngân sách, thời gian/ngày, kỹ năng).

## Các bước
1. Viết rõ **câu hỏi quyết định** (vd "Nền tảng nào cho Amazon affiliate dễ ra traffic nhất khi vận hành từ VN?").
2. Liệt kê **phương án** và **tiêu chí chấm điểm**. Bộ tiêu chí mặc định (thang 1–5, có trọng số):
   - Tiềm năng traffic / nhu cầu
   - Mức cạnh tranh (ngược)
   - Độ dễ sản xuất & khả năng tự động hoá
   - Rào cản vận hành từ VN (tài khoản, IP, thanh toán, xác minh)
   - Rủi ro chính sách (ban, demonetize, chặn link)
   - Thời gian tới đồng tiền đầu tiên
   - Biên lợi nhuận / hoa hồng
3. Thu thập bằng chứng: nguồn chính thức (trang chính sách, help center), công cụ dữ liệu, ví dụ đối thủ thực tế,
   cộng đồng (Reddit, nhóm FB MMO). Ghi nguồn + ngày cho từng khẳng định; chưa chắc → `[CẦN XÁC MINH]`.
4. Chấm điểm → ma trận quyết định trong `projects/<p>/research/market/YYYY-MM-DD-<chu-de>.md`.
5. Kết luận: 1–2 phương án chọn để test, lý do, và những gì sẽ làm thay đổi kết luận.
6. Chuyển kết luận thành đề xuất test (dùng skill `experiment`).
7. Kiến thức chính sách/nền tảng đúng cho nhiều dự án → cập nhật `shared/knowledge/platforms/<nen-tang>.md`.

## Checklist
- [ ] Mọi khẳng định quan trọng có nguồn + ngày
- [ ] Ràng buộc "vận hành từ Việt Nam" được đánh giá riêng
- [ ] Có kết luận hành động được, không chỉ mô tả

## Bài học
- (chưa có)

## Changelog
- 2026-10-10 — Tạo skill.
