# G-Labs Studio (duckspace.net / duckmartians): ghi chú nghiên cứu

> Ngày nghiên cứu: 2026-10-10 · Người làm: Claude (subagent) · Dự án yêu cầu: 01-youtube-ai-finance (có thể dùng sau cho 02-tiktokshop-vn-giadung)
> Phạm vi: đánh giá có nguồn để chủ repo quyết định có mua/dùng G-Labs Studio hay không.
>
> **Giới hạn khi nghiên cứu:** proxy chặn `duckspace.net`, `duckmartians.info`, YouTube, Chrome Web Store,
> `policies.google.com`, `ai.google.dev`. Vì vậy giá và chính sách hoàn tiền của người bán chỉ lấy được
> **qua đoạn trích của công cụ tìm kiếm**, không đọc trực tiếp được trang. Nguồn đọc trực tiếp được là **hai repo GitHub
> công khai của nhà phát triển** (đã clone về và đọc README, tài liệu Webhook, mã nguồn extension Auth Helper).
>
> Nhãn dùng trong file:
> - **[ĐÃ KIỂM]**: tôi đọc trực tiếp từ nguồn gốc (repo, mã nguồn).
> - **[NGƯỜI BÁN NÓI]**: lời quảng cáo/tài liệu của người bán, chưa kiểm chứng độc lập.
> - **[SUY LUẬN]**: nhận định của tôi.
> - **[CẦN XÁC MINH]**: chưa kiểm chứng được.

---

## 0. Kết luận nhanh (TL;DR)

1. G-Labs Studio là **app desktop đóng nguồn** (Windows/macOS, không ký số) do **Đặng Minh Đức ("duckmartians")**,
   một nhà phát triển cá nhân ở Việt Nam, làm ra. Nó **tự động hoá giao diện web/API nội bộ** của Google Flow (Veo 3.1, Nano Banana),
   Google Vids, Google Pics, ChatGPT (GPT Image 2), Meta Vibes và Grok, **bằng chính tài khoản đã đăng nhập (cookie/phiên) của người dùng**.
   App **không dùng API chính thức với API key**. [ĐÃ KIỂM]
2. Extension đi kèm ("Auth Helper") **đọc cookie, chặn header request, và tạo token reCAPTCHA Enterprise trong tab Flow** để đưa cho app desktop.
   Như vậy app lách lớp chống bot của Google. Mã extension cố tình đặt tên đánh lạc hướng ("theme", "font", "analytics") và mã hoá XOR
   dữ liệu trao đổi với app. [ĐÃ KIỂM: đọc mã nguồn]
3. Giá phần mềm rẻ: Basic miễn phí, **Plus khoảng 5 USD/tháng, Max khoảng 10 USD/tháng**, hoàn tiền trong 24 giờ.
   [NGƯỜI BÁN NÓI, lấy qua đoạn trích tìm kiếm của duckspace.net, CẦN XÁC MINH khi mở trang]. **Chi phí thật nằm ở tài khoản AI**
   (Google AI Pro khoảng 19,99 USD/tháng, tức 1.000 credit; Ultra 99,99 đến 199,99 USD/tháng).
4. **Rủi ro chính:**
   - Vi phạm điều khoản của Google (tự động hoá sản phẩm tiêu dùng, lách bảo vệ chống lạm dụng), có thể bị khoá tài khoản Google.
   - Phải giao cookie Google cho phần mềm đóng nguồn không ký số. Nếu dùng **cùng tài khoản Google sở hữu kênh YouTube**, rủi ro bảo mật rất cao.
   - App có tính năng **xoá logo Gemini/Veo**, dễ va chạm với yêu cầu minh bạch nội dung AI.
5. **Không hợp với kênh 01**, vì phong cách kênh là minh hoạ cộng biểu đồ số liệu thật, ngân sách 20–60 USD/tháng, và rủi ro inauthentic content.
   Veo chỉ cho clip 4–8 giây. Một video 10 phút dựng toàn bằng Veo cần khoảng 75 clip cộng phần làm lại, **vượt xa hạn mức AI Pro**.
   Lõi của video tài chính (biểu đồ số liệu thật, lời thoại tiếng Việt) thì G-Labs không làm. [SUY LUẬN]
6. **Khuyến nghị:** **không mua cho kênh 01 lúc này**. Nếu muốn thử Veo làm B-roll/hook, dùng Flow **thủ công** hoặc **Gemini API chính thức**
   (Veo 3.1 Lite 0,05 USD/giây, Fast 0,10 USD/giây ở 720p) với ngân sách giới hạn. Nếu một ngày vẫn muốn thử G-Labs, chỉ chạy trên **tài khoản Google phụ, tách biệt hoàn toàn**,
   trên máy/VM riêng, **tuyệt đối không** dùng tài khoản sở hữu kênh YouTube hay AdSense. Với dự án 02 (TikTok Shop), xem lại sau khi có test thắng (mục 6.4).

