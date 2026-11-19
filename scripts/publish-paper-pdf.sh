#!/usr/bin/env bash
# publish-paper-pdf.sh — build the paper PDF and publish it to gh-pages.
#
#   scripts/publish-paper-pdf.sh [--pdf FILE] [--no-push] [--paper SLUG]
#
# One command, the same in CI (.github/workflows/paper-pdf.yml, on every merge
# to main) and in an agent session (when Actions billing blocks CI, an agent
# runs this after its merge, or after any commit it wants published).
#
# Writes exactly three files on gh-pages, and nothing else in that tree:
#   papers/<slug>/<slug>.pdf       the PDF the root README's "full PDF" link serves
#   papers/<slug>/<slug>.json      {commit, date, pages, bytes, errors, ...}
#   papers/<slug>/<slug>.flat.tex  flattened source: the baseline for branch diffs
#
# Written with scripts/lib/gh-pages-put.sh (git plumbing, no checkout of the
# ~17k-file tree, fast-forward-only push).
#
# Refuses to publish a PDF whose final-pass log has LaTeX errors or undefined
# citations/references (the gate in build-paper-pdf.sh), or from a dirty tree
# under folio/ (the stamp would name a commit the PDF does not come from).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
. "$ROOT/scripts/lib/paper-env.sh"
PAPER="$DEFAULT_PAPER"
PDF=""
PUSH=true
while [[ $# -gt 0 ]]; do
  case "$1" in
    --pdf)     PDF="$2"; shift 2 ;;
    --paper)   PAPER="$2"; shift 2 ;;
    --no-push) PUSH=false; shift ;;
    -h|--help) sed -n 2,23p "$0"; exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
done
cd "$ROOT"

if [ -n "$(git status --porcelain -- folio references.bib)" ]; then
  echo "refusing: uncommitted changes under folio/ or references.bib" >&2; exit 2
fi
SHA=$(git rev-parse HEAD)
SHORT=$(git rev-parse --short HEAD)

OUT="$ROOT/build/paper"
if [ -z "$PDF" ]; then
  bash scripts/build-paper-pdf.sh --paper "$PAPER" --out-dir "$OUT"
  PDF="$OUT/main.pdf"
fi
LOG="$(dirname "$PDF")/main.log"
[ -f "$PDF" ] || { echo "no PDF at $PDF" >&2; exit 1; }
[ -f "$LOG" ] || { echo "no main.log beside $PDF; cannot gate" >&2; exit 1; }

errs=$(grep -c '^\./.*:[0-9]*: \|^! ' "$LOG" || true)
cites=$(grep -c 'Citation .* undefined' "$LOG" || true)
refs=$(grep -c 'LaTeX Warning: Reference' "$LOG" || true)
pages=$( { grep -oE '\(([0-9]+) pages' "$LOG" || true; } | tail -1 | tr -dc 0-9)
if [ "$errs" != 0 ] || [ "$cites" != 0 ] || [ "$refs" != 0 ]; then
  echo "refusing to publish: errors=$errs undefined-citations=$cites undefined-refs=$refs" >&2; exit 1
fi
bytes=$(wc -c < "$PDF" | tr -d ' ')
date=$(git show -s --format=%cI HEAD)

META=$(mktemp)
trap 'rm -f "$META"' EXIT
python3 -I - "$META" <<PY
import json, sys
json.dump({
  "\$schema": "folio-paper-pdf/v1",
  "paper": "$PAPER",
  "commit": "$SHA",
  "commitDate": "$date",
  "pages": int("${pages:-0}"),
  "bytes": $bytes,
  "latexErrors": $errs,
  "undefinedCitations": $cites,
  "undefinedReferences": $refs,
  "builtBy": "scripts/publish-paper-pdf.sh",
}, open(sys.argv[1], "w"), indent=2)
PY

# The flattened, self-contained LaTeX source (chapters inlined, bibliography
# inlined from main.bbl). Published beside the PDF, it is the cached baseline a
# branch diff runs latexdiff against (scripts/paper-diff-pdf.sh), so a diff
# never rebuilds main.
FLAT="$(dirname "$PDF")/main-flat.tex"
( cd "$(dirname "$PDF")" && latexpand --expand-bbl main.bbl main.tex > main-flat.tex )

echo "==> gh-pages: papers/$PAPER/ (${pages} pp, $bytes bytes, from $SHORT)"
args=(-m "paper PDF: $PAPER at $SHORT (${pages} pages)

Built by scripts/publish-paper-pdf.sh from $SHA."
  "papers/$PAPER/$PAPER.pdf=$PDF"
  "papers/$PAPER/$PAPER.json=$META"
  "papers/$PAPER/$PAPER.flat.tex=$FLAT")
$PUSH || args=(--no-push "${args[@]}")
res=$(bash "$ROOT/scripts/lib/gh-pages-put.sh" "${args[@]}")
echo "    gh-pages commit: $res"
$PUSH && [ "$res" != unchanged ] && echo "published: $GHPAGES_BLOB/papers/$PAPER/$PAPER.pdf"
exit 0
