import BraidKnotOctonion.DepthOneHookClassification
import BraidKnotOctonion.SecondMomentKernelVanishes

/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
set_option autoImplicit false

/-!
# The (TAIL) Second Instance (`v = n - 1`): Unconditional Closed Form and `n₁ = 8` Sign Onset (`qou-1a69`)

Completes **D6 (`qou-1a69`)** (and the assembly leg of `qou-ec5z`) by connecting the depth-1
carrier classification and shape data (`QOU.BraidsAndKnots.DepthOneHookClassification`, D1/D3/D4/D5)
and the unconditional Plancherel mean-zero + normalization theorems
(`QOU.BraidsAndKnots.SecondMomentKernelVanishes`, `QOU.BraidsAndKnots.PlancherelNormalisation`)
all the way to the explicit closed form and sign-onset characterization on the corpus hook-spectrum
covariance `YoungDiagramKernelPincer.nuV n (n - 1)`:

`nuV n (n - 1) = (n - 1)(n - 4)(n³ - 11n² + 32n - 30) · C(2n - 6, n - 3) / (3 · n!)`  (`n ≥ 4`).

## Derivation architecture

1. **Symmetric binomial-square moments (`uWeight`, `uMoment1`, `uMoment2`, `uMoment3`)**:
   writing `u(n, j) = j(n - j)`, the absorption identity
   `u(m + 2, k + 1) · C(m + 2, k + 1) = (m + 2)(m + 1) · C(m, k)` reduces the `u⁰, u¹, u², u³`
   moments against `C(n, j)²` to central binomial coefficients in division-free form.
2. **Division-free two-corner dimension (`mul_sytDim_twoCorner`)**:
   `(n - 1) · f^{(i+2, 2, 1^{n-4-i})} = (i + 1)(n - 3 - i) · C(n, i + 2) = (u(n, i+2) - (n - 1)) · C(n, i + 2)`.
3. **Uniform `range (n + 1)` unification (`sq_depthOne_int_sum_eq_u_sum`)**:
   multiplying `6 · Σ_{l ∈ depthOneShapes n} (f^l)² ω₃(n, l)` by `(n - 1)²` unites the single row
   `[n]` (`j = n`), the single column `1^n` (`j = 0`), the two vanishing hooks (`j = 1, n - 1`),
   and all `n - 3` two-corner shapes (`2 ≤ j ≤ n - 2`) into a single cubic-in-`u` sum over
   `j ∈ Finset.range (n + 1)`.
4. **Central-binomial collapse & end-to-end `nuV` theorems**:
   - `nuV_depthOne_closed_form`: `nuV n (n - 1) = nuDepthOneClosedForm n` for every `n ≥ 4`.
   - `nuV_depthOne_witness_values`: exact rational agreement on `nuV n (n - 1)` at `n = 4..9`
     (`0, -4/3, -5/3, -1/6, 119/60, 88/27`), matching
     `computations/deltalambda/wlambda-covariance-epic-A2-tail-second-instance.witness.json`.
   - `nuV_depthOne_eq_zero_iff`, `nuV_depthOne_neg_iff`, `nuV_depthOne_pos_iff`,
     `nuV_depthOne_nonneg_iff`: exact `n₁ = 8` sign onset (`0 < nuV n (n - 1) ↔ 8 ≤ n` for `n ≥ 4`),
     governed by `n³ - 11n² + 32n - 30 = (n - 8)((n - 2)² + (n - 1) + 5) + 34`.
-/

namespace QOU.BraidsAndKnots.YoungDiagramTailSecondInstance

open QOU.BraidsAndKnots.YoungDiagramKernel
open QOU.BraidsAndKnots.YoungDiagramTransposeBridge
open QOU.BraidsAndKnots.YoungDiagramKernelPincer
open QOU.BraidsAndKnots.YoungDiagramTailFirstInstance
open QOU.BraidsAndKnots.DepthOneHookClassification
open QOU.BraidsAndKnots.SecondMomentKernelVanishes

/-! ## 1. Symmetric `u(n, j) = j(n - j)` moments against `C(n, j)²` -/

/-- The symmetric product `u(n, j) = j · (n - j)`, invariant under `j ↦ n - j`. -/
def uWeight (n j : ℕ) : ℕ := j * (n - j)

/-- `uWeight n 0 = 0`. -/
theorem uWeight_zero_left (n : ℕ) : uWeight n 0 = 0 := by
  simp [uWeight]

/-- `uWeight n n = 0`. -/
theorem uWeight_self (n : ℕ) : uWeight n n = 0 := by
  simp [uWeight]

/-- **Symmetric absorption**: `(k + 1)(m + 1 - k) · C(m + 2, k + 1) = (m + 2)(m + 1) · C(m, k)`
for `k ≤ m`. -/
theorem uWeight_succ_mul_choose (m k : ℕ) (hk : k ≤ m) :
    uWeight (m + 2) (k + 1) * (m + 2).choose (k + 1)
      = (m + 2) * (m + 1) * m.choose k := by
  unfold uWeight
  have hsub : m + 2 - (k + 1) = m - k + 1 := by omega
  rw [hsub]
  have h1 : (k + 1) * (m + 2).choose (k + 1) = (m + 2) * (m + 1).choose k :=
    BinomialSquareSums.succ_mul_choose_succ (m + 1) k
  have hsym1 : (m + 1).choose k = (m + 1).choose (m - k + 1) := by
    have hle : k ≤ m + 1 := by omega
    have heq : m + 1 - k = m - k + 1 := by omega
    rw [← Nat.choose_symm hle, heq]
  have h2 : (m - k + 1) * (m + 1).choose (m - k + 1) = (m + 1) * m.choose (m - k) :=
    BinomialSquareSums.succ_mul_choose_succ m (m - k)
  have hsym2 : m.choose (m - k) = m.choose k := Nat.choose_symm hk
  calc (k + 1) * (m - k + 1) * (m + 2).choose (k + 1)
      = (m - k + 1) * ((k + 1) * (m + 2).choose (k + 1)) := by ring
    _ = (m - k + 1) * ((m + 2) * (m + 1).choose k) := by rw [h1]
    _ = (m + 2) * ((m - k + 1) * (m + 1).choose (m - k + 1)) := by rw [hsym1]; ring
    _ = (m + 2) * ((m + 1) * m.choose (m - k)) := by rw [h2]
    _ = (m + 2) * (m + 1) * m.choose k := by rw [hsym2]; ring

