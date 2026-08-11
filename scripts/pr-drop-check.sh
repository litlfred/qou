#!/usr/bin/env bash
# pr-drop-check.sh — find edits a consolidated PR lost on the way to main.
#
# Why this exists (see #4840 on PR #4824, and the #4671 incident it cites):
# deliverable-level tracing — "the headline artifact is on main, so the branch
# landed" — cannot see a dropped edit to a file that was modified on BOTH
# sides. The file still exists, still holds most of the branch's work, and the
# named deliverable really did land. Only a per-file read finds the loss.
#
# Usage:
#   scripts/pr-drop-check.sh 3793 4551 4519          # by PR number
#   BASE=origin/develop scripts/pr-drop-check.sh 42  # against a non-main base
#
# Verdicts:
#   (clean)         branch == main; landed byte-identical
#   DROP            main never touched it and the branch content is absent
#   BOTH-MODIFIED   both sides changed it — READ THE DIFF, this is the
#                   dangerous case; main newer is fine, branch-only is a loss
#   GONE-FROM-MAIN  file no longer on main; check it was deleted deliberately
#
# Only files the branch MODIFIED are examined. Pure additions land or conflict
# loudly, so they are not at risk and would only add noise.
#
# Docs: docs/audits/2026-08-09-pr4824-consolidation-file-level-drop-check.md

set -uo pipefail

BASE="${BASE:-origin/main}"
REMOTE="${REMOTE:-origin}"

if [ "$#" -eq 0 ]; then
  sed -n '2,26p' "$0" | sed 's/^# \?//'
  exit 2
fi

# A shallow clone silently yields an EMPTY merge-base rather than an error,
# which makes every file look like a drop. Deepen both sides before trusting
# anything below.
if [ "$(git rev-parse --is-shallow-repository)" = "true" ]; then
  echo "note: shallow clone — deepening ${BASE} and PR refs (may take a minute)" >&2
  git fetch -q --deepen=1200 "$REMOTE" "${BASE#*/}" 2>/dev/null || true
fi

status=0

for pr in "$@"; do
  ref="refs/prheads/$pr"
  git fetch -q "$REMOTE" "refs/pull/$pr/head:$ref" 2>/dev/null \
    || { echo "=== PR #$pr — could not fetch refs/pull/$pr/head"; status=1; continue; }
  git fetch -q --deepen=400 "$REMOTE" "refs/pull/$pr/head:$ref" 2>/dev/null || true

  mb=$(git merge-base "$BASE" "$ref" 2>/dev/null || true)
  if [ -z "$mb" ]; then
    echo "=== PR #$pr — no merge-base with $BASE (deepen further); SKIPPED"
    status=1
    continue
  fi

  echo "=== PR #$pr (base ${mb:0:8}) ==="
  findings=0
  while IFS= read -r f; do
    [ -n "$f" ] || continue
    a=$(git rev-parse "$mb:$f"   2>/dev/null || true)
    b=$(git rev-parse "$ref:$f"  2>/dev/null || true)
    m=$(git rev-parse "$BASE:$f" 2>/dev/null || true)
    if [ -z "$m" ]; then
      echo "  GONE-FROM-MAIN  $f"; findings=1; continue
    fi
    [ "$b" = "$m" ] && continue                     # landed identical
    if [ "$a" = "$m" ]; then
      echo "  DROP            $f"                    # main untouched, content absent
    else
      echo "  BOTH-MODIFIED   $f"                    # needs a line-level read
    fi
    findings=1
  done < <(git diff --name-status --diff-filter=M "$mb" "$ref" | cut -f2)

  [ "$findings" -eq 0 ] && echo "  (clean — no modified-file divergence)"
done

echo
echo "Read the direction on every DROP / BOTH-MODIFIED above:"
echo "  git diff $BASE refs/prheads/<pr> -- <file>"
exit $status
