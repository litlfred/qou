#!/usr/bin/env bash
# Compile a witness fragment against content-block `.lean` siblings.
#
# WHY THIS EXISTS.  A content-block sibling under `content/<paper>/<chapter>/`
# is not a module: it has no olean and nothing can `import` it.  So a witness
# that needs to see a class declared in one — an inhabitation instance, a
# refutation, a pass-band theorem — cannot be written as an ordinary importing
# file.  The route is copy-and-compile: concatenate the siblings ahead of the
# fragment, hoist every `import` line to the top, and hand the result to
# `lean`-direct.
#
# USAGE
#     scripts/lean-sibling-witness-check.sh <fragment.lean> <sibling.lean>...
#
# The fragment must carry NO imports of its own (the siblings supply them); it
# opens the siblings' namespaces instead.  Exit 0 iff `lean` reports no errors.
#
# NEVER `lake build` here.  A build against a restored olean cache with
# `traces=0` treats every olean as stale and evicts the restore (bean qou-r13s).
set -uo pipefail

if [ "$#" -lt 2 ]; then
  echo "usage: $0 <fragment.lean> <sibling.lean>..." >&2
  exit 2
fi

FRAGMENT="$1"; shift
ROOT="$(git rev-parse --show-toplevel)"
export PATH="$HOME/.elan/bin:$PATH"

# LEAN_PATH: every restored package lib plus the QOU build lib.
LP=""
for d in "$ROOT"/.lake/packages/*/.lake/build/lib/lean; do
  [ -d "$d" ] && LP="$LP:$d"
done
LP="$LP:$ROOT/folio/quantum-observable-universe/lean/.lake/build/lib/lean"
export LEAN_PATH="${LP#:}"

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT INT TERM
COMBINED="$TMP/combined.lean"

# Imports first, deduplicated and in first-seen order; then the bodies.
for f in "$@" "$FRAGMENT"; do
  grep -h '^import ' "$f" 2>/dev/null || true
done | awk '!seen[$0]++' > "$COMBINED"
# `linarith` is used by fragments and is not always pulled in by the siblings.
grep -qx 'import Mathlib.Tactic.Linarith' "$COMBINED" \
  || echo 'import Mathlib.Tactic.Linarith' >> "$COMBINED"

for f in "$@" "$FRAGMENT"; do
  printf '\n-- ==== %s ====\n' "$f" >> "$COMBINED"
  grep -v '^import ' "$f" >> "$COMBINED"
done

OUT="$TMP/out.txt"
timeout "${LEAN_TIMEOUT:-900}" lean "$COMBINED" > "$OUT" 2>&1
rc=$?

if grep -q 'error:' "$OUT"; then
  echo "FAIL: $FRAGMENT"
  grep -n 'error:' -A6 "$OUT" | head -60
  exit 1
fi
if [ "$rc" -ne 0 ]; then
  echo "FAIL (lean exit $rc): $FRAGMENT"
  tail -20 "$OUT"
  exit 1
fi
echo "OK: $FRAGMENT against $# sibling(s)"
