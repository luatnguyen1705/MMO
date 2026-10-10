#!/usr/bin/env bash
# Tạo dự án mới từ khung chuẩn.
# Dùng: scripts/new-project.sh <NN-slug> "<Tên hiển thị>"
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "Dùng: $0 <NN-slug> \"<Tên hiển thị>\"" >&2
  exit 1
fi

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SLUG="$1"
NAME="$2"
DEST="$ROOT/projects/$SLUG"
TODAY="$(date +%F)"

if [[ ! "$SLUG" =~ ^[0-9]{2}-[a-z0-9-]+$ ]]; then
  echo "Slug phải dạng NN-ten-du-an (chữ thường, gạch nối)" >&2
  exit 1
fi
if [[ -e "$DEST" ]]; then
  echo "Đã tồn tại: $DEST" >&2
  exit 1
fi

cp -r "$ROOT/shared/templates/project" "$DEST"
grep -rl '{{NAME}}\|{{DATE}}' "$DEST" | while read -r f; do
  sed -i "s|{{NAME}}|$NAME|g; s|{{DATE}}|$TODAY|g" "$f"
done
echo "- $TODAY — Khởi tạo dự án từ khung chuẩn — OK — new-project" >> "$DEST/ops/JOURNAL.md"

echo "Đã tạo $DEST"
echo "Việc tiếp theo: điền README.md, CLAUDE.md, research/RESEARCH-PLAN.md và thêm dòng vào projects/README.md"
