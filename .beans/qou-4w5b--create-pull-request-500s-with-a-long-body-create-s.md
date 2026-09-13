---
# qou-4w5b
title: create_pull_request 500s with a long body; create-stub-then-update is the workaround
status: todo
type: task
priority: normal
created_at: 2026-09-13T09:09:13Z
updated_at: 2026-09-13T09:09:45Z
---

## Measured 2026-09-13, opening #7281

`mcp__github__create_pull_request` against `litlfred/qou` returned a server error
**three times in a row** when called with a long `body`, and succeeded instantly
with a short one. Same head branch, same title, same base, same session, within
about two minutes.

| attempt | body | result |
|---|---|---|
| 1 | ~4.4 KB (tables, em-dashes, blob URLs, emoji) | `500` |
| 2 | ~4.2 KB (same, blob URLs stripped) | `502 Server Error` |
| 3 | ~3.9 KB (same, unicode arrows -> ASCII) | `500` |
| 4 | **95 bytes**, one plain sentence | **created — #7281** |
| 5 | `update_pull_request` with attempt-3's body verbatim | **applied** |

`list_pull_requests` after each failure returned `[]`, so the failures were
genuine no-ops, not partial successes — unlike the rule-8a undraft case, where a
rate-limit error can accompany a title/body write that DID land. Check anyway
before re-sending; do not assume from this row.

## The workaround, which is solid whatever the cause

**Create with a one-line stub body, then `update_pull_request` with the real
body.** Attempt 5 proves the update path takes content the create path refused,
so nothing is lost — the PR ends up with the full body either way, one extra
call. This is NOT close-and-reopen and does not touch the GraphQL limiter.

## 🛑 What is NOT established — do not quote this as "long bodies fail"

**Size and content are confounded and this did not separate them.** Attempts
1-3 share most of their prose; attempt 4 is 95 bytes of *entirely different*
text. So "the create path chokes above some body size" and "a specific
character or construct present in all three and absent from the fourth" are
both consistent with every observation here. I did not bisect.

What would separate them, if it recurs and is worth the calls: create a throwaway
PR with 4 KB of a single repeated ASCII character. Fails -> size. Succeeds ->
content, and then bisect attempt 3.

Also unestablished: whether this is GitHub, the MCP github server, or the agent
proxy. `curl "$HTTPS_PROXY/__agentproxy/status"` showed recent relay failures
only for `lakecache.blob.core.windows.net` (403 CONNECT, the Lean cache), none
for `api.github.com` — which is evidence against the proxy but not proof, since
a relayed 500 need not register as a relay failure.

## Why it is worth a bean

The ALWAYS-PR rule puts a `create_pull_request` call at the start of every work
tranche, and this repo's PR bodies are long by convention — the four-part frame
AGENTS.md asks for does not fit in 95 bytes. So an agent hitting this meets it at
the moment it is least equipped to diagnose it, and the obvious readings are both
wrong: it is not rate limiting (rule 8a is about the *undraft* GraphQL path and
says every REST path keeps working — create is REST and this IS a create), and
retrying verbatim does not clear it (three attempts, ~2 min apart).
