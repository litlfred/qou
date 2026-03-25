#!/usr/bin/env bash
#
# PreCommit hook: ensure rendered SVGs are up-to-date before committing.
#
# If any content .md files with ```tex blocks are staged, re-renders
# their SVGs and stages the updated SVGs + hashes + .ts manifests.
#
# Exit 0 always — we don't want rendering failures to block commits,
# but we do want to auto-fix stale SVGs when possible.
#
set -uo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# Check if any content .md files are staged
if ! git diff --cached --name-only 2>/dev/null | grep -q '^content/.*\.md$'; then
  exit 0
fi

# Need pdflatex + dvisvgm
if ! command -v pdflatex &>/dev/null || ! command -v dvisvgm &>/dev/null; then
  echo "[pre-commit] WARNING: pdflatex/dvisvgm not installed — SVGs may be stale"
  exit 0
fi

echo "[pre-commit] Re-rendering TeX blocks for staged .md files..."

# Run the renderer (hash-based — only re-renders changed blocks)
bun run "$REPO_ROOT/scripts/render-tex/render-tex-blocks.ts" 2>&1 | sed 's/^/  /' || true

# Stage any updated SVGs, hashes, and .ts manifests
git diff --name-only -- 'content/*/rendered/*.svg' 'content/*/rendered/*.svg.hash' 'content/*/*.ts' 2>/dev/null | while read -r f; do
  git add "$f" 2>/dev/null
done

# Also catch nested chapter dirs (content/paper/chapter/rendered/*)
git diff --name-only -- 'content/*/*/rendered/*.svg' 'content/*/*/rendered/*.svg.hash' 'content/*/*/*.ts' 2>/dev/null | while read -r f; do
  git add "$f" 2>/dev/null
done

echo "[pre-commit] SVG rendering complete."
exit 0
