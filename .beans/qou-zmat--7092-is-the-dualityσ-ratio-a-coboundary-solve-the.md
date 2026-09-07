---
# qou-zmat
title: '#7092: is the duality/σ ratio a coboundary? solve the vertex-gauge system over K exactly (falsifiable form of qou-qjhc)'
status: todo
type: task
priority: normal
created_at: 2026-09-07T18:06:40Z
updated_at: 2026-09-07T18:37:57Z
parent: qou-6g7j
---

Issue #7092 restates qou-qjhc as a yes/no: do vertex scalars λ_v exist with σ(x_t)/x_π(t) = ∏ λ_{v_i}^{t_i} for every Ptolemy coordinate of the exact L6a4 class-1 point? Needs snappy's vertex-incidence data for the L6a4 triangulation, the multiplicative system over K^× (additive in the exponent lattice), and handling of the 5 coordinates eliminated by eliminate_fixed_ptolemys=True. yes → duality = σ-transport up to gauge; no → different maps, Sym² argument keeps resting on class-level agreement. Exact arithmetic, no floats, NO FITTING (no widening the ansatz, no coordinate subset selection).



**ROAST 2026-09-07 (qou-pbwj) — verdict: CONTINUE, re-scoped.** Two objections a referee raises. (1) Arity: the test runs on ONE point (the exact L6a4 class-1 point); a 'yes' establishes that this point is exchanged with its Galois conjugate by duality up to gauge — a point-level fact — not that ρ ↦ ρ^{-T} induces σ as a map on the variety (two rational self-maps can agree on a Galois orbit). Rewrite the deliverable as the point-level statement. (2) The system is multiplicative in K^×, an abelian group — not K-linear. The decisive exact form is integer: with M the (coordinates × vertices) exponent matrix, the ratios r_t are a coboundary iff ∏_t r_t^{a_t} = 1 for every a in the left ℤ-kernel of M (Smith normal form), modulo the μ₃ torsion the fifth pass identified. Fit exposure: ansatz widening on the 5 coordinates eliminated by eliminate_fixed_ptolemys=True (treat them as unknowns; do not add per-tetrahedron scalars) and subset selection (run the full system, not the 6 paired coordinates). Corpus-grep: not answered; GGZ §12 'Duality' in the library is the Ptolemy↔shape (Langlands) duality, not this. L2 relevance: none; the Sym² verdict is independent either way. Worth having even if negative: a definite NO closes qou-qjhc negatively and stops a decoration-formalisation tranche. Full frame: docs/audits/2026-09-07-takeover-fronts-roast.md §Front 2.
