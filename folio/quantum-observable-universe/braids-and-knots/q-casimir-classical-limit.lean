import Mathlib.Tactic
import Mathlib.Topology.Algebra.Order.Field
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Order.Filter.Basic
import QOU.MathlibExt.QIntegerCanonical

/-!
# QOU.QCasimir — Classical limit (q → 1) of the q-Casimir eigenvalue

Formalises `prop:q-casimir-classical-limit` across both integer and half-integer spins:
1. Over any abstract `Field K`, defines `qCasimirEigenvalueField (q : K) (j : ℤ) := qIntBalZ q j * qIntBalZ q (j + 1)`,
   and shows `QCasimirEigenvalue` over `ℝ` is its archimedean `K := ℝ` specialisation.
2. As `q → 1` (`q ≠ 1`) in `ℝ`, proves `[n]_q → n` for all `n ∈ ℤ` and
   `[j]_q [j + 1]_q → j (j + 1)` for all integer spins `j ∈ ℤ`.
3. Extends to all half-integer and integer `𝔰𝔲(2)` spins `j = twoJ / 2` (`twoJ ∈ ℤ`, including
   spin `1/2`, `3/2`, …) via `u = √q` (`q - q⁻¹ = (u - u⁻¹)(u + u⁻¹)`), proving:
   - consistency `QCasimirEigenvalueHalf q (2 * j) = QCasimirEigenvalue q j` (`0 < q`, `q ≠ 1`),
   - exact spin-`1/2` rational identity `QCasimirEigenvalueHalf q 1 = (q^2 + q⁻² - q - q⁻¹)/(q - q⁻¹)^2`,
   - punctured-neighbourhood classical limits `[twoJ / 2]_q → twoJ / 2` and
     `[twoJ / 2]_q [twoJ / 2 + 1]_q → (twoJ / 2) * (twoJ / 2 + 1)` as `q → 1` (`q ≠ 1`).

LaTeX label: `prop:q-casimir-classical-limit`
-/

namespace QOU

open Filter Topology
open QOU.QInteger

/-- Generic-field `q`-Casimir eigenvalue `[j]_q · [j + 1]_q` over any `Field K`. -/
noncomputable def qCasimirEigenvalueField {K : Type*} [Field K] (q : K) (j : ℤ) : K :=
  QOU.QInteger.qIntBalZ q j * QOU.QInteger.qIntBalZ q (j + 1)

/-- Symmetric `q`-number over `ℝ`: `[n]_q = (qⁿ - q⁻ⁿ)/(q - q⁻¹)`. -/
noncomputable abbrev qNumberSym (q : ℝ) (n : ℤ) : ℝ :=
  QOU.QInteger.qIntBalZ q n

/-- `q`-Casimir eigenvalue over `ℝ`: `[j]_q · [j + 1]_q`. -/
noncomputable def QCasimirEigenvalue (q : ℝ) (j : ℤ) : ℝ :=
  qNumberSym q j * qNumberSym q (j + 1)

/-- `QCasimirEigenvalue` is literally the `K := ℝ` specialisation of `qCasimirEigenvalueField`. -/
theorem QCasimirEigenvalue_eq_field_spec (q : ℝ) (j : ℤ) :
    QCasimirEigenvalue q j = qCasimirEigenvalueField q j := rfl

