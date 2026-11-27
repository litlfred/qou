import MathlibExt.Ribbon
import Mathlib.CategoryTheory.Monoidal.Linear
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# QOU.Core.ExteriorAntisymmetryDerivation — what the aether fixes about `Λ²V` and `Λ³W`

Bean `qou-x08k`, owner request 2026-11-27: *derive* the exterior-quotient antisymmetry instead
of assuming it.

All statements are over a generic commutative ring `R`, in a balanced (resp. ribbon) `R`-linear
category.  Sorry-free, with no analytic or empirical input.

## `V`: the twist normalisation is forced by the Hecke eigenvalue

* `quotient_balancing` — for `π : X ⊗ X ↠ L`, `L ≅ Y`, `θ_X = s • 𝟙`, `θ_Y = u • 𝟙` and
  `β ≫ π = c • π`, balancing gives `(s²c² − u) • π = 0`.  This is the single identity behind
  every statement below.
* `hecke_forces_twist_sq` — if the braiding acts on `Λ²V ≅ 𝟙` by the Hecke value `−q⁻¹`, then
  `(s² − q²) • 𝟙_𝟙 = 0`.  So the twist is `θ_V = ±q`, not `q^{1/2}`.  This is derived, not
  chosen; with the antisymmetric reading `c = −s⁻¹` the sign is `s = q`.

## `W`: the cube-root ambiguity is fixed by the dual

The cube `Λ³W ≅ 𝟙` gives only `(c²t)³ = 1`.  The ambiguity is **not** a grading choice:

* `rebraid_invariant` — re-braiding by a `ℤ/3` bicharacter multiplies both `c` and `t` by the same
  cube root `ω`, and `(ωc)²(ωt) = c²t`.  So a grading, or the grouplikes that define one, cannot
  move `c²t`, and so cannot be the source of the root.

What fixes it is the square `Λ²W` read as the dual `Wᘁ`, as at the fibre (`W ⊗ Λ²W → Λ³W ≅ 𝟙`
is the wedge pairing):

* `rightAdjointMate_smul_id` — `(t • 𝟙 X)ᘁ = t • 𝟙 Xᘁ`.
* `twist_dual_of_scalar` — in a ribbon category `θ_X = t • 𝟙` gives `θ_{Xᘁ} = t • 𝟙`.
* `flavour_root_fixed_by_dual` — if `π₂ : W ⊗ W ↠ L₂ ≅ Wᘁ` and the braiding acts on it by `c`,
  then `t • (c²t − 1) • π₂ = 0`; with `t` a unit, `(c²t − 1) • 𝟙_{L₂} = 0`.

So the root is `c²t = 1`, the Drinfeld–Jimbo normalisation.  It comes from the ribbon axiom
`θ_{Xᘁ} = (θ_X)ᘁ` together with `Λ²W ≅ Wᘁ`.  It does not come from a `ℤ/3` grading.

## Honest scope

* `Λ²W ≅ Wᘁ` is a hypothesis here.  It holds at the fibre whenever the wedge pairing
  `W ⊗ Λ²W → Λ³W` is perfect.  It is not derived from the current axioms.
* The Hecke relation `(σ − q)(σ + q⁻¹) = 0` on all of `V ⊗ V` is **not** derived.  Balancing
  constrains only the scalar on the summand `≅ 𝟙`; it says nothing about the scalar on `S²V`.
  See `docs/audits/2026-11-27-deriving-exterior-antisymmetry.md` and bean `qou-x09d`.
-/

set_option linter.unusedSectionVars false

namespace QOU.ExteriorAntisymmetryDerivation

open CategoryTheory MonoidalCategory BraidedCategory QOU.MathlibExt

universe v u

section Balanced

variable {R : Type*} [CommRing R] {C : Type u} [Category.{v} C] [MonoidalCategory C]
  [BraidedCategory C] [BalancedCategory C] [Preadditive C] [Linear R C]
  [MonoidalPreadditive C] [MonoidalLinear R C]

