import HeckeTemperleyLieb.TLNegligibleQuotient
import Mathlib.CategoryTheory.Functor.FullyFaithful

/-!
# Rectangular Temperley–Lieb hom spaces in the semisimplified tower

Bean `hkmt`. `TLNegligibleQuotient` lists the simple objects of the semisimplified tower on every
number of strands. This file builds the hom spaces **between different strand numbers** and
proves that they form a category that does not depend on the ambient number of strands.

## Strand counts inside a larger algebra

Write `[a]` for the object of `a + 1` strands. Inside `TL_{N+1}` it is the idempotent
`P a N`: the identity if `a = N`, and otherwise `capEmb (P a (N − 2))`, that is, `a + 1`
through-strands followed by `(N − a)/2` nested cup–caps, normalised by `δ⁻¹` each. If `N − a`
is odd or `a > N` the recursion bottoms out at `0`, so `P a N = 0` (`P_eq_zero_of_lt`).

## The hom spaces and the category

`Hom N a b` is the corner `P b N · Q N · P a N` of the quotient `Q N` by negligibles. Its
elements are exactly the semisimplified Temperley–Lieb morphisms `[a] → [b]`: a morphism
`[a] → [b]` composed with the caps/cups that pad both sides to `N + 1` strands.

* `TLObj T hε N`: objects are strand labels `a ≤ N`; composition is multiplication in `Q N`;
  the identity of `[a]` is `P a N`. This is a `CategoryTheory.Category` instance.
* `stab`: the cup map `capEmb` induces a functor `TLObj N ⥤ TLObj (N + 2)` that is the
  identity on objects. It is **full and faithful** (`stab_full`, `stab_faithful`). So the hom
  space `Hom(a, b)` does not depend on the ambient `N`, as long as `a, b ≤ N`.

