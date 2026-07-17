#!/usr/bin/env bash
# CI-oriented compile check for content-block .lean siblings.
#
# Wraps `lean`-direct (LEAN_PATH = restored mathlib + QOU oleans) but
# DISTINGUISHES two failure classes that a bare `lean` exit code conflates:
#
#   - INFRA / cache-miss — the file imports a Mathlib (or QOU) module whose
#     olean is NOT in the restored lake-cache subset (the cache ships only
#     QOU's transitive dependency cone, not all of Mathlib). Lean reports
#     `object file '…/X.olean' of module X does not exist`. This is a runner
#     limitation, NOT a defect in the PR's file → NEUTRAL-SKIP (warning).
#
#   - CROSS-PAPER cache miss — a content sibling under paper A imports a
#     sibling-paper package root B (`import UGB.…` from a QOU sibling). When
#     B's oleans are not on the verification path (e.g. CI restores only the
#     mathlib + QOU cones, never builds UGB) Lean cannot even open the prefix
#     and reports `unknown module prefix 'UGB'`. This is the same class as the
#     missing-object-file miss — a cache-cone limitation, NOT a defect — so it
#     is NEUTRAL-SKIPPED, but ONLY for the known paper-package roots
#     (QOU / UGB / Fred2005). A typo'd prefix (`Mathlibb`, `Qou`) still FAILs.
#
#   - GENUINE — a real parse / elaboration / type error (`unexpected token`,
#     `unsolved goals`, `unknown identifier`, IR check, …) that surfaces only
#     AFTER imports resolve. This is the "never compiled standalone" breakage
#     the gate exists to catch → FAIL.
#
#   - STALE IMPORT (bean ckj6, 2026-07-17) — a missing-object-file error whose
#     module does NOT EXIST at the pinned Mathlib rev (renamed/removed module)
#     or names a QOU module with no source file. Indistinguishable from a
#     cache-cone miss by the lean output alone — both print the same
#     `object file … does not exist` — which is how 64 stale imports hid as
#     neutral-skips until 2026-07-01. Disambiguated against the COMMITTED
#     module list `scripts/data/mathlib-modules.txt` (from the pinned rev's
#     `Mathlib.lean` aggregator; regen recipe in its header) and, for `QOU.*`,
#     the in-repo source tree → FAIL. If the list's rev no longer matches
#     `lake-manifest.json` (Mathlib bump without regenerating the list) the
#     check degrades to the old neutral-skip behavior with a warning.
#
# A file is FAIL iff its `lean` output contains an `error:` line that is NOT a
# missing-object-file error and NOT a known-paper-package `unknown module
# prefix`, OR any missing module is provably nonexistent (stale import). Files
# whose ONLY errors are true cache-cone misses are skipped with a warning so a
# cache-subset miss never false-blocks a PR.
#
# Usage:  scripts/lean-verify-siblings.sh <file.lean> [more.lean ...]
# Exit:   0 = all files pass or neutral-skip; 1 = ≥1 genuine error;
#         2 = bad usage; 127 = `lean` not installed.
set -uo pipefail
source "$(dirname "$0")/lib/lean-env.sh"

[ "$#" -eq 0 ] && { echo "usage: $0 <file.lean> [more.lean ...]" >&2; exit 2; }
has lean || { echo "lean-verify-siblings: 'lean' not on PATH" >&2; exit 127; }

# Ensure oleans present (restore on demand; root .lake is the workspace).
existing=$(find "$REPO_ROOT/.lake/packages/mathlib" -name '*.olean' 2>/dev/null | wc -l | tr -d ' ')
if [ "${existing:-0}" -lt 2000 ]; then
  "$(dirname "$0")/lean-cache-restore.sh" || { echo "::warning::olean cache unavailable — skipping all" >&2; exit 0; }
else
  lean_mathlib_url_fix
fi

LP="$(lean_leanpath)"

# Stale-import disambiguation data (bean ckj6): the committed module list is
# authoritative for the pinned Mathlib rev; on rev mismatch, disable the check.
MODLIST="$REPO_ROOT/scripts/data/mathlib-modules.txt"
if [ -f "$MODLIST" ]; then
  list_rev=$(sed -n 's/^# mathlib-rev: //p' "$MODLIST" | head -1)
  pin_rev=$(sed -n 's/.*"rev": "\([0-9a-f]\{40\}\)".*/\1/p' "$REPO_ROOT/lake-manifest.json" | head -20 | grep -F "${list_rev:-nomatch}" | head -1)
  if [ -z "$pin_rev" ]; then
    echo "::warning::mathlib-modules.txt rev ($list_rev) not found in lake-manifest.json — stale-import check disabled; regenerate the list (header recipe)" >&2
    MODLIST=""
  fi
fi
QOU_SRC_ROOT="$REPO_ROOT/content/quantum-observable-universe/lean"

fail=0; pass=0; skip=0
for f in "$@"; do
  out=$(env LEAN_PATH="$LP" ELAN_NO_OVERRIDE_NOTICE=1 lean "$f" 2>&1)
  # Reclassify missing-object-file misses whose module provably does not exist
  # (removed/renamed Mathlib module, or QOU module with no source) → stale.
  stale=""
  for m in $(echo "$out" | grep -oE "of module '?[A-Za-z0-9_.]+'? does not exist" | sed "s/of module '\{0,1\}//; s/'\{0,1\} does not exist//" | sort -u); do
    case "$m" in
      Mathlib|Batteries|Aesop|Qq|Plausible|ImportGraph|LeanSearchClient|ProofWidgets) ;;
      Mathlib.*)
        if [ -n "$MODLIST" ] && ! grep -qx "$m" "$MODLIST"; then stale="$stale $m"; fi ;;
      QOU.*)
        [ -f "$QOU_SRC_ROOT/$(echo "$m" | tr '.' '/').lean" ] || stale="$stale $m" ;;
    esac
  done
  # Genuine = any error: line that is neither a missing-object-file error nor a
  # cross-paper `unknown module prefix '<paper-pkg>'` cache-cone miss. The
  # prefix exclusion is scoped to the known paper-package roots so a genuinely
  # typo'd import prefix is still caught as a fail.
  genuine=$(echo "$out" | grep 'error:' \
    | grep -v "object file '.*' of module .* does not exist" \
    | grep -vE "unknown module prefix '(QOU|UGB|Fred2005)'" || true)
  if [ -n "$stale" ]; then
    fail=$((fail+1))
    echo "::error file=$f::STALE IMPORT — module(s) do not exist at the pinned Mathlib rev / in the QOU source tree:$stale"
  elif [ -z "$(echo "$out" | grep 'error:')" ]; then
    pass=$((pass+1)); echo "✓ $f"
  elif [ -z "$genuine" ]; then
    skip=$((skip+1))
    echo "::warning file=$f::neutral-skip — imports a module outside the cached olean cone (cache-subset miss, not a defect)"
  else
    fail=$((fail+1))
    echo "::error file=$f::genuine compile error (never compiled standalone):"
    echo "$genuine" | head -5
  fi
done
echo "lean-verify-siblings: pass=$pass neutral-skip=$skip fail=$fail"
[ "$fail" -eq 0 ]
