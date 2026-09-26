---
# qou-f50c
title: Nothing at the pinned platform reads config.simulators
status: todo
type: task
priority: normal
tags:
    - simulators
    - platform
created_at: 2026-09-26T10:39:57Z
updated_at: 2026-09-26T10:48:09Z
parent: qou-p7z5
---

**Measured 2026-09-26.** `folio.config.json` and `harness.config.json` both carry
a `simulators` block (`dir`, `pyodideCache`). At the pinned platform `df28d02`,
grepping `src/` and `schemas/` for `simulators` returns exactly **one** hit, and
it is a **comment** in `src/tools/readme-sync.ts:4`. Nothing reads
`config.simulators`.

## What DOES consume the simulators directory

`content/pipeline/readme-sections.ts` — the `folio:simulators` README section,
described by the platform's own `--list` as *"Interactive simulators, from the
folio's configured simulators directory."* That section is live and renders qou's
11 pages (re-synced 2026-09-26).

So the directory is consumed; the **config key** is not, at this pin.

## Why this bean exists

The owner's hypothesis this session was that simulator pages are why the harness
declaration matters. That is the right instinct and the measurement refines it:
at the pin the simulators are reached by a pipeline that walks the directory, not
by anything resolving the declared path. `pyodideCache: true` in particular is
declared and unread here.

Whether platform **main** reads these keys is **not measured** — only the pin
was. That is the thing to check before the pin bump (`qou-ty42` step 5), because
if main does read them, the values move from decorative to load-bearing in the
same commit that bumps.

## Not claimed

No config change is proposed. The keys are harmless where they are, and removing
a key that main may read would be the wrong direction.
