#!/usr/bin/env bash
# Verify Lean file(s) with `lean`-direct — type-checks against the
# restored Mathlib/QOU oleans WITHOUT invoking `lake`.
#
# Why not `lake build`?  Even for one module, `lake` re-resolves the dep
# graph, rebuilds Mathlib from source (the `import Mathlib.Tactic`
# closure is ~3000 modules), AND can wipe the restored oleans on a
# remote-URL mismatch. `lean`-direct sidesteps lake entirely: exit 0
# means the file checks and is sorry-free (a `sorry` emits a warning but
# still exits 0 — grep the output if you need sorry-strictness).
#
# Restores the olean cache first if it is missing.
#
# Usage:  scripts/lean-verify.sh <file.lean> [more.lean ...]
# Exit:   0 = all files check; 1 = a file failed; 2 = bad usage;
#         127 = `lean` not installed.
set -uo pipefail
source "$(dirname "$0")/lib/lean-env.sh"

if [ "$#" -eq 0 ]; then
  echo "usage: $0 <file.lean> [more.lean ...]" >&2
  exit 2
fi
has lean || {
  echo "lean-verify: 'lean' not on PATH — run scripts/setup-lean-toolchain.sh first." >&2
  exit 127
}

# Ensure oleans are present (restore on demand).
existing=$(find "$REPO_ROOT/.lake/packages/mathlib" -name '*.olean' 2>/dev/null | wc -l | tr -d ' ')
if [ "${existing:-0}" -lt 2000 ]; then
  echo "lean-verify: mathlib oleans missing ($existing) — restoring cache first."
  "$(dirname "$0")/lean-cache-restore.sh" || exit $?
else
  lean_mathlib_url_fix
fi

LP="$(lean_leanpath)"
rc=0
for f in "$@"; do
  echo "── lean-verify: $f ──"
  if env LEAN_PATH="$LP" ELAN_NO_OVERRIDE_NOTICE=1 lean "$f"; then
    echo "  ✓ exit 0 — checks"
  else
    echo "  ✗ FAILED (see diagnostics above)" >&2
    rc=1
  fi
done
exit $rc
