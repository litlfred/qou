import QOU.Core.ErrorFiltration
import QOU.BringsSurface.DominationSqueeze

/-!
# QOU.Core.ErrorDepth — error order, the squeeze and the jet valuation are one object

Companion to `QOU.Core.ErrorFiltration`. Three error notions in the corpus are
instances of a single construction:

* the **error filtration** of `QOU.Core.ErrorFiltration` ("`x − y ∈ F n`", the adic
  instance of the cut core);
* the **squeeze** of `QOU.BringsSurface.DominationSqueeze` (a valuation `val` with the
  ultrametric bound; a strictly dominant term cannot be cancelled);
* the **jet valuation** `jetVal` (order of vanishing of a coefficient sequence).

The construction: an antitone tower of additive subgroups `F 0 = ⊤ ⊇ F 1 ⊇ …` has a
**depth** `depth x = sup {n | x ∈ F n} ∈ ℕ ∪ {⊤}`, characterised by
`n ≤ depth x ↔ x ∈ F n` (`coe_le_depth_iff`). The depth is a `Domination`
(`toDomination`), so the squeeze lemmas apply to any filtered error.

* For an error filtration, "agree to order `n`" is `n ≤ depth (x − y)`
  (`near_iff_le_depth`), and depth is super-additive under products
  (`le_depth_mul`).
* The jet valuation is the depth of the "vanishing below `n`" tower
  (`jetFiltration_depth`), so `jetDomination` is this construction
  (`jetDomination_val_eq`). `DominationSqueeze` listed "any `ℕ`-filtered ring, via
  `val x = sup {n | x ∈ Fⁿ}`" as an instance in prose; this file proves it.
* Squeeze for errors (`depth_add_of_lt`): a term of exact depth `d` plus an error of
  order `n > d` has depth `d` and is non-zero.

No `sorry`, no axiom beyond Lean's three, no empirical value.
-/

namespace QOU.Core.Error

open QOU.AlgebraicSubstrate

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

/-- **Every filtration is a domination structure.** The squeeze lemmas of
`DominationSqueeze` (`val_add_eq_of_lt`, `add_ne_zero_of_val_lt`, …) apply to the
depth of any filtered error. -/
noncomputable def toDomination : Domination A ℕ where
  val := E.depth
  val_zero := E.depth_zero
  val_neg := E.depth_neg
  le_val_add := E.min_depth_le_depth_add

/-- **Squeeze for errors.** A term of exact depth `d` perturbed by an error of order
`n > d` keeps depth `d` and cannot vanish. -/
theorem depth_add_of_lt {x e : A} {d n : ℕ} (hx : E.depth x = (d : WithTop ℕ)) (he : e ∈ E.F n)
    (hdn : d < n) : E.depth (x + e) = d ∧ x + e ≠ 0 := by
  have hlt : E.toDomination.val x < E.toDomination.val e := by
    show E.depth x < E.depth e
    rw [hx]
    exact lt_of_lt_of_le (WithTop.coe_lt_coe.mpr hdn) (E.coe_le_depth_iff.mpr he)
  exact ⟨(E.toDomination.val_add_eq_of_lt hlt).trans hx,
    E.toDomination.add_ne_zero_of_val_lt hlt⟩

end AddFiltration

/-! ### Error filtrations -/

namespace ErrorFiltration

variable {R : Type*} [CommRing R] (E : ErrorFiltration R)

/-- The additive tower underlying an error filtration. -/
def toAddFiltration : AddFiltration R where
  F n := (E.F n).toAddSubgroup
  anti _ _ h _ hx := E.anti h hx
  zero_top := by ext x; simp [E.zero_top]

/-- Error depth: the order to which `x` vanishes. -/
noncomputable def depth (x : R) : WithTop ℕ := E.toAddFiltration.depth x

theorem coe_le_depth_iff {x : R} {n : ℕ} : (n : WithTop ℕ) ≤ E.depth x ↔ x ∈ E.F n :=
  E.toAddFiltration.coe_le_depth_iff

/-- "Agree to order `n`" is "the difference has depth at least `n`". -/
theorem near_iff_le_depth {n : ℕ} {x y : R} :
    E.near.near ⟨n⟩ x y ↔ (n : WithTop ℕ) ≤ E.depth (x - y) :=
  (E.coe_le_depth_iff).symm

/-- **Depth is super-additive under products**: orders of errors add. -/
theorem le_depth_mul (x y : R) : E.depth x + E.depth y ≤ E.depth (x * y) := by
  induction hx : E.depth x using WithTop.recTopCoe with
  | top =>
    rw [top_add]
    refine withTop_le_of_forall fun _ _ => E.coe_le_depth_iff.mpr ?_
    exact Ideal.mul_mem_right y _ (E.coe_le_depth_iff.mp (hx ▸ le_top))
  | coe a =>
    induction hy : E.depth y using WithTop.recTopCoe with
    | top =>
      rw [add_top]
      refine withTop_le_of_forall fun _ _ => E.coe_le_depth_iff.mpr ?_
      exact Ideal.mul_mem_left _ x (E.coe_le_depth_iff.mp (hy ▸ le_top))
    | coe b =>
      rw [← WithTop.coe_add, ← castTop, E.coe_le_depth_iff]
      exact E.mul_mem (E.coe_le_depth_iff.mp (by rw [hx, castTop]))
        (E.coe_le_depth_iff.mp (by rw [hy, castTop]))

end ErrorFiltration

/-! ### The jet valuation is a depth -/

/-- Coefficient sequences vanishing below index `n`. -/
def vanishBelow (n : ℕ) : AddSubgroup (ℕ → ℝ) where
  carrier := {f | ∀ m < n, f m = 0}
  zero_mem' _ _ := rfl
  add_mem' ha hb m hm := by simp [ha m hm, hb m hm]
  neg_mem' ha m hm := by simp [ha m hm]

/-- The jet tower: order of vanishing at `q = 1`. -/
def jetFiltration : AddFiltration (ℕ → ℝ) where
  F := vanishBelow
  anti _ _ h _ hf m hm := hf m (lt_of_lt_of_le hm h)
  zero_top := by ext f; simp [vanishBelow]

/-- **The jet valuation is the depth of the jet tower.** -/
theorem jetFiltration_depth (f : ℕ → ℝ) : jetFiltration.depth f = jetVal f := by
  refine withTop_eq_of_forall fun n => ?_
  rw [AddFiltration.coe_le_depth_iff]
  show (∀ m < n, f m = 0) ↔ _
  constructor
  · intro hf
    induction hj : jetVal f using WithTop.recTopCoe with
    | top => exact le_top
    | coe m =>
      have hm := ne_zero_of_jetVal_eq hj
      rw [castTop]
      exact WithTop.coe_le_coe.mpr (not_lt.mp fun hlt => hm (hf m hlt))
  · intro hn m hm
    exact eq_zero_of_lt_jetVal (lt_of_lt_of_le (WithTop.coe_lt_coe.mpr hm) hn)

/-- So the squeeze's jet instance `jetDomination` is the depth construction. -/
theorem jetDomination_val_eq (f : ℕ → ℝ) :
    jetDomination.val f = jetFiltration.toDomination.val f :=
  (jetFiltration_depth f).symm

end QOU.Core.Error
