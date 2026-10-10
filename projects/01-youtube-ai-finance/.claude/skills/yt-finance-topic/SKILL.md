---
name: yt-finance-topic
description: Tìm và chấm điểm chủ đề video cho kênh YouTube AI tài chính (dự án 01). Dùng khi lên lịch nội dung tuần, tìm ý tưởng video mới, hoặc kiểm tra một chủ đề có đáng làm không.
---

# yt-finance-topic — Chọn chủ đề

**Mức tự động hoá:** L0 (bản nháp — chỉnh lại sau lần chạy thật đầu tiên) · **Phạm vi:** dự án 01

## Input
- Ngách con & ngôn ngữ đã chốt (README), số chủ đề cần (mặc định 10).

## Các bước
1. Gom nguồn: video top 30 ngày của kênh đối thủ (research/competitors), Google Trends, tin tài chính nổi bật,
   câu hỏi trong comment đối thủ, gợi ý tìm kiếm YouTube.
2. Lọc chủ đề "evergreen" (≥ 60%) và "thời sự" (≤ 40%).
3. Chấm điểm mỗi chủ đề (1–5): nhu cầu · bằng chứng outlier (video đối thủ vượt trung bình kênh ≥ 3x) ·
   độ dễ minh hoạ bằng AI/stock · khả năng làm khác biệt · rủi ro YMYL (ngược).
4. Viết 3 phương án tiêu đề + 1 ý tưởng thumbnail cho top chủ đề.
5. Lưu `content/ideas/YYYY-MM-DD-topics.md` (bảng điểm).

## Output
- `content/ideas/YYYY-MM-DD-topics.md`

## Hướng tự động hoá
- Cron hằng tuần: kéo video mới của danh sách đối thủ (YouTube Data API) → phát hiện outlier → Claude chấm điểm → gửi danh sách duyệt.

## Bài học
- (chưa có)

## Changelog
- 2026-10-10 — Tạo bản nháp.
