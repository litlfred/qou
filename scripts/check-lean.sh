#!/usr/bin/env bash
# Session-start hook: check if Lean toolchain is available.
# Returns exit code 0 if Lean is ready, 1 if not.
# Prints a JSON status message for Claude Code to consume.

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LEAN_DIR="$REPO_ROOT/lean"

# Check if elan/lean are on PATH
export PATH="$HOME/.elan/bin:$PATH"

if ! command -v lean &>/dev/null; then
    echo '{"lean_available": false, "message": "Lean not installed. Run: ./scripts/setup-lean-mcp.sh"}'
    exit 1
fi

# Check if the correct toolchain is installed
TOOLCHAIN=$(cat "$LEAN_DIR/lean-toolchain" 2>/dev/null | tr -d '[:space:]')
if [ -z "$TOOLCHAIN" ]; then
    echo '{"lean_available": false, "message": "No lean-toolchain file found"}'
    exit 1
fi

# Quick version check (lean --version is fast)
LEAN_VERSION=$(lean --version 2>&1 | head -1)
if [ $? -ne 0 ]; then
    echo "{\"lean_available\": false, \"message\": \"Lean installed but failed version check. Run: elan toolchain install $TOOLCHAIN\"}"
    exit 1
fi

# Check if lake-manifest exists (dependencies fetched)
if [ ! -f "$LEAN_DIR/lake-manifest.json" ]; then
    echo "{\"lean_available\": true, \"deps_ready\": false, \"version\": \"$LEAN_VERSION\", \"message\": \"Lean OK but dependencies not fetched. Run: cd lean && lake exe cache get\"}"
    exit 0
fi

echo "{\"lean_available\": true, \"deps_ready\": true, \"version\": \"$LEAN_VERSION\"}"
exit 0
