---
# qou-i78u
title: 'openalex-paper-search MCP needs OPENALEX_MAILTO (owner chooses contact email)'
status: completed
type: task
created_at: 2026-11-20T18:05:00Z
updated_at: 2026-11-20T18:58:00Z
---

alex-mcp exits at start unless OPENALEX_MAILTO is set. scripts/mcp-lazy.json declares it in requires_env, so `start` refuses with a clear message instead of crashing. OpenAlex asks for a contact email for its polite pool. The owner must choose which address to set and where (session env or a secret); an agent must not pick the owner's private email. Until then, use paper-search-mcp or folio/references/. Split from qou-q261.

## 2026-11-20 done (owner: "use the repo owner's email but pull it dynamically")
PR #8646, merged as 44c50925b1. `env_fallback` resolves OPENALEX_MAILTO from git history when `start` is called; nothing is stored in the repo. Verified: with the variable unset, alex-mcp starts with 2 tools. Real queries are blocked from this sandbox because api.openalex.org is not on the proxy allowlist. That is a network setting and does not affect other environments.
