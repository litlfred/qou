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
# RESTORE INTO EVERY MATHLIB TREE, NOT JUST THE ROOT ONE.  There are two, and
# the two verification paths disagree about which one they read:
#
#   scripts/lean-direct-env.sh    pins  $ROOT/.lake/packages/*        (ROOT)
#   scripts/lean-shadow-verify.sh pins  content/*/lean/.lake/packages/* FIRST
#                                       (PAPER), by design -- the documented
#                                       sandbox restore fills the paper tree, so
#                                       that is the one it can guarantee.
#
# Measured 2026-09-07: this script defaulted to the ROOT tree alone, so plain
# `lean`-direct went green on all seven blocks while the full content sweep
# reported four of them RED -- against a paper tree that still had the gap.
# Both were correct about the tree they read.  A restore that fills only one is
# a restore that half the gates cannot see.
#
# Usage:
#   scripts/lean-restore-gap-oleans.sh            # into EVERY mathlib olean dir
#   scripts/lean-restore-gap-oleans.sh <dir>      # into one dir (e.g. a shadow)
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SLUG=$(cut -d: -f2 "$ROOT/lean-toolchain" | tr -d '\r' | tr . -)
BRANCH="lake-cache/qou-${SLUG}-mathlib-gap-modules"
if [ $# -ge 1 ]; then
  DESTS=("$1")
else
  DESTS=()
  for d in "$ROOT"/content/*/lean/.lake/packages/mathlib/.lake/build/lib/lean \
           "$ROOT"/.lake/packages/mathlib/.lake/build/lib/lean; do
    [ -d "$d" ] && DESTS+=("$d")
  done
fi

[ ${#DESTS[@]} -gt 0 ] || { echo "no mathlib olean tree found under $ROOT" >&2; exit 1; }
for d in "${DESTS[@]}"; do
  [ -d "$d" ] || { echo "no such destination: $d" >&2; exit 1; }
done

TGZ=$(mktemp)
trap 'rm -f "$TGZ"' EXIT INT TERM     # 2.3 MB, but leaking temp files is how
                                      # this container has run out of disk before

git -C "$ROOT" fetch --depth=1 origin "$BRANCH"
C=$(git -C "$ROOT" rev-parse FETCH_HEAD)
git -C "$ROOT" show "$C:mathlib-gap-oleans.tgz" > "$TGZ"
N=$(tar tzf "$TGZ" | wc -l)
for d in "${DESTS[@]}"; do
  tar xzf "$TGZ" -C "$d"
  echo "restored $N olean(s) into $d from $BRANCH ($C)"
done
echo "verify with:  source scripts/lean-direct-env.sh && \\"
echo "  lean -DautoImplicit=false -s 65536 content/quantum-observable-universe/mass-theory/reeb-bundle.lean"