theorem qNumberSym_classical_limit_nat (n : ℕ) :
    Tendsto (fun q : ℝ => qNumberSym q n) (𝓝[≠] 1) (𝓝 (n : ℝ)) := by
  have h_pos : ∀ᶠ q : ℝ in 𝓝 1, 0 < q :=
    IsOpen.mem_nhds isOpen_Ioi (by positivity : (0 : ℝ) < 1)
  have h_pos2 : ∀ᶠ q : ℝ in 𝓝[≠] 1, 0 < q := nhdsWithin_le_nhds h_pos
  have h_eq :
      (fun q : ℝ => q⁻¹ ^ (n - 1) * ∑ i ∈ Finset.range n, (q ^ 2) ^ i) =ᶠ[𝓝[≠] 1]
        (fun q => qNumberSym q n) := by
    filter_upwards [h_pos2, self_mem_nhdsWithin] with q hq0' hq1'
    have hq0 : q ≠ 0 := ne_of_gt hq0'
    have hq1 : q ^ 2 ≠ 1 := by
      intro h
      rcases sq_eq_one_iff.mp h with rfl | rfl
      · exact hq1' rfl
      · linarith
    rw [qNumberSym, qIntBalZ_natCast, qIntBal_eq_twist_canonical q n hq0 hq1, qIntGeo_def]
  have h_lim :
      Tendsto (fun q : ℝ => q⁻¹ ^ (n - 1) * ∑ i ∈ Finset.range n, (q ^ 2) ^ i) (𝓝[≠] 1)
        (𝓝 ((1 : ℝ)⁻¹ ^ (n - 1) * ∑ i ∈ Finset.range n, ((1 : ℝ) ^ 2) ^ i)) := by
    apply Tendsto.mul
    · exact Tendsto.pow ((continuousAt_inv₀ one_ne_zero).tendsto.mono_left nhdsWithin_le_nhds) _
    · refine tendsto_finset_sum _ (fun i _ => ?_)
      exact Tendsto.pow (Tendsto.pow (continuous_id.continuousAt.tendsto.mono_left nhdsWithin_le_nhds) _) _
  have h_eval : ((1 : ℝ)⁻¹ ^ (n - 1) * ∑ i ∈ Finset.range n, ((1 : ℝ) ^ 2) ^ i) = (n : ℝ) := by
    simp
  rw [h_eval] at h_lim
  exact Tendsto.congr' h_eq h_lim

-- Ref: [kassel1995] §VI.4
-- Ref: [lusztig1993]
theorem qNumberSym_classical_limit (n : ℤ) :
    Tendsto (fun q : ℝ => qNumberSym q n) (𝓝[≠] 1) (𝓝 (n : ℝ)) := by
  cases n with
  | ofNat n => exact qNumberSym_classical_limit_nat n
  | negSucc n =>
      have h_eq : (fun q : ℝ => qNumberSym q (Int.negSucc n)) =
          fun q : ℝ => -qNumberSym q (n + 1) := by
        ext q
        have : Int.negSucc n = -((n + 1 : ℕ) : ℤ) := rfl
        rw [this, qNumberSym, qNumberSym, qIntBalZ_neg]
        push_cast
        rfl
      rw [h_eq]
      have H2 := Tendsto.neg (qNumberSym_classical_limit_nat (n + 1))
      have H3 : -((n + 1 : ℕ) : ℝ) = (Int.negSucc n : ℝ) := by push_cast; rfl
      rw [H3] at H2
      exact H2

-- Ref: [kassel1995] §VI.4
-- Ref: [lusztig1993]
theorem QCasimirEigenvalue_classical_limit (j : ℤ) :
    Tendsto (fun q : ℝ => QCasimirEigenvalue q j) (𝓝[≠] 1)
      (𝓝 ((j : ℝ) * (j + 1))) := by
  unfold QCasimirEigenvalue
  have hj := qNumberSym_classical_limit j
  have hj1 := qNumberSym_classical_limit (j + 1)
  have hCast : ((j + 1 : ℤ) : ℝ) = (j : ℝ) + 1 := by push_cast; ring
  rw [hCast] at hj1
  exact hj.mul hj1

/-! ### Half-integer & integer spin spectrum `j = twoJ / 2` (`twoJ ∈ ℤ`) -/

/-- Symmetric `q`-number `[twoJ / 2]_q` for `twoJ ∈ ℤ` on `q > 0`, expressed via `u = √q`:
    `[m/2]_q = (u^m - u^{-m}) / ((u - u⁻¹)(u + u⁻¹)) = [m]_u / (u + u⁻¹)`. -/
noncomputable def qNumberSymHalf (q : ℝ) (twoJ : ℤ) : ℝ :=
  qNumberSym (Real.sqrt q) twoJ / (Real.sqrt q + (Real.sqrt q)⁻¹)

/-- Half-integer/integer `q`-Casimir eigenvalue `[j]_q [j + 1]_q` for `j = twoJ / 2` (`twoJ ∈ ℤ`). -/
noncomputable def QCasimirEigenvalueHalf (q : ℝ) (twoJ : ℤ) : ℝ :=
  qNumberSymHalf q twoJ * qNumberSymHalf q (twoJ + 2)

/-- At even `twoJ = 2 * j`, `qNumberSymHalf q (2 * j)` agrees identically with `qNumberSym q j`
    for every `q > 0` with `q ≠ 1`. -/
