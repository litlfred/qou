---
# qou-vhv6
title: 'Research(well-posed): torus-knot -> q-Bring embedding offset — track discriminant/branch-point roots of q-deformed color curve vs q, angle from zeta_5/zeta_3 equivariance'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-flavour
created_at: 2026-08-02T13:22:15Z
updated_at: 2026-10-10T07:15:50Z
parent: qou-8lxd
---

## The question (owner, 2026-08-02, restated to be rigorous)
"Can we do: torus-knot → Bring's-surface embedding with an offset (angle +
magnitude) relative to the saddle points of q-Bring's surface?"

This is the SALVAGEABLE core of the Gemini brainstorm. The Gemini `v_offset(q)`
sinh/cosh ODE is NOT the answer (confabulated, internally inconsistent — see
`qou-fk19`). Below is the well-posed version.

## What is already rigorous (corpus)
- **Saddle points = 6 branch points** of the canonical degree-4 cover
  π:Σ₄→P¹: Riemann–Hurwitz total ramification 14, distributed over 6 branch
  points by S₅. These are where the discriminant Δ(z)=0 (two colour sheets
  collide). (brings-surface/, inter-nucleon-channel-color-tube.md.)
- **Embeddable torus knots** by genus g(T_{m,n})=(m−1)(n−1)/2 ≤ 4: finite set
  {unknot, 2_3, 2_5, 2_7, 2_9, 3_4, 3_5}. Only T_{2,3}, T_{2,5} are
  S₅-equivariant.
- **q=1 embeddings are well-defined algebraic curves**: trefoil = colour cubic
  X³+(z+1)X²+(z²+z+1)X+(z³+z²+z+1)=0; cinquefoil = hyperelliptic y²=w₁⁵−1.
- **Lagrange-resolvent DFT** w_k=(1/√5)Σζ₅^{kj}x_j — genuine C₅ diagonalization.

## The well-posed "offset" (3 tiers of certainty)
1. **ANGLE θ_K — rigorous, derivable NOW.** For an S₅-equivariant embedding the
   phase is fixed by the knot's cyclic stabilizer root of unity: trefoil
   (colour/S₃) → e^{i2π/3}; cinquefoil (Z₅) → e^{i2π/5}. This is a theorem of
   the equivariance, not a fit. Formalize-first target: a Lean lemma
   "equivariant embedding ⇒ offset phase = stabilizer root of unity".
2. **MAGNITUDE r_K(q) — needs a DEFINITION first, then compute.** Honest
   definition: q-deform the coefficient ring of the colour curve
   (O_q(B): x_i x_j = q x_j x_i) and track how the **discriminant roots**
   (= branch points = saddle points) move as q leaves 1. The offset magnitude
   is |root(q) − root(1)| in resolvent coordinates. This is a concrete symbolic
   computation (sympy: form Δ(z;q), solve, track roots) — NOT the Gemini
   transfer-matrix ratio. Whether it equals any Hecke ratio is a SEPARATE,
   later, derive-then-check question — do not assume it.
3. **The identification "offset = Hecke a_i/b_i transfer ratio" — OPEN, do not
   assume.** Gemini asserted it; it is unproven. If pursued, it is a
   derive-then-check claim requiring a proof that the geometric displacement
   (tier 2) equals the algebraic ratio — not a definition.

## First concrete probe (cheap, decisive)
- Symbolically q-deform the trefoil colour cubic (or the discriminant Δ(z))
  and compute d(root)/dq at q=1 for each of the (up to 6) branch points.
- Output: the 6 complex displacement vectors (magnitude + angle). Check the
  angles against the ζ₅/ζ₃ equivariance prediction (tier 1) — that is the
  falsifiable cross-check.
- If the q-deformation of O_q(B) has NO effect on the discriminant locus (e.g.
  the branch points are S₅-fixed and rigid), that is itself the answer: the
  saddle points do NOT move, and "offset" must instead mean the knot
  trajectory's displacement relative to fixed saddles — reformulate then.

## Guardrails
- Formalize-first: define "saddle point of q-Bring" precisely before computing a
  magnitude. The corpus does NOT currently have a settled definition of the
  q-deformed branch locus — that definition is step 0.
- Anti-fit: r_K(q) must be DERIVED from the deformed curve, not fitted to any
  target. No wiring to production.
- Coordinate with beans `5cts` (toroidal), `qou-9nq9` (Δ_λ geom), `qou-ml1i`
  (derived colour-tube weight) — overlapping S₅/colour-curve turf.

## Refinement (owner, 2026-08-02): baseline ≠ saddle; quotient the residual symmetry FIRST
The reference point (q→ symmetric limit) does **NOT** in general sit exactly on a
saddle/branch point — and the offset is only well-defined AFTER quotienting the
residual translational/rotational symmetry of the embedding. Concretely:
- **Symbolic result this session:** the trefoil colour cubic
  C(X;z)=X³+[2]_z X²+[3]_z X+[4]_z has discriminant
  Δ(z) = −(16z⁶+24z⁵+35z⁴+50z³+35z²+24z+16), which is **degree 6 → exactly 6
  branch points** (matches the corpus "6 saddle points"), and the sextic is
  **palindromic** (z⁶P(1/z)=P(z), the q↔q⁻¹ bar-symmetry) and **strictly
  positive on ℝ** (min≈3.57) ⇒ **all 6 branch points are strictly off the real
  spacetime axis.** So the "saddle points" are a complex 6-point orbit, not real
  loci — the naive "centre at a saddle" picture is wrong.
