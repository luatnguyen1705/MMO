# YouTube AI tài chính — bối cảnh cho Claude

Luật chung ở `/CLAUDE.md`. File này bổ sung luật riêng của dự án.

## Bối cảnh
- Kênh faceless, nội dung tài chính (cá nhân, đầu tư, kinh tế vĩ mô…), sản xuất bằng AI + tool bên ngoài.
- Ngôn ngữ/thị trường chưa chốt — xem RESEARCH-PLAN câu 1 (VN CPM thấp nhưng dễ làm; EN CPM cao nhưng cạnh tranh mạnh).
- Kiến thức nền tảng: `shared/knowledge/platforms/youtube.md`.

## Phạm vi dữ liệu
Chỉ đọc/ghi trong thư mục này. Kiến thức YouTube chung → `shared/knowledge/platforms/youtube.md`.

## Luật riêng
- **Tài chính là chủ đề YMYL**: không đưa lời khuyên mua/bán cụ thể, không hứa lợi nhuận, luôn có disclaimer
  "chỉ mang tính giáo dục". Số liệu phải có nguồn và ngày — kiểm tra lại trước khi xuất bản.
- **Chống "inauthentic content"**: YouTube không kiếm tiền cho nội dung hàng loạt/lặp lại. Mỗi video phải có giá trị
  riêng: góc nhìn, phân tích, cấu trúc kể chuyện — không chỉ là AI đọc lại tin tức. Bật nhãn "altered/synthetic content"
  khi dùng hình ảnh/giọng AI trông như thật.
- Không dùng nhạc/hình có bản quyền khi không có giấy phép.
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
| YouTube Data API | Upload, lấy số liệu | Chưa setup |
| n8n / Make | Điều phối pipeline | Chưa chọn |
