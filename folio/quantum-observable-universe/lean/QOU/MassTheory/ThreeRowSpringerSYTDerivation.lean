import QOU.MassTheory.ThreeRowExtensiveCumulant
import QOU.BraidsAndKnots.DeltaLambdaDTIndexGeneralN
import QOU.Mathlib.IdentityIHLFBridge

/-!
# Closing the `sRow3` Derivation Seam: `≥ 3`-Row Signed Dimension Table from `dimHLF` & `nStatList` (`qou-jkmh`)

In `QOU.MassTheory.ThreeRowExtensiveCumulant` (lines 49–56), `sRow3 : ℕ → ℤ` was entered as a
literal lookup table (`3 ↦ -1`, `4 ↦ -2`, `5 ↦ 4`, `_ ↦ 0`), with an explicit derivation-seam
note recording that the identity

    sRow3 k = Σ_{λ ⊢ k, ℓ(λ) ≥ 3} (-1)^{n(λ)} · f^λ

was checked in a companion Python script rather than derived in Lean from the hook-length
formula and the graded Euler characteristic.

This module closes that seam in Lean (`0 sorry`, `0 axiom`) by combining three already-proved
pillars of the `QOU` library:
1. The general single-degree graded Euler characteristic `QOU.BraidsAndKnots.dtEulerG`, its
   collapse theorem `dtEulerG_collapse`, and the general partition statistic `nStatList`
   from `QOU.BraidsAndKnots.DeltaLambdaDTIndexGeneralN`;
2. The computable hook-length dimension `QOU.BraidKnot.IdentityI.dimHLF` and fuel-based
   partition enumerator `QOU.BraidKnot.IdentityI.partitionsOf` from
   `QOU.BraidKnot.IdentityIContentDecomposition`;
3. The proved bridge `QOU.Mathlib.dimSYT_eq_dimHLF` from `QOU.Mathlib.IdentityIHLFBridge`,
   which equates the genuine `StandardYoungTableau` cardinality `dimSYT p` to
   `dimHLF (p.parts.sort (· ≥ ·))` for every `p : Nat.Partition n`.
-/

namespace QOU.MassTheory.ThreeRowSpringerSYTDerivation

open QOU.MassTheory.ThreeRowExtensiveCumulant
open QOU.BraidsAndKnots
open QOU.BraidKnot.IdentityI
open QOU.Mathlib

/-! ## 1. General Per-Partition Signed Dimension Functional from `dtEulerG`, `nStatList`, and `dimHLF` -/

/-- Per-partition signed dimension evaluated via the single-degree graded sum `dtEulerG`
    at grade `nStatList lam` and hook-length dimension `dimHLF lam`. -/
def deltaLambdaHLF (lam : List ℕ) : ℤ :=
  dtEulerG (nStatList lam) (dimHLF lam)

/-- `deltaLambdaHLF` agrees with `deltaLambdaG` at grade `nStatList lam` and dimension `dimHLF lam`. -/
theorem deltaLambdaHLF_eq_deltaLambdaG (lam : List ℕ) :
    deltaLambdaHLF lam = deltaLambdaG (nStatList lam) (dimHLF lam) :=
  dtEulerG_eq_deltaLambdaG (nStatList lam) (dimHLF lam)

/-- By `dtEulerG_collapse`, `deltaLambdaHLF lam` collapses for every `lam : List ℕ` to
    `(-1 : ℤ) ^ (nStatList lam) * (dimHLF lam : ℤ)`. -/
theorem deltaLambdaHLF_eq_signed_dimHLF (lam : List ℕ) :
    deltaLambdaHLF lam = (-1 : ℤ) ^ (nStatList lam) * (dimHLF lam : ℤ) :=
  dtEulerG_collapse (nStatList lam) (dimHLF lam)

/-- For any `p : Nat.Partition n`, `deltaLambdaHLF` on the sorted part list `p.parts.sort (· ≥ ·)`
    equals `(-1) ^ nStatList (p.parts.sort (· ≥ ·))` times the genuine tableau count `dimSYT p`,
    via `dimSYT_eq_dimHLF`. -/
