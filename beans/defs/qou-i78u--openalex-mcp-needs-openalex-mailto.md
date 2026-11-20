---
# qou-i78u
title: 'openalex-paper-search MCP needs OPENALEX_MAILTO (owner chooses contact email)'
status: todo
type: task
created_at: 2026-11-20T18:05:00Z
updated_at: 2026-11-20T18:05:00Z
---

alex-mcp exits at start unless OPENALEX_MAILTO is set. scripts/mcp-lazy.json declares it in requires_env, so `start` refuses with a clear message instead of crashing. OpenAlex asks for a contact email for its polite pool. The owner must choose which address to set and where (session env or a secret); an agent must not pick the owner's private email. Until then, use paper-search-mcp or folio/references/. Split from qou-q261.
