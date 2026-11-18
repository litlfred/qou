#!/usr/bin/env bash
# publish-paper-pdf.sh — build the paper PDF and publish it to gh-pages.
#
#   scripts/publish-paper-pdf.sh [--pdf FILE] [--no-push] [--paper SLUG]
#
# One command, the same in CI (.github/workflows/paper-pdf.yml, on every merge
# to main) and in an agent session (when Actions billing blocks CI, an agent
# runs this after its merge, or after any commit it wants published).
#
# Writes exactly two files on gh-pages, and nothing else in that tree:
#   papers/<slug>/<slug>.pdf     the PDF the root README's "full PDF" link serves
#   papers/<slug>/<slug>.json    {commit, date, pages, bytes, errors, ...}
#
# gh-pages is large (~17k files), so it is never checked out: the commit is
# built with git plumbing on a shallow fetch (read-tree into a temp index,
# update-index the two blobs, write-tree, commit-tree), then pushed with a
# fast-forward-only push. A concurrent publish makes the push fail rather than
# overwrite; re-run it.
#
# Refuses to publish a PDF whose final-pass log has LaTeX errors or undefined
# citations/references (the gate in build-paper-pdf.sh), or from a dirty tree
# under folio/ (the stamp would name a commit the PDF does not come from).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PAPER="quantum-observable-universe"
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
trap 'rm -f "$META" "${IDX:-}"' EXIT
python3 -I - "$META" <<PY
import json, sys
json.dump({
  "\$schema": "qou-paper-pdf/v1",
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

echo "==> gh-pages: papers/$PAPER/$PAPER.pdf (${pages} pp, $bytes bytes, from $SHORT)"
git fetch -q --depth 1 origin gh-pages
PARENT=$(git rev-parse FETCH_HEAD)
IDX=$(mktemp)
export GIT_INDEX_FILE="$IDX"
git read-tree "$PARENT"
pdf_blob=$(git hash-object -w "$PDF")
meta_blob=$(git hash-object -w "$META")
git update-index --add --cacheinfo 100644 "$pdf_blob" "papers/$PAPER/$PAPER.pdf"
git update-index --add --cacheinfo 100644 "$meta_blob" "papers/$PAPER/$PAPER.json"
TREE=$(git write-tree)
unset GIT_INDEX_FILE
if [ "$TREE" = "$(git rev-parse "$PARENT^{tree}")" ]; then
  echo "gh-pages already has this PDF; nothing to publish"; exit 0
fi
COMMIT=$(printf 'paper PDF: %s at %s (%s pages)\n\nBuilt by scripts/publish-paper-pdf.sh from %s.\n' \
  "$PAPER" "$SHORT" "$pages" "$SHA" | git commit-tree "$TREE" -p "$PARENT")
echo "    commit $COMMIT (parent $PARENT)"
if $PUSH; then
  git push origin "$COMMIT:refs/heads/gh-pages"
  echo "published: https://github.com/litlfred/qou/blob/gh-pages/papers/$PAPER/$PAPER.pdf"
else
  echo "--no-push: not pushed"
fi
