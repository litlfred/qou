---
# qou-bnq7
title: '[REST S-REST-4] Route uploads/ out'
status: todo
type: feature
priority: normal
tags:
    - migration
    - rest
created_at: 2026-10-04T16:35:59Z
updated_at: 2026-11-21T13:30:00Z
parent: qou-n4r9
---

From the REST migration analysis (2026-10-04), story S-REST-4. Full report: docs/audits/2026-10-04-workplan-and-migration/REST_report.md.

4. S-REST-4: Route uploads/ out. - Scope: 8 platform PDFs → cat-harness library, 7 WHO → smart-base. - Done when: every PDF's sha256 is found in its destination entry's record, and qou `uploads/` holds only the keep marker. - Size S.

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- Measured: `uploads/` on main holds only `.gitignore` (the keep marker). The local half of the done-when is met. NOT checked: whether each PDF's sha256 is recorded at its destination (cat-harness library, smart-base). Close once that parity is shown.


## 2026-11-21 — follow-up check (session_01Qmmkt7b8yRZEmMY5Qwa33W)

Traced every PDF that was in `uploads/` on 2026-10-04 (40 files):
- **7 WHO PDFs**: removed in qou `210c6bd25a` (2026-10-10) after a full sha256 check against `source.sha256` in litlfred/smart-base main `391f71c` (`smart-base/library/<id>/structure.json`). Met.
- **`Home _ folio-assistant.pdf`**: same commit; sha256 equal to `fsh-guts/uploads/Home-_-folio-assistant.pdf` on folio-assistant `cat/cat-harness/fsh-guts` (owner: 'Move it to fsh-guts'). Met.
- **`arxiv-astro-ph-0203462v1/`** (23-file extraction residue): removed in `76805d3cb7`; `library/arxiv-astro-ph-0203462v1` is the ingested entry. Met.
- **8 agentic-SE / MCDM arXiv PDFs**: removed in `a0fbe79bf0` (2026-11-15; owner asked to move them to folio-assistant for redistribution, not to the cat-harness library). The receiving PR **litlfred/folio-assistant#3149 is still OPEN and draft** (mergeable_state unstable, last update 2026-11-15). The git blob shas of all 10 files on that PR equal the qou blobs at `a0fbe79bf0^` (measured today), so the bytes are identical and safe on that branch and in qou history, but no destination record holds them yet.

**Done-when not met** until folio-assistant#3149 merges. Nothing is left to do on the qou side.
