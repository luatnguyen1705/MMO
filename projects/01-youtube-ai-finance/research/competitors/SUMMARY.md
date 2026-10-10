# Audit đối thủ — YouTube AI tài chính — 2026-10-10

Nguồn: YouTube Data API v3, chạy `shared/automation/youtube_channel_audit.py` ngày **2026-10-10** trên 17 kênh
([channels.txt](channels.txt)), 50 video gần nhất mỗi kênh. Dữ liệu gốc:
[`data/processed/channel-audit/2026-10-10-channels.csv`](../../data/processed/channel-audit/2026-10-10-channels.csv) ·
[`2026-10-10-videos.csv`](../../data/processed/channel-audit/2026-10-10-videos.csv).

Lưu ý đọc số: "view trung vị" = trung vị view của video dài (> 3 phút) trong 50 video gần nhất; "đăng/tuần" tính trên
khoảng thời gian của 50 video đó. Video < 3 phút được coi là Shorts (ước đoán theo thời lượng). Kênh nào faceless hay có
người dẫn chưa được kiểm tra bằng mắt `[CẦN XÁC MINH 2026-10-10]`.

## 1. Bảng so sánh

### Việt Nam — faceless / kể chuyện
| Kênh | Tạo kênh | Sub | Tổng view | Video | Đăng/tuần | % Shorts | View trung vị (dài) | Độ dài TV | Đăng gần nhất |
|------|---------|-----|-----------|-------|-----------|----------|-----------------|-----------|---------------|
| **Lóng** `@longngghienn` | 2024-01 | 477k | 30,4M | 160 | 0,9 | 22% | **419.753** | 16,6' | 2026-10-08 |
| **Phía Sau Hào Quang** `@phiasauhaoquang` | 2024-04 | 55,9k | 17,0M | 77 | 1,0 | 0% | **132.244** | 11,7' | 2026-02-10 ⚠️ ngưng 8 tháng |
| CLB Tỷ Phú `@clbtyphu` | 2023-06 | 281k | 123,4M | 811 | 8,1 | 2% | 12.710 | 15,6' | 2026-10-09 |
| Thiết Phong - Thích Kinh Tế `@thietphong-thichkinhte` | 2025-04 | 13,2k | 5,7M | 375 | 2,9 | 0% | 7.741 | 12,7' | 2026-09-27 |
| Đế Chế Doanh Nhân `@dechedoanhnhan` | 2024-12 | 4,1k | 0,96M | 76 | 2,7 | 16% | 8.168 | 11,3' | 2025-04-28 ⚠️ ngưng |
| Góc Nhìn Kinh Tế `@gocnhinkinhte0403` | 2025-03 | 19,3k | 0,19M | 70 | 9,5 | 0% | 184 | 61' (live) | 2026-09-23 |
| Cú Thông Thái `@cuthongthai` | 2018-12 | 409k | 27,8M | 1.384 | 12,1 | 92% | 2.972 | 77' | 2026-10-10 |

### Việt Nam — có người dẫn / tổ chức truyền thông (đối chiếu)
| Kênh | Tạo kênh | Sub | Tổng view | Video | Đăng/tuần | % Shorts | View trung vị (dài) | Độ dài TV | Đăng gần nhất |
|------|---------|-----|-----------|-------|-----------|----------|-----------------|-----------|---------------|
| Thái Phạm `@thaiphamofficialvn` | 2018-07 | 1,01M | 128,1M | 2.615 | 2,2 | 4% | 42.672 | 36,8' | 2026-10-08 |
| Tài chính & Kinh doanh `@taichinhkinhdoanhtv` | 2015-05 | 537k | 68,2M | 2.320 | 9,2 | 46% | 30.632 | 30' | 2026-10-09 |
| Spiderum `@spiderum` | 2016-03 | 1,19M | 333,5M | 3.078 | 9,2 | 28% | 46.872 | 24,9' | 2026-06-30 ⚠️ |
| HieuTV `@hieu-tv` | 2009-01 | 844k | 72,0M | 184 | 1,1 | 0% | 204.376 | 17,1' | 2024-07-14 (đã dừng) |

### Quốc tế (mô hình tham khảo)
| Kênh | Sub | Video | Đăng/tuần | View trung vị (dài) | Độ dài TV | Đăng gần nhất |
|------|-----|-------|-----------|-----------------|-----------|---------------|
| How Money Works | 1,75M | 327 | 1,1 | 873.476 | 17,1' | 2026-09-29 |
| MagnatesMedia | 1,86M | 255 | 0,5 | 812.274 | 33,4' | 2025-09-12 |
| Economics Explained | 2,89M | 451 | 0,8 | 514.838 | 16,8' | 2026-10-05 |
| Modern MBA | 832k | 83 | 0,3 | 446.676 | 37,3' | 2026-09-20 |
| The Swedish Investor | 1,02M | 156 | 0,2 | 153.281 | 16,5' | 2025-06-27 |

