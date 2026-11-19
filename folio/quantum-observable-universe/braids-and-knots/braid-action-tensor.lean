import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Monoidal.Braided.Basic
import Mathlib.CategoryTheory.Endomorphism
import Mathlib.GroupTheory.PresentedGroup


/-!
# QOU.Braiding.braid_action_tensor — Braid action on tensor products

For a braided monoidal category `C` with braiding `c_{X,Y}`,
there is for every object `V : C` and every `n ≥ 2` a group homomorphism
`ρ_n : B_n →* Aut_C(V^⊗n)` given on the Artin generators `σ_i` (`1 ≤ i ≤ n - 1`) by
`ρ_n(σ_i) = id^⊗(i-1) ⊗ c_{V,V} ⊗ id^⊗(n-i-1)`.

The adjacent braid relation `ρ_n(σ_i) ρ_n(σ_{i+1}) ρ_n(σ_i) = ρ_n(σ_{i+1}) ρ_n(σ_i) ρ_n(σ_{i+1})`
is mathematically equivalent (`↔`) to the Yang–Baxter equation for `c_{V,V}`,
and far-commutativity `ρ_n(σ_i) ρ_n(σ_j) = ρ_n(σ_j) ρ_n(σ_i)` (`|i - j| ≥ 2`)
holds by the monoidal interchange law on disjoint tensor factor pairs.

LaTeX label: `prop:braid-action-tensor`

## References

- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
- [leitner2026] §4-path-integrals-and-braiding/braid-action-tensor
-/

open CategoryTheory MonoidalCategory BraidedCategory

namespace QOU.Braiding

universe u v

/-! ## Braiding Isomorphism Properties -/

