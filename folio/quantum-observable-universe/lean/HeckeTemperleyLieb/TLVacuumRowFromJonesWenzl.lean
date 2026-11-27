import HeckeTemperleyLieb.TemperleyLiebMarkovNondegenerate
import HeckeTemperleyLieb.TLRootOfUnitySMatrixNondegenerate

/-!
# The vacuum row of the level-`k` `S`-matrix from the Jones–Wenzl Markov trace

`TLRootOfUnitySMatrixNondegenerate` defines the level-`k` modular `S`-matrix
`S_{ij} = [(i+1)(j+1)]` directly in cyclotomic algebra. This file derives its **vacuum row**
`S_{0,j} = [j+1]` from the corpus Temperley–Lieb tower rather than citing it.

* `qInt_add_two`: the balanced quantum integer of `TLRootOfUnity` satisfies the Chebyshev
  recurrence `[n+2] = (ζ + ζ⁻¹)[n+1] − [n]`.
* `qint_eq_qInt`: hence the Chebyshev numbers `qint δ` of `TemperleyLiebMarkov`, at the loop
  value `δ = ζ + ζ⁻¹`, are the balanced quantum integers `qInt ζ`.
* `qInt_ne_zero`: at a primitive `2(k+2)`-th root of unity, `[m] ≠ 0` for `0 < m < k + 2`, which is
  exactly the genericity the Jones–Wenzl recursion needs below level `k`.
* `vacuum_row_eq_sMatrix`: for **any** Markov trace `T` on the TL tower with `δε = 1`, the
  unnormalised trace `δ^{n+1}·τ_n(p_n)` of the Jones–Wenzl projector on `n + 1` strands equals the
  `S`-matrix entry `S_{0,n+1}`, for `n + 1 ≤ k`.

The Markov trace enters as the structure `MarkovTower` (a hypothesis-carrying argument, not an
axiom and not a class instance). The corpus does not yet construct an instance of it at a root of
unity; that existence is the remaining gap for this row. The off-vacuum rows (Hopf-link double
braiding of two Jones–Wenzl projectors) and the twist eigenvalue on `p_n` are not derived here.
-/

namespace QOU.HeckeTemperleyLieb.TLVacuumRow

open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebMarkov
open QOU.HeckeTemperleyLieb.TLRootOfUnity

variable {K : Type*} [Field K]

/-- `ζ·[n+1] = ζ^{n+1} + [n]`. -/
theorem zeta_mul_qInt_succ (ζ : Kˣ) (n : ℕ) :
    (ζ : K) * qInt ζ (n + 1) = ((ζ ^ ((n + 1 : ℕ) : ℤ) : Kˣ) : K) + qInt ζ n := by
  have hp : ((ζ ^ ((n + 1 : ℕ) : ℤ) : Kˣ) : K) = (ζ : K) * ((ζ ^ (n : ℤ) : Kˣ) : K) := by
    rw [show ((n + 1 : ℕ) : ℤ) = 1 + (n : ℤ) by push_cast; ring, zpow_one_add, Units.val_mul]
  show (ζ : K) * (((ζ ^ (n : ℤ) : Kˣ) : K) + ((ζ⁻¹ : Kˣ) : K) * qInt ζ n) = _
  rw [hp, mul_add, ← mul_assoc, Units.mul_inv, one_mul]

/-- The balanced quantum integers satisfy the Chebyshev recurrence in `δ = ζ + ζ⁻¹`. -/
theorem qInt_add_two (ζ : Kˣ) (n : ℕ) :
    qInt ζ (n + 2) = ((ζ : K) + ((ζ⁻¹ : Kˣ) : K)) * qInt ζ (n + 1) - qInt ζ n := by
  have h := zeta_mul_qInt_succ ζ n
  have hq : qInt ζ (n + 2) =
      ((ζ ^ ((n + 1 : ℕ) : ℤ) : Kˣ) : K) + ((ζ⁻¹ : Kˣ) : K) * qInt ζ (n + 1) := rfl
  rw [hq]
  linear_combination -h

