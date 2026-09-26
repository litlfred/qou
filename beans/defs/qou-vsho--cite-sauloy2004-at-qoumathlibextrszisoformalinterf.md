---
# qou-vsho
title: Cite [sauloy2004] at QOU/MathlibExt/RSZIsoformalInterface.lean — Prop 4.1 gives the algebraic 'one slope ⇒ End^{>0}(M0)=0 ⇒ trivial Stokes sheaf' behind rszIsoformalDim_one
status: todo
type: task
tags:
    - paper-relevance-triage
    - qdiff-stokes
created_at: 2026-09-07T08:36:01Z
updated_at: 2026-09-07T08:36:01Z
parent: qou-2akx
---

Source: library/arxiv-math-0409393v1/0409393v1.pdf -> [sauloy2004] (Sauloy, algebraic construction of the Stokes sheaf). Relevance: **supporting** — agent assessment, not yet adjudicated. Raised by local/paper-relevance-triage 2026-09-07. One bean for the document's actions.

The corpus argues "a pure isoclinic module has no local Stokes data" two ways (docs/audits/2026-08-08-c1-infinity-has-no-stokes-multiplier.md §"Why, from RSZ"): the RSZ Thm 3.3.5 dimension count (formalised as `rszIsoformalDim_one` in RSZIsoformalInterface.lean) and the RSZ §4.4 / §5.5.2 unipotent-triangular reading. Sauloy 2004 gives the same conclusion in one algebraic line:

- Prop 4.1 (i): the sheaf λ_I(M0) underlying the Stokes sheaf is the sheaf of sections of the holomorphic vector bundle over E_q associated to End^{>0}(M0) = ⊕_{μ_i > μ_j} Hom(P_j, P_i). With a single slope the sum is empty, End^{>0}(M0) = 0, and Λ_I(M0) is trivial.
- Thm 3.18: the classification F(M0) ≅ H^1(E_q, Λ_I(M0)) proved algebraically (no discrete summation, no Newlander–Nirenberg).
- Thm 3.7: the canonical resummation F_D(U,V) along a divisor "direction" D on E_q, unique subject to a divisor bound on the over-diagonal blocks.

What to do: (1) add `-- Ref: [sauloy2004] https://arxiv.org/abs/math/0409393 (Prop 4.1, Thm 3.18)` next to the RSZ ref in RSZIsoformalInterface.lean and cite Prop 4.1 in the `rszIsoformalDim_one` docstring as the algebraic form of the same fact; (2) add the citation to the c1-infinity audit §2.

Not claimed: anything about C1's global connection matrix (qou-wgnx), which is not a local Stokes-sheaf question.
