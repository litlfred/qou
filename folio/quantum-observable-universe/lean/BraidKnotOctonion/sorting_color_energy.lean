import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Field.Defs
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Group.Units.Basic
import Mathlib.Algebra.GroupWithZero.Basic
import Mathlib.Algebra.Group.Basic
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# QOU.BraidKnot.sorting_color_energy — Hecke eigendecomposition, sorting projectors, and inversion-count crossing energy

**Proposition** ([`prop:sorting-color-energy`](../../../measurement-observation/sorting-color-energy.md)).

*Let `σᵢ` be the Hecke generator acting on `V ⊗ V`. Then:*
1. *(Eigenspace decomposition)* `σᵢ` has eigenvalues `q` (symmetric, ordered) and
   `−q⁻¹` (antisymmetric, disordered) as the unique roots of `(x − q)(x + q⁻¹) = 0`.
2. *(Sorting is projection)* The spectral idempotents
   `e₊ = (σᵢ + q⁻¹)/(q + q⁻¹)` and `e₋ = (q − σᵢ)/(q + q⁻¹)` satisfy
   `e₊ + e₋ = 1`, `e₊ e₋ = 0`, `e₊² = e₊`, and `e₋² = e₋` whenever `σᵢ`
   satisfies the Hecke relation `(σᵢ − q)(σᵢ + q⁻¹) = 0` and `q + q⁻¹ ≠ 0`.
3. *(Energy per crossing)* The eigenvalue gap is `ΔE_colour = q − (−q⁻¹) = q + q⁻¹ ≥ 2`
   (strictly `> 2` for `q > 0, q ≠ 1` over any strict-ordered field).
4. *(Total sorting energy)* For a sequence `w` with inversion count `inv(w)`,
   `E_colour(w) = inv(w) · (q + q⁻¹)`, and swapping an adjacent disordered pair
   `a > b` reduces `inv` by `1` and deposits `q + q⁻¹`.

**Base ring (§7c).** Everything is stated over generic `[CommRing R]` / `[Field K]` /
`[Field K] [LinearOrder K] [IsStrictOrderedRing K]` with **zero `Real` / `ℝ`** imports.

Bean `qou-z9ws`.

-- Ref: [leitner2026] quantum-observable-universe/measurement-observation/sorting-color-energy.md
-/

namespace QOU.BraidKnot

section AlgebraicHeckeRoots

variable {R : Type*} [CommRing R]

/-- **The Hecke relation** at a scalar: `(x − q)(x + q⁻¹) = 0`. -/
-- Ref: [leitner2026] quantum-observable-universe/measurement-observation/sorting-color-energy.md
def heckeRelation (q : Rˣ) (x : R) : Prop :=
  (x - (q : R)) * (x + ((q⁻¹ : Rˣ) : R)) = 0

/-- `q` is a root of the Hecke relation — the symmetric eigenvalue. -/
theorem heckeRelation_q (q : Rˣ) : heckeRelation q (q : R) := by
  simp [heckeRelation]

/-- `−q⁻¹` is a root of the Hecke relation — the antisymmetric eigenvalue. -/
theorem heckeRelation_neg_qInv (q : Rˣ) :
    heckeRelation q (-((q⁻¹ : Rˣ) : R)) := by
  simp [heckeRelation]

/-- **They are the only roots** — over a ring without zero divisors, `q` and `−q⁻¹`
    are the unique roots of the Hecke relation. -/
-- Ref: [leitner2026] quantum-observable-universe/measurement-observation/sorting-color-energy.md
theorem eq_or_eq_of_heckeRelation [NoZeroDivisors R] {q : Rˣ} {x : R}
    (h : heckeRelation q x) :
    x = (q : R) ∨ x = -((q⁻¹ : Rˣ) : R) := by
  rcases mul_eq_zero.mp h with h₁ | h₂
  · exact Or.inl (sub_eq_zero.mp h₁)
  · exact Or.inr (add_eq_zero_iff_eq_neg.mp h₂)

/-- **`NoZeroDivisors` is load-bearing:** counterexample in `ZMod 8` at `q = 1`, `x = 3`. -/
theorem exists_heckeRelation_ne_both_of_zeroDivisors :
    ∃ x : ZMod 8, heckeRelation (1 : (ZMod 8)ˣ) x ∧
      x ≠ ((1 : (ZMod 8)ˣ) : ZMod 8) ∧
      x ≠ -(((1 : (ZMod 8)ˣ)⁻¹ : (ZMod 8)ˣ) : ZMod 8) :=
  ⟨3, by unfold heckeRelation; decide, by decide, by decide⟩

