---
# qou-2dsk
title: S8 Classify docs/audits onto folio-assistant graph kinds
status: todo
type: feature
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:10:17Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-n4r9
---

Owner ruling 2026-10-04 (decision 10): classify only. 2,832 files: per-bean notes -> beans/notes, surveys -> beans/surveys, mechanical verdicts -> qa-reports, judgements -> attestations, derivations stay as content. Moves later, by rename only, after owner approval.

Owner hard rule: no math or physics content is changed. Every story ends with a parity check: block, chapter and .lean counts unchanged, statements byte-identical by hash, witnesses unchanged.


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- Measured: `docs/audits/` holds **2,934** files today (2,832 when this was written). Classify-only per owner decision 10; moves need approval. Not started.
