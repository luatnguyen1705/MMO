# Kể chuyện kinh tế Việt, đừng giả chuyên gia

*Báo cáo nghiên cứu: dự án 01 – kênh YouTube AI tài chính tiếng Việt. Ngày tổng hợp: 2026-10-10. Đây không phải tư vấn pháp lý hay thuế.*

Hướng đi đáng làm nhất cho một người mới ở Việt Nam muốn kênh tài chính sản xuất gần 100% bằng AI là một **kênh video essay "kể chuyện kinh tế và doanh nghiệp Việt bằng dữ liệu"**. Kênh không lộ mặt, có một giọng kể nhất quán và biểu đồ tự dựng, cắt Shorts từ video dài, và **không bao giờ khuyến nghị mua bán mã cụ thể**. Hai hướng còn lại nên bỏ. Thứ nhất là "bản tin thị trường hằng ngày", vì đây là kiểu dễ tự động hoá nhất nhưng cũng đúng mẫu "lặp lại" mà YouTube cắt kiếm tiền. Thứ hai là "AI avatar chuyên gia đầu tư", vì từ tháng 7/2026 YouTube nêu đích danh nội dung dùng AI persona bàn chủ đề tài chính là không được kiếm tiền ([TechCrunch](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/)). Về tiền, cần kỳ vọng thực tế. RPM quảng cáo cho người xem Việt Nam chỉ khoảng **0,2–0,5 USD/1.000 view**, thấp hơn 20–50 lần so với kênh tài chính tiếng Anh ([Dynamoi](https://dynamoi.com/data/youtube-adsense-rpm/vn); [Accesstrade](https://accesstrade.vn/1000-view-youtube-duoc-bao-nhieu-tien-o-viet-nam/)). Một kênh mới thường mất khoảng 5 tháng để có 1.000 sub ([Kapwing](https://kapwing.com/resources/we-grew-a-faceless-youtube-channel-to-1000-subscribers)). Vì vậy 6 tháng đầu là giai đoạn **xây tài sản và kiểm chứng format**, chưa phải giai đoạn kiếm tiền. Rủi ro lớn nhất không đến từ YouTube mà đến từ luật Việt Nam: tư vấn chứng khoán không phép, quảng bá crypto ngoài khuôn khổ thí điểm, và Luật Quảng cáo sửa đổi có hiệu lực từ 1/1/2026 đặt trách nhiệm trực tiếp lên người có ảnh hưởng. Những rủi ro này kiểm soát được nếu dựng khung tuân thủ ngay từ ngày đầu. Có một giới hạn cần nói thẳng: môi trường nghiên cứu không truy cập được YouTube, Social Blade và Playboard (proxy chặn). Vì vậy số liệu từng kênh trong báo cáo chỉ là số thứ cấp, gắn nhãn `[CẦN XÁC MINH]`, và việc lấp khoảng trống này là bước đầu tiên của kế hoạch 30 ngày.

## Số liệu kênh trong báo cáo là thứ cấp, cần một lượt kiểm tra trực tiếp

Mọi con số về subscriber và lượt xem của từng kênh dưới đây đều lấy từ đoạn trích kết quả tìm kiếm, báo chí, hoặc tracker bên thứ ba (vidIQ, HypeAuditor, youtubers.me). Trong phiên nghiên cứu, youtube.com, socialblade.com, playboard.co, noxinfluencer.com và support.google.com đều trả lỗi DNS hoặc bị proxy chặn (CONNECT 403). Nhiều số liệu mang mốc 2024 hoặc không rõ ngày chụp. Báo cáo không bịa thêm số nào. Chỗ nào nguồn không ghi rõ thì được gắn `[CẦN XÁC MINH 2026-10-10]`.

Có hai cách lấp khoảng trống, mất khoảng 1–2 giờ:

- **Cách nhanh, làm tay.** Mở Playboard, lọc Việt Nam theo các danh mục Education/News/People với từ khoá "kinh tế", "tài chính", "tỷ phú", "doanh nghiệp", rồi lấy các kênh tạo trong 2024–2026 đang tăng sub nhanh. Sau đó lấy từ Social Blade các số sub, tổng view, view 30 ngày và ngày tạo kênh. Trên trang kênh, sắp xếp theo "Phổ biến" để lấy top 10 video. Nghe 30 giây mỗi kênh để phân loại giọng (AI hay người thật) và loại hình ảnh.
- **Cách bền, tự động hoá được.** Tạo một API key YouTube Data API v3 và gọi `channels.list` (1 unit) cùng `search.list` với `regionCode=VN` và `relevanceLanguage=vi` (100 unit). Hạn mức mặc định là 10.000 unit/ngày, dư sức cho một lượt quét đối thủ ([ChannelCrawler](https://channelcrawler.com/insights/youtube-api-daily-limit-quotas-costs-and-how-to-scale-beyond-10000-units-channelcrawler); [Phyllo](https://www.getphyllo.com/post/is-the-youtube-api-free-in-2026-quota-limits-costs-when-to-pay)).

Cách thứ hai nên được đóng gói thành script L2 trong `automation/pipelines/`, vì việc theo dõi đối thủ sẽ lặp lại hằng tháng.

## Format thắng là format khó lặp lại: kể chuyện có dữ liệu, không phải slideshow

YouTube không cấm AI. Thứ bị loại khỏi YPP là nội dung **"inauthentic"**, tức sản xuất hàng loạt và chỉ khác nhau ở bề mặt. Khi đổi tên chính sách "repetitious" thành "inauthentic" ngày 15/7/2025, YouTube nêu đích danh hai ví dụ: kênh đăng nhiều câu chuyện có narration chỉ khác nhau sơ sài, và kênh có nhiều slideshow với cùng một kiểu narration ([PPC Land](https://ppc.land/youtube-clarifies-inauthentic-content-policy-changes/); [TechCrunch](https://techcrunch.com/2025/07/09/youtube-prepares-crackdown-on-mass-produced-and-repetitive-videos-as-concern-over-ai-slop-grows)). Đợt làm rõ tháng 7/2026 còn định nghĩa "lặp lại" theo cảm nhận người xem: nếu xem vài video liên tiếp của cùng một kênh mà thấy trùng lặp thì bị tính là lặp, kể cả video hướng dẫn không nguyên bản ([Metricool](https://metricool.com/youtube-ai-content-rules-monetization/)). Từ đó rút ra quy luật trung tâm khi chọn format: **format càng dễ tự động hoá thì càng dễ bị coi là lặp**. Lợi thế bền vững nằm ở chỗ tự động hoá phần sản xuất (giọng, dựng, phụ đề), còn **mỗi tập vẫn giữ nghiên cứu và góc nhìn riêng**.

Bảng dưới tổng hợp các format faceless phổ biến. Phần đánh giá giữ chân người xem là định tính, vì chưa có số liệu retention cho kênh tài chính tiếng Việt.

| Format | Độ dài | Mức tự động hoá | Giữ chân | Rủi ro "inauthentic" / nhãn AI | Kết luận cho dự án |
|---|---|---|---|---|---|
| Documentary/storytelling (doanh nghiệp thăng trầm, tỷ phú, bong bóng) | 10–25 phút | Cao (L2–L3) nếu người duyệt script | Cao | Thấp–TB nếu mỗi tập nghiên cứu riêng | **Format chính** |
| Explainer có biểu đồ dữ liệu thật (lãi suất, vàng, tỷ giá) | 8–15 phút | Cao | TB–cao | Thấp–TB | **Format chính thứ hai** |
| Whiteboard/hoạt hình 2D | 5–12 phút | TB–cao | TB | Thấp (hoạt hình không cần khai AI) | Phong cách hình ảnh nên dùng |
| AI avatar dẫn chương trình | 3–10 phút | Rất cao | Thấp–TB | **Cao từ 7/2026** với chủ đề tài chính | Tránh |
| Bản tin thị trường hằng ngày | 3–8 phút | Rất cao | TB | **Cao**, cùng khung và chỉ đổi số | Tránh làm trục chính |
| Slideshow + giọng đọc | 5–15 phút | Rất cao | Thấp | **Cao nhất**, bị nêu đích danh | Tránh |
| Listicle ("7 sai lầm tài chính tuổi 25") | 8–12 phút | Cao | TB | TB | Thỉnh thoảng |
| Podcast 2 giọng AI | 15–40 phút | Rất cao | TB | TB | Để sau |
| Shorts cắt từ video dài | 15–60 giây | Rất cao | Đo bằng KPI khác | TB–cao nếu làm hàng loạt | Kênh kéo sub, không phải nguồn tiền |

Về công cụ, pipeline faceless phổ biến năm 2026 gồm: LLM viết script, TTS lồng tiếng, công cụ render theo template, sau đó upload. Pipeline này thường được điều phối bằng n8n ([Creatomate](https://creatomate.com/blog/how-to-auto-generate-faceless-shorts-with-chatgpt-and-n8n); [OutlierKit](https://outlierkit.com/resources/n8n-faceless-youtube-template/)). Với một kênh tiếng Việt, khâu quyết định chất lượng là **giọng đọc**, và có ba nhóm lựa chọn:

- **ElevenLabs.** Nhấn nhá cảm xúc tốt và clone được giọng chủ kênh. Đổi lại, khi đọc tiếng Việt dài vẫn có lỗi ngắt chữ và nhịp ([Viettablet](https://www.viettablet.com/giong-doc-ai); [FPT Shop](https://fptshop.com.vn/tin-tuc/danh-gia/elevenlabs-ai-158486)). Giá: Starter khoảng $5–6, Creator $22, Pro $99 mỗi tháng. Các nguồn có mâu thuẫn về giá ([BigVU](https://bigvu.tv/blog/elevenlabs-pricing-2026-plans-credits-commercial-rights-api-costs/)).
- **Nhà cung cấp Việt (Vbee, FPT.AI, Viettel AI).** Xử lý tiếng Việt và giọng vùng miền tốt, có API, nhưng không công khai bảng giá ([Google Cloud – Vbee](https://cloud.google.com/customers/vbee?hl=ja); [FPT.AI docs](https://docs.fpt.ai/docs/en/speech/documentation/text-to-speech)).
- **Cloud lớn.** Google Chirp 3 HD miễn phí 1 triệu ký tự đầu, sau đó $30/1 triệu ký tự ([Google Cloud](https://cloud.google.com/text-to-speech/pricing/?authuser=2)). Một kênh đăng 16 video dài và 45 Shorts mỗi tháng chỉ cần khoảng 200.000 ký tự, nên gần như miễn phí, *nếu* có giọng vi-VN đạt chuẩn `[CẦN XÁC MINH 2026-10]`.

Vì không có benchmark khách quan nào về chất lượng giọng tiếng Việt, việc chọn giọng phải qua một **bài nghe mù**. Dùng cùng một đoạn script 2–3 phút có nhiều số, ký hiệu % và tên riêng tiếng Anh ("Fed", "S&P 500", "VN-Index"), cho chạy qua 4–6 giọng rồi chấm điểm mà không biết giọng nào của hãng nào.

Hình ảnh là khâu tốn tiền nhất nếu dùng sai chỗ. Stock footage có giá rẻ: Envato khoảng $16,5/tháng, Storyblocks $20–40/tháng. Tuy vậy, Envato bị than phiền nhiều về việc nhạc có license vẫn dính Content ID claim ([GTM Directory](https://thegtmdirectory.com/compare/envato-elements-vs-storyblocks); [Checkthat.ai](https://checkthat.ai/brands/envato/reviews)). Video AI hiện có giá khoảng **$0,04–0,15/giây** ở các bản Fast/Turbo và khoảng **$0,40/giây** với Veo 3.1 Standard có âm thanh ([InVideo](https://invideo.io/blog/ai-video-model-pricing); [Apiframe](https://apiframe.ai/blog/ai-video-api-pricing-2026)). Mức giá này đủ rẻ để làm b-roll điểm nhấn, nhưng phủ cả video 10 phút thì tốn khoảng $380–1.150/tháng. Avatar HeyGen tốn khoảng $3–6/phút ([DIYAI](https://diyai.io/ai-tools/video-generation/heygen-pricing/)), vừa đắt vừa vướng chính sách. Phương án tốt nhất là **biểu đồ tự dựng bằng code**: Remotion miễn phí cho nhóm ≤3 người, kể cả dùng thương mại ([Remotion](https://remotion.dev/docs/license)). Biểu đồ dữ liệu thật vừa tăng giá trị cho người xem vừa là bằng chứng "không phải nội dung template".

Ở khâu dựng, CapCut không có API công khai nên không đưa lên được mức L3. Shotstack tính $0,07–0,40/phút render ([Wireflow](https://www.wireflow.ai/blog/shotstack-pricing)). JSON2Video tính $49,95/tháng cho 200 phút ([JSON2Video](https://json2video.com/how-to/creatomate-alternative/)). Tự viết ffmpeg/MoviePy/Remotion thì gần như $0 tiền license. Cộng các đơn giá lại, chi phí ước tính cho khoảng 16 video dài và 45 Shorts mỗi tháng như sau: **Budget khoảng $20–60**, **Standard khoảng $150–300**, **Premium khoảng $600–2.300**. Ở các tier cao, phần chi phí tăng thêm chủ yếu đến từ video AI và avatar, không phải TTS hay LLM. Giá LLM, ảnh AI và n8n chưa được tra trong phiên nên còn `[CẦN XÁC MINH 2026-10]`.

Trước khi nghĩ đến upload tự động có hai điểm kỹ thuật cần biết. Thứ nhất, chi phí quota của `videos.insert` có thể đã giảm từ 1.600 xuống khoảng 100 unit (12/2025). Nhiều nguồn nói vậy nhưng chưa đối chiếu được với trang của Google ([OutlierKit](https://outlierkit.com/resources/youtube-api-quota/)). Thứ hai, theo hiểu biết trước đây, các project API chưa qua audit sẽ chỉ upload được video ở chế độ private `[CẦN XÁC MINH 2026-10]`. Cả hai điểm đều không cản trở giai đoạn đầu, vì upload qua Studio kèm một bước người duyệt vẫn là quy trình đúng cho kênh tài chính.

## Kênh Việt lớn bán niềm tin vào một con người, khoảng trống nằm ở video essay

Nhìn vào các kênh tài chính và kinh tế tiếng Việt đã thành danh, có một điểm chung: **gần như tất cả dựa vào uy tín cá nhân và kiếm tiền chủ yếu ngoài AdSense**.

- **Web5ngay** có khoảng 4,26 triệu sub theo tracker, không rõ ngày cập nhật ([youtubers.me](https://us.youtubers.me/web5ngay/youtuber-stats)) `[CẦN XÁC MINH 2026-10-10]`.
- **Thái Phạm** có khoảng 1,01 triệu sub, ngày chụp không rõ. Chủ kênh dựa vào gần 20 năm kinh nghiệm chứng khoán ([YouTube](https://www.youtube.com/channel/UCDJIGO_3ycJAKLPv7Yh396A/featured)).
- **HieuTV** là ví dụ có số liệu rõ nhất. Kênh có khoảng 850.000 sub và 66,5 triệu view (7/2024), bán khóa học đầu tư giá khoảng 250 USD cho ước tính 27.000 người mua ([CafeF](https://cafef.vn/chu-kenh-youtube-hieutv-xin-loi-hoc-vien-vi-ban-khoa-hoc-dau-tu-tai-chinh-250-usd-nhung-bi-phan-nan-chua-tuong-xung-voi-gia-188240730111437679.chn)). Cũng chính kênh này dính lùm xùm "lùa gà" năm 2024, chủ kênh phải xin lỗi ([24hMoney](https://24hmoney.vn/news/giua-luc-bi-hoc-vien-to-lua-ga-hieu-tv-thong-bao-chia-tay-podcast-nhung-khong-quen-keu-goi-nguoi-xem-mua-khoa-hoc-dau-tu-moi-c26a2340555.html)).

Bài học từ HieuTV có hai mặt. Doanh thu khóa học có thể gấp nhiều lần AdSense. Nhưng thị trường cũng đang có một **khoảng trống niềm tin**, và một kênh minh bạch nguồn, không bán khóa học "làm giàu" có thể chiếm lấy khoảng trống đó. Sự hoài nghi này đã có từ trước, khi báo chí phản ánh tình trạng "chuyên gia chứng khoán trên YouTube, TikTok nhiều quá, người dân tin sái cổ" ([Dân trí](https://dantri.com.vn/kinh-doanh/chuyen-gia-chung-khoan-tren-youtube-tiktok-nhieu-qua-nguoi-dan-tin-sai-co-20231025101642417.htm)).

AI không tái tạo được kinh nghiệm 20 năm hay câu chuyện tự do tài chính của một con người. Thứ AI tái tạo được là **cấu trúc giải thích, nghiên cứu, minh hoạ số liệu và kể chuyện**. Spiderum chứng minh rằng format video essay (kịch bản viết kỹ, giọng đọc diễn cảm, hình minh hoạ) có thể đạt khoảng 240.000 sub ở kênh chính mà không cần ngôi sao. Đây là số đã cũ, và nếu cộng mọi kênh của Spiderum thì hơn 500.000 ([Spiderum](https://spiderum.com/bai-dang/Minh-noi-gi-khi-noi-ve-kenh-Spiderum-Youtube-rc6)). Kênh **Tài chính & Kinh doanh** có khoảng 536.000 sub, 65,6 triệu view, tăng khoảng 1.000 sub/30 ngày ([vidIQ](https://vidiq.com/youtube-stats/channel/@taichinhkinhdoanhtv/)). Con số này cho thấy ngách tài chính cá nhân tiếng Việt vẫn có cầu nhưng tăng trưởng của các kênh lâu năm đã chậm lại.

Nhóm kênh faceless hoặc AI tiếng Việt chỉ xác định được ở mức "ứng viên", vì không lấy được số liệu sống. Có thể chia thành ba cụm:

- **Câu chuyện tỷ phú và đế chế.** Gồm CLB Tỷ Phú (metadata hiện "277000" nhưng không rõ là chỉ số gì) `[CẦN XÁC MINH 2026-10-10]` và Đế Chế Doanh Nhân, kênh có làm Shorts ([CLB Tỷ Phú](https://www.youtube.com/channel/UCC3Sh45d3WA3a4zxP-8JPiw); [Đế Chế Doanh Nhân](https://www.youtube.com/@dechedoanhnhan/shorts)).
- **Kinh tế vĩ mô và tổng hợp tin.** Gồm Kinh Tế World, Thiết Phong – Thích Kinh Tế, Góc Nhìn Kinh Tế ([Góc Nhìn Kinh Tế](https://www.youtube.com/channel/UCfSakFTitm3zqEAUyO4VCzw)).
- **Kiến thức dạng hoạt hình.** Gồm Lóng ([YBOX](https://ybox.vn/ky-nang/toptip-top-3-kenh-youtube-hay-ve-kinh-te-ma-ban-nen-xem-qua-6757d5b867a1fc51a1694f47)) và Spiderum.

Các tiêu đề quan sát được lộ ra ba công thức lặp lại:

- **"Vì sao X sụp đổ?"**, ví dụ "Vì Sao Taxi Mai Linh sụp đổ? Bài Học Cay Đắng Cho Doanh Nghiệp Việt" ([video](https://www.youtube.com/watch?v=0N7ehy0MuXk)).
- **"[N] bài học kinh doanh ĐẮT GIÁ"**, có viết hoa từ khoá cảm xúc ([video](https://www.youtube.com/watch?v=fdq1tpjxNyw)).
- **"[N] dự báo kinh tế thế giới [năm]"** ([video](https://www.youtube.com/watch?v=80uzTboySPA)).

Chưa có dữ liệu về thumbnail, độ dài hay tần suất đăng của bất kỳ kênh nào. Cũng chưa xác nhận được kênh nào dùng giọng AI.

Các kênh quốc tế làm mẫu đều có chung một đặc điểm: **kịch bản gốc và bản sắc riêng**, không phải sản xuất hàng loạt.

| Kênh | Số liệu (nguồn, mốc) | Format | Bài học chuyển sang tiếng Việt |
|---|---|---|---|
| Alux.com | ~5,1M sub ([HypeAuditor](https://hypeauditor.com/youtube/UCNjPtOCvMrKY5eLwr_-7eUg/), 9/2026) | List lifestyle + tài chính, giọng đọc + stock | Đại chúng nhưng dễ trượt thành template |
| Economics Explained | ~2,87M sub, ~367M view ([vidIQ](https://vidiq.com/youtube-stats/channel/@economicsexplained/)) | Vĩ mô, câu hỏi gây tò mò | "Vì sao Việt Nam/Thái Lan…?", vàng, tỷ giá |
| Magnates Media | ~1,86–1,9M sub, 255 video ([vidIQ](https://vidiq.com/youtube-stats/channel/@magnatesmedia/)) | Phim tài liệu kinh doanh | Thăng trầm doanh nghiệp Việt và thương hiệu toàn cầu ở VN |
| The Swedish Investor | ~1,01M sub, 156 video ([Social Blade](https://socialblade.com/youtube/channel/UCAeAB8ABXGoGMbXuYPmiu2A), 3/2026) | Tóm tắt sách đầu tư bằng hoạt hình vẽ tay | Sách đầu tư phổ biến ở VN, kèm ví dụ bối cảnh VN |
| Modern MBA | ~822K sub ([Social Blade](https://socialblade.com/youtube/handle/modernmba), 8/2026) | "How X makes money" | Doanh nghiệp Việt kiếm tiền thế nào |

Magnates Media và Economics Explained đang chững lại: vidIQ ghi +0 sub/30 ngày, nhưng con số này có thể là lỗi dữ liệu. Ngách vẫn có cầu nhưng không còn "dễ". Lợi thế cho người vào sau vì vậy **không nằm ở format mới mà ở thị trường ngôn ngữ chưa bão hoà**. Các tuyên bố kiểu "kênh whiteboard tài chính mới đạt 20.000–30.000 sub trong 2 tháng" đều không nêu tên kênh ([Vozo](https://vozo.ai/blogs/profitable-faceless-youtube-niches)). Thu nhập "trên 10.000 USD/tháng" của MagnatesMedia mà các trang bán khóa học VN hay dẫn cũng là số tự báo cáo ([HVMO](https://hocvienmarketingonline.com/lam-youtube-view-ngoai-ngach-kinh-te-bang-ai)). Một thống kê khác nói chỉ khoảng 3% kênh faceless thành công ([Frameloop](https://frameloop.ai/blog/faceless-youtube-statistics-2026)). Thị trường "dạy làm kênh AI" ở Việt Nam đang rất sôi động ([NOHI](https://nohiedu.com/chien-luoc-ai-content-kiem-tien-youtube-2025-khoa-hoc-youtube-vu-van-thang/); [MKT Software](https://mktsoftware.vn/xay-kenh-youtube-ai)), nghĩa là sẽ có nhiều kênh AI tiếng Việt làm theo cùng một khuôn. Lý do đó càng cho thấy phải khác biệt bằng nghiên cứu.

Từ các kênh trên có thể nhặt ra những khoảng trống đáng thử, tất cả đều là giả thuyết cần Playboard xác nhận:

- **Tài chính cá nhân faceless chất lượng cao.** Các kênh lớn trong mảng này (Hieu Nguyen, Giang Ơi, Thai Pham, Vietsuccess) đều lộ mặt ([misskick](https://misskick.vn/top-7-kenh-youtube-ve-tai-chinh-kinh-doanh-dang-xem-nhat-viet-nam)).
- **Lịch sử tiền tệ và kinh tế Việt Nam kể bằng biểu đồ.** Chưa thấy kênh nào chuyên làm.
- **Giải thích vĩ mô bằng dữ liệu động.** Yêu Kinh Tế chủ yếu là livestream chuyên gia ([Yêu Kinh Tế](https://www.youtube.com/@YeuKinhTe)).
- **Tâm lý tiền bạc.**

## Thị trường đủ lớn, nhưng RPM Việt buộc phải nghĩ ngoài AdSense

Về phía cầu, tín hiệu rất tốt:

- YouTube tiếp cận khoảng **62,3 triệu người dùng ở Việt Nam** (1/2025) ([DataReportal](https://datareportal.com/essential-youtube-stats?rd=1)).
- Theo khảo sát Google/Kantar công bố tháng 9/2026, 93% người dùng Internet xem YouTube mỗi ngày và 82% nói có khả năng mua sản phẩm do creator họ tin giới thiệu ([CafeF](https://cafef.vn/93-nguoi-dung-internet-viet-nam-xem-youtube-moi-ngay-188260917145859624.chn)). Đây là số Google tự công bố.
- Số tài khoản chứng khoán cá nhân trong nước đạt **khoảng 11,8 triệu cuối 2025**, tăng gần 2,6 triệu chỉ trong năm 2025 ([Thời báo Tài chính](https://thoibaotaichinhvietnam.vn/so-luong-tai-khoan-chung-khoan-cua-nha-dau-tu-trong-nuoc-da-tang-gan-26-trieu-tai-khoan-trong-nam-2025-190337.html)). Mỗi năm có hàng triệu người mới cần kiến thức nhập môn.
- Vàng là chủ đề nóng nhất 2025: SJC tăng khoảng 88% lên 154,2–156,2 triệu đồng/lượng ([Vietstock](https://vietstock.vn/2025/12/buc-tranh-thi-truong-vang-nam-2025-gia-lap-dinh-chinh-sach-siet-chat-759-1381911.htm)).
- Nâng hạng thị trường là chủ đề đang nóng ([VTV](https://vtv.vn/vsdc-tiep-tuc-hoan-thien-cac-tieu-chi-sau-nang-hang-va-hoi-nhap-trong-nam-2026-100260106090458334.htm)).

Lịch chủ đề theo mùa là suy luận và cần kiểm chứng bằng Google Trends. Các mốc gồm: Tết và ngày Vía Thần Tài, các cuộc họp Fed, điều hành của Ngân hàng Nhà nước, kỳ đánh giá nâng hạng của FTSE/MSCI, mùa báo cáo tài chính quý, và các thay đổi thuế.

Phía cung tiền thì hẹp hơn nhiều. Dynamoi ước tính AdSense RPM ở Việt Nam khoảng **0,22 USD/1.000 view**, bằng khoảng 0,2 lần trung vị các thị trường (1,09 USD) ([Dynamoi](https://dynamoi.com/data/youtube-adsense-rpm/vn)). Các blog Việt ghi khoảng 0,3–0,5 USD ([Accesstrade](https://accesstrade.vn/1000-view-youtube-duoc-bao-nhieu-tien-o-viet-nam/)). Kênh tài chính tiếng Anh nhắm vào Mỹ được ước tính 10–25 USD ([OutlierKit](https://outlierkit.com/blog/youtube-rpm-finance-niche)). Ngách tài chính tiếng Việt có lẽ cao hơn mức trung bình VN vì nhà quảng cáo là ngân hàng, công ty chứng khoán và fintech. Mức hợp lý để lập kế hoạch là **0,3 / 0,6 / 1,2 USD** (thấp / cơ sở / cao), nhưng đây là ước tính, phải thay bằng số thật trong YouTube Studio sau khi bật kiếm tiền `[CẦN XÁC MINH]`. Shorts tiếng Việt suy ra chỉ khoảng 0,01–0,05 USD/1.000 view, tức gần như không đáng kể về doanh thu.

### Kiều bào là đòn bẩy RPM đáng thử nhất

Google công bố rằng **hơn 50% thời gian xem của các kênh do người Việt sản xuất đến từ người xem ở nước ngoài** ([CafeF](https://cafef.vn/93-nguoi-dung-internet-viet-nam-xem-youtube-moi-ngay-188260917145859624.chn)). Kết hợp với mức chênh RPM (view Việt chỉ vài cent/1.000, trong khi view nước ngoài có thể khoảng 6,5 USD theo một creator chia sẻ, [Lilys](https://lilys.ai/notes/vi/design-with-canva-20251118/ai-youtube-foreign-views)), phép tính minh hoạ cho kết quả rất đáng chú ý. Giả sử 90% view đến từ VN với RPM 0,3 USD và 10% từ Mỹ/Úc/Canada với RPM khoảng 5 USD. RPM pha trộn khi đó là khoảng 0,77 USD, và **10% view kiều bào mang lại khoảng 65% doanh thu AdSense**.

Từ đó có một giả thuyết chiến lược, chưa phải dữ liệu: chủ đề "kinh tế Việt Nam nhìn từ ngoài" có thể nâng RPM đáng kể. Ví dụ là các chủ đề kiều hối, tỷ giá, so sánh mua nhà và chi phí sống, doanh nghiệp Việt vươn ra thế giới. Ngược lại, nội dung chứng khoán và bất động sản nội địa nhiều khả năng có trên 95% view từ VN `[ƯỚC TÍNH]`.

Có một mặt trái cần lưu ý. View từ Mỹ bị khấu trừ thuế 30% (xem phần tài khoản). Ngoài ra, tính năng auto-dubbing của YouTube đã mở cho mọi creator từ 2/2026 với 27 ngôn ngữ ([WinBuzzer](https://winbuzzer.com/2026/02/05/youtube-ai-auto-dubbing-all-creators-27-languages-xcxwbn/)). Điều đó đang thu hẹp cửa sổ "dịch thuần" từ kênh tiếng Anh. Lợi thế chỉ còn ở phần bối cảnh Việt mà bản lồng tiếng tự động không có. Chưa xác minh được tiếng Việt có nằm trong 27 ngôn ngữ đó hay không `[CẦN XÁC MINH 2026-10-10]`. Bài học cụ thể là **mượn cấu trúc format chứ không dịch nội dung**. Kênh slop lớn nhất bị xoá tháng 1/2026 là một kênh tiếng Tây Ban Nha có hơn 1,2 tỷ view ([Tubefilter](https://tubefilter.com/2026/01/29/youtube-ai-slop-channel-crackdown-bans/)): bản địa hoá không giúp kênh thoát khỏi chính sách.

### Doanh thu ngoài AdSense

Với RPM thấp như vậy, doanh thu ngoài AdSense mới là đòn bẩy, theo thứ tự ưu tiên sau:

1. **Affiliate mở tài khoản chứng khoán.** Chương trình "mời bạn" công khai của các công ty chứng khoán thưởng nhỏ: DNSE 10.000 đ/khách (2024), VPS thưởng 100.000–200.000 đ theo thi đua (7/2026) ([DNSE](https://www.dnse.com.vn/hoc/them-ban-them-qua-cung-dnse); [VNBA](https://vnba.org.vn/vi/vps-tang-qua-nguoi-gioi-thieu-khach-hang-moi-7624.htm)). Mô hình chia theo phí giao dịch đáng giá hơn: KIS từng trả tới 70% hoa hồng phí giao dịch trong một chương trình đã kết thúc ([VnEconomy](https://vneconomy.vn/gioi-thieu-ban-qua-vo-han-cung-hoa-hong-toi-70-tai-chung-khoan-kis.htm)). Accesstrade cũng đang đề xuất mô hình revenue share cho công ty chứng khoán ([Brands Vietnam](https://www.brandsvietnam.com/congdong/topic/346105-mo-hinh-moi-giup-cong-ty-chung-khoan-toi-uu-chi-phi-tang-truong-ben-vung)). Mức hoa hồng hiện tại không công khai, phải đăng ký publisher mới xem được.
2. **Link mời app ngân hàng và thẻ.**
3. **Sản phẩm số riêng** (template Excel quản lý tài chính, ebook), sau khi có khoảng 5–10 nghìn sub.
4. **Tài trợ.**
5. **Membership** sau khi đạt Tier 1.
6. **YouTube Shopping.** Tính năng có ở VN từ 11/2024 với Shopee ([Advertising Vietnam](https://advertisingvietnam.com/article/youtube-shopping-affiliate-chinh-thuc-ra-mat-tai-viet-nam-p25438)), nhưng ít hợp ngách tài chính, chỉ dùng được cho sách.

Các mốc sub cho mục 3 và 4 là ước tính, không có nguồn.

### Mục tiêu 3 tháng và 6 tháng phải dựa trên chỉ số dẫn dắt, không dựa trên tiền

YPP Tier 1 yêu cầu 500 sub, 3 video công khai trong 90 ngày, và 3.000 giờ xem/12 tháng hoặc 3 triệu view Shorts/90 ngày. Tier này chỉ mở fan funding. Muốn có chia sẻ quảng cáo phải đạt Tier 2: 1.000 sub cộng 4.000 giờ xem/12 tháng, hoặc 10 triệu view Shorts/90 ngày ([vidIQ](https://vidiq.com/blog/post/monetize-youtube-guide/); [AIR Media-Tech](https://air.io/en/monetization/youtube-partner-program-requirements-2026-the-complete-guide)). Chưa xác nhận trực tiếp được Việt Nam có trong danh sách áp dụng Tier 500 sub. ViệtTimes có đưa tin là có ([ViệtTimes](https://viettimes.vn/youtube-ha-thap-tieu-chi-chao-don-nguoi-dung-kiem-tien-post167681.html)) `[CẦN XÁC MINH]`. Chỉ một nguồn nói từ 1/2/2027 ngưỡng Tier 2 sẽ tăng lên 8.000 giờ xem `[CẦN XÁC MINH 2026-10-10]`. Nếu tin này đúng, kênh cần đạt YPP trước tháng 2/2027, và đây là lý do để bắt đầu ngay.

Mô hình ba kịch bản dưới đây hoàn toàn là ước tính. Giả định: video dài 8–12 phút, thời lượng xem trung bình khoảng 3,5 phút, tỷ giá 26.000 đ/USD `[CẦN XÁC MINH]`.

| Tích luỹ đến tháng 6 | Thận trọng | Cơ sở | Lạc quan |
|---|---|---|---|
| Video dài/tuần | 3 | 4 | 5 |
| Tổng view 6 tháng | ~37.500 | ~189.000 | ~920.000 |
| Giờ xem | ~2.200 | ~11.000 | ~50.000+ |
| Sub | ~250 | ~1.900 | ~11.500 |
| Đạt YPP Tier 2 | Không | Cuối T4–T5 | T2–T3 |
| AdSense 6 tháng | 0 đ | ~1–2 triệu đ | ~20–27 triệu đ |
| Lãi/lỗ 6 tháng (gồm chi phí công cụ ~1,5–3 triệu đ/tháng) | Lỗ ~9–18 triệu | Lỗ ~5–15 triệu | Hoà đến lãi ~10–35 triệu |

**Mục tiêu 3 tháng (cơ sở):** khoảng 45–50 video, khoảng 34.000 view tích luỹ, 350–500 sub, khoảng 2.000 giờ xem, CTR ≥4%, thời lượng xem trung bình (AVD) ≥35%. Nếu đến lúc đó chỉ đạt ≤10.000 view hoặc ≤100 sub, phải xem lại chủ đề và thumbnail *trước khi* tăng sản lượng.

**Mục tiêu 6 tháng (cơ sở):** 1.000–2.000 sub, ≥4.000 giờ xem, được duyệt YPP, có ít nhất một chương trình affiliate tài chính đang chạy với tỷ lệ chuyển đổi đo được.

Các ngưỡng CTR và AVD ở trên là heuristic phổ biến, không phải chuẩn riêng cho tài chính Việt `[CẦN XÁC MINH]`. Chúng cần được hiệu chỉnh bằng dữ liệu thật sau 4–6 tuần.

## Tháng 7/2026 YouTube nhắm thẳng vào "chuyên gia AI" tài chính

Rủi ro chính sách với dự án này đã leo thang qua ba đợt, và đợt gần nhất chạm thẳng vào ngách tài chính.

**Đợt 1, tháng 7/2025.** YouTube đổi tên chính sách thành "inauthentic content". Rene Ritchie (YouTube) gọi đây là "minor update", và nội dung tái sử dụng vẫn kiếm tiền được nếu có bình luận gốc hoặc giá trị giáo dục đáng kể ([exchange4media](https://www.exchange4media.com/digital-news/youtube-issues-clarification-on-monetisation-policy-update-after-creator-backlash-145327.html)).

**Đợt 2, tháng 1/2026.** Trong thư thường niên, CEO Neal Mohan đặt "quản lý AI slop" làm ưu tiên ([Tubefilter](https://www.tubefilter.com/2026/01/21/neal-mohans-2026-letter-to-creators-a-lot-of-ai-a-tiktok-shop-competitor-and-beautifully-produced-tv-to-compete-with-netflix/)). Khoảng 16–18 kênh AI slop lớn bị xoá, tổng cộng hơn 4 tỷ view. Điều quan trọng là YouTube xoá kênh theo **chính sách spam và hành vi lừa đảo (deceptive practices)**, không theo một luật "chống AI" mới ([Boing Boing](https://boingboing.net/2026/01/28/slop.html)). Nói cách khác, tiêu đề và thumbnail gây hiểu lầm có thể dẫn đến *xoá kênh*, không chỉ mất kiếm tiền.

**Đợt 3, tháng 7/2026.** YouTube chia nội dung không được kiếm tiền thành ba nhóm: nội dung chung chung hoặc theo template, nội dung gây khó chịu, và **nội dung dùng AI persona bàn chủ đề nhạy cảm như sức khoẻ và tài chính** ([TechCrunch](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/); [Tubefilter](https://www.tubefilter.com/2026/07/13/youtube-inauthentic-content-monetization-policy-update/)). Tài chính, pháp lý và y tế được nêu là các lĩnh vực mà hình ảnh AI của người thật hoặc AI avatar đưa lời khuyên bị cấm kiếm tiền ([Moneywise](https://moneywise.com/news/top-stories/youtube-ai-slop-inauthentic-content-monetization-rules)).

Cần đọc đúng tinh thần đợt 3. Câu chữ nhắm vào **"chuyên gia giả" đưa lời khuyên**, không nhắm vào giọng AI kể chuyện. Tuy vậy, YouTube không định nghĩa "bao nhiêu là quá nhiều", và giới phê bình chỉ ra rằng cơ chế lọc khó phân biệt phim AI có đạo diễn với bot farm ([HackerNoon](https://hackernoon.com/youtubes-ai-slop-crackdown-cant-tell-a-directed-ai-film-from-a-bot-farm)). Vì vậy kênh nên chủ động đứng xa ranh giới:

- Không dựng một nhân vật AI trông như người thật với tên kiểu "Chuyên gia X".
- Không đưa lời khuyên đầu tư cá nhân hoá.
- Nếu muốn có "người dẫn", dùng nhân vật hoạt hình rõ ràng là minh hoạ, hoặc dùng giọng clone của chính chủ kênh (có đồng ý).

Cũng chưa tìm thấy ca cụ thể nào về một kênh *tài chính* AI bị demonetize. Bằng chứng hiện chủ yếu đến từ kênh truyện, trailer giả và brainrot. Đây là một khoảng trống bằng chứng chứ không phải lý do để chủ quan.

Song song là quy định **công bố nội dung tổng hợp (altered/synthetic)**, áp dụng từ 3/2024. Chỉ phải khai khi nội dung trông thật và có thể bị nhầm là người, địa điểm hoặc sự kiện thật. Dùng AI để viết script, lên ý tưởng hay tạo phụ đề thì không cần khai. Riêng các chủ đề nhạy cảm, trong đó có **tài chính**, nhãn sẽ hiện ngay trên video. Nếu không khai, YouTube có thể tự gắn nhãn và không gỡ được ([YouTube Blog](https://blog.youtube/news-and-events/disclosing-ai-generated-content)). Hệ quả thực tế: hình minh hoạ hoạt hình và biểu đồ không cần nhãn, còn cảnh AI dựng lại một doanh nhân thật hoặc một sự kiện thật thì phải khai và sẽ có nhãn hiện rõ. Đó thêm một lý do để chọn phong cách minh hoạ thay vì phong cách chân thực.

## Luật Việt Nam, không phải YouTube, là rủi ro pháp lý lớn nhất

YouTube có thể cắt kiếm tiền. Luật Việt Nam có thể phạt tiền, thậm chí xử lý hình sự. Có ba vùng rủi ro, xếp theo mức độ nghiêm trọng.

**Thứ nhất, khuyến nghị chứng khoán.** Ủy ban Chứng khoán Nhà nước (UBCKNN) cảnh báo sẽ xử lý nghiêm tổ chức hoặc cá nhân đưa báo cáo phân tích và khuyến nghị mua, bán, nắm giữ chứng khoán mà không có giấy phép ([Bnews/TTXVN](https://bnews.vn/canh-cao-than-trong-voi-cac-hoi-nhom-tu-van-chung-khoan-khong-phep/417919.html)). Một doanh nghiệp đã bị phạt 225 triệu đồng theo Nghị định 156/2020/NĐ-CP vì tư vấn chứng khoán không phép ([Doanh nghiệp Hội nhập](https://doanhnghiephoinhap.vn/xu-phat-doanh-nghiep-tu-van-chung-khoan-chui-canh-bao-rui-ro-tu-cac-khuyen-nghi-dau-tu-tren-mang-132915.html)). Chưa tìm thấy mức phạt cụ thể cho cá nhân là YouTuber `[CẦN XÁC MINH]`. Ranh giới thực hành, cần luật sư xác nhận, như sau:

- **An toàn hơn nhiều:** kiến thức chung như lãi kép, cách đọc báo cáo tài chính, so sánh các loại hình đầu tư, tin vĩ mô có trích nguồn.
- **Rơi vào hành vi tư vấn đầu tư cần giấy phép:** "mua HPG vùng giá X, target Y", nhóm Zalo/Telegram "phím hàng" có thu phí.

**Thứ hai, crypto.** Nghị quyết 05/2025/NQ-CP chỉ cho thí điểm thị trường tài sản mã hoá trong 5 năm, giao dịch qua sàn được cấp phép và thanh toán bằng VND ([LuatVietnam](https://luatvietnam.vn/tin-van-ban-moi/tai-toan-van-nghi-quyet-05-2025-nq-cp-ve-trien-khai-thi-diem-thi-truong-tai-san-ma-hoa-186-103979-article.html)). Nghị định 284/2026/NĐ-CP có hiệu lực từ 1/9/2026, phạt tối đa 100 triệu đồng với cá nhân và 200 triệu đồng với tổ chức ([LSVN](https://lsvn.vn/tu-01-9-cho-phep-xu-phat-vi-pham-hanh-chinh-ve-tai-san-ma-hoa-tren-moi-truong-dien-tu-a176722.html)). Chưa đọc được văn bản nên chưa rõ có điều khoản riêng về quảng bá sàn không phép hay không `[CẦN XÁC MINH]`. Dù vậy, kết luận vẫn dứt khoát: **không affiliate sàn crypto nước ngoài hay dự án token**. Trước đây đây là "mỏ vàng" CPA của nhiều kênh tài chính, giờ nó là rủi ro pháp lý trực tiếp.

**Thứ ba, Luật Quảng cáo sửa đổi số 75/2025/QH15**, có hiệu lực từ 1/1/2026. Luật bổ sung Điều 15a về người có ảnh hưởng, với các nghĩa vụ sau:

- Phải xác minh độ tin cậy của bên quảng cáo và kiểm tra tài liệu sản phẩm.
- Không được giới thiệu sản phẩm mình chưa dùng hoặc chưa hiểu rõ.
- Phải thông báo việc quảng cáo **ngay trước và trong khi** thực hiện.
- Quảng cáo sai sự thật có thể bị xử lý hình sự ([LuatVietnam](https://luatvietnam.vn/linh-vuc-khac/diem-moi-cua-luat-quang-cao-sua-doi-2025-883-102813-article.html); [LuatVietnam – hình sự](https://luatvietnam.vn/tin-van-ban-moi/nguoi-co-anh-huong-quang-cao-sai-su-that-co-the-bi-xu-ly-hinh-su-186-103749-article.html)).

Với một kênh AI, điều này dẫn đến một câu hỏi chưa ai trả lời: "người có ảnh hưởng" là chủ kênh hay giọng AI? Câu trả lời an toàn là chủ kênh chịu toàn bộ trách nhiệm. Mọi video có affiliate hay tài trợ phải công bố bằng lời và bằng chữ ở đầu video và tại đoạn nói về sản phẩm, đồng thời bật nhãn "Includes paid promotion". Ngoài ra cần lưu hồ sơ thẩm định nhà tài trợ, gồm giấy phép và tài liệu sản phẩm.

Hai rủi ro phụ còn lại là thông tin sai sự thật trên mạng và bản quyền.

Về thông tin sai sự thật: có chế tài hành chính (Nghị định 15/2020, sửa bởi Nghị định 14/2022) và hình sự (Điều 288 Bộ luật Hình sự). Mức phạt hiện hành năm 2026 chưa xác minh `[CẦN XÁC MINH]`. Rủi ro này lớn hơn với kênh AI, vì LLM có thể "bịa" số liệu tài chính. Vì vậy bước fact-check số liệu là bắt buộc, không phải tuỳ chọn.

Về bản quyền: phiên nghiên cứu không tìm được nguồn mới. Nguyên tắc an toàn như sau:

- Không phát lại clip VTV, đài truyền hình hay báo. Các đơn vị này và đối tác MCN đăng ký Content ID rộng rãi.
- Chỉ dùng nhạc từ YouTube Audio Library hoặc dịch vụ có license rõ ràng.
- Tóm tắt tin tức bằng lời và ghi nguồn.

Ngoại lệ trích dẫn trong Luật Sở hữu trí tuệ Việt Nam hẹp hơn "fair use" của Mỹ, và cơ chế 3 gậy trong 90 ngày thì chấm dứt kênh. Cả hai đều cần đối chiếu lại `[CẦN XÁC MINH]`.

## Dựng tài khoản đúng một lần: Brand Account, một AdSense, W-8BEN, sổ thuế

Mục tiêu của phần này là kênh không bị vỡ khi lớn lên: không mất kênh vì bị hack, không kẹt khi cần chuyển kênh sang công ty, không bị khấu trừ thuế oan, không bị truy thu.

### Bảo mật và quyền sở hữu

Thiết lập theo các bước sau:

1. Tạo một **Google account riêng** cho kênh, tên thật khớp CCCD (cần cho AdSense sau này), dùng SIM VN chính chủ làm số khôi phục.
2. Đặt kênh dưới dạng **Brand Account / channel permissions**. YouTube đã thay quyền truy cập Brand Account bằng các vai trò Owner, Manager, Editor, Editor (Limited)… ([YouTube Help](https://support.google.com/youtube/answer/9367690?hl=en)).
3. Thêm một Owner dự phòng là tài khoản thứ hai của chính chủ.
4. Không bao giờ cấp quyền Owner cho người làm thuê hay công cụ. Dùng **Editor (Limited)**, vai trò không xem được doanh thu.

Cấu trúc Brand Account còn để ngỏ đường chuyển kênh sang pháp nhân sau này, vì việc chuyển quyền sở hữu vẫn đi qua Brand Account ([Leadsie](https://www.leadsie.com/blog/give-youtube-channel-access)). Có một cảnh báo quan trọng: xoá tài khoản primary owner thì kênh cũng bị xoá theo.

Mối đe doạ số một không phải mật khẩu yếu mà là **email "mời tài trợ" kèm file tải về**. Mã độc trong các file này ăn cắp cookie phiên và **vượt qua được 2FA**. Kênh bị chiếm thường bị bán lại hoặc đổi tên để livestream lừa đảo crypto ([The Hacker News](https://thehackernews.com/2021/10/hackers-stealing-browser-cookies-to.html)). Nguồn này từ 2021, và chưa kiểm chứng được mức độ phổ biến của kiểu tấn công này trong 2025–2026. Biện pháp phòng tránh:

- Dùng máy hoặc trình duyệt riêng cho tài khoản kênh.
- Không mở file .exe, .scr, .zip từ "nhà tài trợ".
- Dùng passkey hoặc khoá bảo mật vật lý.
- Định kỳ xem lại danh sách thiết bị đăng nhập.
- Khi dùng tool tự động hoá, chỉ cấp quyền qua OAuth với project Google Cloud của chính mình, không đưa cookie hay mật khẩu cho SaaS lạ.

Nghị định 147/2024/NĐ-CP yêu cầu tài khoản mạng xã hội xác thực bằng số điện thoại Việt Nam ([VnEconomy](https://vneconomy.vn/tu-ngay-25-12-tai-khoan-mang-xa-hoi-phai-xac-thuc-so-dien-thoai-moi-duoc-dang-bai.htm)). Đặt quốc gia kênh là "Việt Nam" là trung thực và khớp với hồ sơ AdSense và thuế. Đặt quốc gia giả để "tăng RPM" không có cơ sở, vì RPM phụ thuộc vào nơi người xem ở.

### AdSense và thanh toán

Chỉ tạo **một** tài khoản AdSense, tên và địa chỉ khớp CCCD và tài khoản ngân hàng. Địa chỉ phải nhận được thư bưu điện, vì mã PIN gửi qua đường bưu điện. Phương thức thanh toán thực tế là chuyển khoản điện tử (wire) về ngân hàng Việt Nam. Western Union đã ngừng nhận đăng ký mới từ 10/8/2020 ([Search Engine Roundtable](https://www.seroundtable.com/google-adsense-western-union-payment-option-29924.html)).

Hai thông tin phổ biến nhưng chưa trích được nguồn Google trong phiên `[CẦN XÁC MINH 2026-10-10]`:

- Quy tắc "một người – một AdSense".
- Ngưỡng thanh toán 100 USD.

Biểu phí nhận SWIFT của từng ngân hàng cũng cần tự kiểm tra.

### Thuế Mỹ

Nộp **W-8BEN ngay khi bật kiếm tiền**, khai là cá nhân, Việt Nam, không claim hiệp định. Hiệp định thuế Việt – Mỹ ký ngày 7/7/2015 nhưng chưa có hiệu lực ([DFDL](https://www.dfdl.com/insights/legal-and-tax-updates/tax-alert-the-income-tax-treaty-between-vietnam)). Hệ quả: bị khấu trừ 30% trên phần doanh thu từ người xem Mỹ. Nếu không nộp W-8BEN, Google có thể khấu trừ tới **24% doanh thu toàn cầu** ([Hanoi Times](https://hanoitimes.vn/google-withholds-taxes-from-non-us-youtube-creators.583585.html)).

Ví dụ minh hoạ: tháng có 400 USD, trong đó 100 USD từ người xem Mỹ. Có W-8BEN thì bị khấu trừ 30 USD. Không có W-8BEN thì có thể bị khấu trừ tới 96 USD. Khoản thuế Mỹ đã khấu trừ nhiều khả năng **không được trừ vào thuế Việt Nam** `[CẦN XÁC MINH]`.

### Thuế Việt Nam năm 2026

Đây là phần thay đổi nhanh nhất: ba văn bản trong 10 tháng.

| Giai đoạn / văn bản | Quy định |
|---|---|
| Đến hết 2025 | Doanh thu >100 triệu đồng/năm nộp 7% (5% GTGT + 2% TNCN) ([Vietstock](https://vietstock.vn/2026/07/thu-nhap-tu-youtube-duoc-tinh-thue-the-nao-4261-1467965.htm)) |
| Luật Thuế TNCN 109/2025/QH15 (hiệu lực 1/7/2026) | Doanh thu ≤500 triệu không nộp TNCN; 500 triệu–3 tỷ áp dụng 15% ([Cổng Chính phủ](https://xaydungchinhsach.chinhphu.vn/thong-nhat-ho-kinh-doanh-co-doanh-thu-den-500-trieu-dong-nam-khong-phai-nop-thue-119251210100204058.htm)). Thuế suất có mâu thuẫn giữa các nguồn `[CẦN XÁC MINH]` |
| Nghị định 68/2026 (5/3/2026) | Ngưỡng 500 triệu |
| Nghị định 141/2026 (29/4/2026) | Nâng ngưỡng miễn GTGT và TNCN lên **1 tỷ đồng/năm**, áp dụng từ 1/1/2026 ([Tạp chí Công Thương](https://tapchicongthuong.vn/chinh-thuc--nang-nguong-chiu-thue-voi-ho-kinh-doanh-len-1-ty-dong-nam--ap-dung-tu-1-1-2026-514336.htm)) |

Quan hệ giữa ngưỡng 1 tỷ của Nghị định 141 và ngưỡng 500 triệu của Luật 109 chưa rõ. Cũng chưa có hướng dẫn cách tính phần vượt ngưỡng ([VTV](https://vtv.vn/youtuber-dong-thue-the-nao-100260721111643838.htm)) `[CẦN XÁC MINH]`.

Hệ quả cho một kênh mới khá đơn giản. Năm đầu gần như chắc chắn dưới ngưỡng 1 tỷ đồng, nên không phát sinh thuế Việt Nam. Dù vậy vẫn nên làm ba việc:

- **Thông báo doanh thu** theo Mẫu 01/TKN-CNKD trước 31/1 năm sau, theo nguồn thứ cấp ([xcyber](https://xcyber.vn/ho-kinh-doanh-co-doanh-thu-duoi-1-ty/)).
- Lập file theo dõi theo tháng gồm doanh thu gộp, phần Mỹ khấu trừ, thực nhận và tỷ giá ngày nhận.
- Lưu payment receipt AdSense và sao kê ngân hàng.

Có hồ sơ sạch từ năm đầu là cách rẻ nhất để không bị truy thu khi kênh lớn. Khi doanh thu năm tiến gần 1 tỷ đồng, hoặc khi ký hợp đồng tài trợ với doanh nghiệp, cần hỏi kế toán. Lúc đó cân nhắc tính thuế theo thu nhập (doanh thu trừ chi phí AI và editor) và thành lập công ty TNHH một thành viên để chuyển kênh cùng AdSense sang pháp nhân.

## Khuyến nghị: định vị, công cụ, 30 ngày đầu và ba thí nghiệm

### Định vị kênh đề xuất

Đề xuất là một kênh **"Kinh tế Việt kể bằng dữ liệu"**. Kênh giải thích vì sao doanh nghiệp, thị trường và đồng tiền Việt Nam vận hành như vậy, theo hai format chính:

- **Format A, chiếm khoảng 60% sản lượng: kể chuyện doanh nghiệp, 10–15 phút.** Tiêu đề theo các khuôn "Vì sao X sụp đổ", "X kiếm tiền thế nào", "Thăng trầm của X". Đối tượng là doanh nghiệp Việt và thương hiệu toàn cầu có mặt ở Việt Nam.
- **Format B, chiếm khoảng 40%: explainer vĩ mô có biểu đồ thật, 8–12 phút.** Chủ đề gồm vàng, lãi suất, tỷ giá, Fed tác động đến Việt Nam, nâng hạng thị trường. Có một nhánh "nhìn từ ngoài" cho kiều bào.

Cả hai format đều cắt Shorts từ chính video dài. Kênh định vị bằng lời hứa: **"không khuyến nghị mã, không bán khóa học làm giàu, mọi con số có nguồn"**. Lời hứa này biến vụ HieuTV và quy định của UBCKNN thành lợi thế. Về nhận diện, dùng một phong cách minh hoạ hoạt hình nhất quán, biểu đồ tự dựng, và một giọng kể cố định. Ưu tiên clone giọng chính chủ nếu bài nghe mù cho thấy giọng clone tốt hơn các giọng TTS. Mỗi video mở đầu bằng disclaimer "nội dung giáo dục, không phải khuyến nghị đầu tư" và có danh sách nguồn trong phần mô tả.

"100% AI" ở đây nghĩa là AI làm mọi khâu sản xuất, còn **chủ kênh giữ ba điểm chạm 10–20 phút mỗi video**:

1. Chọn góc nhìn.
2. Duyệt số liệu.
3. Bấm publish.

Ba điểm chạm này chính là "giá trị gia tăng của con người" mà chính sách của YouTube đòi hỏi.

### Bộ công cụ (Budget trước, khoảng $20–60/tháng)

| Khâu | Budget (khởi đầu) | Nâng lên khi có tín hiệu |
|---|---|---|
| Nghiên cứu + script | Gói chat LLM có web search (~$20/tháng `[CẦN XÁC MINH]`); LLM thứ hai fact-check số liệu | API LLM trong n8n |
| Giọng | Người thắng bài nghe mù trong các lựa chọn: Google Chirp 3 HD (free 1 triệu ký tự), Azure, Vbee/FPT.AI/Viettel | ElevenLabs Creator $22 (clone giọng chính chủ) hoặc Pro $99 |
| Hình | Ảnh AI phong cách minh hoạ + Pexels/Pixabay (điều khoản `[CẦN XÁC MINH]`) + biểu đồ matplotlib/Remotion | Envato $16,5 (dùng YouTube Audio Library cho nhạc thay vì nhạc Envato); b-roll video AI ~$50–100/tháng |
| Dựng + phụ đề | CapCut làm tay (L1) → ffmpeg/MoviePy/Remotion tự host (L2); phụ đề căn từ chính văn bản script | JSON2Video $49,95 hoặc Shotstack |
| Thumbnail | Canva template + ảnh AI; Test & compare 3 biến thể trong Studio | Canva autofill qua API |
| Điều phối + upload | Upload tay qua Studio, lên lịch | n8n self-host trên VPS (~$5–10 `[CẦN XÁC MINH]`), chỉ sau khi format đã thắng |

Theo luật của repo, chưa xây automation khi chưa có test cho thấy tín hiệu. Vì vậy tháng đầu chạy ở mức L1–L2. Chỉ đẩy lên L3 sau khi một format vượt ngưỡng ở thí nghiệm 1.

### Kế hoạch 30 ngày

| Thời gian | Việc chính | Đầu ra |
|---|---|---|
| Ngày 1–3 | Dựng tài khoản theo phần trên: Google account riêng, Brand Account, Owner dự phòng, passkey, quốc gia = VN, xác minh điện thoại; ghi vào `ops/DECISIONS.md` | Kênh an toàn, sẵn sàng chuyển nhượng |
| Ngày 2–5 | Lấp khoảng trống dữ liệu: lượt Playboard/Social Blade làm tay hoặc script YouTube Data API cho khoảng 12 kênh ứng viên + 5 kênh quốc tế | Bảng đối thủ trong `research/competitors/` |
| Ngày 4–7 | Bài nghe mù TTS (4–6 giọng, đoạn script có nhiều số); chốt phong cách minh hoạ; viết "kinh thánh kênh" (giọng văn, disclaimer, quy trình fact-check, danh sách cấm) | Giọng + style guide |
| Ngày 8–14 | Sản xuất 4 video thử (2 format A, 2 format B) + 8 Shorts cắt từ đó; tính giờ làm và chi phí thật cho từng video | 4 video sẵn sàng |
| Ngày 15–28 | Đăng 3 video dài/tuần + 4–6 Shorts/tuần; bật Test & compare thumbnail; ghi số liệu 48 giờ và 7 ngày của từng video | ~10 video dài, ~20 Shorts |
| Ngày 29–30 | Đánh giá thí nghiệm 1–2 theo ngưỡng; quyết định format chính; cập nhật skill và `ops/JOURNAL.md` | Quyết định tiếp tục / xoay hướng |

### Ba thí nghiệm khởi đầu

Ngưỡng CTR, AVD và retention dưới đây lấy từ heuristic phổ biến cho kênh mới `[CẦN XÁC MINH]`. Nên hiệu chỉnh lại sau tuần thứ 6.

| | Giả thuyết | KPI chính | Đạt | Không đạt | Thời hạn / chi phí tối đa |
|---|---|---|---|---|---|
| **EXP-001 – Format** | Format A (kể chuyện doanh nghiệp) giữ chân tốt hơn format B (explainer vĩ mô) với khán giả tài chính Việt | AVD %, CTR, view 7 ngày (so trung vị) | Format có ≥4 video đạt AVD trung vị ≥35% và CTR ≥4% | Cả hai format AVD <30% và CTR <3%, khi đó đổi chủ đề/thumbnail trước khi tăng sản lượng | 6 tuần, ≥4 video mỗi format; ≤$60/tháng |
| **EXP-002 – Giọng** | Giọng chất lượng cao/clone giọng chính chủ tăng retention 30 giây đầu so với giọng TTS miễn phí | Retention ở giây 30, AVD % | Giọng cao cấp có retention 30 giây ≥65% và hơn giọng miễn phí ≥5 điểm % trên các cặp chủ đề tương đương | Chênh lệch <2 điểm %, khi đó giữ giọng miễn phí và tiết kiệm chi phí | 4 tuần, ≥3 cặp video; thêm ≤$22/tháng |
| **EXP-003 – Kiều bào** | Chủ đề "kinh tế Việt nhìn từ ngoài" kéo được tỷ lệ view ngoài Việt Nam cao hơn rõ rệt, tức RPM pha trộn cao hơn khi kiếm tiền | % view ngoài VN (tab Geography), sau YPP là RPM | Video kiều bào có ≥15% view ngoài VN và gấp ≥2 lần trung bình kênh, không kém về CTR/AVD | <1,5 lần trung bình kênh, khi đó giữ ở mức chủ đề thỉnh thoảng | 8 tuần, ≥4 video; không tốn thêm |

## Kết luận

Câu hỏi thực sự của dự án không còn là "AI có làm được video tài chính tiếng Việt không" (làm được, với giá chỉ vài chục USD mỗi tháng). Câu hỏi là **phần nào của kênh phải giữ là con người để AI được phép làm phần còn lại**. Chính sách YouTube năm 2026 và luật Việt Nam cùng chỉ về một câu trả lời. Phần người là góc nhìn, việc kiểm chứng số liệu và trách nhiệm pháp lý. Phần máy là giọng, hình, dựng và phân phối. Điều này đảo ngược trực giác ban đầu "tự động hoá càng nhiều càng tốt". Các format tự động hoá hoàn toàn (bản tin hằng ngày, slideshow, avatar chuyên gia) đúng là những format đang bị nhắm tới. Lợi thế của người vào sau nằm ở một thị trường ngôn ngữ chưa có kênh video essay tài chính faceless dẫn đầu, cộng với một khoảng trống niềm tin mà các kênh dựa vào cá nhân vừa để lộ.

Hai biến số sẽ quyết định kinh tế học của kênh, và cả hai hiện đều chưa có dữ liệu: RPM thật của ngách tài chính tiếng Việt, và tỷ lệ view kiều bào. Cả hai chỉ đo được bằng chính kênh của mình. Vì vậy 30 ngày đầu nên được xem là một khoản chi để mua dữ liệu, đừng coi đó là một cuộc chạy đua sản lượng. Lượt kiểm tra đối thủ bằng YouTube Data API hoặc Playboard nên được nâng thành skill định kỳ hằng tháng, vì trong một ngách mà các khoá học đang đào tạo hàng loạt người làm kênh AI, bức tranh đối thủ sẽ đổi rất nhanh.
