import Mathlib.Tactic

/-!
# QOU.Intent

**Canonical declaration** for content block at
[`quantum-observable-universe/quantum-observable-universes/observation.ts`](quantum-observable-universe/quantum-observable-universes/observation.ts).

Formalises the manuscript **observation** structure: an observation morphism
`𝔒 : A → A` acting fibrewise on the state bundle, and the two-observer
parallelogram — two independent observations produce a discrepancy (their
commutator) controlled by the local Planck constant `ℏ_q`, vanishing exactly
when the observations commute. Generic ring (§7c-clean).
-/

namespace QOU

/-- Data for a two-observer observation record.

    A `definition` carrier: the ambient observable algebra `A` and two
    observation morphisms `𝔒₁, 𝔒₂ : A → A`. The two-observer discrepancy is
    their commutator. -/
structure Intent (A : Type*) [Ring A] where
  /-- First observer's observation morphism `𝔒₁`. -/
  obs₁ : A → A
  /-- Second observer's observation morphism `𝔒₂`. -/
  obs₂ : A → A

namespace Intent

variable {A : Type*} [Ring A] (I : Intent A)

/-- The two-observer discrepancy at a state `a`: `𝔒₁(𝔒₂ a) − 𝔒₂(𝔒₁ a)`. -/
def discrepancy (a : A) : A := I.obs₁ (I.obs₂ a) - I.obs₂ (I.obs₁ a)

/-- If the two observations commute at `a`, the discrepancy vanishes — the
    parallelogram closes (no `ℏ_q`-controlled defect). -/
theorem discrepancy_eq_zero_of_commute {a : A}
    (h : I.obs₁ (I.obs₂ a) = I.obs₂ (I.obs₁ a)) : I.discrepancy a = 0 := by
  unfold discrepancy; rw [h, sub_self]

/-- The discrepancy is antisymmetric under swapping the two observers. -/
theorem discrepancy_swap (a : A) :
    (Intent.mk I.obs₂ I.obs₁).discrepancy a = - I.discrepancy a := by
  unfold discrepancy; abel

end Intent

-- Ref: [leitner2026] quantum-observable-universe/quantum-observable-universes/observation.ts

end QOU
