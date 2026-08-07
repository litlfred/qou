#!/usr/bin/env bash
# lean-direct-cone.sh — compile a QOU module's import cone with `lean` directly.
#
# Motivation: `lake build <Module>` re-resolves the dependency graph and rebuilds
# Mathlib from source (~3000 modules for the `import Mathlib.Tactic` closure), and
# in a sandbox it also wipes oleans restored from the `lake-cache/*` branch. When the
# Mathlib oleans are already present under `.lake/packages/*/.lake/build/lib/lean`,
# we can bypass Lake entirely: topologically sort the QOU cone and run `lean -o` on
# each module in order, writing oleans into the normal `.lake/build/lib/lean` tree.
#
# Usage:  scripts/lean-direct-cone.sh QOU.BraidKnot.HookProductHLF
#
# Exit 0 = every module in the cone type-checks.
set -euo pipefail

TARGET="${1:?usage: lean-direct-cone.sh <QOU.Module.Name>}"
ROOT="$(git rev-parse --show-toplevel)"
LEANDIR="$ROOT/content/quantum-observable-universe/lean"
OUT="$LEANDIR/.lake/build/lib/lean"

export PATH="$HOME/.elan/bin:$PATH"

# LEAN_PATH: every dependency package's olean dir, plus our own output dir.
LP="$OUT"
for p in "$ROOT"/.lake/packages/*/.lake/build/lib/lean; do
  [ -d "$p" ] && LP="$LP:$p"
done
export LEAN_PATH="$LP"

mkdir -p "$OUT"

# Topologically sort the QOU import cone of TARGET (deps first).
mapfile -t ORDER < <(cd "$LEANDIR" && python3 - "$TARGET" <<'PY'
import re, os, sys
target = sys.argv[1]
imp = {}
for dp, _, fs in os.walk("QOU"):
    for f in fs:
        if f.endswith(".lean"):
            p = os.path.join(dp, f)
            mod = p[:-5].replace("/", ".")
            imp[mod] = [m for m in re.findall(
                r'^import\s+(QOU\.[\w.]+)', open(p).read(), re.M)]
order, state = [], {}
def visit(m):
    st = state.get(m)
    if st == 2:
        return
    if st == 1:
        raise SystemExit(f"IMPORT CYCLE at {m}")
    state[m] = 1
    for d in imp.get(m, ()):
        visit(d)
    state[m] = 2
    order.append(m)
visit(target)
print("\n".join(order))
PY
)

echo "cone: ${#ORDER[@]} modules"
built=0; skipped=0
# Modules rebuilt this run; a module must rebuild if ANY module it imports did, else
# it would keep an olean compiled against a stale dependency (silent staleness).
declare -A DIRTY=()
for mod in "${ORDER[@]}"; do
  src="$LEANDIR/${mod//.//}.lean"
  olean="$OUT/${mod//.//}.olean"
  # Stale if older than its own source, or older than any dependency's olean
  # (the latter catches a dep rebuilt in an *earlier* run — mtime-vs-source alone
  # would silently keep an olean compiled against a since-changed dependency).
  dep_dirty=0
  while read -r d; do
    [ -z "$d" ] && continue
    [ -n "${DIRTY[$d]:-}" ] && dep_dirty=1
    dolean="$OUT/${d//.//}.olean"
    [ -f "$dolean" ] && [ "$dolean" -nt "$olean" ] && dep_dirty=1
  done < <(grep -oP '^import\s+\KQOU\.[\w.]+' "$src" || true)
  if [ "$dep_dirty" -eq 0 ] && [ -f "$olean" ] && [ "$olean" -nt "$src" ]; then
    skipped=$((skipped + 1))
    continue
  fi
  DIRTY[$mod]=1
  mkdir -p "$(dirname "$olean")"
  printf '  [%3d/%3d] %s ... ' "$((built + skipped + 1))" "${#ORDER[@]}" "$mod"
  if lean -o "$olean" -i "${olean%.olean}.ilean" "$src"; then
    echo "ok"
    built=$((built + 1))
  else
    echo "FAILED"
    exit 1
  fi
done
echo "done: $built built, $skipped up-to-date"
