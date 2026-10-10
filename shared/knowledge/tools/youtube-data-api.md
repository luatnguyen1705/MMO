# YouTube Data API v3 — tạo API key

> Cập nhật: 2026-10-10. Dùng bởi: 01, 03 (`shared/automation/youtube_channel_audit.py`).

1. Vào https://console.cloud.google.com, đăng nhập bằng Google account **cá nhân/công việc** (không cần dùng tài khoản kênh).
2. Thanh trên cùng → chọn project → **New Project** → đặt tên (vd `mmo-hq`) → Create. Không cần bật thanh toán.
3. Menu → **APIs & Services → Library** → tìm "YouTube Data API v3" → **Enable**.
4. **APIs & Services → Credentials → Create credentials → API key** → copy key.
5. Bấm vào key vừa tạo → **API restrictions → Restrict key → chỉ chọn YouTube Data API v3** → Save
   (key bị lộ cũng chỉ dùng được cho API này).
6. Lưu key: biến môi trường `YOUTUBE_API_KEY` — trong `.env` (máy local, đã gitignore) hoặc phần secrets/biến môi trường
   của cloud environment Claude Code (session mới mới nhận). **Không dán key vào chat, không commit.**

- Miễn phí, hạn mức 10.000 unit/ngày (audit 1 kênh ~3–5 unit). Key chỉ đọc dữ liệu công khai — không truy cập được kênh của bạn.
- Upload video tự động sau này cần **OAuth client** (không phải API key) — làm ở bước automation.