/-- **First `u`-moment**: `∑_{j ≤ m+1} j(m+1-j) · C(m+1, j)² = (m + 1) m · C(2m, m)`. -/
theorem uMoment1 (m : ℕ) :
    ∑ j ∈ Finset.range (m + 2), uWeight (m + 1) j * ((m + 1).choose j) ^ 2
      = (m + 1) * m * (2 * m).choose m := by
  have hadd : (∑ j ∈ Finset.range (m + 2), uWeight (m + 1) j * ((m + 1).choose j) ^ 2)
      + (∑ j ∈ Finset.range (m + 2), j ^ 2 * ((m + 1).choose j) ^ 2)
      = (m + 1) * ∑ j ∈ Finset.range (m + 2), j * ((m + 1).choose j) ^ 2 := by
    rw [← Finset.sum_add_distrib, Finset.mul_sum]
    refine Finset.sum_congr rfl fun j hj => ?_
    have hle : j ≤ m + 1 := Nat.lt_succ_iff.mp (Finset.mem_range.mp hj)
    have hsplit : j * (m + 1 - j) + j ^ 2 = (m + 1) * j := by
      zify [hle]
      ring
    calc uWeight (m + 1) j * ((m + 1).choose j) ^ 2 + j ^ 2 * ((m + 1).choose j) ^ 2
        = (j * (m + 1 - j) + j ^ 2) * ((m + 1).choose j) ^ 2 := by unfold uWeight; ring
      _ = ((m + 1) * j) * ((m + 1).choose j) ^ 2 := by rw [hsplit]
      _ = (m + 1) * (j * ((m + 1).choose j) ^ 2) := by ring
  have h2m1 := BinomialSquareSums.two_mul_sum_mul_choose_sq (m + 1)
  have hm2 := BinomialSquareSums.sum_sq_mul_choose_sq m
  have hcent := BinomialSquareSums.succ_mul_central_succ m
  set S := ∑ j ∈ Finset.range (m + 2), uWeight (m + 1) j * ((m + 1).choose j) ^ 2
  set S1 := ∑ j ∈ Finset.range (m + 2), j * ((m + 1).choose j) ^ 2
  have hlin : 2 * S + 2 * ((m + 1) ^ 2 * (2 * m).choose m)
      = (m + 1) * (2 * (2 * m + 1) * (2 * m).choose m) := by
    calc 2 * S + 2 * ((m + 1) ^ 2 * (2 * m).choose m)
        = 2 * (S + (m + 1) ^ 2 * (2 * m).choose m) := by ring
      _ = 2 * ((m + 1) * S1) := by rw [← hm2, hadd]
      _ = (m + 1) * (2 * S1) := by ring
      _ = (m + 1) * ((m + 1) * (2 * (m + 1)).choose (m + 1)) := by rw [h2m1]
      _ = (m + 1) * (2 * (2 * m + 1) * (2 * m).choose m) := by rw [hcent]
  have h2S : 2 * S = 2 * ((m + 1) * m * (2 * m).choose m) := by
    zify at hlin ⊢
    linarith
  omega

