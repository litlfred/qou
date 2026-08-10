#!/usr/bin/env bash
# Verify changed .lean files with `lean`-direct against the restored olean
# tree, and report each file's REAL exit status.
#
# Why this exists: the obvious one-liner
#     lean "$f" 2>&1 | head -5 && echo "exit 0"
# reports the exit status of `head`, not of `lean` — so a file that failed
# on a missing import prints "exit 0". That false pass is exactly what the
# §"QA is agent-owned" gate must not produce, and it is easy to write by
# accident when you want the first few error lines. Capture to a file and
# test "${PIPESTATUS[0]}" / the bare command's status instead of piping.
#
# It also separates the two failure kinds, which are NOT the same finding:
#   MISSING-OLEAN — a dependency has not been built yet in this container.
#                   Says nothing about the file. Retry after the build.
#   ERROR         — a real elaboration/type error in the file. Actionable.
#
# Usage:
#   scripts/lean-verify-changed.sh                 # every .lean changed vs HEAD~1
#   scripts/lean-verify-changed.sh <file.lean>...  # explicit list
#   REF=origin/main scripts/lean-verify-changed.sh # changed vs another ref
#
# Exit 0 iff every file checked reached exit 0. MISSING-OLEAN counts as a
# failure for the exit code — an unverified file is not a verified one.
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LEAN_ROOT="$ROOT/content/quantum-observable-universe/lean"
export PATH="$HOME/.elan/bin:$PATH"

if ! command -v lean >/dev/null 2>&1; then
  echo "lean-verify-changed: no lean on PATH (try: export PATH=\"\$HOME/.elan/bin:\$PATH\")" >&2
  exit 2
fi

# Resolve explicit arguments to absolute paths BEFORE cd-ing into the Lake
# root — otherwise a repo-relative path silently stops resolving and every
# file reports "SKIP (gone)", which is a false all-clear.
files=()
if [ "$#" -gt 0 ]; then
  for f in "$@"; do
    case "$f" in
      /*) files+=("$f") ;;
      *)  if   [ -f "$PWD/$f"       ]; then files+=("$PWD/$f")
          elif [ -f "$ROOT/$f"      ]; then files+=("$ROOT/$f")
          elif [ -f "$LEAN_ROOT/$f" ]; then files+=("$LEAN_ROOT/$f")
          else files+=("$f")   # keep it, so it is reported as missing not dropped
          fi ;;
    esac
  done
fi

cd "$LEAN_ROOT" || exit 2

# TWO olean trees exist and they are NOT interchangeable:
#   $ROOT/.lake/packages/...                  the ROOT Lake workspace
#   $LEAN_ROOT/.lake/packages/...             the per-paper workspace
# The root workspace is typically the complete one (~6990 mathlib oleans);
# the per-paper tree is often a partial rebuild. Using the per-paper tree
# alone makes files fail with MISSING-OLEAN on `Mathlib.Tactic` and friends
# and reads as "cannot verify" when verification was available all along.
# Put the ROOT packages FIRST so the complete tree wins, and keep the
# per-paper build dir first overall so this paper's own oleans are found.
LP="$LEAN_ROOT/.lake/build/lib/lean"
for p in "$ROOT"/.lake/build/lib/lean "$ROOT"/.lake/packages/*/.lake/build/lib/lean; do
  [ -d "$p" ] && LP="$LP:$p"
done
for p in "$LEAN_ROOT"/.lake/packages/*/.lake/build/lib/lean; do
  [ -d "$p" ] && LP="$LP:$p"
done
export LEAN_PATH="$LP"

if [ "${#files[@]}" -eq 0 ]; then
  ref="${REF:-HEAD~1}"
  while IFS= read -r f; do
    [ -n "$f" ] && files+=("$ROOT/$f")
  done < <(cd "$ROOT" && git diff --name-only "$ref" -- '*.lean')
fi

if [ "${#files[@]}" -eq 0 ]; then
  echo "lean-verify-changed: no .lean files to check"
  exit 0
fi

ok=0; err=0; missing=0; gone=0
log="$(mktemp)"
trap 'rm -f "$log"' EXIT

for f in "${files[@]}"; do
  # A path that does not resolve is NOT a pass — count it, so a typo or a
  # bad relative path cannot masquerade as a clean run.
  [ -f "$f" ] || { gone=$((gone+1)); printf '%-70s NOT-FOUND\n' "$(basename "$f")"; continue; }
  # No pipe: $? is lean's own status.
  timeout "${LEAN_TIMEOUT:-600}" lean "$f" >"$log" 2>&1
  rc=$?
  if [ "$rc" -eq 0 ]; then
    ok=$((ok+1)); printf '%-70s exit 0\n' "$(basename "$f")"
  elif grep -q "does not exist" "$log"; then
    missing=$((missing+1))
    printf '%-70s MISSING-OLEAN (%s)\n' "$(basename "$f")" \
      "$(grep -o "module [A-Za-z0-9_.]*" "$log" | head -1)"
  else
    err=$((err+1)); printf '%-70s ERROR\n' "$(basename "$f")"
    sed 's/^/      /' "$log" | head -8
  fi
done

echo
echo "lean-verify-changed: ${ok} exit 0, ${err} error, ${missing} unverified (missing olean), ${gone} not-found"
[ "$err" -eq 0 ] && [ "$missing" -eq 0 ] && [ "$gone" -eq 0 ] && [ "$ok" -gt 0 ]
