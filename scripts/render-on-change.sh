#!/usr/bin/env bash
#
# Hook script: re-render TeX blocks and export JSON when content .md files change.
#
# Called by Claude Code PostToolUse hook after Edit/Write operations.
# Checks if any .md files under content/ were modified and triggers:
#   1. TeX block rendering (if pdflatex available)
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

# Re-render TeX blocks if pdflatex is available
if command -v pdflatex &>/dev/null && command -v dvisvgm &>/dev/null; then
  bun run "$REPO_ROOT/scripts/render-tex/render-tex-blocks.ts" 2>&1 | sed 's/^/  /' || true
fi

# Re-export JSON for viewer
if command -v bun &>/dev/null; then
  bun run "$REPO_ROOT/content/pipeline/export-json.ts" 2>&1 | sed 's/^/  /' || true
fi

echo "[render-on-change] Done."