---

## 1. Nó là gì?

### 1.1 Nhà phát triển và kênh bán
| Mục | Thông tin | Nhãn / nguồn |
|---|---|---|
| Nhà phát triển | **Đặng Minh Đức** (GitHub `duckmartians`, commit với tên "Minh Duc"), tự giới thiệu là "Duck Martians AI Labs", "AI researcher & creative technologist" | Trang duckmartians.info qua đoạn trích tìm kiếm; lịch sử commit [ĐÃ KIỂM] |
| Website bán | `duckspace.net/g-labs-studio/` (+ `/en/`), `duckmartians.info/g-labs` | Đoạn trích tìm kiếm |
| Điều khoản | `duckspace.net/terms.html`, `privacy.html`, `refunds.html` (link trong README cũ) | [ĐÃ KIỂM] link trong README; **không đọc được nội dung** (proxy chặn) |
| Cộng đồng | Discord, Telegram, nhóm Zalo, playlist YouTube EN/VI | [ĐÃ KIỂM] link trong README G-Labs-Automation |
| Hệ sinh thái | Cùng tác giả còn có: G-Labs Story Machine, G-Labs Voice Studio, G-Labs Voiceover, G-Labs Video Downloader, G-Labs Music Forge, extension "Auto Flow x G-Labs Automation", "Auto Vibes" | GitHub + đoạn trích tìm kiếm |

### 1.2 Lịch sử phiên bản
- **G-Labs Automation**: repo tạo **2025-12-28**, 173 commit, khoảng 186 sao / 140 fork (lúc kiểm 2026-10-10). Lên tới v9.0.4 (khoảng 24/9/2026). [ĐÃ KIỂM]
- **G-Labs Studio**: bản đổi tên/viết lại. Repo tạo **2026-09-07**, 20 commit, 10 sao. Release v2.0.2 (21/9) đến **v3.0.1 (9/10/2026)**. [ĐÃ KIỂM]
  Tài khoản từ G-Labs Automation **không chuyển sang**, người dùng phải đăng nhập lại tất cả. [ĐÃ KIỂM, README]
- Repo **chỉ chứa README, tài liệu, ảnh chụp màn hình và file zip extension**. **Không có mã nguồn app.** Bộ cài phát qua GitHub Releases và Google Drive. [ĐÃ KIỂM]
- Release **không có release notes** ở repo Studio. Repo cũ có changelog chi tiết. [ĐÃ KIỂM qua trang Releases]
- Tần suất cập nhật **rất dày**: có tuần ra 3–4 bản. Changelog v8.0.8 (28/8/2026) ghi "Protocol synced with latest Flow… field by field", nghĩa là app gọi **giao thức nội bộ của Flow** và phải sửa theo mỗi khi Google đổi. [ĐÃ KIỂM]

### 1.3 Nền tảng và tính năng [NGƯỜI BÁN NÓI: README; ảnh chụp màn hình có trong repo]
- **HĐH:** Windows 10/11 64-bit (.exe), macOS Apple Silicon và Intel (.dmg).
  **Không ký số** với Microsoft/Apple. README hướng dẫn "More info → Run anyway" và chạy `xattr -dr com.apple.quarantine` để bỏ cảnh báo. [ĐÃ KIỂM]
- **Dịch vụ AI kết nối được:**
  - **Google Flow**, ảnh: Nano Banana Pro / 2 / 2 Lite (1K/2K/4K).
  - **Google Flow**, video: **Veo 3.1 Fast / Lite / Quality**, "Veo 3.1 Lite Lower Priority [0 credit]" (chỉ Ultra), **Omni Flash**.
  - **Google Vids**: text/ảnh/components → video, 3–10 giây.
  - **Google Pics**: text/ảnh → ảnh, tối đa 14 ảnh tham chiếu.
  - **ChatGPT GPT Image 2**, **Meta Vibes** (ảnh và video), **Grok Imagine** (ảnh và video 480p–1080p).
