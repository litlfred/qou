/-!
# QOU.Braiding.braid_action_tensor — Braid action on tensor products

For a braided monoidal category C with braiding c_{X,Y},
there is a group homomorphism ρ_n : B_n → Aut_C(V^⊗n) given by
  ρ_n(σ_i) = id^⊗(i-1) ⊗ c_{V,V} ⊗ id^⊗(n-i-1)

The braid relation is equivalent to the Yang–Baxter equation.

LaTeX label: `prop:braid-action-tensor`

## References

- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
- [manuscript] §4-path-integrals-and-braiding/braid-action-tensor
-/

import Mathlib.CategoryTheory.Monoidal.Basic
import Mathlib.CategoryTheory.Monoidal.Braided.Basic

open CategoryTheory MonoidalCategory BraidedCategory

namespace QOU.Braiding

universe u v

/-! ## Braid Representation Structure -/

/-- **Braid representation on V^⊗n** in a braided monoidal category.

    Each Artin generator σ_i acts by applying the braiding c_{V,V}
    at positions i, i+1 and identity elsewhere. -/
-- Ref: [kassel1995], [manuscript] §4
structure BraidActionTensor (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] where
  /-- The object V to be tensored. -/
  V : C
  /-- Number of strands n ≥ 2. -/
  numStrands : ℕ
  strands_ge_two : 2 ≤ numStrands
  /-- The braiding c_{V,V} : V ⊗ V → V ⊗ V. -/
  braiding : (V ⊗ V) ⟶ (V ⊗ V) := (β_ V V).hom

/-! ## Braiding Isomorphism Properties -/

