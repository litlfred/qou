---
# qou-q261
title: 'GAP: corpus_search unreachable from agent sessions (MCP path stale, tool not on MCP surface)'
status: in-progress
type: bug
created_at: 2026-10-12T19:28:25Z
updated_at: 2026-11-20T17:45:00Z
---

Diagnosed 2026-10-12 (session 0113CzoXn3qJ6dQPNkNBtjAp). (1) folio-assistant/ is not set up at session start, so the paper-assistant MCP server cannot launch (CONNECTION_CLOSED). (2) Even after scripts/setup-folio-assistant.sh, .mcp.json points at folio-assistant/cat-harness/src/index.ts, which the platform layer split (pin c56b73b, 2026-10-11) moved: the entry is now cat-harness-tools/src/index.ts (platform's own .mcp.json) or cat-harness-tools/adapters/mcp-server/server.ts. (3) Neither entry registers corpus_search on its MCP tool list (68 tools, none graph): corpus_search exists only in the server's embedded chat-agent executeTool switch and in cat-harness-tools/adapters/mcp-server/tools/graph.ts. AGENTS.md step 0 'corpus_search (MCP)' is therefore unreachable via MCP. Works when called directly: executeGraphTool('corpus_search', {query}, roots) over folio/ + library/ — 37,143 nodes, 104,529 edges. (4) Query semantics: a 4-word query seeded 0; short phrases ('Bring', 'Bring\'s surface') seed 20. Remedies: environment setup script runs setup-folio-assistant.sh; fix the .mcp.json path; register graph tools on the MCP surface upstream; meanwhile a scripts/corpus-search.ts CLI wrapper.

## 2026-11-20 W11 fix (owner: "figure out why the search didn't work and fix it"); branch claude/paper-assistant-mcp-entry-2026-11-20
Re-measured at platform pin 82b3899:
- (2) is still true and is the direct cause of "Connection closed": `folio-assistant/cat-harness/src/index.ts` does not exist. Fixed. `.mcp.json` now runs `scripts/paper-assistant-mcp.sh`, which execs `cat-harness-tools/src/index.ts --stdio` and prints a one-line diagnostic when the platform is absent or light.
- (3) is RESOLVED upstream. `corpus_search` is on the MCP tools/list, and a tools/call returned hits. The server initializes in 2.8 s.
- (1) remains. The SessionStart hook installs the LIGHT platform, which lacks `@modelcontextprotocol/sdk`, so MCP still cannot start in a fresh session. Mitigation: `scripts/corpus-search.ts`, a CLI over the same `executeGraphTool` and `graphRootsResolved`. Verified on BOTH the light and the full platform. AGENTS.md step 0 now points to it.
- Making MCP itself work at session start would require the full 1.7 GB setup in the hook. That is an owner decision because of cost and timeouts.
Keep this bean open until (1) is decided.

## 2026-11-20 W11: MCP on demand (owner: "MCP should only start up if an agent needs the tools")
Commit d39a9d2034 on PR #8603. Every `.mcp.json` server now runs `scripts/mcp-lazy.py`, a stub that exposes only `start` until an agent calls it. So point (1) above (MCP cannot start at session start) is no longer a session-start problem: the full platform is needed only when paper-assistant is actually started.
Also fixed: paper-search-mcp is pinned to `mcp<2`. Still open: openalex needs OPENALEX_MAILTO (owner choice), and the Claude-client reconnect path is unverified until a new session runs. Keep this bean open until a fresh session confirms that `start` plus RefreshMcpTools works.