- **Không có** Kling, Hailuo, ElevenLabs hay TTS trong app này. TTS nằm ở app riêng là G-Labs Voiceover/Voice Studio. [ĐÃ KIỂM]
- **Tính năng chính:**
  - Chạy hàng loạt: dán prompt mỗi dòng một cái hoặc nhập .txt/Excel, chọn số luồng song song, có hàng đợi Run/Pause/Stop, tự thử lại và tự lưu.
  - **Xoay vòng nhiều tài khoản** ("Active: N accounts", round-robin, tự chuyển tài khoản khi lỗi quota/auth).
  - **Thư viện nhân vật** (`@name`: ảnh, giọng preset của Flow, ghi chú) để giữ nhân vật nhất quán.
  - **Scene Chain → Video**; **Workflow node**: prompt → ảnh → video → lấy frame cuối → video tiếp → Merge Video.
  - **Video Tools**: timeline (video + SRT + audio), slideshow ảnh khớp file .srt, cắt video, trích frame, **xoá logo Gemini ✦**.
  - Upscaler ảnh chạy local (Real-ESRGAN…).
  - **Webhook API** local (gói MAX), cổng 8765, cho n8n/Make/script/agent đẩy job vào.
  - 15 ngôn ngữ giao diện, tự cập nhật qua GitHub Releases.
- **Proxy HTTP/SOCKS** (README bản cũ). [NGƯỜI BÁN NÓI]

---

## 2. Cách kết nối với dịch vụ AI (quan trọng nhất)

### 2.1 Không dùng API chính thức, mà dùng phiên đăng nhập/cookie của tài khoản tiêu dùng [ĐÃ KIỂM]
Bằng chứng trong `WEBHOOK_INTEGRATION.en.md` của chính tác giả:
- "Generation runs on the app's **logged-in accounts**… Image/Video use the Google (Flow/Veo) accounts configured in the app."
- Google Vids/Pics: "a **dead cookie is renewed from the account's profile** first. An account whose **cookie** cannot be renewed is switched OFF."
  Có các mã lỗi `VIDS_COOKIE_EXPIRED`, `PICS_COOKIE_EXPIRED`, `Meta cookie expired`.
- ChatGPT: "Access tokens are refreshed automatically before each run". Mỗi tài khoản chạy 5 luồng.
- Changelog v9.0.2: "Auth browser (Built-in mode): Chrome monitored from launch… retries on a fresh profile". App **tự mở Chrome điều khiển qua CDP** để đăng nhập và lấy phiên.
- Changelog v6.0.5 (qua đoạn trích tìm kiếm): tài khoản hết phiên sẽ chuyển sang "expired", người dùng phải **"paste a fresh cookie"** hoặc đăng nhập lại.
- Mô tả trên GitHub: "Desktop app for batch AI image & video generation **with your own accounts**."

→ Kết luận: **cách 2 (tự động hoá trình duyệt/giao thức nội bộ bằng cookie tài khoản đã đăng nhập)**.
Không phải API key chính thức. Cũng **không thấy bằng chứng** người bán cung cấp/bán lại tài khoản dùng chung.
App khuyến khích **thêm nhiều tài khoản** để chạy nhanh hơn và cộng dồn quota ("add more accounts to run faster").

### 2.2 Extension "G-Labs Studio – Auth Helper" (v9.0.17, MV3): đọc mã nguồn trong repo [ĐÃ KIỂM]
File: `G-Labs_Studio_Auth_Helper.zip` trong repo. Cũng có trên Chrome Web Store, id `clhcjdjbcldkogahjfmcgfipmlilmkpg`.
Đoạn trích tìm kiếm ghi "4K+ users" và "chỉ giao tiếp với app G-Labs local".
- **Quyền:** `cookies`, `tabs`, `scripting`, `storage`, `webRequest`, `alarms`.
  Host: `*://*.google.com/*`, `grok.com`, `localhost`, `127.0.0.1`. Content script chạy trên `flow.google.com` và `grok.com`.
- **Việc extension làm:**
  1. Lấy cấu hình từ app local (`http://127.0.0.1:18923/sync/config`). Cấu hình gồm `recaptcha_url`, `recaptcha_ent_key`, `recaptcha_script_url`.
     Sau đó **chèn script reCAPTCHA Enterprise vào tab Flow và gọi `grecaptcha.enterprise.execute(...)` để tạo token**, rồi gửi token về app.
     Tức là app desktop gọi backend Flow trực tiếp và dùng trình duyệt thật của người dùng để **sinh token chống bot**.
  2. Với Grok: **nghe mọi request tới `grok.com/rest/*` và ghi lại header `Cookie`, `User-Agent`, `x-statsig-id`**.
     Kiểm tra cookie `sso`/`sso-rw`, tự mở tab `grok.com/imagine` ẩn.
  3. Nhận lệnh từ app để **xoá toàn bộ cookie** của một domain (domain đó do app cấu hình).
  4. Dữ liệu trao đổi với app được **mã hoá XOR (khoá 0x5A)**. Hàm và biến **đặt tên giả**: `_applyThemeUpdates`, `_onFontCached`, `_submitAnalytics`,
     trong khi thực chất xử lý cookie và token captcha.