Faithfulness uses `negl_capEmb_iff` (the cup map is injective on the quotient). Fullness uses
`corner_surj` (Jones' lemma).

Not proved here: the braiding and the modular data on this category.

No empirical input; everything is over an arbitrary field.

-- Ref: [jones1983] Index for subfactors, §4 (the basic construction and `e x e = E(x) e`).
-- Ref: [leitner2026] the Temperley–Lieb chapter (bean `hkmt`).
-/

namespace QOU.HeckeTemperleyLieb.TLRectHom

open CategoryTheory
open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebMarkov
open QOU.HeckeTemperleyLieb.TLCable QOU.HeckeTemperleyLieb.TLSemisimpleQuotient
open QOU.HeckeTemperleyLieb.TLCupCap QOU.HeckeTemperleyLieb.TLNegligible

/-! ## The strand idempotents -/

section Idem

variable {K : Type*} [Field K] (δ : K)

/-- `P a N`: the object `[a]` (`a + 1` strands) inside `TL_{N+1}`. -/
noncomputable def P (a : ℕ) : (N : ℕ) → TLFin K δ N
  | 0 => if a = 0 then 1 else 0
  | 1 => if a = 1 then 1 else 0
  | n + 1 + 1 => if a = n + 1 + 1 then 1 else capEmb δ n (P a n)

theorem P_self (a : ℕ) : P δ a a = 1 := by
  match a with
  | 0 => simp [P]
  | 1 => simp [P]
  | n + 1 + 1 => simp [P]

theorem P_succ_succ {a n : ℕ} (h : a ≠ n + 1 + 1) : P δ a (n + 1 + 1) = capEmb δ n (P δ a n) := by
  simp [P, h]

theorem P_eq_zero_of_lt {a : ℕ} : ∀ N, N < a → P δ a N = 0
  | 0, h => by simp [P]; omega
  | 1, h => by simp [P]; omega
  | n + 1 + 1, h => by
    rw [P_succ_succ δ (by omega), P_eq_zero_of_lt n (by omega), capEmb_zero]

theorem P_idem (hδ : δ ≠ 0) (a : ℕ) : ∀ N, P δ a N * P δ a N = P δ a N
  | 0 => by unfold P; split_ifs <;> simp
  | 1 => by unfold P; split_ifs <;> simp
  | n + 1 + 1 => by
    by_cases h : a = n + 1 + 1
    · rw [h, P_self, one_mul]
    · rw [P_succ_succ δ h, ← capEmb_mul δ hδ, P_idem hδ a n]

end Idem

/-! ## The cup map on the quotient -/

section Quotient

variable {K : Type*} [Field K] {δ ε : K} (T : MarkovTower δ ε) (hε : δ * ε = 1)

/-- The cup map, descended to the quotient by negligibles. -/
noncomputable def capQ (n : ℕ) : Q T n → Q T (n + 1 + 1) :=
  Quotient.lift (fun x => ((capEmb δ n x : TLFin K δ (n + 1 + 1)) : Q T (n + 1 + 1)))
    (fun x y h => (coe_capEmb_eq_iff T hε x y).mpr ((RingCon.eq _).mpr h))

theorem capQ_coe (n : ℕ) (x : TLFin K δ n) :
    capQ T hε n (x : Q T n) = (capEmb δ n x : Q T (n + 1 + 1)) := rfl

theorem capQ_mul (n : ℕ) (φ ψ : Q T n) :
    capQ T hε n (φ * ψ) = capQ T hε n φ * capQ T hε n ψ := by
  obtain ⟨x, rfl⟩ := coe_surj T φ
  obtain ⟨y, rfl⟩ := coe_surj T ψ
  rw [← RingCon.coe_mul, capQ_coe, capQ_coe, capQ_coe, capEmb_mul δ (left_ne_zero_of_mul_eq_one hε),
    RingCon.coe_mul]

theorem capQ_add (n : ℕ) (φ ψ : Q T n) :
    capQ T hε n (φ + ψ) = capQ T hε n φ + capQ T hε n ψ := by
  obtain ⟨x, rfl⟩ := coe_surj T φ
  obtain ⟨y, rfl⟩ := coe_surj T ψ
  rw [← RingCon.coe_add, capQ_coe, capQ_coe, capQ_coe, capEmb_add, RingCon.coe_add]

theorem capQ_smul (n : ℕ) (c : K) (φ : Q T n) :
    capQ T hε n (c • φ) = c • capQ T hε n φ := by
  obtain ⟨x, rfl⟩ := coe_surj T φ
  rw [← coe_smul', capQ_coe, capQ_coe, capEmb_smul, coe_smul']

theorem capQ_injective (n : ℕ) : Function.Injective (capQ T hε n) := by
  intro φ ψ h
  obtain ⟨x, rfl⟩ := coe_surj T φ
  obtain ⟨y, rfl⟩ := coe_surj T ψ
  exact (coe_capEmb_eq_iff T hε x y).mp h

/-- `[a]` in the quotient. -/
noncomputable abbrev PQ (a N : ℕ) : Q T N := (P δ a N : Q T N)

include hε in
theorem PQ_idem (a N : ℕ) : PQ T a N * PQ T a N = PQ T a N := by
  rw [PQ, ← RingCon.coe_mul, P_idem δ (left_ne_zero_of_mul_eq_one hε)]

theorem capQ_PQ {a n : ℕ} (h : a ≠ n + 1 + 1) : capQ T hε n (PQ T a n) = PQ T a (n + 1 + 1) := by
  rw [PQ, capQ_coe, PQ, P_succ_succ δ h]

/-! ## The hom spaces -/

/-- **`Hom(a, b)` inside `N + 1` strands**: the corner `[b] · Q N · [a]`. -/
def HomSp (N a b : ℕ) : Submodule K (Q T N) where
  carrier := {φ | PQ T b N * φ * PQ T a N = φ}
  zero_mem' := by simp
  add_mem' := by
    intro φ ψ hφ hψ
    simp only [Set.mem_setOf_eq] at *
    rw [mul_add, add_mul, hφ, hψ]
  smul_mem' := by
    intro c φ hφ
    simp only [Set.mem_setOf_eq] at *
    rw [mul_smul_comm, smul_mul_assoc, hφ]

theorem mem_Hom {N a b : ℕ} {φ : Q T N} : φ ∈ HomSp T N a b ↔ PQ T b N * φ * PQ T a N = φ :=
  Iff.rfl

include hε in
theorem left_mul_of_mem {N a b : ℕ} {φ : Q T N} (h : φ ∈ HomSp T N a b) : PQ T b N * φ = φ := by
  conv_lhs => rw [← (mem_Hom T).mp h]
  rw [← mul_assoc, ← mul_assoc, PQ_idem T hε, (mem_Hom T).mp h]

include hε in
theorem right_mul_of_mem {N a b : ℕ} {φ : Q T N} (h : φ ∈ HomSp T N a b) : φ * PQ T a N = φ := by
  conv_lhs => rw [← (mem_Hom T).mp h]
  rw [mul_assoc, PQ_idem T hε, (mem_Hom T).mp h]

include hε in
theorem id_mem (N a : ℕ) : PQ T a N ∈ HomSp T N a a := by
  rw [mem_Hom, PQ_idem T hε, PQ_idem T hε]

include hε in
theorem comp_mem {N a b c : ℕ} {φ ψ : Q T N} (hφ : φ ∈ HomSp T N a b) (hψ : ψ ∈ HomSp T N b c) :
    ψ * φ ∈ HomSp T N a c := by
  rw [mem_Hom, ← mul_assoc, left_mul_of_mem T hε hψ, mul_assoc, right_mul_of_mem T hε hφ]

/-- **The cup map identifies the hom spaces at `N` and `N + 2`.** For `a, b ≤ N`, `capQ` maps
`Hom N a b` bijectively onto `Hom (N + 2) a b`. -/
theorem capQ_mem {N a b : ℕ} (ha : a ≤ N) (hb : b ≤ N) {φ : Q T N} (h : φ ∈ HomSp T N a b) :
    capQ T hε N φ ∈ HomSp T (N + 1 + 1) a b := by
  rw [mem_Hom, ← capQ_PQ T hε (a := a) (by omega), ← capQ_PQ T hε (a := b) (by omega),
    ← capQ_mul, ← capQ_mul, (mem_Hom T).mp h]

theorem capQ_surj {N a b : ℕ} (ha : a ≤ N) (hb : b ≤ N) {ψ : Q T (N + 1 + 1)}
    (h : ψ ∈ HomSp T (N + 1 + 1) a b) : ∃ φ ∈ HomSp T N a b, capQ T hε N φ = ψ := by
  have hδ : δ ≠ 0 := left_ne_zero_of_mul_eq_one hε
  obtain ⟨z, rfl⟩ := coe_surj T ψ
  obtain ⟨c, hc⟩ := corner_surj δ N z
  have hP : ∀ x : ℕ, x ≤ N → (PQ T x (N + 1 + 1)) =
      (capEmb δ N (P δ x N) : Q T (N + 1 + 1)) := fun x hx => by
    rw [PQ, P_succ_succ δ (by omega)]
  have hP1 : ∀ x : ℕ, x ≤ N → capEmb δ N (P δ x N) =
      capEmb δ N (P δ x N) * capEmb δ N 1 := fun x _ => by
    rw [← capEmb_mul δ hδ, mul_one]
  have hP2 : ∀ x : ℕ, x ≤ N → capEmb δ N (P δ x N) =
      capEmb δ N 1 * capEmb δ N (P δ x N) := fun x _ => by
    rw [← capEmb_mul δ hδ, one_mul]
  refine ⟨PQ T b N * (c : Q T N) * PQ T a N, ?_, ?_⟩
  · rw [mem_Hom, ← mul_assoc, ← mul_assoc, PQ_idem T hε, mul_assoc, PQ_idem T hε, mul_assoc]
  · rw [← (mem_Hom T).mp h, hP a ha, hP b hb, PQ, PQ, ← RingCon.coe_mul, ← RingCon.coe_mul,
      capQ_coe, capEmb_mul δ hδ, capEmb_mul δ hδ, hP1 b hb, hP2 a ha, ← hc, ← RingCon.coe_mul,
      ← RingCon.coe_mul]
    have hEE : ∀ X, capEmb δ N 1 * (capEmb δ N 1 * X) = capEmb δ N 1 * X := fun X => by
      rw [← mul_assoc, capEmb_one_idem δ hδ]
    congr 1
    simp only [mul_assoc, hEE]

/-! ## The category -/

/-- **Objects of the truncated semisimplified category**: strand labels `a ≤ N`. -/
structure TLObj (T : MarkovTower δ ε) (hε : δ * ε = 1) (N : ℕ) where
  /-- The object `[a]` has `a + 1` strands. -/
  a : ℕ
  le : a ≤ N

/-- **The semisimplified Temperley–Lieb category on at most `N + 1` strands.** -/
noncomputable instance (N : ℕ) : Category (TLObj T hε N) where
  Hom X Y := ↥(HomSp T N X.a Y.a)
  id X := ⟨PQ T X.a N, id_mem T hε N X.a⟩
  comp f g := ⟨g.1 * f.1, comp_mem T hε f.2 g.2⟩
  id_comp f := Subtype.ext (right_mul_of_mem T hε f.2)
  comp_id f := Subtype.ext (left_mul_of_mem T hε f.2)
  assoc f g h := Subtype.ext (mul_assoc h.1 g.1 f.1).symm

variable {T hε} in
/-- The underlying element of a morphism. -/
def val {N : ℕ} {X Y : TLObj T hε N} (f : X ⟶ Y) : Q T N :=
  (show ↥(HomSp T N X.a Y.a) from f).1

variable {T hε} in
theorem val_mem {N : ℕ} {X Y : TLObj T hε N} (f : X ⟶ Y) : val f ∈ HomSp T N X.a Y.a :=
  (show ↥(HomSp T N X.a Y.a) from f).2

variable {T hε} in
/-- A morphism from an element of the hom space. -/
def mkHom {N : ℕ} {X Y : TLObj T hε N} (φ : Q T N) (h : φ ∈ HomSp T N X.a Y.a) : X ⟶ Y :=
  (⟨φ, h⟩ : ↥(HomSp T N X.a Y.a))

variable {T hε} in
theorem hom_ext {N : ℕ} {X Y : TLObj T hε N} {f g : X ⟶ Y} (h : val f = val g) : f = g :=
  Subtype.ext h

theorem val_id {N : ℕ} (X : TLObj T hε N) : val (𝟙 X) = PQ T X.a N := rfl

theorem val_comp {N : ℕ} {X Y Z : TLObj T hε N} (f : X ⟶ Y) (g : Y ⟶ Z) :
    val (f ≫ g) = val g * val f := rfl

/-- **Adding two strands.** The cup map is a functor `TLObj N ⥤ TLObj (N + 2)`, the identity on
objects. -/
noncomputable def stab (N : ℕ) : TLObj T hε N ⥤ TLObj T hε (N + 1 + 1) where
  obj X := ⟨X.a, by have := X.le; omega⟩
  map {X Y} f := mkHom (capQ T hε N (val f)) (capQ_mem T hε X.le Y.le (val_mem f))
  map_id X := hom_ext (capQ_PQ T hε (by have := X.le; omega))
  map_comp f g := hom_ext (capQ_mul T hε N (val g) (val f))

/-- **The hom spaces do not depend on the ambient strand count: `stab` is faithful.** -/
instance stab_faithful (N : ℕ) : (stab T hε N).Faithful where
  map_injective h := hom_ext (capQ_injective T hε N (congrArg val h))

/-- **`stab` is full.** -/
instance stab_full (N : ℕ) : (stab T hε N).Full where
  map_surjective {X Y} g := by
    obtain ⟨φ, hφ, hφg⟩ := capQ_surj T hε X.le Y.le (val_mem g)
    exact ⟨mkHom φ hφ, hom_ext hφg⟩

end Quotient

end QOU.HeckeTemperleyLieb.TLRectHom
