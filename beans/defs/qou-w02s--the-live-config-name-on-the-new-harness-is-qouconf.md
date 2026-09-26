---
# qou-w02s
title: The live config name on the new harness is qou.config.json, not harness.config.json
status: todo
type: feature
priority: high
tags:
    - platform
    - config
created_at: 2026-09-26T10:31:23Z
updated_at: 2026-09-26T10:35:27Z
parent: qou-ty42
---

**Measured 2026-09-26.** Parent epic `qou-ty42` records the platform-split
migration stopping at `harness.config.json`. Upstream moved again **two days
later**, so the name that file settled on is already retired.

## What platform main says, in its own source

`cat-harness/schemas/harness-config.ts` (platform `main` `e53bba80284`):

```
export const LEGACY_HARNESS_CONFIG = "harness.config.json";
```

with the docstring: *"The retired global name. Kept as a constant so
`check:instance-config` can FIND it, never so a reader can fall back to it."*

The owner's ruling quoted in that same file, 2026-09-20:

> "mv to root at `cat-harness.config.json` as will all instantiated instances
> (not just materialized KGs). `root/` is where instantiation is tracked."

So the live name is **`<name>.config.json` at the instantiation root**. `harness.json`
declares `"name": "qou"`, so for this repo that is **`qou.config.json`** at the
checkout root — which is what the owner said in session on 2026-09-26, before
this was measured: *"Will need qou.config.json if new harness."* Confirmed.

## And `harness.json` itself is EXCISED upstream

Same file: *"`<name>.config.json` is the declaration too **since `harness.json`
was excised**"*. The directory declaration does not live in a separate file on
main — it folds into the instance config. So a bumped qou needs ONE new file and
loses one, rather than gaining a third.

## So qou currently carries three config spellings and none of the live one

| file | status upstream | read at the pin `df28d02`? |
|---|---|---|
| `folio.config.json` | retired 2026-09-18, "not read" | **YES — this is the live one here** |
| `harness.config.json` | `LEGACY_HARNESS_CONFIG`, gated by `check:instance-config` | no |
| `harness.json` | **excised** | no |
| `qou.config.json` | the live name | **ABSENT** |

## Why nothing is broken today

The pin is `df28d02` (2026-09-07), which predates all of it: measured, that
platform has **0** occurrences of `readDeclaration`, **0** of `harness.json`, no
`schemas/harness-config.ts` and no `resolveHarnessConfigPath`. It resolves
`folio.config.json` at `src/index.ts:94`. Platform main has **101** files
referencing `readDeclaration`.

## Cost and blocking

This is **step 5+ of `qou-ty42`** and is BLOCKED on the pin bump, which that
epic records as **"NOT DONE — owner's call"**. Writing `qou.config.json` before
the bump adds a fourth inert spelling. Writing it as part of the bump is a
handful of lines: take `harness.config.json`'s contents, add the `directories`
block from `harness.json`, name it `qou.config.json`.

Do NOT delete `folio.config.json` as part of this — `qou-ty42` says it "must
not be", and at the pin it is the only config actually read.
