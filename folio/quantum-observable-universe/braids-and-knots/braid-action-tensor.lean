import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Monoidal.Braided.Basic


/-!
# QOU.Braiding.braid_action_tensor — Braid action on tensor products

For a braided monoidal category C with braiding c_{X,Y},
there is a group homomorphism ρ_n : B_n → Aut_C(V^⊗n) given by
  ρ_n(σ_i) = id^⊗(i-1) ⊗ c_{V,V} ⊗ id^⊗(n-i-1)

The braid relation is equivalent to the Yang–Baxter equation.

LaTeX label: `prop:braid-action-tensor`

## References

- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
- [leitner2026] §4-path-integrals-and-braiding/braid-action-tensor
-/

open CategoryTheory MonoidalCategory BraidedCategory

namespace QOU.Braiding

universe u v

/-! ## Braid Representation Structure -/

/-- **Braid representation on V^⊗n** in a braided monoidal category.

    Each Artin generator σ_i acts by applying the braiding c_{V,V}
    at positions i, i+1 and identity elsewhere. -/
-- Ref: [kassel1995], [leitner2026] §4
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
  simp [sigma1, ← MonoidalCategory.comp_whiskerRight, Iso.hom_inv_id]

/-- σ₂ is an isomorphism: σ₂ ≫ σ₂⁻¹ = id. -/
theorem sigma2_is_iso {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    sigma2 V ≫ ((α_ V V V).hom ≫ (V ◁ (β_ V V).inv) ≫ (α_ V V V).inv)
    = 𝟙 ((V ⊗ V) ⊗ V) := by
  simp only [sigma2, Category.assoc]
  -- After simp: α ≫ (V◁β) ≫ α⁻¹ ≫ α ≫ (V◁β⁻¹) ≫ α⁻¹ = id
  -- Cancel α⁻¹ ≫ α = id in the middle:
  rw [Iso.inv_hom_id_assoc]
  -- Now: α ≫ (V◁β) ≫ (V◁β⁻¹) ≫ α⁻¹ = id.
  -- `rw [← whiskerLeft_comp]` does NOT apply here: `≫` is right-associated,
  -- so the two whiskers are `V◁β ≫ (V◁β⁻¹ ≫ α⁻¹)` and the pattern
  -- `?W ◁ ?f ≫ ?W ◁ ?g` is not a syntactic subterm.  `slice_lhs` re-brackets
  -- the named segment first, which is what it exists for (AGENTS.md §5).
  slice_lhs 2 3 => rw [← MonoidalCategory.whiskerLeft_comp, Iso.hom_inv_id,
                       MonoidalCategory.whiskerLeft_id]
  -- Now: α ≫ α⁻¹ = id
  simp

/-! ## Yang–Baxter Equation (Braid Relation) -/

/-- **Lemma (hexagon reduction).**
    σ₁ ≫ σ₂ = α ≫ β_{V,V⊗V}.

    Proof: from hexagon_forward, (β▷V) ≫ α ≫ (V◁β) = α ≫ β_{V,V⊗V} ≫ α.
    Post-composing with α⁻¹ and using α ≫ α⁻¹ = id gives the result. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2, Ch. XIII
private theorem sigma12_eq_alpha_braiding {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    sigma1 V ≫ sigma2 V = (α_ V V V).hom ≫ (β_ V (V ⊗ V)).hom := by
  simp only [sigma1, sigma2]
  -- Goal: (β_ V V).hom ▷ V ≫ (α_ V V V).hom ≫ V ◁ (β_ V V).hom ≫ (α_ V V V).inv
  --     = (α_ V V V).hom ≫ (β_ V (V ⊗ V)).hom
  -- Uses BraidedCategory.hexagon_forward V V V (with X=Y=Z=V):
  --   (α_ V V V).hom ≫ (β_ V (V ⊗ V)).hom ≫ (α_ V V V).hom
  --   = ((β_ V V).hom ▷ V) ≫ (α_ V V V).hom ≫ (V ◁ (β_ V V).hom)
  -- Post-compose both sides with (α_ V V V).inv and cancel α.hom ≫ α.inv = id.
  -- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
  -- Mathlib lemma: BraidedCategory.hexagon_forward
  have hex := BraidedCategory.hexagon_forward (C := C) V V V
  -- hex : (α_ V V V).hom ≫ (β_ V (V ⊗ V)).hom ≫ (α_ V V V).hom
  --     = (β_ V V).hom ▷ V ≫ (α_ V V V).hom ≫ V ◁ (β_ V V).hom
  -- From hex.symm: LHS first 3 terms = RHS with extra α at end
  -- We need: LHS_3_terms ≫ α⁻¹ = α ≫ β_{V,V⊗V}
  -- Same bracketing point as in `sigma2_is_iso`: `hex`'s right-hand side is
  -- the FIRST THREE factors of the goal's left-hand side, but the goal is
  -- `X ≫ (Y ≫ (Z ≫ α⁻¹))`, so `rw [← hex]` finds no `X ≫ (Y ≫ Z)` to match.
  slice_lhs 1 3 => rw [← hex]
  -- Goal: (α_ V V V).hom ≫ (β_ V (V ⊗ V)).hom ≫ (α_ V V V).hom ≫ (α_ V V V).inv
  --     = (α_ V V V).hom ≫ (β_ V (V ⊗ V)).hom
  simp

/-- **Lemma (braiding naturality).**
    β_{V,V⊗V} ≫ (β_{V,V} ▷ V) = (V ◁ β_{V,V}) ≫ β_{V,V⊗V}.

    This is the naturality of the braiding in the second variable,
    applied to the endomorphism β_{V,V} : V⊗V → V⊗V. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2, Ch. XIII
private theorem braiding_nat_sigma {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    (β_ V (V ⊗ V)).hom ≫ ((β_ V V).hom ▷ V) =
    (V ◁ (β_ V V).hom) ≫ (β_ V (V ⊗ V)).hom := by
  -- Uses BraidedCategory.braiding_naturality_right.
  -- Naturality of β in the second variable with f = (β_ V V).hom:
  --   (V ◁ f) ≫ (β_ V (V ⊗ V)).hom = (β_ V (V ⊗ V)).hom ≫ (f ▷ V)
  -- which is exactly our goal read right-to-left.
  -- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
  -- Mathlib lemma: BraidedCategory.braiding_naturality_right
  exact (BraidedCategory.braiding_naturality_right V ((β_ V V).hom)).symm

/-- **Lemma (σ₂–α interchange).**
    σ₂ ≫ α = α ≫ (V ◁ β_{V,V}).

    Proof: expand σ₂ = α ≫ (V◁β) ≫ α⁻¹, then
    (α ≫ (V◁β) ≫ α⁻¹) ≫ α = α ≫ (V◁β) ≫ (α⁻¹ ≫ α) = α ≫ (V◁β). -/
private theorem sigma2_alpha_interchange {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    sigma2 V ≫ (α_ V V V).hom = (α_ V V V).hom ≫ (V ◁ (β_ V V).hom) := by
  simp only [sigma2, Category.assoc]
  -- (α ≫ (V◁β) ≫ α⁻¹) ≫ α = α ≫ (V◁β) ≫ (α⁻¹ ≫ α) = α ≫ (V◁β)
  rw [Iso.inv_hom_id, Category.comp_id]

/-- **The Yang–Baxter equation / braid relation** for the categorical braiding.

    **Theorem** (Kassel, Theorem XIII.1.3).
    σ₁σ₂σ₁ = σ₂σ₁σ₂ as endomorphisms of (V ⊗ V) ⊗ V.

    This is the central result connecting B₃ to braided monoidal categories:
    it shows that ρ₃ : B₃ → Aut_C(V^⊗3) is a well-defined group homomorphism.

    **Proof** (diagram chase using three lemmas):
    1. `sigma12_eq_alpha_braiding`: σ₁ ≫ σ₂ = α ≫ β_{V,V⊗V}  (hexagon)
    2. `braiding_nat_sigma`: β_{V,V⊗V} ≫ σ₁ = (V◁β) ≫ β_{V,V⊗V}  (naturality)
    3. `sigma2_alpha_interchange`: σ₂ ≫ α = α ≫ (V◁β)  (definition) -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2, Theorem XIII.1.3
theorem yang_baxter_braiding {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    sigma1 V ≫ sigma2 V ≫ sigma1 V =
    sigma2 V ≫ sigma1 V ≫ sigma2 V := by
  -- Abbreviations for the three lemmas:
  have key := sigma12_eq_alpha_braiding V
  have nat := braiding_nat_sigma V
  have s2a := sigma2_alpha_interchange V
  -- Both sides are endomorphisms of (V ⊗ V) ⊗ V.
  -- Note: ≫ is right-associative, so a ≫ b ≫ c = a ≫ (b ≫ c).
  -- We prove LHS = RHS by:
  --   σ₁(σ₂σ₁) = (σ₁σ₂)σ₁ = (α·β_{V,V⊗V})σ₁ = α·(β_{V,V⊗V}·σ₁)
  --            = α·((V◁β)·β_{V,V⊗V}) = (α·(V◁β))·β_{V,V⊗V}
  --            = (σ₂·α)·β_{V,V⊗V} = σ₂·(α·β_{V,V⊗V}) = σ₂(σ₁σ₂)
  calc sigma1 V ≫ (sigma2 V ≫ sigma1 V)
      _ = (sigma1 V ≫ sigma2 V) ≫ sigma1 V := by
          rw [← Category.assoc]
      _ = ((α_ V V V).hom ≫ (β_ V (V ⊗ V)).hom) ≫ sigma1 V := by
          rw [key]
      _ = ((α_ V V V).hom ≫ (β_ V (V ⊗ V)).hom) ≫ ((β_ V V).hom ▷ V) := by
          rfl  -- sigma1 V = (β_ V V).hom ▷ V by definition
      _ = (α_ V V V).hom ≫ ((β_ V (V ⊗ V)).hom ≫ ((β_ V V).hom ▷ V)) := by
          rw [Category.assoc]
      _ = (α_ V V V).hom ≫ ((V ◁ (β_ V V).hom) ≫ (β_ V (V ⊗ V)).hom) := by
          rw [nat]
      _ = ((α_ V V V).hom ≫ (V ◁ (β_ V V).hom)) ≫ (β_ V (V ⊗ V)).hom := by
          rw [← Category.assoc]
      _ = (sigma2 V ≫ (α_ V V V).hom) ≫ (β_ V (V ⊗ V)).hom := by
          rw [← s2a]
      _ = sigma2 V ≫ ((α_ V V V).hom ≫ (β_ V (V ⊗ V)).hom) := by
          rw [Category.assoc]
      _ = sigma2 V ≫ (sigma1 V ≫ sigma2 V) := by
          rw [← key]

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
  braid_rel : gen1 ≫ gen2 ≫ gen1 = gen2 ≫ gen1 ≫ gen2

/-- Every braided monoidal category yields a B₃ representation on V⊗³. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2, Cor. XIII.1.4
def braid_action_tensor {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    BraidRepB3 C where
  V := V
  gen1 := sigma1 V
  gen2 := sigma2 V
  braid_rel := yang_baxter_braiding V

end QOU.Braiding
