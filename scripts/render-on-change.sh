#!/usr/bin/env bash
#
# Hook script: re-render TeX blocks and export JSON when content .md files change.
#
# Called by Claude Code PostToolUse hook after Edit/Write operations.
# Checks if any .md files under content/ were modified and triggers:
#   1. TeX block rendering (installing pdflatex/dvisvgm if needed)
#   2. JSON export for the viewer
#
# Exit 0 always — rendering failures should not block the edit.
#
set -uo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# Only trigger for content .md file changes
if ! git diff --name-only 2>/dev/null | grep -q '^content/.*\.md$'; then
  exit 0
fi

echo "[render-on-change] Content .md file changed, re-rendering..."

# Auto-install pdflatex + dvisvgm if missing
if ! command -v pdflatex &>/dev/null || ! command -v dvisvgm &>/dev/null; then
  echo "[render-on-change] Installing TeX dependencies..."
  sudo apt-get update -qq 2>/dev/null
  sudo apt-get install -y -qq texlive-latex-base texlive-latex-extra \
    texlive-fonts-recommended texlive-pictures dvisvgm 2>/dev/null || true
fi

# Re-render TeX blocks
if command -v pdflatex &>/dev/null && command -v dvisvgm &>/dev/null; then
  bun run "$REPO_ROOT/scripts/render-tex/render-tex-blocks.ts" 2>&1 | sed 's/^/  /' || true
else
  echo "[render-on-change] WARNING: pdflatex/dvisvgm not available, SVGs may be stale"
fi

# Re-export JSON for viewer
if command -v bun &>/dev/null; then
  bun run "$REPO_ROOT/content/pipeline/export-json.ts" 2>&1 | sed 's/^/  /' || true
fi

echo "[render-on-change] Done."
