---
# qou-ki4u
title: Cite [yekutieli2015] at prop:topological-mass-eigenspace-decomp
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:13Z
updated_at: 2026-10-10T07:26:05Z
parent: qou-mub3
---

Correct or remove the '[Proposition 5.3, yekutieli2015]' locator; the document's numbering is three-level and 5.3.3 says something else.

**From the source**
- Prop. 5.3.3 (the only 5.3-prefixed result in the document) — For a Lie quasi crossed module with additive feedback over X, f*(α) and Lie(Θ_G)(α) relate as stated for connection–curvature pairs.
  Use here: Establishes that the cited 'Proposition 5.3' locator does not exist and that 5.3.3 is not an orthogonal-direct-sum additivity statement.

Source: `library/arxiv-1007.1250v4/1007.1250v4.pdf` (`yekutieli2015`)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.


## 2026-10-10 — pointer

Tracked under carriers M2 and M14 of epic `qou-d8c7` "Mass endomorphism" (issue litlfred/qou#7547). Parent and status unchanged; the epic body lists what is still open for this item and where it sits in the attack-vector catalogue.

## 2026-10-10 — Done in issue litlfred/qou#7552: the locator `[Proposition 5.3, yekutieli2015]` is deleted from `topological-mass-eigenspace-decomp-proof.md:38`. No substitute exists in the held source (arXiv:1007.1250v4): Prop 5.3.3 is about pullbacks, and Thm 2.1.2(iii)'s commutator term points against the factorisation. The proof step itself stays defective; that question is `qou-wuxx` (orthogonal split refuted at free data), not this bean.
