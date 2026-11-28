import QOU.Observations.KnotConvolutionLog

/-!
# The `4₁` convolution operator is unipotent: `c_N(4₁) = 1` at `ℏ = 0`

`KnotConvolutionLog.lean` proves that a unipotent convolution operator (scalars equal to `1` at
`ℏ = 0`) is the exponential of its tangent family, with unipotence as a hypothesis. This file
removes that hypothesis for the figure-eight knot `4₁`, the one knot whose normalised coloured
Jones polynomial the corpus defines for every colour (Habiro's cyclotomic sum `habiroJ41`).

* `habiroJ41R q qi N = Σ_{m<N} Π_{j<m} (q^N + qi^N − q^{j+1} − qi^{j+1})`: Habiro's sum over any
  commutative ring, with `qi` in place of `q⁻¹`. `habiroJ41R_inv`: over a field it is
  `habiroJ41 q N`.
* `habiroJ41R_one_one`: at `q = qi = 1` it is `1` for every colour `N ≥ 1` (each factor with
  `m ≥ 1` contains `j = 0`, which is `1 + 1 − 1 − 1 = 0`).
* `habiroOp41`: the operator with `c_N = habiroJ41R (e^ℏ) (e^{−ℏ}) N` in `K⟦ℏ⟧`, where
  `e^{±ℏ} = gmExp (±X)` and `gmExp X * gmExp (−X) = 1` (`gmExp_mul_gmExp_neg`). The colour-`0`
  block is empty (`Matrix (Fin 0) (Fin 0)`), so its scalar is set to `1`.
* `isUnipotent_habiroOp41`: **`c_N(4₁) = 1` at `ℏ = 0` for every colour**, proved, since
  `constantCoeff` is a ring map sending `e^{±ℏ}` to `1`.
* `habiroOp41_eq_expOp_logOp`: hence `c(4₁) = exp(log c(4₁))` with no hypothesis.

Scope: only `4₁`. The corpus has no coloured Jones polynomial for a general knot, so the
statement `c_N(K) = 1` at `ℏ = 0` for every knot is not stated here. Pure algebra over a field of
characteristic `0`. No measured values.
-/

namespace QOU.Observations.KnotConvolutionOperator

open PowerSeries QOU.FormalGroups.GmLog

noncomputable section

section Ring

variable {R S : Type*} [CommRing R] [CommRing S]

/-- Habiro's sum for `4₁` over a commutative ring, with `qi` in place of `q⁻¹`. -/
def habiroJ41R (q qi : R) (N : ℕ) : R :=
  ∑ m ∈ Finset.range N, ∏ j ∈ Finset.range m, (q ^ N + qi ^ N - q ^ (j + 1) - qi ^ (j + 1))

/-- **At `q = qi = 1` the sum is `1` in every colour `N ≥ 1`.** -/
theorem habiroJ41R_one_one (N : ℕ) (hN : 1 ≤ N) : habiroJ41R (1 : R) 1 N = 1 := by
  obtain ⟨n, rfl⟩ : ∃ n, N = n + 1 := ⟨N - 1, by omega⟩
  unfold habiroJ41R
  rw [Finset.sum_range_succ']
  simp

/-- Ring maps commute with the Habiro sum. -/
theorem map_habiroJ41R (f : R →+* S) (q qi : R) (N : ℕ) :
    f (habiroJ41R q qi N) = habiroJ41R (f q) (f qi) N := by
  simp [habiroJ41R, map_sum, map_prod]

end Ring

theorem habiroJ41R_inv {F : Type*} [Field F] [DecidableEq F] (q : F) (N : ℕ) :
    habiroJ41R q q⁻¹ N = habiroJ41 q N := by
  simp [habiroJ41R, habiroJ41, inv_pow]

variable {K : Type*} [Field K] [CharZero K]

/-- `e^ℏ · e^{−ℏ} = 1` in `K⟦ℏ⟧`. -/
theorem gmExp_mul_gmExp_neg : gmExp (X : K⟦X⟧) * gmExp (-X) = 1 := by
  rw [← gmExp_add (by simp) (by simp), add_neg_cancel]
  have h := gmExp_formalLog (f := (1 : K⟦X⟧)) (by simp)
  rwa [formalLog_one] at h

/-- The `4₁` convolution operator in `K⟦ℏ⟧`: `c_N = J'_N(4₁)` at `q = e^ℏ`. The colour-`0`
block is empty, and its scalar is set to `1`. -/
def habiroOp41 : ConvOp K⟦X⟧ :=
  ⟨fun N => if N = 0 then 1 else habiroJ41R (gmExp (X : K⟦X⟧)) (gmExp (-X)) N⟩

omit [CharZero K] in
/-- **`c_N(4₁) = 1` at `ℏ = 0`, for every colour.** -/
theorem isUnipotent_habiroOp41 : IsUnipotent (habiroOp41 (K := K)) := by
  intro N
  dsimp only [habiroOp41]
  split_ifs with hN
  · simp
  · rw [map_habiroJ41R, constantCoeff_gmExp, constantCoeff_gmExp]
    exact habiroJ41R_one_one N (by omega)

/-- **`c(4₁) = exp(log c(4₁))`, unconditionally.** -/
theorem habiroOp41_eq_expOp_logOp : expOp (logOp (habiroOp41 (K := K))) = habiroOp41 :=
  expOp_logOp isUnipotent_habiroOp41

end

end QOU.Observations.KnotConvolutionOperator
