---
name: experiment
description: Thiết kế, theo dõi và đánh giá một test (kênh mới, format nội dung, sản phẩm, giờ đăng, hook, livestream…) cho dự án MMO. Dùng khi muốn kiểm chứng giả thuyết trước khi đầu tư/tự động hoá, hoặc khi test đến hạn cần kết luận.
---

# experiment — Test nhỏ, kết luận rõ

**Mức tự động hoá:** L1 · **Phạm vi:** dùng chung

## Các bước

### A. Thiết kế
1. Lấy số tiếp theo trong `projects/<p>/experiments/INDEX.md`.
2. Copy `shared/templates/EXPERIMENT.template.md` → `projects/<p>/experiments/EXP-<NNN>-<slug>.md`.
3. Điền: giả thuyết (dạng "Nếu… thì… vì…"), biến thay đổi (chỉ 1 biến chính), chỉ số chính + phụ,
   **ngưỡng thắng / thua**, cỡ mẫu tối thiểu (vd ≥ 20 video, ≥ 14 ngày), ngân sách tối đa, ngày kết thúc.
4. Thêm dòng vào INDEX.md với trạng thái `Đang chạy`.

### B. Theo dõi
- Ghi số liệu vào `projects/<p>/data/metrics/` (CSV) hoặc ngay trong file EXP theo ngày.
- Không đổi thiết kế giữa chừng; nếu buộc phải đổi → ghi lý do, coi như test mới.

### C. Kết luận
1. So với ngưỡng đã đặt → `Thắng` / `Thua` / `Không kết luận được`.
2. Ghi bài học + quyết định (nhân rộng / sửa & test lại / bỏ) → `ops/DECISIONS.md`.
3. Nếu thắng: quy trình đã dùng → `save-skill`; cân nhắc `automation-build`.
4. Cập nhật INDEX.md.

## Nguyên tắc
- Test rẻ và nhanh trước, đẹp sau. Kết luận dựa trên số, không dựa trên cảm giác.
- Trên nền tảng thuật toán (TikTok/Shorts/Reels), một nội dung không nói lên gì — đánh giá theo lô.

## Bài học
- (chưa có)

## Changelog
- 2026-10-10 — Tạo skill.
