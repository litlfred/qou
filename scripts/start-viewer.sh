#!/usr/bin/env bash
#
# Start the QOU content viewer (HTML renderer).
#
# Usage:
#   ./scripts/start-viewer.sh                  # default paper, port 3200
#   ./scripts/start-viewer.sh --open           # also open browser
#   ./scripts/start-viewer.sh --port 8080      # custom port
#   ./scripts/start-viewer.sh --paper my-paper # different paper
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Ensure bun is available
if ! command -v bun &>/dev/null; then
  echo "[start-viewer] bun not found. Installing..." >&2
  curl -fsSL https://bun.sh/install | bash
  export PATH="$HOME/.bun/bin:$PATH"
fi

# Ensure viewer deps are installed
if [ ! -d "$REPO_ROOT/viewer/node_modules" ]; then
  echo "[start-viewer] Installing viewer dependencies..." >&2
  cd "$REPO_ROOT/viewer" && bun install 2>&1 >&2
fi

cd "$REPO_ROOT"
exec bun run viewer/serve.ts "$@"
