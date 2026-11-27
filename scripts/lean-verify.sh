#!/usr/bin/env bash
# Verify Lean file(s) with `lean`-direct — type-checks against the
# restored Mathlib/QOU oleans WITHOUT invoking `lake`.
#
# Why not `lake build`?  Even for one module, `lake` re-resolves the dep
# graph, rebuilds Mathlib from source (the `import Mathlib.Tactic`
# closure is ~3000 modules), AND can wipe the restored oleans on a
# remote-URL mismatch. `lean`-direct sidesteps lake entirely: exit 0
# means the file type-checks. It does NOT mean sorry-free: a `sorry` is a
# warning and lean still exits 0. The verify line therefore reports the
# count of `declaration uses 'sorry'` warnings, and LEAN_VERIFY_NO_SORRY=1
# turns any such warning into a failure (bean qou-zf7n).
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

# Ensure oleans are present (restore on demand).  Count under REPO_ROOT —
# that is where lean-cache-restore.sh extracts the payload (and what
# lean-verify-siblings.sh checks).  $LEAN_DIR/.lake holds only a vestigial
# handful of oleans, so counting there reported "missing" on a fully
# restored tree and re-ran the restore on every invocation.
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
  # -DautoImplicit=false -s 65536 mirror the lakefile leanOptions; a bare lean
  # auto-binds unbound identifiers and exits 0 on broken files (bean qou-zf7n).
  out=$(env LEAN_PATH="$LP" ELAN_NO_OVERRIDE_NOTICE=1 lean -DautoImplicit=false -s 65536 "$f" 2>&1)
  lrc=$?
  [ -n "$out" ] && printf '%s\n' "$out"
  nsorry=$(printf '%s\n' "$out" | grep -c "declaration uses 'sorry'")
  if [ "$lrc" -eq 0 ] && [ "$nsorry" -eq 0 ]; then
    echo "  ✓ exit 0 — checks, sorry-free"
  elif [ "$lrc" -eq 0 ] && [ "${LEAN_VERIFY_NO_SORRY:-0}" != "1" ]; then
    echo "  ⚠ exit 0 — checks, but $nsorry declaration(s) use sorry (NOT sorry-free)"
  elif [ "$lrc" -eq 0 ]; then
    echo "  ✗ FAILED — $nsorry declaration(s) use sorry (LEAN_VERIFY_NO_SORRY=1)" >&2
    rc=1
  else
    echo "  ✗ FAILED (see diagnostics above)" >&2
    rc=1
  fi
done
exit $rc