- **Điểm trấn an:** trong mã extension, **mọi request đi ra chỉ tới `127.0.0.1`**, không thấy gửi cookie thẳng ra server lạ.
  **Nhưng** app desktop (đóng nguồn) nhận cookie/token và có kết nối tới server của người bán (đăng nhập license, "server config", thanh toán).
  **Không thể kiểm chứng** app có gửi cookie Google ra ngoài hay không. [CẦN XÁC MINH: chỉ kiểm được bằng phân tích lưu lượng/sandbox]
- [SUY LUẬN] Tên đặt giả và mã hoá không tự chứng minh mã độc. Đó là kỹ thuật phổ biến để **né việc Google phát hiện/review**.
  Nhưng nó cho thấy chính tác giả biết hành vi này không được Google chấp thuận.

### 2.3 Hệ quả với điều khoản (ToS)
- Điều khoản Google (bản sửa 2026, theo các trang theo dõi chính sách; **không đọc trực tiếp được** policies.google.com) cấm
  truy cập tự động trái với chỉ dẫn máy đọc được, và cấm lạm dụng/gây cản trở dịch vụ. [CẦN XÁC MINH: nguyên văn hiện hành]
- **Generative AI Prohibited Use Policy** của Google cấm "**circumvention of abuse protections or safety filters**"
  ("Do not compromise the security of others' or Google's services"). Vi phạm lặp lại có thể dẫn tới **hạn chế dùng AI tạo sinh hoặc khoá tài khoản Google**.
  Có kháng nghị. (support.google.com/gemini/answer/16625148, qua kết quả tìm kiếm 2026-10-10)
- [SUY LUẬN] Dùng extension sinh token reCAPTCHA cho request tự động, cộng xoay vòng nhiều tài khoản để vượt quota, **rất có thể** bị coi là lách bảo vệ chống lạm dụng.
  Grok (xAI), Meta, OpenAI cũng cấm truy cập tự động/scrape trong ToS tiêu dùng. [CẦN XÁC MINH: nguyên văn từng nền tảng]
- **Chưa tìm thấy báo cáo công khai** về đợt khoá tài khoản cụ thể vì dùng G-Labs. [CẦN XÁC MINH]
  Hãy hỏi trong Discord/Zalo của chính tool và các group MMO. Nhóm người dùng của tool có xu hướng không đăng chuyện bị khoá.

---

## 3. Giá

### 3.1 Phần mềm G-Labs Studio
| Gói | Giá | Ghi chú | Nhãn |
|---|---|---|---|
| Basic | Miễn phí | Mở khoá ít công cụ/model | Đoạn trích duckspace.net + README |
| Plus | **~5 USD/tháng** | Có Google Vids/Pics; changelog cũ ghi Plus giới hạn hàng đợi 10 task | Đoạn trích tìm kiếm duckspace.net/en/g-labs-studio, [CẦN XÁC MINH] |
| Max | **~10 USD/tháng** | Có Webhook API; kèm G-Labs Story Machine | Như trên, [CẦN XÁC MINH] |
| Team | Tăng theo số thiết bị | Mỗi tài khoản 1 máy cùng lúc; máy cũ bị đăng xuất trong 10 phút | README + changelog v9.0.0 |

- License theo **1 / 6 / 12 tháng, không tự gia hạn**. Nâng cấp giữa kỳ chỉ trả phần chênh lệch.
  Thanh toán **VietQR, PayPal, USDT**, mua trong app. README cảnh báo "mua ngoài app là lừa đảo".
- **Hoàn tiền:** "trong 24 giờ đầu sau khi thanh toán nếu license chưa dùng nhiều", người bán khuyên thử gói Basic trước.
  (Đoạn trích tìm kiếm từ trang duckspace; **chưa đọc** `refunds.html`, [CẦN XÁC MINH])
- App con G-Labs Voice Studio (cùng tác giả) ghi giá 100.000đ ≈ 5 USD/tháng, cho thấy mặt bằng giá của tác giả rất rẻ.

