#!/usr/bin/env bash
# paper-diff-pdf.sh — a latexdiff PDF of this branch against main, published to
# gh-pages under drafts/<branch>/: the PDF counterpart of the site's
# STAGING/<branch>/ preview.
#
#   scripts/paper-diff-pdf.sh [--base FLAT.tex] [--no-push] [--paper SLUG] [--branch NAME]
#
#   1. build this branch (scripts/build-paper-pdf.sh -> build/paper/)
#   2. flatten it (latexpand, bibliography inlined from main.bbl)
#   3. the BASE is main's flattened source as last published
#      (gh-pages papers/<slug>/<slug>.flat.tex, written by publish-paper-pdf.sh),
#      so main is never rebuilt here; --base overrides it
#   4. latexdiff base -> branch, compile with latexmk -f
#   5. publish drafts/<branch>/<slug>.pdf, <slug>-diff.pdf, <slug>-diff.json
#
# Run by an agent after a commit (when Actions billing blocks CI) or by
# .github/workflows/paper-pdf.yml on dispatch. A diff that fails to compile is
# still reported (and the branch PDF still published), never silently dropped.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PAPER="quantum-observable-universe"
BASE=""
PUSH=true
BRANCH="$(git -C "$ROOT" rev-parse --abbrev-ref HEAD)"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --base)    BASE="$2"; shift 2 ;;
    --paper)   PAPER="$2"; shift 2 ;;
    --branch)  BRANCH="$2"; shift 2 ;;
    --no-push) PUSH=false; shift ;;
    -h|--help) sed -n 2,19p "$0"; exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
done
[ "$BRANCH" != HEAD ] || { echo "detached HEAD: pass --branch NAME" >&2; exit 2; }
command -v latexdiff >/dev/null || { echo "latexdiff not found (apt: latexdiff)" >&2; exit 2; }
cd "$ROOT"
SHA=$(git rev-parse HEAD); SHORT=$(git rev-parse --short HEAD)
OUT="$ROOT/build/paper"
DIFF="$ROOT/build/paper-diff"

echo "==> branch build"
bash scripts/build-paper-pdf.sh --paper "$PAPER" --out-dir "$OUT"
( cd "$OUT" && latexpand --expand-bbl main.bbl main.tex > main-flat.tex )

mkdir -p "$DIFF"
if [ -z "$BASE" ]; then
  git fetch -q --depth 1 origin gh-pages
  if ! git cat-file -e "FETCH_HEAD:papers/$PAPER/$PAPER.flat.tex" 2>/dev/null; then
    echo "no published baseline (gh-pages papers/$PAPER/$PAPER.flat.tex); run publish-paper-pdf.sh on main first" >&2
    exit 1
  fi
  git show "FETCH_HEAD:papers/$PAPER/$PAPER.flat.tex" > "$DIFF/base-flat.tex"
  BASE_COMMIT=$( { git show "FETCH_HEAD:papers/$PAPER/$PAPER.json" 2>/dev/null || echo '{}'; } \
    | python3 -I -c 'import json,sys; print(json.load(sys.stdin).get("commit","unknown"))')
else
  cp "$BASE" "$DIFF/base-flat.tex"; BASE_COMMIT="(--base $BASE)"
fi

echo "==> latexdiff (base $BASE_COMMIT -> $SHORT)"
for d in figures assets; do [ -e "$ROOT/$d" ] && [ ! -e "$DIFF/$d" ] && ln -s "$ROOT/$d" "$DIFF/$d"; done
start=$(date +%s)
latexdiff --type=UNDERLINE --math-markup=coarse --allow-spaces \
  "$DIFF/base-flat.tex" "$OUT/main-flat.tex" > "$DIFF/main-diff.tex" 2> "$DIFF/latexdiff.log" || true
ldsecs=$(( $(date +%s) - start ))
set +e
( cd "$DIFF" && latexmk -pdf -f -interaction=nonstopmode -file-line-error main-diff.tex > latexmk.log 2>&1 )
rc=$?
set -e
L="$DIFF/main-diff.log"
errs=$( { grep -c '^\./.*:[0-9]*: \|^! ' "$L" 2>/dev/null || true; } )
pages=$( { grep -oE '\(([0-9]+) pages' "$L" 2>/dev/null || true; } | tail -1 | tr -dc 0-9)
added=$(grep -c '\\DIFadd' "$DIFF/main-diff.tex" || true)
deleted=$(grep -c '\\DIFdel' "$DIFF/main-diff.tex" || true)
echo "==> diff: pages=${pages:-0} latex-errors=${errs:-0} latexmk-exit=$rc DIFadd=$added DIFdel=$deleted latexdiff=${ldsecs}s"

META="$DIFF/main-diff.json"
python3 -I - "$META" <<PY
import json, sys
json.dump({
  "\$schema": "qou-paper-diff/v1", "paper": "$PAPER", "branch": "$BRANCH",
  "commit": "$SHA", "baseCommit": "$BASE_COMMIT",
  "diffPages": int("${pages:-0}" or 0), "latexErrors": int("${errs:-0}" or 0),
  "latexmkExit": $rc, "addMarks": $added, "deleteMarks": $deleted,
  "builtBy": "scripts/paper-diff-pdf.sh",
}, open(sys.argv[1], "w"), indent=2)
PY

dest="drafts/$BRANCH"
args=(-m "paper diff: $BRANCH at $SHORT vs main ${BASE_COMMIT:0:9}" \
  "$dest/$PAPER.pdf=$OUT/main.pdf" "$dest/$PAPER-diff.json=$META")
[ -f "$DIFF/main-diff.pdf" ] && args+=("$dest/$PAPER-diff.pdf=$DIFF/main-diff.pdf")
$PUSH || args=(--no-push "${args[@]}")
res=$(bash scripts/lib/gh-pages-put.sh "${args[@]}")
echo "    gh-pages commit: $res"
if $PUSH && [ "$res" != unchanged ]; then
  echo "branch PDF: https://github.com/litlfred/qou/blob/gh-pages/$dest/$PAPER.pdf"
  [ -f "$DIFF/main-diff.pdf" ] && echo "diff PDF:   https://github.com/litlfred/qou/blob/gh-pages/$dest/$PAPER-diff.pdf"
fi
[ -f "$DIFF/main-diff.pdf" ] || { echo "diff PDF did not compile; see $DIFF/latexmk.log" >&2; exit 1; }
