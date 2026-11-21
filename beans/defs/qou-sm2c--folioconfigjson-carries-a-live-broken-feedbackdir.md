---
# qou-sm2c
title: folio.config.json carries a live-broken feedbackDir at the pinned platform
status: completed
type: bug
priority: high
tags:
    - platform
    - config
    - reorg-2026-10-04
created_at: 2026-09-26T10:31:54Z
updated_at: 2026-11-21T12:30:00Z
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

## Resolution recorded 2026-11-15 (`Q-10V9-3 = 1`)

Option 1 and Option 2 have both landed on `main`:

1. Commit `dad33d9790184b9a5c4bc1f7d9c63ba318c8f145` (`qou-yf1y: qou.json + qou.config.json, and the feedbackDir defect that was live at the pin`) changed `"feedbackDir"` from `"folio-assistant/feedback"` to `".folio-feedback"` in `folio.config.json` (Option 1) and renamed `harness.config.json` to `qou.config.json` (which also carries `"feedbackDir": ".folio-feedback"`).
2. Commit `5369ef849cdafec3ffb960d7fee999d6047c986f` (`S1: bump the platform pin to folio-assistant main and declare qou's stack`) subsequently bumped `.folio-assistant-pin` past `26c5d37` so the platform reads `qou.config.json` (`"feedbackDir": ".folio-feedback"`) directly and removed the retired `folio.config.json`.
3. Verified on `main` (`b8a698e518f74a1c7fd4d053438c71042ec323a5`): `qou.config.json` sets `"feedbackDir": ".folio-feedback"` and no `folio.config.json` or `harness.config.json` remains. Kept `status: in-progress` per owner rule (no unilateral bean closure).


## 2026-11-21 — verified on main and closed (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`.

- `folio.config.json`, `harness.config.json` and `harness.json` are all absent. `qou.config.json:23` sets `"feedbackDir": ".folio-feedback"`, and the pin reads `qou.config.json`. The defect in the title is gone.
