import QOU.Core.FlavourCentralPhase
import MathlibExt.Ribbon

/-!
# QOU.Core.ExteriorQuotientNormalisation — the twist fixes the braiding scalar on `Λ²V`, `Λ³W`

Bean `qou-x08k`.  Supports adopting the antisymmetric-quotient pins of
`docs/audits/2026-11-27-pin-exterior-quotients-proposal.md`.

In a balanced `R`-linear category, let `π : V ⊗ V ↠ L ≅ 𝟙` with `θ_V = s • 𝟙` and the braiding
acting on the quotient by a scalar, `β ≫ π = c • π`.  The balancing axiom together with
`θ_𝟙 = 𝟙` gives

* `exteriorSquare_balancing` — `(s²c² - 1) • π = 0`, so `c = ±s⁻¹` over a domain.

The antisymmetric choice is `c = -s⁻¹`.  For `W` with `π₃ : W^{⊗3} ↠ L ≅ 𝟙`, `θ_W = t • 𝟙` and
both adjacent crossings acting by `c`:

* `exteriorCube_balancing` — `(t³c⁶ - 1) • π₃ = 0`, so `(c²t)³ = 1`: the braiding scalar
  on `Λ³W` is fixed by the twist **only up to a cube root of unity**.  That ambiguity is
  exactly the `ℤ/3` phase of `QOU.FlavourCentralPhase`.

And a warning about the corpus normalisation:

* `hecke_halfTwist_forces_q_one` — with `θ_V = q^{1/2}` (`s² = q`) and the Hecke eigenvalue
  `c = -q⁻¹`, the balancing axiom forces `(q⁻¹ - 1) • 𝟙_𝟙 = 0`.  The two normalisations the
  corpus quotes cannot both hold at `q ≠ 1`; the consistent pair is `θ_V = s`, `c = -s⁻¹`.

Generic commutative ring `R`, sorry-free, no analytic or empirical input.
-/

namespace QOU.ExteriorQuotientNormalisation

open CategoryTheory MonoidalCategory BraidedCategory QOU.MathlibExt QOU.FlavourCentralPhase

universe v u

variable {R : Type*} [CommRing R] {C : Type u} [Category.{v} C] [MonoidalCategory C]
  [BraidedCategory C] [BalancedCategory C] [Preadditive C] [Linear R C]
  [MonoidalPreadditive C] [MonoidalLinear R C]

/-- The twist is trivial on any object isomorphic to the unit. -/
theorem twist_of_iso_unit {L : C} (e : L ≅ 𝟙_ C) : BalancedCategory.twist L = 𝟙 L := by
  have h := BalancedCategory.twist_naturality e.hom
  rw [BalancedCategory.twist_unit, Category.comp_id] at h
  calc BalancedCategory.twist L = BalancedCategory.twist L ≫ e.hom ≫ e.inv := by simp
    _ = e.hom ≫ e.inv := by rw [← Category.assoc, h]
    _ = 𝟙 L := e.hom_inv_id

/-- A scalar killing an epi onto an object `≅ 𝟙` kills `𝟙_𝟙`. -/
theorem smul_unit_eq_zero_of_epi {X L : C} (π : X ⟶ L) [Epi π] (e : L ≅ 𝟙_ C) (k : R)
    (h : k • π = 0) : k • 𝟙 (𝟙_ C) = 0 := by
  have h1 : π ≫ (k • 𝟙 L) = π ≫ 0 := by rw [Linear.comp_smul, Category.comp_id, h,
    Limits.comp_zero]
  have h2 : k • 𝟙 L = 0 := (cancel_epi π).1 h1
  calc k • 𝟙 (𝟙_ C) = e.inv ≫ (k • 𝟙 L) ≫ e.hom := by simp
    _ = 0 := by rw [h2]; simp

/-- **Balancing on `Λ²V`**: `(s²c² - 1) • π = 0`. -/
theorem exteriorSquare_balancing {V L : C} (π : V ⊗ V ⟶ L) (e : L ≅ 𝟙_ C) (s c : R)
    (hθ : BalancedCategory.twist V = s • 𝟙 V) (hβ : (β_ V V).hom ≫ π = c • π) :
    (s * s * (c * c) - 1) • π = 0 := by
  have h1 : BalancedCategory.twist (V ⊗ V) ≫ π = π := by
    rw [BalancedCategory.twist_naturality, twist_of_iso_unit e, Category.comp_id]
  rw [BalancedCategory.twist_tensor, hθ, smul_id_tensor_smul_id] at h1
  simp only [Category.assoc, Linear.smul_comp, Category.id_comp, Linear.comp_smul, hβ,
    smul_smul] at h1
  rw [sub_smul, one_smul, sub_eq_zero, ← h1]
  congr 1
  try ring

