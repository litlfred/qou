#!/usr/bin/env bash
# Compile a QOU module and every QOU dependency it needs, in dependency order.
#
# `lean -o` on a module whose imports have no olean fails, so a missing module
# cannot be built in isolation -- its cone has to come first. This walks
# imports depth-first, compiles the leaves, then the module.
#
# Only QOU/UGB/Fred2005 imports are followed; Mathlib comes from the restored
# lake-cache and is never rebuilt (a `lake build` here would EVICT that cache
# -- see AGENTS.md and bean qou-r13s).
#
# Usage: scripts/lean/compile-cone.sh <Module.Name> [Module.Name ...]
set -uo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
export PATH="$HOME/.elan/bin:$PATH" ELAN_NO_OVERRIDE_NOTICE=1
LEANDIR="$ROOT/content/quantum-observable-universe/lean"
B="$LEANDIR/.lake/build/lib/lean"

LP=""
for d in "$ROOT"/.lake/packages/*/.lake/build/lib/lean; do LP="$LP$d:"; done
LP="$LP$B"
export LEAN_PATH="$LP"

declare -A SEEN
compile() {
  local m="$1" rel src olean
  [[ -n "${SEEN[$m]:-}" ]] && return 0
  SEEN[$m]=1
  rel="${m//.//}"
  olean="$B/$rel.olean"
  src="$LEANDIR/$rel.lean"
  [[ -f "$olean" ]] && return 0          # already cached
  [[ -f "$src" ]]   || { echo "  no source: $m" >&2; return 1; }
  # deps first
  while read -r dep; do
    case "$dep" in QOU*|UGB*|Fred2005*) compile "$dep" ;; esac
  done < <(grep -oP '^import \K\S+' "$src")
  mkdir -p "$(dirname "$olean")"
  if timeout "${CONE_TIMEOUT:-300}" lean "$src" -o "$olean" >/dev/null 2>&1; then
    echo "  built: $m"
  else
    rm -f "$olean"; echo "  FAILED: $m" >&2; return 1
  fi
}

for m in "$@"; do echo "== $m"; compile "$m" || echo "  (cone incomplete)"; done