/-- The braiding is an isomorphism (right inverse). -/
-- Ref: [kassel1995] Chapter XIII
theorem braiding_is_iso {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    (β_ V V).hom ≫ (β_ V V).inv = 𝟙 (V ⊗ V) :=
  Iso.hom_inv_id (β_ V V)

/-- The inverse braiding composes to the identity on the left (left inverse). -/
-- Ref: [kassel1995] Chapter XIII
theorem braiding_inv_hom {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    (β_ V V).inv ≫ (β_ V V).hom = 𝟙 (V ⊗ V) :=
  Iso.inv_hom_id (β_ V V)

/-! ## Braid Generators on `V ⊗ V ⊗ V` and Two-Sided Isomorphisms -/

/-- `σ₁(c)` acting on `(V ⊗ V) ⊗ V` for any endomorphism `c : V ⊗ V ⟶ V ⊗ V`:
    applies `c` to the first two tensor factors (`c ⊗ id_V`). -/
def sigma1Of {C : Type u} [Category.{v} C] [MonoidalCategory C]
    (V : C) (c : (V ⊗ V) ⟶ (V ⊗ V)) :
    (V ⊗ V) ⊗ V ⟶ (V ⊗ V) ⊗ V :=
  c ▷ V

/-- `σ₂(c)` acting on `(V ⊗ V) ⊗ V` for any endomorphism `c : V ⊗ V ⟶ V ⊗ V`:
    applies `c` to the last two tensor factors (`id_V ⊗ c`), transported through
    the associator `α_{V,V,V}`. -/
def sigma2Of {C : Type u} [Category.{v} C] [MonoidalCategory C]
    (V : C) (c : (V ⊗ V) ⟶ (V ⊗ V)) :
    (V ⊗ V) ⊗ V ⟶ (V ⊗ V) ⊗ V :=
  (α_ V V V).hom ≫ (V ◁ c) ≫ (α_ V V V).inv

/-- `σ₁` acting on `(V ⊗ V) ⊗ V` via the categorical braiding `β_{V,V}`. -/
def sigma1 {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    (V ⊗ V) ⊗ V ⟶ (V ⊗ V) ⊗ V :=
  (β_ V V).hom ▷ V

/-- `σ₂` acting on `(V ⊗ V) ⊗ V` via the categorical braiding `β_{V,V}`. -/
def sigma2 {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    (V ⊗ V) ⊗ V ⟶ (V ⊗ V) ⊗ V :=
  (α_ V V V).hom ≫ (V ◁ (β_ V V).hom) ≫ (α_ V V V).inv

/-- Full two-sided categorical isomorphism `σ₁Iso V : (V ⊗ V) ⊗ V ≅ (V ⊗ V) ⊗ V`. -/
def sigma1Iso {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    ((V ⊗ V) ⊗ V) ≅ ((V ⊗ V) ⊗ V) :=
  whiskerRightIso (β_ V V) V

/-- Full two-sided categorical isomorphism `σ₂Iso V : (V ⊗ V) ⊗ V ≅ (V ⊗ V) ⊗ V`. -/
def sigma2Iso {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    ((V ⊗ V) ⊗ V) ≅ ((V ⊗ V) ⊗ V) :=
  (α_ V V V) ≪≫ whiskerLeftIso V (β_ V V) ≪≫ (α_ V V V).symm

/-- `σ₁` right-inverse identity: `σ₁ ≫ σ₁⁻¹ = id`. -/
theorem sigma1_is_iso {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    sigma1 V ≫ ((β_ V V).inv ▷ V) = 𝟙 ((V ⊗ V) ⊗ V) := by
  simp [sigma1, ← MonoidalCategory.comp_whiskerRight, Iso.hom_inv_id]

/-- `σ₁` left-inverse identity: `σ₁⁻¹ ≫ σ₁ = id`. -/
theorem sigma1_inv_hom {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    ((β_ V V).inv ▷ V) ≫ sigma1 V = 𝟙 ((V ⊗ V) ⊗ V) := by
  simp [sigma1, ← MonoidalCategory.comp_whiskerRight, Iso.inv_hom_id]

/-- `σ₂` right-inverse identity: `σ₂ ≫ σ₂⁻¹ = id`. -/
theorem sigma2_is_iso {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    sigma2 V ≫ ((α_ V V V).hom ≫ (V ◁ (β_ V V).inv) ≫ (α_ V V V).inv)
    = 𝟙 ((V ⊗ V) ⊗ V) := by
  simp only [sigma2, Category.assoc]
  rw [Iso.inv_hom_id_assoc]
  slice_lhs 2 3 => rw [← MonoidalCategory.whiskerLeft_comp, Iso.hom_inv_id,
                       MonoidalCategory.whiskerLeft_id]
  simp

/-- `σ₂` left-inverse identity: `σ₂⁻¹ ≫ σ₂ = id`. -/
theorem sigma2_inv_hom {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    ((α_ V V V).hom ≫ (V ◁ (β_ V V).inv) ≫ (α_ V V V).inv) ≫ sigma2 V
    = 𝟙 ((V ⊗ V) ⊗ V) := by
  simp only [sigma2, Category.assoc]
  rw [Iso.inv_hom_id_assoc]
  slice_lhs 2 3 => rw [← MonoidalCategory.whiskerLeft_comp, Iso.inv_hom_id,
                       MonoidalCategory.whiskerLeft_id]
  simp

/-! ## Equivalence of the Adjacent Braid Relation and the Yang–Baxter Equation -/

/-- The **Yang–Baxter equation** for an endomorphism `c : V ⊗ V ⟶ V ⊗ V` in a
    monoidal category `C`:
    `(c ⊗ id_V) ∘ (id_V ⊗ c) ∘ (c ⊗ id_V) = (id_V ⊗ c) ∘ (c ⊗ id_V) ∘ (id_V ⊗ c)`
    on `(V ⊗ V) ⊗ V` (with associator transport for `id_V ⊗ c`). -/
def YangBaxterEquation {C : Type u} [Category.{v} C] [MonoidalCategory C]
    (V : C) (c : (V ⊗ V) ⟶ (V ⊗ V)) : Prop :=
  (c ▷ V) ≫ (α_ V V V).hom ≫ (V ◁ c) ≫ (α_ V V V).inv ≫ (c ▷ V) =
  (α_ V V V).hom ≫ (V ◁ c) ≫ (α_ V V V).inv ≫ (c ▷ V) ≫
    (α_ V V V).hom ≫ (V ◁ c) ≫ (α_ V V V).inv

/-- **Two-way equivalence (`↔`)** between the adjacent braid relation
    `σ₁(c) ≫ σ₂(c) ≫ σ₁(c) = σ₂(c) ≫ σ₁(c) ≫ σ₂(c)` and the Yang–Baxter
    equation for any morphism `c : V ⊗ V ⟶ V ⊗ V`. -/
-- Ref: [kassel1995] Theorem XIII.1.3
theorem braid_rel_iff_yang_baxter {C : Type u} [Category.{v} C] [MonoidalCategory C]
    (V : C) (c : (V ⊗ V) ⟶ (V ⊗ V)) :
    sigma1Of V c ≫ sigma2Of V c ≫ sigma1Of V c =
      sigma2Of V c ≫ sigma1Of V c ≫ sigma2Of V c ↔
    YangBaxterEquation V c := by
  simp only [sigma1Of, sigma2Of, YangBaxterEquation, Category.assoc]

/-! ## Derivation of the Yang–Baxter Equation from the Braided Monoidal Axioms -/

/-- **Lemma (hexagon reduction):** `σ₁ ≫ σ₂ = α ≫ β_{V, V ⊗ V}`. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2, Ch. XIII
private theorem sigma12_eq_alpha_braiding {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    sigma1 V ≫ sigma2 V = (α_ V V V).hom ≫ (β_ V (V ⊗ V)).hom := by
  simp only [sigma1, sigma2]
  have hex := BraidedCategory.hexagon_forward (C := C) V V V
  slice_lhs 1 3 => rw [← hex]
  simp

/-- **Lemma (braiding naturality):**
    `β_{V, V ⊗ V} ≫ (β_{V,V} ▷ V) = (V ◁ β_{V,V}) ≫ β_{V, V ⊗ V}`. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2, Ch. XIII
private theorem braiding_nat_sigma {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    (β_ V (V ⊗ V)).hom ≫ ((β_ V V).hom ▷ V) =
    (V ◁ (β_ V V).hom) ≫ (β_ V (V ⊗ V)).hom :=
  (BraidedCategory.braiding_naturality_right V ((β_ V V).hom)).symm

/-- **Lemma (`σ₂–α` interchange):** `σ₂ ≫ α = α ≫ (V ◁ β_{V,V})`. -/
private theorem sigma2_alpha_interchange {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    sigma2 V ≫ (α_ V V V).hom = (α_ V V V).hom ≫ (V ◁ (β_ V V).hom) := by
  simp only [sigma2, Category.assoc]
  rw [Iso.inv_hom_id, Category.comp_id]

/-- **The Yang–Baxter equation / braid relation** for the categorical braiding `β_{V,V}`:
    `σ₁ ≫ σ₂ ≫ σ₁ = σ₂ ≫ σ₁ ≫ σ₂` on `(V ⊗ V) ⊗ V`. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2, Theorem XIII.1.3
theorem yang_baxter_braiding {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    sigma1 V ≫ sigma2 V ≫ sigma1 V =
    sigma2 V ≫ sigma1 V ≫ sigma2 V := by
  have key := sigma12_eq_alpha_braiding V
  have nat := braiding_nat_sigma V
  have s2a := sigma2_alpha_interchange V
  calc sigma1 V ≫ (sigma2 V ≫ sigma1 V)
      _ = (sigma1 V ≫ sigma2 V) ≫ sigma1 V := by rw [← Category.assoc]
      _ = ((α_ V V V).hom ≫ (β_ V (V ⊗ V)).hom) ≫ sigma1 V := by rw [key]
      _ = ((α_ V V V).hom ≫ (β_ V (V ⊗ V)).hom) ≫ ((β_ V V).hom ▷ V) := rfl
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

/-- The categorical braiding `(β_ V V).hom` satisfies `YangBaxterEquation V (β_ V V).hom`. -/
theorem yangBaxterEquation_of_braided {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    YangBaxterEquation V (β_ V V).hom :=
  (braid_rel_iff_yang_baxter V (β_ V V).hom).mp (yang_baxter_braiding V)

/-! ## General `n`-Fold Tensor Power `V^⊗n` and Artin Generators `σ_i` -/

/-- Recursive `n`-fold tensor power `V^{\otimes n}` in any monoidal category `C`:
    - `n = 0`: `𝟙_ C`
    - `n = 1`: `V`
    - `n + 2`: `tensorPow V (n + 1) ⊗ V` (left-associated: `((V ⊗ V) ⊗ V) ⊗ ...`). -/
def tensorPow {C : Type u} [Category.{v} C] [MonoidalCategory C]
    (V : C) : ℕ → C
  | 0 => 𝟙_ C
  | 1 => V
  | n + 2 => tensorPow V (n + 1) ⊗ V

@[simp] theorem tensorPow_zero {C : Type u} [Category.{v} C] [MonoidalCategory C] (V : C) :
    tensorPow V 0 = 𝟙_ C := rfl

@[simp] theorem tensorPow_one {C : Type u} [Category.{v} C] [MonoidalCategory C] (V : C) :
    tensorPow V 1 = V := rfl

@[simp] theorem tensorPow_two {C : Type u} [Category.{v} C] [MonoidalCategory C] (V : C) :
    tensorPow V 2 = V ⊗ V := rfl

@[simp] theorem tensorPow_three {C : Type u} [Category.{v} C] [MonoidalCategory C] (V : C) :
    tensorPow V 3 = (V ⊗ V) ⊗ V := rfl

@[simp] theorem tensorPow_succ_succ {C : Type u} [Category.{v} C] [MonoidalCategory C]
    (V : C) (n : ℕ) :
    tensorPow V (n + 2) = tensorPow V (n + 1) ⊗ V := rfl

/-- Recursive definition of `artinGen V n i : tensorPow V n ≅ tensorPow V n`
    for every `n : ℕ` and generator index `i : ℕ`.
    (For `i + 1 < n` this is the genuine Artin generator `ρ_n(σ_{i+1})`;
    out of range `i + 1 ≥ n` it defaults to `Iso.refl`.) -/
def artinGen {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    (n : ℕ) → (i : ℕ) → (tensorPow V n ≅ tensorPow V n)
  | 0, _ => Iso.refl _
  | 1, _ => Iso.refl _
  | 2, 0 => β_ V V
  | 2, _ + 1 => Iso.refl _
  | m + 3, i =>
      if i < m + 1 then
        whiskerRightIso (artinGen V (m + 2) i) V
      else if i = m + 1 then
        (α_ (tensorPow V (m + 1)) V V) ≪≫
          whiskerLeftIso (tensorPow V (m + 1)) (β_ V V) ≪≫
          (α_ (tensorPow V (m + 1)) V V).symm
      else
        Iso.refl _

theorem artinGen_succ_lt_hom {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) (m i : ℕ) (h : i < m + 1) :
    (artinGen V (m + 3) i).hom = (artinGen V (m + 2) i).hom ▷ V := by
  change (if i < m + 1 then
      whiskerRightIso (artinGen V (m + 2) i) V
    else if i = m + 1 then
      (α_ (tensorPow V (m + 1)) V V) ≪≫
        whiskerLeftIso (tensorPow V (m + 1)) (β_ V V) ≪≫
        (α_ (tensorPow V (m + 1)) V V).symm
    else Iso.refl _).hom = _
  rw [if_pos h]
  rfl

theorem artinGen_succ_eq_hom {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) (m : ℕ) :
    (artinGen V (m + 3) (m + 1)).hom =
      (α_ (tensorPow V (m + 1)) V V).hom ≫
        (tensorPow V (m + 1) ◁ (β_ V V).hom) ≫
        (α_ (tensorPow V (m + 1)) V V).inv := by
  have hlt : ¬ (m + 1 < m + 1) := Nat.lt_irrefl (m + 1)
  change (if m + 1 < m + 1 then
      whiskerRightIso (artinGen V (m + 2) (m + 1)) V
    else if m + 1 = m + 1 then
      (α_ (tensorPow V (m + 1)) V V) ≪≫
        whiskerLeftIso (tensorPow V (m + 1)) (β_ V V) ≪≫
        (α_ (tensorPow V (m + 1)) V V).symm
    else Iso.refl _).hom = _
  rw [if_neg hlt, if_pos rfl]
  rfl

theorem artinGen_succ_gt_hom {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) (m i : ℕ) (h : m + 1 < i) :
    (artinGen V (m + 3) i).hom = 𝟙 (tensorPow V (m + 3)) := by
  have hlt : ¬ (i < m + 1) := by omega
  have heq : ¬ (i = m + 1) := by omega
  change (if i < m + 1 then
      whiskerRightIso (artinGen V (m + 2) i) V
    else if i = m + 1 then
      (α_ (tensorPow V (m + 1)) V V) ≪≫
        whiskerLeftIso (tensorPow V (m + 1)) (β_ V V) ≪≫
        (α_ (tensorPow V (m + 1)) V V).symm
    else Iso.refl _).hom = _
  rw [if_neg hlt, if_neg heq]
  rfl

/-- On `n = 3` strands, `artinGen V 3 0` is `sigma1Iso V` (`c_{V,V} ⊗ id_V`). -/
theorem artinGen_three_zero_hom {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    (artinGen V 3 0).hom = sigma1 V := rfl

/-- On `n = 3` strands, `artinGen V 3 1` is `sigma2Iso V` (`α ≫ (id_V ⊗ c_{V,V}) ≫ α⁻¹`). -/
theorem artinGen_three_one_hom {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    (artinGen V 3 1).hom = sigma2 V := rfl

/-- Every Artin generator `artinGen V n i` is a two-sided isomorphism on `V^{\otimes n}`:
    both `hom ≫ inv = 𝟙` and `inv ≫ hom = 𝟙` hold for all `n` and `i`. -/
theorem artinGen_hom_inv_and_inv_hom {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) (n i : ℕ) :
    (artinGen V n i).hom ≫ (artinGen V n i).inv = 𝟙 (tensorPow V n) ∧
    (artinGen V n i).inv ≫ (artinGen V n i).hom = 𝟙 (tensorPow V n) :=
  ⟨(artinGen V n i).hom_inv_id, (artinGen V n i).inv_hom_id⟩

/-! ## General Adjacent Braid Relation and Far-Commutativity -/

/-- Helper lemma: for any object `W : C` and `V : C` in a braided monoidal category,
    the top two generators on `(W ⊗ V) ⊗ V` coupled to a right factor `V`, namely
    `g₁ = (α_{W,V,V} ≫ (W ◁ β_{V,V}) ≫ α_{W,V,V}⁻¹) ▷ V` and
    `g₂ = α_{W ⊗ V, V, V} ≫ ((W ⊗ V) ◁ β_{V,V}) ≫ α_{W ⊗ V, V, V}⁻¹`,
    satisfy the adjacent braid relation `g₁ ≫ g₂ ≫ g₁ = g₂ ≫ g₁ ≫ g₂`.
    This is proved by transporting the 3-strand Yang–Baxter identity `yang_baxter_braiding V`
    under the left-whiskering functor `W ◁ -` via the pentagon identity. -/
theorem top_adjacent_braid_rel {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (W V : C) :
    let g1 : ((W ⊗ V) ⊗ V) ⊗ V ⟶ ((W ⊗ V) ⊗ V) ⊗ V :=
      ((α_ W V V).hom ≫ (W ◁ (β_ V V).hom) ≫ (α_ W V V).inv) ▷ V
    let g2 : ((W ⊗ V) ⊗ V) ⊗ V ⟶ ((W ⊗ V) ⊗ V) ⊗ V :=
      (α_ (W ⊗ V) V V).hom ≫ ((W ⊗ V) ◁ (β_ V V).hom) ≫ (α_ (W ⊗ V) V V).inv
    g1 ≫ g2 ≫ g1 = g2 ≫ g1 ≫ g2 := by
  intro g1 g2
  let Φ : ((W ⊗ V) ⊗ V) ⊗ V ≅ W ⊗ ((V ⊗ V) ⊗ V) :=
    (whiskerRightIso (α_ W V V) V) ≪≫ (α_ W (V ⊗ V) V)
  have hg1 : g1 = Φ.hom ≫ (W ◁ sigma1 V) ≫ Φ.inv := by
    dsimp [g1, Φ, sigma1]
    have hmid : (α_ W (V ⊗ V) V).hom ≫ (W ◁ ((β_ V V).hom ▷ V)) =
        ((W ◁ (β_ V V).hom) ▷ V) ≫ (α_ W (V ⊗ V) V).hom :=
      (associator_naturality_middle W (β_ V V).hom V).symm
    calc ((α_ W V V).hom ≫ W ◁ (β_ V V).hom ≫ (α_ W V V).inv) ▷ V
        = (α_ W V V).hom ▷ V ≫ (W ◁ (β_ V V).hom) ▷ V ≫ (α_ W V V).inv ▷ V := by
          simp only [comp_whiskerRight]
      _ = (α_ W V V).hom ▷ V ≫
            (((W ◁ (β_ V V).hom) ▷ V ≫ (α_ W (V ⊗ V) V).hom) ≫ (α_ W (V ⊗ V) V).inv) ≫
            (α_ W V V).inv ▷ V := by
          simp only [Category.assoc, Iso.hom_inv_id_assoc]
      _ = (α_ W V V).hom ▷ V ≫
            (((α_ W (V ⊗ V) V).hom ≫ (W ◁ ((β_ V V).hom ▷ V))) ≫ (α_ W (V ⊗ V) V).inv) ≫
            (α_ W V V).inv ▷ V := by
          rw [hmid]
      _ = ((α_ W V V).hom ▷ V ≫ (α_ W (V ⊗ V) V).hom) ≫ W ◁ (β_ V V).hom ▷ V ≫
            (α_ W (V ⊗ V) V).inv ≫ (α_ W V V).inv ▷ V := by
          simp only [Category.assoc]
  have hg2 : g2 = Φ.hom ≫ (W ◁ sigma2 V) ≫ Φ.inv := by
    dsimp [g2, Φ, sigma2]
    have hpent : (α_ W V V).hom ▷ V ≫ (α_ W (V ⊗ V) V).hom ≫ (W ◁ (α_ V V V).hom) =
        (α_ (W ⊗ V) V V).hom ≫ (α_ W V (V ⊗ V)).hom := by
      simp [MonoidalCategory.pentagon]
    have hpent_inv : (W ◁ (α_ V V V).inv) ≫ (α_ W (V ⊗ V) V).inv ≫ (α_ W V V).inv ▷ V =
        (α_ W V (V ⊗ V)).inv ≫ (α_ (W ⊗ V) V V).inv := by
      let E1 : ((W ⊗ V) ⊗ V) ⊗ V ≅ W ⊗ (V ⊗ (V ⊗ V)) :=
        whiskerRightIso (α_ W V V) V ≪≫ α_ W (V ⊗ V) V ≪≫ whiskerLeftIso W (α_ V V V)
      let E2 : ((W ⊗ V) ⊗ V) ⊗ V ≅ W ⊗ (V ⊗ (V ⊗ V)) :=
        α_ (W ⊗ V) V V ≪≫ α_ W V (V ⊗ V)
      have hE : E1 = E2 := by
        ext
        exact hpent
      have hEinv : E1.inv = E2.inv := congrArg Iso.inv hE
      dsimp [E1, E2] at hEinv
      simpa only [Category.assoc] using hEinv
    have hnat_r : (W ⊗ V) ◁ (β_ V V).hom =
        (α_ W V (V ⊗ V)).hom ≫ (W ◁ (V ◁ (β_ V V).hom)) ≫ (α_ W V (V ⊗ V)).inv := by
      rw [← associator_naturality_right_assoc, Iso.hom_inv_id, Category.comp_id]
    simp only [whiskerLeft_comp, Category.assoc]
    calc (α_ (W ⊗ V) V V).hom ≫ (W ⊗ V) ◁ (β_ V V).hom ≫ (α_ (W ⊗ V) V V).inv
        = (α_ (W ⊗ V) V V).hom ≫
            ((α_ W V (V ⊗ V)).hom ≫ (W ◁ (V ◁ (β_ V V).hom)) ≫ (α_ W V (V ⊗ V)).inv) ≫
            (α_ (W ⊗ V) V V).inv := by
          rw [hnat_r]
      _ = ((α_ (W ⊗ V) V V).hom ≫ (α_ W V (V ⊗ V)).hom) ≫ (W ◁ (V ◁ (β_ V V).hom)) ≫
            ((α_ W V (V ⊗ V)).inv ≫ (α_ (W ⊗ V) V V).inv) := by
          simp only [Category.assoc]
      _ = ((α_ W V V).hom ▷ V ≫ (α_ W (V ⊗ V) V).hom ≫ (W ◁ (α_ V V V).hom)) ≫
            (W ◁ (V ◁ (β_ V V).hom)) ≫
            ((W ◁ (α_ V V V).inv) ≫ (α_ W (V ⊗ V) V).inv ≫ (α_ W V V).inv ▷ V) := by
          rw [← hpent, ← hpent_inv]
      _ = (α_ W V V).hom ▷ V ≫ (α_ W (V ⊗ V) V).hom ≫ W ◁ (α_ V V V).hom ≫
            W ◁ (V ◁ (β_ V V).hom) ≫ W ◁ (α_ V V V).inv ≫ (α_ W (V ⊗ V) V).inv ≫
            (α_ W V V).inv ▷ V := by
          simp only [Category.assoc]
  rw [hg1, hg2]
  have hyb := congrArg (fun f => W ◁ f) (yang_baxter_braiding V)
  simp only [whiskerLeft_comp] at hyb
  calc (Φ.hom ≫ W ◁ sigma1 V ≫ Φ.inv) ≫ (Φ.hom ≫ W ◁ sigma2 V ≫ Φ.inv) ≫
        (Φ.hom ≫ W ◁ sigma1 V ≫ Φ.inv)
      = Φ.hom ≫ (W ◁ sigma1 V ≫ W ◁ sigma2 V ≫ W ◁ sigma1 V) ≫ Φ.inv := by
        simp only [Category.assoc, Iso.inv_hom_id_assoc]
    _ = Φ.hom ≫ (W ◁ sigma2 V ≫ W ◁ sigma1 V ≫ W ◁ sigma2 V) ≫ Φ.inv := by
        rw [hyb]
    _ = (Φ.hom ≫ W ◁ sigma2 V ≫ Φ.inv) ≫ (Φ.hom ≫ W ◁ sigma1 V ≫ Φ.inv) ≫
        (Φ.hom ≫ W ◁ sigma2 V ≫ Φ.inv) := by
        simp only [Category.assoc, Iso.inv_hom_id_assoc]

/-- **General Adjacent Braid Relation on `V^{\otimes n}`:**
    For every `n : ℕ` and every `i : ℕ` with `i + 2 < n`,
    `ρ_n(σ_i) ≫ ρ_n(σ_{i+1}) ≫ ρ_n(σ_i) = ρ_n(σ_{i+1}) ≫ ρ_n(σ_i) ≫ ρ_n(σ_{i+1})`. -/
theorem artinGen_braid_rel {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    ∀ (n i : ℕ), i + 2 < n →
      (artinGen V n i).hom ≫ (artinGen V n (i + 1)).hom ≫ (artinGen V n i).hom =
      (artinGen V n (i + 1)).hom ≫ (artinGen V n i).hom ≫ (artinGen V n (i + 1)).hom
  | 0, _, h => by omega
  | 1, _, h => by omega
  | 2, _, h => by omega
  | 3, i, h => by
      have hi : i = 0 := by omega
      subst hi
      exact yang_baxter_braiding V
  | m + 4, i, h => by
      by_cases hlt : i + 1 < m + 2
      · have hi : i < m + 2 := by omega
        have hrec := artinGen_braid_rel V (m + 3) i (by omega)
        rw [artinGen_succ_lt_hom V (m + 1) i hi,
            artinGen_succ_lt_hom V (m + 1) (i + 1) hlt]
        simp only [← comp_whiskerRight]
        rw [hrec]
      · have hi : i = m + 1 := by omega
        subst hi
        have hi1 : m + 1 < m + 2 := by omega
        rw [artinGen_succ_lt_hom V (m + 1) (m + 1) hi1,
            artinGen_succ_eq_hom V (m + 1),
            artinGen_succ_eq_hom V m]
        exact top_adjacent_braid_rel (tensorPow V (m + 1)) V

/-- Helper lemma: a right-whiskered morphism `(f ▷ V) ▷ V` on `(W ⊗ V) ⊗ V`
    commutes with the top generator `α_{W,V,V} ≫ (W ◁ g) ≫ α_{W,V,V}⁻¹`
    for any `f : W ⟶ W` and `g : V ⊗ V ⟶ V ⊗ V`, by the monoidal interchange law
    and naturality of the associator `α_{W,V,V}` in its first argument. -/
theorem whiskerRight_twice_comm_top {C : Type u} [Category.{v} C]
    [MonoidalCategory C] {W V : C} (f : W ⟶ W) (g : (V ⊗ V) ⟶ (V ⊗ V)) :
    ((f ▷ V) ▷ V) ≫ ((α_ W V V).hom ≫ (W ◁ g) ≫ (α_ W V V).inv) =
    ((α_ W V V).hom ≫ (W ◁ g) ≫ (α_ W V V).inv) ≫ ((f ▷ V) ▷ V) := by
  calc ((f ▷ V) ▷ V) ≫ ((α_ W V V).hom ≫ (W ◁ g) ≫ (α_ W V V).inv)
      = (((f ▷ V) ▷ V) ≫ (α_ W V V).hom) ≫ (W ◁ g) ≫ (α_ W V V).inv := by
        simp only [Category.assoc]
    _ = ((α_ W V V).hom ≫ (f ▷ (V ⊗ V))) ≫ (W ◁ g) ≫ (α_ W V V).inv := by
        rw [associator_naturality_left]
    _ = (α_ W V V).hom ≫ ((f ▷ (V ⊗ V)) ≫ (W ◁ g)) ≫ (α_ W V V).inv := by
        simp only [Category.assoc]
    _ = (α_ W V V).hom ≫ ((W ◁ g) ≫ (f ▷ (V ⊗ V))) ≫ (α_ W V V).inv := by
        rw [whisker_exchange]
    _ = (α_ W V V).hom ≫ (W ◁ g) ≫ ((f ▷ (V ⊗ V)) ≫ (α_ W V V).inv) := by
        simp only [Category.assoc]
    _ = (α_ W V V).hom ≫ (W ◁ g) ≫ ((α_ W V V).inv ≫ ((f ▷ V) ▷ V)) := by
        congr 2
        apply (cancel_epi (α_ W V V).hom).mp
        slice_lhs 1 2 => rw [← associator_naturality_left]
        simp
    _ = ((α_ W V V).hom ≫ (W ◁ g) ≫ (α_ W V V).inv) ≫ ((f ▷ V) ▷ V) := by
        simp only [Category.assoc]

/-- **General Far-Commutativity on `V^{\otimes n}` (`i + 2 ≤ j`):**
    For every `n : ℕ` and generator indices `i, j : ℕ` with `i + 2 ≤ j`,
    `ρ_n(σ_i) ≫ ρ_n(σ_j) = ρ_n(σ_j) ≫ ρ_n(σ_i)`. -/
theorem artinGen_far_comm_lt {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    ∀ (n i j : ℕ), i + 2 ≤ j →
      (artinGen V n i).hom ≫ (artinGen V n j).hom =
      (artinGen V n j).hom ≫ (artinGen V n i).hom
  | 0, _, _, _ => by simp [artinGen]
  | 1, _, _, _ => by simp [artinGen]
  | 2, i, j, h => by
      cases j with
      | zero => omega
      | succ j' =>
        change (artinGen V 2 i).hom ≫ 𝟙 (tensorPow V 2) =
          𝟙 (tensorPow V 2) ≫ (artinGen V 2 i).hom
        simp
  | m + 3, i, j, h => by
      by_cases hj_lt : j < m + 1
      · have hi_lt : i < m + 1 := by omega
        have hrec := artinGen_far_comm_lt V (m + 2) i j h
        rw [artinGen_succ_lt_hom V m i hi_lt,
            artinGen_succ_lt_hom V m j hj_lt]
        simp only [← comp_whiskerRight]
        rw [hrec]
      · by_cases hj_eq : j = m + 1
        · subst hj_eq
          cases m with
          | zero => omega
          | succ m' =>
            have hi_lt1 : i < m' + 1 + 1 := by omega
            have hi_lt0 : i < m' + 1 := by omega
            rw [artinGen_succ_lt_hom V (m' + 1) i hi_lt1,
                artinGen_succ_lt_hom V m' i hi_lt0,
                artinGen_succ_eq_hom V (m' + 1)]
            exact whiskerRight_twice_comm_top (artinGen V (m' + 2) i).hom (β_ V V).hom
        · have hj_gt : m + 1 < j := by omega
          rw [artinGen_succ_gt_hom V m j hj_gt]
          simp

/-- **General Far-Commutativity on `V^{\otimes n}` (`|i - j| ≥ 2`):**
    Whenever `i + 2 ≤ j ∨ j + 2 ≤ i`, the Artin generators commute:
    `ρ_n(σ_i) ≫ ρ_n(σ_j) = ρ_n(σ_j) ≫ ρ_n(σ_i)`. -/
theorem artinGen_far_comm {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C)
    (n i j : ℕ) (h : i + 2 ≤ j ∨ j + 2 ≤ i) :
    (artinGen V n i).hom ≫ (artinGen V n j).hom =
    (artinGen V n j).hom ≫ (artinGen V n i).hom := by
  rcases h with hij | hji
  · exact artinGen_far_comm_lt V n i j hij
  · exact (artinGen_far_comm_lt V n j i hji).symm

/-! ## Artin Braid Group Presentation `B_n` and Homomorphism `B_n →* Aut_C(V^⊗n)` -/

/-- The `i`-th Artin generator as an automorphism in the group `Aut (tensorPow V n)`. -/
def artinGenAut {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) (n : ℕ) (i : Fin (n - 1)) :
    Aut (tensorPow V n) :=
  artinGen V n i.val

/-- The generating relations of the Artin braid group `B_n` in the free group
    `FreeGroup (Fin (n - 1))` on the `n - 1` Artin generators `σ_0, …, σ_{n-2}`:
    1. Adjacent braid relations: `σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}` for `i + 1 < n - 1`,
       encoded as `(σ_i σ_{i+1} σ_i) (σ_{i+1} σ_i σ_{i+1})⁻¹ = 1`.
    2. Far-commutativity relations: `σ_i σ_j = σ_j σ_i` for `i + 2 ≤ j`,
       encoded as `(σ_i σ_j) (σ_j σ_i)⁻¹ = 1`. -/
def artinBraidRels (n : ℕ) : Set (FreeGroup (Fin (n - 1))) :=
  { r | (∃ (i j : Fin (n - 1)), i.val + 1 = j.val ∧
          r = (FreeGroup.of i * FreeGroup.of j * FreeGroup.of i) *
              (FreeGroup.of j * FreeGroup.of i * FreeGroup.of j)⁻¹) ∨
        (∃ (i j : Fin (n - 1)), i.val + 2 ≤ j.val ∧
          r = (FreeGroup.of i * FreeGroup.of j) *
              (FreeGroup.of j * FreeGroup.of i)⁻¹) }

/-- The **Artin braid group `B_n`** on `n` strands, defined as the `PresentedGroup`
    on `Fin (n - 1)` quotiented by the adjacent braid and far-commutativity relations
    `artinBraidRels n`. -/
abbrev ArtinBraidGroup (n : ℕ) : Type :=
  PresentedGroup (artinBraidRels n)

/-- The `i`-th Artin generator `σ_i` as an element of `ArtinBraidGroup n`. -/
def artinBraidGen (n : ℕ) (i : Fin (n - 1)) : ArtinBraidGroup n :=
  PresentedGroup.of i

/-- Every relation word in `artinBraidRels n` maps to `1 : Aut (tensorPow V n)`
    under `FreeGroup.lift (artinGenAut V n)`. -/
theorem artinBraidRels_satisfied {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) (n : ℕ) :
    ∀ r ∈ artinBraidRels n,
      (FreeGroup.lift (artinGenAut V n)) r = 1 := by
  intro r hr
  rcases hr with ⟨i, j, hij, rfl⟩ | ⟨i, j, hij, rfl⟩
  · simp only [map_mul, map_inv, FreeGroup.lift_apply_of, mul_inv_eq_one]
    ext
    simp only [Aut.Aut_mul_def, Iso.trans_hom, artinGenAut]
    have hlt : i.val + 2 < n := by omega
    rw [← hij]
    exact artinGen_braid_rel V n i.val hlt
  · simp only [map_mul, map_inv, FreeGroup.lift_apply_of, mul_inv_eq_one]
    ext
    simp only [Aut.Aut_mul_def, Iso.trans_hom, artinGenAut]
    exact (artinGen_far_comm_lt V n i.val j.val hij).symm

/-- **The categorical braid group homomorphism**
    `ρ_n : B_n →* Aut_C(V^{\otimes n})` for every object `V : C` and every `n : ℕ`
    in a braided monoidal category `C`. -/
-- Ref: [kassel1995] Theorem XIII.1.3 & Corollary XIII.1.4
def braid_action_tensor_hom {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) (n : ℕ) :
    ArtinBraidGroup n →* Aut (tensorPow V n) :=
  PresentedGroup.toGroup (artinBraidRels_satisfied V n)

/-- On the `i`-th Artin generator `σ_i ∈ B_n`, `braid_action_tensor_hom V n` evaluates
    to the categorical isomorphism `artinGen V n i.val ∈ Aut_C(V^{\otimes n})`. -/
@[simp]
theorem braid_action_tensor_hom_of {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) (n : ℕ) (i : Fin (n - 1)) :
    braid_action_tensor_hom V n (artinBraidGen n i) = artinGenAut V n i :=
  PresentedGroup.toGroup.of (artinBraidRels_satisfied V n)

/-! ## Packaged Representation Structures (`BraidActionTensor`, `BraidRepB3`, `braid_action_tensor`) -/

/-- **Braid representation on `V^{\otimes n}`** in a braided monoidal category,
    carrying the `n`-strand group homomorphism `ρ_n : B_n →* Aut_C(V^{\otimes n})`
    along with the adjacent braid and far-commutativity theorems. -/
-- Ref: [kassel1995], [leitner2026] §4
structure BraidActionTensor (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] where
  /-- The object `V` to be tensored. -/
  V : C
  /-- Number of strands `n ≥ 2`. -/
  numStrands : ℕ
  strands_ge_two : 2 ≤ numStrands
  /-- The braiding `c_{V,V} : V ⊗ V → V ⊗ V`. -/
  braiding : (V ⊗ V) ⟶ (V ⊗ V) := (β_ V V).hom
  /-- The group homomorphism `ρ_n : B_n →* Aut_C(V^{\otimes n})`. -/
  rho : ArtinBraidGroup numStrands →* Aut (tensorPow V numStrands) :=
    braid_action_tensor_hom V numStrands

/-- **`B₃` representation data** together with the general `n`-strand homomorphism
    `ρ_n : B_n →* Aut_C(V^{\otimes n})`, two-sided generator invertibility,
    adjacent braid relation, far-commutativity, and Yang–Baxter equivalence. -/
structure BraidRepB3 (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] where
  /-- The fundamental object `V`. -/
  V : C
  /-- Generator `σ₁ = c_{V,V} ⊗ id_V` on `(V ⊗ V) ⊗ V`. -/
  gen1 : (V ⊗ V) ⊗ V ⟶ (V ⊗ V) ⊗ V := sigma1 V
  /-- Generator `σ₂ = id_V ⊗ c_{V,V}` (via associator) on `(V ⊗ V) ⊗ V`. -/
  gen2 : (V ⊗ V) ⊗ V ⟶ (V ⊗ V) ⊗ V := sigma2 V
  /-- The 3-strand braid relation holds. -/
  braid_rel : gen1 ≫ gen2 ≫ gen1 = gen2 ≫ gen1 ≫ gen2
  /-- General `n`-strand group homomorphism `ρ_n : B_n →* Aut_C(V^{\otimes n})`. -/
  hom : ∀ (n : ℕ), ArtinBraidGroup n →* Aut (tensorPow V n)
  /-- General adjacent braid relation for all `n` and `i + 2 < n`. -/
  adjacent_braid_rel : ∀ (n i : ℕ), i + 2 < n →
    (artinGen V n i).hom ≫ (artinGen V n (i + 1)).hom ≫ (artinGen V n i).hom =
    (artinGen V n (i + 1)).hom ≫ (artinGen V n i).hom ≫ (artinGen V n (i + 1)).hom
  /-- General far-commutativity for all `n` and `|i - j| ≥ 2`. -/
  far_comm : ∀ (n i j : ℕ), i + 2 ≤ j ∨ j + 2 ≤ i →
    (artinGen V n i).hom ≫ (artinGen V n j).hom =
    (artinGen V n j).hom ≫ (artinGen V n i).hom
  /-- Equivalence between the adjacent braid relation and the Yang–Baxter equation. -/
  yb_iff : ∀ (c : (V ⊗ V) ⟶ (V ⊗ V)),
    sigma1Of V c ≫ sigma2Of V c ≫ sigma1Of V c =
      sigma2Of V c ≫ sigma1Of V c ≫ sigma2Of V c ↔
    YangBaxterEquation V c

/-- Every braided monoidal category yields a group homomorphism
    `ρ_n : B_n →* Aut_C(V^{\otimes n})` for all `n` (including the `B₃` representation
    on `V^{\otimes 3}`), with adjacent braid relations equivalent to the Yang–Baxter
    equation and far-commutativity on disjoint strand pairs. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2, Theorem XIII.1.3 & Cor. XIII.1.4
def braid_action_tensor {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [BraidedCategory C] (V : C) :
    BraidRepB3 C where
  V := V
  gen1 := sigma1 V
  gen2 := sigma2 V
  braid_rel := yang_baxter_braiding V
  hom := braid_action_tensor_hom V
  adjacent_braid_rel := artinGen_braid_rel V
  far_comm := artinGen_far_comm V
  yb_iff := braid_rel_iff_yang_baxter V

end QOU.Braiding