theorem deltaLambdaHLF_sort_eq_signed_dimSYT {n : ℕ} (p : Nat.Partition n) :
    deltaLambdaHLF (p.parts.sort (· ≥ ·)) =
      (-1 : ℤ) ^ (nStatList (p.parts.sort (· ≥ ·))) * (dimSYT p : ℤ) := by
  rw [deltaLambdaHLF_eq_signed_dimHLF, dimSYT_eq_dimHLF]

/-! ## 2. Exact `dimHLF`, `nStatList`, and `deltaLambdaHLF` for All `≥ 3`-Row Partitions of `k ≤ 5` -/

/-- Hook-length dimension `dimHLF [1, 1, 1] = 1` for `λ = (1³) ⊢ 3`. -/
theorem dimHLF_111 : dimHLF [1, 1, 1] = 1 := by decide

/-- Grade statistic `nStatList [1, 1, 1] = 3` for `λ = (1³) ⊢ 3`. -/
theorem nStatList_111 : nStatList [1, 1, 1] = 3 := by decide

/-- Signed dimension `deltaLambdaHLF [1, 1, 1] = -1` for `λ = (1³) ⊢ 3`. -/
theorem deltaLambdaHLF_111 : deltaLambdaHLF [1, 1, 1] = -1 := by decide

/-- Hook-length dimension `dimHLF [2, 1, 1] = 3` for `λ = (2, 1, 1) ⊢ 4`. -/
theorem dimHLF_211 : dimHLF [2, 1, 1] = 3 := by decide

/-- Grade statistic `nStatList [2, 1, 1] = 3` for `λ = (2, 1, 1) ⊢ 4`. -/
theorem nStatList_211 : nStatList [2, 1, 1] = 3 := by decide

/-- Signed dimension `deltaLambdaHLF [2, 1, 1] = -3` for `λ = (2, 1, 1) ⊢ 4`. -/
theorem deltaLambdaHLF_211 : deltaLambdaHLF [2, 1, 1] = -3 := by decide

/-- Hook-length dimension `dimHLF [1, 1, 1, 1] = 1` for `λ = (1⁴) ⊢ 4`. -/
theorem dimHLF_1111 : dimHLF [1, 1, 1, 1] = 1 := by decide

/-- Grade statistic `nStatList [1, 1, 1, 1] = 6` for `λ = (1⁴) ⊢ 4`. -/
theorem nStatList_1111 : nStatList [1, 1, 1, 1] = 6 := by decide

/-- Signed dimension `deltaLambdaHLF [1, 1, 1, 1] = 1` for `λ = (1⁴) ⊢ 4`. -/
theorem deltaLambdaHLF_1111 : deltaLambdaHLF [1, 1, 1, 1] = 1 := by decide

/-- Hook-length dimension `dimHLF [3, 1, 1] = 6` for `λ = (3, 1, 1) ⊢ 5`. -/
theorem dimHLF_311 : dimHLF [3, 1, 1] = 6 := by decide

/-- Grade statistic `nStatList [3, 1, 1] = 3` for `λ = (3, 1, 1) ⊢ 5`. -/
theorem nStatList_311 : nStatList [3, 1, 1] = 3 := by decide

/-- Signed dimension `deltaLambdaHLF [3, 1, 1] = -6` for `λ = (3, 1, 1) ⊢ 5`. -/
theorem deltaLambdaHLF_311 : deltaLambdaHLF [3, 1, 1] = -6 := by decide

/-- Hook-length dimension `dimHLF [2, 2, 1] = 5` for `λ = (2, 2, 1) ⊢ 5`. -/
theorem dimHLF_221 : dimHLF [2, 2, 1] = 5 := by decide

/-- Grade statistic `nStatList [2, 2, 1] = 4` for `λ = (2, 2, 1) ⊢ 5`. -/
theorem nStatList_221 : nStatList [2, 2, 1] = 4 := by decide

/-- Signed dimension `deltaLambdaHLF [2, 2, 1] = 5` for `λ = (2, 2, 1) ⊢ 5`. -/
theorem deltaLambdaHLF_221 : deltaLambdaHLF [2, 2, 1] = 5 := by decide

