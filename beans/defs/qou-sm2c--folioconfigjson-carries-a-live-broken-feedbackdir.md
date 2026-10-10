---
# qou-sm2c
title: folio.config.json carries a live-broken feedbackDir at the pinned platform
status: todo
type: bug
priority: high
tags:
    - platform
    - config
    - reorg-2026-10-04
created_at: 2026-09-26T10:31:54Z
updated_at: 2026-10-04T15:14:36Z
parent: qou-n4r9
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
