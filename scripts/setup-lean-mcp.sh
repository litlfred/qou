#!/usr/bin/env bash
# Setup script for Lean 4 MCP server on ChromeOS/Crostini (Debian/Ubuntu)
#
# What this does:
#   1. Installs elan (Lean version manager) if missing
#   2. Installs the pinned Lean toolchain from lean-toolchain
#   3. Builds Mathlib cache (lake exe cache get)
#   4. Verifies lake build works
#
# Usage:
#   chmod +x scripts/setup-lean-mcp.sh
#   ./scripts/setup-lean-mcp.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LEAN_DIR="$REPO_ROOT/lean"
TOOLCHAIN_FILE="$LEAN_DIR/lean-toolchain"

echo "=== Lean 4 MCP Setup for ChromeOS/Crostini ==="
echo ""

# ── 1. Prerequisites ──────────────────────────────────────────────
echo "▸ Checking prerequisites..."

# curl or wget needed for elan installer
if ! command -v curl &>/dev/null && ! command -v wget &>/dev/null; then
    echo "  Installing curl..."
    sudo apt-get update -qq && sudo apt-get install -y -qq curl
fi

# git is required by lake
if ! command -v git &>/dev/null; then
    echo "  Installing git..."
    sudo apt-get update -qq && sudo apt-get install -y -qq git
fi

# ── 2. Install elan ───────────────────────────────────────────────
if command -v elan &>/dev/null; then
    echo "▸ elan already installed: $(elan --version)"
else
    echo "▸ Installing elan (Lean version manager)..."
    curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh -s -- -y --default-toolchain none
    # Source elan env for this session
    export PATH="$HOME/.elan/bin:$PATH"
    echo "  ✓ elan installed: $(elan --version)"
fi

# Ensure elan is on PATH
export PATH="$HOME/.elan/bin:$PATH"

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

# ── 4. Verify lean and lake are available ─────────────────────────
echo "▸ Verifying installation..."
cd "$LEAN_DIR"
echo "  lean: $(lean --version 2>&1 | head -1)"
echo "  lake: $(lake --version 2>&1 | head -1)"

# ── 5. Fetch Mathlib cache ────────────────────────────────────────
echo "▸ Fetching Mathlib oleans (this may take a few minutes)..."
lake exe cache get 2>&1 | tail -3
echo "  ✓ Cache fetched"

# ── 6. Build ──────────────────────────────────────────────────────
echo "▸ Running lake build (first build may take a while)..."
if lake build 2>&1 | tail -5; then
    echo "  ✓ Build succeeded"
else
    echo "  ⚠ Build had errors (this is OK — the MCP server will still work)"
fi

echo ""
echo "=== Setup complete ==="
echo ""
echo "Lean is ready. To use with Claude Code:"
echo "  1. The .mcp.json in the repo root configures a local Lean MCP server"
echo "  2. Claude Code will auto-detect it on session start"
echo ""
echo "Quick reference:"
echo "  lake build          — build all Lean files"
echo "  lake exe cache get  — refresh Mathlib cache"
echo "  lean --version      — check Lean version"
echo "  elan show           — show installed toolchains"
