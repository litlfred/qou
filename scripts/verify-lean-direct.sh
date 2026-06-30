#!/usr/bin/env bash
# Verify a single QOU .lean file with lean-direct (no lake rebuild storm).
# Usage: scripts/verify-lean-direct.sh <path-to-.lean> [out.olean]
set -e
export PATH="$HOME/.elan/bin:$PATH"
cd "$(git rev-parse --show-toplevel)"
LP=""
for d in $(find .lake/packages -path '*/.lake/build/lib' -type d 2>/dev/null); do
  if [ -d "$d/lean" ]; then LP="$LP:$d/lean"; else LP="$LP:$d"; fi
done
QD="content/quantum-observable-universe/lean/.lake/build/lib"
LP="$LP:$QD:$QD/lean"
export LEAN_PATH="${LP#:}"
F="$1"
if [ -n "$2" ]; then
  timeout 500 lean -o "$2" "$F"
else
  timeout 500 lean "$F"
fi
echo "EXIT: $?"
