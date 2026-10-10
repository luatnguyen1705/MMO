---
name: amazon-compliance-check
description: Kiểm tra một nội dung/lô nội dung có link Amazon affiliate trước khi đăng — disclosure FTC & Amazon, vị trí đặt link, giá, hình ảnh, khẳng định sản phẩm, quy định riêng của nền tảng (dự án 03). Dùng trước mọi lần đăng thủ công và là bước bắt buộc trong pipeline tự động.
---

# amazon-compliance-check — Không để mất tài khoản Associates

**Mức tự động hoá:** L1 (checklist) → mục tiêu L2 (Claude chấm tự động trong pipeline) · **Phạm vi:** dự án 03

## Checklist
**Disclosure**
- [ ] Có câu công bố rõ ràng, gần link/đầu nội dung (vd "As an Amazon Associate I earn from qualifying purchases." /
      "#ad · affiliate link"). Không giấu sau "xem thêm".
- [ ] Dùng tính năng gắn nhãn affiliate/paid partnership của nền tảng nếu có.

**Link**
- [ ] Link chứa đúng tracking ID; link rút gọn dùng amzn.to hoặc cho thấy rõ là đi tới Amazon `[CẦN XÁC MINH quy định link rút gọn hiện hành]`.
- [ ] Không đặt link trong email, PDF, ebook, ứng dụng nhắn tin riêng hay bất kỳ dạng offline nào.
- [ ] Không tự bấm/nhờ người khác mua qua link của mình; không khuyến khích "click để ủng hộ".

**Nội dung**
- [ ] Không ghi giá cố định (hoặc lấy từ API kèm thời điểm cập nhật).
- [ ] Không dùng logo/thương hiệu Amazon gây hiểu nhầm là Amazon chính thức.
- [ ] Hình ảnh: tự tạo / có giấy phép / lấy theo cách Amazon cho phép (API).
- [ ] Không khẳng định sai về sản phẩm, không review giả, không nói "đã dùng" nếu chưa dùng.

**Nền tảng**
- [ ] Tuân thủ quy định affiliate của nền tảng đăng (xem `shared/knowledge/platforms/<nen-tang>.md`).
- [ ] Tần suất đăng trong giới hạn an toàn đã ghi ở knowledge.

## Output
- Đạt / Không đạt + danh sách lỗi cần sửa. Trong pipeline: lô không đạt bị chặn đăng.

## Bài học
- (chưa có)

## Changelog
- 2026-10-10 — Tạo skill.
