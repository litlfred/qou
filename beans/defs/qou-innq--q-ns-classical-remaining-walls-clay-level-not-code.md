---
# qou-innq
title: 'q-NS classical: remaining WALLS (Clay-level, not code-closable)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-07-24T15:49:33Z
updated_at: 2026-11-27T17:50:00Z
parent: qou-a3n3
---

Open after the T1-T9 tractable tranche (categorical mechanism fully formalized; framing fixed). Genuine walls, none code-closable: (1) Bridge B2 — functor from categorical q-NS flow on Ω¹(A) to Leray-Hopf on ℝ³ (q=1 identification); (2) Bridge B3 = conj:regularity-breakdown R1/R2 — existence of smooth finite-energy v₀ with finite-T enstrophy blowup (= Clay); (3) Levi branch value — compute β=limsup log C_L/log κ (which trichotomy regime); (4) DSS/Type-II existence — nontrivial discretely-self-similar Leray profile (finite-dim ODE shooting problem, hardest tractable target); (5) true α from actual q-NS spectrum; (6) prove DSS space-time singular set within CKN parabolic ≤1. Most tractable = (4). See docs/audits/2026-07-18-q-ns-classical-gap-decomposition.md.

## Round 72 Progress (PR #8491)
- De-vacuified and proved genuine Lean 4.24.0 theorems in PR `litlfred/qou#8491` (C1 `0a93eba0e8b5b8ee92b4af6972a325d2dc1a28fd`, C2 `a9b922df9d2baa717878dbac10e60b5a5c341c6e`, 80-dps mpmath witness verified, 0 static audit findings).

## 2026-11-22T21:58:00Z: applicability review — RESCOPE

Owner instruction 2026-11-22 ("reviewed for applicability ... critical analysis"). Checked against docs/coordination/owner-rulings.md on origin/main, git log since the bean's last update, and the state of every PR it cites. The wall list predates the 2026-11-21 restatement (issue #8864) and the 2026-11-22 Galerkin dead end. (1) B2 as a q = 1 identification with Leray-Hopf is withdrawn as framed: the q -> 1 endpoint is Euler. (2) "B3 = Clay" is withdrawn: conj:regularity-breakdown is now Part A (Omega(q) -> infinity as q -> 1+) and Part B (a classical backward DSS solution with |V| ~ |y|^-1, not in L^3). (4) "Most tractable = DSS Leray profile" no longer holds: the Galerkin route is closed (scope a) and needs a new idea; the decay is r^-1. Corrected wall list: prove Part A; Part B existence by a non-Galerkin method; items (5), (6) unchanged; item (3) restated 2026-11-27 as branch (B) of conj:levi-degeneracy on the Levi scalar ξ·curl ξ (tracked in qou-fm7s), since β is undefined after ruling Q1. #8491 was closed unmerged the same day (see the 2026-11-27 note below).

## 2026-11-27: PR #8491 closed unmerged (stale reference)

PR #8491 was closed unmerged on 2026-11-22 as superseded, on the owner's decision. The "Round 72 Progress" block above describes work that never reached main. Checked against main `22b1f41263`. Already on main in some form: `LiTwo_neg_one` (`QCalculus/LiTwoNegOne.lean`, `MathlibExt/DilogarithmArchimedeanLimit.lean`), `chord_le_arc` (`QOU/BringsSurface/MobiusKernel.lean`), `not_subsingleton_unit_hom_of_nontrivial` (`QOU/Core/WitnessObstruction.lean`). Not on main, and only corollaries or wrappers of the above: `twelve_mul_LiTwo_neg_one`, `twelve_mul_cLiTwoExt_neg_one`, `chord_sq_le_arc_sq`, `mobiusKernel_symm`, `moduleCat_not_subsingleton_unit_hom_of_ne_zero`, `qou_eulerChar_nonzero` (a projection of a class field), and two `decide` checks on integer literals. None of it bears on this bean's open content. Nothing salvaged; status unchanged.

