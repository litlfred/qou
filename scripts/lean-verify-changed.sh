#!/usr/bin/env bash
# Verify changed .lean files with `lean`-direct against the restored olean
# tree, and report each file's REAL exit status.
#
# Why this exists: the obvious one-liner
#     lean "$f" 2>&1 | head -5 && echo "exit 0"
# reports the exit status of `head`, not of `lean` — so a file that failed
# on a missing import prints "exit 0". That false pass is exactly what the
# §"QA is agent-owned" gate must not produce, and it is easy to write by
# accident when you want the first few error lines. Capture to a file and
# test "${PIPESTATUS[0]}" / the bare command's status instead of piping.
#
# It also separates the two failure kinds, which are NOT the same finding:
#   MISSING-OLEAN — a dependency has not been built yet in this container.
#                   Says nothing about the file. Retry after the build.
#   ERROR         — a real elaboration/type error in the file. Actionable.
#
# A MISSING-OLEAN naming a QOU.* module is a THIRD situation, distinct from
# both of the above: the paper-dir QOU olean tree is a dated snapshot
# (2026-07-19), so any module added or changed since then has no olean
# anywhere, and modules that DO have one can be stale enough to produce a
# false ERROR — `KnotFactorAmphicheiral` reports an `Application type
# mismatch: HeckeExpansion R` against the snapshot that vanishes when the
# upstream module is rebuilt from current source. Restoring a complete
# Mathlib does not help; this is QOU staleness, not Mathlib staleness.
#
# `--build-missing` handles it: on a MISSING-OLEAN naming a QOU module, it
# compiles that module from CURRENT source into a scratch olean root and
# retries, looping until the cone resolves. Because the upstream is built
# from current source, the result is real-import-cone verification AND free
# of stale-snapshot contamination. Scratch oleans are kept out of the shared
# .lake tree so a concurrent `lake build` is not disturbed.
#
# Usage:
#   scripts/lean-verify-changed.sh                 # every .lean changed vs HEAD~1
#   scripts/lean-verify-changed.sh <file.lean>...  # explicit list
#   REF=origin/main scripts/lean-verify-changed.sh # changed vs another ref
#   scripts/lean-verify-changed.sh --build-missing ...   # rebuild stale QOU deps
#
# Exit 0 iff every file checked reached exit 0. MISSING-OLEAN counts as a
# failure for the exit code — an unverified file is not a verified one.
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Shared changed-file collection. ONE definition, so the fifth gate script
# cannot repeat the defect the first four shared (bean qou-pt9b).
. "$ROOT/scripts/lib/changed-files.sh"
LEAN_ROOT="$ROOT/content/quantum-observable-universe/lean"
export PATH="$HOME/.elan/bin:$PATH"

if ! command -v lean >/dev/null 2>&1; then
  echo "lean-verify-changed: no lean on PATH (try: export PATH=\"\$HOME/.elan/bin:\$PATH\")" >&2
  exit 2
fi

# Resolve explicit arguments to absolute paths BEFORE cd-ing into the Lake
# root — otherwise a repo-relative path silently stops resolving and every
# file reports "SKIP (gone)", which is a false all-clear.
BUILD_MISSING=0
args=()
for a in "$@"; do
  if [ "$a" = "--build-missing" ]; then BUILD_MISSING=1; else args+=("$a"); fi
done
set -- ${args+"${args[@]}"}

files=()
if [ "$#" -gt 0 ]; then
  for f in "$@"; do
    case "$f" in
      /*) files+=("$f") ;;
      *)  if   [ -f "$PWD/$f"       ]; then files+=("$PWD/$f")
          elif [ -f "$ROOT/$f"      ]; then files+=("$ROOT/$f")
          elif [ -f "$LEAN_ROOT/$f" ]; then files+=("$LEAN_ROOT/$f")
          else files+=("$f")   # keep it, so it is reported as missing not dropped
          fi ;;
    esac
  done
fi

cd "$LEAN_ROOT" || exit 2

# TWO olean trees exist and they are NOT interchangeable:
#   $ROOT/.lake/packages/...                  the ROOT Lake workspace
#   $LEAN_ROOT/.lake/packages/...             the per-paper workspace
# The root workspace is typically the complete one (~6990 mathlib oleans);
# the per-paper tree is often a partial rebuild. Using the per-paper tree
# alone makes files fail with MISSING-OLEAN on `Mathlib.Tactic` and friends
# and reads as "cannot verify" when verification was available all along.
# Put the ROOT packages FIRST so the complete tree wins, and keep the
# per-paper build dir first overall so this paper's own oleans are found.
LP="$LEAN_ROOT/.lake/build/lib/lean"
for p in "$ROOT"/.lake/build/lib/lean "$ROOT"/.lake/packages/*/.lake/build/lib/lean; do
  [ -d "$p" ] && LP="$LP:$p"
