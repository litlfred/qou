#!/usr/bin/env bash
#
# feature-build.sh — QUICK draft build for branch/feature iteration.
#
# Builds ONLY the changed sections (chapters), not the full paper, using the
# precompiled qou.fmt (so the heavy preamble isn't re-parsed), and emits a
# latexdiff of each changed chapter vs a base ref in BOTH colored and plain
# (monochrome) form. Numbers are the pipeline-fixed values (correct); cross-
# references to chapters not in this build resolve to '??' — acceptable for a
# preview. This is NOT a publish build; use publish.yml / the full build for
# the final PDF.
#
# Usage:
#   scripts/feature-build.sh [--base <ref>] [--chapters s1,s2] [--paper <dir>] [--out <dir>]
#     --base      diff against this ref            (default: origin/main)
#     --chapters  explicit chapter slugs, csv      (default: auto from git diff)
#     --paper     paper dir under content/         (default: quantum-observable-universe)
#     --out       output dir (gitignored)          (default: build-feature)
#
# Requires a TeX engine (run scripts/install-tex.sh first if absent) + bun.
#
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"; cd "$ROOT"
PAPER="quantum-observable-universe"; BASE="origin/main"; CHAPTERS=""; OUT="build-feature"
while [ $# -gt 0 ]; do case "$1" in
  --base) BASE="$2"; shift 2;;
  --chapters) CHAPTERS="$2"; shift 2;;
  --paper) PAPER="$2"; shift 2;;
  --out) OUT="$2"; shift 2;;
  *) echo "feature-build: unknown arg: $1" >&2; exit 2;;
esac; done
PAPERDIR="content/$PAPER"

echo "feature-build: [1/4] preamble format (qou.fmt)…"
bash scripts/build-fmt.sh --preamble latex/preamble.tex --name qou

echo "feature-build: [2/4] render chapters (cheap; pdflatex restricted to changed)…"
( cd content && bun run pipeline/build.ts "$PAPER/$PAPER.ts" \
    --out-dir ../chapters/ --generate-main --main-out ../main.tex \
    --preamble ../latex/preamble.tex --use-format qou --memoize >/dev/null 2>&1 ) \
  || echo "feature-build: (content build reported issues — continuing)"

if [ -z "$CHAPTERS" ]; then
  CHAPTERS="$(git diff --name-only "$BASE"...HEAD -- "$PAPERDIR/" 2>/dev/null \
    | sed -nE "s#^$PAPERDIR/([^/]+)/.*#\1#p" | sort -u | paste -sd, -)"
fi
[ -z "$CHAPTERS" ] && { echo "feature-build: no changed chapters vs $BASE — nothing to build."; exit 0; }
echo "feature-build: changed chapters → $CHAPTERS"

mkdir -p "$OUT"; cp -f qou.fmt "$OUT/"
IFS=',' read -ra CHS <<< "$CHAPTERS"

echo "feature-build: [3/4] quick changed-sections PDF…"
{ echo '%&qou'; echo '\begin{document}'
  for c in "${CHS[@]}"; do [ -f "chapters/$c.tex" ] && echo "\\input{$ROOT/chapters/$c}"; done
  echo '\end{document}'; } > "$OUT/changed.tex"
( cd "$OUT" && latexmk -pdf -shell-escape -f -interaction=nonstopmode changed.tex >changed.log 2>&1 || true )
[ -f "$OUT/changed.pdf" ] && echo "  → $OUT/changed.pdf" || echo "  ! changed.pdf not produced (see $OUT/changed.log)"

echo "feature-build: [4/4] per-chapter latexdiff (colored + plain)…"
command -v latexdiff >/dev/null 2>&1 || { echo "  (latexdiff not installed — skipping diffs)"; exit 0; }
for c in "${CHS[@]}"; do
  [ -f "chapters/$c.tex" ] || continue
  if git show "$BASE:chapters/$c.tex" > "$OUT/$c.base.tex" 2>/dev/null; then :; else
    echo "  $c: new chapter (no base) — diff = full content"; printf '' > "$OUT/$c.base.tex"
  fi
  # Colored markup (latexdiff default: blue add / red del, via xcolor+ulem in qou.fmt).
  latexdiff "$OUT/$c.base.tex" "chapters/$c.tex" > "$OUT/$c.body-color.tex" 2>/dev/null || true
  # Plain/monochrome: strip the \color{...} switches but keep \uwave/\sout markup.
  sed -E 's/\\color\{[a-zA-Z]+\}//g' "$OUT/$c.body-color.tex" > "$OUT/$c.body-plain.tex" || true
  for v in color plain; do
    { echo '%&qou'; echo '\begin{document}'
      echo "\\input{$ROOT/$OUT/$c.body-$v}"; echo '\end{document}'; } > "$OUT/$c.diff-$v.tex"
    ( cd "$OUT" && latexmk -pdf -shell-escape -f -interaction=nonstopmode "$c.diff-$v.tex" >/dev/null 2>&1 || true )
  done
  echo "  $c → $OUT/$c.diff-color.pdf , $OUT/$c.diff-plain.pdf"
done
echo "feature-build: done. (preview only — not a publish build)"
