# MMO HQ

Đầu não của tất cả dự án MMO: nghiên cứu → test → automation, mọi thao tác được lưu thành skill.

## Dự án đang chạy

| # | Dự án | Thị trường | Mô hình kiếm tiền | Phase |
|---|-------|-----------|-------------------|-------|
| 01 | [YouTube AI tài chính](projects/01-youtube-ai-finance/) | Theo kênh (mặc định: VN, cân nhắc EN) | AdSense, affiliate, sponsor | 0 · Nghiên cứu |
| 02 | [TikTok Shop VN · gia dụng](projects/02-tiktokshop-vn-giadung/) | Việt Nam | Hoa hồng affiliate (video + live) | 0 · Nghiên cứu |
| 03 | [Social US · Amazon Affiliate](projects/03-us-amazon-affiliate/) | Mỹ | Hoa hồng Amazon Associates | 0 · Nghiên cứu |

Registry đầy đủ: [`projects/README.md`](projects/README.md)

## Bắt đầu nhanh

- Luật chung, bố cục, vòng lặp skill: [`CLAUDE.md`](CLAUDE.md)
- Skill dùng chung: [`.claude/skills/`](.claude/skills/)
- Kiến thức chung (nền tảng, tool): [`shared/knowledge/`](shared/knowledge/)
- Tạo dự án mới: `scripts/new-project.sh 04-ten-du-an "Tên hiển thị"`

## Cách giao việc cho Claude

Nói rõ dự án + việc cần làm, ví dụ:

- "Dự án 03: chạy nghiên cứu nền tảng nào đang khai thác tốt Amazon affiliate"
- "Dự án 02: phân tích 10 kênh affiliate gia dụng top đầu"
- "Dự án 01: viết kịch bản video tuần này theo skill sản xuất"

Claude sẽ làm việc trong đúng thư mục dự án, ghi nhật ký, và tạo/cập nhật skill sau mỗi thao tác.
