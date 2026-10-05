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
#
# CONSEQUENCE — `build-missing-mathlib-oleans.sh` CANNOT feed this script.
# That producer compiles with `lean -o` (lean-direct), and `.trace` is a Lake
# bookkeeping artifact that only `lake build` writes. So the documented
# "build-missing → seed" flow now populates $BUILT_FILE and then *correctly*
# trips the 90% trace guard below. That refusal is the right answer, NOT a bug:
# a lean-direct tree has no traces to seed, so the cache it would publish is
# the useless kind. The only escape hatch is seeding from a real `lake build`
# tree. (Flagged by the sibling agent on PR #4705, who wired that producer up.)
set -euo pipefail
ROOT="$(git -C "$(dirname "$0")/.." rev-parse --show-toplevel)"
REPO_ROOT="$ROOT" source "$ROOT/scripts/lib/lake-cache-family.sh"
cd "$ROOT"
BUILT_FILE="${BUILT_FILE:-/tmp/parbuild_built.txt}"
SLUG="$(cut -d: -f2 lean-toolchain | tr -d '\r' | tr . -)"      # v4.24.0 -> v4-24-0
# ROOT-vs-BRANCH mismatch (measured 2026-08-07). This script collects from the
# WORKSPACE ROOT (`cd $ROOT`; `.lake/packages/...`). Per the authoritative
# roster .github/lake-packages.json, the workspace root is the **mathlib**
# package (`"package": "mathlib", "lake-root": "."`); `qou`'s lake-root is
# folio/quantum-observable-universe/lean. QOU.* oleans are built into THAT
# tree — root `.lake/build/lib` holds zero of them (verified: 0 at root vs 942
# under the paper lean root).
#
# So seeding "lake-cache/qou-$SLUG" from here publishes a qou-NAMED branch with
# zero qou CONTENT — which is precisely the live defect in bean 5d7z
# ("7268 oleans, every one a dependency, zero QOU.*"). Default to the branch
# that matches what is actually collected; override with CACHE_BRANCH= when
# seeding a paper package from its own lake root (with SEED_PAPER=1).
BR="${CACHE_BRANCH:-$(lake_cache_write_branch "mathlib-$SLUG")}"
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

# FALLBACK: derive $BUILT_FILE from the tree itself when it is absent or empty.
#
# The file is written only by build-missing-mathlib-oleans.sh, and only when
# somebody ran it. After a plain `lake build QOU UGB Fred2005` — the ordinary
# way to get a traced tree, and the only way to get one that passes the guard
# below — nothing has written it, and the seeder refused with n_ml=0 even
# though a perfectly seedable tree was sitting right there. That refusal cost
# a session, which is one session more than it should have.
#
# Only PAIRED oleans are taken: an olean without its .trace is exactly what
# must not be seeded, so deriving from the trace side makes the 90% guard pass
# by construction rather than by luck. Set BUILT_FILE= to override.
if [ "$n_ml" -eq 0 ] && [ -d "$MLLIB" ]; then
  echo "  \$BUILT_FILE absent/empty — deriving from paired oleans in $MLLIB"
  while IFS= read -r tr; do
    ol="${tr%.trace}.olean"
    [ -f "$ol" ] || continue
    rel="${ol#"$MLLIB"/}"; rel="${rel%.olean}"
    mod="${rel//\//.}"
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
  done < <(find "$MLLIB" -name '*.trace' -type f 2>/dev/null)
  echo "  derived mathlib oleans: $n_ml  (traces: $n_tr)"
fi

# No mathlib modules collected at all. The `n_ml > 0` wrapper on the coverage
# check below is load-bearing (div-by-zero), so without this an absent or empty
# $BUILT_FILE falls straight through it and seeds only the rev-independent dep
# oleans. The own-package guard further down does happen to stop the default
# mathlib branch, but it reports the wrong cause ("zero belong to mathlib",
# pointing at SEED_PAPER) when the real fault is that $BUILT_FILE was never
# written. Diagnose it here, where the cause is knowable.
#
# Raised by the sibling agent on PR #4705, which found that nothing in the repo
# ever wrote $BUILT_FILE: build-missing-mathlib-oleans.sh recorded builds as
# decorated `BUILT(n) <mod>` lines in its own $LOG — a different path in a
# different format — so producer and consumer never connected.
#
# 🛑 THAT HALF IS FIXED AND THIS COMMENT WAS STALE (2026-09-06).
# build-missing-mathlib-oleans.sh now writes the bare list: `: > "$BUILT_FILE"`
# at its line 53, `echo "$mod" >> "$BUILT_FILE"` at line 70, annotated "the
# seed's cleanliness contract". Producer and consumer DO connect. Read the code
# before repeating this paragraph — I quoted it as current fact in a merged PR
# and in lean-environment-setup.md, and it was already wrong.
#
# What remains true, and is the reason a seed can still be blocked: that
# producer compiles module-by-module with `lean -o` against a mathlib source
# clone, and `lean -o` writes NO .trace. So its output populates $BUILT_FILE
# with modules whose oleans would fail the 90% trace guard below — correctly,
# since Lake would rebuild and evict every one of them on restore. A seedable
# $BUILT_FILE has to come from a real `lake build`. The fallback immediately
# below derives one, so the absent-file case is no longer a dead end.
#
# TWO LEGITIMATE MATHLESS CASES are exempted (both from #4705's version of this
# guard; an earlier absorption here dropped them and wrongly blocked the first):
#   SEED_PAPER=1            a paper-only reseed right after `lake build QOU`
#                           has no fresh mathlib BY DESIGN — that is the whole
#                           point of the flag, so refusing it is a regression.
#   SEED_ALLOW_NO_MATHLIB=1 explicit escape hatch for anything else.
if [ "$n_ml" -eq 0 ] && [ "${SEED_PAPER:-0}" != "1" ] && [ "${SEED_ALLOW_NO_MATHLIB:-0}" != "1" ]; then
  echo "REFUSING to seed '$BR': no mathlib modules collected (n_ml=0)." >&2
  if [ ! -f "$BUILT_FILE" ]; then
    echo "\$BUILT_FILE does not exist: $BUILT_FILE" >&2
  else
    echo "\$BUILT_FILE exists but yielded no modules: $BUILT_FILE" >&2
    echo "Expected one bare module name per line (e.g. Mathlib.Init), NOT the" >&2
    echo "decorated 'BUILT(n) <mod>' lines that build-missing-mathlib-oleans.sh" >&2
    echo "writes to its own log — that format will not parse here." >&2
  fi
  echo "Seeding now would publish only the rev-independent dependency oleans," >&2
  echo "with none of the pinned-rev mathlib set the cache exists to carry." >&2
  echo "With --push that FORCE-PUSHES a mathlib-less branch over a good one;" >&2
  echo "the next agent's restore then counts ~0 mathlib oleans and concludes" >&2
  echo "\"Lean is unavailable in the sandbox\" — the failure AGENTS.md tells" >&2
  echo "agents not to accept, manufactured by our own tooling. Override only" >&2
  echo "if you mean it:" >&2
  echo "  SEED_PAPER=1 ...              # paper-only reseed after \`lake build QOU\`" >&2
  echo "  SEED_ALLOW_NO_MATHLIB=1 ...   # explicit escape hatch" >&2
  exit 1
