#!/usr/bin/env bash
# Setup script for Lean 4 + lean-lsp-mcp on ChromeOS/Crostini
#
# Scans lakefile.toml for all dependencies and ensures everything is
# installed and built. Safe to re-run — skips already-installed components.
#
# Installs:
#   1. uv (Python package manager, needed by lean-lsp-mcp)
#   2. elan + pinned Lean toolchain
#   3. ripgrep (for lean_local_search)
#   4. All Lake dependencies (lake update)
#   5. Mathlib cache (lake exe cache get)
#   6. Full build (lake build)
#   7. Verifies lean-lsp-mcp is runnable
#
# Prerequisites: git, curl (assumed installed)
#
# Usage:
#   ./scripts/setup-lean-mcp.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LEAN_DIR="$REPO_ROOT/lean-archive"
TOOLCHAIN_FILE="$LEAN_DIR/lean-toolchain"
LAKEFILE="$LEAN_DIR/lakefile.toml"

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
    echo "▸ Toolchain: $TOOLCHAIN"
    # elan exits non-zero if already installed — suppress that noise
    OUTPUT=$(elan toolchain install "$TOOLCHAIN" 2>&1 || true)
    if echo "$OUTPUT" | grep -q "already installed"; then
        echo "  ✓ Toolchain already installed"
    else
        echo "  ✓ Toolchain installed"
    fi
else
    echo "✗ No lean-toolchain file found at $TOOLCHAIN_FILE"
    exit 1
fi

# ── 4. Verify lean and lake ──────────────────────────────────────
echo "▸ Verifying installation..."
cd "$LEAN_DIR"
echo "  lean: $(lean --version 2>&1 | head -1)"
echo "  lake: $(lake --version 2>&1 | head -1)"

# ── 5. Install ripgrep (for lean_local_search) ───────────────────
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

# ── 6. Scan lakefile.toml and fetch all dependencies ──────────────
echo ""
echo "▸ Scanning $LAKEFILE for dependencies..."
if [ -f "$LAKEFILE" ]; then
    # Extract dependency names and git URLs from lakefile.toml
    echo "  Dependencies found:"
    grep -A2 '^\[\[require\]\]' "$LAKEFILE" | grep -E '(name|git)' | while read line; do
        echo "    $line"
    done
    echo ""

    # lake update fetches all dependencies declared in lakefile.toml
    echo "▸ Running lake update (fetching all dependencies)..."
    if lake update 2>&1 | tail -10; then
        echo "  ✓ All dependencies fetched"
    else
        echo "  ⚠ lake update had issues (continuing anyway)"
    fi
else
    echo "  ⚠ No lakefile.toml found — skipping dependency scan"
fi

# ── 7. Fetch Mathlib cache ───────────────────────────────────────
echo "▸ Fetching Mathlib oleans (this may take a few minutes)..."
if lake exe cache get; then
    echo "  ✓ Cache fetched"
else
    echo "  ⚠ Cache fetch had issues (may already be cached, continuing)"
fi

# ── 8. Build ─────────────────────────────────────────────────────
echo "▸ Running lake build (recommended before first MCP session)..."
if lake build; then
    echo "  ✓ Build succeeded"
else
    echo "  ⚠ Build had errors (MCP server will still work for diagnostics)"
fi

# ── 9. Verify lean-lsp-mcp is runnable ───────────────────────────
echo "▸ Checking lean-lsp-mcp..."
if uvx lean-lsp-mcp --help &>/dev/null; then
    echo "  ✓ lean-lsp-mcp available via uvx"
else
    echo "  ⚠ lean-lsp-mcp test failed (uvx will auto-install it on first use)"
fi

# ── 10. Summary ──────────────────────────────────────────────────
echo ""
echo "=== Setup complete ==="
echo ""
echo "Installed components:"
command -v uv   &>/dev/null && echo "  ✓ uv       $(uv --version 2>&1)"
command -v elan &>/dev/null && echo "  ✓ elan     $(elan --version 2>&1 | head -1)"
command -v lean &>/dev/null && echo "  ✓ lean     $(lean --version 2>&1 | head -1)"
command -v lake &>/dev/null && echo "  ✓ lake     $(lake --version 2>&1 | head -1)"
command -v rg   &>/dev/null && echo "  ✓ ripgrep  $(rg --version 2>&1 | head -1)"
[ -f "$LEAN_DIR/lake-manifest.json" ] && echo "  ✓ lake-manifest.json (deps fetched)"
echo ""
echo "The .mcp.json in the repo root configures lean-lsp-mcp for Claude Code."
echo "Claude Code will auto-start the MCP server on next session."
echo ""
echo "Quick reference:"
echo "  lake build              — rebuild Lean files"
echo "  lake exe cache get      — refresh Mathlib cache"
echo "  lake update             — re-fetch all dependencies"
echo "  lean --version          — check Lean version"
echo "  elan show               — show installed toolchains"
echo "  uvx lean-lsp-mcp --help — MCP server help"
