---
# qou-7y3g
title: 'NOT-LEAN-PROVED (Mathlib gap): Vol(4_1)=2xV_tet, Vol(B_3)=2xV_oct are numerical only'
status: todo
type: task
priority: low
created_at: 2026-08-07T17:10:12Z
updated_at: 2026-08-07T17:10:12Z
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

## GUARD (unchanged, and it is the point of this bean)

Do NOT axiomatise the volume identity as a Lean class and consume it downstream.
That is the laundering AGENTS.md forbids. Leave numerical, labelled numerical.