/-- **Second `u`-moment**: `∑_{j ≤ m+2} u(m+2, j)² · C(m+2, j)² = (m + 2)² (m + 1)² · C(2m, m)`. -/
theorem uMoment2 (m : ℕ) :
    ∑ j ∈ Finset.range (m + 3), (uWeight (m + 2) j) ^ 2 * ((m + 2).choose j) ^ 2
      = (m + 2) ^ 2 * (m + 1) ^ 2 * (2 * m).choose m := by
  rw [Finset.sum_range_succ', uWeight_zero_left, Finset.sum_range_succ, uWeight_self]
  simp only [ne_eq, OfNat.ofNat_ne_zero, not_false_eq_true, zero_pow, zero_mul, add_zero]
  have hterm : ∀ k ∈ Finset.range (m + 1),
      (uWeight (m + 2) (k + 1)) ^ 2 * ((m + 2).choose (k + 1)) ^ 2
        = (m + 2) ^ 2 * (m + 1) ^ 2 * (m.choose k) ^ 2 := by
    intro k hk
    have hle : k ≤ m := Nat.lt_succ_iff.mp (Finset.mem_range.mp hk)
    calc (uWeight (m + 2) (k + 1)) ^ 2 * ((m + 2).choose (k + 1)) ^ 2
        = (uWeight (m + 2) (k + 1) * (m + 2).choose (k + 1)) ^ 2 := by ring
      _ = ((m + 2) * (m + 1) * m.choose k) ^ 2 := by rw [uWeight_succ_mul_choose m k hle]
      _ = (m + 2) ^ 2 * (m + 1) ^ 2 * (m.choose k) ^ 2 := by ring
  rw [Finset.sum_congr rfl hterm, ← Finset.mul_sum, BinomialSquareSums.sum_choose_sq m]

/-- **Third `u`-moment** (`n = r + 3`):
`∑_{j ≤ r+3} u(r+3, j)³ · C(r+3, j)² = (r + 3)² (r + 2)² · [(r + 1) r C(2r, r) + (r + 2) C(2r+2, r+1)]`. -/
theorem uMoment3 (r : ℕ) :
    ∑ j ∈ Finset.range (r + 4), (uWeight (r + 3) j) ^ 3 * ((r + 3).choose j) ^ 2
      = (r + 3) ^ 2 * (r + 2) ^ 2
        * ((r + 1) * r * (2 * r).choose r + (r + 2) * (2 * (r + 1)).choose (r + 1)) := by
  have hpeel : r + 4 = (r + 2) + 1 + 1 := by omega
  rw [hpeel, Finset.sum_range_succ', uWeight_zero_left, Finset.sum_range_succ]
  have htop : uWeight (r + 3) (r + 2 + 1) = 0 := uWeight_self (r + 3)
  rw [htop]
  simp only [ne_eq, OfNat.ofNat_ne_zero, not_false_eq_true, zero_pow, zero_mul, add_zero]
  have hterm : ∀ k ∈ Finset.range (r + 2),
      (uWeight (r + 3) (k + 1)) ^ 3 * ((r + 3).choose (k + 1)) ^ 2
        = (r + 3) ^ 2 * (r + 2) ^ 2 * (uWeight (r + 1) k * ((r + 1).choose k) ^ 2)
          + (r + 3) ^ 2 * (r + 2) ^ 2 * ((r + 2) * ((r + 1).choose k) ^ 2) := by
    intro k hk
    have hle : k ≤ r + 1 := Nat.lt_succ_iff.mp (Finset.mem_range.mp hk)
    have habs := uWeight_succ_mul_choose (r + 1) k hle
    have hshift : uWeight (r + 3) (k + 1) = uWeight (r + 1) k + (r + 2) := by
      unfold uWeight
      have hsub : r + 3 - (k + 1) = r + 1 - k + 1 := by omega
      rw [hsub]
      zify [hle]
      ring
    calc (uWeight (r + 3) (k + 1)) ^ 3 * ((r + 3).choose (k + 1)) ^ 2
        = uWeight (r + 3) (k + 1) * (uWeight (r + 3) (k + 1) * (r + 3).choose (k + 1)) ^ 2 := by
            ring
      _ = (uWeight (r + 1) k + (r + 2)) * ((r + 3) * (r + 2) * (r + 1).choose k) ^ 2 := by
            rw [habs, hshift]
      _ = (r + 3) ^ 2 * (r + 2) ^ 2 * (uWeight (r + 1) k * ((r + 1).choose k) ^ 2)
          + (r + 3) ^ 2 * (r + 2) ^ 2 * ((r + 2) * ((r + 1).choose k) ^ 2) := by
            ring
  rw [Finset.sum_congr rfl hterm, Finset.sum_add_distrib, ← Finset.mul_sum, ← Finset.mul_sum,
    ← Finset.mul_sum, uMoment1 r, BinomialSquareSums.sum_choose_sq (r + 1)]
  ring

/-! ## 2. Division-free two-corner `sytDim` and uniform `range (n + 1)` reduction -/

/-- **Division-free two-corner dimension identity**:
for `i < n - 3`, `(n - 1) · f^{(i+2, 2, 1^{n-4-i})} = (i + 1)(n - 3 - i) · C(n, i + 2)`. -/
theorem mul_sytDim_twoCorner (n i : ℕ) (hi : i < n - 3) :
    (n - 1) * sytDim ((i + 2) :: 2 :: List.replicate (n - 4 - i) 1)
      = (i + 1) * (n - 3 - i) * n.choose (i + 2) := by
  set l := (i + 2) :: 2 :: List.replicate (n - 4 - i) 1
  have hmem : l ∈ partsOf n := twoCornerShape_mem_partsOf n i hi
  obtain ⟨hsum, hpos, hsort⟩ := partsOf_facts n l hmem
  have hmul : sytDim l * hookProd l = n.factorial := by
    rw [YoungDiagramKernelDimPos.sytDim_eq_numSYTenum l hsort hpos,
      YoungDiagramKernelDimPos.hookProd_eq_prodHooks l hsort, ← hsum]
    exact QOU.Mathlib.SYTEnum.numSYTenum_mul_prodHooks l hsort hpos
  have hhp : hookProd l
      = (n - 1) * (i + 2) * (n - 2 - i) * i.factorial * (n - 4 - i).factorial := by
    have h := hookProd_twoCorner (i + 2) (n - 4 - i) (by omega)
    have h1 : i + 2 + (n - 4 - i) + 1 = n - 1 := by omega
    have h2 : n - 4 - i + 2 = n - 2 - i := by omega
    have h3 : i + 2 - 2 = i := by omega
    rw [h1, h2, h3] at h
    exact h
  have hfac1 : (i + 2).factorial = (i + 2) * (i + 1) * i.factorial := by
    rw [Nat.factorial_succ, Nat.factorial_succ]
    ring
  have hfac2 : (n - 2 - i).factorial
      = (n - 2 - i) * (n - 3 - i) * (n - 4 - i).factorial := by
    have heq1 : n - 2 - i = (n - 4 - i) + 2 := by omega
    have heq2 : n - 3 - i = (n - 4 - i) + 1 := by omega
    rw [heq1, heq2, Nat.factorial_succ, Nat.factorial_succ]
    ring
  have hchoose : n.choose (i + 2) * (i + 2).factorial * (n - 2 - i).factorial = n.factorial := by
    have hsub : n - (i + 2) = n - 2 - i := by omega
    rw [← hsub]
    exact Nat.choose_mul_factorial_mul_factorial (by omega)
  set F := (i + 2).factorial * (n - 2 - i).factorial
  have hFpos : 0 < F := Nat.mul_pos (Nat.factorial_pos _) (Nat.factorial_pos _)
  apply Nat.mul_right_cancel hFpos
  have hlhs : (n - 1) * sytDim l * F = (i + 1) * (n - 3 - i) * n.factorial := by
    calc (n - 1) * sytDim l * F
        = sytDim l * ((n - 1) * ((i + 2).factorial * (n - 2 - i).factorial)) := by
            dsimp [F]; ring
      _ = sytDim l * (hookProd l * ((i + 1) * (n - 3 - i))) := by
            rw [hfac1, hfac2, hhp]; ring
      _ = (sytDim l * hookProd l) * ((i + 1) * (n - 3 - i)) := by ring
      _ = (i + 1) * (n - 3 - i) * n.factorial := by rw [hmul]; ring
  have hrhs : (i + 1) * (n - 3 - i) * n.choose (i + 2) * F
      = (i + 1) * (n - 3 - i) * n.factorial := by
    calc (i + 1) * (n - 3 - i) * n.choose (i + 2) * F
        = (i + 1) * (n - 3 - i) * (n.choose (i + 2) * (i + 2).factorial * (n - 2 - i).factorial) := by
            dsimp [F]; ring
      _ = (i + 1) * (n - 3 - i) * n.factorial := by rw [hchoose]
  rw [hlhs, hrhs]

/-- `List.range`-map sum as a `Finset.range` sum over `ℤ`. -/
theorem list_sum_map_range_int (n : ℕ) (f : ℕ → ℤ) :
    ((List.range n).map f).sum = ∑ j ∈ Finset.range n, f j := by
  induction n with
  | zero => simp
  | succ m ih =>
      rw [List.range_succ, List.map_append, List.sum_append, Finset.sum_range_succ, ih]
      simp

/-- `6 · ω₃(n, [n]) = 2 n (n - 1)(n - 2)` for `2 ≤ n`. -/
theorem six_mul_omega3_singleRow (n : ℕ) (hn : 2 ≤ n) :
    6 * omega3 n [n] = 2 * (n : ℤ) * ((n : ℤ) - 1) * ((n : ℤ) - 2) := by
  have h := six_mul_omega3_hookShape n (n - 1) (by omega)
  have hshape : (n - 1 + 1) :: List.replicate (n - 1 - (n - 1)) 1 = [n] := by
    have h1 : n - 1 + 1 = n := by omega
    have h2 : n - 1 - (n - 1) = 0 := by omega
    rw [h1, h2]; rfl
  rw [hshape] at h
  have hn1 : ((n - 1 : ℕ) : ℤ) = (n : ℤ) - 1 := by omega
  rw [hn1] at h
  linarith

/-- `6 · ω₃(n, 1^n) = 2 n (n - 1)(n - 2)` for `2 ≤ n`. -/
theorem six_mul_omega3_singleCol (n : ℕ) (hn : 2 ≤ n) :
    6 * omega3 n (List.replicate n 1) = 2 * (n : ℤ) * ((n : ℤ) - 1) * ((n : ℤ) - 2) := by
  have h := six_mul_omega3_hookShape n 0 (by omega)
  have hshape : (0 + 1) :: List.replicate (n - 1 - 0) 1 = List.replicate n 1 := by
    obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by omega⟩
    simp [List.replicate_succ]
  rw [hshape] at h
  push_cast at h
  linarith

/-- **Uniform `Finset.range (n + 1)` reduction**: multiplying the `ℤ`-valued depth-1 `6 · ω₃` sum
by `(n - 1)²` unites `[n]` (`j = n`), `1^n` (`j = 0`), the two zero terms (`j = 1, n - 1`), and
all `n - 3` two-corner shapes (`2 ≤ j ≤ n - 2`) into one polynomial-in-`u` sum. -/
theorem sq_depthOne_int_sum_eq_u_sum (n : ℕ) (hn : 4 ≤ n) :
    ((n : ℤ) - 1) ^ 2 *
        (((depthOneShapes n).map (fun l => (sytDim l : ℤ) ^ 2 * (6 * omega3 n l))).sum)
      = 2 * ((n : ℤ) - 1) * ∑ j ∈ Finset.range (n + 1),
          ((uWeight n j : ℤ) - ((n : ℤ) - 1)) ^ 2
            * ((n : ℤ) * ((n : ℤ) - 2) - 3 * (uWeight n j : ℤ))
            * (n.choose j : ℤ) ^ 2 := by
  unfold depthOneShapes twoCornerShapes
  simp only [List.map_cons, List.sum_cons, List.map_map]
  rw [sytDim_singleRow n (by omega), sytDim_singleCol n (by omega),
    six_mul_omega3_singleRow n (by omega), six_mul_omega3_singleCol n (by omega),
    list_sum_map_range_int]
  -- Peel j = 0, j = 1 from the bottom and j = n - 1, j = n from the top of range (n + 1).
  have hsplit_range : n + 1 = (n - 3) + 1 + 1 + 1 + 1 := by omega
  rw [hsplit_range, Finset.sum_range_succ', Finset.sum_range_succ',
    Finset.sum_range_succ, Finset.sum_range_succ]
  have hback : (n - 3) + 1 + 1 + 1 = n := by omega
  rw [hback]
  have hu0 : (uWeight n 0 : ℤ) = 0 := by simp [uWeight]
  have hu1 : (uWeight n (0 + 1) : ℤ) = (n : ℤ) - 1 := by
    change (uWeight n 1 : ℤ) = (n : ℤ) - 1
    unfold uWeight
    have h1 : 1 * (n - 1) = n - 1 := Nat.one_mul _
    rw [h1]
    omega
  have hun1 : (uWeight n (n - 3 + 1 + 1) : ℤ) = (n : ℤ) - 1 := by
    have heq : n - 3 + 1 + 1 = n - 1 := by omega
    rw [heq]
    unfold uWeight
    have h1 : n - (n - 1) = 1 := by omega
    rw [h1, Nat.mul_one]
    omega
  have hun : (uWeight n n : ℤ) = 0 := by
    rw [uWeight_self]; rfl
  have hc0 : (n.choose 0 : ℤ) = 1 := by simp
  have hcn : (n.choose n : ℤ) = 1 := by
    rw [Nat.choose_self]; rfl
  rw [hu0, hu1, hun1, hun, hc0, hcn]
  have hterms : ((n : ℤ) - 1) ^ 2 * ∑ i ∈ Finset.range (n - 3),
        ((fun l => (sytDim l : ℤ) ^ 2 * (6 * omega3 n l)) ∘
          fun k => (k + 2) :: 2 :: List.replicate (n - 4 - k) 1) i
      = 2 * ((n : ℤ) - 1) * ∑ i ∈ Finset.range (n - 3),
          ((uWeight n (i + 1 + 1) : ℤ) - ((n : ℤ) - 1)) ^ 2
            * ((n : ℤ) * ((n : ℤ) - 2) - 3 * (uWeight n (i + 1 + 1) : ℤ))
            * (n.choose (i + 1 + 1) : ℤ) ^ 2 := by
    rw [Finset.mul_sum, Finset.mul_sum]
    refine Finset.sum_congr rfl fun i hi => ?_
    dsimp only [Function.comp_apply]
    change ((n : ℤ) - 1) ^ 2 *
          ((sytDim ((i + 2) :: 2 :: List.replicate (n - 4 - i) 1) : ℤ) ^ 2
            * (6 * omega3 n ((i + 2) :: 2 :: List.replicate (n - 4 - i) 1)))
      = 2 * ((n : ℤ) - 1) * (((uWeight n (i + 2) : ℤ) - ((n : ℤ) - 1)) ^ 2
            * ((n : ℤ) * ((n : ℤ) - 2) - 3 * (uWeight n (i + 2) : ℤ))
            * (n.choose (i + 2) : ℤ) ^ 2)
    have hi' : i < n - 3 := Finset.mem_range.mp hi
    have hdim := congrArg (fun x : ℕ => (x : ℤ)) (mul_sytDim_twoCorner n i hi')
    push_cast at hdim
    have hn1_cast : ((n - 1 : ℕ) : ℤ) = (n : ℤ) - 1 := by omega
    have hu_i : ((i : ℤ) + 1) * (((n - 3 - i : ℕ) : ℤ))
        = (uWeight n (i + 2) : ℤ) - ((n : ℤ) - 1) := by
      unfold uWeight
      zify [show i ≤ n - 3 by omega, show 3 ≤ n by omega, show i + 2 ≤ n by omega]
      ring
    rw [hn1_cast, hu_i] at hdim
    have hom := six_mul_omega3_twoCorner n i hi'
    have hom_u : 6 * omega3 n ((i + 2) :: 2 :: List.replicate (n - 4 - i) 1)
        = 2 * ((n : ℤ) - 1) * ((n : ℤ) * ((n : ℤ) - 2) - 3 * (uWeight n (i + 2) : ℤ)) := by
      rw [hom]
      unfold uWeight
      zify [show i + 2 ≤ n by omega]
      ring
    calc ((n : ℤ) - 1) ^ 2 *
          ((sytDim ((i + 2) :: 2 :: List.replicate (n - 4 - i) 1) : ℤ) ^ 2
            * (6 * omega3 n ((i + 2) :: 2 :: List.replicate (n - 4 - i) 1)))
        = (((n : ℤ) - 1) * (sytDim ((i + 2) :: 2 :: List.replicate (n - 4 - i) 1) : ℤ)) ^ 2
            * (6 * omega3 n ((i + 2) :: 2 :: List.replicate (n - 4 - i) 1)) := by ring
      _ = (((uWeight n (i + 2) : ℤ) - ((n : ℤ) - 1)) * (n.choose (i + 2) : ℤ)) ^ 2
            * (2 * ((n : ℤ) - 1) * ((n : ℤ) * ((n : ℤ) - 2) - 3 * (uWeight n (i + 2) : ℤ))) := by
            rw [hdim, hom_u]
      _ = 2 * ((n : ℤ) - 1) * (((uWeight n (i + 2) : ℤ) - ((n : ℤ) - 1)) ^ 2
            * ((n : ℤ) * ((n : ℤ) - 2) - 3 * (uWeight n (i + 2) : ℤ))
            * (n.choose (i + 2) : ℤ) ^ 2) := by ring
  set S_tc := ∑ i ∈ Finset.range (n - 3),
    ((fun l => (sytDim l : ℤ) ^ 2 * (6 * omega3 n l)) ∘
      fun k => (k + 2) :: 2 :: List.replicate (n - 4 - k) 1) i
  have hlhs : ((n : ℤ) - 1) ^ 2 *
      (((1 : ℕ) : ℤ) ^ 2 * (2 * (n : ℤ) * ((n : ℤ) - 1) * ((n : ℤ) - 2)) +
        (((1 : ℕ) : ℤ) ^ 2 * (2 * (n : ℤ) * ((n : ℤ) - 1) * ((n : ℤ) - 2)) + S_tc))
      = 4 * (n : ℤ) * ((n : ℤ) - 1) ^ 3 * ((n : ℤ) - 2) + ((n : ℤ) - 1) ^ 2 * S_tc := by
    push_cast; ring
  rw [hlhs, hterms]
  ring

/-! ## 3. Exact central-binomial collapse and end-to-end `nuV` closed form -/

/-- **Collapse of the `ℤ` depth-1 numerator** (`n = r + 3`, `r ≥ 1`):
`6 · Σ_{l ∈ depthOneShapes n} (f^l)² ω₃(n, l) = 2(n - 1)(n - 4)(n³ - 11n² + 32n - 30) · C(2r, r)`. -/
theorem depthOne_int_sum_collapse (r : ℕ) (hr : 1 ≤ r) :
    ((depthOneShapes (r + 3)).map
        (fun l => (sytDim l : ℤ) ^ 2 * (6 * omega3 (r + 3) l))).sum
      = 2 * ((r : ℤ) + 2) * ((r : ℤ) - 1)
          * (((r : ℤ) + 3) ^ 3 - 11 * ((r : ℤ) + 3) ^ 2 + 32 * ((r : ℤ) + 3) - 30)
          * ((2 * r).choose r : ℤ) := by
  have hunif := sq_depthOne_int_sum_eq_u_sum (r + 3) (by omega)
  -- Expand the cubic-in-u summand into the four moments u^3, u^2, u^1, u^0.
  set N : ℤ := (r : ℤ) + 3
  have hcastN : ((r + 3 : ℕ) : ℤ) = N := by push_cast; rfl
  have hexpand : ∑ j ∈ Finset.range (r + 4),
        ((uWeight (r + 3) j : ℤ) - (((r + 3 : ℕ) : ℤ) - 1)) ^ 2
          * (((r + 3 : ℕ) : ℤ) * (((r + 3 : ℕ) : ℤ) - 2) - 3 * (uWeight (r + 3) j : ℤ))
          * ((r + 3).choose j : ℤ) ^ 2
      = (-3) * (∑ j ∈ Finset.range (r + 4), (uWeight (r + 3) j : ℤ) ^ 3 * ((r + 3).choose j : ℤ) ^ 2)
        + (N * (N - 2) + 6 * (N - 1))
          * (∑ j ∈ Finset.range (r + 4), (uWeight (r + 3) j : ℤ) ^ 2 * ((r + 3).choose j : ℤ) ^ 2)
        - (2 * N * (N - 1) * (N - 2) + 3 * (N - 1) ^ 2)
          * (∑ j ∈ Finset.range (r + 4), (uWeight (r + 3) j : ℤ) * ((r + 3).choose j : ℤ) ^ 2)
        + (N * (N - 2) * (N - 1) ^ 2)
          * (∑ j ∈ Finset.range (r + 4), ((r + 3).choose j : ℤ) ^ 2) := by
    rw [hcastN, Finset.mul_sum, Finset.mul_sum, Finset.mul_sum, Finset.mul_sum,
      ← Finset.sum_add_distrib, ← Finset.sum_sub_distrib, ← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl fun j _ => by ring
  -- Cast the four ℕ moments to ℤ.
  have hm0 : (∑ j ∈ Finset.range (r + 4), ((r + 3).choose j : ℤ) ^ 2)
      = ((2 * (r + 3)).choose (r + 3) : ℤ) := by
    have h := congrArg (fun x : ℕ => (x : ℤ)) (BinomialSquareSums.sum_choose_sq (r + 3))
    push_cast at h; exact h
  have hm1 : (∑ j ∈ Finset.range (r + 4), (uWeight (r + 3) j : ℤ) * ((r + 3).choose j : ℤ) ^ 2)
      = ((r : ℤ) + 3) * ((r : ℤ) + 2) * ((2 * (r + 2)).choose (r + 2) : ℤ) := by
    have h := congrArg (fun x : ℕ => (x : ℤ)) (uMoment1 (r + 2))
    push_cast at h; convert h using 2
  have hm2 : (∑ j ∈ Finset.range (r + 4), (uWeight (r + 3) j : ℤ) ^ 2 * ((r + 3).choose j : ℤ) ^ 2)
      = ((r : ℤ) + 3) ^ 2 * ((r : ℤ) + 2) ^ 2 * ((2 * (r + 1)).choose (r + 1) : ℤ) := by
    have h := congrArg (fun x : ℕ => (x : ℤ)) (uMoment2 (r + 1))
    push_cast at h; convert h using 2
  have hm3 : (∑ j ∈ Finset.range (r + 4), (uWeight (r + 3) j : ℤ) ^ 3 * ((r + 3).choose j : ℤ) ^ 2)
      = ((r : ℤ) + 3) ^ 2 * ((r : ℤ) + 2) ^ 2
        * (((r : ℤ) + 1) * (r : ℤ) * ((2 * r).choose r : ℤ)
          + ((r : ℤ) + 2) * ((2 * (r + 1)).choose (r + 1) : ℤ)) := by
    have h := congrArg (fun x : ℕ => (x : ℤ)) (uMoment3 r)
    push_cast at h; convert h using 2
  -- Central-binomial step relations connecting C_r3, C_r2, C_r1 to Cr = C(2r, r).
  set Cr : ℤ := ((2 * r).choose r : ℤ)
  set Cr1 : ℤ := ((2 * (r + 1)).choose (r + 1) : ℤ)
  set Cr2 : ℤ := ((2 * (r + 2)).choose (r + 2) : ℤ)
  set Cr3 : ℤ := ((2 * (r + 3)).choose (r + 3) : ℤ)
  have hc1 : ((r : ℤ) + 1) * Cr1 = 2 * (2 * (r : ℤ) + 1) * Cr := by
    have h := congrArg (fun x : ℕ => (x : ℤ)) (BinomialSquareSums.succ_mul_central_succ r)
    push_cast at h; exact h
  have hc2 : ((r : ℤ) + 2) * Cr2 = 2 * (2 * (r : ℤ) + 3) * Cr1 := by
    have h := congrArg (fun x : ℕ => (x : ℤ)) (BinomialSquareSums.succ_mul_central_succ (r + 1))
    push_cast at h; convert h using 2
  have hc3 : ((r : ℤ) + 3) * Cr3 = 2 * (2 * (r : ℤ) + 5) * Cr2 := by
    have h := congrArg (fun x : ℕ => (x : ℤ)) (BinomialSquareSums.succ_mul_central_succ (r + 2))
    push_cast at h; convert h using 2
  rw [hexpand, hm0, hm1, hm2, hm3] at hunif
  rw [hcastN] at hunif
  set S := ((depthOneShapes (r + 3)).map
      (fun l => (sytDim l : ℤ) ^ 2 * (6 * omega3 (r + 3) l))).sum
  -- Reduce each of the four central-binomial terms after multiplying by (r + 1).
  have hp2 : ((r : ℤ) + 1) * (((r : ℤ) + 2) * Cr2)
      = 4 * (2 * (r : ℤ) + 3) * (2 * (r : ℤ) + 1) * Cr := by
    calc ((r : ℤ) + 1) * (((r : ℤ) + 2) * Cr2)
        = ((r : ℤ) + 1) * (2 * (2 * (r : ℤ) + 3) * Cr1) := by rw [hc2]
      _ = 2 * (2 * (r : ℤ) + 3) * (((r : ℤ) + 1) * Cr1) := by ring
      _ = 2 * (2 * (r : ℤ) + 3) * (2 * (2 * (r : ℤ) + 1) * Cr) := by rw [hc1]
      _ = 4 * (2 * (r : ℤ) + 3) * (2 * (r : ℤ) + 1) * Cr := by ring
  have hp3 : ((r : ℤ) + 1) * (((r : ℤ) + 2) * (((r : ℤ) + 3) * Cr3))
      = 8 * (2 * (r : ℤ) + 5) * (2 * (r : ℤ) + 3) * (2 * (r : ℤ) + 1) * Cr := by
    calc ((r : ℤ) + 1) * (((r : ℤ) + 2) * (((r : ℤ) + 3) * Cr3))
        = ((r : ℤ) + 1) * (((r : ℤ) + 2) * (2 * (2 * (r : ℤ) + 5) * Cr2)) := by rw [hc3]
      _ = 2 * (2 * (r : ℤ) + 5) * (((r : ℤ) + 1) * (((r : ℤ) + 2) * Cr2)) := by ring
      _ = 2 * (2 * (r : ℤ) + 5) * (4 * (2 * (r : ℤ) + 3) * (2 * (r : ℤ) + 1) * Cr) := by rw [hp2]
      _ = 8 * (2 * (r : ℤ) + 5) * (2 * (r : ℤ) + 3) * (2 * (r : ℤ) + 1) * Cr := by ring
  have ht3 : ((r : ℤ) + 1) *
        (-3 * (((r : ℤ) + 3) ^ 2 * ((r : ℤ) + 2) ^ 2
          * (((r : ℤ) + 1) * (r : ℤ) * Cr + ((r : ℤ) + 2) * Cr1)))
      = (-3 * ((r : ℤ) + 3) ^ 2 * ((r : ℤ) + 2) ^ 2
          * (((r : ℤ) + 1) ^ 2 * (r : ℤ) + 2 * ((r : ℤ) + 2) * (2 * (r : ℤ) + 1))) * Cr := by
    calc ((r : ℤ) + 1) *
          (-3 * (((r : ℤ) + 3) ^ 2 * ((r : ℤ) + 2) ^ 2
            * (((r : ℤ) + 1) * (r : ℤ) * Cr + ((r : ℤ) + 2) * Cr1)))
        = -3 * ((r : ℤ) + 3) ^ 2 * ((r : ℤ) + 2) ^ 2 * ((r : ℤ) + 1) ^ 2 * (r : ℤ) * Cr
          - 3 * ((r : ℤ) + 3) ^ 2 * ((r : ℤ) + 2) ^ 3 * (((r : ℤ) + 1) * Cr1) := by ring
      _ = -3 * ((r : ℤ) + 3) ^ 2 * ((r : ℤ) + 2) ^ 2 * ((r : ℤ) + 1) ^ 2 * (r : ℤ) * Cr
          - 3 * ((r : ℤ) + 3) ^ 2 * ((r : ℤ) + 2) ^ 3 * (2 * (2 * (r : ℤ) + 1) * Cr) := by rw [hc1]
      _ = (-3 * ((r : ℤ) + 3) ^ 2 * ((r : ℤ) + 2) ^ 2
            * (((r : ℤ) + 1) ^ 2 * (r : ℤ) + 2 * ((r : ℤ) + 2) * (2 * (r : ℤ) + 1))) * Cr := by ring
  have ht2 : ((r : ℤ) + 1) *
        ((N * (N - 2) + 6 * (N - 1)) * (((r : ℤ) + 3) ^ 2 * ((r : ℤ) + 2) ^ 2 * Cr1))
      = (2 * (N * (N - 2) + 6 * (N - 1)) * ((r : ℤ) + 3) ^ 2 * ((r : ℤ) + 2) ^ 2
          * (2 * (r : ℤ) + 1)) * Cr := by
    calc ((r : ℤ) + 1) *
          ((N * (N - 2) + 6 * (N - 1)) * (((r : ℤ) + 3) ^ 2 * ((r : ℤ) + 2) ^ 2 * Cr1))
        = (N * (N - 2) + 6 * (N - 1)) * ((r : ℤ) + 3) ^ 2 * ((r : ℤ) + 2) ^ 2
            * (((r : ℤ) + 1) * Cr1) := by ring
      _ = (N * (N - 2) + 6 * (N - 1)) * ((r : ℤ) + 3) ^ 2 * ((r : ℤ) + 2) ^ 2
            * (2 * (2 * (r : ℤ) + 1) * Cr) := by rw [hc1]
      _ = (2 * (N * (N - 2) + 6 * (N - 1)) * ((r : ℤ) + 3) ^ 2 * ((r : ℤ) + 2) ^ 2
            * (2 * (r : ℤ) + 1)) * Cr := by ring
  have ht1 : ((r : ℤ) + 1) *
        ((2 * N * (N - 1) * (N - 2) + 3 * (N - 1) ^ 2) * (((r : ℤ) + 3) * ((r : ℤ) + 2) * Cr2))
      = (4 * (2 * N * (N - 1) * (N - 2) + 3 * (N - 1) ^ 2) * ((r : ℤ) + 3)
          * (2 * (r : ℤ) + 3) * (2 * (r : ℤ) + 1)) * Cr := by
    calc ((r : ℤ) + 1) *
          ((2 * N * (N - 1) * (N - 2) + 3 * (N - 1) ^ 2) * (((r : ℤ) + 3) * ((r : ℤ) + 2) * Cr2))
        = (2 * N * (N - 1) * (N - 2) + 3 * (N - 1) ^ 2) * ((r : ℤ) + 3)
            * (((r : ℤ) + 1) * (((r : ℤ) + 2) * Cr2)) := by ring
      _ = (2 * N * (N - 1) * (N - 2) + 3 * (N - 1) ^ 2) * ((r : ℤ) + 3)
            * (4 * (2 * (r : ℤ) + 3) * (2 * (r : ℤ) + 1) * Cr) := by rw [hp2]
      _ = (4 * (2 * N * (N - 1) * (N - 2) + 3 * (N - 1) ^ 2) * ((r : ℤ) + 3)
            * (2 * (r : ℤ) + 3) * (2 * (r : ℤ) + 1)) * Cr := by ring
  have ht0 : ((r : ℤ) + 1) * ((N * (N - 2) * (N - 1) ^ 2) * Cr3)
      = (8 * ((r : ℤ) + 1) * ((r : ℤ) + 2)
          * (2 * (r : ℤ) + 5) * (2 * (r : ℤ) + 3) * (2 * (r : ℤ) + 1)) * Cr := by
    dsimp [N]
    calc ((r : ℤ) + 1) * ((((r : ℤ) + 3) * (((r : ℤ) + 3) - 2) * (((r : ℤ) + 3) - 1) ^ 2) * Cr3)
        = ((r : ℤ) + 1) * ((r : ℤ) + 2) * (((r : ℤ) + 1) * (((r : ℤ) + 2) * (((r : ℤ) + 3) * Cr3))) := by
            ring
      _ = ((r : ℤ) + 1) * ((r : ℤ) + 2)
            * (8 * (2 * (r : ℤ) + 5) * (2 * (r : ℤ) + 3) * (2 * (r : ℤ) + 1) * Cr) := by rw [hp3]
      _ = (8 * ((r : ℤ) + 1) * ((r : ℤ) + 2)
            * (2 * (r : ℤ) + 5) * (2 * (r : ℤ) + 3) * (2 * (r : ℤ) + 1)) * Cr := by ring
  have hclear : (((r : ℤ) + 1) * ((r : ℤ) + 2) ^ 2) * S
      = (((r : ℤ) + 1) * ((r : ℤ) + 2) ^ 2)
        * (2 * ((r : ℤ) + 2) * ((r : ℤ) - 1)
          * (((r : ℤ) + 3) ^ 3 - 11 * ((r : ℤ) + 3) ^ 2 + 32 * ((r : ℤ) + 3) - 30) * Cr) := by
    have hmul : ((r : ℤ) + 1) * ((N - 1) ^ 2 * S)
        = 2 * (N - 1) *
            (((r : ℤ) + 1) * (-3 * (((r : ℤ) + 3) ^ 2 * ((r : ℤ) + 2) ^ 2
                * (((r : ℤ) + 1) * (r : ℤ) * Cr + ((r : ℤ) + 2) * Cr1)))
              + ((r : ℤ) + 1) * ((N * (N - 2) + 6 * (N - 1)) * (((r : ℤ) + 3) ^ 2 * ((r : ℤ) + 2) ^ 2 * Cr1))
              - ((r : ℤ) + 1) * ((2 * N * (N - 1) * (N - 2) + 3 * (N - 1) ^ 2)
                  * (((r : ℤ) + 3) * ((r : ℤ) + 2) * Cr2))
              + ((r : ℤ) + 1) * ((N * (N - 2) * (N - 1) ^ 2) * Cr3)) := by
      have h := congrArg (fun z : ℤ => ((r : ℤ) + 1) * z) hunif
      dsimp only at h
      linarith [h]
    rw [ht3, ht2, ht1, ht0] at hmul
    dsimp [N] at hmul
    linarith [show (((r : ℤ) + 1) * ((r : ℤ) + 2) ^ 2) * S
        = ((r : ℤ) + 1) * ((((r : ℤ) + 3) - 1) ^ 2 * S) by ring,
      hmul,
      show 2 * (((r : ℤ) + 3) - 1) *
            ((-3 * ((r : ℤ) + 3) ^ 2 * ((r : ℤ) + 2) ^ 2
                * (((r : ℤ) + 1) ^ 2 * (r : ℤ) + 2 * ((r : ℤ) + 2) * (2 * (r : ℤ) + 1))) * Cr
              + (2 * (((r : ℤ) + 3) * (((r : ℤ) + 3) - 2) + 6 * (((r : ℤ) + 3) - 1))
                  * ((r : ℤ) + 3) ^ 2 * ((r : ℤ) + 2) ^ 2 * (2 * (r : ℤ) + 1)) * Cr
              - (4 * (2 * ((r : ℤ) + 3) * (((r : ℤ) + 3) - 1) * (((r : ℤ) + 3) - 2)
                    + 3 * (((r : ℤ) + 3) - 1) ^ 2)
                  * ((r : ℤ) + 3) * (2 * (r : ℤ) + 3) * (2 * (r : ℤ) + 1)) * Cr
              + (8 * ((r : ℤ) + 1) * ((r : ℤ) + 2)
                  * (2 * (r : ℤ) + 5) * (2 * (r : ℤ) + 3) * (2 * (r : ℤ) + 1)) * Cr)
          = (((r : ℤ) + 1) * ((r : ℤ) + 2) ^ 2)
              * (2 * ((r : ℤ) + 2) * ((r : ℤ) - 1)
                * (((r : ℤ) + 3) ^ 3 - 11 * ((r : ℤ) + 3) ^ 2 + 32 * ((r : ℤ) + 3) - 30) * Cr) by ring]
  have hpos : (0 : ℤ) < ((r : ℤ) + 1) * ((r : ℤ) + 2) ^ 2 := by positivity
  exact mul_left_cancel₀ (ne_of_gt hpos) hclear

/-! ## 4. Closed form and `n₁ = 8` sign onset on `nuV n (n - 1)` -/

/-- The cubic factor `n³ - 11n² + 32n - 30` governing the sign of `nuV n (n - 1)`. -/
def depthOneCubicFactor (x : ℝ) : ℝ :=
  x ^ 3 - 11 * x ^ 2 + 32 * x - 30

/-- The full polynomial prefactor `(n - 1)(n - 4)(n³ - 11n² + 32n - 30)` of `nuV n (n - 1)`. -/
def depthOnePolyFactor (x : ℝ) : ℝ :=
  (x - 1) * (x - 4) * depthOneCubicFactor x

/-- The explicit closed-form expression for `nuV n (n - 1)` (`n ≥ 4`). -/
noncomputable def nuDepthOneClosedForm (n : ℕ) : ℝ :=
  depthOnePolyFactor (n : ℝ) * (((2 * n - 6).choose (n - 3) : ℕ) : ℝ)
    / (3 * (Nat.factorial n : ℝ))

/-- **D6 (`qou-1a69`): Unconditional closed form for `nuV n (n - 1)` at every `n ≥ 4`.**
Combines mean-zero (`SecondMomentKernelVanishes.tiltedMean_zero`), Plancherel normalization
(`PlancherelNormalisation.tiltNorm_zero_eq_factorial`), depth-1 carrier restriction
(`DepthOneHookClassification.depthOne_mixedMoment_eq_depthOneShapes_sum`), and
`depthOne_int_sum_collapse`. -/
theorem nuV_depthOne_closed_form (n : ℕ) (hn : 4 ≤ n) :
    nuV n (n - 1) = nuDepthOneClosedForm n := by
  obtain ⟨r, rfl⟩ : ∃ r, n = r + 3 := ⟨n - 3, by omega⟩
  have hr : 1 ≤ r := by omega
  unfold nuV nuDepthOneClosedForm depthOnePolyFactor depthOneCubicFactor
  rw [tiltedMean_zero (r + 3), mul_zero, sub_zero]
  unfold nuMixedMoment
  rw [depthOne_mixedMoment_eq_depthOneShapes_sum (r + 3) (by omega),
    PlancherelNormalisation.tiltNorm_zero_eq_factorial (r + 3)]
  have hcast : 6 * (((depthOneShapes (r + 3)).map
        (fun l => tilt 0 (sytDim l) * (omega3 (r + 3) l : ℝ))).sum)
      = ((((depthOneShapes (r + 3)).map
          (fun l => (sytDim l : ℤ) ^ 2 * (6 * omega3 (r + 3) l))).sum : ℤ) : ℝ) := by
    rw [Int.cast_list_sum, List.map_map, ← list_sum_map_mul_left]
    refine congrArg List.sum (List.map_congr_left fun l _ => ?_)
    simp only [Function.comp_apply]
    rw [tilt_zero]
    push_cast
    ring
  have hcol : ((((depthOneShapes (r + 3)).map
        (fun l => (sytDim l : ℤ) ^ 2 * (6 * omega3 (r + 3) l))).sum : ℤ) : ℝ)
      = ((2 * ((r : ℤ) + 2) * ((r : ℤ) - 1)
          * (((r : ℤ) + 3) ^ 3 - 11 * ((r : ℤ) + 3) ^ 2 + 32 * ((r : ℤ) + 3) - 30)
          * ((2 * r).choose r : ℤ) : ℤ) : ℝ) :=
    congrArg Int.cast (depthOne_int_sum_collapse r hr)
  rw [hcol] at hcast
  push_cast at hcast
  have hsub1 : 2 * (r + 3) - 6 = 2 * r := by omega
  have hsub2 : r + 3 - 3 = r := by omega
  rw [hsub1, hsub2]
  have hfac : (0 : ℝ) < (Nat.factorial (r + 3) : ℝ) := by
    exact_mod_cast Nat.factorial_pos (r + 3)
  field_simp
  push_cast
  linarith [hcast]

/-- Exact positivity decomposition of the depth-1 cubic factor around `n₁ = 8`:
`x³ - 11x² + 32x - 30 = (x - 8)((x - 2)² + (x - 1) + 5) + 34`. -/
theorem depthOneCubicFactor_decomp (x : ℝ) :
    depthOneCubicFactor x = (x - 8) * ((x - 2) ^ 2 + (x - 1) + 5) + 34 := by
  unfold depthOneCubicFactor
  ring

/-- For every `x ≥ 8`, `depthOneCubicFactor x ≥ 34 > 0`. -/
theorem depthOneCubicFactor_pos_of_ge_eight {x : ℝ} (hx : 8 ≤ x) :
    0 < depthOneCubicFactor x := by
  rw [depthOneCubicFactor_decomp]
  have h1 : 0 ≤ x - 8 := by linarith
  have h2 : 0 ≤ (x - 2) ^ 2 + (x - 1) + 5 := by nlinarith [sq_nonneg (x - 2)]
  nlinarith [mul_nonneg h1 h2]

/-- **Witness cross-check (`wlambda-covariance-epic-A2-tail-second-instance.witness.json`)**:
exact rational values of `nuV n (n - 1)` for `n = 4, 5, 6, 7, 8, 9`. -/
theorem nuV_depthOne_witness_values :
    nuV 4 3 = 0 ∧
    nuV 5 4 = -4 / 3 ∧
    nuV 6 5 = -5 / 3 ∧
    nuV 7 6 = -1 / 6 ∧
    nuV 8 7 = 119 / 60 ∧
    nuV 9 8 = 88 / 27 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · rw [nuV_depthOne_closed_form 4 (by omega)]; unfold nuDepthOneClosedForm depthOnePolyFactor depthOneCubicFactor; norm_num [Nat.factorial]
  · rw [nuV_depthOne_closed_form 5 (by omega)]; unfold nuDepthOneClosedForm depthOnePolyFactor depthOneCubicFactor; norm_num [Nat.factorial, Nat.choose]
  · rw [nuV_depthOne_closed_form 6 (by omega)]; unfold nuDepthOneClosedForm depthOnePolyFactor depthOneCubicFactor; norm_num [Nat.factorial, Nat.choose]
  · rw [nuV_depthOne_closed_form 7 (by omega)]; unfold nuDepthOneClosedForm depthOnePolyFactor depthOneCubicFactor; norm_num [Nat.factorial, Nat.choose]
  · rw [nuV_depthOne_closed_form 8 (by omega)]; unfold nuDepthOneClosedForm depthOnePolyFactor depthOneCubicFactor; norm_num [Nat.factorial, Nat.choose]
  · rw [nuV_depthOne_closed_form 9 (by omega)]; unfold nuDepthOneClosedForm depthOnePolyFactor depthOneCubicFactor; norm_num [Nat.factorial, Nat.choose]

/-- For every `n ≥ 8`, `0 < nuV n (n - 1)` unconditionally (`Nat.choose_pos` discharged). -/
theorem nuV_depthOne_pos_of_ge_eight (n : ℕ) (hn : 8 ≤ n) :
    0 < nuV n (n - 1) := by
  rw [nuV_depthOne_closed_form n (by omega)]
  unfold nuDepthOneClosedForm depthOnePolyFactor
  have hnR : (8 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
  have hcub := depthOneCubicFactor_pos_of_ge_eight hnR
  have hpre : 0 < ((n : ℝ) - 1) * ((n : ℝ) - 4) := by nlinarith
  have hch_nat : 0 < (2 * n - 6).choose (n - 3) := Nat.choose_pos (by omega)
  have hch : (0 : ℝ) < (((2 * n - 6).choose (n - 3) : ℕ) : ℝ) := by exact_mod_cast hch_nat
  have hfac : (0 : ℝ) < (Nat.factorial n : ℝ) := by exact_mod_cast Nat.factorial_pos n
  positivity

/-- **Exact `n₁ = 8` positive-onset equivalence (`qou-1a69`)**: for `n ≥ 4`,
`0 < nuV n (n - 1) ↔ 8 ≤ n`. -/
theorem nuV_depthOne_pos_iff (n : ℕ) (hn : 4 ≤ n) :
    0 < nuV n (n - 1) ↔ 8 ≤ n := by
  constructor
  · intro hpos
    by_contra hlt
    obtain ⟨h4, h5, h6, h7, _, _⟩ := nuV_depthOne_witness_values
    interval_cases n
    · rw [h4] at hpos; norm_num at hpos
    · rw [h5] at hpos; norm_num at hpos
    · rw [h6] at hpos; norm_num at hpos
    · rw [h7] at hpos; norm_num at hpos
  · exact nuV_depthOne_pos_of_ge_eight n

/-- **Exact zero-locus equivalence (`qou-1a69`)**: for `n ≥ 4`, `nuV n (n - 1) = 0 ↔ n = 4`. -/
theorem nuV_depthOne_eq_zero_iff (n : ℕ) (hn : 4 ≤ n) :
    nuV n (n - 1) = 0 ↔ n = 4 := by
  obtain ⟨h4, h5, h6, h7, _, _⟩ := nuV_depthOne_witness_values
  constructor
  · intro hz
    by_cases hge8 : 8 ≤ n
    · linarith [nuV_depthOne_pos_of_ge_eight n hge8]
    · interval_cases n
      · rfl
      · rw [h5] at hz; norm_num at hz
      · rw [h6] at hz; norm_num at hz
      · rw [h7] at hz; norm_num at hz
  · rintro rfl; exact h4

/-- **Exact negative-window equivalence (`qou-1a69`)**: for `n ≥ 4`,
`nuV n (n - 1) < 0 ↔ n = 5 ∨ n = 6 ∨ n = 7`. -/
theorem nuV_depthOne_neg_iff (n : ℕ) (hn : 4 ≤ n) :
    nuV n (n - 1) < 0 ↔ n = 5 ∨ n = 6 ∨ n = 7 := by
  obtain ⟨h4, h5, h6, h7, _, _⟩ := nuV_depthOne_witness_values
  constructor
  · intro hneg
    by_cases hge8 : 8 ≤ n
    · linarith [nuV_depthOne_pos_of_ge_eight n hge8]
    · interval_cases n
      · rw [h4] at hneg; norm_num at hneg
      · exact Or.inl rfl
      · exact Or.inr (Or.inl rfl)
      · exact Or.inr (Or.inr rfl)
  · rintro (rfl | rfl | rfl)
    · rw [h5]; norm_num
    · rw [h6]; norm_num
    · rw [h7]; norm_num

/-- **Exact nonnegativity equivalence (`qou-1a69`)**: for `n ≥ 4`,
`0 ≤ nuV n (n - 1) ↔ n = 4 ∨ 8 ≤ n`. -/
theorem nuV_depthOne_nonneg_iff (n : ℕ) (hn : 4 ≤ n) :
    0 ≤ nuV n (n - 1) ↔ n = 4 ∨ 8 ≤ n := by
  constructor
  · intro hnn
    by_cases hge8 : 8 ≤ n
    · exact Or.inr hge8
    · have hnotneg : ¬ nuV n (n - 1) < 0 := not_lt.mpr hnn
      rw [nuV_depthOne_neg_iff n hn] at hnotneg
      left; omega
  · rintro (rfl | hge8)
    · rw [nuV_depthOne_witness_values.1]
    · exact le_of_lt (nuV_depthOne_pos_of_ge_eight n hge8)

end QOU.BraidsAndKnots.YoungDiagramTailSecondInstance
