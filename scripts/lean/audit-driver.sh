#!/usr/bin/env bash
# Kernel-level borrowed-name audit driver.
#
# Usage:  scripts/lean/audit-driver.sh <Module.Name> [Module.Name ...]
# Emits one JSON object per module on stdout.
#
# Requires oleans for the target modules.  Restore them with the lake-cache
# recipe in AGENTS.md 3715 / local/lean-environment-setup.md 210, VERBATIM.
#
# Failure mode worth knowing, because retyping the recipe from memory hits it:
# the blobs are `lake-oleans.tgz.part00..17` (plural).  Typing `lake-olean.`
# matches nothing, and the pipeline does not fail -- it writes a 0-byte tarball
# and reports `gzip: stdin: unexpected end of file`, which reads like a corrupt
# cache rather than a typo.  The recipe in the docs is correct; copy it.
#
# Second trap: the tarball restores the ROOT workspace
# (`.lake/packages/*/.lake/build/lib/lean`), NOT
# `content/<paper>/lean/.lake/packages/...`.  A LEAN_PATH built from the
# per-paper package dir finds batteries but no Mathlib, and the resulting
# "unknown module prefix 'Mathlib'" looks like a missing cache.  Hence the
# ROOT-anchored LP below.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
export PATH="$HOME/.elan/bin:$PATH" ELAN_NO_OVERRIDE_NOTICE=1

LP=""
for d in "$ROOT"/.lake/packages/*/.lake/build/lib/lean; do LP="$LP$d:"; done
LP="$LP$ROOT/content/quantum-observable-universe/lean/.lake/build/lib/lean"
LP="$LP:$ROOT/scripts/lean"
export LEAN_PATH="$LP"

lean "$ROOT/scripts/lean/BorrowedNameKernel.lean" \
     -o "$ROOT/scripts/lean/BorrowedNameKernel.olean" 2>/dev/null

TMP="$(mktemp /tmp/bnk-XXXX.lean)"
{
  for m in "$@"; do echo "import $m"; done
  echo "import BorrowedNameKernel"
  echo "open Lean Elab Command BorrowedNameKernel"
  echo "run_cmd liftTermElabM do"
  for m in "$@"; do
    echo "  logInfo (render \`$m (<- analyzeModule \`$m))"
  done
} > "$TMP"
lean "$TMP" 2>&1 | grep -v '^warning:' | grep -v 'deprecated'
rm -f "$TMP"
