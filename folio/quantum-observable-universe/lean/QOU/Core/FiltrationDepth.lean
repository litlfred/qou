import Mathlib.Algebra.Group.Subgroup.Lattice
import Mathlib.Algebra.Order.Monoid.Unbundled.WithTop
import Mathlib.Data.Nat.Find

/-!
# QOU.Core.FiltrationDepth — the depth of a filtered element

This is the shared core under the squeeze (`QOU.BringsSurface.DominationSqueeze`), the
jet valuation, and the error filtration (`QOU.Core.ErrorFiltration`,
`QOU.Core.ErrorDepth`).

Let `F 0 = ⊤ ⊇ F 1 ⊇ …` be an antitone tower of additive subgroups. Its
**depth** is `depth x = sup {n | x ∈ F n} ∈ ℕ ∪ {⊤}`, characterised by
`n ≤ depth x ↔ x ∈ F n` (`coe_le_depth_iff`). Depth is unchanged by negation, and is
at least the minimum depth of two summands. These are exactly the axioms of a
`Domination`.

The jet tower (`jetFiltration`) is the tower of coefficient sequences vanishing
below `n`. Its depth is the order of vanishing, `jetVal`
(`QOU.AlgebraicSubstrate.jetFiltration_depth`).

No order, no field, no `ℝ`. No `sorry`, no axiom beyond Lean's three.
-/

namespace QOU.Core.Error

/-- The cast `ℕ → ℕ ∪ {⊤}` is the inclusion. -/
theorem castTop (n : ℕ) : (n : WithTop ℕ) = WithTop.some n := rfl

/-- Two elements of `ℕ ∪ {⊤}` compare as their lower sets of naturals do. -/
theorem withTop_le_of_forall {a b : WithTop ℕ}
    (h : ∀ n : ℕ, (n : WithTop ℕ) ≤ a → (n : WithTop ℕ) ≤ b) : a ≤ b := by
  induction a using WithTop.recTopCoe with
  | top =>
    induction b using WithTop.recTopCoe with
    | top => exact le_rfl
    | coe m =>
      have := h (m + 1) le_top
      rw [castTop] at this
      exact absurd (WithTop.coe_le_coe.mp this) (by omega)
  | coe m => exact h m le_rfl

theorem withTop_eq_of_forall {a b : WithTop ℕ}
    (h : ∀ n : ℕ, (n : WithTop ℕ) ≤ a ↔ (n : WithTop ℕ) ≤ b) : a = b :=
  le_antisymm (withTop_le_of_forall fun n => (h n).mp)
    (withTop_le_of_forall fun n => (h n).mpr)

/-- In `ℕ ∪ {⊤}`, being positive is being at least one. -/
theorem withTop_pos_iff {a : WithTop ℕ} : 0 < a ↔ ((1 : ℕ) : WithTop ℕ) ≤ a := by
  induction a using WithTop.recTopCoe with
  | top => simp
  | coe m =>
    rw [castTop, WithTop.coe_le_coe, show (0 : WithTop ℕ) = WithTop.some 0 from rfl,
      WithTop.coe_lt_coe]
    omega

/-- An antitone tower of additive subgroups starting at `⊤`. -/
structure AddFiltration (A : Type*) [AddCommGroup A] where
  F : ℕ → AddSubgroup A
  anti : Antitone F
  zero_top : F 0 = ⊤

namespace AddFiltration

variable {A : Type*} [AddCommGroup A] (E : AddFiltration A)

open Classical in
/-- Depth of `x`: the largest `n` with `x ∈ F n`, or `⊤` if `x` lies in every level. -/
noncomputable def depth (x : A) : WithTop ℕ :=
  if h : ∃ n, x ∉ E.F (n + 1) then ((Nat.find h : ℕ) : WithTop ℕ) else ⊤

/-- **Characterisation of depth.** -/
theorem coe_le_depth_iff {x : A} {n : ℕ} : (n : WithTop ℕ) ≤ E.depth x ↔ x ∈ E.F n := by
  classical
  unfold depth
  split_ifs with h
  · rw [castTop, castTop, WithTop.coe_le_coe]
    constructor
    · intro hn
      rcases n with _ | m
      · simp [E.zero_top]
      · by_contra hx
        exact Nat.find_min h (by omega) hx
    · intro hx
      by_contra hlt
      exact Nat.find_spec h (E.anti (show Nat.find h + 1 ≤ n by omega) hx)
  · push_neg at h
    simp only [le_top, true_iff]
    rcases n with _ | m
    · simp [E.zero_top]
    · exact h m

theorem depth_zero : E.depth 0 = ⊤ :=
  withTop_eq_of_forall fun n => by simp [coe_le_depth_iff, zero_mem]

theorem depth_neg (x : A) : E.depth (-x) = E.depth x :=
  withTop_eq_of_forall fun n => by rw [coe_le_depth_iff, coe_le_depth_iff, neg_mem_iff]

theorem min_depth_le_depth_add (x y : A) : min (E.depth x) (E.depth y) ≤ E.depth (x + y) :=
  withTop_le_of_forall fun _ hn => E.coe_le_depth_iff.mpr <|
    add_mem (E.coe_le_depth_iff.mp (hn.trans (min_le_left _ _)))
      (E.coe_le_depth_iff.mp (hn.trans (min_le_right _ _)))

/-- Positive depth is membership in the first level. -/
theorem depth_pos_iff {x : A} : 0 < E.depth x ↔ x ∈ E.F 1 := by
  rw [withTop_pos_iff, coe_le_depth_iff]

end AddFiltration

/-- Coefficient sequences vanishing below index `n`. -/
def vanishBelow (M : Type*) [AddCommGroup M] (n : ℕ) : AddSubgroup (ℕ → M) where
  carrier := {f | ∀ m < n, f m = 0}
  zero_mem' _ _ := rfl
  add_mem' ha hb m hm := by simp [ha m hm, hb m hm]
  neg_mem' ha m hm := by simp [ha m hm]

/-- The jet tower: order of vanishing of a coefficient sequence. -/
def jetFiltration (M : Type*) [AddCommGroup M] : AddFiltration (ℕ → M) where
  F := vanishBelow M
  anti _ _ h _ hf m hm := hf m (lt_of_lt_of_le hm h)
  zero_top := by ext f; simp [vanishBelow]

end QOU.Core.Error
