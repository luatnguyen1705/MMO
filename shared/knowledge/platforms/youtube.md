# YouTube — kiến thức nền tảng

> Cập nhật lần cuối: 2026-10-10 (nghiên cứu dự án 01). Dùng bởi: 01, 03. Chi tiết + nguồn: `projects/01-youtube-ai-finance/research/reports/`.

## Kiếm tiền (YPP)
- Tier 1: 500 sub + 3 video công khai/90 ngày + 3.000 giờ xem/12 tháng hoặc 3M view Shorts/90 ngày → chỉ fan funding/Shopping. VN có áp dụng `[CẦN XÁC MINH]`.
- Tier 2 (chia sẻ quảng cáo): 1.000 sub + 4.000 giờ xem/12 tháng, hoặc 10M view Shorts/90 ngày.
  Một nguồn duy nhất nói từ 1/2/2027 tăng lên 8.000 giờ / 20M Shorts `[CẦN XÁC MINH]`.
- RPM người xem VN ước tính ~0,2–0,5 USD/1.000 view (Dynamoi ~0,22); tài chính tiếng Anh ~10–25 USD. Shorts VN ~0,01–0,05 (suy luận).
- Google (9/2026): > 50% thời gian xem kênh do người Việt sản xuất đến từ nước ngoài → kiều bào là đòn bẩy RPM.
- YouTube Shopping affiliate có ở VN từ 11/2024 (Shopee).

## Chính sách AI / inauthentic content
- 15/7/2025: "repetitious" → **"inauthentic content"**; ví dụ bị nêu: chuỗi truyện narration khác nhau sơ sài, slideshow cùng kiểu narration. AI không bị cấm nếu có giá trị thật.
- 1/2026: CEO đặt "quản lý AI slop" làm ưu tiên; ~16–18 kênh AI slop (> 4 tỷ view) bị xoá theo chính sách **spam & deceptive practices** → tiêu đề/thumbnail lừa dối có thể dẫn tới xoá kênh.
- 7/2026: không kiếm tiền cho (1) nội dung chung chung/template, (2) nội dung gây khó chịu, (3) **AI persona/"chuyên gia AI" bàn chủ đề nhạy cảm (tài chính, sức khoẻ, pháp lý)**. "Lặp lại" được đánh giá theo cảm nhận người xem khi xem vài video liên tiếp.
- Nhãn **altered/synthetic** (từ 3/2024): chỉ bắt buộc khi nội dung trông thật/có thể nhầm là người, nơi, sự kiện thật; dùng AI viết script/phụ đề không cần khai. Chủ đề nhạy cảm (gồm tài chính) → nhãn hiện ngay trên video.

## Công cụ & API
- Multi-language audio mở cho mọi creator (9/2025); auto-dubbing AI 27 ngôn ngữ (2/2026) — tiếng Việt có hay không `[CẦN XÁC MINH]`.
- Test & Compare: tối đa 3 thumbnail, chọn theo watch-time share; test tiêu đề từ 7/2025.
- Data API: 10.000 unit/ngày mặc định; `videos.insert` 1.600 unit (có nguồn nói giảm còn ~100 từ 12/2025 `[CẦN XÁC MINH]`).
  Project API chưa qua audit có thể chỉ upload được private `[CẦN XÁC MINH]`.
- googleapis.com truy cập được từ môi trường cloud của Claude (cần API key); youtube.com/Social Blade/Playboard bị chặn.

## Link affiliate
- Link trong mô tả video dài bấm được. Link trong mô tả Shorts không bấm được (từ 2023) `[CẦN XÁC MINH]`.

## Bảo mật
- Mối đe doạ chính: email "mời tài trợ" kèm file mã độc ăn cắp cookie (vượt 2FA). Xem skill `youtube-channel-setup`.
