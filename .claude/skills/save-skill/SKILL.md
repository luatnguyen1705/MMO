---
name: save-skill
description: Tạo skill mới hoặc cập nhật skill có sẵn sau khi hoàn thành một thao tác trong bất kỳ dự án MMO nào. Dùng sau mỗi tác vụ có ý nghĩa, khi người dùng nói "lưu thành skill", "cập nhật skill", hoặc khi một quy trình vừa làm sẽ còn lặp lại.
---

# save-skill — Biến thao tác thành tài sản

**Mức tự động hoá:** L1 (checklist) · **Phạm vi:** dùng chung

## Khi nào dùng
- Vừa hoàn thành một việc sẽ lặp lại (nghiên cứu, viết kịch bản, đăng bài, phân tích số liệu…).
- Một skill có sẵn vừa được dùng và phát hiện bước thiếu/sai/thừa.
- Người dùng yêu cầu lưu lại cách làm.

## Các bước

1. **Xác định phạm vi**
   - Dùng được cho nhiều dự án → `.claude/skills/<ten-skill>/SKILL.md`
   - Gắn với một dự án → `projects/<p>/.claude/skills/<ten-skill>/SKILL.md`
2. **Tìm skill trùng/gần giống** (`ls .claude/skills projects/*/.claude/skills`). Ưu tiên cập nhật hơn tạo mới.
   Nếu skill dự án hoá ra dùng chung được → chuyển lên `.claude/skills/` và để lại 1 dòng trỏ tới.
3. **Tạo mới**: copy `shared/templates/SKILL.template.md`, điền đủ các mục. Tên: chữ thường, gạch nối, động từ/danh từ rõ nghĩa
   (vd `script-video-finance`, `source-douyin-video`).
   `description` trong frontmatter phải nói rõ **làm gì + khi nào dùng** — đây là thứ quyết định skill có được kích hoạt hay không.
4. **Cập nhật**: sửa bước, thêm vào mục **Bài học** (cái gì hiệu quả / không hiệu quả, kèm số liệu nếu có),
   thêm 1 dòng **Changelog** `YYYY-MM-DD — thay đổi gì — vì sao`.
5. **Đánh giá mức tự động hoá** (L0–L3). Nếu skill đã chạy ổn ≥3 lần ở L1 → ghi đề xuất nâng lên L2 vào mục "Hướng tự động hoá".
6. **Ghi nhật ký**: 1 dòng vào `projects/<p>/ops/JOURNAL.md` (hoặc bỏ qua nếu skill thuần chung).
7. Nếu là skill dự án, cập nhật bảng skill trong `projects/<p>/README.md`.

## Tiêu chuẩn một skill tốt
- Người/agent khác đọc xong làm được ngay, không cần hỏi lại.
- Có input rõ, output rõ (file nào, đặt ở đâu, định dạng gì).
- Có checklist kiểm tra chất lượng trước khi coi là xong.
- Ngắn gọn: chi tiết dài (prompt mẫu, ví dụ) tách ra file cạnh SKILL.md và trỏ tới.

## Bài học
- (chưa có)

## Changelog
- 2026-10-10 — Tạo skill.
