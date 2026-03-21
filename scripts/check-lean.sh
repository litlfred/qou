#!/usr/bin/env bash
# Session-start hook: check if Lean toolchain + dependencies + MCP are ready.
# Scans lakefile.toml for required dependencies and verifies they're fetched.
# Prints JSON status for Claude Code to consume.
#
# Run on every session start via .claude/settings.json SessionStart hook.

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LEAN_DIR="$REPO_ROOT/lean"
LAKEFILE="$LEAN_DIR/lakefile.toml"
MANIFEST="$LEAN_DIR/lake-manifest.json"

export PATH="$HOME/.elan/bin:$HOME/.local/bin:$PATH"

# ── Check lean ────────────────────────────────────────────────────
if ! command -v lean &>/dev/null; then
    echo '{"lean_available": false, "message": "Lean not installed. Run: ./scripts/setup-lean-mcp.sh"}'
    exit 1
fi

# ── Check uv (needed for uvx lean-lsp-mcp) ───────────────────────
UV_OK=true
if ! command -v uv &>/dev/null; then
    UV_OK=false
fi

# ── Check toolchain ──────────────────────────────────────────────
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

# ── Check ripgrep (optional) ─────────────────────────────────────
RG_OK=false
if command -v rg &>/dev/null; then
    RG_OK=true
fi

# ── Scan lakefile.toml for required dependencies ──────────────────
DEPS_READY=true
MISSING_DEPS=""

if [ -f "$LAKEFILE" ] && [ -f "$MANIFEST" ]; then
    # Extract required dependency names from lakefile.toml
    REQUIRED_DEPS=$(grep -A1 '^\[\[require\]\]' "$LAKEFILE" | grep 'name' | sed 's/.*= *"\(.*\)"/\1/' | tr -d '"' | tr -d ' ')

    # Check each required dep exists in lake-manifest.json
    for dep in $REQUIRED_DEPS; do
        if ! grep -q "\"name\": *\"$dep\"" "$MANIFEST" 2>/dev/null && \
           ! grep -q "\"name\":\"$dep\"" "$MANIFEST" 2>/dev/null; then
            DEPS_READY=false
            if [ -z "$MISSING_DEPS" ]; then
                MISSING_DEPS="$dep"
            else
                MISSING_DEPS="$MISSING_DEPS, $dep"
            fi
        fi
    done
elif [ ! -f "$MANIFEST" ]; then
    DEPS_READY=false
    MISSING_DEPS="all (no lake-manifest.json)"
fi

# ── Check if oleans exist (Mathlib cache) ─────────────────────────
CACHE_OK=true
if [ ! -d "$LEAN_DIR/.lake/packages/mathlib/.lake/build/lib" ] 2>/dev/null; then
    CACHE_OK=false
fi

# ── Build result JSON ─────────────────────────────────────────────
MSG=""
if [ "$DEPS_READY" = false ]; then
    MSG="Missing dependencies: $MISSING_DEPS. Run: cd lean && lake update && lake exe cache get"
elif [ "$CACHE_OK" = false ]; then
    MSG="Mathlib cache missing. Run: cd lean && lake exe cache get"
elif [ "$UV_OK" = false ]; then
    MSG="uv not installed (needed for MCP server). Run: curl -LsSf https://astral.sh/uv/install.sh | sh"
fi

if [ -n "$MSG" ]; then
    echo "{\"lean_available\": true, \"deps_ready\": $DEPS_READY, \"cache_ok\": $CACHE_OK, \"uv_available\": $UV_OK, \"ripgrep\": $RG_OK, \"version\": \"$LEAN_VERSION\", \"message\": \"$MSG\"}"
else
    echo "{\"lean_available\": true, \"deps_ready\": true, \"cache_ok\": true, \"uv_available\": $UV_OK, \"ripgrep\": $RG_OK, \"version\": \"$LEAN_VERSION\"}"
fi
exit 0
