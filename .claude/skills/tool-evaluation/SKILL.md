---
name: tool-evaluation
description: Đánh giá một tool/phần mềm/SaaS bên ngoài (tool AI tạo video, TTS, tool MMO, extension, dịch vụ tự động hoá…) trước khi mua hoặc cài cho dự án MMO — cách hoạt động, chi phí thật, rủi ro tài khoản/bảo mật/chính sách, độ phù hợp. Dùng khi người dùng gửi link tool và hỏi có nên dùng không.
---

# tool-evaluation — Thẩm định tool trước khi mua/cài

**Mức tự động hoá:** L1 · **Phạm vi:** dùng chung

## Các bước
1. **Nhận diện**: ai làm (cá nhân/công ty), dạng app/web/extension, mã nguồn mở/đóng, có ký số (code-signed) không, tần suất cập nhật.
   Trang bán bị chặn → tìm GitHub/release/changelog của dev, video demo, nhóm cộng đồng; đọc mã nguồn công khai nếu có.
2. **Cách kết nối dịch vụ** (quan trọng nhất):
   - API chính thức + key của mình → rủi ro thấp.
   - Tự động hoá trình duyệt bằng **cookie/phiên đăng nhập** tài khoản thường, xoay nhiều tài khoản, lách captcha/anti-bot
     → vi phạm ToS, rủi ro khoá tài khoản; **không bao giờ dùng tài khoản sở hữu kênh/AdSense/tài khoản chính**.
   - Tài khoản dùng chung/bán lại → rủi ro cao nhất.
3. **Chi phí thật** = giá tool + giá dịch vụ AI bên dưới (gói, credit, giới hạn) + thời gian sửa khi tool hỏng. Quy đổi ra chi phí/1 video thành phẩm.
4. **Đầu ra**: chất lượng, độ dài clip, watermark (kể cả vô hình như SynthID), ngôn ngữ/giọng Việt, có ráp được video hoàn chỉnh không.
5. **Rủi ro**: ToS nền tảng; bảo mật (app đóng/không ký giữ cookie = nguy cơ chiếm tài khoản); uy tín người bán, chính sách hoàn tiền;
   chính sách kiếm tiền của nền tảng đăng (nội dung hàng loạt).
6. **Độ phù hợp** với định vị & ngân sách của dự án (đọc `projects/<p>/CLAUDE.md`); so 2–4 phương án thay thế.
7. **Kết luận**: Dùng / Thử có kiểm soát (EXP có trần chi phí, tài khoản + máy/VM riêng) / Không dùng.
8. Lưu ghi chú `shared/knowledge/tools/research-notes/YYYY-MM-DD-<tool>.md`, thêm dòng `shared/knowledge/tools/REGISTRY.md`, ghi JOURNAL dự án liên quan.

## Checklist an toàn khi quyết định thử
- [ ] Tài khoản Google/AI riêng, không liên quan kênh/AdSense
- [ ] Máy ảo hoặc máy/trình duyệt riêng; tải bản gốc từ nguồn chính chủ (không bản crack/fork)
- [ ] Trần chi phí + thời hạn thử; huỷ được trong thời gian hoàn tiền

## Bài học
- 2026-10-10 — G-Labs Studio: trang bán bị chặn, nhưng GitHub của dev có README/changelog/mã extension → đủ để biết tool dùng cookie
  + tạo token reCAPTCHA để lách anti-bot. Luôn tìm mã nguồn/tài liệu của dev, đừng chỉ dựa vào trang bán.
- 2026-10-10 — Tool "hàng loạt" thường tối ưu số lượng clip, không tối ưu giá trị biên tập — đối chiếu với chính sách inauthentic content trước khi mua.

## Changelog
- 2026-10-10 — Tạo skill từ lần đánh giá G-Labs Studio.