/-- Hook-length dimension `dimHLF [2, 1, 1, 1] = 4` for `λ = (2, 1³) ⊢ 5`. -/
theorem dimHLF_2111 : dimHLF [2, 1, 1, 1] = 4 := by decide

/-- Grade statistic `nStatList [2, 1, 1, 1] = 6` for `λ = (2, 1³) ⊢ 5`. -/
theorem nStatList_2111 : nStatList [2, 1, 1, 1] = 6 := by decide

/-- Signed dimension `deltaLambdaHLF [2, 1, 1, 1] = 4` for `λ = (2, 1³) ⊢ 5`. -/
theorem deltaLambdaHLF_2111 : deltaLambdaHLF [2, 1, 1, 1] = 4 := by decide

/-- Hook-length dimension `dimHLF [1, 1, 1, 1, 1] = 1` for `λ = (1⁵) ⊢ 5`. -/
theorem dimHLF_11111 : dimHLF [1, 1, 1, 1, 1] = 1 := by decide

/-- Grade statistic `nStatList [1, 1, 1, 1, 1] = 10` for `λ = (1⁵) ⊢ 5`. -/
theorem nStatList_11111 : nStatList [1, 1, 1, 1, 1] = 10 := by decide

/-- Signed dimension `deltaLambdaHLF [1, 1, 1, 1, 1] = 1` for `λ = (1⁵) ⊢ 5`. -/
theorem deltaLambdaHLF_11111 : deltaLambdaHLF [1, 1, 1, 1, 1] = 1 := by decide

/-! ## 3. Complete Partition Tables & First-Principles Derivation of `sRow3` -/

/-- Every list `lam ∈ partitionsOf k` for `k ≤ 5` sums to `k`, is weakly decreasing
    (`lam.Sorted (· ≥ ·)`), and has strictly positive parts (`∀ p ∈ lam, 0 < p`). -/
theorem partitionsOf_valid_le5 (k : ℕ) (hk : k ≤ 5) :
    ∀ lam ∈ partitionsOf k,
      lam.sum = k ∧ lam.Sorted (· ≥ ·) ∧ ∀ p ∈ lam, 0 < p := by
  interval_cases k <;> decide

/-- The `≥ 3`-row stratum of `partitionsOf k`, obtained by filtering for `3 ≤ lam.length`. -/
def threeRowPartitionsOf (k : ℕ) : List (List ℕ) :=
  (partitionsOf k).filter (fun lam => decide (3 ≤ lam.length))

/-- For `k = 0`, `threeRowPartitionsOf 0` is empty. -/
theorem threeRowPartitionsOf_zero : threeRowPartitionsOf 0 = [] := by decide

/-- For `k = 1`, `threeRowPartitionsOf 1` is empty. -/
theorem threeRowPartitionsOf_one : threeRowPartitionsOf 1 = [] := by decide

/-- For `k = 2`, `threeRowPartitionsOf 2` is empty. -/
theorem threeRowPartitionsOf_two : threeRowPartitionsOf 2 = [] := by decide

/-- For `k = 3`, `threeRowPartitionsOf 3` consists of `[1, 1, 1]`. -/
theorem threeRowPartitionsOf_three : threeRowPartitionsOf 3 = [[1, 1, 1]] := by decide

/-- For `k = 4`, `threeRowPartitionsOf 4` consists of `[2, 1, 1]` and `[1, 1, 1, 1]`. -/
theorem threeRowPartitionsOf_four :
    threeRowPartitionsOf 4 = [[2, 1, 1], [1, 1, 1, 1]] := by decide

/-- For `k = 5`, `threeRowPartitionsOf 5` consists of `[3, 1, 1]`, `[2, 2, 1]`,
    `[2, 1, 1, 1]`, and `[1, 1, 1, 1, 1]`. -/
theorem threeRowPartitionsOf_five :
    threeRowPartitionsOf 5 = [[3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]] := by decide

/-- First-principles derived `≥ 3`-row signed dimension sum:
    sums `deltaLambdaHLF lam = dtEulerG (nStatList lam) (dimHLF lam)` over all
    `lam ∈ partitionsOf k` with `3 ≤ lam.length`. -/
