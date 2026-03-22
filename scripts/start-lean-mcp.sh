#!/usr/bin/env bash
# Wrapper for lean-lsp-mcp that ensures lake update/cache before starting.
#
# 1. Checks lean/lake availability
# 2. Runs lake update + cache get if needed (non-blocking on failure)
# 3. Starts lean-lsp-mcp via uvx
#
# Used by .mcp.json as the lean-lsp server command.

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LEAN_DIR="$REPO_ROOT/lean-archive"

export PATH="$HOME/.elan/bin:$HOME/.local/bin:$PATH"

# ── Pre-flight: ensure lean is available ──────────────────────────
if ! command -v lean &>/dev/null; then
    echo "lean not found — lean-lsp-mcp will start but tools may fail" >&2
    echo "Run: ./scripts/setup-lean-mcp.sh" >&2
fi

if ! command -v lake &>/dev/null; then
    echo "lake not found — lean-lsp-mcp will start but tools may fail" >&2
fi

# ── Ensure deps + cache (quick, non-blocking) ────────────────────
if [ -d "$LEAN_DIR" ] && command -v lake &>/dev/null; then
    cd "$LEAN_DIR"

    # lake update if manifest is missing or stale
    if [ ! -f "lake-manifest.json" ]; then
        echo "[lean-mcp] Running lake update..." >&2
        lake update > /tmp/qou-lake-update.log 2>&1 || \
            echo "[lean-mcp] lake update had issues (continuing)" >&2
    fi

    # Fetch cache if Mathlib oleans are missing
    if [ ! -d ".lake/packages/mathlib/.lake/build/lib" ] 2>/dev/null; then
        echo "[lean-mcp] Fetching Mathlib cache..." >&2
        lake exe cache get > /tmp/qou-lake-cache.log 2>&1 || \
            echo "[lean-mcp] cache fetch had issues (continuing)" >&2
    fi
fi

# ── Start lean-lsp-mcp ───────────────────────────────────────────
cd "$LEAN_DIR" 2>/dev/null || cd "$REPO_ROOT"
exec uvx lean-lsp-mcp "$@"
