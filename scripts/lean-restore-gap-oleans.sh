#!/usr/bin/env bash
# Restore the seven Mathlib oleans that lake-cache/qou-<slug> is missing.
#
# WHY THIS EXISTS.  The restored olean cache is short seven Mathlib modules, and
# seven content-block `.lean` files import them transitively.  In a stock
# container those seven cannot be checked at all: `lean`-direct fails at the
# import line, which reads like a source error and is not one.  AGENTS.md
# records the diagnosis ("their imports are fine, the cache is short") and the
# remedy ("fix at the cache branch").  This is that fix.
#
# Measured 2026-09-07: with these restored, all seven blocks compile
# `lean -DautoImplicit=false -s 65536` exit 0.
#
# NOT a Lake restore.  These are plain oleans with no `.trace` sidecars, so Lake
# would treat them as stale and evict them along with the rest of the restored
# cache (AGENTS.md, bean 02kc).  Untar them and use `lean`-direct; never
# `lake build` afterwards.
#
# Usage:
#   scripts/lean-restore-gap-oleans.sh            # into the mathlib olean dir
#   scripts/lean-restore-gap-oleans.sh <dir>      # into a shadow overlay
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SLUG=$(cut -d: -f2 "$ROOT/lean-toolchain" | tr -d '\r' | tr . -)
BRANCH="lake-cache/qou-${SLUG}-mathlib-gap-modules"
DEST="${1:-$ROOT/.lake/packages/mathlib/.lake/build/lib/lean}"

[ -d "$DEST" ] || { echo "no such destination: $DEST" >&2; exit 1; }

TGZ=$(mktemp)
trap 'rm -f "$TGZ"' EXIT INT TERM     # 2.3 MB, but leaking temp files is how
                                      # this container has run out of disk before

git -C "$ROOT" fetch --depth=1 origin "$BRANCH"
C=$(git -C "$ROOT" rev-parse FETCH_HEAD)
git -C "$ROOT" show "$C:mathlib-gap-oleans.tgz" > "$TGZ"
tar xzf "$TGZ" -C "$DEST"

echo "restored $(tar tzf "$TGZ" | wc -l) olean(s) into $DEST from $BRANCH ($C)"
echo "verify with:  source scripts/lean-direct-env.sh && \\"
echo "  lean -DautoImplicit=false -s 65536 content/quantum-observable-universe/mass-theory/reeb-bundle.lean"