### 3.2 Chi phí thật: tài khoản AI bên dưới (tham khảo 10/2026, nhiều nguồn bên thứ ba, [CẦN XÁC MINH] trên trang Google)
| Gói | Giá | Credit Flow/tháng | Ghi chú |
|---|---|---|---|
| Google AI Pro | 19,99 USD/tháng. Một bài vnreview (không ghi ngày) nêu ở VN **489.000đ/tháng**, 5 triệu đồng/năm, tháng đầu miễn phí | ~1.000 | Veo 3.1 Fast 20 credit/lần, Quality 100 credit/lần |
| Google AI Ultra (bậc mới từ 19/5/2026) | 99,99 USD/tháng | ~10.000 | Fast/Lite giảm nửa giá (Fast 10 credit) |
| Google AI Ultra (bậc cao) | 199,99 USD/tháng (trước là 249,99) | ~25.000 | Có "Lite Lower Priority 0 credit"; 4K và clip 4/6 giây chỉ có ở Ultra theo tài liệu G-Labs |
| Gemini API (chính thức), Veo 3.1 | Standard 0,40 USD/giây (720p/1080p), 0,60 USD/giây (4K); **Fast 0,10 / 0,12 / 0,30**; **Lite 0,05 / 0,08** | Trả theo dùng | Giá có audio; free tier không gồm Veo (ai.google.dev pricing, qua kết quả tìm kiếm) |

- [SUY LUẬN] AI Pro được khoảng 50 lần Veo Fast (khoảng 400 giây, gần 6,7 phút **trước** khi trừ phần làm lại).
  Muốn sản xuất hàng loạt thì phải nhiều tài khoản Pro hoặc Ultra. Đây chính là động cơ của tính năng "xoay vòng tài khoản",
  và cũng là hành vi rủi ro nhất về ToS (nhiều tài khoản để vượt hạn mức).
- [SUY LUẬN] So sánh: 1 phút B-roll Veo 3.1 Lite qua API chính thức là 60 × 0,05 = **3 USD**. Fast 720p là **6 USD/phút**.
  Với kênh chỉ cần 1–2 phút B-roll/video, **API chính thức rẻ hơn hoặc ngang** AI Pro cộng G-Labs, và không có rủi ro ToS.

---

## 4. Đầu ra

| Hạng mục | Thông tin | Nhãn |
|---|---|---|
| Độ dài clip | Veo 3.1: **4/6/8 giây** (4/6 giây cần Ultra); Omni Flash 4/6/8/10 giây; Google Vids 3–10 giây; Grok 6/10/15 giây | [ĐÃ KIỂM] tài liệu Webhook |
| Độ phân giải | Video gốc 720p (Omni Flash có 360p), upscale lên 1080p; **4K chỉ Ultra**. Tỉ lệ 16:9 / 9:16 | [ĐÃ KIỂM] |
| Âm thanh | Veo 3.1 có audio sinh kèm. Giọng nhân vật chọn từ **giọng preset của Flow** (chế độ components). Changelog: video lỗi audio được giữ dạng câm | [ĐÃ KIỂM] |
| Giọng tiếng Việt | **Không có TTS tiếng Việt trong G-Labs Studio.** Lời thoại tiếng Việt do Veo sinh ra: chất lượng [CẦN XÁC MINH]. TTS nằm ở app G-Labs Voiceover (giọng CapCut và 322 giọng Microsoft Edge, có vi-VN), cũng là truy cập không chính thức | GitHub G-Labs-Voiceover |
| Watermark | Flow: logo "Veo" hiển thị (theo blog bên thứ ba, nay có công tắc "Visible watermarking"), cộng **SynthID ẩn luôn có** trên mọi đầu ra Veo/Omni/Nano Banana. G-Labs **tự xoá logo Gemini ✦** trên ảnh Pics và video Vids (mặc định BẬT xoá). SynthID vẫn còn | [ĐÃ KIỂM] README; thông tin watermark Flow [CẦN XÁC MINH] trên trang help của Google |
| Ghép thành video dài | **Có công cụ ghép cơ bản**: node Merge Video (2 clip), Video Edit timeline (video + SRT + audio → xuất 1 file), slideshow ảnh khớp SRT. Pipeline "idea → video tài liệu hoàn chỉnh" nằm ở **G-Labs Story Machine** (kèm gói MAX): LLM (Claude/Codex CLI…) viết kịch bản, Voiceover đọc, Studio tạo ảnh/video, render, gợi ý SEO, xuất sang CapCut | [NGƯỜI BÁN NÓI] |
| Biểu đồ số liệu | **Không có** công cụ vẽ biểu đồ từ dữ liệu thật. Ảnh/video AI sinh biểu đồ "trông như thật" nhưng **số liệu bịa**, rất nguy hiểm với kênh tài chính | [SUY LUẬN] |

---

## 5. Rủi ro

### 5.1 Rủi ro tài khoản và ToS (cao)
- Như mục 2.3: tự động hoá giao thức nội bộ, sinh token reCAPTCHA, xoay nhiều tài khoản. Nếu Google xử lý, có thể mất **cả tài khoản Google**
  (Gmail, Drive, **YouTube**, AdSense nếu chung tài khoản), không chỉ mất quyền Flow. [SUY LUẬN, dựa trên chính sách mục 2.3]
