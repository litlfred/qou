#!/usr/bin/env bash
# gh-pages-put.sh — commit files onto gh-pages WITHOUT checking it out.
#
#   scripts/lib/gh-pages-put.sh [--no-push] -m "<message>" <dest>=<src> [<dest>=<src> ...]
#   scripts/lib/gh-pages-put.sh [--no-push] -m "<message>" --tree <prefix>=<dir>
#
# --tree REPLACES the whole <prefix>/ subtree with the contents of <dir>, in the
# same single commit: every entry under <prefix>/ is dropped and every file of
# <dir> is added beneath it. Nothing outside <prefix>/ changes. Used to publish
# the Lean doc-gen4 render under lean/ (owner, 2026-11-19).
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
trees=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --no-push) PUSH=false; shift ;;
    -m) MSG="$2"; shift 2 ;;
    --tree) trees+=("$2"); shift 2 ;;
    *=*) pairs+=("$1"); shift ;;
    *) echo "gh-pages-put: bad argument: $1" >&2; exit 2 ;;
  esac
done
[ -n "$MSG" ] && [ $(( ${#pairs[@]} + ${#trees[@]} )) -gt 0 ] || { echo "usage: gh-pages-put.sh [--no-push] -m MSG dest=src ..." >&2; exit 2; }

git fetch -q --depth 1 origin gh-pages
PARENT=$(git rev-parse FETCH_HEAD)
IDX=$(mktemp)
trap 'rm -f "$IDX" "$IDX.list" "$IDX.sha"' EXIT
export GIT_INDEX_FILE="$IDX"
git read-tree "$PARENT"
for p in "${pairs[@]}"; do
  dest=${p%%=*}; src=${p#*=}
  [ -f "$src" ] || { echo "gh-pages-put: missing $src" >&2; exit 1; }
  git update-index --add --cacheinfo 100644 "$(git hash-object -w "$src")" "$dest"
done
for t in ${trees[@]+"${trees[@]}"}; do
  prefix=${t%%=*}; prefix=${prefix%/}; dir=${t#*=}
  case "$prefix" in ""|.|/*|*..*) echo "gh-pages-put: refusing --tree prefix '$prefix'" >&2; exit 2 ;; esac
  [ -d "$dir" ] || { echo "gh-pages-put: missing directory $dir" >&2; exit 1; }
  git rm -r -q --cached --ignore-unmatch -- "$prefix" >/dev/null
  ( cd "$dir" && find . -type f -printf '%P\n' | LC_ALL=C sort ) > "$IDX.list"
  GD=$(git rev-parse --absolute-git-dir)
  ( cd "$dir" && git --git-dir="$GD" hash-object -w --stdin-paths < "$IDX.list" ) > "$IDX.sha"
  paste -d '\t' "$IDX.sha" "$IDX.list" \
    | awk -v pfx="$prefix/" -F '\t' '{ printf "100644 %s\t%s%s\n", $1, pfx, $2 }' \
    | git update-index --add --index-info
  echo "gh-pages-put: $prefix/ <- $dir ($(wc -l < "$IDX.list") files)" >&2
  rm -f "$IDX.list" "$IDX.sha"
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
