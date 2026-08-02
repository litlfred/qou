---
# qou-vhv6
title: 'Research(well-posed): torus-knot -> q-Bring embedding offset — track discriminant/branch-point roots of q-deformed color curve vs q, angle from zeta_5/zeta_3 equivariance'
status: todo
type: task
created_at: 2026-08-02T13:22:15Z
updated_at: 2026-08-02T13:22:15Z
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