- Phụ thuộc giao diện/giao thức của Google: mỗi lần Flow đổi, tool hỏng cho tới khi có bản vá.
  Tác giả vá nhanh (nhiều bản/tuần) nhưng đó cũng là tín hiệu "đuổi theo" thay đổi. [ĐÃ KIỂM changelog]

### 5.2 Rủi ro bảo mật (cao nếu dùng tài khoản chính)
- App **đóng nguồn, không ký số**, tự cập nhật từ GitHub Releases và **cả Google Drive**. Người dùng được hướng dẫn tắt SmartScreen/Gatekeeper.
- Lưu cookie và phiên của **nhiều tài khoản Google, ChatGPT, Meta, Grok** tại `%APPDATA%\G-Labs Studio` hoặc `~/Library/Application Support/G-Labs Studio`.
  Bất kỳ mã độc nào trên máy lấy được thư mục này là chiếm được các phiên đó.
- Đã có **140 fork** của repo cũ (ví dụ `MechaRengar/G-Labs-Automation`, có kèm file zip extension riêng).
  Fork/bản "crack" là kênh phát tán mã độc phổ biến. **Chỉ tải từ repo `duckmartians` gốc.** [ĐÃ KIỂM fork tồn tại; nội dung zip fork chưa kiểm]
- Bối cảnh: Google TAG (10/2021) công bố chiến dịch **mã độc ăn cookie nhắm vào YouTuber** (RedLine, Vidar, Raccoon…),
  dùng phần mềm giả để chiếm kênh **vượt qua 2FA**. Kênh bị chiếm được bán từ 3 đến 4.000 USD. Xem thêm `shared/knowledge/platforms/youtube.md` (mục bảo mật) và skill `youtube-channel-setup`.
- [SUY LUẬN] Không có bằng chứng G-Labs là mã độc. Tác giả công khai danh tính, có lịch sử gần 1 năm, cộng đồng hàng nghìn người.
  Nhưng **mô hình tin cậy** (phần mềm đóng nguồn cầm cookie tài khoản Google) **không chấp nhận được với tài khoản sở hữu kênh**.

### 5.3 Rủi ro người bán
- Nhà phát triển cá nhân, không thấy pháp nhân công ty. [CẦN XÁC MINH: có thể ghi trong terms.html]
- Đánh giá độc lập: chỉ có số liệu cho extension "Auto Flow" cùng hệ: khoảng **3,85★ / 195 đánh giá, khoảng 40.000 người dùng**
  (chrome-stats, qua đoạn trích tìm kiếm). Lời chê hay gặp: thiếu ổn định, giá, hay lỗi khi Flow thay đổi. Lời khen: hỗ trợ nhanh qua Discord, cập nhật đều.
  Extension Auth Helper khoảng 4.000+ người dùng. [CẦN XÁC MINH]
- Hoàn tiền chỉ 24 giờ. License gói theo thời gian. Nếu Google chặn kiểu truy cập này, phần còn lại của license gần như mất giá trị. [SUY LUẬN]

### 5.4 Rủi ro nội dung và kiếm tiền YouTube
- Chính sách **inauthentic content** (đổi tên 15/7/2025). Làm rõ 7/2026: không kiếm tiền cho nội dung template/hàng loạt,
  **AI persona bàn tài chính/sức khoẻ/pháp lý**. Đợt xoá kênh AI slop 1/2026.
  Chi tiết và nguồn ở `shared/knowledge/platforms/youtube.md` và `projects/01-youtube-ai-finance/research/reports/`.
- Tính năng "hàng loạt + xoay tài khoản + xoá logo AI" **được thiết kế cho đúng loại nội dung YouTube đang siết**. [SUY LUẬN]
- Xoá watermark hiển thị không xoá SynthID. Nếu nội dung trông như thật mà không khai nhãn "altered/synthetic" thì có nguy cơ bị phạt. [SUY LUẬN]

---

## 6. Mức độ phù hợp với dự án

