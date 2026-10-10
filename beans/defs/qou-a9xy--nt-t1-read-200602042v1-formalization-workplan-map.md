---
# qou-a9xy
title: 'NT-T1: read 2006.02042v1 + formalization workplan — map thms/lemmas to Lean bricks, Mathlib gap analysis (q-Weyl, Ore localization, q-holonomic ideals)'
status: completed
type: task
priority: normal
created_at: 2026-07-20T03:21:57Z
updated_at: 2026-07-20T03:37:38Z
---

Done: read library/arxiv-2006.02042v1/2006.02042v1.pdf in full — scope confirmed as 4₁ exactly (Thm 1, Conj 2 = Sikora strong AJ √(ε(A^σ))=p; Lemmas 2.1/2.2, eqs (2.1)–(2.14)).
Workplan: docs/workplans/2026-07-20-nguyen-tran-strong-aj-lean-workplan.md — 12 bricks (B1–B12); recurrence certificate already sorry-free in corpus (AJFigureEightAnnihilation); walls: B3 skew-Euclidean T̃, B5 character-variety A-ideal, B7 [Tr4] transfer lemmas.
Mathlib check (olean scan, v4.24.0): HAS OreLocalization/SkewMonoidAlgebra/MvPolynomial.Groebner/Ideal.radical; NO qFactorial/qBinomial, no Ore extension, no skew Laurent, no noncomm PID.
