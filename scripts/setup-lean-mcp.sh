#!/usr/bin/env bash
# Setup script for Lean 4 + lean-lsp-mcp on ChromeOS/Crostini
#
# Installs:
#   1. uv (Python package manager, needed by lean-lsp-mcp)
#   2. elan + pinned Lean toolchain
#   3. Mathlib cache
#   4. Runs lake build
#   5. Installs ripgrep (for lean_local_search)
#
# Prerequisites: git, curl (assumed installed)
#
# Usage:
#   ./scripts/setup-lean-mcp.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LEAN_DIR="$REPO_ROOT/lean"
TOOLCHAIN_FILE="$LEAN_DIR/lean-toolchain"

echo "=== Lean 4 MCP Setup (lean-lsp-mcp) ==="
echo ""

# ── 1. Install uv ────────────────────────────────────────────────
if command -v uv &>/dev/null; then
    echo "▸ uv already installed: $(uv --version)"
else
    echo "▸ Installing uv (Python package manager)..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
    echo "  ✓ uv installed: $(uv --version)"
fi

# ── 2. Install elan ──────────────────────────────────────────────
if command -v elan &>/dev/null; then
    echo "▸ elan already installed: $(elan --version)"
else
    echo "▸ Installing elan (Lean version manager)..."
    curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh -s -- -y --default-toolchain none
    export PATH="$HOME/.elan/bin:$PATH"
    echo "  ✓ elan installed: $(elan --version)"
fi

export PATH="$HOME/.elan/bin:$HOME/.local/bin:$PATH"

# ── 3. Install the pinned toolchain ──────────────────────────────
if [ -f "$TOOLCHAIN_FILE" ]; then
    TOOLCHAIN=$(cat "$TOOLCHAIN_FILE" | tr -d '[:space:]')
    echo "▸ Installing toolchain: $TOOLCHAIN"
    elan toolchain install "$TOOLCHAIN"
    echo "  ✓ Toolchain ready"
else
    echo "✗ No lean-toolchain file found at $TOOLCHAIN_FILE"
    exit 1
fi

# ── 4. Verify lean and lake ──────────────────────────────────────
echo "▸ Verifying installation..."
cd "$LEAN_DIR"
echo "  lean: $(lean --version 2>&1 | head -1)"
echo "  lake: $(lake --version 2>&1 | head -1)"

# ── 5. Fetch Mathlib cache ───────────────────────────────────────
echo "▸ Fetching Mathlib oleans (this may take a few minutes)..."
lake exe cache get 2>&1 | tail -3
echo "  ✓ Cache fetched"

# ── 6. Build ─────────────────────────────────────────────────────
echo "▸ Running lake build (recommended before first MCP session)..."
if lake build 2>&1 | tail -5; then
    echo "  ✓ Build succeeded"
else
    echo "  ⚠ Build had errors (MCP server will still work for diagnostics)"
fi

# ── 7. Install ripgrep (optional, for lean_local_search) ─────────
if command -v rg &>/dev/null; then
    echo "▸ ripgrep already installed"
else
    echo "▸ Installing ripgrep (for lean_local_search)..."
    if sudo apt-get install -y -qq ripgrep 2>/dev/null; then
        echo "  ✓ ripgrep installed"
    else
        echo "  ⚠ ripgrep not available via apt — lean_local_search will be disabled"
    fi
fi

# ── 8. Verify lean-lsp-mcp is runnable ───────────────────────────
echo "▸ Checking lean-lsp-mcp..."
if uvx lean-lsp-mcp --help &>/dev/null; then
    echo "  ✓ lean-lsp-mcp available via uvx"
else
    echo "  ⚠ lean-lsp-mcp test failed (uvx will auto-install it on first use)"
fi

echo ""
echo "=== Setup complete ==="
echo ""
echo "The .mcp.json in the repo root configures lean-lsp-mcp for Claude Code."
echo "Claude Code will auto-start the MCP server on next session."
echo ""
echo "Quick reference:"
echo "  lake build              — rebuild Lean files"
echo "  lake exe cache get      — refresh Mathlib cache"
echo "  lean --version          — check Lean version"
echo "  elan show               — show installed toolchains"
echo "  uvx lean-lsp-mcp --help — MCP server help"