### 6.1 Kênh 01: AI tài chính tiếng Việt (faceless, giải thích/tài liệu, minh hoạ + biểu đồ thật, ngân sách 20–60 USD/tháng)
| Nhu cầu | G-Labs đáp ứng? |
|---|---|
| Kịch bản chính xác, có nguồn | Không (Story Machine dùng LLM, nhưng kiểm chứng số liệu vẫn phải làm tay) |
| Lời thoại tiếng Việt chất lượng | Không có trong Studio; Voiceover dùng giọng CapCut/Edge (không chính thức) |
| **Biểu đồ số liệu thật** | **Không**, đây là lõi giá trị của kênh |
| Ảnh minh hoạ phong cách nhất quán | **Có** (Nano Banana, thư viện nhân vật), nhưng làm thủ công trên Flow/Gemini cũng được, và với ~20–40 ảnh/video thì không cần chạy hàng loạt |
| B-roll/hook động 5–8 giây | **Có**, nhưng một video chỉ cần vài clip, không cần hàng loạt |
| Ghép video 8–15 phút | Có công cụ cơ bản/Story Machine; CapCut/ffmpeg/Remotion làm tốt hơn và kiểm soát được |
| Ngân sách | Phần mềm rẻ, nhưng sản xuất Veo đủ lượng thì cần Ultra (≥ 99,99 USD) hoặc nhiều tài khoản Pro, **vượt ngân sách và rủi ro** |

→ [SUY LUẬN] **Độ phù hợp thấp.** G-Labs giải bài toán "nhiều clip AI, rẻ, nhanh",
còn kênh 01 cần "ít mà đúng: số liệu thật, giọng tốt, góc nhìn riêng".

### 6.2 So sánh phương án thay thế (giá tham khảo 10/2026, [CẦN XÁC MINH] trước khi mua)
| Phương án | Ưu | Nhược | Hợp kênh 01? |
|---|---|---|---|
| **Pipeline tự xây**: LLM viết script → TTS (ElevenLabs/Google TTS/Azure vi-VN) → ảnh (Gemini/Imagen API hoặc Flow thủ công) + **biểu đồ từ dữ liệu thật** (matplotlib/plotly/Remotion) → ffmpeg/Remotion ghép | Đúng ToS, biểu đồ thật, kiểm soát chất lượng, tiến dần lên L2/L3 theo vòng lặp skill của repo | Tốn công dựng ban đầu | **Tốt nhất về lâu dài** |
| **Gemini API chính thức (Veo 3.1 Lite/Fast)** cho vài clip B-roll | Hợp lệ, trả theo dùng (~3–6 USD/phút), tự động hoá bằng script được | Cần thẻ thanh toán/billing; không có free tier cho Veo | Tốt cho B-roll/hook |
| **Flow thủ công với AI Pro** (~19,99 USD hoặc ~489k/tháng) | Hợp lệ, 1.000 credit, kèm Gemini Pro và Nano Banana | Bấm tay; có watermark/SynthID; credit ít | Ổn nếu chỉ vài clip/tuần |
| **CapCut** (desktop/web) | TTS tiếng Việt sẵn, phụ đề tự động, template; người VN quen dùng | API không chính thức; lệ thuộc template, dễ "trông giống mọi kênh" | Tốt cho khâu dựng/phụ đề |
| **InVideo / Pictory** | Script → video stock nhanh | Stock chung chung, dễ bị coi là template; tiếng Việt hạn chế [CẦN XÁC MINH] | Trung bình–thấp |
| **Kling / Hailuo** (web hoặc API) | Clip dài hơn (5–10 giây), giá credit rẻ | Như Veo: chỉ là clip, không giải được biểu đồ/giọng | Chỉ cho B-roll |
| **G-Labs Studio** | Rẻ, nhiều model một chỗ, hàng loạt, có webhook | ToS/khoá tài khoản, bảo mật cookie, xoá watermark, không có biểu đồ và TTS Việt | **Không khuyến nghị cho 01** |

### 6.3 Nếu vẫn muốn thử G-Labs (chỉ để đánh giá, theo luật test của repo)
- Lập file `experiments/EXP-xxx` có giả thuyết, KPI, hạn và chi phí tối đa (ví dụ 10 USD license cộng 1 tháng AI Pro trên **tài khoản phụ**).
- **Cách ly:** máy ảo hoặc máy phụ, profile Chrome riêng, **tài khoản Google phụ không liên quan kênh/AdSense/Drive chính**, không đăng nhập tài khoản chính trên máy đó.
- Theo dõi lưu lượng mạng của app (ví dụ Little Snitch/Wireshark) để xem app có gửi cookie ra ngoài không. Đây là gap chưa kiểm được.
- **Không** bật tính năng xoá logo. Khai nhãn altered/synthetic khi nội dung trông như thật.

### 6.4 Dự án 02 (TikTok Shop VN, đồ gia dụng)
- [SUY LUẬN] Video sản phẩm cần **hình ảnh sản phẩm thật**. Video AI "giả sản phẩm" dễ bị coi là gây hiểu nhầm.
  TikTok yêu cầu gắn nhãn nội dung AI. [CẦN XÁC MINH: chính sách TikTok Shop VN 2026 về video AI cho sản phẩm]
  G-Labs có thể hữu ích cho cảnh nền/hook (ảnh sản phẩm thật → video qua image-to-video), nhưng rủi ro tài khoản Google vẫn y nguyên.
  Đánh giá lại khi dự án 02 có test chứng minh định dạng thắng.

