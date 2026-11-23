#!/usr/bin/env bash
# Launcher for the `paper-assistant` MCP server named in .mcp.json.
#
# Why a launcher instead of a bare `bun run <entry>` (2026-11-20):
#
# 1. The entry point moved. .mcp.json named
#    `folio-assistant/cat-harness/src/index.ts`. The platform's server code
#    moved to cat-harness-tools (bean 8lcl, pin bump 2026-10-30), and that file
#    does not exist at the pinned platform 82b3899. Every session since then
#    reported "paper-assistant: Connection closed": the process exits at once
#    on a missing file. That exit took out `corpus_search`, step 0 of the
#    corpus-grep checklist in AGENTS.md. The platform's own package.json
#    names the entry as `start:stdio`: `bun run cat-harness-tools/src/index.ts --stdio`.
#
# 2. The light platform cannot run it. The SessionStart hook installs
#    scripts/mount-platform-lite.sh, which is enough for beans but has no
#    @modelcontextprotocol/sdk, so even the right entry dies with "Cannot find
#    module". Only scripts/setup-folio-assistant.sh (full platform) can serve
#    MCP. Then reconnect the server (/mcp) or start a new session.
#
# This script turns both failures into a one-line diagnostic on stderr,
# instead of a silent "Connection closed".
set -u
ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$ROOT" || exit 1
ENTRY=folio-assistant/cat-harness-tools/src/index.ts
if [ ! -f "$ENTRY" ]; then
  echo "paper-assistant-mcp: $ENTRY not found: the platform is not installed or has moved. Run scripts/setup-folio-assistant.sh." >&2
  exit 1
fi
if ! (cd folio-assistant/cat-harness-tools/src && bun -e 'await import("@modelcontextprotocol/sdk/server/mcp.js")') >/dev/null 2>&1; then
  echo "paper-assistant-mcp: @modelcontextprotocol/sdk does not resolve from the platform at $(readlink -f folio-assistant). That is the light platform (beans only). Run scripts/setup-folio-assistant.sh, then reconnect the server." >&2
  exit 1
fi
exec bun run "$ENTRY" --stdio --repo "$ROOT"
