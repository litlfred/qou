#!/usr/bin/env bash
#
# Start the QOU Paper Writing Assistant MCP server.
#
# Usage:
#   ./scripts/start-assistant.sh              # stdio mode (for .mcp.json)
#   ./scripts/start-assistant.sh --http       # HTTP mode (for remote/Docker)
#   ./scripts/start-assistant.sh --install    # install deps first, then start
#   ./scripts/start-assistant.sh --check      # just check deps, don't start
#
# Works on: ChromeOS/Crostini, macOS, Ubuntu, any POSIX system with bun.
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
MCP_DIR="$REPO_ROOT/scripts/mcp-server"

MODE="--stdio"
DO_INSTALL=false
CHECK_ONLY=false

for arg in "$@"; do
  case "$arg" in
    --http)    MODE="--http" ;;
    --stdio)   MODE="--stdio" ;;
    --install) DO_INSTALL=true ;;
    --check)   CHECK_ONLY=true ;;
    --help|-h)
      echo "Usage: $0 [--stdio|--http] [--install] [--check]"
      echo ""
      echo "  --stdio    Start in stdio mode (default, for .mcp.json)"
      echo "  --http     Start in HTTP mode (for remote/Docker, port 8080)"
      echo "  --install  Run full dependency install before starting"
      echo "  --check    Just check dependencies, don't start the server"
      exit 0
      ;;
  esac
done

# ── Ensure bun is available ──────────────────────────────────────

if ! command -v bun &>/dev/null; then
  echo "[start-assistant] bun not found. Installing..." >&2
  curl -fsSL https://bun.sh/install | bash
  export PATH="$HOME/.bun/bin:$PATH"
fi

# ── Full install if requested ────────────────────────────────────

if $DO_INSTALL; then
  echo "[start-assistant] Running full install..." >&2
  bash "$MCP_DIR/install.sh"
fi

# ── Ensure MCP server node_modules exist ─────────────────────────

if [ ! -d "$MCP_DIR/node_modules" ]; then
  echo "[start-assistant] Installing MCP server dependencies..." >&2
  cd "$MCP_DIR" && bun install 2>&1 >&2
fi

# ── Ensure content pipeline node_modules exist ───────────────────

if [ -d "$REPO_ROOT/content" ] && [ ! -d "$REPO_ROOT/content/node_modules" ]; then
  echo "[start-assistant] Installing content pipeline dependencies..." >&2
  cd "$REPO_ROOT/content" && bun install 2>&1 >&2
fi

# ── Check-only mode ─────────────────────────────────────────────

if $CHECK_ONLY; then
  cd "$MCP_DIR"
  exec bun run server.ts --check-deps
fi

# ── Start server ─────────────────────────────────────────────────

cd "$MCP_DIR"
exec bun run server.ts "$MODE"
