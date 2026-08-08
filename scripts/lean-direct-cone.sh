#!/usr/bin/env bash
# lean-direct-cone.sh — compile a QOU module's import cone with `lean` directly.
#
# Motivation: `lake build <Module>` re-resolves the dependency graph and rebuilds
# Mathlib from source (~3000 modules for the `import Mathlib.Tactic` closure), and
# in a sandbox it also wipes oleans restored from the `lake-cache/*` branch. When the
# Mathlib oleans are already present under `.lake/packages/*/.lake/build/lib/lean`,
# we can bypass Lake entirely: topologically sort the QOU cone and run `lean -o` on
# each module in order, writing oleans into the normal `.lake/build/lib/lean` tree.
#
# Usage:
#   scripts/lean-direct-cone.sh QOU.BraidKnot.HookProductHLF
#   scripts/lean-direct-cone.sh --all -k -j4 --report /tmp/qou-cone.tsv
#
# Options are forwarded to scripts/lean_cone_build.py:
#   --all           build every QOU module (whole-corpus survey)
#   -k/--keep-going continue past a red module; its dependents are recorded
#                   `blocked` (NOT compiled), which separates genuine errors
#                   from missing-olean cascades
#   -j N            parallel workers (default nproc-1)
#   --report FILE   TSV + JSON per-module status report
#
# Exit 0 = every module in the cone type-checks (or --keep-going was given).
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
LEANDIR="$ROOT/content/quantum-observable-universe/lean"
OUT="$LEANDIR/.lake/build/lib/lean"

export PATH="$HOME/.elan/bin:$PATH"

# LEAN_PATH: our own output dir, every fetched dependency package's olean dir,
# plus the sibling *path* packages (ugb/fred2005), which do NOT live under
# .lake/packages — QOU imports UGB.GrobnerShirshov.HeckeGS.
LP="$OUT"
for p in "$ROOT"/.lake/packages/*/.lake/build/lib/lean; do
  [ -d "$p" ] && LP="$LP:$p"
done
for p in "$ROOT"/content/*/lean/.lake/build/lib/lean; do
  [ -d "$p" ] && [ "$p" != "$OUT" ] && LP="$LP:$p"
done
export LEAN_PATH="$LP"

# Match the package's `moreLeanArgs`: QOU/.../AllKnownIsotopesUniqueness is
# machine-generated (~12800 declarations) and overflows Lean's default
# elaboration-thread stack, aborting with a bare exit 134 rather than a source
# error. Without -s it reports as a spurious red.
export LEAN_CONE_EXTRA_ARGS="${LEAN_CONE_EXTRA_ARGS:--s 65536}"

exec python3 "$ROOT/scripts/lean_cone_build.py" --leandir "$LEANDIR" "$@"