---

## 7. Đánh giá người dùng và demo
- **Không tìm được review độc lập** (blog, forum) về G-Labs Studio. [CẦN XÁC MINH]
- Có video hướng dẫn chính chủ: "G-Labs Automation v4.0 Setup Guide for Beginners — Automate Google Flow, Veo & Grok at Scale"
  (youtube.com/watch?v=jlRdi2RR_QM) cùng playlist EN/VI. **Không xem được** (proxy chặn YouTube).
- Đối tượng người bán nhắm tới (README cũ): "print-on-demand sellers and agencies running AI production at scale".
- Ảnh chụp màn hình giao diện có trong repo: `docs/screenshots/{en,vi}/*.webp`.
- Việc nên làm: vào nhóm Zalo/Discord của tool (link ở README `duckmartians/G-Labs-Automation`) hỏi về
  (1) tỉ lệ tài khoản bị khoá/hạn chế, (2) thời gian chết khi Flow đổi giao thức, (3) ví dụ kênh YouTube đang kiếm tiền bằng nội dung làm từ tool.

---

## 8. Khoảng trống chưa kiểm chứng
1. Nội dung trực tiếp của `duckspace.net/g-labs-studio/`: bảng giá chính xác (VND/USD), quyền lợi từng gói, `refunds.html`, `terms.html`, `privacy.html`. Proxy chặn.
2. App desktop có gửi cookie/token ra server người bán không. Cần phân tích lưu lượng/sandbox.
3. Báo cáo thực tế về khoá tài khoản Google/Grok/OpenAI do dùng G-Labs hoặc tool tương tự.
4. Nguyên văn hiện hành của Google ToS (2026) và trang help Flow về watermark. Chưa mở được trang gốc.
5. Giá Google AI Pro/Ultra tại VN năm 2026, và việc Flow/Veo có đầy đủ ở VN không (các nguồn mâu thuẫn).
6. Chất lượng lời thoại tiếng Việt do Veo 3.1 sinh ra.
7. Google Vids/Google Pics: hạn mức theo gói, điều khoản riêng.

## 9. Nguồn (truy cập 2026-10-10)
- GitHub `duckmartians/G-Labs-Studio` (README, `docs/readme/README.en.md`, `WEBHOOK_INTEGRATION.en.md`, `G-Labs_Studio_Auth_Helper.zip`, lịch sử commit, trang Releases): https://github.com/duckmartians/G-Labs-Studio
- GitHub `duckmartians/G-Labs-Automation` (README, changelog Releases v8.0.5–v9.0.4): https://github.com/duckmartians/G-Labs-Automation , https://github.com/duckmartians/G-Labs-Automation/releases
- GitHub `duckmartians/G-Labs-Story-Machine`: https://github.com/duckmartians/G-Labs-Story-Machine
- GitHub `duckmartians/G-Labs-Voiceover`, `G-Labs-Voice-Studio` (qua kết quả tìm kiếm)
- Fork: https://github.com/MechaRengar/G-Labs-Automation
- duckspace.net/en/g-labs-studio/ và duckmartians.info/g-labs/ (**chỉ đoạn trích tìm kiếm**, không mở được trực tiếp)
- Chrome Web Store: G-Labs Studio – Auth Helper (`clhcjdjbcldkogahjfmcgfipmlilmkpg`); Auto Flow x G-Labs Automation (`lhcmnhdbddgagibbbgppakocflbnknoa`), chrome-stats (đoạn trích)
- Giá Gemini API: https://ai.google.dev/gemini-api/docs/pricing (qua kết quả tìm kiếm); giá Flow/AI Pro/Ultra: costgoat.com/pricing/google-flow, diyai.io, saascrmreview.com (bên thứ ba)
- Google Generative AI Prohibited Use Policy: https://support.google.com/gemini/answer/16625148 ; Google ToS: https://policies.google.com/terms (qua conductatlas.com)
- Giá VN AI Pro: vnreview.vn (bài không ghi ngày)
- Watermark Flow/SynthID: atlascloud.ai blog (bên thứ ba, có lợi ích bán tool xoá watermark)
- Mã độc ăn cookie nhắm YouTuber: Google TAG 10/2021 qua darkreading.com, securityaffairs.com
- Chính sách YouTube inauthentic content: xem `shared/knowledge/platforms/youtube.md`
