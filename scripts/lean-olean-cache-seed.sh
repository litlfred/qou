#!/usr/bin/env bash
# Seed / reseed the lake-cache/qou-<toolchain-slug> orphan branch with a
# CLEAN, single-rev olean set.
#
# Cleanliness contract (see docs/audits/2026-07-13-mathlib-cache-f897ebc-revskew.md):
# only mathlib oleans that were REBUILT this session from the pinned source
# (listed in $BUILT_FILE) are included — never a mix of pre-/post-pin oleans.
# Non-mathlib package oleans (batteries/aesop/Qq/…) are rev-independent and
# included as-is; the qou/ugb/fred2005 PAPER oleans are EXCLUDED by default
# (they go stale the moment mathlib is rebuilt, since a verification session
# never writes them) — set SEED_PAPER=1 only right after a `lake build QOU` at
# the pinned rev.
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

# 2. non-mathlib package oleans (rev-independent).
#    NOTE: qou/ugb/fred2005 PAPER oleans are intentionally EXCLUDED — they are
#    only rebuilt when the paper lib itself is compiled with `-o`, which a
#    lean-direct *verification* session does not do.  Any paper oleans present
#    are therefore the pre-f897ebc restored set (stale); seeding them would make
#    a restoring agent hit an olean hash-mismatch the moment one qou module
#    imports another.  The seed is mathlib + rev-independent deps only; the small
#    paper libs rebuild fast against the restored mathlib.  (Set SEED_PAPER=1 to
#    include them, e.g. right after a full `lake build QOU` at the pinned rev.)
for pkg in batteries aesop Qq plausible importGraph LeanSearchClient proofwidgets; do
  d=".lake/packages/$pkg/.lake/build/lib/lean"
  [ -d "$d" ] && find "$d" -name '*.olean' -o -name '*.ilean' 2>/dev/null | sed 's#^\./##' >> "$LIST" || true
done
if [ "${SEED_PAPER:-0}" = "1" ]; then
  for paperlib in content/*/lean/.lake/build/lib/lean; do
    [ -d "$paperlib" ] && find "$paperlib" -name '*.olean' -o -name '*.ilean' 2>/dev/null >> "$LIST" || true
  done
fi
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

# 4. commit + push from an ISOLATED worktree — never touch the working branch.
#    INCREMENTAL: one commit per 90 MB part, pushed one at a time, so no single
#    push exceeds the git server's request-size limit (a full-set single push of
#    ~1.5 GB returns HTTP 413).  The first commit force-pushes (replacing the old
#    seed history); each subsequent part fast-forwards.  FETCH_HEAD's tree still
#    carries ALL parts, so the restore recipe (`git ls-tree FETCH_HEAD | grep
#    part`) is unchanged.
WT="$(mktemp -d)/seed-wt"
git worktree add --detach -q "$WT"
mv lake-oleans.tgz.part* "$WT"/
(
  cd "$WT"
  git checkout -q --orphan "seed-tmp-$SLUG"
  git reset -q --hard 2>/dev/null || true
  git rm -rf -q --cached . 2>/dev/null || true
  find . -maxdepth 1 -type f ! -name 'lake-oleans.tgz.part*' ! -name '.git' -delete 2>/dev/null || true
  first=1
  for p in $(ls lake-oleans.tgz.part* | sort); do
    git add -f "$p"
    git commit -q -m "seed lean cache @ $SLUG: $p (fresh f897ebc, incl ZetaValues cone)"
    if [ "$first" = 1 ]; then
      for i in 1 2 3 4; do git push -f origin "HEAD:$BR" && { first=0; break; } || sleep $((2**i)); done
    else
      for i in 1 2 3 4; do git push origin "HEAD:$BR" && break || sleep $((2**i)); done
    fi
    echo "  pushed $p"
  done
)
git worktree remove --force "$WT" 2>/dev/null || true
git branch -D "seed-tmp-$SLUG" 2>/dev/null || true
echo "pushed $BR (incremental)"