theorem qNumberSymHalf_two_mul {q : ℝ} (hq : 0 < q) (hq1 : q ≠ 1) (j : ℤ) :
    qNumberSymHalf q (2 * j) = qNumberSym q j := by
  unfold qNumberSymHalf qNumberSym QOU.QInteger.qIntBalZ
  set u := Real.sqrt q
  have hu_pos : 0 < u := Real.sqrt_pos.mpr hq
  have hu_ne : u ≠ 0 := ne_of_gt hu_pos
  have hu_sq : u ^ 2 = q := Real.sq_sqrt (le_of_lt hq)
  have hu_ne1 : u - u⁻¹ ≠ 0 := by
    intro h0
    have h1 : u ^ 2 = 1 := by
      have : u * (u - u⁻¹) = 0 := by rw [h0, mul_zero]
      rw [mul_sub, mul_inv_cancel₀ hu_ne] at this
      linarith
    exact hq1 (hu_sq.symm.trans h1)
  have hu_sum_ne : u + u⁻¹ ≠ 0 := ne_of_gt (by positivity)
  have hpow1 : u ^ (2 * j) = q ^ j := by
    rw [zpow_mul]
    norm_cast
    rw [hu_sq]
  have hpow2 : u ^ (-(2 * j)) = q ^ (-j) := by
    have : -(2 * j) = 2 * (-j) := by ring
    rw [this, zpow_mul]
    norm_cast
    rw [hu_sq]
  have hden : (u - u⁻¹) * (u + u⁻¹) = q - q⁻¹ := by
    have hinv_sq : u⁻¹ ^ 2 = q⁻¹ := by
      rw [inv_pow, hu_sq]
    calc (u - u⁻¹) * (u + u⁻¹) = u ^ 2 - u⁻¹ ^ 2 := by ring
      _ = q - q⁻¹ := by rw [hu_sq, hinv_sq]
  rw [hpow1, hpow2, div_div, hden]

/-- Spin-`1/2` (`twoJ = 1`) Casimir eigenvalue matches `(q^2 + q⁻² - q - q⁻¹) / (q - q⁻¹)^2`. -/
theorem QCasimirEigenvalueHalf_one {q : ℝ} (hq : 0 < q) (hq1 : q ≠ 1) :
    QCasimirEigenvalueHalf q 1 = (q ^ 2 + (q⁻¹) ^ 2 - q - q⁻¹) / (q - q⁻¹) ^ 2 := by
  unfold QCasimirEigenvalueHalf qNumberSymHalf qNumberSym QOU.QInteger.qIntBalZ
  set u := Real.sqrt q
  have hu_pos : 0 < u := Real.sqrt_pos.mpr hq
  have hu_ne : u ≠ 0 := ne_of_gt hu_pos
  have hu_sq : u ^ 2 = q := Real.sq_sqrt (le_of_lt hq)
  have hinv_sq : u⁻¹ ^ 2 = q⁻¹ := by rw [inv_pow, hu_sq]
  have hden : (u - u⁻¹) * (u + u⁻¹) = q - q⁻¹ := by
    calc (u - u⁻¹) * (u + u⁻¹) = u ^ 2 - u⁻¹ ^ 2 := by ring
      _ = q - q⁻¹ := by rw [hu_sq, hinv_sq]
  have hq_diff_ne : q - q⁻¹ ≠ 0 := by
    intro h0
    have h1 : q ^ 2 = 1 := by
      have : q * (q - q⁻¹) = 0 := by rw [h0, mul_zero]
      rw [mul_sub, mul_inv_cancel₀ (ne_of_gt hq)] at this
      linarith
    rcases sq_eq_one_iff.mp h1 with rfl | rfl
    · exact hq1 rfl
    · linarith
  have hnum : (u ^ (1 : ℤ) - u ^ (-1 : ℤ)) * (u ^ ((1 : ℤ) + 2) - u ^ (-((1 : ℤ) + 2))) =
      q ^ 2 + (q⁻¹) ^ 2 - q - q⁻¹ := by
    norm_num
    calc (u - u⁻¹) * (u ^ 3 - (u ^ 3)⁻¹)
        = (u ^ 2) ^ 2 + (u⁻¹ ^ 2) ^ 2 - u ^ 2 * (u * u⁻¹) - (u⁻¹ ^ 2) * (u * u⁻¹) := by
          field_simp; ring
      _ = q ^ 2 + (q ^ 2)⁻¹ - q - q⁻¹ := by
          rw [hu_sq, hinv_sq, mul_inv_cancel₀ hu_ne, inv_pow]
          ring
  calc ((u ^ (1 : ℤ) - u ^ (-1 : ℤ)) / (u - u⁻¹) / (u + u⁻¹)) *
        ((u ^ ((1 : ℤ) + 2) - u ^ (-((1 : ℤ) + 2))) / (u - u⁻¹) / (u + u⁻¹))
      = ((u ^ (1 : ℤ) - u ^ (-1 : ℤ)) * (u ^ ((1 : ℤ) + 2) - u ^ (-((1 : ℤ) + 2)))) /
          (((u - u⁻¹) * (u + u⁻¹)) ^ 2) := by
        rw [div_div, div_div, div_mul_div_comm, sq]
    _ = (q ^ 2 + (q⁻¹) ^ 2 - q - q⁻¹) / (q - q⁻¹) ^ 2 := by rw [hnum, hden]

