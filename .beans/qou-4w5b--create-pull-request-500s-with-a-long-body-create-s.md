---
# qou-4w5b
title: GitHub PR create AND update both 5xx intermittently on long bodies — retry; the create-vs-update split was wrong
status: todo
type: task
priority: normal
created_at: 2026-09-13T09:09:13Z
updated_at: 2026-09-13T10:32:20Z
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


## 🛑 CORRECTED within the hour — the create-vs-update split is WRONG, and it was mine

The section above says *"the update path takes content the create path refused"*
and builds the whole workaround on that. **`update_pull_request` then failed the
same way**, on the very next long body I sent it:

    PATCH /repos/litlfred/qou/pulls/7281 -> 502 Server Error

Confirmed a genuine no-op by re-reading the PR — the body was unchanged. Then it
**succeeded on a plain retry** with a body of the same order.

Full series, both endpoints, one session, ~10 minutes:

| # | call | body | result |
|---|---|---|---|
| 1 | create | ~4.4 KB | 500 |
| 2 | create | ~4.2 KB | 502 |
| 3 | create | ~3.9 KB | 500 |
| 4 | create | **95 B** | **ok** |
| 5 | update | ~4.2 KB | **ok** |
| 6 | update | ~5.5 KB | 502 |
| 7 | update | ~5.4 KB | **ok** |

### What the corrected series actually supports

**It is INTERMITTENT, and the endpoint is not the variable.** Rows 6 and 7 are the
same endpoint with near-identical bodies, minutes apart, one failing and one not.
Any rule of the form "endpoint X fails / endpoint Y works" is refuted by rows 5-7
alone.

**Size is not a clean threshold either.** Row 3 failed at 3.9 KB while row 5
succeeded at 4.2 KB, so there is no single byte count separating pass from fail. A
weak size *correlation* survives — every failure is above 3.9 KB and the only
sub-KB call passed — but that is one data point at the small end, and with
intermittency in play it may be luck rather than mechanism.

**So I have not established a cause, and the earlier entry claimed a pattern from
two points.** Rows 4 and 5 were read as "create is broken, update is fine". Row 6
is the same call as row 5 and it failed. Two points are a line through anything.

### The workaround that survives the correction

**Retry.** It is intermittent, so the same call spaced out does land — row 7 is row
6 retried. Creating with a stub body still helps, because it gets the PR *open*
(the ALWAYS-PR artifact) on a call small enough to have never failed here, after
which the body is a retryable edit rather than a blocker.

**Always re-read before re-sending.** Every failure here was a true no-op, verified
by `list_pull_requests` / `pull_request_read`. That is NOT guaranteed — AGENTS.md
rule 8a records a sibling measuring `update_pull_request` returning an error while
the title and body writes **landed anyway**. Checking is one call and prevents a
double write.

### Still not established

Whether this is GitHub, the MCP github server, or the agent proxy.
`curl "$HTTPS_PROXY/__agentproxy/status"` showed recent relay failures only for
`lakecache.blob.core.windows.net` (403 CONNECT, the Lean cache) and none for
`api.github.com` — evidence against the proxy, not proof, since a relayed 5xx need
not register as a relay failure. The bisect proposed above (4 KB of one repeated
ASCII character) is now much weaker as a test: against an intermittent fault a
single pass or fail decides nothing, and it would need repetition to say anything.


---

## INDEPENDENT CONFIRMATION 2026-09-13, opening #7280 (session 01QdzbDV, ~09:0x)

Same defect, same hour, different session and different PR — reached before
seeing this bean, so this is a genuine second observation rather than an echo.
It **agrees with every conclusion above**, including the one the title
corrects: update 5xxs on a long body too.

| attempt | call | body | result |
|---|---|---|---|
| 1 | `create_pull_request` | ~6 KB, em-dash in TITLE, `draft: false` | `500` |
| 2 | `create_pull_request` | same | `500` |
| 3 | `create_pull_request` | **46 bytes**, em-dash in title, `draft: false` | `500` |
| 4 | `create_pull_request` | 13 bytes, **ASCII title**, no `draft` field | **created — #7280** |
| 5 | `update_pull_request` | ~6 KB | `500` |
| 6 | `update_pull_request` | ~6 KB, retried verbatim | `500` |
| 7 | `update_pull_request` | **~1.5 KB** | **applied** |
| 8 | `add_issue_comment` | ~5 KB, same prose that 5xx'd as a body | **posted** |

**What this adds to the rows above.**

* **A bracketing pair on ONE PR.** #7280 accepted ~1.5 KB and rejected ~6 KB
  minutes apart, so the size dependence is visible without varying the PR,
  the branch or the session. That is the cleanest form of the observation
  here.
* **`add_issue_comment` is unaffected.** ~5 KB of the *same prose* that 5xx'd
  as a PR body posted as a comment first try, and four more comments of
  similar size followed. So the failure is specific to the pull-request body
  field, not to the content or to the client.
* **`request_copilot_review` also 5xx'd twice, then succeeded** on the third
  try with no change of any kind. That endpoint carries no body at all, which
  is evidence the 5xx is **partly time-varying** and not purely a function of
  body size — a caveat neither of our runs can separate.

**One thing I could NOT isolate, recorded so nobody quotes a cause.** My
attempt 3 changed *two* things at once against attempt 4 — the em-dash in the
title and the explicit `draft` field — so my create-side failures do not
discriminate between them, and a 46-byte body failing while a 13-byte body
succeeded is more likely the time-variation above than a size effect. The
rows above are the better create-side evidence; mine is the better
update-side and comment-side evidence.

**Same verification discipline, independently.** `list_pull_requests` after
each create failure returned `[]`, and `pull_request_read` after the first
update failure showed the body unchanged — so all of mine were genuine
no-ops too. Two sessions, same check, same answer.

**Practical upshot, unchanged:** open with a short body, fill it in with a
second call, and put anything long in a comment.
