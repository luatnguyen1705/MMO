---
name: automation-build
description: Nâng một skill/quy trình thủ công lên bán tự động hoặc tự động (script, n8n/Make workflow, cron, API). Dùng khi một quy trình đã được test thắng và lặp lại ổn định, hoặc khi người dùng yêu cầu tự động hoá một bước.
---

# automation-build — Từ skill thành cỗ máy

**Mức tự động hoá:** L1 · **Phạm vi:** dùng chung

## Điều kiện trước khi làm
- Quy trình đã có skill ở L1 và đã chạy thủ công thành công ≥ 3 lần.
- Có test chứng minh đầu ra của quy trình có giá trị (không tự động hoá thứ chưa hiệu quả).

## Các bước
1. Vẽ pipeline: `trigger → input → các bước → output → nơi lưu → thông báo`. Đánh dấu bước nào cần người duyệt
   (human-in-the-loop) — mặc định giữ bước duyệt trước khi **đăng công khai**.
2. Chọn công cụ:
   - Logic/AI/xử lý file → Python trong `projects/<p>/automation/pipelines/` (dùng lại `shared/automation/lib/`).
   - Kết nối nhiều SaaS, lịch chạy → n8n/Make; export workflow JSON vào `automation/pipelines/`.
   - Lịch chạy → cron / GitHub Actions / n8n schedule.
3. Cấu hình ở `automation/config/*.yaml` (không chứa secret); secret ở `.env`.
4. Mỗi pipeline có: README ngắn (chạy thế nào), log ra `data/` , xử lý lỗi + retry, chế độ `--dry-run`.
5. Chạy thử dry-run → chạy thật quy mô nhỏ → theo dõi 1 tuần → mới tăng quy mô.
6. Cập nhật skill gốc: mức tự động hoá mới (L2/L3), cách chạy pipeline, Changelog.
7. Thành phần dùng được cho dự án khác → tách vào `shared/automation/lib/`.

## Nguyên tắc an toàn
- Giới hạn tốc độ đăng, tránh hành vi giống bot/spam; tôn trọng ToS và rate limit của API.
- Không lưu token/cookie trong repo. Không chạy trên tài khoản chính khi đang thử nghiệm.

## Bài học
- (chưa có)

## Changelog
- 2026-10-10 — Tạo skill.
