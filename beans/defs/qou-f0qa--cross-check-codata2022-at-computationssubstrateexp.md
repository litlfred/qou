---
# qou-f0qa
title: Cross-check [codata2022] at computations/substrate/experimental_constants.py
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:20Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-mub3
---

experimental_constants.py:55,58,71 states 'CODATA 2022' in its header and comments while holding the 2018 m_p/m_n/m_e and the 2018 n-p difference; correct the values or correct the label.

**From the source**
- row 'neutron-proton mass difference energy equivalent in MeV' — Delta_np = 1.29333251(38) MeV in the 2022 adjustment.
  Use here: The L2 Delta_pn accuracy target is currently scored against the 2018 value 1.2933321(5) hardcoded in experimental_constants.py; re-score against 1.29333251.

Source: `library/codata-2022-constants.txt` (`codata2022`)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8489, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