def sRow3Derived (k : ℕ) : ℤ :=
  (((partitionsOf k).filter (fun lam => decide (3 ≤ lam.length))).map deltaLambdaHLF).sum

/-- `sRow3Derived` at `k = 0` evaluates to `0`. -/
theorem sRow3Derived_zero : sRow3Derived 0 = 0 := by decide

/-- `sRow3Derived` at `k = 1` evaluates to `0`. -/
theorem sRow3Derived_one : sRow3Derived 1 = 0 := by decide

/-- `sRow3Derived` at `k = 2` evaluates to `0`. -/
theorem sRow3Derived_two : sRow3Derived 2 = 0 := by decide

/-- `sRow3Derived` at `k = 3` evaluates to `-1` (from `[1, 1, 1]`). -/
theorem sRow3Derived_three : sRow3Derived 3 = -1 := by decide

/-- `sRow3Derived` at `k = 4` evaluates to `-2` (from `-3 + 1` on `[2, 1, 1]` and `[1, 1, 1, 1]`). -/
theorem sRow3Derived_four : sRow3Derived 4 = -2 := by decide

/-- `sRow3Derived` at `k = 5` evaluates to `4` (from `-6 + 5 + 4 + 1` on the four `≥ 3`-row partitions). -/
theorem sRow3Derived_five : sRow3Derived 5 = 4 := by decide

/-- **Seam-Closing Theorem (`qou-jkmh`):**
    For all `k ≤ 5`, the first-principles hook-length / graded-characteristic sum `sRow3Derived k`
    equals the table `sRow3 k` of `QOU.MassTheory.ThreeRowExtensiveCumulant`. -/
theorem sRow3Derived_eq_sRow3 (k : ℕ) (hk : k ≤ 5) :
    sRow3Derived k = sRow3 k := by
  interval_cases k <;> decide

/-! ## 4. Downstream Extensive Cluster & Cumulant Consequences from `sRow3Derived` -/

/-- Homogeneous extensive cluster evaluation defined directly from `sRow3Derived`. -/
def BextDerived (A : ℕ) : ℤ :=
  ∑ k ∈ Finset.range (A + 1), (A.choose k : ℤ) * sRow3Derived k

/-- For `A ≤ 5`, `BextDerived A` agrees identically with `Bext A` from `ThreeRowExtensiveCumulant`. -/
theorem BextDerived_eq_Bext (A : ℕ) (hA : A ≤ 5) :
    BextDerived A = Bext A := by
  unfold BextDerived Bext
  refine Finset.sum_congr rfl ?_
  intro k hk
  rw [Finset.mem_range] at hk
  rw [sRow3Derived_eq_sRow3 k (by omega)]

/-- Forward 2-body cumulant defined directly from `sRow3Derived`. -/
def nu2Derived : ℤ := sRow3Derived 2

/-- Forward 3-body cumulant defined directly from `sRow3Derived`. -/
def nu3Derived : ℤ := sRow3Derived 3 - 3 * nu2Derived

/-- Forward 4-body cumulant defined directly from `sRow3Derived`. -/
def nu4Derived : ℤ := sRow3Derived 4 - 6 * nu2Derived - 4 * nu3Derived

/-- The derived forward cumulants `(nu2Derived, nu3Derived, nu4Derived)` equal `(nu2, nu3, nu4)`
    from `ThreeRowExtensiveCumulant`. -/
theorem nuDerived_eq_nu :
    nu2Derived = nu2 ∧ nu3Derived = nu3 ∧ nu4Derived = nu4 := by
  refine ⟨by decide, by decide, by decide⟩

/-- Seam-closed forward cumulant sign and ratio theorem proved directly on
    `(nu2Derived, nu3Derived, nu4Derived)` without passing through the lookup table `sRow3`. -/
theorem derived_cumulants_sign_and_ratio :
    nu2Derived = 0 ∧ (nu3Derived < 0 ∧ 0 < nu4Derived) ∧ nu4Derived = -2 * nu3Derived := by
  refine ⟨by decide, ⟨by decide, by decide⟩, by decide⟩

end QOU.MassTheory.ThreeRowSpringerSYTDerivation
