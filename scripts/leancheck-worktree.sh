#!/usr/bin/env bash
# lean-direct verification helper for a worktree-isolated agent.
#
# The worktree has no .lake/ (gitignored), so LEAN_PATH must point at the MAIN
# checkout's restored olean cache. NEVER run `lake` against that tree: the
# oleans are restored without .trace files, so Lake treats them as stale,
# rebuilds from source and EVICTS the restore (bean `qou-r13s`).
#
# Any QOU module the target imports that is NOT already present in the main
# checkout's build dir is compiled here, lean-direct, into a worktree-local
# scratch olean tree (.leanscratch/, gitignored) which is prepended to
# LEAN_PATH. Nothing is written into the main checkout.
#
# Usage:
#   scripts/leancheck-worktree.sh --dep QOU.Mass.SelfMutualPartition ... -- <file.lean> ...
#   scripts/leancheck-worktree.sh <file.lean> ...
set -u
export PATH="$HOME/.elan/bin:$PATH"
M=/home/user/qou
W="$(cd "$(dirname "$0")/.." && pwd)"
S="$W/.leanscratch"
mkdir -p "$S"

P="$S:"
for d in mathlib batteries aesop Qq proofwidgets importGraph LeanSearchClient plausible Cli; do
  P="$P$M/.lake/packages/$d/.lake/build/lib/lean:"
done
P="$P$M/content/quantum-observable-universe/lean/.lake/build/lib/lean"
export LEAN_PATH="$P"

DEPS=()
while [ $# -gt 0 ]; do
  case "$1" in
    --dep) DEPS+=("$2"); shift 2 ;;
    --) shift; break ;;
    *) break ;;
  esac
done

for mod in ${DEPS+"${DEPS[@]}"}; do
  rel="${mod//.//}"
  src="$W/content/quantum-observable-universe/lean/$rel.lean"
  out="$S/$rel.olean"
  if [ -f "$S/$rel.olean" ]; then echo "=== dep cached $mod"; continue; fi
  mkdir -p "$(dirname "$out")"
  echo "=== dep build $mod"
  timeout 1800 lean "$src" -o "$out" || { echo "=== dep FAILED $mod"; exit 1; }
done

rc=0
for f in "$@"; do
  echo "=== lean $f"
  timeout 1800 lean "$f"
  s=$?
  echo "=== exit $s  ($f)"
  [ "$s" -ne 0 ] && rc=$s
done
exit $rc
