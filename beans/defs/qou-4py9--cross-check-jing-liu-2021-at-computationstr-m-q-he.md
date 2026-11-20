---
# qou-4py9
title: Cross-check [jing-liu-2021] at computations/tr_m_q_hecke_seminormal.py
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:35:24Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-mub3
---

jing-liu-2021 is cited only in the .ts cites[] and none of its results is used. Its hook (Thm 2.9) and two-row (Thm 2.11) closed forms give a parameter-free external cross-check of the chi^lambda_q values the block's producer computes, which would make the citation load-bearing instead of decorative.

**From the source**
- Thm 2.9 — Closed formula for the irreducible Iwahori-Hecke character chi^lambda labelled by a HOOK partition, for any mu |- n.
  Use here: Independent closed form to cross-check computations/tr_m_q_hecke_seminormal.py and the Hoefsmit chi^lambda_q values on hook irreps.
- Thm 2.11 — Closed formula for the irreducible Hecke characters labelled by TWO-ROW partitions.
  Use here: Second independent cross-check family for the same chi^lambda_q compute (n>=4 two-row blocks).

Source: `library/arxiv-2104.06067v1/2104.06067v1.pdf` (`jing-liu-2021`)
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8475, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
