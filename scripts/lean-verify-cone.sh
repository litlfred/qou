#!/usr/bin/env bash
# Verify edited Lean files AND their consumers, without the stale-olean trap.
#
# Why this script exists (bean qou-fjcd)
# --------------------------------------
# `lean`-direct verification reads the file on the command line from SOURCE,
# but every one of its imports from a compiled `.olean`.  So after editing
# file A, running `lean B.lean` (where B imports A) checks B against the OLD
# A.  It prints OK and means nothing.
#
# This bit a session on 2026-08-08: PR #4750 claimed "lean-direct exit 0 on
# every consumer" when the consumer checks had all run against oleans still
# containing the instances that had just been removed.  The conclusion
# happened to hold, but the check had not actually been performed.
#
# Usage
# -----
#   scripts/lean-verify-cone.sh QOU/A.lean QOU/B.lean -- QOU/Consumer1.lean ...
#
# Files before `--` are the ones you EDITED: each is compiled and its olean
# is REPLACED, in the order given (so list them dependency-order, base first).
# Files after `--` are consumers, checked only once every olean is fresh.
#
# With no `--`, every argument is treated as edited (rebuild + verify).
set -uo pipefail

ROOT=$(git rev-parse --show-toplevel)
LEAN_DIR="$ROOT/folio/quantum-observable-universe/lean"
BUILD="$LEAN_DIR/.lake/build/lib/lean"

export PATH="$HOME/.elan/bin:$PATH"
LP=""
for d in "$ROOT"/.lake/packages/*/.lake/build/lib/lean \
         "$ROOT"/.lake/build/lib/lean \
         "$BUILD"; do
  [ -d "$d" ] && LP="$LP:$d"
done
export LEAN_PATH="${LP#:}"

if [ -z "${LEAN_PATH:-}" ]; then
  echo "error: no olean directories found — restore the lake-cache branch first" >&2
  echo "       (see .claude/skills/local/lean-environment-setup.md)" >&2
  exit 2
fi

edited=(); consumers=(); seen_sep=0
for a in "$@"; do
  if [ "$a" = "--" ]; then seen_sep=1; continue; fi
  if [ "$seen_sep" -eq 1 ]; then consumers+=("$a"); else edited+=("$a"); fi
done

if [ ${#edited[@]} -eq 0 ]; then
  echo "usage: $0 <edited.lean>... [-- <consumer.lean>...]" >&2
  exit 2
fi

cd "$LEAN_DIR"
rc=0

echo "== rebuilding oleans for ${#edited[@]} edited file(s) =="
for f in "${edited[@]}"; do
  rel="${f#folio/quantum-observable-universe/lean/}"
  out="$BUILD/${rel%.lean}.olean"
  mkdir -p "$(dirname "$out")"
  if lean -o "$out" "$rel"; then
    echo "  OK      $rel  (olean refreshed)"
  else
    echo "  FAIL    $rel"
    # Leave the stale olean in place rather than a half-written one, and stop:
    # checking consumers now would repeat the exact bug this script prevents.
    echo "error: aborting before consumer checks — a failed rebuild leaves a" >&2
    echo "       stale olean, so any consumer result would be meaningless." >&2
    exit 1
  fi
done

if [ ${#consumers[@]} -gt 0 ]; then
  echo "== checking ${#consumers[@]} consumer(s) against fresh oleans =="
  for f in "${consumers[@]}"; do
    rel="${f#folio/quantum-observable-universe/lean/}"
    if lean "$rel"; then echo "  OK      $rel"; else echo "  FAIL    $rel"; rc=1; fi
  done
fi

exit $rc
