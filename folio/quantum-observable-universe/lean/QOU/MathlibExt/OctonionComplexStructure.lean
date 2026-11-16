import QOU.MathlibExt.OctonionSU3BracketClosure

set_option maxHeartbeats 4000000
set_option maxSynthPendingDepth 5

/-!
# QOU.MathlibExt.OctonionComplexStructure — the ℚ-form of `𝕆 = ℂ ⊕ ℂ³`

The Dubois-Violette–Todorov splitting (`dubois-violette-todorov2018`
Sec. 2) fixes a unit imaginary octonion and reads `𝕆` as a 4-dimensional
complex vector space; the colour `SU(3)` is then the complex-linear
symmetry. This file lands the ℚ-form of that structure on the corpus's
own concrete octonions (`octMul`, Baez convention), for the standard
imaginary unit `e₁`:

* `Le : 𝕆 →ₗ 𝕆` — left multiplication by `e₁`;
* `Le_sq_eq_neg_id` — **`Le² = −id`**: `Le` is a complex structure on
  the full 8-dimensional ℚ-space (the alternative-algebra identity
  `u(ux) = u²x = −x`, machine-checked componentwise on the concrete
  multiplication table);
* `su3_comp_Le_eq_Le_comp` — **the colour stabilizer acts
  ℂ-linearly**: every derivation `D ∈ su3 e₁` commutes with `Le`. The
  proof is pure Leibniz — `D(e₁·x) = D(e₁)·x + e₁·D(x) = e₁·D(x)`
  since `D(e₁) = 0` — so the stabilizer's action on the octonion base
  module is not merely ℚ-linear (the tautological instance of
  `OctonionColourActionBaseModule`) but linear over the complex
  structure the fixed unit defines. This is the algebraic heart of the
  `𝟏 ⊕ 𝟑` colour decomposition, in exact rational arithmetic.

Together these are the first brick of the M₃(ℂ)-route (bean `qou-1gix`,
feeding GAP bean `qou-ni4b`): the remaining steps are the `Le`-stable
splitting `span(1, e₁) ⊕ span(e₂, …, e₇)` with its `𝟏 ⊕ 𝟑` block
structure, and — the open physics — transport to the three-strand Hecke
state space. Base ring ℚ; nothing archimedean.
-/

namespace QOU.MathlibExt.OctonionDerivations

open DerivationRankNullity

/-- The standard unit imaginary octonion `e₁` as a concrete vector. -/
def stdIm : Fin 8 → ℚ := ![0, 1, 0, 0, 0, 0, 0, 0]

/-- Left multiplication by `e₁`, as a ℚ-linear endomorphism of `𝕆`. -/
def Le : (Fin 8 → ℚ) →ₗ[ℚ] (Fin 8 → ℚ) := octMulₗ stdIm

@[simp] theorem Le_apply (x : Fin 8 → ℚ) : Le x = octMul stdIm x := rfl

/-- **`Le` is a complex structure**: left multiplication by the unit
imaginary `e₁` squares to `−id` on all of `𝕆` (the alternative-algebra
identity `u(ux) = u²x`, verified componentwise on the concrete
multiplication table). -/
theorem Le_sq_eq_neg_id : Le ∘ₗ Le = -LinearMap.id := by
  apply LinearMap.ext
  intro x
  funext k
  fin_cases k <;>
    simp [Le, stdIm, octMul, Fin.isValue]

/-- Zero-left-argument vanishing for the concrete product (helper). -/
theorem octMul_zero_left (v : Fin 8 → ℚ) : octMul 0 v = 0 := by
  funext k
  fin_cases k <;> simp [octMul]

/-- **The colour stabilizer acts ℂ-linearly on the octonions**: every
derivation fixing `e₁` commutes with the complex structure `Le`. Pure
Leibniz: `D(e₁·x) = D(e₁)·x + e₁·D(x) = e₁·D(x)`. -/
-- Ref: [dubois-violette-todorov2018] §2 (complex structure on 𝕆 = ℂ ⊕ ℂ³ and ℂ-linearity of su(3))
theorem su3_comp_Le_eq_Le_comp {D : Der𝕆} (hD : D ∈ su3 stdIm) :
    D.1 ∘ₗ Le = Le ∘ₗ D.1 := by
  have hleib : ∀ x y : Fin 8 → ℚ,
      D.1 (octMulₗ x y) = octMulₗ (D.1 x) y + octMulₗ x (D.1 y) :=
    mem_ker_leibnizDefect_iff.mp D.2
  have he : D.1 stdIm = 0 := mem_su3_iff.mp hD
  apply LinearMap.ext
  intro x
  have h := hleib stdIm x
  simp only [octMulₗ_apply] at h
  simp [Le, LinearMap.comp_apply, h, he, octMul_zero_left]

end QOU.MathlibExt.OctonionDerivations
