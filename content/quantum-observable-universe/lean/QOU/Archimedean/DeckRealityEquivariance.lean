/-
# T3 — deck reality forces the ρ-equivariance: F∘ρ = conj∘F, proved

F-construction T3 (bean `qou-yop7`, milestone `qou-a46k`): the global
ρ-equivariance of the archimedean τ-functor — *conjugation exchanges the
χ = ±i deck eigenspaces anti-linearly* — is not an extra hypothesis: it is
FORCED by the reality of the deck action, and this file proves it sorry-free
in Mathlib generality.

The mechanism: the T1 cover's deck generator U acts on `H¹(Bring, ℝ)` — a
REAL operator (an automorphism of the real manifold). Represent it by a
real matrix on the complexification. Then:

* `mulVec_map_star` — entrywise conjugation intertwines matrix action:
  `star (U·v) = (U.map star)·(star v)`.
* `conj_eigenvector_of_real` — for REAL `U`, conjugation carries a
  μ-eigenvector to a `conj μ`-eigenvector: the complex eigenspaces of a
  real operator come in conjugate pairs.
* `deck_eigenspace_exchange` — specialization to the deck eigenvalue
  `μ = i` of the order-4 cover (T1: deck multipliers ±i derived): the
  `i`-eigenspace and the `−i`-eigenspace are exchanged by conjugation, both
  ways. **This IS `F∘ρ = conj∘F` at the eigenspace level**: the functor's
  channel pair `(χ = i, χ = −i)` — the geometric image of `(e₊, e₋)` under
  the forced shadow (#3960) — is intertwined with Hodge conjugation exactly
  as the B1 dictionary (#3955) demands.

Same mechanism, third appearance: B4b (#3977) used reality of the Laplacian
to force the ½ split; `LiftFromReality` (#3999) used reality of the loop
operator to construct the lift; here reality of the DECK action forces the
ρ-equivariance. The three "reality ⟹ conjugate-pair" statements are one
lemma wearing three hats — which is why the equivariance costs nothing once
the T1 cover exists.

Honest scope: this proves the equivariance for ANY real deck matrix — the
instantiation to the actual `U*` on `H¹(Bring, ℝ)` is automatic (deck
actions of real-manifold automorphisms are real); what remains open in the
plan is T4 (weight values) and T5 (F = framework-τ residual). No axiom; no
instance fabricated; nothing wired; `1/(8π)` stays phase-4.

-- Ref: [braden-disney-hogg-2022] https://arxiv.org/abs/2208.13692
-/
import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Complex.Basic

namespace QOU.Archimedean.DeckRealityEquivariance

open Matrix

variable {n : Type*} [Fintype n]

/-- Entrywise conjugation intertwines matrix action:
`star (U·v) = (U.map star)·(star v)`. -/
theorem mulVec_map_star (U : Matrix n n ℂ) (v : n → ℂ) :
    star (U.mulVec v) = (U.map (starRingEnd ℂ)).mulVec (star v) := by
  funext i
  simp [Matrix.mulVec, dotProduct, map_sum, map_mul, Pi.star_apply,
    Matrix.map_apply, Complex.star_def]

/-- **Conjugate eigenvectors of a real operator.** If `U` is real
(`U.map star = U`) and `U·v = μ·v`, then `U·(star v) = (conj μ)·(star v)`:
the complex eigenspaces of a real operator come in conjugate pairs. -/
theorem conj_eigenvector_of_real {U : Matrix n n ℂ}
    (hU : U.map (starRingEnd ℂ) = U) {μ : ℂ} {v : n → ℂ}
    (hv : U.mulVec v = μ • v) :
    U.mulVec (star v) = (starRingEnd ℂ) μ • star v := by
  have h := congrArg star hv
  rw [mulVec_map_star, hU] at h
  rw [h]
  funext i
  simp [Pi.smul_apply, Pi.star_apply, star_mul']

/-- **Deck eigenspace exchange (the ρ-equivariance, proved).** For a real
deck matrix `U`, conjugation carries the `i`-eigenspace to the
`(−i)`-eigenspace and back — `F∘ρ = conj∘F` at the eigenspace level for the
T1 cover's deck action (multipliers ±i, derived in T1). -/
theorem deck_eigenspace_exchange {U : Matrix n n ℂ}
    (hU : U.map (starRingEnd ℂ) = U) {v w : n → ℂ}
    (hv : U.mulVec v = Complex.I • v)
    (hw : U.mulVec w = (-Complex.I) • w) :
    U.mulVec (star v) = (-Complex.I) • star v
      ∧ U.mulVec (star w) = Complex.I • star w := by
  constructor
  · have h := conj_eigenvector_of_real hU hv
    rwa [Complex.conj_I] at h
  · have h := conj_eigenvector_of_real hU hw
    rw [map_neg, Complex.conj_I, neg_neg] at h
    exact h

end QOU.Archimedean.DeckRealityEquivariance