/-- Tensor of two scaled identities. -/
theorem smul_id_tensor_smul_id' (a b : R) (X Y : C) :
    ((a • 𝟙 X) ⊗ₘ (b • 𝟙 Y)) = (a * b) • 𝟙 (X ⊗ Y) := by
  rw [tensorHom_def, MonoidalLinear.smul_whiskerRight, MonoidalLinear.whiskerLeft_smul,
    Linear.smul_comp, Linear.comp_smul, smul_smul, id_whiskerRight, whiskerLeft_id,
    Category.id_comp, mul_comm]

/-- **Balancing on a braided quotient.**  For `π : X ⊗ X ⟶ L` with `L ≅ Y`, `θ_X = s • 𝟙`,
`θ_Y = u • 𝟙` and the braiding acting on `π` by `c`: `(s²c² − u) • π = 0`. -/
theorem quotient_balancing {X L Y : C} (π : X ⊗ X ⟶ L) (e : L ≅ Y) (s u c : R)
    (hθX : BalancedCategory.twist X = s • 𝟙 X) (hθY : BalancedCategory.twist Y = u • 𝟙 Y)
    (hβ : (β_ X X).hom ≫ π = c • π) :
    (s * s * (c * c) - u) • π = 0 := by
  have hθL : BalancedCategory.twist L = u • 𝟙 L := by
    have h := BalancedCategory.twist_naturality e.hom
    rw [hθY] at h
    calc BalancedCategory.twist L = BalancedCategory.twist L ≫ e.hom ≫ e.inv := by simp
      _ = (e.hom ≫ (u • 𝟙 Y)) ≫ e.inv := by rw [← Category.assoc, h]
      _ = u • 𝟙 L := by simp
  have h1 : BalancedCategory.twist (X ⊗ X) ≫ π = u • π := by
    rw [BalancedCategory.twist_naturality, hθL, Linear.comp_smul, Category.comp_id]
  rw [BalancedCategory.twist_tensor, hθX, smul_id_tensor_smul_id'] at h1
  simp only [Category.assoc, Linear.smul_comp, Category.id_comp, Linear.comp_smul, hβ,
    smul_smul] at h1
  rw [sub_smul, sub_eq_zero, ← h1]

/-- The twist is trivial on an object isomorphic to `𝟙`. -/
theorem twist_eq_one_of_iso_unit {L : C} (e : L ≅ 𝟙_ C) :
    BalancedCategory.twist L = (1 : R) • 𝟙 L := by
  have h := BalancedCategory.twist_naturality e.hom
  rw [BalancedCategory.twist_unit, Category.comp_id] at h
  rw [one_smul]
  calc BalancedCategory.twist L = BalancedCategory.twist L ≫ e.hom ≫ e.inv := by simp
    _ = e.hom ≫ e.inv := by rw [← Category.assoc, h]
    _ = 𝟙 L := e.hom_inv_id

/-- A scalar killing an epi kills the identity of its target. -/
theorem smul_id_eq_zero_of_epi {X L : C} (π : X ⟶ L) [Epi π] (k : R) (h : k • π = 0) :
    k • 𝟙 L = 0 := by
  apply (cancel_epi π).1
  rw [Linear.comp_smul, Category.comp_id, h, Limits.comp_zero]

/-- **The Hecke eigenvalue forces `θ_V = ±q`.**  If the braiding acts on `π : V ⊗ V ↠ L ≅ 𝟙` by
`−q⁻¹` and `θ_V = s • 𝟙`, then `(s² − q²) • 𝟙_𝟙 = 0`.  Not `q^{1/2}`. -/
theorem hecke_forces_twist_sq {V L : C} (π : V ⊗ V ⟶ L) [Epi π] (e : L ≅ 𝟙_ C)
    (s q qi : R) (hq : q * qi = 1)
    (hθ : BalancedCategory.twist V = s • 𝟙 V) (hβ : (β_ V V).hom ≫ π = (-qi) • π) :
    (s * s - q * q) • 𝟙 (𝟙_ C) = 0 := by
  have h := quotient_balancing π e s 1 (-qi) hθ
    (by rw [BalancedCategory.twist_unit, one_smul]) hβ
  have h2 : (s * s * (-qi * -qi) - 1) • 𝟙 L = 0 := smul_id_eq_zero_of_epi π _ h
  have h3 : (s * s * (-qi * -qi) - 1) • 𝟙 (𝟙_ C) = 0 := by
    calc (s * s * (-qi * -qi) - 1) • 𝟙 (𝟙_ C)
        = e.inv ≫ ((s * s * (-qi * -qi) - 1) • 𝟙 L) ≫ e.hom := by simp
      _ = 0 := by rw [h2]; simp
  have : s * s - q * q = (q * q) * (s * s * (-qi * -qi) - 1) := by
    linear_combination (-(s * s) * (q * qi + 1)) * hq
  rw [this, ← smul_smul, h3, smul_zero]

/-- **Re-braiding by a `ℤ/3` bicharacter does not move `c²t`.**  Re-braiding multiplies the
braiding on `W ⊗ W` and the twist of `W` by the same `ω` (`θ'_X = χ(g,g) θ_X`), and `ω³ = 1`. -/
theorem rebraid_invariant (ω c t : R) (hω : ω ^ 3 = 1) :
    (ω * c) * (ω * c) * (ω * t) = c * c * t := by
  linear_combination (c * c * t) * hω

end Balanced

section Ribbon

variable {R : Type*} [CommRing R] {C : Type u} [Category.{v} C] [MonoidalCategory C]
  [BraidedCategory C] [RightRigidCategory C] [RibbonCategory C] [Preadditive C] [Linear R C]
  [MonoidalPreadditive C] [MonoidalLinear R C]

/-- The right adjoint mate of a scaled identity. -/
theorem rightAdjointMate_smul_id (X : C) (t : R) : (t • 𝟙 X)ᘁ = t • 𝟙 Xᘁ := by
  have h : (t • 𝟙 X)ᘁ = t • (𝟙 X)ᘁ := by
    simp only [rightAdjointMate, MonoidalLinear.whiskerLeft_smul,
      MonoidalLinear.smul_whiskerRight, Linear.smul_comp, Linear.comp_smul]
  rw [h, rightAdjointMate_id]

/-- **Ribbon:** a scalar twist on `X` gives the same scalar twist on `Xᘁ`. -/
theorem twist_dual_of_scalar (X : C) (t : R) (hθ : BalancedCategory.twist X = t • 𝟙 X) :
    BalancedCategory.twist Xᘁ = t • 𝟙 Xᘁ := by
  rw [RibbonCategory.twist_dual, hθ, rightAdjointMate_smul_id]

/-- **The dual fixes the cube root.**  If `π₂ : W ⊗ W ⟶ L₂` with `L₂ ≅ Wᘁ`, `θ_W = t • 𝟙` and the
braiding acts on `π₂` by `c`, then `t • ((c²t − 1) • π₂) = 0`. -/
theorem flavour_root_fixed_by_dual {W L : C} (π : W ⊗ W ⟶ L) (e : L ≅ Wᘁ) (t c : R)
    (hθ : BalancedCategory.twist W = t • 𝟙 W) (hβ : (β_ W W).hom ≫ π = c • π) :
    t • ((c * c * t - 1) • π) = 0 := by
  have h := quotient_balancing π e t t c hθ (twist_dual_of_scalar W t hθ) hβ
  rw [smul_smul]
  rw [show t * (c * c * t - 1) = t * t * (c * c) - t by ring]
  exact h

/-- With `t` a unit: `(c²t − 1) • 𝟙_{L₂} = 0`, the Drinfeld–Jimbo normalisation `c²t = 1`. -/
theorem flavour_root_eq_one {W L : C} (π : W ⊗ W ⟶ L) [Epi π] (e : L ≅ Wᘁ) (t ti c : R)
    (ht : ti * t = 1)
    (hθ : BalancedCategory.twist W = t • 𝟙 W) (hβ : (β_ W W).hom ≫ π = c • π) :
    (c * c * t - 1) • 𝟙 L = 0 := by
  have h := flavour_root_fixed_by_dual π e t c hθ hβ
  have h' : (c * c * t - 1) • π = 0 := by
    have := congrArg (ti • ·) h
    simp only [smul_smul, smul_zero] at this
    rwa [← mul_assoc, ht, one_mul] at this
  exact smul_id_eq_zero_of_epi π _ h'

end Ribbon

end QOU.ExteriorAntisymmetryDerivation
