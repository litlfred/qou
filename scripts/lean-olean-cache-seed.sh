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
#
# LEGACY PATH. `.github/workflows/lake-cache-refresh.yml` seeds through
# folio-assistant/scripts/lake-cache.sh, which tars the whole `.lake` tree and
# so cannot miss an artifact class. This script hand-picks files by extension
# and is kept only for manual reseeds; prefer the service script.
#
# ARTIFACT SET (measured 2026-08-07, lib-only package, olean mtime as the
# oracle — a library is what mathlib/QOU are, and it behaves differently from
# an exe-coupled package, so do not "simplify" this list from intuition):
#
#   restored content                      -> `lake build` result
#   lib + ir, everything                     no-op   (cache honoured)
#   lib + ir, .trace deleted                 REBUILT  <- .trace REQUIRED
#   lib + ir, .hash deleted                  no-op    (.hash not needed)
#   lib + ir/*.setup.json but no ir/*.c      REBUILT  <- ir/*.c REQUIRED
#   lib only, no ir/                         REBUILT
#   lib only, olean+ilean only (was this)    REBUILT  <- the old bug
#
# So the minimal honoured set is: .olean, .ilean, .trace, and ir/ (.c +
# .setup.json). Seeding oleans without their .trace siblings produces a cache
# that Lake treats as entirely stale: it rebuilds, and rebuilding EVICTS the
# untraced oleans. That is the defect this script used to ship (bean 02kc);
# such a cache only ever worked for direct `lean` + LEAN_PATH invocations.
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

# 1. freshly-rebuilt mathlib oleans (+ .ilean, + the .trace that makes Lake
#    honour them, + the ir/ C outputs the module job records as its "c" output)
MLBUILD=".lake/packages/mathlib/.lake/build"
MLLIB="$MLBUILD/lib/lean"
MLIR="$MLBUILD/ir"
n_ml=0; n_tr=0
if [ -f "$BUILT_FILE" ]; then
  while IFS= read -r mod; do
    [ -z "$mod" ] && continue
    rel="${mod//.//}"
    for ext in olean ilean trace; do
      f="$MLLIB/$rel.$ext"
      [ -f "$f" ] || continue
      echo "$f" >> "$LIST"
      [ "$ext" = olean ] && n_ml=$((n_ml+1))
      [ "$ext" = trace ] && n_tr=$((n_tr+1))
    done
    for ext in c setup.json; do
      f="$MLIR/$rel.$ext"
      [ -f "$f" ] && echo "$f" >> "$LIST"
    done
  done < "$BUILT_FILE"
fi
echo "  fresh mathlib oleans: $n_ml  (traces: $n_tr)"

# A cache whose oleans lack traces is worse than no cache: Lake rebuilds and
# evicts them. Refuse to seed one rather than publish a silently-useless
# branch. Mirrors the 90% guard in folio-assistant/scripts/lake-cache.sh.
if [ "$n_ml" -gt 0 ]; then
  cov=$(( n_tr * 100 / n_ml ))
  echo "  trace coverage: ${cov}%"
  if [ "$cov" -lt 90 ]; then
    echo "REFUSING to seed: trace coverage ${cov}% ($n_tr traces for $n_ml oleans)." >&2
    echo "Lake reads .trace to decide staleness, so it would rebuild — and evict —" >&2
    echo "everything untraced. Seed from a tree where a real \`lake build\` (not a" >&2
    echo "lean-direct \`lean -o\` pass) produced the traces alongside the oleans." >&2
    exit 1
  fi
fi

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
  d=".lake/packages/$pkg/.lake/build"
  [ -d "$d" ] || continue
  # NB: the -o alternatives must be parenthesised, else -type f binds to the
  # last -name only and the other branches emit directories too.
  find "$d" \( -name '*.olean' -o -name '*.ilean' -o -name '*.trace' \
            -o -name '*.c' -o -name '*.setup.json' \) -type f 2>/dev/null \
    | sed 's#^\./##' >> "$LIST" || true
done
if [ "${SEED_PAPER:-0}" = "1" ]; then
  for paperbuild in content/*/lean/.lake/build; do
    [ -d "$paperbuild" ] || continue
    find "$paperbuild" \( -name '*.olean' -o -name '*.ilean' -o -name '*.trace' \
                       -o -name '*.c' -o -name '*.setup.json' \) -type f 2>/dev/null \
      >> "$LIST" || true
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
# unique per-run orphan branch + worktree so a prior aborted run can't collide
git worktree prune 2>/dev/null || true
TMPBR="seed-tmp-$SLUG-$$"
WT="$(mktemp -d)/seed-wt"
git worktree add --detach -q "$WT"
mv lake-oleans.tgz.part* "$WT"/
push_ok=1
(
  cd "$WT"
  git checkout -q --orphan "$TMPBR"
  git reset -q --hard 2>/dev/null || true
  git rm -rf -q --cached . 2>/dev/null || true
  find . -maxdepth 1 -type f ! -name 'lake-oleans.tgz.part*' ! -name '.git' -delete 2>/dev/null || true
  first=1
  for p in $(ls lake-oleans.tgz.part* | sort); do
    git add -f "$p"
    git commit -q -m "seed lean cache @ $SLUG: $p (fresh f897ebc, incl ZetaValues cone)"
    ok=0
    if [ "$first" = 1 ]; then
      for i in 1 2 3 4; do git push -f origin "HEAD:$BR" && { first=0; ok=1; break; } || sleep $((2**i)); done
    else
      for i in 1 2 3 4; do git push origin "HEAD:$BR" && { ok=1; break; } || sleep $((2**i)); done
    fi
    [ "$ok" = 1 ] && echo "  pushed $p" || { echo "  FAILED $p"; exit 7; }
  done
) || push_ok=0
git worktree remove --force "$WT" 2>/dev/null || true
git branch -D "$TMPBR" 2>/dev/null || true
[ "$push_ok" = 1 ] && echo "pushed $BR (incremental)" || { echo "SEED PUSH FAILED"; exit 7; }
