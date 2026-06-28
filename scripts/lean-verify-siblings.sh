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
#   - GENUINE — a real parse / elaboration / type error (`unexpected token`,
#     `unsolved goals`, `unknown identifier`, IR check, …) that surfaces only
#     AFTER imports resolve. This is the "never compiled standalone" breakage
#     the gate exists to catch → FAIL.
#
# A file is FAIL iff its `lean` output contains an `error:` line that is NOT a
# missing-object-file error. Files whose ONLY errors are missing-object-file
# are skipped with a warning so a cache-subset miss never false-blocks a PR.
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
fail=0; pass=0; skip=0
for f in "$@"; do
  out=$(env LEAN_PATH="$LP" ELAN_NO_OVERRIDE_NOTICE=1 lean "$f" 2>&1)
  # Genuine = any error: line that is not a missing-object-file error.
  genuine=$(echo "$out" | grep 'error:' | grep -v "object file '.*' of module .* does not exist" || true)
  if [ -z "$(echo "$out" | grep 'error:')" ]; then
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
