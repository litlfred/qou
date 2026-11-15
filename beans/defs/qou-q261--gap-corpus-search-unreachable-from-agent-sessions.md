---
# qou-q261
title: 'GAP: corpus_search unreachable from agent sessions (MCP path stale, tool not on MCP surface)'
status: todo
type: bug
created_at: 2026-10-12T19:28:25Z
updated_at: 2026-10-12T19:28:25Z
---

Diagnosed 2026-10-12 (session 0113CzoXn3qJ6dQPNkNBtjAp). (1) folio-assistant/ is not set up at session start, so the paper-assistant MCP server cannot launch (CONNECTION_CLOSED). (2) Even after scripts/setup-folio-assistant.sh, .mcp.json points at folio-assistant/cat-harness/src/index.ts, which the platform layer split (pin c56b73b, 2026-10-11) moved: the entry is now cat-harness-tools/src/index.ts (platform's own .mcp.json) or cat-harness-tools/adapters/mcp-server/server.ts. (3) Neither entry registers corpus_search on its MCP tool list (68 tools, none graph): corpus_search exists only in the server's embedded chat-agent executeTool switch and in cat-harness-tools/adapters/mcp-server/tools/graph.ts. AGENTS.md step 0 'corpus_search (MCP)' is therefore unreachable via MCP. Works when called directly: executeGraphTool('corpus_search', {query}, roots) over folio/ + library/ — 37,143 nodes, 104,529 edges. (4) Query semantics: a 4-word query seeded 0; short phrases ('Bring', 'Bring\'s surface') seed 20. Remedies: environment setup script runs setup-folio-assistant.sh; fix the .mcp.json path; register graph tools on the MCP surface upstream; meanwhile a scripts/corpus-search.ts CLI wrapper.
