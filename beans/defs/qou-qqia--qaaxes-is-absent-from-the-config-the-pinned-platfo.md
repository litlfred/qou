---
# qou-qqia
title: qaAxes is absent from the config the pinned platform actually reads
status: completed
type: bug
priority: normal
tags:
    - platform
    - config
    - qa
    - reorg-2026-10-04
created_at: 2026-09-26T10:32:26Z
updated_at: 2026-11-21T12:30:00Z
parent: qou-n4r9
---

**Measured 2026-09-26.**

## The claim

`harness.config.json` adds `"qaAxes": ["archimedean-wall"]`, with a long comment
saying six criteria have been unregistered since the rename. The config the
pinned platform actually reads — `folio.config.json` — has **no `qaAxes` key at
all**. But the consequence at the pin is NOT the one that comment describes.

## What is actually true at the pin, measured

`folioOptionalAxes()` exists at `df28d02`
(`content/pipeline/qa-criteria-registry.ts:2009`) and reads:

```
const cfgPath = join(findContentRepoRoot(), "folio.config.json");
```

— the OLD name, so at the pin it reads the right file and finds no `qaAxes`.

Then: **`archimedean-wall` is not an axis at the pin.** The whole registry
contains exactly one occurrence of the string, and it is part of a criterion
**id** at line 1389, `detangler-archimedean-wall` — not an axis name. The only
axis the pin gates on is `q-usage` (lines 2193, 2264). And
`framework-canonical` / `wall-side-correct` are registered **unconditionally**
at lines 307 / 329 and listed at 2306 / 2307.

So at the pin: the six wall criteria are **registered, not fenced**, and adding
`qaAxes: ["archimedean-wall"]` would be a **no-op**. The fencing (#523) is
post-pin.

## What this means for the two claims in circulation

- `harness.config.json`'s comment — "all six criteria have been unregistered
  since" — describes **platform main**, and is false of what this repo runs. See
  sibling `qou-29i6`, which is about that class of statement generally.
- The key is nonetheless **load-bearing after a bump**: on main the fencing is
  real, so a bumped qou without `qaAxes` loses all six.

## The separate, live question: `q-usage` is OFF

`q-usage` IS an axis at the pin and gates seven criteria plus watcher buckets.
`folio.config.json` has no `qaAxes`, so **`q-usage` is unregistered right now.**
`harness.config.json` deliberately omits it too — *"that is its own decision"* —
so this is not an oversight to fix silently. Whether qou wants the q-usage axis
registered is an owner call and is **not** proposed here; the `q-usage-watcher`
skill exists and `AGENTS.md` routes to it, which is weak evidence the axis was
meant to be on, but the config has never carried it and no measurement here says
what turning it on would report.

## Cost

Adding `qaAxes` to `folio.config.json`: one line, no-op at the pin, correct after
a bump. Deciding `q-usage`: an owner call, unmeasured.


## 2026-11-21 — verified on main and closed (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`.

- The pin now reads `qou.config.json`, which carries `qaAxes` (line 19) and a correction comment (line 41) recording this bean's finding. The title's defect (`qaAxes` absent from the config the platform reads) is gone.
- Still open, and an owner question, not this bean's: whether the `q-usage` axis should be on. The comment at `qou.config.json:41` records it as undecided.
