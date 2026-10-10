# YouTube AI tài chính — bối cảnh cho Claude

Luật chung ở `/CLAUDE.md`. File này bổ sung luật riêng của dự án.

## Bối cảnh
- Kênh faceless **tiếng Việt** (chốt 2026-10-10), sản xuất bằng AI + tool bên ngoài.
- Định vị đề xuất (chờ chủ kênh duyệt): **"Kinh tế Việt kể bằng dữ liệu"** — video essay không lộ mặt.
  - Format A (~60%): kể chuyện doanh nghiệp 10–15 phút ("Vì sao X sụp đổ", "X kiếm tiền thế nào").
  - Format B (~40%): explainer vĩ mô có biểu đồ thật 8–12 phút (vàng, lãi suất, tỷ giá, Fed→VN); nhánh "nhìn từ ngoài" cho kiều bào.
  - Shorts cắt từ video dài. Lời hứa kênh: "không khuyến nghị mã, không bán khoá học làm giàu, mọi con số có nguồn".
- Nghiên cứu nền: `research/reports/Kênh YouTube AI tài chính Việt.md` (2026-10-10).
- Kiến thức nền tảng: `shared/knowledge/platforms/youtube.md`.

## Phạm vi dữ liệu
Chỉ đọc/ghi trong thư mục này. Kiến thức YouTube chung → `shared/knowledge/platforms/youtube.md`.

## Luật riêng
- **Tài chính là chủ đề YMYL**: không đưa lời khuyên mua/bán cụ thể, không hứa lợi nhuận, luôn có disclaimer
  "chỉ mang tính giáo dục". Số liệu phải có nguồn và ngày — kiểm tra lại trước khi xuất bản.
- **Chống "inauthentic content"**: YouTube không kiếm tiền cho nội dung hàng loạt/lặp lại. Mỗi video phải có giá trị
  riêng: góc nhìn, phân tích, cấu trúc kể chuyện — không chỉ là AI đọc lại tin tức. Bật nhãn "altered/synthetic content"
  khi dùng hình ảnh/giọng AI trông như thật.
- **Không dùng AI avatar/persona "chuyên gia" trông như người thật** — từ 7/2026 YouTube không kiếm tiền cho AI persona
  bàn chủ đề tài chính. Nếu cần "người dẫn": nhân vật hoạt hình rõ là minh hoạ, hoặc giọng clone của chính chủ kênh.
- **Tránh làm trục chính**: bản tin thị trường hằng ngày, slideshow + giọng đọc (đúng mẫu "inauthentic").
- **Luật VN**: không khuyến nghị mua/bán/nắm giữ mã chứng khoán cụ thể (tư vấn chứng khoán cần giấy phép — UBCKNN);
  không affiliate sàn crypto nước ngoài/dự án token (NQ 05/2025, NĐ 284/2026); video có affiliate/tài trợ phải công bố
  bằng lời + chữ ở đầu video và tại đoạn nhắc sản phẩm, bật "Includes paid promotion" (Luật Quảng cáo 75/2025, Điều 15a).
- **Fact-check số liệu là bắt buộc** (LLM có thể bịa số; tin sai sự thật có chế tài hành chính & hình sự).
- Nhạc chỉ từ YouTube Audio Library/nguồn license rõ; không phát lại clip VTV/báo đài (Content ID).
- Ưu tiên phong cách minh hoạ/biểu đồ thay vì hình AI chân thực (tránh nhãn synthetic hiện trên video tài chính).
- Chủ kênh giữ 3 điểm chạm mỗi video: chọn góc nhìn · duyệt số liệu · bấm đăng.
- Giữ bước người duyệt kịch bản + thumbnail trước khi đăng, kể cả khi đã tự động hoá.

## Tool bên ngoài (dự kiến)
| Tool | Dùng cho | Trạng thái |
|------|----------|-----------|
| Claude | Nghiên cứu, kịch bản, tiêu đề | Sẵn sàng |
| Canva (đã kết nối MCP) | Thumbnail, hình minh hoạ | Đã kết nối |
| Google Drive (đã kết nối MCP) | Lưu asset, chia sẻ | Đã kết nối |
| ElevenLabs / TTS khác | Giọng đọc | Chưa setup |
| CapCut / ffmpeg / Remotion | Dựng video | Chưa chọn |
| vidIQ / TubeBuddy / Nexlev | Nghiên cứu từ khoá, đối thủ | Chưa setup |
| YouTube Data API | Audit đối thủ (`shared/automation/youtube_channel_audit.py`), số liệu, upload | Script sẵn sàng — cần API key |
| n8n / Make | Điều phối pipeline | Chưa chọn |
