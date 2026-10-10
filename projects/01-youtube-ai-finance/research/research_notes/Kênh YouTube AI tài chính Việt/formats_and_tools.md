# Format video & bộ công cụ sản xuất video tài chính 100% AI cho kênh YouTube tiếng Việt (ngày nghiên cứu: 2026-10-10)

> Ghi chú chung: phần lớn giá lấy từ blog/aggregator bên thứ ba (2026). Một số trang chính thức (developers.google.com, blotato.com) **không truy cập được** từ môi trường nghiên cứu (lỗi DNS), nên các con số quan trọng đều cần đối chiếu lại trang giá chính thức. Giá ghi theo USD, thời điểm nguồn ghi bên cạnh. Mọi thứ không có nguồn rõ được gắn `[CẦN XÁC MINH 2026-10]`.

## 1. Các format video faceless/AI cho nội dung tài chính, và rủi ro chính sách YouTube

### Takeaway
YouTube không cấm AI; thứ bị loại khỏi kiếm tiền (YPP) là nội dung "inauthentic" — sản xuất hàng loạt, lặp lại, khác nhau chỉ bề mặt (ví dụ YouTube nêu đích danh: chuỗi video kể chuyện có giọng đọc chỉ khác nhau sơ sài, chuỗi slideshow cùng kiểu narration). Format càng "template + giọng TTS + ảnh tĩnh" thì càng dễ tự động hoá nhưng càng rủi ro; format có nghiên cứu/góc nhìn riêng, dữ liệu, biểu đồ, kể chuyện có cấu trúc thì an toàn hơn. Nội dung tài chính thuộc nhóm "nhạy cảm" nên nếu dùng hình/giọng AI trông như thật về người/sự kiện thật thì nhãn AI có thể hiện ngay trên video.

