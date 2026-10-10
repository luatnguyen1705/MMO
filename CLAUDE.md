# MMO HQ — Bộ não trung tâm

Repo này là nơi lưu trữ và vận hành **tất cả** dự án kiếm tiền online (MMO) của chủ repo:
nghiên cứu đối thủ, insight, chiến lược, test, nội dung, automation, số liệu.

Đọc file này trước mọi tác vụ. Sau đó đọc `projects/<dự-án>/CLAUDE.md` của dự án đang làm.

---

## 1. Bố cục

```
MMO/
├── CLAUDE.md                 ← luật chung (file này)
├── README.md                 ← tổng quan + danh mục dự án
├── .claude/skills/           ← skill DÙNG CHUNG cho mọi dự án (quy trình chung)
├── shared/
│   ├── knowledge/            ← kiến thức chung: chính sách nền tảng, tool, bài học xuyên dự án
│   ├── automation/           ← code/thư viện dùng chung (LLM, TTS, upload, scheduler…)
│   └── templates/project/    ← khung chuẩn cho dự án mới
├── projects/
│   ├── README.md             ← registry: danh sách dự án + trạng thái
│   └── <NN-ten-du-an>/       ← MỖI DỰ ÁN LÀ MỘT THẾ GIỚI RIÊNG
└── scripts/                  ← script tiện ích của repo (tạo dự án mới…)
```

Khung của mỗi dự án:

```
projects/<NN-ten-du-an>/
├── README.md        ← mục tiêu, KPI, phase hiện tại, link nhanh
├── CLAUDE.md        ← bối cảnh + luật riêng của dự án
├── .claude/skills/  ← skill RIÊNG của dự án (quy trình đặc thù)
├── research/        ← competitors/ · insights/ · market/
├── strategy/        ← định vị, content pillar, kế hoạch kiếm tiền
├── experiments/     ← mỗi test = 1 file EXP-xxx; INDEX.md tổng hợp
├── content/         ← ideas/ · scripts/ · published/ (log đã đăng)
├── automation/      ← pipelines/ (code) · config/ (cấu hình, không chứa secret)
├── data/            ← raw/ (KHÔNG commit) · processed/ · metrics/
└── ops/             ← JOURNAL.md (nhật ký) · DECISIONS.md (quyết định & lý do)
```

## 2. Luật tách bạch dữ liệu (bắt buộc)

1. **Một tác vụ chỉ ghi vào thư mục của đúng một dự án.** Không ghi dữ liệu dự án A vào dự án B.
2. Kiến thức chỉ được đưa lên `shared/knowledge/` khi nó **đúng cho nhiều dự án** (ví dụ: chính sách YouTube,
   cách dùng ElevenLabs). Khi đưa lên, ghi rõ nguồn dự án và ngày.
3. Code dùng chung đặt ở `shared/automation/`; code đặc thù đặt trong `projects/<p>/automation/`.
   Dự án được import từ `shared/`, `shared/` **không bao giờ** import từ một dự án.
4. Secret (API key, cookie, mật khẩu) chỉ nằm trong `projects/<p>/.env` hoặc `.env` gốc — đã bị gitignore.
   Mẫu khai báo đặt ở `.env.example`. Không bao giờ commit secret.
5. File media nặng (video, audio, ảnh gốc) và dữ liệu thô (`data/raw/`) không commit — chỉ commit metadata/log.
6. Tên file: `YYYY-MM-DD-<mo-ta-ngan>.md` cho tài liệu theo thời gian; chữ thường, gạch nối, không dấu.

## 3. Vòng lặp Skill — mỗi thao tác đều thành tài sản

Mục tiêu: mọi việc làm từ 2 lần trở lên phải trở thành **skill** để lần sau làm nhanh hơn, đúng hơn, và
tiến tới tự động hoàn toàn.

**Sau MỖI tác vụ có ý nghĩa, bắt buộc:**

1. Kiểm tra đã có skill cho việc này chưa (`.claude/skills/` chung và `projects/<p>/.claude/skills/`).
2. Nếu **chưa có** và việc này sẽ lặp lại → tạo skill mới bằng skill `save-skill`.
3. Nếu **đã có** → cập nhật: thêm bước thiếu, sửa bước sai, ghi vào mục **Bài học** và **Changelog**.
4. Ghi 1 dòng vào `projects/<p>/ops/JOURNAL.md` (làm gì, kết quả, skill nào được tạo/cập nhật).

Chọn nơi lưu skill:
- Quy trình dùng được cho nhiều dự án (nghiên cứu đối thủ, setup test, review tuần…) → `.claude/skills/`
- Quy trình gắn với một dự án/nền tảng cụ thể → `projects/<p>/.claude/skills/`

Mỗi skill có **mức tự động hoá** (ghi trong SKILL.md):
`L0 thủ công` → `L1 có checklist/prompt` → `L2 có script bán tự động` → `L3 chạy tự động theo lịch`.
Mục tiêu dài hạn là đẩy các skill cốt lõi lên L3.

## 4. Quy trình chuẩn cho một dự án

`Nghiên cứu → Insight → Giả thuyết → Test nhỏ (có KPI, có hạn) → Đánh giá → Nhân rộng → Tự động hoá`

- Không xây automation trước khi có ít nhất một test chứng minh hướng đi có tín hiệu.
- Mọi test phải có: giả thuyết, chỉ số đo, ngưỡng thành công/thất bại, thời hạn, chi phí tối đa.
- Mọi quyết định lớn (dừng, xoay hướng, đầu tư thêm) ghi vào `ops/DECISIONS.md` kèm số liệu.

## 5. Quy ước làm việc với Claude

- Thông tin chưa kiểm chứng (chính sách nền tảng, số liệu thị trường) phải gắn nhãn `[CẦN XÁC MINH]`
  kèm ngày, và ghi nguồn khi đã xác minh. Chính sách nền tảng thay đổi nhanh — luôn ghi ngày.
- Ngôn ngữ tài liệu: tiếng Việt; nội dung cho thị trường US viết bằng tiếng Anh.
- Tuân thủ chính sách nền tảng và pháp luật: công bố affiliate (disclosure), không reup vi phạm bản quyền
  nguyên trạng, không spam, không lời khuyên tài chính sai lệch. Ưu tiên tài khoản bền vững hơn lợi nhuận ngắn hạn.
- Khi thêm dự án mới: dùng skill `new-project` (hoặc `scripts/new-project.sh`) và cập nhật `projects/README.md`.
