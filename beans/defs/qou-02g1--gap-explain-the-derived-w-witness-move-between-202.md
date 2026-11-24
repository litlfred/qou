---
# qou-02g1
title: 'GAP: explain the derived-w witness move between 2026-09-05 and 2026-11-22'
status: completed
type: task
priority: normal
created_at: 2026-11-22T16:40:02Z
updated_at: 2026-11-24T11:54:26Z
parent: qou-trd0
---

The derived-w probe (computations/qbeta/qbeta_derived_w_overdetermined_test_probe.py) was re-run fresh in PR #9055 (merged 2026-11-22). Its output matches the 2026-11-21 precomputed witness byte for byte, but it moved a lot against the witness committed 2026-09-05: for 2H, dtr_pred went 0.55654 -> 0.14705 and tr(D*sigma1)/tr(D) went 1.31845 -> 0.85480, and 3H and 3He moved as well. The verdict did not change: no candidate has a spread under 5%. Cause NOT determined. Candidates: the Case C Markov-trace reduction fix (#8940), the convention-D per-generator volumes (4603bfab4a), and edits to mass_at_3A_proper. Next step: bisect by re-running the probe at those commits.

## 2026-11-22 tracker hygiene (qou-w3yy, owner-approved)

Parent set to `qou-trd0`: no parent (fell into roadmap Miscellaneous). No change to this bean's scope or status.

Closed post-merge: landed on origin/main in PR #9325 (62a45d6ca1c).
