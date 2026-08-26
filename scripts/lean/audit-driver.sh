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
  # A long module list is one big list literal; the elaborator hits
  # `maximum recursion depth` building it (measured: fine at 8, fails at 15).
  echo "set_option maxRecDepth 100000 in"
  # The COMMAND has its own 200000-heartbeat budget, separate from the 20000
  # cap `defeqCollapse` puts around each isDefEq. The whole loop consumes it
  # (measured: 8 modules fit, 15 do not). 0 = unlimited; the per-isDefEq cap
  # still bounds any single hard goal, so a pathological one cannot hang.
  echo "set_option maxHeartbeats 0 in"
  echo "run_cmd liftTermElabM do"
  # ONE pass over the environment for all modules -- see `analyzeModules`.
  printf '  let rs <- analyzeModules ['
  sep=""
  for m in "$@"; do printf '%s`%s' "$sep" "$m"; sep=", "; done
  printf ']\n'
  echo '  for (m, rows) in rs do logInfo (render m rows)' 
} > "$TMP"
lean "$TMP" 2>&1 | grep -v '^warning:' | grep -v 'deprecated'
rm -f "$TMP"