Loại khỏi phân tích: **Kinh Tế Học Vui Vẻ** (đã chuyển sang nhạc, lệch ngách), **Kinh Tế World** (64,8k sub nhưng 0 video
công khai), **Web5ngay** (API không tìm ra kênh chính — `[CẦN XÁC MINH]` tra tay).

## 2. Nội dung top (hệ số outlier = view / trung vị kênh)

| Kênh | Video top | View | Outlier | Pattern |
|------|-----------|------|---------|---------|
| Lóng | Vì sao ngành F&B lỗ mà người ta vẫn làm? | 1,59M | 3,8× | "Vì sao + nghịch lý" |
| Lóng | Thời kì quần áo đắt tiền đã sụp đổ như thế nào? | 1,55M | 3,7× | sụp đổ của 1 ngành |
| Lóng | Tất cả những gì bạn cần biết về sự thoái trào của Labubu | 1,45M | 3,5× | trend nóng + "tất cả những gì bạn cần biết" |
| Lóng | Cafe Trung Nguyên đang đánh chiếm thị trường Trung Quốc thế nào? | 686k | 1,6× | doanh nghiệp Việt vươn ra ngoài |
| Phía Sau Hào Quang | Từ MC quyền lực nhất nước Mỹ đến kẻ bị đá ra khỏi showbiz | 1,17M | 8,8× | "Từ đỉnh cao → sụp đổ" |
| Phía Sau Hào Quang | Sự suy tàn của Cartoon Network / Ben 10 | 564k / 310k | 4,3× / 2,4× | thương hiệu suy tàn |
| Đế Chế Doanh Nhân | Khám phá 5 siêu dự án sẽ thay đổi Việt Nam trong 2025! | 182k | 22× | listicle hạ tầng VN + con số tỷ USD |
| Thiết Phong | Tin đồn: VinSpeed đặt 86 máy đào hầm TBM… / Vì sao VinSpeed dùng công nghệ Đức? | 63k / 41k | 8× / 5× | doanh nghiệp VN lớn (Vin), metro, Tesla vào VN |
| Thái Phạm | Vì sao vàng sẽ lên ngôi vương, đô la lung lay | 209k | 4,9× | vĩ mô: vàng – Fed – USD |
| Thái Phạm | Vì sao lãi suất Fed nếu có tăng thì vàng vẫn tăng? | 196k | 4,6× | Fed → vàng |
| Tài chính & Kinh doanh | Fed lần đầu tăng lãi suất sau 3 năm, Việt Nam có tăng lãi suất điều hành? | 129k | 4,2× | Fed → VN |
| CLB Tỷ Phú | Biển người cướp iPhone 18 & trả thù Huawei… | 214k | 16,9× | giật gân địa chính trị TQ (vùng rủi ro) |
| How Money Works | Why A National Debt Default Now Looks Genuinely Possible | 3,05M | 3,5× | vĩ mô + "khủng hoảng" |
| Modern MBA | Why Crumbl Cookies Can't Survive | 2,30M | 5,1× | mô hình kinh doanh 1 thương hiệu |

## 3. Pattern lặp lại
1. **Ít mà chất thắng nhiều mà loãng.** Hai kênh faceless VN mạnh nhất (Lóng 420k, Phía Sau Hào Quang 132k view trung vị)
   đăng **~1 video/tuần**, 12–20 phút. CLB Tỷ Phú đăng 8 video/tuần nhưng trung vị chỉ 12,7k; Góc Nhìn Kinh Tế
   9,5 video/tuần (livestream dài) chỉ 184 view. Kênh quốc tế top đều ≤ 1 video/tuần. Khớp với luật chống
   "inauthentic content" của dự án.
2. **Format A (kể chuyện doanh nghiệp/ngành) đã có cầu thật ở VN.** Lóng (kênh 2 năm 9 tháng tuổi, 477k sub) chứng minh
   "Vì sao X…/X sụp đổ thế nào/Tất cả những gì bạn cần biết về X" kéo được 1–1,5M view/video bằng tiếng Việt.
3. **Format B (vĩ mô: vàng – Fed – lãi suất – tỷ giá) có cầu nhưng VN chỉ có dạng người dẫn nói 25–50 phút**
   (Thái Phạm, Tài chính & Kinh doanh). Chưa thấy kênh faceless làm explainer vĩ mô gọn 10–15 phút có biểu đồ —
   khoảng trống trực tiếp cho định vị "Kinh tế Việt kể bằng dữ liệu".
