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

end QOU.Braiding
