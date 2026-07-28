import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp

/-!
# Per-block weights over disjoint index sets impose no constraint on A-growth

**Why no finite list of failed weight candidates excludes the class.**

In the Δ_λ binding programme a *per-block weight* is a function on partitions,
and each isotope samples it on partitions of its **own** `n`: the deuteron uses
`λ ⊢ 6` (11 of them), tritium and ³He use `λ ⊢ 9` (30), ⁴He uses `λ ⊢ 12` (77).
Those index sets are **disjoint** — they share no partition at all. The natural
question is then whether the observed A-growth

  `S(⁴He) / S(D) = (∑ᵢ u i * A i) / (∑ⱼ v j * B j)`

constrains the weight. This file proves it does not: with disjoint index sets
the weight restricted to each isotope is an *independent* degree of freedom, so
**every** positive growth value is attainable (`growth_ratio_attains_any`), and
a fortiori no finite collection of failed candidates can exclude the class.

The contrast with `QOU.MathlibExt.GibbsRatioMonotonicity` is the point: there a
*one-parameter family* (damping time `τ`) is genuinely constrained and can be
excluded wholesale; here the *unrestricted class* is not. An exclusion in this
programme therefore has to name a formula family — it cannot be inferred from a
pattern of misses, however uniform that pattern looks.

Recorded because the session repeatedly read the uniform isotope-spread failures
(6.61×, 34.1×, 0.04–3.07, 455×) as evidence against per-block weights as such.
That inference does not hold, and this file is the reason.

Base ring: **generic** `[Field R] [LinearOrder R] [IsStrictOrderedRing R]` (§7c).
No `Real.exp`, no completeness, no archimedean construct beyond the ordering —
so the statement holds over any ordered field, not merely `ℝ`. (Note that
Mathlib has retired the bundled `LinearOrderedField`; this is its current
spelling.)
-/

namespace QOU.MassTheory.PerBlockWeightFeasibility

open Finset

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]
variable {ι κ : Type*} [Fintype ι] [Fintype κ] [DecidableEq ι] [DecidableEq κ]

/-- A weight concentrated on a single index (a point mass of size `c`). -/
noncomputable def pointMass (i₀ : ι) (c : R) : ι → R := fun i => if i = i₀ then c else 0

omit [IsStrictOrderedRing R] [Fintype ι] in
/-- A point mass is non-negative when its size is. -/
theorem pointMass_nonneg {i₀ : ι} {c : R} (hc : 0 ≤ c) : ∀ i, 0 ≤ pointMass i₀ c i := by
  intro i
  unfold pointMass
  split <;> simp [hc]

omit [LinearOrder R] [IsStrictOrderedRing R] in
/-- A point-mass–weighted sum collapses to the single term. -/
theorem sum_pointMass (i₀ : ι) (c : R) (A : ι → R) :
    ∑ i, pointMass i₀ c i * A i = c * A i₀ := by
  unfold pointMass
  simp [Finset.sum_ite_eq' Finset.univ i₀ (fun i => c * A i)]

/-- **Every positive A-growth is attainable.** Given any target `t > 0`, there
are non-negative per-block weights `u` (on the numerator's index set) and `v`
(on the denominator's) realising it exactly.

This is what disjointness of the index sets buys: `u` and `v` are unconstrained
relative to one another, so the ratio carries no information about the weight.
Hence the per-block-weight class is **not excludable** by any finite list of
failed candidates. -/
theorem growth_ratio_attains_any (A : ι → R) (B : κ → R) (i₀ : ι) (j₀ : κ)
    (hA : 0 < A i₀) (hB : 0 < B j₀) {t : R} (ht : 0 < t) :
    ∃ u : ι → R, ∃ v : κ → R,
      (∀ i, 0 ≤ u i) ∧ (∀ j, 0 ≤ v j) ∧
      (∑ i, u i * A i) / (∑ j, v j * B j) = t := by
  refine ⟨pointMass i₀ (t * B j₀ / A i₀), pointMass j₀ 1,
    pointMass_nonneg (div_nonneg (mul_nonneg ht.le hB.le) hA.le),
    pointMass_nonneg zero_le_one, ?_⟩
  rw [sum_pointMass, sum_pointMass]
  field_simp

/-- **The class-level statement.** For any two targets whatsoever, both are
attainable — so no inequality between attained growths can distinguish the
class. Corollary of `growth_ratio_attains_any`, recorded as the form the Δ_λ
argument actually uses. -/
theorem no_growth_constraint (A : ι → R) (B : κ → R) (i₀ : ι) (j₀ : κ)
    (hA : 0 < A i₀) (hB : 0 < B j₀) {t₁ t₂ : R} (h₁ : 0 < t₁) (h₂ : 0 < t₂) :
    (∃ u : ι → R, ∃ v : κ → R, (∀ i, 0 ≤ u i) ∧ (∀ j, 0 ≤ v j) ∧
        (∑ i, u i * A i) / (∑ j, v j * B j) = t₁) ∧
    (∃ u : ι → R, ∃ v : κ → R, (∀ i, 0 ≤ u i) ∧ (∀ j, 0 ≤ v j) ∧
        (∑ i, u i * A i) / (∑ j, v j * B j) = t₂) :=
  ⟨growth_ratio_attains_any A B i₀ j₀ hA hB h₁,
   growth_ratio_attains_any A B i₀ j₀ hA hB h₂⟩

end QOU.MassTheory.PerBlockWeightFeasibility