### Cited Findings
**Chính sách**
- 15/07/2025 YouTube cập nhật hướng dẫn YPP để "nhận diện tốt hơn nội dung sản xuất hàng loạt và lặp lại"; Rene Ritchie (YouTube) gọi đây là "làm rõ nhỏ", loại nội dung này vốn đã không được kiếm tiền từ trước — [BetaNews](https://betanews.com/2025/07/10/youtube-is-fighting-ai-slop-with-new-monetization-guidelines/); [TechCrunch](https://techcrunch.com/2025/07/09/youtube-prepares-crackdown-on-mass-produced-and-repetitive-videos-as-concern-over-ai-slop-grows)
- Chính sách "repetitious content" được đổi tên thành "inauthentic content". Ví dụ bị cấm gồm: kênh đăng nhiều câu chuyện có narration chỉ khác nhau bề mặt, kênh có nhiều slideshow với narration giống hệt nhau; danh sách không đầy đủ; áp dụng bất kể công cụ tạo — [PPC Land](https://ppc.land/youtube-clarifies-inauthentic-content-policy-changes/)
- AI vẫn được kiếm tiền nếu nội dung "authentic"/bổ sung giá trị gốc; reaction và clip không bị ảnh hưởng — [AlternativeTo](https://alternativeto.net/news/2025/7/youtube-updates-its-policy-to-demonetize-inauthentic-mass-produced-ai-generated-content); [BetaNews](https://betanews.com/2025/07/10/youtube-is-fighting-ai-slop-with-new-monetization-guidelines/)
- Quy định công bố "altered or synthetic content" (từ 03/2024): phải khai khi nội dung trông thật có thể bị nhầm là người/địa điểm/sự kiện thật (đổi mặt, clone giọng người thật, dựng cảnh sự kiện không xảy ra). Không cần khai nếu AI chỉ dùng cho năng suất (viết script, ý tưởng, phụ đề tự động) hoặc nội dung rõ ràng không thực/hoạt hình. Với chủ đề nhạy cảm (sức khoẻ, tin tức, bầu cử, **tài chính**) nhãn đặt ngay trên video. Không khai → YouTube tự gắn nhãn không gỡ được; vi phạm lặp lại có thể bị gỡ/đình chỉ — [YouTube Blog](https://blog.youtube/news-and-events/disclosing-ai-generated-content); [NBC News](https://www.nbcnews.com/tech/tech-news/youtube-says-will-require-creators-label-ai-content-rcna143937)

**Bằng chứng về format/pipeline được dùng thực tế (2026)**
- Pipeline phổ biến: ChatGPT viết script → ElevenLabs lồng tiếng → Creatomate render Short có phụ đề động → (tuỳ chọn) upload YouTube hoặc lưu Google Drive để duyệt — [Creatomate (09/2026)](https://creatomate.com/blog/how-to-auto-generate-faceless-shorts-with-chatgpt-and-n8n)
- Format "AI presenter lip-sync + caption" bằng n8n + Orshot API — [Orshot](https://orshot.com/blog/how-to-make-faceless-videos-with-n8n)
- Format "AI-generated cinematic" bằng Sora 2 + n8n đăng tự động — [GrowwStacks](https://growwstacks.com/blog/automated-faceless-youtube-channel-sora2-n8n/)

### Inferences
Bảng đánh giá format (suy luận tổng hợp từ chính sách + chi phí công cụ ở các mục dưới; mức độ "giữ chân" là đánh giá định tính, chưa có số liệu kênh tiếng Việt):

| Format | Độ dài điển hình | Độ khó SX | Mức tự động hoá đạt được | Tiềm năng retention | Rủi ro "inauthentic"/nhãn AI |
|---|---|---|---|---|---|
| Documentary/storytelling (câu chuyện doanh nghiệp, tỷ phú, sụp đổ, bong bóng) | 10–25 phút | Trung bình–cao (script dài, cần fact-check, nhiều cảnh) | Cao (L2–L3) nếu script được duyệt bởi người | Cao (dạng kể chuyện giữ chân tốt) | Thấp–TB nếu mỗi tập nghiên cứu riêng; cao nếu cùng template, khác tên nhân vật |
| Explainer stock footage + chart (lãi suất, lạm phát, vàng, chứng khoán VN) | 8–15 phút | TB | Cao | TB–cao | Thấp–TB; biểu đồ dữ liệu thật tạo giá trị riêng |
| Whiteboard/animated explainer (2D, minh hoạ AI) | 5–12 phút | TB (cần style nhất quán) | TB–cao (ảnh AI + chuyển động Ken Burns/Remotion) | TB | Thấp (hoạt hình, không cần khai AI) |
| AI avatar presenter (HeyGen/Synthesia/D-ID) | 3–10 phút | Thấp | Rất cao | Thấp–TB (khán giả VN dễ nhận ra avatar) | TB: avatar trông thật + tài chính → có thể phải gắn nhãn; chi phí cao |
| News recap / market update (VN-Index, vàng SJC, tỷ giá hàng ngày) | 3–8 phút; hoặc Shorts | Thấp–TB | Rất cao (dữ liệu → script → render) | TB; phụ thuộc tốc độ | **Cao** nếu ngày nào cũng cùng khung, chỉ đổi số — đúng mẫu "repetitive" |
| Chart/data animation ("bar chart race", so sánh tài sản) | 1–5 phút | TB (cần dữ liệu sạch) | Rất cao (code-driven) | TB | TB (dễ thành lặp lại nếu không có bình luận) |
| Slideshow + voice | 5–15 phút | Rất thấp | Rất cao | Thấp | **Cao nhất** — YouTube nêu đích danh ví dụ slideshow |
| Listicle ("7 sai lầm tài chính tuổi 25") | 8–12 phút | Thấp–TB | Cao | TB | TB |
| AI-generated cinematic (Veo/Kling/Runway/Hailuo/Sora) | b-roll trong video dài, hoặc Shorts 30–60s | TB (prompt, nhất quán nhân vật) | Cao nhưng tốn tiền | Cao về thị giác | TB: cảnh "người/sự kiện thật" dựng lại cần khai AI; phong cách điện ảnh hư cấu thì ít rủi ro hơn |
| Podcast-style 2 giọng AI (hỏi–đáp) | 15–40 phút | Thấp | Rất cao | TB (dạng nghe nền) | TB |
| Shorts/vertical (cắt từ video dài hoặc sản xuất riêng) | 15–60s | Thấp | Rất cao | — (KPI khác: view, sub) | TB–cao nếu hàng loạt, cùng template |

- Format hợp lý nhất để cân bằng tự động hoá và an toàn YPP: **documentary/storytelling + explainer có chart dữ liệu thật**, dùng ảnh/video AI làm b-roll, Shorts cắt từ video dài. News recap hàng ngày dễ tự động nhất nhưng rủi ro "repetitive" cao nhất.
- Giọng clone **của chính chủ kênh** (có đồng ý) ít rủi ro hơn giọng giả người nổi tiếng; không bao giờ dùng giọng/mặt doanh nhân thật để "nói" điều họ không nói.

### Gaps
- Chưa đọc được văn bản chính thức trang Help YPP "inauthentic content" (chỉ có báo chí thuật lại). Cần mở trực tiếp support.google.com/youtube.
- Chưa có số liệu retention theo format cho kênh tài chính tiếng Việt — cần đo bằng test riêng.
- Không tìm thấy thay đổi chính sách nhãn AI sau 2024 (có thể đã có; cần kiểm tra Help Center 10/2026).

## 2. TTS / giọng đọc tiếng Việt

### Takeaway
Lựa chọn chia ba nhóm: (1) **ElevenLabs** — cảm xúc/nhấn nhá tốt, clone giọng, nhưng tiếng Việt đọc dài đôi khi ngắt sai, đắt nhất; (2) **nhà cung cấp Việt (Vbee, FPT.AI, Viettel AI, Zalo AI)** — xử lý tiếng Việt và giọng vùng miền tốt, có API, nhưng giá công khai khó tìm; (3) **cloud lớn (Google Chirp 3 HD/Gemini TTS, Azure)** — rẻ hoặc gần như miễn phí ở khối lượng một kênh (vài trăm nghìn ký tự/tháng), API ổn định, nhưng cần xác minh giọng vi-VN của từng dòng.

### Cited Findings
**ElevenLabs** (giá thay đổi trong 2026, các nguồn mâu thuẫn)
- Free 10.000 credit/tháng, không có quyền thương mại; Starter $5–6/tháng 30.000 credit, có quyền thương mại + instant voice clone; Creator $22/tháng (~100–121k credit; tháng đầu $11), gói thấp nhất có Professional Voice Cloning; Pro $99 (500–600k credit); Scale $299 hoặc $330; Business $990 hoặc $1.320 — [BigVU](https://bigvu.tv/blog/elevenlabs-pricing-2026-plans-credits-commercial-rights-api-costs/); [Fora Soft (05/2026)](https://www.forasoft.com/learn/ai-for-video-engineering/articles-ai/elevenlabs-pricing-voice-cloning-no-fakes-act); [Smallest.ai](https://smallest.ai/blog/elevenlabs-pricing-plans-cost-what-you-get-in-2026)
- 1 credit = 1 ký tự với Multilingual v2; ~1.000 credit ≈ 1 phút audio; Flash/Turbo ~0,5 credit/ký tự; trả năm tiết kiệm ~17% — [HappyRobot](https://www.happyrobot.ai/hub/elevenlabs-pricing); [BigVU](https://bigvu.tv/blog/elevenlabs-pricing-2026-plans-credits-commercial-rights-api-costs/)
- Đánh giá tiếng Việt: giọng tự nhiên, kiểm soát cảm xúc/nhấn nhá tốt hơn Minimax; nhưng đọc tiếng Việt dài vẫn có lỗi ngắt chữ/nhịp; gói free hay lỗi khi đọc dài — [Viettablet](https://www.viettablet.com/giong-doc-ai); [FPT Shop](https://fptshop.com.vn/tin-tuc/danh-gia/elevenlabs-ai-158486)

**Vbee**
- Nhà cung cấp TTS Việt, >200 giọng, 50 ngôn ngữ, giọng vùng miền, cảm xúc tự nhiên; khách hàng Google Cloud, người dùng active tăng ~20%/tháng — [Google Cloud case study](https://cloud.google.com/customers/vbee?hl=ja); [MISA AMIS](https://amis.misa.vn/203941/cong-cu-ai-chuyen-van-ban-thanh-giong-noi/)
- Được đánh giá "thuần Việt", xử lý ngôn ngữ tiếng Việt rất tốt — [Viettablet](https://www.viettablet.com/giong-doc-ai)
- App "Chữ thành lời" (Vbee) trên App Store VN — [App Store](https://apps.apple.com/vn/app/id6479488252)

**FPT.AI**
- API tổng hợp tiếng nói tiếng Việt, có mở dùng thử miễn phí; chỉnh tốc độ, cao độ; giọng 3 miền — [FPT.AI docs](https://docs.fpt.ai/docs/en/speech/documentation/text-to-speech); [MISA AMIS](https://amis.misa.vn/203941/cong-cu-ai-chuyen-van-ban-thanh-giong-noi/)

**Viettel AI**
- Bài 06/2024: 16 giọng tiếng Việt, tối đa 10 triệu ký tự/tháng; một số giọng miễn phí, gói khối lượng lớn "chi phí hợp lý" (không công bố giá) — [Viettel AI](https://viettelai.vn/en/tin-tuc/nghe-giong-ai-cua-viettel-lieu-ban-co-the-phan-biet-duoc-giong-may-hay-giong-nguoi)
- Bài 03/2025: 50.000 ký tự miễn phí trong 1 tháng từ khi đăng ký; kết nối qua API — [Viettel AI](https://viettelai.vn/en/tin-tuc/top-5-phan-mem-doc-van-ban-thanh-giong-noi-mien-phi); hướng dẫn cũ: bản thử giới hạn 300 ký tự/lần — [Quantrimang](https://quantrimang.com/cach-chuyen-van-ban-thanh-giong-noi-text-to-speech-cua-viettel-164030)

**Google Cloud TTS**
- Chirp 3: HD: 1 triệu ký tự đầu miễn phí, sau đó $30/1 triệu ký tự; instant custom voice $60/1M, không có free tier. Gemini TTS tính theo token: 2.5 Flash TTS $0,50/1M token text vào + $10/1M token audio ra; 2.5 Pro TTS $1/$20; Gemini 3.1 Flash TTS (preview) $1/$20; 25 token audio/giây — [Google Cloud pricing](https://cloud.google.com/text-to-speech/pricing/?authuser=2)

**Azure**
- Neural voice ~$15/1M ký tự, custom ~$24/1M, free 5 triệu ký tự/tháng (nguồn bên thứ ba, chưa xác nhận cho vi-VN) — [SpeechActors](https://speechactors.com/article/microsoft-azure-pricing-and-plans)

**CapCut** có 269 giọng TTS trong app (không phải API) — [AI Indigo](https://aiindigo.com/blog/capcut-review-2026-the-standard-for-short-form-content)

### Inferences
- Khối lượng ước tính (16 video dài × ~10 phút + 45 Shorts × ~45s ≈ 195 phút audio/tháng; giả định ~900–1.000 ký tự tiếng Việt/phút) ≈ **~200.000 ký tự/tháng**:
  - ElevenLabs Multilingual v2: ~200k credit → cần **Pro $99**; nếu dùng Flash/Turbo (~100k credit) → **Creator $22** vừa đủ, nhưng chất lượng tiếng Việt của Flash cần nghe thử.
  - Google Chirp 3 HD: dưới 1M ký tự free → **~$0** (nếu có giọng vi-VN đạt yêu cầu). Gemini 2.5 Flash TTS: 195 phút × 60 × 25 token = ~292k token audio → ~$3/tháng.
  - Azure: nằm trong free 5M ký tự → ~$0 (nếu áp dụng cho vi-VN).
- Đề xuất test: cùng một đoạn script 2–3 phút (có số liệu, tên riêng tiếng Anh như "Fed", "S&P 500", "VN-Index") qua ElevenLabs v2/v3, Vbee, FPT.AI, Viettel, Google Chirp 3 HD/Gemini TTS, Azure HoaiMy/NamMinh → chấm điểm mù. Tài chính có nhiều số, ký hiệu %, viết tắt — chuẩn hoá văn bản (number normalization) trước TTS là bước bắt buộc trong pipeline.
- Voice clone giọng chủ kênh (ElevenLabs Creator+) tạo "danh tính" riêng, giúp giảm cảm giác "kênh AI hàng loạt".

### Gaps
- Không tìm được bảng giá API công khai của Vbee, FPT.AI, Viettel AI, Zalo AI (Zalo AI hoàn toàn không có thông tin trong kết quả) — cần vào trang giá/đăng ký trực tiếp.
- Chưa xác nhận Chirp 3 HD / Gemini TTS / OpenAI TTS có giọng vi-VN chất lượng nào và giá Azure riêng cho vi-VN (HoaiMyNeural, NamMinhNeural) `[CẦN XÁC MINH 2026-10]`.
- Không có benchmark khách quan về chất lượng tiếng Việt giữa các nhà cung cấp; các bài VN là listicle/quảng bá.

## 3. Viết script, nghiên cứu/fact-check, dịch

### Takeaway
LLM (Claude/GPT/Gemini) là bước rẻ nhất trong pipeline; rủi ro chính là **sai số liệu tài chính** và vi phạm "lời khuyên tài chính sai lệch". Script nên qua bước nghiên cứu có nguồn + fact-check + người duyệt trước khi TTS. Cách làm phổ biến trong pipeline n8n là LLM viết script từ transcript các video top hoặc từ prompt, rồi log vào Google Sheets để duyệt.

### Cited Findings
- Template n8n miễn phí soạn script từ transcript video hiệu quả cao, log vào Google Sheets (chỉ phần script, không voice/upload) — [OutlierKit (07/2026)](https://outlierkit.com/resources/n8n-faceless-youtube-template/)
- Pipeline mẫu dùng ChatGPT cho script trong n8n — [Creatomate](https://creatomate.com/blog/how-to-auto-generate-faceless-shorts-with-chatgpt-and-n8n); dịch vụ Upwork dùng Gemini/Vertex AI cho script + voice — [Upwork](https://www.upwork.com/services/product/video-audio-n8n-youtube-video-automation-system-with-ai-voicing-and-auto-upload-2002820730681834049)
- YouTube không yêu cầu khai AI khi AI chỉ dùng viết script/ý tưởng — [YouTube Blog](https://blog.youtube/news-and-events/disclosing-ai-generated-content)

### Inferences
- Quy trình gợi ý: (1) LLM có web search thu thập nguồn (báo cáo tài chính, Bloomberg/Reuters, CafeF/VnExpress Kinh doanh) → (2) outline + script tiếng Việt (viết thẳng tiếng Việt thay vì dịch từ Anh để giọng văn tự nhiên) → (3) LLM thứ hai fact-check từng con số với nguồn → (4) người duyệt → (5) chuẩn hoá văn bản cho TTS. Với chuyện doanh nghiệp quốc tế, có thể tổng hợp nhiều nguồn tiếng Anh rồi viết tiếng Việt; tránh dịch nguyên văn video của kênh khác (rủi ro bản quyền/reup).
- Chi phí LLM cho ~16 script dài + 45 script Shorts/tháng nhiều khả năng chỉ vài USD đến vài chục USD qua API, hoặc gói chat ~$20/tháng `[CẦN XÁC MINH 2026-10]` (chưa tra giá token trong lượt này).

### Gaps
- Chưa tra giá API hiện tại của Claude/GPT/Gemini (10/2026) và chưa có so sánh chất lượng văn tiếng Việt giữa các model.

## 4. Hình ảnh & video: stock, ảnh AI, video AI, biểu đồ

### Takeaway
Stock footage (Envato ~$16,5/tháng hoặc Storyblocks $20–40/tháng) là nền rẻ nhất cho explainer; ảnh AI dùng cho minh hoạ/thumbnail; video AI (Veo 3.1, Kling, Hailuo, Runway) giờ có giá **~$0,04–0,15/giây** ở mức Fast/Turbo và **~$0,40/giây** ở Veo 3.1 Standard có audio — đủ rẻ để làm b-roll điểm nhấn, chưa đủ rẻ để phủ toàn bộ video 15 phút ở chất lượng cao nhất.

### Cited Findings
**Stock**
- Storyblocks 2026: Basic/Plus/Max $20/$30/$40 mỗi tháng (Basic 5 lượt tải/tháng, Max không giới hạn); bài cũ hơn ghi $25/$35/$50; Storyblocks quảng cáo bảo hiểm pháp lý tới $20.000 — [ToolSurf](https://www.toolsurf.com/storyblocks-pricing-2026-plans-costs-cheapest-alternative-2026-plans-features-best-deals-compared/); [GTM Directory](https://thegtmdirectory.com/compare/envato-elements-vs-storyblocks)
- Envato Elements ~$16,50/tháng (trả năm), tải không giới hạn; license gắn với từng lượt tải đã đăng ký, giữ nguyên sau khi huỷ; than phiền lớn nhất 2025–2026 là **nhạc Envato bị Content ID claim** dù có license — [GTM Directory](https://thegtmdirectory.com/compare/envato-elements-vs-storyblocks); [Checkthat.ai](https://checkthat.ai/brands/envato/reviews)

**Video AI (giá API, nguồn tổng hợp 05–08/2026, chưa phải bảng giá gốc)**
- Veo 3.1: Lite $0,05/s (720p), $0,08/s (1080p); Fast ~$0,10–0,12/s; Standard có audio $0,40/s; 4K $0,60/s — [InVideo (08/2026)](https://invideo.io/blog/ai-video-model-pricing); [Apiframe](https://apiframe.ai/blog/ai-video-api-pricing-2026)
- Kling: API chính thức bán gói tài nguyên trả trước, không tính theo giây; qua reseller ~$0,075–0,14/s; Kling 3.0 Turbo ~¥0,8/s (~$0,11) 720p — [CloudZero](https://www.cloudzero.com/blog/kling-ai-pricing/); [Rangy](https://rangy.ai/blog/ai-video-pricing-explained)
- Hailuo (MiniMax): MiniMax-H3 $0,13/s ở 2K (~$0,08/s ở 768p); Hailuo 2.3 qua reseller ~$0,01/s (512p), ~$0,04/s (768p), ~$0,08/s (1080p) — [Aireiter](https://aireiter.com/de/blog/video-generation-api-pricing-billing-dimensions); mâu thuẫn giữa các nguồn
- Runway: credit $0,01; Gen-4 Turbo 5 credit/s ($0,05/s); Gen-4.5 12 credit/s ($0,12/s); Veo 3.1 qua Runway 20–40 credit/s (~$0,40/s có audio) — [InVideo](https://invideo.io/blog/ai-video-model-pricing)
- Cảnh báo: giá reseller có thể cao gấp 2–3 lần giá chính thức — [Apiframe](https://apiframe.ai/blog/ai-video-api-pricing-2026)
- Sora 2 đã được dùng trong pipeline faceless tự động với n8n — [GrowwStacks](https://growwstacks.com/blog/automated-faceless-youtube-channel-sora2-n8n/)

**AI avatar**
- HeyGen API là sản phẩm trả theo dùng riêng, ví nạp từ $5, ngừng tặng credit API miễn phí từ 02/2026; Avatar IV qua API ~6 credit/phút, credit ~$0,50–0,99; gói web Creator $29, Pro $49 hoặc $99 (nguồn mâu thuẫn), Business $149 + $20/seat — [DIYAI](https://diyai.io/ai-tools/video-generation/heygen-pricing/); [Creatify](https://creatify.ai/blog/heygen-pricing-(2026)-plans-and-what-you-ll-actually-pay); [Arcade](https://www.arcade.software/post/heygen-pricing)

**Biểu đồ/hoạt hoạ dữ liệu**
- Remotion (video bằng React) miễn phí cho cá nhân/công ty ≤3 người kể cả thương mại; gói công ty từ ~$100/tháng hoặc ~$0,01/render (nguồn mâu thuẫn); cần Node.js 18+ và FFmpeg — [Remotion license](https://remotion.dev/docs/license); [Remotion blog](https://www.remotion.dev/blog/company-licenses); [Tooliverse](https://tooliverse.ai/tools/remotion)

### Inferences
- Kịch bản b-roll AI: 2 phút video AI/video dài × 16 video = 1.920 giây/tháng → ~$77–230/tháng ở mức $0,04–0,12/s (Hailuo/Kling/Veo Fast/Runway Turbo); ~$770/tháng nếu dùng Veo 3.1 Standard có audio. Phủ toàn bộ 10 phút/video bằng video AI → ~$380–1.150/tháng ở mức Fast — chỉ hợp lý cho tier premium.
- Avatar HeyGen: ~6 credit/phút × $0,5–0,99 ≈ **$3–6/phút**; 160 phút/tháng ≈ $480–950 → đắt hơn nhiều so với stock + TTS, và chưa xác nhận chất lượng lip-sync tiếng Việt.
- Biểu đồ tài chính: Remotion (miễn phí với team ≤3 người) hoặc matplotlib/Plotly xuất frame + ffmpeg là lựa chọn tự động hoá tốt nhất; biểu đồ dữ liệu thật vừa tăng giá trị vừa giảm rủi ro "inauthentic".
- Nhạc nền: nên dùng YouTube Audio Library hoặc nguồn có cam kết không claim; cẩn trọng nhạc Envato vì Content ID.

### Gaps
- Chưa có giá chính thức Midjourney, Flux, Ideogram, Imagen, Pexels API (Pexels miễn phí — chưa xác minh điều khoản API trong lượt này) `[CẦN XÁC MINH 2026-10]`.
- Chưa xác nhận HeyGen/Synthesia/D-ID có avatar/giọng tiếng Việt và chất lượng lip-sync tiếng Việt.
- Giá video AI chủ yếu từ aggregator; cần đối chiếu Google Vertex AI, Kling, MiniMax, Runway pricing pages.

## 5. Dựng/ghép video tự động (assembly) & phụ đề

### Takeaway
Ba hướng: (a) **tự code** (ffmpeg/MoviePy/Remotion) — rẻ nhất, linh hoạt nhất, cần kỹ năng; (b) **render API theo template JSON** (Shotstack, Creatomate, JSON2Video) — ~$0,07–0,40/phút render, cắm thẳng vào n8n/Make; (c) **app "text-to-video" all-in-one** (InVideo AI, Pictory, Fliki) — nhanh nhưng output giống nhau, rủi ro "template hoá". CapCut không có API công khai (chỉ template trong app), nên không phù hợp cho L3.

### Cited Findings
- Shotstack: 1 credit = 1 phút render bất kể độ phân giải (4K = 720p), tính theo giây; pay-as-you-go $0,40/phút (gói 25 credit) xuống $0,07/phút (gói 10.000 credit); hết số dư thì ngừng render — [Wireflow](https://www.wireflow.ai/blog/shotstack-pricing); [Shotstack](https://shotstack.io/vs/creatomate-alternatives/)
- Creatomate: tính credit theo độ phân giải/fps, ~14 credit/phút 720p 25fps; gói Essential được ghi $29/$39/$41/$54 tuỳ nguồn (2.000 credit); Growth ~$99/tháng 10.000 credit — [Submagic](https://www.submagic.co/blog/creatomate-pricing); [Toolradar](https://toolradar.com/tools/creatomate/pricing)
- JSON2Video Professional $49,95/tháng gồm 200 phút Full HD, hết credit thì API dừng, không phí vượt (tuyên bố của vendor) — [JSON2Video](https://json2video.com/how-to/creatomate-alternative/)
- Creatomate có hướng dẫn chính thức n8n + ChatGPT + ElevenLabs → Short có phụ đề động, cảnh báo email khi render lỗi — [Creatomate](https://creatomate.com/blog/how-to-auto-generate-faceless-shorts-with-chatgpt-and-n8n)
- Remotion: miễn phí cho ≤3 người; Lambda render có chi phí riêng cần theo dõi — [Remotion](https://remotion.dev/docs/license); [Tooliverse](https://tooliverse.ai/tools/remotion)
- CapCut: AI caption, auto-reframe, script-to-video, voiceover, caption 130+ ngôn ngữ, avatar — đều là công cụ trong app; không tìm thấy API template/render công khai — [FrankX](https://frankx.ai/blog/ultimate-capcut-workflow-2026); [AI Indigo](https://aiindigo.com/blog/capcut-review-2026-the-standard-for-short-form-content); template faceless qua Pippit — [Pippit](https://pippit.capcut.com/templates/faceless-by-serotonin-capcut-template)

### Inferences
- Khối lượng ~195 phút render/tháng: Shotstack ~$14 (mức $0,07) đến ~$78 (mức $0,40); JSON2Video $49,95 (200 phút, vừa khít); Creatomate ~2.700 credit (720p) → cần Growth ~$99 (1080p tốn credit hơn). Tự code ffmpeg/MoviePy/Remotion trên máy/VPS → ~$0 phí license + chi phí máy.
- Phụ đề tiếng Việt: có thể tạo bằng Whisper/forced alignment từ chính file TTS (biết sẵn văn bản) → burn-in bằng ffmpeg/Remotion; Submagic/Opus Clip tiện cho Shorts nhưng thêm chi phí thuê bao.
- Shorts: cắt từ video dài bằng script (đã có timestamp từng đoạn) rẻ hơn Opus Clip; Opus Clip phù hợp khi cắt từ video không có cấu trúc.

### Gaps
- Chưa tra giá InVideo AI, Pictory, Fliki, Opus Clip, Submagic (10/2026) và chất lượng tiếng Việt của chúng `[CẦN XÁC MINH 2026-10]`.
- Chưa xác nhận CapCut/Pippit có API doanh nghiệp hay không.

## 6. Thumbnail & thử nghiệm thumbnail

### Takeaway
YouTube "Test & compare" cho thử tối đa 3 thumbnail (và từ 07/2025 bắt đầu thử cả tiêu đề), chọn thắng theo **watch time share** chứ không theo CTR. Thumbnail có thể tạo bằng ảnh AI + template Canva; Canva có MCP/API (Autofill brand template) để tự động hoá.

### Cited Findings
- Test & Compare live giữa 2024, tối đa 3 thumbnail; 07/2025 YouTube bắt đầu thử nghiệm test tiêu đề cho một nhóm nhỏ creator; người thắng chọn theo watch time share — [Social Samosa](https://www.socialsamosa.com/news-2/youtube-thumbnail-testing-tool-more-creators-9498934); [Social Media Today](https://www.socialmediatoday.com/news/youtube-adds-title-testing-youtube-studio/753015/); [TubeFilter](https://www.tubefilter.com/?p=187324)
- Mở rộng tới mọi creator YPP (Creator Handbook) / tới mọi creator đủ điều kiện toàn cầu 12/2025 (Vidanalyze) — chưa có thông báo chính thức xác nhận — [Creator Handbook](https://www.creatorhandbook.net/youtube-expands-a-b-testing-for-titles-and-thumbnails/); [Vidanalyze](https://vidanalyze.com/news/youtube-ab-testing-for-titles-thumbnails-2026-guide)

### Inferences
- Pipeline thumbnail tự động: LLM đề xuất 3 concept → ảnh AI (nhân vật/vật thể, KHÔNG dùng mặt người thật khi gây hiểu nhầm) → Canva brand template autofill (chữ tiếng Việt to, 3–5 từ) → upload 3 biến thể vào Test & compare (bước này hiện làm tay trong Studio; chưa thấy API cho Test & compare).
- Thumbnail tĩnh đơn lẻ có thể set qua API (`thumbnails.set`), nhưng A/B testing là thao tác Studio.

### Gaps
- Chưa xác nhận Test & compare có trong YouTube Data API không (khả năng cao là không) `[CẦN XÁC MINH 2026-10]`; chưa tra giá Midjourney/Ideogram cho thumbnail.

## 7. Điều phối (orchestration), YouTube Data API & stack thực tế

### Takeaway
Stack "faceless automation" phổ biến 2026: **n8n (lịch) → LLM viết script → TTS (ElevenLabs) → renderer (Creatomate/Shotstack) → upload YouTube (node n8n hoặc thủ công) / lưu Drive để duyệt**. Hạn mức YouTube Data API mặc định 10.000 unit/ngày; chi phí `videos.insert` có thể đã giảm từ 1.600 xuống ~100 unit (12/2025) — chưa xác minh được trên trang Google. Với 1–4 upload/ngày, cả hai mức đều đủ.

### Cited Findings
- Pattern chung: scheduler n8n + LLM + TTS (ElevenLabs) + renderer (Creatomate/Shotstack) + node upload YouTube hoặc upload tay — [Creatomate](https://creatomate.com/blog/how-to-auto-generate-faceless-shorts-with-chatgpt-and-n8n); [OutlierKit](https://outlierkit.com/resources/n8n-faceless-youtube-template/); [GrowwStacks](https://growwstacks.com/blog/build-24-7-faceless-youtube-ai-agent-n8n/)
- Có dịch vụ freelance đóng gói sẵn hệ thống n8n "AI voicing + auto upload" — [Upwork](https://www.upwork.com/services/product/video-audio-n8n-youtube-video-automation-system-with-ai-voicing-and-auto-upload-2002820730681834049)
- Quota mặc định 10.000 unit/ngày, reset nửa đêm giờ Pacific, không mua thêm được — chỉ xin qua form mở rộng; đọc (`videos.list`) 1 unit, `search.list` 100 unit, ghi thường 50 unit — [Phyllo](https://www.getphyllo.com/post/is-the-youtube-api-free-in-2026-quota-limits-costs-when-to-pay); [ChannelCrawler (03/2026)](https://channelcrawler.com/insights/youtube-api-daily-limit-quotas-costs-and-how-to-scale-beyond-10000-units-channelcrawler)
- **Mâu thuẫn**: nhiều nguồn 2026 nói Google giảm `videos.insert` từ ~1.600 xuống ~100 unit ngày 04/12/2025 (theo Revision History); trang quota-cost của Google mà công cụ tìm kiếm trả về vẫn ghi 1.600 (có thể bản cũ). Một tóm tắt bên thứ ba còn nói có bucket riêng 100 lượt `videos.insert`/ngày — [OutlierKit](https://outlierkit.com/resources/youtube-api-quota/); [Google determine_quota_cost](https://developers.google.com/youtube/v3/determine_quota_cost) (không truy cập được trực tiếp)

### Inferences
- Lịch đăng mục tiêu (12–20 video dài + 30–60 Shorts/tháng ≈ 2–3 upload/ngày): ở mức 1.600 unit/upload → tối đa ~6 upload/ngày/project → đủ; mức 100 unit thì dư nhiều.
- Lựa chọn điều phối: **n8n self-host** (rẻ, có node YouTube, hợp chủ kênh ở VN dùng VPS) > Make/Zapier (tính theo operation, đắt khi pipeline nhiều bước) ; **Python** cho các bước nặng (TTS chunking, ffmpeg, chart) gọi từ n8n. Khuyến nghị: upload ở chế độ private/scheduled + bước duyệt người (đọc lại số liệu) trước khi public — vừa an toàn chính sách vừa bảo vệ uy tín kênh tài chính.
- Theo CLAUDE.md của repo: không xây automation trước khi có test chứng minh tín hiệu → giai đoạn đầu nên L1–L2 (script bán tự động), chỉ đẩy L3 sau khi format thắng.

### Gaps
- Chưa xác minh trực tiếp con số `videos.insert` hiện hành và quy định "API project chưa qua audit chỉ được upload private" (theo hiểu biết trước đây: các project tạo sau 28/07/2020 chưa audit thì video upload bị khoá private) `[CẦN XÁC MINH 2026-10]` — rất quan trọng cho tự động upload; nếu đúng cần nộp YouTube API audit hoặc upload thủ công/qua Studio.
- Chưa tra giá n8n Cloud, Make, Zapier (10/2026).

## 8. Ước tính chi phí theo 3 tier (12–20 video dài + 30–60 Shorts/tháng)

### Takeaway
Ước tính (suy luận từ đơn giá ở các mục trên, giả định trung bình 16 video dài × 10 phút + 45 Shorts × 45s ≈ 195 phút/tháng, ~200k ký tự TTS): **Budget ~$20–60/tháng (~$0,3–1/video)**, **Standard ~$150–300/tháng (~$2,5–5/video)**, **Premium ~$600–1.500+/tháng (~$10–25+/video)**. Chi phí lớn nhất ở tier cao là video AI và avatar, không phải TTS hay LLM.

### Cited Findings
- Đơn giá đầu vào: ElevenLabs Creator $22 / Pro $99 — [BigVU](https://bigvu.tv/blog/elevenlabs-pricing-2026-plans-credits-commercial-rights-api-costs/); Google Chirp 3 HD 1M ký tự free rồi $30/1M — [Google Cloud](https://cloud.google.com/text-to-speech/pricing/?authuser=2); Envato ~$16,50 — [GTM Directory](https://thegtmdirectory.com/compare/envato-elements-vs-storyblocks); Storyblocks $20–40 — [ToolSurf](https://www.toolsurf.com/storyblocks-pricing-2026-plans-costs-cheapest-alternative-2026-plans-features-best-deals-compared/); Shotstack $0,07–0,40/phút, JSON2Video $49,95/200 phút, Creatomate Growth ~$99 — [Wireflow](https://www.wireflow.ai/blog/shotstack-pricing); [JSON2Video](https://json2video.com/how-to/creatomate-alternative/); [Submagic](https://www.submagic.co/blog/creatomate-pricing); video AI $0,04–0,40/s — [InVideo](https://invideo.io/blog/ai-video-model-pricing); HeyGen ~$3–6/phút — [DIYAI](https://diyai.io/ai-tools/video-generation/heygen-pricing/); Remotion free ≤3 người — [Remotion](https://remotion.dev/docs/license)

### Inferences
| Hạng mục / tháng | Budget | Standard | Premium |
|---|---|---|---|
| Script (LLM) | gói chat có sẵn / API ~$5 `[CẦN XÁC MINH]` | API ~$10–30 `[CẦN XÁC MINH]` | ~$30–60 (thêm research model) `[CẦN XÁC MINH]` |
| TTS | Google Chirp 3 HD/Azure free tier hoặc Viettel/FPT gói thấp: ~$0–10 | ElevenLabs Creator $22 (Flash) hoặc Pro $99 (v2) | ElevenLabs Pro $99 + Professional Voice Clone |
| Hình ảnh | Pexels/Pixabay miễn phí + ảnh AI rẻ: ~$0–10 | Envato $16,5 hoặc Storyblocks $30 + ảnh AI ~$10–30 | Storyblocks Max $40 + ảnh AI ~$30 |
| Video AI b-roll | 0 | ~1 phút/video dài × 16 = 960s × ~$0,05–0,10 ≈ $50–100 | ~3–5 phút/video × 16 ≈ 2.900–4.800s × $0,10–0,40 ≈ $290–1.900 |
| Avatar (tuỳ chọn) | 0 | 0 | intro/outro 1 phút × 16 × $3–6 ≈ $50–100 |
| Render/dựng | ffmpeg/MoviePy/Remotion tự host: $0 | JSON2Video $49,95 hoặc Shotstack ~$15–80 | Creatomate Growth ~$99 hoặc Remotion + Lambda |
| Điều phối | n8n self-host trên VPS ~$5–10 `[CẦN XÁC MINH]` | như budget | n8n Cloud/Make `[CẦN XÁC MINH]` |
| **Tổng ước tính** | **~$20–60** | **~$150–300** | **~$600–2.300** |
| Mỗi video dài (Shorts tính gộp) | ~$1–4 | ~$9–19 | ~$40–140 |

(Lưu ý: hàng "mỗi video" chia tổng cho 16 video dài vì Shorts chủ yếu cắt từ video dài; chi phí thực/Short riêng lẻ rất thấp.)
- Mức tự động hoá theo tier: Budget đạt L2 (cần người dựng/duyệt nhiều hơn), Standard có thể đạt L2–L3 với bước duyệt người, Premium L3 nhưng chi phí tăng chủ yếu do video AI.
- Khuyến nghị bắt đầu ở Budget/Standard thấp để chạy test format (theo quy trình repo), chỉ tăng ngân sách video AI khi có dữ liệu retention.

### Gaps
- Chưa có số liệu chi phí thực tế từ kênh tài chính AI tiếng Việt đang hoạt động; tất cả là ước tính từ đơn giá.
- Chưa có giá LLM, ảnh AI, n8n/Make/Zapier, Opus Clip/Submagic để chốt con số chính xác.
- Các đơn giá chính (ElevenLabs, Creatomate, video AI) có mâu thuẫn giữa nguồn — cần kiểm tra trang giá chính thức trước khi lập ngân sách.