/-- **Bridge.** The corpus Chebyshev numbers at the loop value `δ = ζ + ζ⁻¹` are the balanced
quantum integers of the root-of-unity `S`-matrix file. -/
theorem qint_eq_qInt (ζ : Kˣ) : ∀ n, qint ((ζ : K) + ((ζ⁻¹ : Kˣ) : K)) n = qInt ζ n
  | 0 => by simp [qInt]
  | 1 => by simp [qInt]
  | n + 2 => by rw [qint_add_two, qInt_add_two, qint_eq_qInt ζ (n + 1), qint_eq_qInt ζ n]

/-- At a primitive `2(k+2)`-th root of unity, `[m] ≠ 0` for `0 < m < k + 2`. -/
theorem qInt_ne_zero {ζ : Kˣ} (k : ℕ) (hζ : IsPrimitiveRoot ζ (2 * (k + 2))) {m : ℕ}
    (hm0 : 0 < m) (hm : m < k + 2) : qInt ζ m ≠ 0 := by
  intro h
  have h1 := qDelta_mul_qInt ζ m
  rw [h, mul_zero] at h1
  have hu : (ζ ^ (m : ℤ) : Kˣ) = ζ ^ (-(m : ℤ)) := Units.ext (sub_eq_zero.mp h1.symm)
  have h2 : ζ ^ ((2 * m : ℕ) : ℤ) = 1 := by
    rw [show ((2 * m : ℕ) : ℤ) = (m : ℤ) - (-(m : ℤ)) by push_cast; ring, zpow_sub, hu,
      mul_inv_cancel]
  rw [zpow_natCast] at h2
  exact hζ.pow_ne_one_of_pos_of_lt (by omega) (by omega) h2

/-- **Vacuum row from the Jones–Wenzl trace.** For any Markov trace on the Temperley–Lieb tower at
loop value `δ = ζ + ζ⁻¹` with `δε = 1`, `ζ` a primitive `2(k+2)`-th root of unity, the unnormalised
trace of the Jones–Wenzl projector on `n + 1` strands is the `S`-matrix entry `S_{0,n+1} = [n+2]`,
for every `n + 1 ≤ k`. -/
theorem vacuum_row_eq_sMatrix {ζ : Kˣ} (k : ℕ) (hζ : IsPrimitiveRoot ζ (2 * (k + 2))) {ε : K}
    (T : MarkovTower ((ζ : K) + ((ζ⁻¹ : Kˣ) : K)) ε)
    (hε : ((ζ : K) + ((ζ⁻¹ : Kˣ) : K)) * ε = 1) (n : ℕ) (hn : n + 1 ≤ k) :
    ((ζ : K) + ((ζ⁻¹ : Kˣ) : K)) ^ (n + 1) * T.τ n (jw ((ζ : K) + ((ζ⁻¹ : Kˣ) : K)) n) =
      sMatrix ζ k 0 ⟨n + 1, by omega⟩ := by
  have hg : ∀ j ≤ n, qint ((ζ : K) + ((ζ⁻¹ : Kˣ) : K)) (j + 1) ≠ 0 := fun j hj => by
    rw [qint_eq_qInt]; exact qInt_ne_zero k hζ (by omega) (by omega)
  rw [tau_jw T hε n hg (fun m hm => jw_spec _ m (fun j hj => hg j (by omega))), qint_eq_qInt]
  have hs : sMatrix ζ k 0 ⟨n + 1, by omega⟩ = qInt ζ (n + 2) := by
    simp only [sMatrix, Fin.val_zero]; congr 1; ring
  rw [hs, mul_left_comm, ← mul_pow, hε, one_pow, mul_one]

/-! ## Non-vacuity

In `𝔽₁₇`, `ζ = 2` has order `8 = 2(2+2)` (level `k = 2`), `ζ⁻¹ = 9`, `δ = 11`. The Chebyshev
numbers vanish first at `[k+2] = [4]`, as `qInt_ne_zero` and the truncation require. -/

example : qint (11 : ZMod 17) 4 = 0 ∧ qint (11 : ZMod 17) 3 ≠ 0 ∧ qint (11 : ZMod 17) 2 ≠ 0 := by
  haveI : Fact (Nat.Prime 17) := ⟨by norm_num⟩
  simp only [qint]; decide

end QOU.HeckeTemperleyLieb.TLVacuumRow
