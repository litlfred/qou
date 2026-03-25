#!/usr/bin/env bash
#
# Open the QOU content viewer.
#
# The viewer is served by the MCP assistant (start-assistant.sh).
# This script just opens the browser to the viewer URL.
#
# Usage:
#   ./scripts/start-viewer.sh              # open default URL
#   ./scripts/start-viewer.sh --port 3200  # custom port
#
set -euo pipefail

# Read viewer_port from config (single source of truth), fall back to default
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CONFIG="$REPO_ROOT/lean-mcp.config.json"
CONFIG_PORT=""
if command -v jq &>/dev/null && [ -f "$CONFIG" ]; then
  CONFIG_PORT=$(jq -r '.viewer_port // empty' "$CONFIG" 2>/dev/null)
elif command -v python3 &>/dev/null && [ -f "$CONFIG" ]; then
  CONFIG_PORT=$(python3 -c "import json; print(json.load(open('$CONFIG')).get('viewer_port',''))" 2>/dev/null)
fi
DEFAULT_PORT="${CONFIG_PORT:-3200}"
PORT="${1:-$DEFAULT_PORT}"
[[ "${1:-}" == "--port" ]] && PORT="${2:-$DEFAULT_PORT}"

URL="http://localhost:${PORT}/viewer/"

echo "Opening viewer: $URL"
echo "(Make sure the assistant is running: ./scripts/start-assistant.sh)"

if command -v xdg-open &>/dev/null; then
  xdg-open "$URL"
elif command -v open &>/dev/null; then
  open "$URL"
else
  echo "Open in browser: $URL"
fi
