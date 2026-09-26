---
# qou-29i6
title: harness.json and harness.config.json assert platform-main behaviour as present-tense fact
status: todo
type: bug
priority: normal
tags:
    - platform
    - docs
created_at: 2026-09-26T10:32:57Z
updated_at: 2026-09-26T10:37:01Z
parent: qou-ty42
---

**Measured 2026-09-26. This is a documentation-integrity bean, and it is the one
most likely to cost a future agent a session.**

## The claim

`harness.json` and `harness.config.json` describe **platform main** in the
present tense, while this repo pins `df28d02`. Both files read as statements
about the running system. Neither is.

Two examples, quoted from the files:

- `harness.json`: *"Omitting it is not a warning — `readDeclaration` THROWS, so
  every call through folioDir() dies, which is every pipeline entry point."*
- `harness.config.json`: *"the platform stopped reading the old name on
  2026-09-18 and it is NOT a fallback — `resolveHarnessConfigPath` in
  folio-assistant's schemas/harness-config.ts reads `harness.config.json` and
  nothing else, so a folio still carrying the old name is UNCONFIGURED rather
  than half-configured."*

## Both are false of the pinned platform

Measured at `df28d02`:

| symbol | occurrences at the pin | at platform main `e53bba80284` |
|---|---|---|
| `readDeclaration` | **0** | 101 files |
| `harness.json` (in `*.ts`) | **0** | — |
| `resolveHarnessConfigPath` | **0** | present |
| `schemas/harness-config.ts` | **does not exist** | exists (under `cat-harness/`) |

And `src/index.ts:94` at the pin reads `folio.config.json`. So a folio carrying
the old name is not "UNCONFIGURED" here — it is **the only configured one**.

## Why this matters more than a stale comment usually does

An agent that reads `harness.config.json` concludes the folio is configured and
that the six wall criteria are the live problem. Measured, the opposite holds:
`folio.config.json` is what configures this repo, and it carries a genuinely
broken `feedbackDir` (`qou-sm2c`) that `harness.config.json`'s own comment
correctly diagnoses — and then fixes in a file nothing reads. **The accurate
diagnosis and the inert location together produce a false all-clear.**

This is the `vbase` failure class one level up: `.folio-assistant-pin` exists so
that every count this repo quotes names its platform, and these two files quote
platform behaviour with no platform named.

## The fix

Cheap and non-behavioural: scope each present-tense assertion to the platform it
is about — "on platform main (not the pinned `df28d02`), `readDeclaration`
throws…". No JSON values change; only `_comment` strings. Under the
ASK-THE-OWNER rule this is exemption 2 (the corpus, i.e. the platform source and
the pin file, decides it) and a reviewer can check it by opening the platform at
the pin.

**Default if nobody acts:** both files keep reading as current, and the next
agent to touch the instance config starts from a false model of which file is
live. `qou-ty42` already carries the true state, but nothing points from these
two files to it.
