---
# qou-0y6h
title: 'B3: invariant Gram bilinear form on cell modules; Schur element = hook/content product (reuse WenzlSchurElement.schurElement); det(Gram)=∏ Schur (Geck-Pfeiffer)'
status: todo
type: task
priority: normal
created_at: 2026-07-24T16:21:38Z
updated_at: 2026-08-29T16:33:12Z
---

## 2026-08-29 — this is closer than the standing plan implies (from qou-0ubf)

The Schur-element NON-VANISHING half is **already proved for all n**:
`WenzlSchurElement.schurElement_ne_zero` (line 231) is sorry-free, hypotheses
`1 < Q` and `X <= 0` only, no class hypothesis. And `semisimple_of_substrate`
already composes it into all-rank semisimplicity — but conditionally, on
`[SchurElementCriterion Q X ss]`, which has NO INSTANCE (verified by grep over
content/**/lean/QOU on main @ df81b22be4).

So this bean's remaining content is **exactly** Geck-Pfeiffer Thm 7.2.6 — 'every
Schur element nonzero => semisimple'. Formalising it turns `semisimple_of_substrate`
from class-conditional into an outright theorem at every rank, which discharges the
`WenzlCriterion` hypothesis of PNeqNpEquivalence for real.

Note the 2026-07-25 status audit §5 item 1 sends you to build the T_w/Matsumoto
basis + the symmetrizing-trace Gram determinant instead. That route is still the
honest Mathlib gap for the DETERMINANT approach and is worth doing on its own
merits, but it is NOT on the critical path to all-n semisimplicity. Corrected in
place in that audit; full re-measurement in
docs/audits/2026-08-29-pneqnp-gap-inventory-refresh.md.

Crosses no barrier — semisimplicity is a magnitude-axis fact. It removes one of the
two remaining cited classes from the conditional chain.