/-- **Eigenspace decomposition with explicit Hecke eigenvalues**
([`prop:sorting-color-energy`] item (1)), as a proposition over caller-supplied data. -/
-- Ref: [leitner2026] quantum-observable-universe/measurement-observation/sorting-color-energy.md
def sorting_color_energy (q : Rˣ) (sym_eigenvalue wedge_eigenvalue : R) : Prop :=
  sym_eigenvalue = (q : R) ∧ wedge_eigenvalue = -((q⁻¹ : Rˣ) : R)

/-- **Item (1), derived** from the Hecke relation and channel separation. -/
-- Ref: [leitner2026] quantum-observable-universe/measurement-observation/sorting-color-energy.md
theorem sorting_color_energy_of_heckeRelation [NoZeroDivisors R] {q : Rˣ}
    {sym_eigenvalue wedge_eigenvalue : R}
    (hsym : heckeRelation q sym_eigenvalue)
    (hwedge : heckeRelation q wedge_eigenvalue)
    (hsym' : sym_eigenvalue ≠ -((q⁻¹ : Rˣ) : R))
    (hwedge' : wedge_eigenvalue ≠ (q : R)) :
    sorting_color_energy q sym_eigenvalue wedge_eigenvalue :=
  ⟨(eq_or_eq_of_heckeRelation hsym).resolve_right hsym',
   (eq_or_eq_of_heckeRelation hwedge).resolve_left hwedge'⟩

/-- Refutability of `sorting_color_energy` at freely-chosen eigenvalues. -/
theorem not_sorting_color_energy_of_free_data :
    ¬ sorting_color_energy (1 : ℤˣ) 0 0 := by
  simp [sorting_color_energy]

end AlgebraicHeckeRoots

/-! ## Items (2) and (3): Spectral idempotents `e₊, e₋` and the crossing-energy gap `q + q⁻¹` -/

section ProjectorsAndEnergyGap

/-- Single-crossing colour energy gap `ΔE_colour = q − (−q⁻¹) = q + q⁻¹` over any field `K`. -/
def crossingEnergyGap {K : Type*} [Field K] (q : K) : K :=
  q - (-q⁻¹)

theorem crossingEnergyGap_eq {K : Type*} [Field K] (q : K) :
    crossingEnergyGap q = q + q⁻¹ := by
  unfold crossingEnergyGap
  ring

/-- Exact AM-GM identity `q + q⁻¹ − 2 = (q − 1)² / q` over any field `K` (`q ≠ 0`). -/
theorem crossingEnergyGap_sub_two_eq {K : Type*} [Field K] {q : K} (hq : q ≠ 0) :
    crossingEnergyGap q - 2 = (q - 1) ^ 2 / q := by
  rw [crossingEnergyGap_eq]
  have hmul : (q + q⁻¹ - 2) * q = (q - 1) ^ 2 := by
    calc
      (q + q⁻¹ - 2) * q = q ^ 2 + q⁻¹ * q - 2 * q := by ring
      _ = q ^ 2 + 1 - 2 * q := by rw [inv_mul_cancel₀ hq]
      _ = (q - 1) ^ 2 := by ring
  exact (eq_div_iff hq).mpr hmul

/-- Over any strict-ordered field `K`, `0 < q + q⁻¹` and `2 ≤ q + q⁻¹` for `q > 0`. -/
theorem crossingEnergyGap_pos {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {q : K} (hq : 0 < q) :
    0 < crossingEnergyGap q := by
  rw [crossingEnergyGap_eq]
  positivity

theorem crossingEnergyGap_ge_two {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {q : K} (hq : 0 < q) :
    2 ≤ crossingEnergyGap q := by
  have hsub : 0 ≤ crossingEnergyGap q - 2 := by
    rw [crossingEnergyGap_sub_two_eq (ne_of_gt hq)]
    positivity
  linarith

theorem crossingEnergyGap_gt_two {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {q : K} (hq : 0 < q) (hne : q ≠ 1) :
    2 < crossingEnergyGap q := by
  have hsub : 0 < crossingEnergyGap q - 2 := by
    rw [crossingEnergyGap_sub_two_eq (ne_of_gt hq)]
    have hsq : 0 < (q - 1) ^ 2 := sq_pos_of_ne_zero (sub_ne_zero.mpr hne)
    exact div_pos hsq hq
  linarith

/-- Symmetric Hecke spectral projector `e₊ = (σ + q⁻¹) / (q + q⁻¹)` over any field `K`. -/
def heckeProjectorSym {K : Type*} [Field K] (q σ : K) : K :=
  (σ + q⁻¹) / (q + q⁻¹)

/-- Antisymmetric Hecke spectral projector `e₋ = (q − σ) / (q + q⁻¹)` over any field `K`. -/
def heckeProjectorWedge {K : Type*} [Field K] (q σ : K) : K :=
  (q - σ) / (q + q⁻¹)

/-- Partition of unity: `e₊ + e₋ = 1` whenever `q + q⁻¹ ≠ 0`. -/
theorem heckeProjector_add_eq_one {K : Type*} [Field K] {q : K}
    (hdenom : q + q⁻¹ ≠ 0) (σ : K) :
    heckeProjectorSym q σ + heckeProjectorWedge q σ = 1 := by
  unfold heckeProjectorSym heckeProjectorWedge
  rw [← add_div]
  have hnum : σ + q⁻¹ + (q - σ) = q + q⁻¹ := by ring
  rw [hnum, div_self hdenom]

/-- On the symmetric eigenspace (`σ = q`), `e₊(q) = 1` and `e₋(q) = 0`. -/
theorem heckeProjector_at_sym {K : Type*} [Field K] {q : K} (hdenom : q + q⁻¹ ≠ 0) :
    heckeProjectorSym q q = 1 ∧ heckeProjectorWedge q q = 0 := by
  unfold heckeProjectorSym heckeProjectorWedge
  exact ⟨div_self hdenom, by simp⟩

/-- On the antisymmetric eigenspace (`σ = −q⁻¹`), `e₊(−q⁻¹) = 0` and `e₋(−q⁻¹) = 1`. -/
theorem heckeProjector_at_wedge {K : Type*} [Field K] {q : K} (hdenom : q + q⁻¹ ≠ 0) :
    heckeProjectorSym q (-q⁻¹) = 0 ∧ heckeProjectorWedge q (-q⁻¹) = 1 := by
  unfold heckeProjectorSym heckeProjectorWedge
  refine ⟨by simp, ?_⟩
  have hnum : q - -q⁻¹ = q + q⁻¹ := by ring
  rw [hnum, div_self hdenom]

/-- Orthogonality of the spectral projectors: `(σ − q)(σ + q⁻¹) = 0 ⟹ e₊ e₋ = 0`. -/
theorem heckeProjector_mul_eq_zero {K : Type*} [Field K] {q σ : K}
    (hhecke : (σ - q) * (σ + q⁻¹) = 0) :
    heckeProjectorSym q σ * heckeProjectorWedge q σ = 0 := by
  unfold heckeProjectorSym heckeProjectorWedge
  rw [div_mul_div_comm]
  have hnum : (σ + q⁻¹) * (q - σ) = -((σ - q) * (σ + q⁻¹)) := by ring
  rw [hnum, hhecke, neg_zero, zero_div]

/-- Idempotence of the symmetric projector: `(σ − q)(σ + q⁻¹) = 0 ⟹ e₊² = e₊`. -/
theorem heckeProjectorSym_sq {K : Type*} [Field K] {q σ : K}
    (hdenom : q + q⁻¹ ≠ 0) (hhecke : (σ - q) * (σ + q⁻¹) = 0) :
    (heckeProjectorSym q σ) ^ 2 = heckeProjectorSym q σ := by
  have hsum := heckeProjector_add_eq_one hdenom σ
  have hmul := heckeProjector_mul_eq_zero hhecke
  calc
    (heckeProjectorSym q σ) ^ 2
        = heckeProjectorSym q σ * (heckeProjectorSym q σ + heckeProjectorWedge q σ) -
          heckeProjectorSym q σ * heckeProjectorWedge q σ := by ring
    _ = heckeProjectorSym q σ * 1 - 0 := by rw [hsum, hmul]
    _ = heckeProjectorSym q σ := by ring

/-- Idempotence of the antisymmetric projector: `(σ − q)(σ + q⁻¹) = 0 ⟹ e₋² = e₋`. -/
theorem heckeProjectorWedge_sq {K : Type*} [Field K] {q σ : K}
    (hdenom : q + q⁻¹ ≠ 0) (hhecke : (σ - q) * (σ + q⁻¹) = 0) :
    (heckeProjectorWedge q σ) ^ 2 = heckeProjectorWedge q σ := by
  have hsum := heckeProjector_add_eq_one hdenom σ
  have hmul := heckeProjector_mul_eq_zero hhecke
  calc
    (heckeProjectorWedge q σ) ^ 2
        = (heckeProjectorSym q σ + heckeProjectorWedge q σ) * heckeProjectorWedge q σ -
          heckeProjectorSym q σ * heckeProjectorWedge q σ := by ring
    _ = 1 * heckeProjectorWedge q σ - 0 := by rw [hsum, hmul]
    _ = heckeProjectorWedge q σ := by ring

end ProjectorsAndEnergyGap

/-! ## Item (4): Inversion count `inv(w)` and total colour-sorting energy `inv(w) · (q + q⁻¹)` -/

section InversionSortingEnergy

/-- Number of elements in `xs` strictly smaller than `x` (inversions anchored at head `x`). -/
def countInversionsWith (x : ℕ) (xs : List ℕ) : ℕ :=
  (xs.filter (fun y => y < x)).length

/-- Combinatorial inversion count `inv(w)` of a sequence `w`. -/
def inversionCount : List ℕ → ℕ
  | [] => 0
  | x :: xs => countInversionsWith x xs + inversionCount xs

/-- Total energy deposited in the colour fibre when sorting `w`, over any `[CommRing R]`
    with unit `q : Rˣ`: `E_colour(w) = inv(w) · (q + q⁻¹)`. -/
def sortingColorEnergyTotal {R : Type*} [CommRing R] (q : Rˣ) (w : List ℕ) : R :=
  (inversionCount w : R) * ((q : R) + ((q⁻¹ : Rˣ) : R))

theorem sortingColorEnergyTotal_nil {R : Type*} [CommRing R] (q : Rˣ) :
    sortingColorEnergyTotal q [] = 0 := by
  simp [sortingColorEnergyTotal, inversionCount]

theorem countInversionsWith_cons (x y : ℕ) (xs : List ℕ) :
    countInversionsWith x (y :: xs) =
      (if y < x then 1 else 0) + countInversionsWith x xs := by
  unfold countInversionsWith
  by_cases h : y < x
  · simp [List.filter, h, Nat.add_comm]
  · simp [List.filter, h]

/-- **Adjacent transposition step**: when `b < a`, swapping the disordered adjacent pair `a, b`
    at the head of `a :: b :: xs` to `b :: a :: xs` decreases `inversionCount` by `1`. -/
theorem inversionCount_swap_adj {a b : ℕ} (hab : b < a) (xs : List ℕ) :
    inversionCount (a :: b :: xs) = inversionCount (b :: a :: xs) + 1 := by
  have hnot : ¬ (a < b) := Nat.not_lt_of_gt hab
  simp only [inversionCount, countInversionsWith_cons, if_pos hab, if_neg hnot]
  omega

/-- **Energy per sorting swap**: sorting one adjacent disordered pair `a > b` reduces the remaining
    sorting energy by one crossing quantum `q + q⁻¹` in any commutative ring `R`. -/
theorem sortingColorEnergyTotal_swap_adj {R : Type*} [CommRing R] (q : Rˣ)
    {a b : ℕ} (hab : b < a) (xs : List ℕ) :
    sortingColorEnergyTotal q (a :: b :: xs) =
      sortingColorEnergyTotal q (b :: a :: xs) + ((q : R) + ((q⁻¹ : Rˣ) : R)) := by
  simp only [sortingColorEnergyTotal, inversionCount_swap_adj hab xs, Nat.cast_add, Nat.cast_one]
  ring

/-- Verification of the six permutations of `S₃` in `tbl:sorting-color-energy-table-data`. -/
theorem three_socks_inversion_table :
    inversionCount [1, 2, 3] = 0 ∧
    inversionCount [1, 3, 2] = 1 ∧
    inversionCount [2, 1, 3] = 1 ∧
    inversionCount [2, 3, 1] = 2 ∧
    inversionCount [3, 1, 2] = 2 ∧
    inversionCount [3, 2, 1] = 3 := by
  decide

end InversionSortingEnergy

end QOU.BraidKnot
