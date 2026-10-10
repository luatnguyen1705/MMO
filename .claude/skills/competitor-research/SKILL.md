---
name: competitor-research
description: Nghiên cứu đối thủ (kênh YouTube, tài khoản TikTok, trang Pinterest/Facebook, website affiliate…) cho một dự án MMO — thu thập số liệu, mổ xẻ format nội dung, cách kiếm tiền, điểm yếu để khai thác. Dùng khi bắt đầu dự án, khi tìm ngách, hoặc định kỳ cập nhật đối thủ.
---

# competitor-research — Mổ xẻ đối thủ

**Mức tự động hoá:** L1 · **Phạm vi:** dùng chung (mỗi dự án có thể có biến thể riêng)

## Input
- Dự án, nền tảng, từ khoá ngách, số lượng đối thủ cần phân tích (mặc định 10).

## Các bước
1. **Tìm danh sách**: tìm kiếm theo từ khoá ngách trên nền tảng + công cụ ngoài (vd Social Blade, vidIQ/Nexlev cho YouTube;
   Kalodata/FastMoss/TikTok Shop Creator Center cho TikTok Shop; PinInspector/Tailwind cho Pinterest). Chọn 3 nhóm:
   *top lớn* (chuẩn mực), *đang lên nhanh* (≤ 12 tháng tuổi, tăng mạnh — đáng học nhất), *nhỏ nhưng ra đơn/ra view đều*.
2. **Ghi hồ sơ từng đối thủ** vào `projects/<p>/research/competitors/<nen-tang>-<ten>.md` theo mẫu bên dưới.
3. **Phân tích nội dung top**: 10 nội dung tốt nhất + 5 nội dung gần nhất của mỗi đối thủ — hook 3 giây đầu, độ dài,
   cấu trúc, CTA, tần suất đăng, giờ đăng, cách gắn link/sản phẩm.
4. **Tổng hợp** vào `projects/<p>/research/competitors/SUMMARY.md`: bảng so sánh, pattern lặp lại, khoảng trống thị trường,
   format có thể "sao chép có cải tiến", ước tính doanh thu.
5. **Rút insight** → ghi vào `research/insights/` (mỗi insight: quan sát · bằng chứng · hàm ý hành động · giả thuyết test).
6. Chạy `save-skill` nếu phát hiện cách nghiên cứu tốt hơn cho nền tảng này.

## Mẫu hồ sơ đối thủ
```markdown
# <Tên> — <nền tảng> — cập nhật YYYY-MM-DD
- Link:
- Tuổi kênh / followers / tổng view:
- Tần suất đăng / độ dài nội dung:
- Ngách & đối tượng:
- Format chủ đạo (mặt người? AI voice? faceless? live?):
- Nội dung top (link + số liệu + vì sao hiệu quả):
- Kiếm tiền bằng gì (ads, affiliate, sản phẩm số, sponsor) + ước tính:
- Tool/quy trình đoán họ dùng:
- Điểm mạnh:
- Điểm yếu / khoảng trống:
- Học được gì cho dự án mình:
```

## Checklist
- [ ] Mọi số liệu có ngày thu thập
- [ ] Có ít nhất 3 kênh "đang lên nhanh"
- [ ] SUMMARY.md kết thúc bằng danh sách giả thuyết test cụ thể

## Bài học
- (chưa có)

## Changelog
- 2026-10-10 — Tạo skill.
