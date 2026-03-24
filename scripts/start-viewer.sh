#!/usr/bin/env bash
#
# Open the QOU content viewer.
#
# The viewer is served by the MCP assistant (start-folio-assistant.sh).
# This script just opens the browser to the viewer URL.
#
# Usage:
#   ./scripts/start-viewer.sh              # open default URL
#   ./scripts/start-viewer.sh --port 3200  # custom port
#
set -euo pipefail

PORT="${1:-3200}"
[[ "$1" == "--port" ]] && PORT="${2:-3200}"

URL="http://localhost:${PORT}/viewer/"

echo "Opening viewer: $URL"
echo "(Make sure the assistant is running: ./scripts/start-folio-assistant.sh)"

if command -v xdg-open &>/dev/null; then
  xdg-open "$URL"
elif command -v open &>/dev/null; then
  open "$URL"
else
  echo "Open in browser: $URL"
fi
