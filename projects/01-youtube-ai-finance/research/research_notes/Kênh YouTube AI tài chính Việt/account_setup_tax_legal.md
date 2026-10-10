# Thiết lập tài khoản, AdSense, thuế & pháp lý cho kênh YouTube tài chính của cá nhân ở Việt Nam (2025-2026)

> Ngày nghiên cứu: 2026-10-10. Đây KHÔNG phải tư vấn pháp lý/thuế. Môi trường nghiên cứu không truy cập được support.google.com và nhiều tên miền .vn (lỗi DNS), nên phần lớn số liệu lấy từ bản tóm tắt kết quả tìm kiếm. Mục nào chưa đối chiếu được văn bản gốc đều gắn nhãn `[CẦN XÁC MINH 2026-10-10]`. Phần thuế 2026 thay đổi rất nhanh (có tới 3 văn bản trong 10 tháng) — **phải hỏi kế toán thuế/Thuế cơ sở nơi cư trú trước khi kê khai**.

## A. Cấu trúc tài khoản & bảo mật

### Takeaway
Tạo kênh trên một Google account riêng (không dùng email cá nhân hằng ngày), đặt kênh dưới dạng Brand Account/channel permissions để có thể cấp quyền cho người khác và chuyển nhượng sau này, bật xác minh 2 bước mạnh (passkey/khoá bảo mật), và coi email "mời tài trợ kèm file tải về" là mối đe doạ số 1 vì mã độc ăn cắp cookie vượt qua được 2FA.

