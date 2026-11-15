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
#   -B/--force      recompile even modules whose olean looks fresh. A manual
#                   override, not a workaround: freshness here is
#                   scripts/lean_freshness.py, the SAME rule lean-axiom-guard.py
#                   gates on, so the two can no longer disagree. Until 2026-08-26
#                   this script compared MTIME and the guard COMMIT time, which
#                   deadlocked the documented compose whenever you built before
#                   committing. Bean qou-5v24.
#   -k/--keep-going continue past a red module; its dependents are recorded
#                   `blocked` (NOT compiled), which separates genuine errors
#                   from missing-olean cascades
#   -j N            parallel workers (default nproc-1)
#   --report FILE   TSV + JSON per-module status report
#
# Exit 0 = every module in the cone type-checks (or --keep-going was given).
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
LEANDIR="$ROOT/folio/quantum-observable-universe/lean"
OUT="$LEANDIR/.lake/build/lib/lean"

export PATH="$HOME/.elan/bin:$PATH"

# LEAN_PATH: our own output dir, every fetched dependency package's olean dir,
# plus the sibling *path* packages (ugb/fred2005), which do NOT live under
# .lake/packages — QOU imports UGB.GrobnerShirshov.HeckeGS.
LP="$OUT"
for p in "$ROOT"/.lake/packages/*/.lake/build/lib/lean; do
  [ -d "$p" ] && LP="$LP:$p"
done
for p in "$ROOT"/folio/*/lean/.lake/build/lib/lean; do
  [ -d "$p" ] && [ "$p" != "$OUT" ] && LP="$LP:$p"
done
export LEAN_PATH="$LP"

# NOTE — `-DautoImplicit=false` is NOT set here, and that is correct: it is
# hardcoded, unconditionally, in the `lean` invocation inside
# scripts/lean_cone_build.py (see `compile_one`). LEAN_CONE_EXTRA_ARGS is
# *appended* to it, so overriding this variable cannot turn autoImplicit back
# on. Do not "restore" the flag here — it moved in 6d60eb3e2a, it was not lost.
# Why it matters: with autoImplicit on, a class field such as
# `chi : ℕ → ℕ → R` inside a `extends MarkovTraceContext` descendant silently
# auto-binds `R` as a fresh implicit instead of resolving to the inherited
# parent field, and a no-op base-ring refactor compiles green.
#
# Match the package's `moreLeanArgs`: QOU/.../AllKnownIsotopesUniqueness is
# machine-generated (~12800 declarations) and overflows Lean's default
# elaboration-thread stack, aborting with a bare exit 134 rather than a source
# error. Without -s it reports as a spurious red.
export LEAN_CONE_EXTRA_ARGS="${LEAN_CONE_EXTRA_ARGS:--s 65536}"

exec python3 "$ROOT/scripts/lean_cone_build.py" --leandir "$LEANDIR" "$@"
