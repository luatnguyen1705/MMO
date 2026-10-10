---
name: weekly-review
description: Review định kỳ (tuần) cho một hoặc tất cả dự án MMO — tổng hợp số liệu, tiến độ test, việc tuần tới, skill nào cần cập nhật/nâng mức tự động hoá. Dùng khi người dùng hỏi "tuần này thế nào", "review", hoặc theo lịch.
---

# weekly-review — Nhìn lại và điều chỉnh

**Mức tự động hoá:** L1 → mục tiêu L3 (chạy tự động sáng thứ Hai) · **Phạm vi:** dùng chung

## Các bước
1. Với mỗi dự án đang chạy (`projects/README.md`):
   - Đọc `ops/JOURNAL.md` 7 ngày gần nhất, `experiments/INDEX.md`, `data/metrics/`.
   - Tính KPI so với mục tiêu trong README dự án (view, follower, click, đơn, doanh thu, chi phí, giờ công).
2. Ghi `projects/<p>/ops/reviews/YYYY-Www.md`: số liệu · điều gì hiệu quả · điều gì không · test đến hạn · 3 ưu tiên tuần tới.
3. Rà skill: skill nào dùng nhiều nhất → ứng viên tự động hoá; skill nào lỗi thời → cập nhật.
4. Nếu review tất cả dự án: ghi tổng hợp `ops-reviews/YYYY-Www.md` ở gốc (phân bổ thời gian/tiền giữa các dự án).
5. Cập nhật phase trong `projects/README.md` nếu có thay đổi.

## Bài học
- (chưa có)

## Changelog
- 2026-10-10 — Tạo skill.