fi

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

# GUARD: refuse to seed a payload with no mathlib.
#
# $BUILT_FILE absent or empty used to fall straight through to `n_ml=0`,
# and the seed carried on and built a tarball of nothing but the ~278
# rev-independent dep oleans. With --push that FORCE-PUSHES a
# mathlib-less branch over a good one; the next agent's restore then
# counts 0 < 2000 mathlib oleans, exits non-zero, and concludes "Lean is
# unavailable in the sandbox" — the failure AGENTS.md tells agents not to
# accept, manufactured by our own tooling. Nothing produced $BUILT_FILE
# until build-missing-mathlib-oleans.sh was taught to (same change), so
# this path was reachable by simply running the two scripts in order.
#
# A paper-only reseed (SEED_PAPER=1 right after `lake build QOU`) is the
# one legitimate mathlib-less case; SEED_ALLOW_NO_MATHLIB=1 is the
# explicit override for anything else.
if [ "$n_ml" -eq 0 ] && [ "${SEED_PAPER:-0}" != "1" ] && [ "${SEED_ALLOW_NO_MATHLIB:-0}" != "1" ]; then
  echo "lean-olean-cache-seed: REFUSING to seed — 0 fresh mathlib oleans." >&2
  if [ ! -f "$BUILT_FILE" ]; then
    echo "  \$BUILT_FILE does not exist: $BUILT_FILE" >&2
    echo "  Run a build first; it writes that list:" >&2
    echo "    scripts/build-missing-mathlib-oleans.sh <Mathlib.Module ...>" >&2
  else
    echo "  \$BUILT_FILE is empty: $BUILT_FILE" >&2
    echo "  Nothing was rebuilt this session, so there is nothing clean to seed." >&2
  fi
  echo "  Seeding anyway would push a cache branch with no mathlib and break" >&2
  echo "  every restoring agent. Override only if you mean it:" >&2
  echo "    SEED_PAPER=1 ...              # paper-only reseed after \`lake build QOU\`" >&2
  echo "    SEED_ALLOW_NO_MATHLIB=1 ...   # explicit escape hatch" >&2
  exit 1
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

# Own-package guard, mirroring folio-assistant/scripts/lake-cache.sh. A cache
# named for a package but carrying none of that package's oleans looks healthy
# by total count while being useless for the thing it is named after — the
# 5d7z defect. Derive the expected own-package prefix from the branch name and
# refuse to publish a branch that contains none of it.
own_pkg="${BR##*/}"; own_pkg="${own_pkg%-"$SLUG"}"          # lake-cache/qou-v4-24-0 -> qou
case "$own_pkg" in
  mathlib) own_n=$(grep -c '/mathlib/' "$LIST" || true) ;;
  qou)     own_n=$(grep -c '/lean/QOU/' "$LIST" || true) ;;
  ugb)     own_n=$(grep -c '/lean/UGB/' "$LIST" || true) ;;
  fred2005) own_n=$(grep -c '/lean/Fred2005/' "$LIST" || true) ;;
  *)       own_n=-1 ;;                                      # unknown: skip the check
esac
if [ "$own_n" = "0" ]; then
  echo "REFUSING to seed '$BR': $total files collected but ZERO belong to '$own_pkg'." >&2
  echo "This script collects from the WORKSPACE ROOT, which per" >&2
  echo ".github/lake-packages.json is the 'mathlib' package. Seeding a" >&2
  echo "'$own_pkg'-named branch from here reproduces bean 5d7z. To seed a paper" >&2
  echo "package, run with SEED_PAPER=1 and CACHE_BRANCH=$(lake_cache_write_branch "$own_pkg-$SLUG")" >&2
  echo "from a tree where that paper's lib was actually built." >&2
  exit 1
fi
[ "$own_n" -gt 0 ] 2>/dev/null && echo "  own-package ($own_pkg) files: $own_n"

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
