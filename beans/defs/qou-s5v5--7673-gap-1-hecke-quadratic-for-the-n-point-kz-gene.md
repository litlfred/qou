---
# qou-s5v5
title: '#7673 gap 1: Hecke quadratic for the n-point KZ generator (local monodromy at the collision divisor)'
status: completed
type: task
priority: normal
created_at: 2026-10-12T18:13:09Z
updated_at: 2026-10-12T18:43:26Z
parent: qou-xhci
---

docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md §5.1 gap 1. Tools on main: QOU/KZ/Fuchsian*, KZHalfMonodromy (#7706).


2026-10-12 (gap1 agent, PR #7673): **gap 1 of audit §5.1 CLOSED, sorry-free.** New file QOU/Mass/KZHolonomy/LocalMonodromy.lean: kzBraidRep_sigma_isHeckeQuad (all n >= 2, all kappa, all c, any rho : S_n ->* A, A complete normed C-algebra): e^{2 pi i kappa c} theta(sigma_j) satisfies beta^2 = (q - q^{-1}) beta + 1, q = e^{2 pi i kappa}; heckeOfKZ / heckeOfKZ_σ: factorisation through H_n(q). Route: convergent Fuchsian solution H(u)u^{M0} near z0 = z1 (existing QOU.KZ Fuchsian theory), exchange symmetry H(-u) = P H(u) P from uniqueness of the formal solution, H(1) invertible via ODE on [eps,1], monodromy relation theta(sigma0) H(1) = H(1) P e^{i pi M0}; the non-resonance hypothesis (kappa not in +-N/4) is removed by continuity in kappa plus density of the complement of a countable set. Axioms: propext, Classical.choice, Quot.sound. Gaps 2 (continuity of Wedderburn in q) and 3 (base point at q = 1) untouched.