/-- The same, read on `End 𝟙`. -/
theorem exteriorSquare_balancing_unit {V L : C} (π : V ⊗ V ⟶ L) [Epi π] (e : L ≅ 𝟙_ C)
    (s c : R) (hθ : BalancedCategory.twist V = s • 𝟙 V) (hβ : (β_ V V).hom ≫ π = c • π) :
    (s * s * (c * c) - 1) • 𝟙 (𝟙_ C) = 0 :=
  smul_unit_eq_zero_of_epi π e _ (exteriorSquare_balancing π e s c hθ hβ)

/-- **The corpus normalisation is inconsistent away from `q = 1`.**  With `s * s = q`,
`q * qi = 1` and the Hecke eigenvalue `c = -qi`, balancing forces `(qi - 1) • 𝟙_𝟙 = 0`. -/
theorem hecke_halfTwist_forces_q_one {V L : C} (π : V ⊗ V ⟶ L) [Epi π] (e : L ≅ 𝟙_ C)
    (s q qi : R) (hs : s * s = q) (hq : q * qi = 1)
    (hθ : BalancedCategory.twist V = s • 𝟙 V) (hβ : (β_ V V).hom ≫ π = (-qi) • π) :
    (qi - 1) • 𝟙 (𝟙_ C) = 0 := by
  have h := exteriorSquare_balancing_unit π e s (-qi) hθ hβ
  have : s * s * (-qi * -qi) - 1 = qi - 1 := by
    rw [hs, neg_mul_neg, ← mul_assoc, hq, one_mul]
  rwa [this] at h

/-- The antisymmetric normalisation `c = -s⁻¹` is consistent with balancing. -/
theorem antisym_normalisation_consistent (s si : R) (hs : s * si = 1) :
    s * s * (-si * -si) - 1 = 0 := by
  rw [neg_mul_neg]
  linear_combination (s * si + 1) * hs

/-- Tensoring a scaled morphism with a scaled identity. -/
theorem smul_tensor_smul_id {X : C} (a b : R) (f : X ⟶ X) (Z : C) :
    ((a • f) ⊗ₘ (b • 𝟙 Z)) = (a * b) • (f ▷ Z) := by
  rw [tensorHom_def, MonoidalLinear.smul_whiskerRight, MonoidalLinear.whiskerLeft_smul,
    Linear.smul_comp, Linear.comp_smul, smul_smul, whiskerLeft_id, Category.comp_id]

/-- **Balancing on `Λ³W`**: if `θ_W = t • 𝟙` and both adjacent crossings act on
`π₃ : (W ⊗ W) ⊗ W ↠ L ≅ 𝟙` by `c`, then `(t³c⁶ - 1) • π₃ = 0`. -/
theorem exteriorCube_balancing {W L : C} (π : (W ⊗ W) ⊗ W ⟶ L) (e : L ≅ 𝟙_ C) (t c : R)
    (hθ : BalancedCategory.twist W = t • 𝟙 W)
    (h₁ : (β_ W W).hom ▷ W ≫ π = c • π)
    (h₂ : (α_ W W W).hom ≫ W ◁ (β_ W W).hom ≫ (α_ W W W).inv ≫ π = c • π) :
    (t * t * t * (c * c * c * c * c * c) - 1) • π = 0 := by
  have h1 : BalancedCategory.twist ((W ⊗ W) ⊗ W) ≫ π = π := by
    rw [BalancedCategory.twist_naturality, twist_of_iso_unit e, Category.comp_id]
  rw [BalancedCategory.twist_tensor, BalancedCategory.twist_tensor, hθ,
    smul_id_tensor_smul_id] at h1
  simp only [Linear.comp_smul, Category.comp_id] at h1
  rw [smul_tensor_smul_id, braiding_tensor_left_hom, braiding_tensor_right_hom] at h1
  simp only [Category.assoc, Linear.smul_comp, Linear.comp_smul, comp_whiskerRight,
    Iso.hom_inv_id_assoc, h₁, h₂, smul_smul] at h1
  rw [sub_smul, one_smul, sub_eq_zero, ← h1]
  congr 1
  try ring

/-- The same, read on `End 𝟙`: `(c²t)³ = 1` there. -/
theorem exteriorCube_balancing_unit {W L : C} (π : (W ⊗ W) ⊗ W ⟶ L) [Epi π] (e : L ≅ 𝟙_ C)
    (t c : R) (hθ : BalancedCategory.twist W = t • 𝟙 W)
    (h₁ : (β_ W W).hom ▷ W ≫ π = c • π)
    (h₂ : (α_ W W W).hom ≫ W ◁ (β_ W W).hom ≫ (α_ W W W).inv ≫ π = c • π) :
    ((c * c * t) ^ 3 - 1) • 𝟙 (𝟙_ C) = 0 := by
  have h := smul_unit_eq_zero_of_epi π e _ (exteriorCube_balancing π e t c hθ h₁ h₂)
  rwa [show t * t * t * (c * c * c * c * c * c) - 1 = (c * c * t) ^ 3 - 1 by ring] at h

end QOU.ExteriorQuotientNormalisation
