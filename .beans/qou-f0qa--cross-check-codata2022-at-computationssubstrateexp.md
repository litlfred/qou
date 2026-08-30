---
# qou-f0qa
title: Cross-check [codata2022] at computations/substrate/experimental_constants.py
status: todo
type: task
created_at: 2026-08-08T23:34:20Z
updated_at: 2026-08-08T23:34:20Z
---

experimental_constants.py:55,58,71 states 'CODATA 2022' in its header and comments while holding the 2018 m_p/m_n/m_e and the 2018 n-p difference; correct the values or correct the label.

**From the source**
- row 'neutron-proton mass difference energy equivalent in MeV' — Delta_np = 1.29333251(38) MeV in the 2022 adjustment.
  Use here: The L2 Delta_pn accuracy target is currently scored against the 2018 value 1.2933321(5) hardcoded in experimental_constants.py; re-score against 1.29333251.

Source: `library/codata-2022-constants.txt` (`codata2022`)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.
