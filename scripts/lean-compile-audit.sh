#!/bin/bash
# Run the lean compile audit end-to-end.
# Usage: ./scripts/lean-compile-audit.sh
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

# ── Install elan if missing ─────────────────────────────────────
if ! command -v lean &>/dev/null && ! [ -f "$HOME/.elan/bin/lean" ]; then
  echo "Installing elan (Lean toolchain manager)..."
  curl https://elan.lean-lang.org/install.sh -sSf | sh -s -- -y
fi
export PATH="$HOME/.elan/bin:$PATH"

# ── Install bun if missing ──────────────────────────────────────
if ! command -v bun &>/dev/null; then
  echo "Installing bun..."
  curl -fsSL https://bun.sh/install | bash
  export PATH="$HOME/.bun/bin:$PATH"
fi

# ── Fetch Mathlib cache + build ─────────────────────────────────
echo "Fetching Mathlib cache..."
lake exe cache get 2>/dev/null || true

echo "Building Lean (this may take a while on first run)..."
lake build || echo "Build had errors — continuing to collect diagnostics"

# ── Install content deps ────────────────────────────────────────
(cd content && bun install --frozen-lockfile 2>/dev/null || bun install)

# ── Collect diagnostics ─────────────────────────────────────────
echo "Collecting diagnostics from .lean files..."
TARGETS=$(bun run content/pipeline/lean-compile-audit.ts --list 2>/dev/null \
  | grep '\.lean$')
TOTAL=$(echo "$TARGETS" | wc -l)
JSONL=$(mktemp /tmp/lean-diag.XXXXXX.jsonl)
COUNT=0

echo "$TARGETS" | while IFS= read -r f; do
  COUNT=$((COUNT + 1))
  printf "\r[%d/%d] %s" "$COUNT" "$TOTAL" "$f"
  DIAG=$(lake env lean "$f" 2>&1 | grep ': error:' | head -10 || true)
  ENTRIES=""
  if [ -n "$DIAG" ]; then
    ENTRIES=$(echo "$DIAG" | while IFS= read -r line; do
      LN=$(echo "$line" | sed -n 's/.*:\([0-9]*\):[0-9]*: error:.*/\1/p')
      MSG=$(echo "$line" | sed 's/.*: error: //' | cut -c1-500 | sed 's/"/\\"/g; s/\\/\\\\/g')
      printf '{"line":%s,"severity":"error","message":"%s"},' "${LN:-0}" "$MSG"
    done | sed 's/,$//')
  fi
  echo "{\"file\":\"$f\",\"diagnostics\":[$ENTRIES]}" >> "$JSONL"
done
echo ""

# ── Ingest + sweep ──────────────────────────────────────────────
echo "Ingesting diagnostics..."
bun run content/pipeline/lean-compile-audit.ts --ingest "$JSONL"

echo "Running QA sweep..."
bun run content/pipeline/qa-sweep.ts content/ --only proof-lean-compiles

rm -f "$JSONL"

# ── Commit + push results ──────────────────────────────────────
echo "Committing results..."
git add docs/audits/lean-compile-diagnostics.json
git add 'content/**/*.qa.json'
git diff --cached --quiet || git commit -m "audit: lean compile diagnostics + sidecar entries"
git push

echo "Done."
