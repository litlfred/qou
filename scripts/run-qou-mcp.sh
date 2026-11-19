#!/usr/bin/env bash
# Turnkey launcher for the QOU cat-harness MCP & Content Assistant Server.
#
# Why this wrapper exists:
#   `findContentRepoRoot()` in `folio-assistant/cat-harness-tools/pipeline/repo-root.ts`
#   walks upward from `process.cwd()` looking for `cat-harness.jsonld`, whereas
#   `~/.gemini/config/mcp_config.json` (and Claude Desktop / Cursor MCP configs)
#   only accept `command`, `args`, and `env` (no `cwd` field).
#   This launcher guarantees `cwd` is always the QOU repository root, optionally
#   loads `ANTHROPIC_API_KEY` from the user's local environment files if unset,
#   and execs Bun on `folio-assistant/cat-harness-tools/adapters/mcp-server/server.ts`.

set -euo pipefail

QOU_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$QOU_ROOT"

# Optionally load ANTHROPIC_API_KEY from user-local files only if not already set.
if [ -z "${ANTHROPIC_API_KEY:-}" ]; then
  if [ -f "$HOME/.anthropic_env" ]; then
    # shellcheck disable=SC1091
    . "$HOME/.anthropic_env"
  elif [ -f "$HOME/.config/anthropic/key" ]; then
    ANTHROPIC_API_KEY="$(tr -d '[:space:]' < "$HOME/.config/anthropic/key")"
    export ANTHROPIC_API_KEY
  fi
fi

# Resolve Bun binary.
if [ -n "${BUN_BIN:-}" ] && [ -x "$BUN_BIN" ]; then
  :
elif [ -x "$HOME/.bun/bin/bun" ]; then
  BUN_BIN="$HOME/.bun/bin/bun"
elif command -v bun >/dev/null 2>&1; then
  BUN_BIN="$(command -v bun)"
else
  echo "ERROR: bun executable not found (checked \$BUN_BIN, \$HOME/.bun/bin/bun, and PATH)." >&2
  exit 1
fi

SERVER_TS="$QOU_ROOT/folio-assistant/cat-harness-tools/adapters/mcp-server/server.ts"
if [ ! -f "$SERVER_TS" ]; then
  echo "ERROR: MCP server entrypoint not found at $SERVER_TS" >&2
  exit 1
fi

if [ "$#" -eq 0 ]; then
  set -- --stdio
fi

exec "$BUN_BIN" run "$SERVER_TS" "$@"
