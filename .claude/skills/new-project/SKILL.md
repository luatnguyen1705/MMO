---
name: new-project
description: Khởi tạo một dự án MMO mới trong repo theo khung chuẩn (thư mục, README, CLAUDE.md, journal, registry). Dùng khi người dùng muốn thêm dự án/kênh/mô hình kiếm tiền mới.
---

# new-project — Khởi tạo dự án mới

**Mức tự động hoá:** L2 (có script) · **Phạm vi:** dùng chung

## Input
- Số thứ tự + slug (vd `04-pinterest-etsy`), tên hiển thị, thị trường, mô hình kiếm tiền, mục tiêu ban đầu.

## Các bước
1. Chạy `scripts/new-project.sh <NN-slug> "<Tên hiển thị>"` — copy khung từ `shared/templates/project/`.
2. Điền `projects/<p>/README.md`: mục tiêu, KPI, phase, ngân sách test, rủi ro chính.
3. Điền `projects/<p>/CLAUDE.md`: bối cảnh, đối tượng, nền tảng, luật riêng (chính sách cần tuân thủ), tool bên ngoài.
4. Thêm dòng vào `projects/README.md` và bảng trong `README.md` gốc.
5. Tạo `research/RESEARCH-PLAN.md` liệt kê câu hỏi cần trả lời trước khi test.
6. Ghi dòng đầu tiên vào `ops/JOURNAL.md` và quyết định khởi tạo vào `ops/DECISIONS.md`.

## Checklist
- [ ] Không có dữ liệu của dự án khác bị copy sang
- [ ] Có KPI và tiêu chí dừng
- [ ] Registry đã cập nhật

## Bài học
- (chưa có)

## Changelog
- 2026-10-10 — Tạo skill.
