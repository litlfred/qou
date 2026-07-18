#!/usr/bin/env bash
# Seed / reseed the lake-cache/qou-<toolchain-slug> orphan branch with a
# CLEAN, single-rev olean set.
#
# Cleanliness contract (see docs/audits/2026-07-13-mathlib-cache-f897ebc-revskew.md):
# only mathlib oleans that were REBUILT this session from the pinned source
# (listed in $BUILT_FILE) are included — never a mix of pre-/post-pin oleans.
# Non-mathlib package oleans (batteries/aesop/Qq/…) are rev-independent and
# included as-is; the qou/ugb/fred2005 package oleans are included if present.
#
# Usage: scripts/lean-olean-cache-seed.sh [--push]
#   (dry by default: builds the tarball + parts, prints size; --push commits
#    the orphan branch and force-pushes it)
set -euo pipefail
ROOT="$(git -C "$(dirname "$0")/.." rev-parse --show-toplevel)"
cd "$ROOT"
BUILT_FILE="${BUILT_FILE:-/tmp/parbuild_built.txt}"
SLUG="$(cut -d: -f2 lean-toolchain | tr -d '\r' | tr . -)"      # v4.24.0 -> v4-24-0
BR="lake-cache/qou-$SLUG"
WORK="$(mktemp -d)"
LIST="$WORK/files.txt"
TGZ="$WORK/lake-oleans.tgz"
PUSH=0; [ "${1:-}" = "--push" ] && PUSH=1

echo "seed branch: $BR"
: > "$LIST"

# 1. freshly-rebuilt mathlib oleans (+ sibling .ilean if present)
MLLIB=".lake/packages/mathlib/.lake/build/lib/lean"
n_ml=0
if [ -f "$BUILT_FILE" ]; then
  while IFS= read -r mod; do
    [ -z "$mod" ] && continue
    rel="${mod//.//}"
    for ext in olean ilean; do
      f="$MLLIB/$rel.$ext"
      [ -f "$f" ] && { echo "$f" >> "$LIST"; [ "$ext" = olean ] && n_ml=$((n_ml+1)); }
    done
  done < "$BUILT_FILE"
fi
echo "  fresh mathlib oleans: $n_ml"

# 2. non-mathlib package oleans (rev-independent) + qou paper packages
for pkg in batteries aesop Qq plausible importGraph LeanSearchClient proofwidgets; do
  d=".lake/packages/$pkg/.lake/build/lib/lean"
  [ -d "$d" ] && find "$d" -name '*.olean' -o -name '*.ilean' 2>/dev/null | sed 's#^\./##' >> "$LIST" || true
done
for paperlib in content/*/lean/.lake/build/lib/lean; do
  [ -d "$paperlib" ] && find "$paperlib" -name '*.olean' -o -name '*.ilean' 2>/dev/null >> "$LIST" || true
done
total=$(wc -l < "$LIST")
echo "  total files to seed: $total"

# 3. tar + split into 90 MB git-blob parts
tar czf "$TGZ" -T "$LIST"
sz=$(du -h "$TGZ" | cut -f1)
echo "  tarball: $sz"
rm -f lake-oleans.tgz.part*
split -b 90M -d "$TGZ" lake-oleans.tgz.part
ls -la lake-oleans.tgz.part* | awk '{print "  "$NF" "$5}'

if [ "$PUSH" -ne 1 ]; then
  echo "DRY RUN — rerun with --push to commit+push orphan branch $BR"
  echo "parts staged in $ROOT (remove with: rm lake-oleans.tgz.part*)"
  exit 0
fi

# 4. commit to a fresh orphan branch and force-push
CUR="$(git rev-parse --abbrev-ref HEAD)"
git stash -u >/dev/null 2>&1 || true
git checkout --orphan "seed-tmp-$SLUG"
git rm -rf --cached . >/dev/null 2>&1 || true
git add -f lake-oleans.tgz.part*
git commit -q -m "seed lean cache: qou+mathlib oleans @ $SLUG (fresh f897ebc rebuild incl ZetaValues cone)"
git push -f origin "HEAD:$BR"
git checkout -f "$CUR"
git branch -D "seed-tmp-$SLUG" || true
git stash pop >/dev/null 2>&1 || true
rm -f lake-oleans.tgz.part*
echo "pushed $BR"
