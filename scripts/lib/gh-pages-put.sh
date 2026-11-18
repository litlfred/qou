#!/usr/bin/env bash
# gh-pages-put.sh — commit files onto gh-pages WITHOUT checking it out.
#
#   scripts/lib/gh-pages-put.sh [--no-push] -m "<message>" <dest>=<src> [<dest>=<src> ...]
#
# gh-pages holds ~17k files (lean/, drafts/, STAGING/ ...), so a checkout is
# slow and a worktree is gigabytes. This builds the commit with git plumbing on
# a depth-1 fetch: read-tree into a temp index, update-index each blob,
# write-tree, commit-tree on the fetched tip, then a fast-forward-only push.
# A concurrent writer makes the push fail instead of overwriting; re-run.
# Only the named <dest> paths change. Prints the new commit (or "unchanged").
set -euo pipefail
PUSH=true; MSG=""
pairs=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --no-push) PUSH=false; shift ;;
    -m) MSG="$2"; shift 2 ;;
    *=*) pairs+=("$1"); shift ;;
    *) echo "gh-pages-put: bad argument: $1" >&2; exit 2 ;;
  esac
done
[ -n "$MSG" ] && [ ${#pairs[@]} -gt 0 ] || { echo "usage: gh-pages-put.sh [--no-push] -m MSG dest=src ..." >&2; exit 2; }

git fetch -q --depth 1 origin gh-pages
PARENT=$(git rev-parse FETCH_HEAD)
IDX=$(mktemp)
trap 'rm -f "$IDX"' EXIT
export GIT_INDEX_FILE="$IDX"
git read-tree "$PARENT"
for p in "${pairs[@]}"; do
  dest=${p%%=*}; src=${p#*=}
  [ -f "$src" ] || { echo "gh-pages-put: missing $src" >&2; exit 1; }
  git update-index --add --cacheinfo 100644 "$(git hash-object -w "$src")" "$dest"
done
TREE=$(git write-tree)
unset GIT_INDEX_FILE
if [ "$TREE" = "$(git rev-parse "$PARENT^{tree}")" ]; then
  echo "unchanged"; exit 0
fi
COMMIT=$(printf '%s\n' "$MSG" | git commit-tree "$TREE" -p "$PARENT")
if $PUSH; then
  git push -q origin "$COMMIT:refs/heads/gh-pages"
fi
echo "$COMMIT"
