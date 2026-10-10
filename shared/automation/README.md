# Automation dùng chung

Quy ước (chi tiết ở skill `automation-build`):

- `lib/` — module Python dùng chung (client LLM, TTS, upload, log metrics…). Không chứa logic đặc thù dự án.
- Code đặc thù đặt ở `projects/<p>/automation/pipelines/`; cấu hình ở `projects/<p>/automation/config/`.
- Dự án import từ `shared/automation/lib`, không bao giờ ngược lại.
- Secret qua biến môi trường (`.env`), xem `.env.example`.
- Mọi pipeline: có `--dry-run`, log kết quả vào `projects/<p>/data/`, có giữ bước người duyệt trước khi đăng công khai.

Hiện chưa có module nào — sẽ thêm khi một skill đầu tiên được nâng lên L2.
