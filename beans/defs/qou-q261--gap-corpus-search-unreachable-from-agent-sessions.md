---
# qou-q261
title: 'GAP: corpus_search unreachable from agent sessions (MCP path stale, tool not on MCP surface)'
status: in-progress
type: bug
priority: normal
created_at: 2026-10-12T19:28:25Z
updated_at: 2026-10-12T20:04:38Z
---

Diagnosed 2026-10-12 (session 0113CzoXn3qJ6dQPNkNBtjAp). (1) folio-assistant/ is not set up at session start, so the paper-assistant MCP server cannot launch (CONNECTION_CLOSED). (2) Even after scripts/setup-folio-assistant.sh, .mcp.json points at folio-assistant/cat-harness/src/index.ts, which the platform layer split (pin c56b73b, 2026-10-11) moved: the entry is now cat-harness-tools/src/index.ts (platform's own .mcp.json) or cat-harness-tools/adapters/mcp-server/server.ts. (3) Neither entry registers corpus_search on its MCP tool list (68 tools, none graph): corpus_search exists only in the server's embedded chat-agent executeTool switch and in cat-harness-tools/adapters/mcp-server/tools/graph.ts. AGENTS.md step 0 'corpus_search (MCP)' is therefore unreachable via MCP. Works when called directly: executeGraphTool('corpus_search', {query}, roots) over folio/ + library/ — 37,143 nodes, 104,529 edges. (4) Query semantics: a 4-word query seeded 0; short phrases ('Bring', 'Bring\'s surface') seed 20. Remedies: environment setup script runs setup-folio-assistant.sh; fix the .mcp.json path; register graph tools on the MCP surface upstream; meanwhile a scripts/corpus-search.ts CLI wrapper.

2026-10-12 (session 0113CzoXn3qJ6dQPNkNBtjAp), remedies 2-4. Tracking issue litlfred/qou#7762, PR litlfred/qou#7763.

**Remedy 3 (done, works now).** Added scripts/corpus-search.ts, a CLI wrapper. It calls the same executeGraphTool handler over the same roots as the server: the declared folio plus every declared library, else folio/ and library/. Measured: 'Bring' gives 20 seeds and 68 hits. 'Temperley-Lieb' with --direction in and --search-text gives 20 seeds (11 authored, 9 ingested). The 5-word query 'Bring surface binding energy closure' gives noSeeds. If folio-assistant/ is missing, it exits 3 and names scripts/setup-folio-assistant.sh. AGENTS.md step 0 now names the CLI as the fallback.

**Remedy 2 (done, partial until the pin moves).** .mcp.json now points at folio-assistant/cat-harness-tools/src/index.ts. Over stdio it starts and lists 68 tools, but still without corpus_search at pin c56b73b.

**Remedy 4 (platform PRs, draft).** litlfred/cat-harness#186 adds four Tool nodes in tools/mcp.ts. litlfred/cat-harness-tools#177 adds src/tools/graph.ts (registerGraphTools) and four tests. With both applied, the stdio server lists the four graph tools, and corpus_search 'Bring' gives 20 seeds and 68 hits.

**OPEN, for the owner:** merge both platform PRs, re-pin the folio-assistant index, then bump qou's .folio-assistant-pin, build.yml and qou.config.json. Until then, use the CLI.