done
for p in "$LEAN_ROOT"/.lake/packages/*/.lake/build/lib/lean; do
  [ -d "$p" ] && LP="$LP:$p"
done
SCRATCH="${LEAN_SCRATCH_OLEANS:-${TMPDIR:-/tmp}/qou-scratch-oleans}"
if [ "$BUILD_MISSING" = "1" ]; then
  mkdir -p "$SCRATCH"
  LP="$SCRATCH:$LP"          # scratch wins over the dated snapshot
fi
export LEAN_PATH="$LP"

# Compile one QOU module from CURRENT source into the scratch olean root,
# RECURSIVELY building any QOU upstream it is itself missing.
#
# The non-recursive version gave up exactly one level deep, and the caller
# below could not tell why: it built `QOU.Mathlib.NonAbelianStokes` fine, then
# `QOU.Mathlib.HeckeAlgebra` failed because *its* dependency
# `QOU.MathlibExt.QPartitionCombinatorics` was absent, `build_qou_module`
# returned 1, and the retry loop `break`ed. The file under test was then
# reported MISSING-OLEAN naming `HeckeAlgebra` — which reads as "the cache is
# short one module" when the truth was "the cache is short a whole cone and
# this script stopped after the first". Measured 2026-08-24 on the merged q407
# branch: 5 of 16 changed files unverified, every one of them behind a cone
# that resolves once the recursion is there. Bean `qou-1ugy`.
#
# It also swallowed lean's output (`>/dev/null 2>&1`), so a REAL compile error
# in an upstream was indistinguishable from a missing sub-dependency. Both now
# come back distinctly, and `$_BUILD_ERR` carries the reason for the caller.
#
# Cycle/repeat safety: `_MOD_SEEN` marks every module whose build has been
# ATTEMPTED, so a diamond in the import graph costs one build rather than
# many, and an import cycle terminates instead of recursing forever.
# `_MOD_OK` short-circuits a later caller that needs an already-built module.
_MOD_SEEN=" "
_MOD_OK=" "
_BUILD_ERR=""
build_qou_module() {
  local mod="$1" depth="${2:-0}" rel src blog sub rc i
  case "$_MOD_OK"   in *" $mod "*) return 0 ;; esac
  case "$_MOD_SEEN" in *" $mod "*) _BUILD_ERR="already attempted: $mod"; return 1 ;; esac
  _MOD_SEEN="$_MOD_SEEN$mod "
  if [ "$depth" -gt "${LEAN_BUILD_DEPTH:-32}" ]; then
    _BUILD_ERR="import cone deeper than LEAN_BUILD_DEPTH at $mod"; return 1
  fi
  rel="$(printf '%s' "$mod" | tr '.' '/')"
  src="$LEAN_ROOT/$rel.lean"
  [ -f "$src" ] || { _BUILD_ERR="no source for $mod"; return 1; }
  mkdir -p "$SCRATCH/$(dirname "$rel")"
  blog="$(mktemp)"
  for i in $(seq 1 "${LEAN_BUILD_FANOUT:-64}"); do
    timeout "${LEAN_TIMEOUT:-600}" lean "$src" -o "$SCRATCH/$rel.olean" >"$blog" 2>&1
    rc=$?
    if [ "$rc" -eq 0 ]; then
      _MOD_OK="$_MOD_OK$mod "; rm -f "$blog"; return 0
    fi
    # Not a missing-olean failure => a REAL error in THIS module. Say so; do
    # not let it masquerade as a cache gap.
    if ! grep -q "does not exist" "$blog"; then
      _BUILD_ERR="compile error in $mod: $(grep -m1 'error:' "$blog" | cut -c1-160)"
      rm -f "$blog"; return 1
    fi
    sub=$(grep -o "of module [A-Za-z0-9_.]*" "$blog" | head -1 | sed 's/of module //')
    # Mathlib gaps are `scripts/build-missing-oleans.py`'s job, not this one.
    case "$sub" in
      QOU.*) ;;
      *) _BUILD_ERR="non-QOU olean missing under $mod: $sub"; rm -f "$blog"; return 1 ;;
    esac
    build_qou_module "$sub" "$((depth+1))" || { rm -f "$blog"; return 1; }
  done
  _BUILD_ERR="gave up after ${LEAN_BUILD_FANOUT:-64} upstreams under $mod"
  rm -f "$blog"; return 1
}

# ---------------------------------------------------------------------------
# STALE-OLEAN FRESHNESS PASS (owner ruling 2026-08-24, bean `qou-1ugy`).
#
# `--build-missing` used to fire only on lean's "does not exist". A
# stale-but-PRESENT olean was used as-is, and that is not a harmless
# approximation -- it produces a confident, wrong ERROR. Measured: the QOU
# olean snapshot in `.lake/build/lib/lean` is dated 2026-07-19 while every
# source is current, and `QOU/Mathlib/UpstreamSubstrateBridge.lean` reported
#
#     Application type mismatch: ... yekutieli_finite_slice_substrate Y
#
# against it. The file is fine: `origin/main`'s own copy fails identically,
# and the error vanishes once `QOU.Mathlib.NonAbelianStokes` is rebuilt from
# current source. An agent reading that ERROR goes looking for a proof bug
# that does not exist -- the failure mode this script's header calls a "false
# ERROR" and, until now, could still produce.
#
# So: before verifying a file, walk its QOU import cone and rebuild anything
# whose olean is older than its source. Rebuilding an upstream INVALIDATES
# everything compiled against the old one, so the walk is post-order and a
# rebuilt module propagates "you must follow too" to its dependents via exit
# status 10. Without that propagation the cone half-rebuilds and the mismatch
# survives one level down.
#
# COST, stated plainly: after a mathlib or toolchain bump this approaches a
# full QOU rebuild, because every olean is then older than its source. That is
# the accepted trade -- a slow true answer over a fast false one. Set
# LEAN_NO_REBUILD_STALE=1 to skip the pass and take the old behaviour.
_FRESH_SEEN=" "     # modules the freshness pass has visited
_MOD_FRESH=" "      # modules REBUILT from current source during this run

qou_imports() {
  grep -E '^[[:space:]]*import[[:space:]]+QOU\.' "$1" 2>/dev/null \
    | sed -E 's/^[[:space:]]*import[[:space:]]+//; s/[[:space:]].*$//'
}

# ensure_fresh <module> [depth]
#   exit 0  = nothing to do (already current)
#   exit 10 = REBUILT this call, so every dependent must be rebuilt as well
ensure_fresh() {
  local mod="$1" depth="${2:-0}" rel src olean snap need=0 up rc
  case "$_FRESH_SEEN" in *" $mod "*)
    case "$_MOD_FRESH" in *" $mod "*) return 10 ;; *) return 0 ;; esac ;;
  esac
  _FRESH_SEEN="$_FRESH_SEEN$mod "
  [ "$depth" -gt "${LEAN_FRESH_DEPTH:-64}" ] && return 0
  rel="$(printf '%s' "$mod" | tr '.' '/')"
  src="$LEAN_ROOT/$rel.lean"
  [ -f "$src" ] || return 0            # not a QOU source (Mathlib, batteries, ...)
  while IFS= read -r up; do
    [ -n "$up" ] || continue
    ensure_fresh "$up" "$((depth+1))"; rc=$?
    [ "$rc" -eq 10 ] && need=1
  done < <(qou_imports "$src")
  olean="$SCRATCH/$rel.olean"
  snap="$LEAN_ROOT/.lake/build/lib/lean/$rel.olean"
  if [ -f "$olean" ]; then
    [ "$src" -nt "$olean" ] && need=1
  elif [ ! -f "$snap" ] || [ "$src" -nt "$snap" ]; then
    need=1
  fi
  if [ "$need" = "1" ]; then
    if build_qou_module "$mod"; then
      _MOD_FRESH="$_MOD_FRESH$mod "
      printf '%-70s  ..rebuilt stale %s\n' "" "$mod"
      return 10
    fi
    # A rebuild we could not do is NOT a pass. Say why; the file will still be
    # verified and will report ERROR or MISSING-OLEAN on its own merits.
    printf '%-70s  ..cannot rebuild %s -- %s\n' "" "$mod" "$_BUILD_ERR"
  fi
  return 0
}

# Rebuild every stale QOU module in one file's import cone.
freshen_cone() {
  local f="$1" up
  [ "${LEAN_NO_REBUILD_STALE:-0}" = "1" ] && return 0
  [ "$BUILD_MISSING" = "1" ] || return 0
  while IFS= read -r up; do
    [ -n "$up" ] || continue
    ensure_fresh "$up" 0
  done < <(qou_imports "$f")
}

if [ "${#files[@]}" -eq 0 ]; then
  # DEFAULT IS THE MERGE-BASE, NOT HEAD~1. A different shape from the
  # qou-s2gm working-tree defect but the same family: HEAD~1 sees only the
  # MOST RECENT COMMIT, so on a branch built the way AGENTS.md rule 3 asks
  # for -- "each logically distinct change gets its own commit" -- this
  # verified one commit's .lean files and reported "no .lean files to check"
  # for every earlier one. Under-coverage that reads as a pass.
  #
  # This is the Lean side of the §"QA is agent-owned; CI is a backup" gate,
  # and a library file under lean/QOU/** has no .qa.json sidecar and is
  # covered by nothing else, so narrow-by-default is the wrong direction.
  # Verifying more files costs `lean` time; missing one costs a wrong proof
  # on main.
  #
  # REF= still overrides, so `REF=HEAD~1 scripts/lean-verify-changed.sh` is
  # the old behaviour when you deliberately want just the last commit.
  ref="${REF:-$(changed_files_base)}"
  # An unresolvable base already warned on stderr from the helper. HEAD~1 is
  # the last-resort fallback and is DELIBERATELY the old, narrow behaviour --
  # better one commit verified than zero, and the warning says which happened.
  [ -n "$ref" ] || ref="HEAD~1"
  while IFS= read -r f; do
    [ -n "$f" ] && files+=("$ROOT/$f")
  done < <(cd "$ROOT" && git diff --name-only "$ref" -- '*.lean')
fi

if [ "${#files[@]}" -eq 0 ]; then
  # A SKIP IS NOT A PASS (#5495, requested by the sibling on #5453). "0 files
  # considered" and "N considered, none relevant" were the same sentence, and
  # they are not the same fact: the first means this gate examined NOTHING.
  # The scope line says what was compared, so a caller can tell a genuine skip
  # from the merge-base half having been dropped.
  echo "lean-verify-changed: 0 .lean file(s) — this check examined NOTHING."
  echo "  scope: $(changed_files_scope)"
  exit 0
fi

ok=0; err=0; missing=0; gone=0
log="$(mktemp)"
trap 'rm -f "$log"' EXIT

for f in "${files[@]}"; do
  # A path that does not resolve is NOT a pass — count it, so a typo or a
  # bad relative path cannot masquerade as a clean run.
  [ -f "$f" ] || { gone=$((gone+1)); printf '%-70s NOT-FOUND\n' "$(basename "$f")"; continue; }
  freshen_cone "$f"
  # No pipe: $? is lean's own status.
  timeout "${LEAN_TIMEOUT:-600}" lean "$f" >"$log" 2>&1
  rc=$?
  # --build-missing: rebuild stale QOU upstreams from current source, retry.
  if [ "$rc" -ne 0 ] && [ "$BUILD_MISSING" = "1" ]; then
    for _ in $(seq 1 12); do
      grep -q "does not exist" "$log" || break
      mod=$(grep -o "of module [A-Za-z0-9_.]*" "$log" | head -1 | sed 's/of module //')
      case "$mod" in QOU.*) ;; *) break ;; esac   # only QOU; Mathlib gaps are the build's job
      if ! build_qou_module "$mod"; then
        # WHY it could not be built is the whole finding. Silence here is what
        # made a deep cone look like a single missing module. Bean `qou-1ugy`.
        printf '%-70s  ..cannot build %s -- %s\n' "" "$mod" "$_BUILD_ERR"
        break
      fi
      printf '%-70s  ..built upstream %s\n' "" "$mod"
      timeout "${LEAN_TIMEOUT:-600}" lean "$f" >"$log" 2>&1
      rc=$?
      [ "$rc" -eq 0 ] && break
    done
  fi
  if [ "$rc" -eq 0 ]; then
    ok=$((ok+1)); printf '%-70s exit 0\n' "$(basename "$f")"
  elif grep -q "does not exist" "$log"; then
    missing=$((missing+1))
    printf '%-70s MISSING-OLEAN (%s)\n' "$(basename "$f")" \
      "$(grep -o "module [A-Za-z0-9_.]*" "$log" | head -1)"
  else
    err=$((err+1)); printf '%-70s ERROR\n' "$(basename "$f")"
    sed 's/^/      /' "$log" | head -8
  fi
done

echo
echo "lean-verify-changed: ${ok} exit 0, ${err} error, ${missing} unverified (missing olean), ${gone} not-found"
[ "$err" -eq 0 ] && [ "$missing" -eq 0 ] && [ "$gone" -eq 0 ] && [ "$ok" -gt 0 ]
