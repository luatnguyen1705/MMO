---
name: youtube-channel-setup
description: Thiết lập kênh YouTube kiếm tiền chuẩn ngay từ đầu cho người ở Việt Nam — Google account, Brand Account/quyền kênh, bảo mật chống chiếm kênh, AdSense, W-8BEN, nhận tiền, sổ thuế VN. Dùng khi mở kênh YouTube mới cho bất kỳ dự án nào, khi bật kiếm tiền, hoặc khi rà lại bảo mật/quyền sở hữu kênh.
---

# youtube-channel-setup — Dựng kênh đúng một lần

**Mức tự động hoá:** L1 (checklist) · **Phạm vi:** dùng chung (dự án 01, 03, kênh YouTube sau này)
**Nguồn:** `projects/01-youtube-ai-finance/research/reports/Kênh YouTube AI tài chính Việt.md` (2026-10-10). Không phải tư vấn pháp lý/thuế.

## A. Ngày 1 — Tài khoản & quyền sở hữu
- [ ] Tạo **Google account riêng** cho kênh, tên thật khớp CCCD, số khôi phục = SIM VN chính chủ (NĐ 147/2024 yêu cầu xác thực SĐT VN).
- [ ] Tạo kênh dạng **Brand Account / channel permissions** (để sau này chuyển kênh sang công ty được).
- [ ] Thêm **Owner dự phòng** = tài khoản thứ hai của chính chủ. Không xoá tài khoản primary owner (xoá là mất kênh).
- [ ] Người làm thuê/tool: chỉ cấp **Editor (Limited)** (không xem doanh thu). Không bao giờ cấp Owner.
- [ ] Quốc gia kênh = **Việt Nam** (trung thực, khớp AdSense & thuế; RPM phụ thuộc nơi người xem, không phụ thuộc cài đặt này).
- [ ] Xác minh điện thoại để mở tính năng nâng cao.
- [ ] Ghi cấu trúc tài khoản (không ghi mật khẩu) vào `projects/<p>/ops/DECISIONS.md`.

## B. Bảo mật chống chiếm kênh
- [ ] Passkey hoặc khoá bảo mật vật lý; bật 2FA.
- [ ] Máy/trình duyệt riêng cho tài khoản kênh.
- [ ] **Không mở file .exe/.scr/.zip từ email "mời tài trợ"** — mã độc ăn cắp cookie phiên, vượt được 2FA.
- [ ] Rà danh sách thiết bị đăng nhập hằng tháng.
- [ ] Tool tự động hoá chỉ dùng OAuth qua **project Google Cloud của chính mình**; không đưa cookie/mật khẩu cho SaaS lạ.

## C. Khi đủ điều kiện kiếm tiền
- [ ] Chỉ **một** tài khoản AdSense; tên/địa chỉ khớp CCCD và tài khoản ngân hàng; địa chỉ nhận được thư (PIN gửi bưu điện).
- [ ] Phương thức nhận tiền: chuyển khoản (wire/SWIFT) về ngân hàng VN (Western Union đã ngừng đăng ký mới từ 8/2020). Kiểm tra phí nhận SWIFT của ngân hàng.
- [ ] Nộp **W-8BEN** ngay: cá nhân, Việt Nam, không claim hiệp định (hiệp định Việt–Mỹ chưa hiệu lực) → khấu trừ 30% phần doanh thu từ người xem Mỹ. Không nộp → có thể bị khấu trừ tới 24% doanh thu toàn cầu.
- [ ] Nội dung tài trợ/affiliate: bật "Includes paid promotion" + công bố bằng lời và chữ (Luật Quảng cáo 75/2025).

## D. Sổ thuế VN (từ tháng đầu có tiền)
- [ ] File theo dõi theo tháng: doanh thu gộp · phần Mỹ khấu trừ · thực nhận · tỷ giá ngày nhận. Lưu payment receipt AdSense + sao kê.
- [ ] Thông báo doanh thu (Mẫu 01/TKN-CNKD, trước 31/1 năm sau) dù dưới ngưỡng `[CẦN XÁC MINH]`.
- [ ] Ngưỡng chịu thuế 2026: NĐ 141/2026 nêu 1 tỷ đ/năm; Luật 109/2025 nêu 500 triệu — `[CẦN XÁC MINH]`, xem `shared/knowledge/vietnam-legal-tax.md`.
- [ ] Doanh thu tiến gần ngưỡng hoặc ký hợp đồng tài trợ → hỏi kế toán; cân nhắc tính thuế theo thu nhập hoặc lập công ty TNHH và chuyển kênh + AdSense sang pháp nhân.

## Bài học
- (chưa có — cập nhật sau lần setup kênh thật đầu tiên)

## Changelog
- 2026-10-10 — Tạo skill từ nghiên cứu dự án 01.