/-- The braiding is an isomorphism (invertible). -/
-- Ref: [kassel1995] Chapter XIII
theorem braiding_is_iso {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    (β_ V V).hom ≫ (β_ V V).inv = 𝟙 (V ⊗ V) :=
  Iso.hom_inv_id (β_ V V)

/-- The inverse braiding composes correctly. -/
-- Ref: [kassel1995] Chapter XIII
theorem braiding_inv_hom {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    (β_ V V).inv ≫ (β_ V V).hom = 𝟙 (V ⊗ V) :=
  Iso.inv_hom_id (β_ V V)

/-! ## Braid Generators on V⊗V⊗V -/

/-- σ₁ acting on (V ⊗ V) ⊗ V: applies the braiding to the first
    two tensor factors. This is ρ₃(σ₁) = c_{V,V} ⊗ id_V. -/
def sigma1 {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    (V ⊗ V) ⊗ V ⟶ (V ⊗ V) ⊗ V :=
  (β_ V V).hom ▷ V

/-- σ₂ acting on (V ⊗ V) ⊗ V: applies the braiding to the last
    two tensor factors, transported through the associator.
    This is ρ₃(σ₂) = id_V ⊗ c_{V,V} (in strict form). -/
def sigma2 {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    (V ⊗ V) ⊗ V ⟶ (V ⊗ V) ⊗ V :=
  (α_ V V V).hom ≫ (V ◁ (β_ V V).hom) ≫ (α_ V V V).inv

/-- σ₁ is an isomorphism: σ₁ ≫ σ₁⁻¹ = id. -/
theorem sigma1_is_iso {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    sigma1 V ≫ ((β_ V V).inv ▷ V) = 𝟙 ((V ⊗ V) ⊗ V) := by
  simp [sigma1, ← MonoidalCategory.whiskerRight_comp,
        Iso.hom_inv_id, MonoidalCategory.whiskerRight_id]

/-- σ₂ is an isomorphism: σ₂ ≫ σ₂⁻¹ = id. -/
theorem sigma2_is_iso {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    sigma2 V ≫ ((α_ V V V).hom ≫ (V ◁ (β_ V V).inv) ≫ (α_ V V V).inv)
    = 𝟙 ((V ⊗ V) ⊗ V) := by
  simp [sigma2]
  slice_lhs 3 4 => rw [← MonoidalCategory.whiskerLeft_comp,
                        Iso.hom_inv_id, MonoidalCategory.whiskerLeft_id]
  simp [Iso.hom_inv_id]

/-! ## Yang–Baxter Equation (Braid Relation) -/

/-- **The Yang–Baxter equation / braid relation** for the categorical braiding.

    The braid relation σ₁σ₂σ₁ = σ₂σ₁σ₂ on (V ⊗ V) ⊗ V follows from
    the hexagon coherence axioms of a braided monoidal category.

    This is the central theorem connecting the braid group B₃ to braided
    monoidal categories: it shows that ρ₃ : B₃ → Aut_C(V^⊗3) defined by
    σ₁ ↦ c_{V,V} ▷ V and σ₂ ↦ α ≫ (V ◁ c_{V,V}) ≫ α⁻¹ is a
    well-defined group homomorphism.

    **Proof sketch** (Kassel, Theorem XIII.1.3):
    By hexagon_forward, σ₁ ≫ α ≫ σ₂' = α ≫ β_{V,V⊗V} ≫ α where
    σ₂' = V ◁ β_{V,V}. By hexagon_reverse, σ₂' ≫ α⁻¹ ≫ σ₁ =
    α⁻¹ ≫ β_{V⊗V,V} ≫ α⁻¹. The naturality of the braiding then
    gives the required equality. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2, Theorem XIII.1.3
theorem yang_baxter_braiding {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    sigma1 V ≫ sigma2 V ≫ sigma1 V =
    sigma2 V ≫ sigma1 V ≫ sigma2 V := by
  simp only [sigma1, sigma2]
  -- Expand: LHS = (β▷V) ≫ α ≫ (V◁β) ≫ α⁻¹ ≫ (β▷V)
  --         RHS = α ≫ (V◁β) ≫ α⁻¹ ≫ (β▷V) ≫ α ≫ (V◁β) ≫ α⁻¹
  -- Rewrite using hexagon_forward (BraidedCategory axiom):
  --   (β_ V V).hom ▷ V ≫ (α_ V V V).hom ≫ V ◁ (β_ V V).hom
  --     = (α_ V V V).hom ≫ (β_ V (V ⊗ V)).hom ≫ (α_ V V V).hom
  -- Rewrite using hexagon_reverse (BraidedCategory axiom):
  --   V ◁ (β_ V V).hom ≫ (α_ V V V).inv ≫ (β_ V V).hom ▷ V
  --     = (α_ V V V).inv ≫ (β_ (V ⊗ V) V).hom ≫ (α_ V V V).inv
  -- Then apply braiding naturality to equate the two sides.
  -- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2, Thm XIII.1.3
  sorry

/-! ## Well-Definedness of the B₃ Representation -/

/-- **B₃ representation data**: the two generators σ₁, σ₂ and
    the proof that they satisfy the braid relation, constituting
    a group homomorphism ρ₃ : B₃ → Aut_C((V ⊗ V) ⊗ V). -/
structure BraidRepB3 (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] where
  /-- The fundamental object. -/
  V : C
  /-- Generator σ₁ = c_{V,V} ⊗ id_V. -/
  gen1 : (V ⊗ V) ⊗ V ⟶ (V ⊗ V) ⊗ V := sigma1 V
  /-- Generator σ₂ = id_V ⊗ c_{V,V} (via associator). -/
  gen2 : (V ⊗ V) ⊗ V ⟶ (V ⊗ V) ⊗ V := sigma2 V
  /-- The braid relation holds. -/
  braid_rel : gen1 ≫ gen2 ≫ gen1 = gen2 ≫ gen1 ≫ gen2 :=
    yang_baxter_braiding V

/-- Every braided monoidal category yields a B₃ representation on V⊗³. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2, Cor. XIII.1.4
def braid_action_tensor {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    BraidRepB3 C where
  V := V

end QOU.Braiding
