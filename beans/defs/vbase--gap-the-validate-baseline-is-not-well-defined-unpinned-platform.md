---
# vbase
title: 'GAP: the validate baseline is not well-defined — folio-assistant is unpinned'
status: completed
type: task
priority: high
tags: [infra, qa, verification]
created_at: 2026-08-08T14:00:00Z
updated_at: 2026-08-08T14:00:00Z
---

`bun run scripts/run-validate.ts content/<paper>` is the repo's primary
content-verification gate, and **its result is not reproducible across
environments.** Two agents verifying the *same corpus commit* legitimately
disagreed today.

## Measured

Both on clean `origin/main` @ `455013fcf5`, same machine, same session:

| environment | `folio-assistant` clone | HEAD | result |
|---|---|---|---|
| main checkout | `/home/user/folio-assistant` | `e1030e8` (platform #70) | **`✓ Valid — 10 issue(s)`** |
| agent worktrees | `.claude/worktrees/folio-assistant` | `e3c2d6b` (platform #73) | **`✓ Valid — 29 issue(s)`** |

Neither is wrong. The corpus is identical; the **checkers** differ by three
platform PRs.

## Cause

`content/pipeline/` and the Zod schemas live in the separate
`litlfred/folio-assistant` repo (the `miga` migration). `folio-assistant/` in
this tree is a **symlink** to a sibling clone created by
[`scripts/setup-folio-assistant.sh`](../scripts/setup-folio-assistant.sh),
which clones the **default branch with no ref, tag or commit pin**:

```sh
CLONE_DIR="${FOLIO_ASSISTANT_DIR:-$ROOT/../folio-assistant}"
```

Two consequences:

1. **Unpinned in time.** Whoever runs setup later gets newer checkers, hence a
   different issue count, with no signal that the gate moved.
2. **Path-relative.** `$ROOT/../folio-assistant` resolves *relative to the
   checkout*, so a git worktree at `.claude/worktrees/agent-X` clones its own
   copy at `.claude/worktrees/folio-assistant` rather than reusing the main
   one — which is exactly how the two versions above arose.

## Why it matters more than a count

"Validate is unchanged from baseline" is the standard verification sentence in
this repo's PR bodies, and it is the *content-side* half of the AGENTS.md §rule-10
verification gate that stands in for CI (CI being `workflow_dispatch`-only). If
the baseline silently depends on an external repo's default branch, then:

- a PR can read "baseline unchanged" in one environment and "+19 issues" in
  another, with neither author at fault;
- a real regression can hide inside a platform-version delta;
- worse, a *fixed* issue can be misread as a regression, or vice versa.

This session put `✓ Valid — 10 issue(s)` into four agent briefings as the
baseline to hold. Three agents measured 29 and correctly flagged the number as
stale. It was not stale — it was **measured against a different platform**, and
the briefing never said which.

## Dispositions

1. **Pin the platform.** Record a `folio-assistant` commit (a file like
   `.folio-assistant-pin`, or a `[folio]` stanza in `folio.config.json`), have
   `setup-folio-assistant.sh` check it out, and fail loudly on drift. This is
   the real fix.
2. **Make the version visible.** Have `run-validate.ts` print the resolved
   platform SHA in its header, so every quoted baseline carries its own
   provenance. Cheap, and it would have made today's disagreement self-resolving.
3. **Share one clone across worktrees** (or set `FOLIO_ASSISTANT_DIR` to an
   absolute path in agent setup) so isolation does not fork the toolchain.

(1) and (2) are independent and both worth doing; (2) alone would have prevented
the confusion even without (1).

## Verification note for anyone quoting a baseline meanwhile

State the platform SHA alongside the count:
`git -C "$(readlink -f folio-assistant)" rev-parse --short HEAD`.
A bare issue count is not a claim anyone else can check.

---

## RESOLVED 2026-08-08 — the platform is pinned

`.folio-assistant-pin` now carries the platform SHA, and
`scripts/setup-folio-assistant.sh` defaults its `REF` to that file instead of
`main`. `FOLIO_ASSISTANT_REF` still overrides for testing. Bumping the platform
is a reviewable one-line commit; the pin file asks for before/after issue counts
in the bump message, so a checker behaviour change gets seen rather than absorbed.

Pinned at `e1030e83b6be3605e2a08b5e19a35e20c6d6d2a7`.

**A third variance axis, found while doing this.** The bean framed the problem as
platform-only. It is not. Against the *same* platform `e1030e8`, the corpus moved
too: `run-validate` reported **10** issues earlier in the session and **4** now,
because #4786 ("fix every cross-reference warning") landed in between. So a bare
quoted count is under-determined by *both* inputs. The pin fixes one axis; the
other is fixed by quoting the corpus commit alongside the number, which
`run-validate` does not print. Small follow-up if it recurs.

