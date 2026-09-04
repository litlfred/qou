---
# qou-pbql
title: 'PR-body write path wraps any link URL of >= 150 characters in double backticks, breaking the link'
status: completed
type: bug
priority: normal
created_at: 2026-09-04T11:25:00Z
updated_at: 2026-09-04T11:25:00Z
---

## The finding

A link destination of **150 characters or more** in a pull-request body comes
back wrapped in double backticks:

```
[`label`](``https://…very long…``)
```

Markdown link destinations do not process backticks, so the destination becomes
the literal string `` `https://…` `` and **the link is broken** in the rendered
body. 149 characters or fewer is untouched.

**It is not the author's input.** The same body was rewritten twice with plain
single-delimiter markdown and came back mangled both times. Something in the
write path — the GitHub MCP tool or GitHub itself — inserts them. This bean does
not identify which; the discriminator would be a write through a different
client.

## Measured

Binary search over the PR-body write path on `litlfred/qou#6632`, reading the
stored body back after each write. Probe URLs were generated with an assertion
on their length, not hand-counted.

| probe | URL length | result |
|---|---|---|
| T146 – T149 | 146–149 | clean |
| **T150** | **150** | **mangled** |
| T151 | 151 | mangled |

**It is the URL length, not the line length.** A control with a 130-character
label and a 110-character URL is clean.

**Neither candidate feature matters.** The first three instances were all
`.beans/…` paths containing `--`, which made both look causal. Tested in
isolation, both are clean:

| probe | has `--` | dot-dir | URL length | result |
|---|---|---|---|---|
| C | yes | no | 114 | clean |
| D | no | yes (`.beans`) | short | clean |
| F | yes | yes (`.beans`) | 98 | clean |
| I | no | no | 155 | **mangled** |

F is the one that settles it: it carries *both* features and is clean, while I
carries *neither* and is mangled.

## Why it looked like a `.beans` problem for three instances

Bean filenames are `<id>--<slug>.md` and the slugs are long, so a bean's
branch-form blob URL routinely clears 150 while a `scripts/foo.py` URL does not.
The correlation was perfect and causally empty.

## What to do

**Keep blob URLs under 150 characters.** The cheap fix is to address the file by
short commit sha rather than by branch name — a `claude/<theme>-<date>` branch
name is ~43 characters of the budget:

| form | length |
|---|---|
| `…/blob/claude/replay-check-context-drift-2026-09-04/.beans/qou-vtau--post-merge-diff-against-origin-main-is-tautological.md` | **153** — breaks |
| `…/blob/5d370ae/.beans/qou-vtau--post-merge-diff-against-origin-main-is-tautological.md` | **116** — fine |

A sha-form link is also more durable: a branch-form link dies when the branch is
rewritten, and this repo rebase-merges everything.

**This affects the AGENTS.md rule "Always provide GitHub links".** That rule
gives the pattern `https://github.com/litlfred/qou/blob/<branch>/<path-to>/<block>.md`,
which for a long chapter path plus a long branch name silently exceeds the
budget and produces a broken link in the artifact a reviewer reads. Prefer the
sha form for anything long.

## Prior state

The 2026-09-04 check-in Routine for #6586 recorded this as cosmetic and
undetermined: *"I have twice believed I fixed it and it persists, and I have not
determined whether the cause is my input or GitHub's storage — two adjacent
identically-shaped links in that same body differ, only one mangled."* Both
halves are now answered: not the input, and the two adjacent links differed
because one was 153 characters and the other 110.