4. **Chủ đề kéo view VN:** doanh nghiệp/tập đoàn VN (Vin, Trung Nguyên, Shark Bình), siêu dự án hạ tầng VN (metro,
   đường sắt tốc độ cao), vàng/Fed/USD, trend tiêu dùng (Labubu, F&B, thời trang).
5. **Tiêu đề:** câu hỏi "Vì sao…", nghịch lý, con số cụ thể ("84 tỷ USD", "86 cỗ máy"), cấu trúc "Từ … đến …",
   "trong 15 phút". Kênh VN dùng nhiều chữ IN HOA; kênh top (Lóng) thì không.
6. **Kênh tăng nhanh rồi chết vì không bền:** Đế Chế Doanh Nhân (video top 182k) và Phía Sau Hào Quang đều ngừng đăng;
   CLB Tỷ Phú trôi sang tin giật gân địa chính trị chưa kiểm chứng — đúng vùng rủi ro "tin sai sự thật" và
   chính sách YouTube mà dự án phải tránh.

## 4. Khoảng trống thị trường
- **Explainer vĩ mô faceless có dữ liệu, 10–15 phút** — đối thủ VN đều là talk dài 30–50 phút có người dẫn.
- **Ngách "siêu dự án / hạ tầng Việt Nam"** — từng ra 182k view ở kênh 4k sub, kênh đó đã bỏ; Thiết Phong làm nhưng
  thiên về tin đồn. Có thể làm bản có nguồn, có số liệu.
- **"Rise & fall" doanh nghiệp/thương hiệu** — Phía Sau Hào Quang (thiên giải trí) đã ngưng 8 tháng; Lóng chưa phủ hết
  doanh nghiệp Việt.
- **Doanh nghiệp Việt vươn ra thế giới** (Trung Nguyên, Green SM vào Hà Lan, Vin) — hợp nhánh kiều bào (EXP-003).

## 5. Ước tính doanh thu AdSense (minh hoạ, `[ƯỚC TÍNH]`)
Dùng RPM kế hoạch 0,3 / 0,6 / 1,2 USD (báo cáo nghiên cứu, mục RPM):
- Lóng: ~4 video × 420k view/tháng ≈ 1,7M view → **~500–2.000 USD/tháng** chỉ từ video mới.
- Phía Sau Hào Quang (khi còn đăng): ~4 × 132k ≈ 530k view → ~160–640 USD/tháng.
- CLB Tỷ Phú: ~35 × 12,7k ≈ 445k view → ~130–530 USD/tháng — sản lượng gấp 8 lần mà doanh thu ngang kênh ít video.
→ Mốc tham chiếu: một kênh faceless VN thành công ở format A cỡ vài trăm đến ~2.000 USD/tháng AdSense; phần lớn tiền
phải đến từ ngoài AdSense, đúng như báo cáo đã kết luận.

## 6. Giả thuyết test đề xuất
1. **EXP-A — Ít mà chất:** 1 video dài/tuần (12–16') đạt view trung vị cao hơn 3 video/tuần cùng tổng thời gian sản xuất.
   KPI: view 28 ngày/video, AVD. 8 tuần.
2. **EXP-B — Explainer vĩ mô ngắn:** video "Fed/vàng/tỷ giá → túi tiền người Việt" 10–12' có biểu đồ đạt CTR ≥ 5% và
   AVD ≥ 40% — tốt hơn trung bình kênh. 4 video.
3. **EXP-C — Siêu dự án VN có nguồn:** chủ đề hạ tầng/tập đoàn VN cho outlier ≥ 2× trung vị kênh mình. 3 video.
4. **EXP-D — Tiêu đề kiểu "Vì sao + nghịch lý" vs "Con số + IN HOA":** A/B thumbnail-title (Test & Compare của YouTube)
   trên 4 video.
5. Đo lại đối thủ hằng tháng (cùng script) để theo dõi kênh mới nổi và kênh chết.

## 7. Việc còn thiếu
- Xác minh faceless/AI hay người dẫn bằng cách xem 1–2 video mỗi kênh (proxy chặn youtube.com — người dùng xem tay).
- Tìm thêm ≥ 3 kênh VN **đang lên nhanh, ≤ 12 tháng tuổi** (hiện chỉ có Thiết Phong ~18 tháng) — dùng vidIQ/Nexlev hoặc
  YouTube search API theo từ khoá chủ đề top ở mục 2.
- Hồ sơ chi tiết từng kênh (mẫu trong skill `competitor-research`) cho 3 kênh quan trọng nhất: Lóng, Phía Sau Hào Quang,
  Thái Phạm.
