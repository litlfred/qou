#!/usr/bin/env bash
# Session-start hook: check if Lean toolchain + MCP server are available.
# Prints JSON status for Claude Code to consume.

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LEAN_DIR="$REPO_ROOT/lean"

export PATH="$HOME/.elan/bin:$HOME/.local/bin:$PATH"

# Check elan/lean
if ! command -v lean &>/dev/null; then
    echo '{"lean_available": false, "uv_available": false, "message": "Lean not installed. Run: ./scripts/setup-lean-mcp.sh"}'
    exit 1
fi

# Check uv (needed for uvx lean-lsp-mcp)
UV_OK=true
if ! command -v uv &>/dev/null; then
    UV_OK=false
fi

# Check toolchain
TOOLCHAIN=$(cat "$LEAN_DIR/lean-toolchain" 2>/dev/null | tr -d '[:space:]')
if [ -z "$TOOLCHAIN" ]; then
    echo '{"lean_available": false, "message": "No lean-toolchain file found"}'
    exit 1
fi

LEAN_VERSION=$(lean --version 2>&1 | head -1)
if [ $? -ne 0 ]; then
    echo "{\"lean_available\": false, \"message\": \"Lean failed version check. Run: elan toolchain install $TOOLCHAIN\"}"
    exit 1
fi

# Check dependencies
DEPS_READY=true
if [ ! -f "$LEAN_DIR/lake-manifest.json" ]; then
    DEPS_READY=false
fi

# Check ripgrep (optional)
RG_OK=false
if command -v rg &>/dev/null; then
    RG_OK=true
fi

echo "{\"lean_available\": true, \"deps_ready\": $DEPS_READY, \"uv_available\": $UV_OK, \"ripgrep\": $RG_OK, \"version\": \"$LEAN_VERSION\"}"
exit 0
