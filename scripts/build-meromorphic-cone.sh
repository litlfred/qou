#!/usr/bin/env bash
# Build the Mathlib `Meromorphic` olean cone from pinned mathlib source.
#
# WHY: the restored `lake-cache/qou-<slug>` olean cache ships only the subset of
# Mathlib that the QOU library transitively imports. The `Mathlib.Analysis.
# Meromorphic.*` cone (divisor / normal-form API) is NOT in that subset, so files
# that use it (e.g. `QOU/QBeta/RatioEntireOfSameDivisor.lean`) cannot be verified
# `lean`-direct until this cone is built. CI has full Mathlib and is unaffected.
#
# This script clones mathlib SOURCE at the pinned rev (github egress works even
# when the release-server olean cache / `lake exe cache get` are firewalled) and
# compiles ONLY the ~10 missing Meromorphic-cone modules into the mathlib olean
# dir, using the already-restored oleans as the dependency base. Total ~2 min of
# `lean`-direct compiles (no `lake` rebuild storm).
#
# Idempotent: skips modules whose olean already exists. Safe to re-run.
#
# Usage:  scripts/build-meromorphic-cone.sh
# Exit:   0 = cone present (built or already there); non-zero = build failure.
set -uo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"
export PATH="$HOME/.elan/bin:$HOME/.elan/toolchains/leanprover--lean4---v4.24.0/bin:$PATH"
source scripts/lib/lean-env.sh 2>/dev/null

OLE="$REPO_ROOT/.lake/packages/mathlib/.lake/build/lib/lean"
# Pinned mathlib rev (must match lake-manifest.json).
REV="$(python3 - <<'PY'
import json
d = json.load(open('lake-manifest.json'))
for p in d.get('packages', []):
    if p.get('name') == 'mathlib':
        print(p.get('rev')); break
PY
)"
[ -n "$REV" ] || { echo "build-meromorphic-cone: could not read mathlib rev from lake-manifest.json" >&2; exit 1; }

# Topologically-ordered missing modules (deps first). If Mathlib re-shuffles the
# Meromorphic cone this list may need refreshing — recompute with the BFS in the
# session audit (docs/audits/2026-07-24-meromorphic-infra-build.md).
mods=(
  Mathlib.Analysis.Analytic.Order
  Mathlib.Analysis.Meromorphic.Basic
  Mathlib.Algebra.Order.WithTop.Untop0
  Mathlib.Analysis.Meromorphic.Order
  Mathlib.Analysis.Meromorphic.TrailingCoefficient
  Mathlib.Topology.LocallyFinsupp
  Mathlib.Analysis.Meromorphic.Divisor
  Mathlib.Analysis.Meromorphic.NormalForm
  Mathlib.Analysis.Meromorphic.IsolatedZeros
  Mathlib.Analysis.Meromorphic.FactorizedRational
)

# Already built?
present=1
for m in "${mods[@]}"; do
  [ -f "$OLE/${m//.//}.olean" ] || { present=0; break; }
done
if [ "$present" = 1 ]; then
  echo "build-meromorphic-cone: cone already present — skipping."
  exit 0
fi

SRC="${MATHLIB_SRC:-$REPO_ROOT/../mathlib4-src}"
if [ ! -f "$SRC/Mathlib/Analysis/Meromorphic/Order.lean" ]; then
  echo "build-meromorphic-cone: cloning mathlib source @ $REV -> $SRC"
  rm -rf "$SRC"; mkdir -p "$SRC"
  git -C "$SRC" init -q
  git -C "$SRC" remote add origin https://github.com/leanprover-community/mathlib4.git
  git -C "$SRC" fetch --depth 1 origin "$REV" || { echo "fetch failed" >&2; exit 1; }
  git -C "$SRC" checkout -q FETCH_HEAD
fi

export LEAN_PATH="$(lean_leanpath 2>/dev/null)"
for m in "${mods[@]}"; do
  rel="${m//.//}"; out="$OLE/$rel.olean"
  [ -f "$out" ] && { echo "  skip (present) $m"; continue; }
  mkdir -p "$(dirname "$out")"
  echo ">>> $m"
  if ! lean --root="$SRC" -o "$out" "$SRC/$rel.lean"; then
    echo "build-meromorphic-cone: FAILED $m" >&2; exit 1
  fi
done
echo "build-meromorphic-cone: cone built."
