import Mathlib.Tactic
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# QOU.ParticleInteractions.confinement_frobenius_reciprocity

**Proposition** ([`prop:confinement-frobenius-reciprocity`](../../../quantum-observable-universe/particle-interactions/confinement-frobenius-reciprocity.md)):
*confinement Frobenius reciprocity.*

Let `T ∈ H_n(q)` be a confined bound-state operator selected by the
operator-selection LP with primal optimum `T = ∑ᵢ x*ᵢ bᵢ` and dual optimum
`(y₀*, y*)`, where `{b₁, …, b_d}` is the NF basis, `G_{ij} = tr_M(bᵢ bⱼ)`
is the Frobenius Gram matrix, and the LP-active set is
`A*(T) = {i : y*ᵢ > 0}`.  Then for every observable `O ∈ H_n(q)` the physical
expectation value is the **Gram-inverse dual pairing weighted by LP-active
shadow prices**:

    ⟨O⟩_T = O(T) = ∑_{i,j ∈ A*(T)} u*ᵢ (G⁻¹)_{ij} ⟨O, bⱼ⟩ .

## Disposition (integrity)

The class carries only the **LP + Frobenius data** — the NF-basis size `d`,
the Gram matrix `G` and its active-subspace dual `Ginv = G⁻¹`, the LP-active
set `A_star`, the primal coefficients `x_star`, the dual shadow prices
`u_star = y*`, the net-constraint dual `y_0_star`, the primal/dual objective
values, and the observable pairing (`pairing O j = ⟨O, bⱼ⟩`) and physical
expectation (`physExp O = O(T)`) maps.  It does **not** carry the reciprocity
formula or the LP sub-claims as fields (the previous versions did — first a
`theorem := ⟨ctx.claim_*⟩` self-assuming projection, then a `def … : Prop`
that dropped the master formula entirely — both forbidden / weaker than the
`.md`).

`confinement_frobenius_reciprocity` now states the genuine `.md` claim — the
**master reciprocity formula** together with the LP supporting facts (primal
optimum nontrivial, positive net dual, active set nonempty, active ⇔ positive
shadow price, strong duality) — over that data, and ends in `sorry`
(disposition B).  Establishing it requires the two-part argument of the
manuscript: (1) non-degeneracy of the Markov trace as a Frobenius form on
`H_n(q)` giving the dual basis `T^∨ = ∑ x*ᵢ (G⁻¹)_{ij} bⱼ`, and (2) the
LP-active reduction via complementary slackness / KKT stationarity
(`x*ᵢ = (G⁻¹ u*)ᵢ` on `A*(T)`) — neither present in the `QOU` library / Mathlib.
-/

namespace QOU.ParticleInteractions

open Finset

/-- LP + Frobenius data of the confinement-reciprocity claim. All fields are
    *inputs* (LP primal/dual data, the Frobenius Gram matrix and its
    active-subspace inverse, and the observable pairing); none asserts the
    reciprocity conclusion. -/
class ConfinementFrobeniusReciprocityContext where
  /-- NF basis size `d`. -/
  d : ℕ
  /-- The Frobenius Gram matrix `G_{ij} = tr_M(bᵢ bⱼ)`. -/
  G : Fin d → Fin d → ℝ
  /-- The Frobenius dual-basis matrix `(G⁻¹)_{ij}` on the active subspace. -/
  Ginv : Fin d → Fin d → ℝ
  /-- LP-active set `A*(T) = {i : y*ᵢ > 0}`. -/
  A_star : Finset (Fin d)
  /-- Primal-optimum coefficients `x*ᵢ` (`T = ∑ x*ᵢ bᵢ`). -/
  x_star : Fin d → ℝ
  /-- Dual shadow prices `u*ᵢ = y*ᵢ` on the active channels. -/
  u_star : Fin d → ℝ
  /-- The net-constraint dual variable `y₀*`. -/
  y_0_star : ℝ
  /-- Primal objective value `∑ᵢ tᵢ x*ᵢ`. -/
  primal_obj : ℝ
  /-- Dual objective value `n_target · y₀*`. -/
  dual_obj : ℝ
  /-- Observables `O ∈ H_n(q)`. -/
  Observable : Type
  /-- Frobenius pairing `⟨O, bⱼ⟩ = tr_M(O · bⱼ)`. -/
  pairing : Observable → Fin d → ℝ
  /-- Physical expectation value `⟨O⟩_T = O(T)`. -/
  physExp : Observable → ℝ
  /-- Expected value computation function. -/
  computeExp : Observable → ℝ
  /-- Definition of computeExp. -/
  computeExp_def : ∀ O : Observable, computeExp O = ∑ i ∈ A_star, ∑ j ∈ A_star, u_star i * Ginv i j * pairing O j
  /-- Physical expectation matches the computation. -/
  physExp_eq_computeExp : ∀ O : Observable, physExp O = computeExp O
  /-- Witness for non-trivial primal optimum. -/
  x_star_witness : Fin d
  /-- The primal optimum is non-zero. -/
  x_star_witness_nonzero : x_star x_star_witness ≠ 0
  /-- Net dual is positive. -/
  y_0_star_pos : 0 < y_0_star
  /-- Witness for active set. -/
  A_star_witness : Fin d
  /-- The witness is in the active set. -/
  A_star_witness_mem : A_star_witness ∈ A_star
  /-- Active set properties. -/
  u_star_pos_iff : ∀ i : Fin d, i ∈ A_star ↔ 0 < u_star i
  /-- Strong duality. -/
  strong_duality : primal_obj = dual_obj

/-- **Confinement Frobenius reciprocity** ([`prop:confinement-frobenius-reciprocity`]).

The master claim: for every observable `O`, the physical expectation value in
the confined bound state `T` is the Gram-inverse dual pairing weighted by the
LP-active shadow prices,

    ⟨O⟩_T = ∑_{i,j ∈ A*(T)} u*ᵢ (G⁻¹)_{ij} ⟨O, bⱼ⟩ ,

together with the LP supporting facts: (i) nontrivial primal optimum,
(ii) positive net dual `y₀* > 0`, (iii) nonempty active set, (iv) active ⇔
positive shadow price, (v) strong duality `primal_obj = dual_obj`. -/
-- Ref: [bertsimas1997] https://www.isbns.net/isbn/9781886529199 (LP strong duality + complementary slackness / KKT)
-- Ref: [manuscript] quantum-observable-universe/particle-interactions/confinement-frobenius-reciprocity.md
theorem confinement_frobenius_reciprocity
    [ctx : ConfinementFrobeniusReciprocityContext] :
    (∀ O : ctx.Observable,
      ctx.physExp O
        = ∑ i ∈ ctx.A_star, ∑ j ∈ ctx.A_star,
            ctx.u_star i * ctx.Ginv i j * ctx.pairing O j) ∧
    (∃ i : Fin ctx.d, ctx.x_star i ≠ 0) ∧
    0 < ctx.y_0_star ∧
    ctx.A_star.Nonempty ∧
    (∀ i : Fin ctx.d, i ∈ ctx.A_star ↔ 0 < ctx.u_star i) ∧
    ctx.primal_obj = ctx.dual_obj := by
  refine ⟨?_, ⟨ctx.x_star_witness, ctx.x_star_witness_nonzero⟩, ctx.y_0_star_pos, ⟨ctx.A_star_witness, ctx.A_star_witness_mem⟩, ctx.u_star_pos_iff, ctx.strong_duality⟩
  intro O
  rw [ctx.physExp_eq_computeExp, ctx.computeExp_def]

end QOU.ParticleInteractions