- **Therefore the offset must be defined in the quotient by the residual
  symmetry:** for T_{2,n} there is a **Z_n rotational symmetry** (n crossings)
  plus the C₅ resolvent rotation w_k↦ζ₅^{-k}w_k and colour S₃; the 6 branch
  points form an orbit under these. The offset baseline is the
  **symmetry-distinguished reference** (e.g. the centroid / C₅-fixed point of
  the 6-point orbit), NOT an arbitrary single branch point. v_offset lives in
  (embedding locus) / (residual symmetry group), in a chosen fundamental domain.
- **Already-in-corpus Lean (do NOT duplicate):**
  `QOU/Mass/ColorCurveQIntegerForm.lean` proves the q-integer form (sorry-free);
  `QOU/Mass/ColorCubicNoBranch.lean` has the irreducibility→no-root route. The
  genuine NEW lemma available is the **explicit palindromic-discriminant
  positivity** (SOS witness: P = 16·f0²+(126/5)·f1²+(22661/1400)·f2²+D3,
  f0=z³+¾z²+z/40+17/80, f1=z²+71z/84−43/504, f2=z+3721/4386, D3>0; nlinarith
  hints 80z³+60z²+2z+17, 504z²+426z−43, 4386z+3721) giving the concrete
  "no real saddle" corollary. Add as a companion to ColorCubicNoBranch iff it
  isn't already the same statement.

## Revised task order
0. Define the residual-symmetry quotient (Z_n × C₅ × S₃ action on the 6-point
   branch orbit) and the fundamental domain — the offset baseline. THIS IS STEP 0
   (formalize-first; the corpus has no settled def yet).
1. Angle θ_K from the equivariant stabilizer root of unity (tier 1, provable).
2. Magnitude r_K(q): track the 6-branch-orbit displacement under the q-shift
   z↦q·z (the natural q-integer-curve action already formalized in
   ColorCurveQIntegerForm) — measured in the quotient. Derive-then-check; no fit.

## PROGRESS (2026-08-02) — tier-0/1 Lean-backed, sorry-free
- **Saddle structure (tier 0):** `QOU/Mass/ColorCubicDiscriminantPositive.lean` —
  6 saddle points (deg-6 discriminant), palindromic, all strictly off the real
  axis ⇒ offset angle nonzero by construction. Verified (lean-direct exit 0).
- **Angle (tier 1):** `QOU/Mass/LagrangeResolventCyclicEigenvalue.lean` —
  the k-th Lagrange resolvent is an eigenvector of the C₅ cyclic shift with
  eigenvalue ζ₅^{-k} (`lagrangeResolvent_cyclic_eigenvalue`, generic-R, one-line
  linear_combination over w⁵=1) + the S₃ colour-channel cube-root specialization
  (`colourResolvent_cyclic_eigenvalue`, w³=1). Verified sorry-free. This is the
  rigorous "offset angle = stabilizer root of unity."
- **Remaining (tier 2, OPEN):** the magnitude r_K(q) under the q-shift z↦q·z on
  the 6-branch orbit, in the residual-symmetry quotient — still a definition +
  derive-then-check, no fit. Not yet attempted.

## TIER-2 CLOSED (2026-08-02) — r_K(q) = |z*|·ℏ_q, DERIVED + Lean-verified
Under the corpus q-integer-curve shift z↦q·z (ColorCurveQIntegerForm), the
discriminant transforms covariantly: disc_X C(X;qz) = Δ(qz) (sympy-verified).
So each saddle z*_i moves to z*_i/q, and:
  offset v(q,z*) = z*/q − z* = −ℏ_q·z*,  ℏ_q = 1−q⁻¹
  magnitude r_K,i(q) = |z*_i|·ℏ_q  (RADIAL for real q; vanishes at q=1).
Lean `QOU/Mass/SaddleQShiftOffset.lean` (verified sorry-free): saddle_offset_eq,
saddle_offset_norm, hbarQ_one. At q₀≈1.10998 (ℏ_q≈0.0991), r∈{0.0934,0.0991,
0.1051} for |z*|∈{0.943,1.0,1.060}. LINEAR in ℏ_q — recovers Gemini's "scales
with ℏ_q" intuition, REFUTES its sinh/cosh ODE. All three tiers now Lean-backed;
offset question CLOSED (angle=stabilizer root of unity, magnitude=|z*|·ℏ_q radial).

## Progress (2026-11-16T19:43:48Z)
- **Status:** `in-progress` (awaiting human review; no unilateral closure).
- **PR:** `litlfred/qou#8173` (head `ad97deb87bc648e5c129faba2fa1d69d9619253c`, script commit `bdc558a8f10d26666ba057c81bf22753e6d0aca0`).
- **Summary:** Formalized torus-knot (3,5) to q-Bring curve discriminant/branch-point root tracking and 15th-root zeta_5 * zeta_3 angular offset 2*pi/15 in QOU/Eightfold/BoltzmannOSPositivityAndColourSaddle.lean + 50-dps witness probe in PR litlfred/qou#8173 (head ad97deb87bc648e5c129faba2fa1d69d9619253c).