### Cited Findings
- YouTube đã thay vai trò của Brand Account bằng "channel permissions" với các vai trò Owner, Manager, Editor, Editor (Limited), Subtitle Editor, Viewer, Viewer (Limited). Owner không bị giới hạn (kể cả xoá kênh) nhưng **không thể chuyển quyền sở hữu qua màn hình permissions**; Manager không xoá được kênh. — [YouTube Help: Migrate from Brand Account user access to channel permissions](https://support.google.com/youtube/answer/9367690?hl=en)
- Editor (Limited) giống Editor nhưng không xem được dữ liệu doanh thu → vai trò phù hợp cho editor thuê ngoài. — [YouTube Help 9367690](https://support.google.com/youtube/answer/9367690?hl=en)
- Phải đăng nhập bằng primary owner của Brand Account mới bật được permissions; chỉ nên opt-out permissions khi cần thực hiện chuyển nhượng kênh (Studio → Settings → Permissions). — [YouTube Help 9367690](https://support.google.com/youtube/answer/9367690?hl=en)
- Cảnh báo: nếu xoá tài khoản primary owner gắn với kênh thì kênh cũng bị xoá. — [YouTube Help 9367690](https://support.google.com/youtube/answer/9367690?hl=en) (theo tóm tắt kết quả tìm kiếm)
- Chuyển nhượng quyền sở hữu vẫn đi qua Brand Account: có thể chuyển kênh từ tài khoản cá nhân sang Brand Account, và từ Brand Account này sang Brand Account khác. — [Leadsie](https://www.leadsie.com/blog/give-youtube-channel-access); [Sirency](https://www.sirency.com/blog/youtube-channel-permissions) (nguồn thứ cấp)
- Một số công cụ bên thứ ba yêu cầu vai trò Owner để kết nối kênh qua API. — [Metricool Help](https://help.metricool.com/youtube-channel-permissions-nq073)
- Google TAG (10/2021): chiến dịch giả làm nhà tài trợ gửi email "hợp tác quảng cáo", dẫn tới trang tải phần mềm giả (hoặc PDF trên Google Drive) chứa mã độc ăn cắp cookie trình duyệt; cookie phiên cho phép chiếm kênh **vượt qua 2FA**, đổi mật khẩu và thông tin khôi phục. Kênh bị chiếm được bán giá 3–4.000 USD hoặc đổi tên để livestream lừa đảo crypto. ≥1.011 tên miền, ~15.000 tài khoản liên quan; sau khi Google chặn, kẻ tấn công chuyển sang dẫn nạn nhân qua WhatsApp/Telegram/Discord. — [The Hacker News](https://thehackernews.com/2021/10/hackers-stealing-browser-cookies-to.html); [Dark Reading](https://www.darkreading.com/attacks-breaches/google-phishing-campaign-targets-youtube-creators); [Hackread](https://www.hackread.com/google-cookie-stealer-malware-hit-youtubers/)
- Nghị định 147/2024/NĐ-CP (hiệu lực 25/12/2024): tài khoản mạng xã hội phải xác thực bằng số điện thoại di động Việt Nam (không có số VN thì xác thực bằng số định danh cá nhân); chỉ tài khoản đã xác thực mới được đăng bài, bình luận, livestream, chia sẻ; tài khoản livestream có mục đích thương mại phải xác thực bằng số định danh cá nhân; nghĩa vụ áp dụng cho nền tảng xuyên biên giới vượt ngưỡng (ví dụ ≥100.000 lượt truy cập/tháng từ VN), thời hạn chuyển tiếp 90 ngày. — [VnEconomy](https://vneconomy.vn/tu-ngay-25-12-tai-khoan-mang-xa-hoi-phai-xac-thuc-so-dien-thoai-moi-duoc-dang-bai.htm); [Cổng TTĐT Hà Tĩnh](https://hatinh.gov.vn/vi/bai-viet/tu-hom-nay-tai-khoan-mang-xa-hoi-phai-xac-thuc-so-dien-thoai-moi-duoc-dang-bai); [Vision & Associates](https://vision-associates.com/vi/new-decree-on-management-provision-and-use-of-internet-services-and-online-information/?print=pdf). Các nguồn không thống nhất là quy định áp lên mọi nền tảng hay chỉ nền tảng vượt ngưỡng.

### Inferences
- Cấu trúc khuyến nghị: (1) Google account riêng cho kênh, đứng tên thật của chủ kênh (khớp CCCD — cần cho AdSense sau này); (2) kênh dạng Brand Account để có thể thêm Owner dự phòng (tài khoản thứ hai của chính chủ) và sau này chuyển sang công ty nếu thành lập doanh nghiệp; (3) người làm thuê chỉ nhận Editor (Limited) hoặc Manager, không bao giờ Owner; (4) tool tự động hoá upload ưu tiên dùng OAuth/YouTube Data API với vai trò thấp nhất chạy được — không đưa mật khẩu/cookie cho tool.
- Vì cookie theft vượt được 2FA, biện pháp quan trọng nhất là vệ sinh thiết bị: không mở file .exe/.scr/.zip/"phần mềm dùng thử" từ nhà tài trợ; dùng máy/trình duyệt riêng cho tài khoản kênh; định kỳ xem "Your devices" và đăng xuất phiên lạ.
- Quốc gia kênh đặt "Việt Nam" là trung thực và khớp với địa chỉ AdSense/thuế; đặt quốc gia giả để "tăng RPM" là không có cơ sở (RPM phụ thuộc nơi người xem) và tạo mâu thuẫn hồ sơ — đây là suy luận, chưa có nguồn Google trích được.
- Nếu Google account mới gặp yêu cầu xác thực số điện thoại để mở tính năng nâng cao (video >15 phút, thumbnail tuỳ chỉnh), dùng SIM chính chủ VN — cũng phù hợp Nghị định 147.

### Gaps
- Không truy cập được support.google.com nên không trích trực tiếp được: chính sách "nhiều kênh/một người", tác động của VPN, mô tả "intermediate/advanced features" (xác minh điện thoại, ID/video selfie, lịch sử kênh), passkey/Advanced Protection Program, và quy trình chuyển chủ sở hữu Brand Account (chờ 7 ngày sau khi thêm owner mới — theo kiến thức nền, `[CẦN XÁC MINH]`).
- Không tìm thấy nguồn cho thấy chiến dịch cookie-theft kiểu 2021 còn phổ biến ở 2025-2026 (dù các vụ hack kênh lớn vẫn được báo chí đưa tin — chưa kiểm chứng trong phiên này).

## B. AdSense & thanh toán

### Takeaway
Liên kết một tài khoản AdSense (đúng tên trên CCCD, địa chỉ nhận thư thật ở VN) khi đủ điều kiện YPP; với người mới năm 2026 phương thức thực tế là chuyển khoản điện tử (wire/SWIFT) về ngân hàng VN — Western Union đã ngừng nhận đăng ký mới từ 2020. Các ngưỡng cụ thể cho VN phải xem trong tài khoản AdSense.

### Cited Findings
- Trang Google về Western Union Quick Cash vẫn liệt kê Việt Nam (USD, giới hạn 4.000 USD/lần, không tách khoản), nhưng trang này đã cũ ~6 năm. — [AdSense Help: Western Union Quick Cash](https://support.google.com/adsense/answer/2850006?hl=en)
- Google thông báo từ 10/8/2020 không thể chọn Western Union làm phương thức mới; người đang dùng phải chuyển sang phương thức khác đầu 2021. — [Search Engine Roundtable](https://www.seroundtable.com/google-adsense-western-union-payment-option-29924.html)
- Trang "Add your payment method for AdSense or AdSense for YouTube" liệt kê phương thức theo quốc gia (khu vực châu Á - Thái Bình Dương có Wire), nhưng không xác nhận được dòng Việt Nam. — [AdSense Help 1714397](https://support.google.com/adsense/answer/1714397?hl=en)
- Quy trình chung: sau xác minh danh tính và đạt ngưỡng xác minh, Google gửi mã PIN qua bưu điện tới địa chỉ thanh toán; ngưỡng chọn phương thức thanh toán thường là 10 USD (nguồn thứ ba, không riêng VN). — [MonetizeHelper](https://monetizehelper.com/blog/adsense-payment-methods-guide); [optAd360](https://optad360.com/blog/google-adsense-payment/); [AdPushup](https://www.adpushup.com/blog/google-adsense-payment/)

### Inferences
- Quy tắc "một người – một tài khoản AdSense" và ngưỡng thanh toán 100 USD (chu kỳ: thu nhập chốt cuối tháng, thanh toán quanh ngày 21 tháng sau) là kiến thức phổ biến nhưng chưa trích được nguồn Google trong phiên này `[CẦN XÁC MINH 2026-10-10]`. Nhiều kênh có thể liên kết vào cùng một AdSense — vì vậy người làm nhiều kênh không nên tạo AdSense thứ hai.
- Tên người nhận thanh toán trên AdSense phải trùng tên tài khoản ngân hàng VN và CCCD (viết không dấu theo thứ tự trên sổ ngân hàng); địa chỉ phải nhận được thư bưu điện (PIN có thể mất vài tuần). Nếu không nhận được PIN, Google thường cho phép yêu cầu lại/xác minh thay thế `[CẦN XÁC MINH]`.
- Ngoại tệ USD về ngân hàng VN: ngân hàng sẽ hỏi mục đích giao dịch; nên giữ chứng từ (payment receipt AdSense) vì dòng tiền này có thể được cơ quan thuế đối chiếu.

### Gaps
- Chưa có nguồn đáng tin về ngân hàng VN nào nhận wire AdSense tốt nhất, phí nhận SWIFT, tỷ giá quy đổi, và phí trung gian. Cần kiểm tra biểu phí của ngân hàng dự định dùng (Vietcombank, Techcombank, VIB, ACB… — chỉ là ví dụ, chưa so sánh).
- Chưa trích được nguồn Google về quy trình xác minh danh tính AdSense cho VN.

## B2. Thông tin thuế Mỹ trong AdSense (W-8BEN, khấu trừ tại nguồn)

### Takeaway
Cá nhân VN nộp W-8BEN trong AdSense; vì hiệp định thuế Việt–Mỹ (ký 7/7/2015) chưa có hiệu lực nên không có ưu đãi hiệp định → khấu trừ 30% trên phần doanh thu từ người xem ở Mỹ. Nếu không nộp thông tin thuế, Google có thể khấu trừ tới 24% trên **toàn bộ** doanh thu toàn cầu — nộp W-8BEN ngay khi bật kiếm tiền.

### Cited Findings
- Google: mức khấu trừ trên thu nhập từ người xem Mỹ từ 0–30% tuỳ quốc gia có hiệp định thuế với Mỹ hay không; nếu không nộp thông tin thuế, Google "có thể phải khấu trừ tới 24% thu nhập toàn cầu". — [Digital Music News](https://www.digitalmusicnews.com/2021/03/10/youtube-witholds-us-taxes/); [Hanoi Times](https://hanoitimes.vn/google-withholds-taxes-from-non-us-youtube-creators.583585.html)
- Hanoi Times: ngoài khấu trừ 24–30% từ YouTube, creator VN vẫn phải nộp thuế thu nhập tại VN. — [Hanoi Times](https://hanoitimes.vn/google-withholds-taxes-from-non-us-youtube-creators.583585.html)
- W-8BEN không có yêu cầu hưởng hiệp định → áp dụng mức luật định 30%. — [Acadifi](https://acadifi.com/knowledge/form-w-8ben-foreign-creators-withholding-tax-ea); [Easton Dev AdSense tax guide 2026](https://eastondev.com/blog/de/posts/media/20260109-adsense-tax-guide/)
- Hiệp định tránh đánh thuế hai lần Việt Nam – Hoa Kỳ ký ngày 7/7/2015 nhưng chỉ có hiệu lực khi hai bên trao đổi văn kiện phê chuẩn; nguồn gần đây mô tả là "signed but not in force", không có trong danh sách hiệp định hiệu lực của IRS. — [DFDL](https://www.dfdl.com/insights/legal-and-tax-updates/tax-alert-the-income-tax-treaty-between-vietnam); [Duane Morris](https://www.duanemorris.com/alerts/first-ever_tax_treaty_and_protocol_united_states_vietnam_0715.html); [Greenback Tax Services](https://www.greenbacktaxservices.com/country-guide/us-taxes-vietnam-americans/)

### Inferences
- Ví dụ minh hoạ: tháng có 400 USD doanh thu, trong đó 25% từ người xem Mỹ (100 USD) → khấu trừ 30 USD (30% × 100); nhận 370 USD. Không nộp W-8BEN → có thể bị khấu trừ tới 96 USD (24% × 400). Kênh tài chính tiếng Việt có tỷ lệ người xem Mỹ thấp (chủ yếu Việt kiều) nên tác động nhỏ; kênh tiếng Anh cho thị trường US thì 30% là chi phí lớn.
- Thuế đã bị Mỹ khấu trừ có được trừ vào thuế VN hay không: hiện không có hiệp định nên khả năng cao **không được khấu trừ** — cần hỏi kế toán `[CẦN XÁC MINH]`.
- Khi điền W-8BEN: cá nhân, quốc tịch/cư trú Việt Nam, không chọn treaty benefit; nếu có MST cá nhân VN (nay dùng số CCCD làm MST) thì điền Foreign TIN.

### Gaps
- Không truy cập được trang chính thức YouTube Help (answer 10391462) và IRS treaty list để trích trực tiếp; nhận định "hiệp định chưa hiệu lực" dựa trên nguồn thứ cấp.

## C1. Thuế thu nhập cá nhân tại Việt Nam cho thu nhập YouTube (2025-2026)

### Takeaway
Thu nhập từ Google/YouTube là thu nhập kinh doanh của cá nhân và phải tự kê khai (Google không khấu trừ thuế VN). Đến hết 2025: doanh thu >100 triệu đồng/năm nộp 7% (5% GTGT + 2% TNCN). Từ 2026 khung pháp lý thay đổi mạnh: Luật Thuế TNCN số 109/2025/QH15 (hiệu lực 1/7/2026), Nghị định 68/2026/NĐ-CP (5/3/2026, ngưỡng 500 triệu) và Nghị định 141/2026/NĐ-CP (29/4/2026, nâng ngưỡng miễn thuế GTGT và TNCN lên **1 tỷ đồng/năm**, áp dụng từ 1/1/2026). Dưới ngưỡng vẫn phải **thông báo doanh thu** (Mẫu 01/TKN-CNKD trước 31/01 năm sau). Cách tính phần vượt ngưỡng và tỷ lệ riêng cho creator còn chưa rõ — bắt buộc hỏi kế toán.

### Cited Findings
- Quy định cũ (đến hết 2025): cá nhân có doanh thu >100 triệu/năm nộp GTGT 5% + TNCN 2% = 7% trên doanh thu. — [Vietstock 07/2026](https://vietstock.vn/2026/07/thu-nhap-tu-youtube-duoc-tinh-thue-the-nao-4261-1467965.htm); [iHoaDon](https://ihoadon.vn/hddt/co-phai-dong-thue-tncn-tu-youtube-google-va-facebook-khong.html)
- Từ 2026, VnExpress: hộ kinh doanh có doanh thu trên 500 triệu/năm phải nộp thuế (ngưỡng nâng từ 100 triệu). — [VnExpress](https://vnexpress.net/tu-2026-ho-kinh-doanh-co-doanh-thu-tren-500-trieu-dong-mot-nam-phai-nop-thue-4991878.html)
- Luật Thuế TNCN 2025 (số 109/2025/QH15) hiệu lực 1/7/2026: khoản 1 Điều 7 — cá nhân cư trú kinh doanh có doanh thu năm ≤500 triệu không nộp TNCN; doanh thu 500 triệu–3 tỷ áp dụng 15% và được chọn tính theo tỷ lệ trên doanh thu hoặc theo thu nhập (doanh thu trừ chi phí); biểu lũy tiến rút còn 5 bậc (5/10/20/30/35%). — [VietnamNet](https://vietnamnet.vn/5-thay-doi-lon-cua-luat-thue-thu-nhap-ca-nhan-2025-tu-1-7-2481753.html); [Cổng Xây dựng chính sách – Chính phủ](https://xaydungchinhsach.chinhphu.vn/thong-nhat-ho-kinh-doanh-co-doanh-thu-den-500-trieu-dong-nam-khong-phai-nop-thue-119251210100204058.htm); [MeInvoice](https://www.meinvoice.vn/tin-tuc/13150/luat-thue-tncn/); [Báo Chính phủ](https://baochinhphu.vn/nhieu-thay-doi-ve-thue-doi-voi-ca-nhan-va-ho-kinh-doanh-102260106104740091.htm)
- Mâu thuẫn về thuế suất: một nguồn nêu 15% cho 500 triệu–3 tỷ (trên thu nhập), VnExpress nêu 17% cho 3–50 tỷ. — tóm tắt từ [VnExpress](https://vnexpress.net/tu-2026-ho-kinh-doanh-co-doanh-thu-tren-500-trieu-dong-mot-nam-phai-nop-thue-4991878.html) và [cuthongthai](https://cuthongthai.vn/thue-youtuber-tiktoker-content-creator-2026/) `[CẦN XÁC MINH]`
- Nghị định 68/2026/NĐ-CP ngày 5/3/2026: doanh thu năm ≤500 triệu không chịu GTGT và không nộp TNCN. — [cuthongthai (blog)](https://thue.cuthongthai.vn/blog/7-thue-youtube-fb-2026-creator-vn-tren-500-trieu-nop-ra-sao); [Vietstock](https://vietstock.vn/2026/07/thu-nhap-tu-youtube-duoc-tinh-thue-the-nao-4261-1467965.htm)
- Nghị định 141/2026/NĐ-CP ký 29/4/2026 sửa Nghị định 68/2026: nâng ngưỡng từ 500 triệu lên 1 tỷ đồng/năm cho miễn GTGT và TNCN của hộ/cá nhân kinh doanh, áp dụng từ 1/1/2026 (một nguồn gọi là hồi tố); bổ sung miễn TNDN cho doanh nghiệp doanh thu ≤1 tỷ; hộ dưới 1 tỷ chưa bắt buộc hoá đơn điện tử. Cục Thuế đã ra công điện triển khai. — [Tạp chí Công Thương](https://tapchicongthuong.vn/chinh-thuc--nang-nguong-chiu-thue-voi-ho-kinh-doanh-len-1-ty-dong-nam--ap-dung-tu-1-1-2026-514336.htm); [VnEconomy](https://vneconomy.vn/ho-kinh-doanh-co-doanh-thu-duoi-1-ty-dong-chua-bat-buoc-dung-hoa-don-dien-tu.htm); [Thuế & Hải quan – Tạp chí KT-TC](https://thuehaiquan.tapchikinhtetaichinh.vn/cuc-thue-gui-cong-dien-trien-khai-ngay-nghi-dinh-141-ve-mien-thue-cho-doanh-nghiep-ho-kinh-doanh-154989.html)
- Hộ/cá nhân thuộc diện miễn vẫn phải thông báo doanh thu với cơ quan thuế trước 31/01 năm sau theo Mẫu 01/TKN-CNKD. — [xcyber.vn](https://xcyber.vn/ho-kinh-doanh-co-doanh-thu-duoi-1-ty/); [fastca.vn](https://fastca.vn/ho-kinh-doanh-co-doanh-thu-duoi-1-ty) (nguồn thứ cấp)
- Vietstock/VTV (7/2026): người có doanh thu YouTube năm 2026 không nên mặc định tiếp tục nhân 7%; nghĩa vụ xác định theo NĐ 68/2026, NĐ 141/2026 và văn bản hướng dẫn; chưa có hướng dẫn cụ thể cách xác định phần doanh thu tính thuế khi vượt ngưỡng; ai đã nhận tiền mà chưa kê khai nên liên hệ cơ quan thuế để xác định năm phải khai và số thuế. — [Vietstock](https://vietstock.vn/2026/07/thu-nhap-tu-youtube-duoc-tinh-thue-the-nao-4261-1467965.htm); [VTV](https://vtv.vn/youtuber-dong-thue-the-nao-100260721111643838.htm); [Baomoi/Vnbusiness](https://baomoi.com/quy-dinh-moi-tu-nam-2026-va-loi-canh-bao-cho-cac-youtuber-c55655961.epi)
- Blog thuế cho rằng ngưỡng tính trên tổng doanh thu từ mọi nền tảng xuyên biên giới và thuế áp trên phần vượt ngưỡng — chưa phải văn bản pháp luật. — [cuthongthai](https://cuthongthai.vn/thue-youtuber-tiktoker-content-creator-2026/) `[CẦN XÁC MINH]`
- Thực tế 2026 có creator đang hỏi: năm 2025 doanh thu >100 triệu đã kê khai, năm 2026 dưới ngưỡng thì có phải nộp tạm rồi xin hoàn hay không. — [Công ty Luật ACC (hỏi đáp)](https://congtyluatacc.vn/minh-lam-youtube-doanh-thu-chua-toi-500-trieu-mot-nam-nam-2025-tren-100-trieu-thi-khai-nop-binh-thuong-gio-nam-2026-duoi-500-trieu-duoc-mien-thi-ke-khai-nhu-the-nao-a-co-the-ke-khai-xoa-so-thue-ve-0-d/)

### Inferences
- Với kênh mới, năm đầu gần như chắc chắn dưới ngưỡng 1 tỷ đồng (≈38.000 USD) → không phát sinh thuế VN, nhưng **vẫn nên thông báo doanh thu** hằng năm và lưu toàn bộ payment receipt AdSense + sao kê ngân hàng (cơ quan thuế có thể đối chiếu dòng ngoại tệ từ Google). Đây là cách "không vỡ khi lớn lên": có hồ sơ sạch từ năm đầu.
- Doanh thu tính ngưỡng nên hiểu là tổng doanh thu gộp (trước khi Mỹ khấu trừ 30%?) — chưa rõ, hỏi kế toán `[CẦN XÁC MINH]`.
- Khi doanh thu vượt ~1 tỷ/năm: cân nhắc chọn phương pháp tính theo thu nhập (doanh thu − chi phí: thuê editor, phần mềm AI, thiết bị) nếu chi phí lớn — cần sổ sách và hoá đơn chi phí. Khi vượt vài tỷ hoặc có thuê nhân sự/ký hợp đồng tài trợ với doanh nghiệp → cân nhắc thành lập công ty (TNHH một thành viên) và chuyển kênh (Brand Account) + AdSense sang pháp nhân. Mốc cụ thể cần kế toán tính.
- Thông tư 40/2021/TT-BTC và cơ chế thuế khoán (đã bị bãi bỏ từ 2026 theo định hướng Nghị quyết 198/2025/QH15 — kiến thức nền, chưa trích được nguồn trong phiên) có thể đã được thay bằng văn bản hướng dẫn mới `[CẦN XÁC MINH]`.

### Gaps
- Không đọc được văn bản gốc NĐ 68/2026, NĐ 141/2026, Luật 109/2025/QH15 (tên miền .vn không truy cập được); không xác định được: tỷ lệ % trên doanh thu cho "dịch vụ/nội dung số" khi vượt ngưỡng; khai theo quý hay năm cho thu nhập từ nước ngoài; ngưỡng tính trên doanh thu gộp hay thực nhận; mối quan hệ giữa ngưỡng 1 tỷ (NĐ 141) và 500 triệu (Luật 109 hiệu lực 1/7/2026).
- Chưa tìm thấy nguồn về việc ngân hàng báo cáo kiều hối/ngoại tệ từ Google cho cơ quan thuế (chỉ có thông tin cơ quan thuế yêu cầu Google cung cấp dữ liệu trong các năm trước — chưa kiểm chứng trong phiên).
- Không tìm được nguồn chính thức về việc thuế Mỹ đã khấu trừ có được trừ vào thuế VN.

## C2. Quy định nội dung online & rủi ro pháp lý của nội dung tài chính

### Takeaway
Rủi ro lớn nhất của kênh tài chính VN không phải YouTube mà là pháp luật VN: (1) đưa khuyến nghị mua/bán/nắm giữ mã chứng khoán cụ thể khi không có giấy phép UBCKNN có thể bị xử phạt; (2) crypto chỉ được hợp pháp hoá trong khuôn khổ thí điểm qua sàn được cấp phép, nên quảng bá sàn nước ngoài/dự án token rất rủi ro; (3) Luật Quảng cáo sửa đổi 2025 (hiệu lực 1/1/2026) đặt nghĩa vụ trực tiếp cho người có ảnh hưởng: xác minh, thông báo quảng cáo, chịu trách nhiệm, có thể bị xử lý hình sự nếu quảng cáo sai sự thật.

### Cited Findings
- UBCKNN: tổ chức/cá nhân đưa ra báo cáo phân tích và khuyến nghị mua, bán, nắm giữ chứng khoán cho nhà đầu tư khi chưa được UBCKNN cấp phép sẽ bị xử lý nghiêm. — [Bnews (TTXVN)](https://bnews.vn/canh-cao-than-trong-voi-cac-hoi-nhom-tu-van-chung-khoan-khong-phep/417919.html)
- Ví dụ xử phạt: một doanh nghiệp bị phạt 225 triệu đồng vì kinh doanh chứng khoán (tư vấn) khi chưa được cấp phép theo Nghị định 156/2020/NĐ-CP. — [Doanh nghiệp Hội nhập](https://doanhnghiephoinhap.vn/xu-phat-doanh-nghiep-tu-van-chung-khoan-chui-canh-bao-rui-ro-tu-cac-khuyen-nghi-dau-tu-tren-mang-132915.html)
- Nghị định 156/2020/NĐ-CP (xử phạt VPHC lĩnh vực chứng khoán) được sửa bởi Nghị định 128/2021 và Nghị định 306/2025/NĐ-CP ngày 25/11/2025 (chủ yếu về chào bán cổ phiếu riêng lẻ). — [LuatVietnam NĐ 156/2020](https://luatvietnam.vn/chung-khoan/nghi-dinh-156-2020-nd-cp-xu-phat-vi-pham-hanh-chinh-linh-vuc-chung-khoan-196491-d1.html); [LuatVietnam EN NĐ 306/2025](https://english.luatvietnam.vn/decree-no-306-2025-nd-cp-dated-november-25-2025-of-the-government-amending-and-supplementing-a-number-of-articles-of-the-governments-decree-no-156-419668-doc1.html); [Báo Chính phủ](https://baochinhphu.vn/sua-doi-bo-sung-quy-dinh-ve-xu-phat-vi-pham-hanh-chinh-lien-quan-den-chao-ban-phat-hanh-co-phieu-rieng-le-102251125164602717.htm)
- Luật Công nghiệp công nghệ số (thông qua 6/2025, hiệu lực 1/1/2026) luật hoá tài sản số; khoản 2 Điều 47: tài sản mã hoá là một loại tài sản số. — [Luật Việt An](https://luatvietan.vn/nghi-quyet-05-2025-nq-cp-trien-khai-thi-diem-thi-truong-tai-san-ma-hoa-tai-viet-nam.html); [Diễn đàn Doanh nghiệp](https://diendandoanhnghiep.vn/tai-san-ma-hoa-viet-nam-khi-the-che-mo-duong-cho-tang-truong-10168173.html)
- Nghị quyết 05/2025/NQ-CP ngày 9/9/2025 (hiệu lực ngay): thí điểm 5 năm chào bán, phát hành, tổ chức thị trường giao dịch và dịch vụ tài sản mã hoá; giao dịch/thanh toán phải bằng VND; theo nguồn thứ cấp, sàn được cấp phép cần vốn tối thiểu 10.000 tỷ đồng, sở hữu nước ngoài ≤49%. — [Luật Việt An](https://luatvietan.vn/nghi-quyet-05-2025-nq-cp-trien-khai-thi-diem-thi-truong-tai-san-ma-hoa-tai-viet-nam.html); [VnEconomy](https://vneconomy.vn/nghi-quyet-05-dong-vai-tro-bo-loc-loai-bo-nhung-mo-hinh-tiem-an-rui-ro-ve-tai-san-ma-hoa.htm); [Thương hiệu & Công luận](https://thuonghieucongluan.com.vn/dragon-capital-quy-mo-nam-giu-tai-san-ma-hoa-tai-viet-nam-khoang-100-ty-usd-a280060.html); [Tiền Phong](https://tienphong.vn/thi-diem-thi-truong-tai-san-ma-hoa-tang-toc-co-kiem-soat-post1798961.html)
- Nghị định 284/2026/NĐ-CP quy định xử phạt VPHC đối với hoạt động liên quan tài sản mã hoá. — [Tiền Phong / tổng hợp tìm kiếm](https://tienphong.vn/thi-diem-thi-truong-tai-san-ma-hoa-tang-toc-co-kiem-soat-post1798961.html) `[CẦN XÁC MINH: chưa đọc được văn bản, chưa rõ có điều khoản xử phạt quảng bá sàn không phép]`
- Luật Quảng cáo sửa đổi số 75/2025/QH15 (thông qua 16/6/2025, hiệu lực 1/1/2026), bổ sung Điều 15a về người chuyển tải sản phẩm quảng cáo/người có ảnh hưởng: phải xác minh độ tin cậy của người quảng cáo; kiểm tra tài liệu sản phẩm; chưa sử dụng hoặc chưa hiểu rõ sản phẩm thì không được giới thiệu; thông báo về việc quảng cáo ngay trước và trong khi thực hiện; quảng cáo sai sự thật có thể bị xử lý hình sự. — [LuatVietnam: 7 điểm mới](https://luatvietnam.vn/linh-vuc-khac/diem-moi-cua-luat-quang-cao-sua-doi-2025-883-102813-article.html); [Thư viện Pháp luật – Luật 75/2025/QH15](https://thuvienphapluat.vn/van-ban/Thuong-mai/Luat-Quang-cao-sua-doi-2025-so-75-2025-QH15-555035.aspx); [LuatVietnam: xử lý hình sự](https://luatvietnam.vn/tin-van-ban-moi/nguoi-co-anh-huong-quang-cao-sai-su-that-co-the-bi-xu-ly-hinh-su-186-103749-article.html); [Advertising Vietnam](https://advertisingvietnam.com/article/luat-quang-cao-ap-dung-tu-2026-doi-voi-influencer-marketing-p27549)
- Nghị định 147/2024/NĐ-CP: xác thực tài khoản, xem mục A. — [VnEconomy](https://vneconomy.vn/tu-ngay-25-12-tai-khoan-mang-xa-hoi-phai-xac-thuc-so-dien-thoai-moi-duoc-dang-bai.htm)

### Inferences
- Ranh giới an toàn cho kênh tài chính AI (suy luận từ các nguồn trên, cần luật sư xác nhận): nội dung **giáo dục/kiến thức chung** (lãi kép, cách đọc báo cáo tài chính, so sánh loại hình đầu tư, tin vĩ mô có trích nguồn) an toàn hơn nhiều so với **khuyến nghị mã cụ thể** ("mua HPG vùng giá X", "target Y"), tín hiệu, nhóm Zalo/Telegram "phím hàng" thu phí — loại sau rơi vào hành vi tư vấn đầu tư chứng khoán cần giấy phép.
- Không gọi vốn, không quản lý tiền hộ, không bán "khoá học làm giàu cam kết lợi nhuận".
- Crypto: chỉ nên giáo dục; không affiliate/quảng bá sàn nước ngoài chưa được cấp phép tại VN hay dự án token — vừa rủi ro theo NQ 05/2025 + NĐ 284/2026, vừa vi phạm chính sách quảng cáo của Google/YouTube với sản phẩm tài chính.
- Mọi video có tài trợ/affiliate: nêu rõ "quảng cáo" bằng lời và chữ ở đầu video và trong lúc nói về sản phẩm (đáp ứng "ngay trước và trong khi" của Điều 15a) + bật nhãn "Includes paid promotion" của YouTube; lưu hồ sơ xác minh nhà tài trợ (giấy phép, tài liệu sản phẩm).
- Nội dung AI (giọng/avatar AI) về tài chính: nên gắn disclaimer "không phải lời khuyên đầu tư" và công bố nội dung tổng hợp/AI theo yêu cầu của YouTube với nội dung chân thực bị chỉnh sửa.
- Thông tin sai sự thật trên mạng có chế tài hành chính (Nghị định 15/2020/NĐ-CP sửa bởi 14/2022/NĐ-CP — kiến thức nền) và hình sự (Điều 288 BLHS) `[CẦN XÁC MINH mức phạt hiện hành 2026]`.

### Gaps
- Không tìm được điều khoản và mức phạt cụ thể cho cá nhân/YouTuber tư vấn chứng khoán không phép (cần đọc Điều liên quan trong NĐ 156/2020 đã sửa đổi); chưa có vụ YouTuber cụ thể bị phạt được kiểm chứng.
- Chưa xác minh mức phạt tung tin sai sự thật hiện hành và có văn bản thay thế NĐ 15/2020 trong 2025-2026 hay chưa.
- Chưa có danh sách sàn tài sản mã hoá đã được cấp phép thí điểm tính đến 10/2026.

## C3. Bản quyền (tin tức, clip VTV, nhạc, Content ID)

### Takeaway
Không tìm được nguồn mới trong phiên; theo nguyên tắc chung: không dùng nguyên trạng clip VTV/đài truyền hình/báo, nhạc thương mại — các đơn vị này (và đối tác MCN) đăng ký Content ID rộng rãi tại VN, có thể dẫn tới claim chuyển doanh thu hoặc gậy bản quyền.

### Cited Findings
- Không có phát hiện được trích nguồn trong phiên này (giới hạn số lượt tìm kiếm).

### Inferences
- Thực hành an toàn cho kênh AI tài chính: tự dựng hình (biểu đồ tự vẽ từ dữ liệu công khai, stock footage có giấy phép, ảnh do AI tạo), nhạc từ YouTube Audio Library hoặc dịch vụ có licence rõ ràng; trích dẫn tin tức bằng lời tóm tắt + ghi nguồn thay vì phát lại clip; nếu cần trích ngắn để bình luận, giữ ngắn và biến đổi (luật VN có ngoại lệ trích dẫn hợp lý theo Luật SHTT, nhưng phạm vi hẹp hơn "fair use" Mỹ) `[CẦN XÁC MINH]`.
- Content ID claim không phải gậy nhưng làm mất doanh thu video; 3 gậy bản quyền trong 90 ngày → chấm dứt kênh (chính sách YouTube phổ biến, `[CẦN XÁC MINH]`).

### Gaps
- Chưa xác minh: chính sách Content ID của VTV/các đài; điều khoản trích dẫn trong Luật SHTT sửa đổi 2022 (Luật 07/2022/QH15); trường hợp YouTube "reused content" với video tổng hợp tin bằng AI.

## D. Checklist ngày đầu tiên (theo mức ưu tiên)

### Takeaway
Thứ tự: bảo mật & quyền sở hữu → danh tính khớp CCCD → AdSense/W-8BEN khi bật kiếm tiền → hồ sơ thuế → khung tuân thủ nội dung tài chính.

### Cited Findings
- (Tổng hợp từ các nguồn ở mục A–C2; xem trích dẫn tương ứng.)

### Inferences
1. **Tạo Google account riêng** cho kênh, tên thật khớp CCCD; SIM VN chính chủ làm số khôi phục (phù hợp NĐ 147/2024); email khôi phục là tài khoản khác của chính chủ.
2. **Bật xác minh 2 bước mạnh**: passkey hoặc khoá bảo mật vật lý; tắt SMS làm phương án chính nếu có thể; cân nhắc Google Advanced Protection `[CẦN XÁC MINH khả dụng]`. Lưu mã dự phòng offline.
3. **Tạo kênh dạng Brand Account/permissions**; thêm một Owner dự phòng (tài khoản thứ 2 của chính chủ). Không bao giờ cấp Owner cho editor/tool — dùng Editor (Limited) ([YouTube Help](https://support.google.com/youtube/answer/9367690?hl=en)).
4. **Quốc gia kênh = Việt Nam**, ngôn ngữ, thông tin liên hệ business email riêng (không lộ email đăng nhập).
5. **Xác minh điện thoại** để mở tính năng nâng cao (thumbnail, video dài).
6. **Vệ sinh bảo mật**: máy/trình duyệt riêng cho kênh; không tải file từ "nhà tài trợ"; kiểm tra định kỳ thiết bị đăng nhập & ứng dụng bên thứ ba có quyền (myaccount.google.com → Security) ([TAG/Hacker News](https://thehackernews.com/2021/10/hackers-stealing-browser-cookies-to.html)).
7. **Tool upload/automation**: dùng YouTube Data API qua OAuth với project Google Cloud của chính mình; không đưa cookie/mật khẩu cho SaaS lạ; thu hồi token khi ngừng dùng.
8. **Khi đủ điều kiện YPP**: tạo/ liên kết **một** AdSense duy nhất, tên & địa chỉ khớp CCCD và tài khoản ngân hàng USD/VND; nhập địa chỉ nhận thư được để nhận PIN; chọn wire transfer về ngân hàng VN (Western Union không còn cho đăng ký mới — [SER](https://www.seroundtable.com/google-adsense-western-union-payment-option-29924.html)).
9. **Nộp W-8BEN ngay** (cá nhân, Việt Nam, không claim treaty) để tránh khấu trừ tới 24% doanh thu toàn cầu; chấp nhận 30% trên doanh thu người xem Mỹ ([DFDL](https://www.dfdl.com/insights/legal-and-tax-updates/tax-alert-the-income-tax-treaty-between-vietnam); [Hanoi Times](https://hanoitimes.vn/google-withholds-taxes-from-non-us-youtube-creators.583585.html)).
10. **Hồ sơ thuế VN**: kiểm tra MST cá nhân (số CCCD); lập file theo dõi doanh thu tháng (gross, US withholding, net, tỷ giá ngày nhận); lưu payment receipt + sao kê; đầu mỗi năm thông báo doanh thu (Mẫu 01/TKN-CNKD trước 31/01) nếu áp dụng; **hỏi kế toán khi doanh thu năm tiến gần 1 tỷ đồng** hoặc khi có hợp đồng tài trợ ([Vietstock](https://vietstock.vn/2026/07/thu-nhap-tu-youtube-duoc-tinh-thue-the-nao-4261-1467965.htm)).
11. **Khung tuân thủ nội dung tài chính**: disclaimer cố định "nội dung giáo dục, không phải khuyến nghị đầu tư"; cấm khuyến nghị mã/giá mục tiêu; không quảng bá sàn crypto/forex không phép; quy trình công bố quảng cáo theo Điều 15a Luật 75/2025/QH15; lưu hồ sơ thẩm định nhà tài trợ.
12. **Bản quyền**: chỉ dùng tài nguyên có licence; không phát lại clip đài truyền hình/báo.
13. **Ghi vào `ops/DECISIONS.md`** cấu trúc tài khoản đã chọn và lịch xem lại thuế (mỗi khi có nghị định mới).

### Gaps
- Checklist dựa một phần vào kiến thức nền về Google Help không truy cập được trong phiên; nên đối chiếu lại các trang YouTube/AdSense Help hiện hành trước khi thực hiện.