## 2026-11-27: overlap check with open PRs #9434 and #9428

Neither PR settles any wall. #9428 (holography / q-NS essay review) works on Bring's 2D finite complex; it says nothing about Part A, Part B, or items (3), (5), (6). #9434 (q-NS literature formalisation, qou-0nqs) proves exact facts on a finite 2-complex (energy equality dE/dt = -nu*Omega, conditional enstrophy decay) and, for nu_q = (1 - q^-1)/2, the bound `nuQ_one_add_le`: nu_q(1 + eps) <= eps/2. That touches item (5) only as an ingredient: the conditional alpha = 1 route (closure Omega = eps/nu_q, see qou-15gb, qou-l5pt) would use nu_q ~ (q - 1)/2 exactly, but the closure stays a named hypothesis and alpha is not settled. Part A and Part B are untouched.

## 2026-11-27: item (3) has no subject on main

Item (3), "Levi branch value: compute β = limsup log C_L / log κ", no longer has a subject. Owner ruling Q1 (2026-10-13, bean qou-fm7s) re-scoped the Levi chain onto Θ = f·ξ♭ on the 3D flow domain, where the Levi form is 1 × 1 (the scalar ξ·curl ξ). C_L, β and the trichotomy are withdrawn as undefined (`conj:levi-degeneracy`, `QOU/FluidDynamics/levi_growth_trichotomy.lean` header, checked on main `ba53c84cd5`). Branch (A) is withdrawn (`beltrami_refutes_branchA`). What survives is branch (B) on the Levi scalar, an open conjecture carried by `LeviDegeneracyQ1.LeviDegeneracy` (no instance), tracked in qou-fm7s. Suggested restatement of item (3), pending the owner: "branch (B) of conj:levi-degeneracy on ξ·curl ξ (see qou-fm7s)", or drop it from this list. Not edited above; status unchanged.

## 2026-11-27 Part A (sibling thread "Prove q-NS Part A blowup") — PR #9485

Part A now has Lean: `QOU/FluidDynamics/q_ns_enstrophy_order_parameter.lean` (sorry-free).
Relative to `QNsWellposednessContext` (scope (b), invariant = field `modal_inequality` + `qIntBal_mono`):
substrate-layer (q-independent) data -> Part A FALSE (Omega attained at t=0, monotone in q, bounded as q->1+);
physical-layer data -> alpha = 2 by unit conversion only (artifact); free q-dependent data -> empty.
`stokesContext` (linear Stokes flow) satisfies every field, so the context cannot see nonlinear mode transfer.
Part A stays OPEN for a modal law with triad transfer. Owner decision pending: weaken thm:q-ns-wellposedness
property 3 / withdraw Part A / record physical-layer reading as artifact. Audit:
docs/audits/2026-11-27-qns-part-a-enstrophy-order-parameter.md

## 2026-11-27 Part B route (thread 'Find q-NS Part B route'), PR #9491

Owner chose R4, tail matching + degree. Part B is a nonzero zero of g(c) = Ac + Q(c) on log-phase tail coefficients. Q is even, so if Q has no real projective zero, every truncation has nonzero zeros, which explains the Galerkin artifacts. Open step: an a priori bound uniform in the truncation (Leray–Schauder). R1 (Lamb-gradient / Beltrami) is closed: the Kummer coefficients are nonzero (DSSTailMatching.lean, sorry-free). R2 gives only Landau. Owner asked for a separate thread on the Bernoulli-flux bound. Item 3: no subject (see above). Items 5 and 6 are now child beans. Audit: docs/audits/2026-11-27-qns-part-b-route-assessment.md. Status stays in-progress: Part B is open.

## 2026-11-27: item (3) restated

Owner took the recommended options (2026-11-27). Item (3) now reads "branch (B) of conj:levi-degeneracy on ξ·curl ξ (see qou-fm7s)" in the corrected wall list above, replacing the withdrawn β computation. Status unchanged.