/-- Punctured-neighbourhood classical limit `[twoJ / 2]_q → twoJ / 2` as `q → 1` (`q ≠ 1`)
    for every integer or half-integer spin `j = twoJ / 2` (`twoJ ∈ ℤ`). -/
theorem qNumberSymHalf_classical_limit (twoJ : ℤ) :
    Tendsto (fun q : ℝ => qNumberSymHalf q twoJ) (𝓝[≠] 1) (𝓝 ((twoJ : ℝ) / 2)) := by
  have hsqrt_cont : ContinuousAt Real.sqrt 1 := Real.continuous_sqrt.continuousAt
  have hsqrt_lim : Tendsto Real.sqrt (𝓝[≠] 1) (𝓝 1) := by
    simpa [Real.sqrt_one] using hsqrt_cont.tendsto.mono_left nhdsWithin_le_nhds
  have h_pos : ∀ᶠ q : ℝ in 𝓝[≠] 1, 0 < q :=
    nhdsWithin_le_nhds (IsOpen.mem_nhds isOpen_Ioi (by positivity : (0 : ℝ) < 1))
  have hsqrt_punc : Tendsto Real.sqrt (𝓝[≠] 1) (𝓝[≠] 1) := by
    refine tendsto_nhdsWithin_iff.mpr ⟨hsqrt_lim, ?_⟩
    filter_upwards [h_pos, self_mem_nhdsWithin] with q hq0 hq1
    intro hsq1
    apply hq1
    have := congrArg (fun x : ℝ => x ^ 2) hsq1
    simpa [Real.sq_sqrt (le_of_lt hq0)] using this
  have hnum : Tendsto (fun q : ℝ => qNumberSym (Real.sqrt q) twoJ) (𝓝[≠] 1) (𝓝 (twoJ : ℝ)) :=
    (qNumberSym_classical_limit twoJ).comp hsqrt_punc
  have hden : Tendsto (fun q : ℝ => Real.sqrt q + (Real.sqrt q)⁻¹) (𝓝[≠] 1) (𝓝 (1 + (1 : ℝ)⁻¹)) :=
    hsqrt_lim.add (hsqrt_lim.inv₀ one_ne_zero)
  have hden2 : (1 + (1 : ℝ)⁻¹) = (2 : ℝ) := by norm_num
  rw [hden2] at hden
  exact hnum.div hden two_ne_zero

/-- Punctured-neighbourhood classical limit `[j]_q [j + 1]_q → j (j + 1)` as `q → 1` (`q ≠ 1`)
    for every integer or half-integer `𝔰𝔲(2)` spin `j = twoJ / 2` (`twoJ ∈ ℤ`). -/
theorem QCasimirEigenvalueHalf_classical_limit (twoJ : ℤ) :
    Tendsto (fun q : ℝ => QCasimirEigenvalueHalf q twoJ) (𝓝[≠] 1)
      (𝓝 (((twoJ : ℝ) / 2) * ((twoJ : ℝ) / 2 + 1))) := by
  unfold QCasimirEigenvalueHalf
  have h1 := qNumberSymHalf_classical_limit twoJ
  have h2 := qNumberSymHalf_classical_limit (twoJ + 2)
  have hcast : ((twoJ + 2 : ℤ) : ℝ) / 2 = (twoJ : ℝ) / 2 + 1 := by push_cast; ring
  rw [hcast] at h2
  exact h1.mul h2

end QOU
