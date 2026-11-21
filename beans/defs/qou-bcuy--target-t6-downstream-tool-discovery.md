---
# qou-bcuy
title: '[TARGET T6] Downstream Tool discovery'
status: todo
type: feature
priority: normal
tags:
    - migration
    - target
    - upstream-fa
created_at: 2026-10-04T16:35:40Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-k3er
---

From the TARGET migration analysis (2026-10-04), story T6. Full report: docs/audits/2026-10-04-workplan-and-migration/TARGET_report.md.

T6 — Downstream Tool discovery. Size M. Target: cat-harness. - Work: make `discoverTools` walk the folio root and its dependencies. - Done when qou's Tools appear in `check:tools` run from qou.

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.


## Evidence 2026-10-04: kg-validate is a concrete instance
From qou with platform 26c5d37: `bun run folio-assistant/cat-harness/scripts/kg-validate.ts library/0110001v3/structure.json` → "could not determine: no declared directory owns this path". `owningInstanceRoot` iterates `instanceRootsIn(checkoutRootFor(fallback))`, where fallback is the script's own instance, so the downstream checkout's `qou.json` is never read. This blocks T2's done-when (qou-4r5m).


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- Not started. This story is owner-gated (AGENTS.md 'ask the owner before changing things') and needs work in a platform repo as well as qou, so it was not started in the wave-1 drain.
