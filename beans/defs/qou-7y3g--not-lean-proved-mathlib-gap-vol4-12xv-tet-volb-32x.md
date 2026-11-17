---
# qou-7y3g
title: 'NOT-LEAN-PROVED (Mathlib gap): Vol(4_1)=2xV_tet, Vol(B_3)=2xV_oct are numerical only'
status: in-progress
type: task
priority: low
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T17:10:12Z
updated_at: 2026-11-17T10:08:09Z
parent: qou-c8p8
---

NOT LEAN-PROVED, and NOT REALISTICALLY CLOSABLE SOON — a large Mathlib gap.
Recorded so the numerical status is not mistaken for a proof.

CLAIM (PR #4513, qbeta_sdp_angle_offset_theta_probe.py, R1 section):
  Vol(4_1)  = 2 x volume of the regular ideal TETRAHEDRON
  Vol(B_3)  = 2 x volume of the regular ideal OCTAHEDRON
verified numerically to 9.5e-12 and 3.1e-13 relative (SnapPy vs closed forms
Im Li_2(e^{i*pi/3}) and 4*Catalan).

CONSEQUENCE BEING CLAIMED ON THIS BASIS: neither volume is a measured input —
both are FORCED by the cell decomposition. That reclassifies them from
untraceable literals to `structural` for the no-free-parameter certificate
(bean qou-skum). That reclassification currently rests on NUMERICS.

WHY IT IS HARD: Mathlib has no hyperbolic-volume theory for ideal tetrahedra —
no Lobachevsky function, no ideal-simplex volume, no Mostow rigidity. Proving
this in Lean means building that infrastructure first. This is infra-scale, not
a session-scale task.

HONEST DISPOSITION: leave numerical, labelled numerical. Do NOT axiomatise the
volume identity as a Lean `class` and consume it downstream — that would be
exactly the laundering AGENTS.md forbids ("Axiomatization is NOT a Proof"). If
qou-skum wants `structural` classification, the justification is the cited
literature fact plus this numeric check, stated as such.

---

# ATTACK VECTORS (2026-08-08)

## Where it sits in the chain

At the **Archimedean end**: `Vol(K)` enters the mass formula
`m(K) = m_e * Vol(K) * rho(K) / hbar_q^2` and the binding channel's
`V_41(0) = Vol(4_1)`. It intervenes between **the knot's hyperbolic geometry and
the MeV observable**. So it is not decorative — it is load-bearing for absolute
mass, which is why "numerical only" is worth tracking rather than shrugging at.

## AV1 — this bean is now BLOCKED ON, and unblocked by, one shared piece of infra

The same missing Mathlib theory blocks `qou-krvm` hypothesis (iv) (Rivin volume
concavity). Both need ideal-simplex volume in Lean. Split out as its own
infra bean so the two consumers stop each carrying the same "large Mathlib gap"
note: see the ideal-tetrahedron-volume bean.

## AV2 — the two claims have DIFFERENT difficulty; do not treat them as one

  * `Vol(B_3) = 2 * V_oct = 8*Catalan`  — the octahedral one reduces to Catalan's
    constant, and `Mathlib` has more Catalan/Clausen material than it has ideal
    simplices. Check `Mathlib.Analysis.SpecialFunctions` for Clausen/Lobachevsky
    before assuming both are equally far.
  * `Vol(4_1) = 2 * V_tet = 2*Cl_2(pi/3)`  — needs the Lobachevsky function.

`QOU.Archimedean.ClausenFunctionMathlibFiller` already exists in the tree (it is
in the `FigureEightComplexVolume` import cone). START THERE — the gap may be
narrower than this bean assumed when it was filed.

## AV3 — the honest interim already exists and should be used, not re-litigated

`V_41(0) = 2*Cl_2(pi/3)` is stated EXACTLY in `FigureEightComplexVolume`
(`V₄₁_zero_re`), because `a_2` is purely imaginary. So the corpus already has
the closed form as a Lean-level statement; what is missing is the bridge from
"the closed form" to "the hyperbolic volume of the manifold". Name that bridge
precisely — it is a smaller target than "hyperbolic volume theory".

## AV4 — an EXACT appearance of the octahedral shape (added 2026-08-08, PR #4769)

Relevant to the `Vol(B_3) = 2 x V_oct` half, and NOT numerical. The Descartes
cubic at the classical point `q = 1` factors over Q:

    27x^3 + 18x + 20 = (3x + 2)(9x^2 - 6x + 10)   -> roots -2/3, 1/3 +- i

so the Legendre invariant is `z_1 = (1+i)/(1-i) = i` EXACTLY — the shape of the
ideal tetrahedron whose angle triple is `(pi/2, pi/4, pi/4)` and whose volume is
`D(i) = Catalan G`, one quarter of the regular ideal octahedron (`4G`), i.e.
`Vol(B_3)/8`. Machine-checked over `fractions.Fraction` in
[`computations/qbeta/xi_classical_limit_probe.py`](../computations/qbeta/xi_classical_limit_probe.py)
(`q1_exact()`).

**WHAT THIS DOES AND DOES NOT GIVE YOU.** It does NOT close this bean and does
NOT prove `Vol(B_3) = 8G`. The gap this bean names is the GEOMETRIC bridge —
"this closed form" -> "the hyperbolic volume of that manifold" — and an exact
shape parameter supplies no part of it. What it does give: the octahedral shape
now appears in the corpus by **exact algebra** rather than only by SnapPy
numerics, so a future closure has an anchor-free starting point on the shape
side. Treat as a lead, not as progress on the volume identification.

## GUARD (unchanged, and it is the point of this bean)

Do NOT axiomatise the volume identity as a Lean class and consume it downstream.
That is the laundering AGENTS.md forbids. Leave numerical, labelled numerical.
AV4 above is an exact fact about a SHAPE PARAMETER; it is not the volume
identity and must not be cited as if it were.

### Progress Update (2026-11-17, Round 59 — lane-e667)
- **PR:** `litlfred/qou#8291` (`https://github.com/litlfred/qou/pull/8291`), head `97f9ffaed50b1b3971470d9bc651293cd4f935e3` (`COMMIT1 = 9f95671d31537da41246588ea9801b300607f995`), labeled `ready-to-merge` + `release`, `ready: 97f9ffaed50b1b3971470d9bc651293cd4f935e3` (`https://github.com/litlfred/qou/pull/8291#issuecomment-6944908884`).
- **Lean 4.24.0 Module:** `folio/quantum-observable-universe/lean/QOU/Foundations/HyperbolicScalingDescartesCubicFarkasDuality.lean` (wired into `QOU.lean`; `0` `sorry`, `0` `axiom`, `0` warnings, `0` CRITICAL/major/advisory across all 6 static vacuity & borrowed-name audits):
  - `qou-322e`: `chordal_step_symmetry_diagonal_and_concatenation` over `CommRingCarrier R`.
  - `qou-4tsl`: `alternating_two_wedge_antisym_and_three_wedge_vanishing` and `alternating_two_wedge_ring_antisym_and_diag` over `Int` and `CommRingCarrier R`.
  - `qou-5gai`: `dilation_cube_jacobian_density_cancellation` over `CommRingCarrier R`.
  - `qou-7y3g`: `classical_av4_cubic_factorization_and_complex_roots` over `Int`.
  - `qou-9h4t`: `primal_dual_slack_gap_and_complementary_slackness` over `Int`.
- **80-dps Probe & 2-Commit Witness:** `computations/probes/hyperbolic_scaling_descartes_cubic_farkas_duality_probe.py` + `computations/probes/hyperbolic-scaling-descartes-cubic-farkas-duality.witness.json` (`scriptHash = 9b07010b5e8c`, `scriptCommitSha = 9f95671d31537da41246588ea9801b300607f995`, `allPassed = True`).
- **Adversarial Cross-Review (Round 59):** Verified `litlfred/qou#8276` (`1909a7bd3bec6ebbdc594cc42f836c8a59fb6451`, `0` advisories) and remediated `3 major, 2 advisory` borrowed-name findings on sibling PR `litlfred/qou#8261`, pushing `77aeb5c622eb2876245d1628c2f107b5f85999f8` and posting `ready: 77aeb5c622eb2876245d1628c2f107b5f85999f8` (`https://github.com/litlfred/qou/pull/8261#issuecomment-6942739479`).
- **Status:** Kept at `in-progress` pending Merge Manager verification and merge.
