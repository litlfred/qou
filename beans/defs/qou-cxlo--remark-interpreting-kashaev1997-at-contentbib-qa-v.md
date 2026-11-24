---
# qou-cxlo
title: Remark interpreting [kashaev1997] at content/bib-qa-verifications.json
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:37Z
updated_at: 2026-11-24T13:03:46Z
parent: qou-vva9
---

Correct the join to kashaev1997 in the ledger so the volume-conjecture key finally has its source document attached, and so faddeev_kashaev1994 stops appearing verified by four documents none of which is it.

Source: `library/arxiv-q-alg-9601025v2/9601025v2.pdf` (`kashaev1997`)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## 2026-11-22 — fixed in PR #9116: Ledger: faddeev_kashaev1994 now has two rows on its own document (the dead uploads/ path repointed to library/arxiv-hep-th-9310070v1). The kashaev1997 row joins arXiv:q-alg/9601025v2.

Session: https://claude.ai/code/session_01Qmmkt5c8TSSh1GGk4PoPDu



## 2026-11-24 — Tranche 3 origin/main reconciliation

Verified on origin/main (acb646cc6fe): faddeev_kashaev1994 and kashaev1997 ledger rows repointed to library/arxiv-hep-th-9310070v1 and arXiv:q-alg/9601025v2 in merged PR #9116 (58ffccb4d16 / 3885f1e31ec).
