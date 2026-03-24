#!/usr/bin/env bash
#
# SessionStart hook: start the assistant server (if not running) and open browser.
#
# Checks if the MCP assistant HTTP server is already up on VIEWER_PORT (default 3200).
# If not, starts it in the background. Then opens the assistant landing page.
#
set -uo pipefail

PORT="${VIEWER_PORT:-3200}"
URL="http://localhost:${PORT}/assistant/"

# ── Check if server is already running ───────────────────────────
if curl -sf --max-time 2 "http://localhost:${PORT}/health" &>/dev/null; then
  echo '{"assistant_server": "running", "url": "'"$URL"'"}'
else
  echo '{"assistant_server": "not_running", "url": "'"$URL"'", "message": "Start with: ./scripts/start-folio-assistant.sh"}'
fi

# ── Open browser ─────────────────────────────────────────────────
if command -v xdg-open &>/dev/null; then
  nohup xdg-open "$URL" &>/dev/null &
elif command -v open &>/dev/null; then
  open "$URL"
fi

exit 0
