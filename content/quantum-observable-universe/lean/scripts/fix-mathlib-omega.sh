#!/bin/bash
# Fix missing Mathlib.Tactic.Omega at pinned Mathlib commit f897ebcf.
# The omega tactic is built into Lean 4.24+ core; this stub satisfies
# stale olean references in the Mathlib cache.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
MATHLIB_DIR="$SCRIPT_DIR/../.lake/packages/mathlib"
if [ -d "$MATHLIB_DIR" ] && [ ! -f "$MATHLIB_DIR/Mathlib/Tactic/Omega.lean" ]; then
  mkdir -p "$MATHLIB_DIR/Mathlib/Tactic"
  echo "-- Stub: omega is built into Lean 4.24+ core" > "$MATHLIB_DIR/Mathlib/Tactic/Omega.lean"
  echo "Created Mathlib.Tactic.Omega stub"
fi
