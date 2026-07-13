#!/usr/bin/env bash
# Build missing Mathlib oleans for QOU by lean-compiling each target from a
# local mathlib source clone against the oleans already present on LEAN_PATH
# (e.g. the restored lake-cache/qou-v4-24-0 set). Topological: a module is
# compiled only after all its Mathlib imports are present. Uses lean-direct
# (NOT lake) so it TRUSTS the present oleans instead of re-resolving the dep
# graph and rebuilding Mathlib from scratch.
#
# Usage:
#   scripts/build-missing-mathlib-oleans.sh [MODULE ...]
# with no args it reads targets (one Mathlib.* module per line) from stdin.
#
# Env overrides:
#   CLONE   local mathlib source clone            (default: ../mathlib4 or /home/user/mathlib4)
#   OUT     olean output dir                      (default: qou mathlib .lake build lib/lean)
#   LOG     build log path                        (default: /tmp/build_missing_oleans.log)
#   TIMEOUT per-module compile timeout in seconds (default: 500)
#
# NOTE ON REV SKEW (2026-07-13): if the present oleans predate the current
# mathlib pin (e.g. cache reseeded before an f897ebc bump), modules that cross a
# reorganized foundational instance will fail "failed to synthesize …" even
# though all their deps are present. That is not fixable incrementally — it
# needs a full clean rebuild at the pinned rev. See
# docs/audits/2026-07-13-mathlib-cache-f897ebc-revskew.md.
set -u
export PATH="$HOME/.elan/bin:$PATH"
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$ROOT" || exit 1

CLONE="${CLONE:-}"
if [ -z "$CLONE" ]; then
  for c in "$ROOT/../mathlib4" /home/user/mathlib4; do
    [ -d "$c/Mathlib" ] && CLONE="$c" && break
  done
fi
[ -n "$CLONE" ] && [ -d "$CLONE/Mathlib" ] || { echo "no mathlib source clone found (set CLONE=)"; exit 1; }

OUT="${OUT:-$ROOT/.lake/packages/mathlib/.lake/build/lib/lean}"
LOG="${LOG:-/tmp/build_missing_oleans.log}"
TIMEOUT="${TIMEOUT:-500}"
export LEAN_PATH="${LEAN_PATH:-$(find "$ROOT/.lake/packages" -type d -path '*/.lake/build/lib/lean' 2>/dev/null | tr '\n' ':')}"
: > "$LOG"
built=0; failed=0
declare -A INPROG

build_module() {
  local mod="$1" rel olean src imp
  rel="${mod//.//}"; olean="$OUT/$rel.olean"; src="$CLONE/$rel.lean"
  [ -f "$olean" ] && return 0                    # already present (memoized)
  [ -f "$src" ]   || { echo "NOSRC $mod" >>"$LOG"; return 1; }
  [ -n "${INPROG[$mod]:-}" ] && return 0          # cycle guard
  INPROG[$mod]=1
  while read -r imp; do
    [ -n "$imp" ] && build_module "$imp"
  done < <(grep -E "^import Mathlib\." "$src" | sed 's/^import //')
  mkdir -p "$(dirname "$olean")"
  if timeout "$TIMEOUT" lean -o "$olean" --root="$CLONE" "$src" >>"$LOG" 2>&1 && [ -f "$olean" ]; then
    built=$((built+1)); echo "BUILT($built) $mod" | tee -a "$LOG"
  else
    failed=$((failed+1)); echo "FAILED $mod" | tee -a "$LOG"
  fi
  unset 'INPROG[$mod]'
}

if [ "$#" -gt 0 ]; then TARGETS=("$@"); else mapfile -t TARGETS; fi
echo "START targets=${#TARGETS[@]} CLONE=$CLONE" | tee -a "$LOG"
for t in "${TARGETS[@]}"; do [ -n "$t" ] && build_module "$t"; done
echo "DONE built=$built failed=$failed  (root errors: grep -E 'error:' $LOG | grep -v 'object file')" | tee -a "$LOG"
echo "total mathlib oleans now: $(find "$OUT" -name '*.olean' | wc -l)" | tee -a "$LOG"
