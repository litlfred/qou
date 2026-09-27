---
# qou-sm2c
title: folio.config.json carries a live-broken feedbackDir at the pinned platform
status: completed
type: bug
priority: high
tags:
    - platform
    - config
created_at: 2026-09-26T10:31:54Z
updated_at: 2026-09-27T16:44:44Z
parent: qou-ty42
---

**Measured 2026-09-26. This is the one LIVE defect in the set — it bites at the
pinned platform, not after a bump.**

## The claim

`folio.config.json` — the file the pinned platform actually reads — sets

```json
"feedbackDir": "folio-assistant/feedback"
```

`folio-assistant/` is a **symlink into the platform checkout**
(`/home/user/qou/folio-assistant -> ../folio-assistant`). `feedbackDir` is
resolved against the **repo root**, so this points qou's feedback store *inside
the platform clone* — a directory qou does not own, in a checkout that
`setup-folio-assistant.sh` re-clones.

## Evidence

Platform `df28d02`, `src/index.ts`:

```
 90: let feedbackDir = resolve(repoRoot, ".folio-feedback");
100:     if (config.feedbackDir) feedbackDir = resolve(repoRoot, config.feedbackDir);
122: const feedbackStore = new FeedbackStore(feedbackDir);
```

So line 100 overrides the correct default with the broken value, and
`FeedbackStore` would **create** the directory there on first write.

## The fix already exists — in a file nothing reads

`harness.config.json` carries `"feedbackDir": ".folio-feedback"` and states why:

> CHANGED from `folio-assistant/feedback`, which is the one value that did not
> survive the rename. That path does not exist under either layout, and
> `feedbackDir` is resolved against the FOLIO root, so the old value pointed the
> feedback store inside the platform checkout.

That diagnosis is correct. But `harness.config.json` is not read at the pin (see
sibling `qou-w02s`), so **the fix is inert and the defect is live.**

## Blast radius, and why it has not been noticed

Small, and that is why: qou has **no feedback store on disk today**, so nothing
has written through the bad path yet. `harness.config.json` says the same. The
cost is latent — the first feedback write lands in the platform clone, where a
re-clone or `git clean` loses it, and the platform's own `git status` gains an
untracked directory belonging to another repo.

## Options

1. **Set `feedbackDir` to `.folio-feedback` in `folio.config.json`** (one line).
   Arguably covered by the ASK-THE-OWNER exemption 2 (derived from the corpus:
   the sibling config already decides the value and states the reasoning, and
   `.folio-feedback` is the platform default that `folio_init` writes). Cost: one
   line. Risk: near zero — no data moves, there is nothing on disk to migrate.
2. **Leave it until the pin bump**, when `qou.config.json` carries the right
   value anyway. Cost: nothing now; the latent defect stays live for however long
   the pin does not move, and `qou-ty42` records that as an owner decision with no
   date.
3. **Do nothing.** The default if nobody acts: the bad path stays live and the
   first feedback write goes into the platform clone.

**Recommendation (agent judgement, not a finding): option 1.** It is one line, it
is the value the corpus already chose, and it makes the live config agree with
the migrated one instead of silently disagreeing on the single value that
matters. Option 2 is defensible only if the bump is imminent.

## Already fixed — measured 2026-09-27, and the file is now gone entirely

This bean is `todo`, priority **high**, and asserts a **live** defect:

> `folio.config.json` … sets `"feedbackDir": "folio-assistant/feedback"` …
> points qou's feedback store *inside the platform clone*.

**Measured on `main` `18e1ba553e`, before any change of mine:** that file read
`"feedbackDir": ".folio-feedback"`, and `qou.config.json` carried a
`_feedbackDir_comment` recording the same correction in its own words — *"CHANGED
from `folio-assistant/feedback`, which is the one value that did not survive the
rename."* So the defect was repaired at some point after this bean was written
(2026-09-26T10:31) and nothing updated the bean.

`.folio-feedback` does not exist on disk either, so **no data was ever
implicated** in either direction.

As of `c8b40bec85` the question is moot at a second level: `folio.config.json`
is **deleted**. The surviving config is `qou.config.json`, whose `feedbackDir`
is `.folio-feedback`.

### Why this is completable under §13a

§13a bars completing a bean whose subject is an **open conjecture**. This is a
`type: bug` about a config string: no conjecture, no conditional class, no
epistemic tier. Its whole task was mechanical and the mechanism is gone.

### Why it mattered while it was wrong

A high-priority bug bean advertising a fixed defect is not inert — it is a
standing invitation to spend a session on nothing, and it was cited as the
*urgency* argument for the `folio.config.json` deletion in the 2026-09-27
blocker-options doc. The argument was spent; the deletion turned out to be
justified on different grounds (nothing reads the file, per the pinned
platform's own source), and separately to be *riskier* than this bean implied,
because the file was the only carrier of a correct `simulators.dir` and of an
owner ruling. Both are recorded on `qou-8321`.

**Completing** rather than scrapping: the bean was a correct finding when
written, and its body is the record of how the `feedbackDir` value was
reasoned about.
