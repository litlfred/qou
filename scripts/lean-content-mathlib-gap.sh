#!/usr/bin/env bash
# lean-content-mathlib-gap.sh — the Mathlib modules content blocks import that
# `lake build QOU UGB Fred2005` does NOT build.
#
# WHY THIS EXISTS
#
# A seed taken from a Lake build cannot contain them, structurally: Lake builds
# the dependency cone of the three *libraries*, and content-block `.lean` files
# live outside the package, so their imports are invisible to it. Anything they
# import and the libraries do not is absent from the tree and therefore absent
# from the cache — and a restoring agent's content sweep then reports REDs that
# are cache gaps wearing the costume of corpus defects.
#
# Measured 2026-09-06 (bean `qou-tpdg`, PR #6827): content blocks import 252
# distinct Mathlib modules; 4 were missing, and those 4 accounted for all 8 REDs
# of a 938-file sweep. The first reseed that day inherited the gap because the
# recipe was `lake build QOU UGB Fred2005` and nothing else.
#
# USAGE
#   scripts/lean-content-mathlib-gap.sh           # list the gap
#   scripts/lean-content-mathlib-gap.sh --build   # lake build it (traced)
#
# Run it before seeding. `--build` goes through `lake`, not `lean -o`, so the
# oleans carry the `.trace` the seeder's coverage guard requires.

set -uo pipefail
ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"
export PATH="$HOME/.elan/bin:$PATH"

MLLIB=".lake/packages/mathlib/.lake/build/lib/lean"
[ -d "$MLLIB" ] || { echo "no mathlib build tree at $MLLIB" >&2; exit 2; }

mapfile -t IMPORTS < <(
  find folio -path '*/lean/*' -prune -o -name '*.lean' -print |
    xargs grep -ho '^import Mathlib[A-Za-z0-9_.]*' 2>/dev/null |
    sed 's/^import //' | sort -u)

MISSING=()
for m in "${IMPORTS[@]}"; do
  [ -f "$MLLIB/${m//./\/}.olean" ] || MISSING+=("$m")
done

echo "content-block Mathlib imports: ${#IMPORTS[@]}"
echo "absent from the built tree:    ${#MISSING[@]}"
# `printf '%s\n' "${arr[@]}"` on an empty array still prints one blank line
# under `set -u`, which reads as "one missing module with an empty name".
[ "${#MISSING[@]}" -gt 0 ] && printf '  %s\n' "${MISSING[@]}"

[ "${#MISSING[@]}" -eq 0 ] && { echo "nothing to build — seed is safe on this axis"; exit 0; }
[ "${1:-}" = "--build" ] || { echo; echo "rerun with --build to lake build them"; exit 1; }

echo; echo "lake build ${#MISSING[@]} module(s) ..."
lake build "${MISSING[@]}"
