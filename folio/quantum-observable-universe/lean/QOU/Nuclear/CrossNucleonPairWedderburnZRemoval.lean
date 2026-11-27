/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Tactic
import HeckeTemperleyLieb.OcneanuWeight
import BraidKnotOctonion.TwoRowDimCatalan
import BraidKnotOctonion.BorromeanMarkovTrace
import QOU.Nuclear.WeightedTraceSide
import QOU.Nuclear.PairTermSectorSymmetry
import QOU.Nuclear.NeutralExchangeSplit
import QOU.Nuclear.CoulombNeedsZRemoval
import QOU.MassTheory.QuarkChargeReduction

/-!
# All-`q` `H₇(q), H₈(q)` Two-Row Wedderburn Pair Identities, Coideal Killing-Norm Hypercharge Slope `1/2`, and Separated-Hadron `Z`-Channel Removal

Workstream `W2` — Beans `qou-20sx`, `qou-vudb`, `qou-fbrp`.
Pre-registered 80-dps companion probe:
`computations/probes/w2_h7_h8_wedderburn_zremoval/w2_h7_h8_wedderburn_zremoval_probe.py`.

Following `§7c` base-ring discipline, Sections 1–3 and the algebraic neutral-current identities of
Section 4 are proved over arbitrary `[CommRing R]` or `[Field F]` (`0` empirical numbers inside
Lean), specializing to `ℝ` solely at the archimedean boundary where `Real.exp` governs the massive
`Z` Yukawa propagator `λ(x) = exp(-x)`.

## Summary of Main Theorems

1. **Section 1 — Convention-D Two-Row Wedderburn Reduction on `H₇(q)` and `H₈(q)`:**
   * At Convention D (`z_D = q³ / (q² + 1)`), `OcneanuWeight.ocneanuWeight_conventionD_eq_zero_of_three_rows`
     annihilates every partition with `ℓ(λ) ≥ 3`, collapsing any weighted character sum on `H₇(q)`
     (`7! = 5,040`) to the **four** two-row blocks `{(7,0), (6,1), (5,2), (4,3)}` of ballot
     dimensions `(1, 6, 14, 14)` (`∑ d_λ² = 429 = C₇`, radical corank `4,611`,
     `h7_twoRow_wedderburn_reduction`) and on `H₈(q)` (`8! = 40,320`) to the **five** two-row
     blocks `{(8,0), (7,1), (6,2), (5,3), (4,4)}` of ballot dimensions `(1, 7, 20, 28, 14)`
     (`∑ d_λ² = 1,430 = C₈`, radical corank `38,890`, `h8_twoRow_wedderburn_reduction`).
   * Division-free quantum Schur–Weyl character decompositions on `(V₂)^{⊗7}` and `(V₂)^{⊗8}` over
     any `[CommRing R]` (`h7_quantum_schur_weyl_decomp`, `h8_quantum_schur_weyl_decomp`), normalized
     two-row weight sums `∑ d_λ w_λ = 1` (`h7_twoRowWeightD_sum_eq_one`, `h8_twoRowWeightD_sum_eq_one`),
     and exact two-row generator character sums `∑ w_λ χ^λ(σ_i) = z_D` and
     `∑ w_λ χ^λ(σ_i⁻¹) = z̄_D = 1 / (q(q² + 1))` (`h7_twoRow_gen_trace_eq_zD`,
     `h8_twoRow_gen_trace_eq_zD`).

2. **Section 2 — Extending `WeightedTraceSide` to `H₇(q), H₈(q)` & Cross-Nucleon Pair Identities (`qou-vudb`):**
   * Normalized right-spectator closure of `Ř` and `Ř⁻¹` equals `z_D` and `z̄_D`
     (`rightTrace_R_norm_eq_zD`, `rightTrace_Rinv_norm_eq_zDBar`), and two-step right stabilization
     on `H₈(q)` (`L8e`) factors multiplicatively (`rightTrace2_R_norm_eq_zD_sq`,
     `rightTrace2_R_Rinv_norm_eq_zD_mul_zDBar`).
   * Iterated left-spectator closure (`leftChainOp`) of `m + 1` crossings collapses by induction
     over any `[Field F]` (`q ≠ 0`) to the exact rank-2 diagonal weight-counting operator
     `diag(1 + (q² + 1)(q^{2m} - q⁻²), 1)` (`leftChainOp_succ_closed_form`), satisfying the exact
     `H₈`–`H₇` linear dependence `L₂(q) = (q² + 1) L₁(q) - q² I₂` (`leftChainOp_two_linear_comb`),
     being non-scalar whenever `q² + 1 ≠ 0` and `(q²)^{m+1} ≠ 1` (`leftChainOp_succ_not_scalar`),
     and preserving the six-strand rational pair parameter `α₆(q)` satisfying
     `α₆(q) + α₆(q⁻¹) = 1` (`alphaSix_add_betaSix`, `h7_h8_pinned_alphaSix_not_coulomb`).
   * Cross-cluster skein dressings (`pp`, `pn`, `nn`) have purely isovector split
     `T_pp - T_nn = (q - q⁻¹) F` and zero `Q_A Q_B` Coulomb curvature `T_pp - 2 T_pn + T_nn = 0`
     (`crossCluster_skein_isovector_and_zero_coulomb`).

3. **Section 3 — Split-Bundle `F = V₂ ⊕ W₃*` Killing-Norm Normalization & GMN Slope `1/2` (`qou-20sx`, `qou-fbrp`):**
   * On `F = V₂ ⊕ W₃*`, weak isospin `T₃` satisfies `Tr_F(T₃) = 0`, `Tr_F(T₃²) = 1/2`,
     `Tr_F((2 T₃)²) = 2` (`splitT3_traces`), and Killing orthogonality `Tr_F(T₃ Y) = 0`
     (`splitT3_orthogonal_splitY`). Tracelessness `Tr_F(Y) = 0` forces `y₃ = -(2/3) y₂`
     (`traceless_splitY_iff`), giving `Tr_F((Y/2)²) = 5/6` at `y₂ = -1` (`splitY_half_sq_trace`),
     full-generation traces `Tr_G(T₃²) = 2` and `Tr_G((Y/2)²) = 10/3`, and unrenormalized Weinberg
     angle `sin²θ_W⁰ = 3/8` on both `F` and `G` (`weinberg_trace_ratio_three_eighths`).
   * Either coideal highest-weight neutrality `Q(ν_L) = 0` or Killing-norm closure
     `Tr_F(Q²) = 4/3` with `Q(ν_L) = 0` unconditionally forces the Gell-Mann–Nishijima slope
     `α_Y = 1/2` in `Q = T₃ + α_Y Y` (`gmn_slope_half_iff`, `gmn_slope_half_from_killing_norm`),
     deriving `Y(Q_L) = 1/3`, `c = 1/6`, `(q_u, q_d) = (2/3, -1/3)`, `(Q_p, Q_n) = (1, 0)`, and
     all three chiral anomaly cancellations (`chiral_generation_anomaly_cancellation`).

4. **Section 4 — Separated-Hadron `Z`-Channel Removal (`CoulombNeedsZRemoval` Bridge & `< 10⁻²⁸⁰` Yukawa Suppression):**
   * Exact neutral-current residuals of `CoulombNeedsZRemoval.exch` at arbitrary `λ`
     (`exch_at_one_pp_eq_nn`, `exch_residuals_exact`, `exch_at_weinberg_three_eighths`).
   * Pure `Real.sum_le_exp_of_nonneg` proof that `0 < exp(-x) < 10⁻²⁸² < 10⁻²⁸⁰` for every
     dimensionless Compton separation `x ≥ 653` (`yukawaZ_lt_ten_neg_282`), suppressing all
     neutral-current `Z`-contamination relative to `e²` below `10⁻²⁸⁰`
     (`nuclear_z_channel_coulomb_isolation_280_digits`).

-- Ref: [jimbo1986] https://doi.org/10.1007/BF00400222
-- Ref: [wenzl1988] https://doi.org/10.1007/BF01394347
-- Ref: [ram1997] https://doi.org/10.1112/S0024611597000282
-/

namespace QOU.QBeta.CrossNucleonPairWedderburnZRemoval

open scoped BigOperators
open QOU.Mathlib (ballot dimHLF_two_row_sq_sum)
open QOU.SchurWeyl (ocneanuWeight ocneanuWeight_conventionD_eq_zero_of_three_rows)
open QOU.QBeta.WeightedTraceSide (Kw R Rinv rightTrace leftTrace rightTrace_R rightTrace_Rinv
  leftTrace_R)
open QOU.QBeta.PairTermSectorSymmetry (pairTerm not_coulomb_of_pinned_alpha)
open QOU.QBeta.CoulombNeedsZRemoval (exch CoulombShape coulombShape_iff_Z_removed)
open QOU.MassTheory.QuarkChargeReduction (qu qd charges_of_c)

/-! ## Section 1: Convention-D Two-Row Wedderburn Accounting on `H₇(q)` and `H₈(q)` -/

section TwoRowWedderburnAccounting

/-- Two-row ballot dimensions `(1, 6, 14, 14)` on `H₇(q)` (`λ ∈ {(7,0), (6,1), (5,2), (4,3)}`),
their Wedderburn square-sum `429 = C₇`, and the Convention-D radical corank `7! - 429 = 4,611`. -/
theorem h7_twoRow_wedderburn_reduction :
    ballot 7 0 = 1 ∧
    ballot 7 1 = 6 ∧
    ballot 7 2 = 14 ∧
    ballot 7 3 = 14 ∧
    (ballot 7 0) ^ 2 + (ballot 7 1) ^ 2 + (ballot 7 2) ^ 2 + (ballot 7 3) ^ 2 = 429 ∧
    catalan 7 = 429 ∧
    Nat.factorial 7 - 429 = 4611 := by
  refine ⟨by decide, by decide, by decide, by decide, by decide, ?_, by decide⟩
  rw [catalan_eq_centralBinom_div]
  decide

/-- Two-row ballot dimensions `(1, 7, 20, 28, 14)` on `H₈(q)`
(`λ ∈ {(8,0), (7,1), (6,2), (5,3), (4,4)}`), their Wedderburn square-sum `1,430 = C₈`, and the
Convention-D radical corank `8! - 1,430 = 38,890`. -/
theorem h8_twoRow_wedderburn_reduction :
    ballot 8 0 = 1 ∧
    ballot 8 1 = 7 ∧
    ballot 8 2 = 20 ∧
    ballot 8 3 = 28 ∧
    ballot 8 4 = 14 ∧
    (ballot 8 0) ^ 2 + (ballot 8 1) ^ 2 + (ballot 8 2) ^ 2 + (ballot 8 3) ^ 2 +
      (ballot 8 4) ^ 2 = 1430 ∧
    catalan 8 = 1430 ∧
    Nat.factorial 8 - 1430 = 38890 := by
  refine ⟨by decide, by decide, by decide, by decide, by decide, by decide, ?_, by decide⟩
  rw [catalan_eq_centralBinom_div]
  decide

/-- Division-free balanced quantum integer `[m]_q = ∑_{s=0}^{m-1} q^{m-1-s} qi^s` over any
commutative ring `R`. When `q * qi = 1`, this equals `(q^m - qi^m) / (q - qi)`. -/
def qIntSum {R : Type*} [CommRing R] (q qi : R) (m : ℕ) : R :=
  ∑ s ∈ Finset.range m, q ^ (m - 1 - s) * qi ^ s

/-- Telescoping identity `(q - qi) * [m]_q = q^m - qi^m` over any commutative ring `R`. -/
theorem mul_qIntSum_eq_pow_sub {R : Type*} [CommRing R] (q qi : R) (m : ℕ) :
    (q - qi) * qIntSum q qi m = q ^ m - qi ^ m := by
  induction m with
  | zero =>
    simp [qIntSum]
  | succ m ih =>
    cases m with
    | zero =>
      simp [qIntSum]
    | succ n =>
      have hsplit :
          qIntSum q qi (n + 2) = q * qIntSum q qi (n + 1) + qi ^ (n + 1) := by
        unfold qIntSum
        rw [Finset.sum_range_succ, Finset.mul_sum]
        have hlast : q ^ (n + 2 - 1 - (n + 1)) * qi ^ (n + 1) = qi ^ (n + 1) := by
          have hz : n + 2 - 1 - (n + 1) = 0 := by omega
          rw [hz, pow_zero, one_mul]
        rw [hlast]
        congr 1
        refine Finset.sum_congr rfl fun s hs => ?_
        have hlt : s < n + 1 := Finset.mem_range.mp hs
        have hexp : n + 2 - 1 - s = (n + 1 - 1 - s) + 1 := by omega
        rw [hexp, pow_succ]
        ring
      rw [hsplit, mul_add, ← mul_assoc]
      have hcomm : (q - qi) * q = q * (q - qi) := by ring
      rw [hcomm, mul_assoc, ih]
      ring

/-- Clebsch–Gordan two-box step `(q + qi) * [m + 1]_q = [m + 2]_q + [m]_q` (`1 ≤ m ≤ 7`) over any
commutative ring `R` whenever `q * qi = 1`. -/
theorem qIntSum_two_mul_steps {R : Type*} [CommRing R] (q qi : R) (hqi : q * qi = 1) :
    qIntSum q qi 1 = 1 ∧
    qIntSum q qi 2 = q + qi ∧
    (q + qi) * qIntSum q qi 2 = qIntSum q qi 3 + qIntSum q qi 1 ∧
    (q + qi) * qIntSum q qi 3 = qIntSum q qi 4 + qIntSum q qi 2 ∧
    (q + qi) * qIntSum q qi 4 = qIntSum q qi 5 + qIntSum q qi 3 ∧
    (q + qi) * qIntSum q qi 5 = qIntSum q qi 6 + qIntSum q qi 4 ∧
    (q + qi) * qIntSum q qi 6 = qIntSum q qi 7 + qIntSum q qi 5 ∧
    (q + qi) * qIntSum q qi 7 = qIntSum q qi 8 + qIntSum q qi 6 ∧
    (q + qi) * qIntSum q qi 8 = qIntSum q qi 9 + qIntSum q qi 7 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · simp [qIntSum]
  · simp [qIntSum, Finset.sum_range_succ]
  · simp only [qIntSum, Finset.sum_range_succ, Finset.sum_range_zero]; linear_combination 1 * hqi
  · simp only [qIntSum, Finset.sum_range_succ, Finset.sum_range_zero]
    linear_combination (q + qi) * hqi
  · simp only [qIntSum, Finset.sum_range_succ, Finset.sum_range_zero]
    linear_combination (q ^ 2 + q * qi + qi ^ 2) * hqi
  · simp only [qIntSum, Finset.sum_range_succ, Finset.sum_range_zero]
    linear_combination (q ^ 3 + q ^ 2 * qi + q * qi ^ 2 + qi ^ 3) * hqi
  · simp only [qIntSum, Finset.sum_range_succ, Finset.sum_range_zero]
    linear_combination (q ^ 4 + q ^ 3 * qi + q ^ 2 * qi ^ 2 + q * qi ^ 3 + qi ^ 4) * hqi
  · simp only [qIntSum, Finset.sum_range_succ, Finset.sum_range_zero]
    linear_combination
      (q ^ 5 + q ^ 4 * qi + q ^ 3 * qi ^ 2 + q ^ 2 * qi ^ 3 + q * qi ^ 4 + qi ^ 5) * hqi
  · simp only [qIntSum, Finset.sum_range_succ, Finset.sum_range_zero]
    linear_combination
      (q ^ 6 + q ^ 5 * qi + q ^ 4 * qi ^ 2 + q ^ 3 * qi ^ 3 + q ^ 2 * qi ^ 4 + q * qi ^ 5 +
        qi ^ 6) * hqi

/-- Quantum Schur–Weyl character decompositions on `(V₂)^{⊗5}` and `(V₂)^{⊗6}`, used to evaluate
single-crossing generator traces on `H₇(q)` and `H₈(q)` by column-removal branching. -/
theorem h5_h6_quantum_schur_weyl_decomp {R : Type*} [CommRing R] (q qi : R) (hqi : q * qi = 1) :
    (1 * qIntSum q qi 6 + 4 * qIntSum q qi 4 + 5 * qIntSum q qi 2 = (q + qi) ^ 5) ∧
    (1 * qIntSum q qi 7 + 5 * qIntSum q qi 5 + 9 * qIntSum q qi 3 + 5 * qIntSum q qi 1 =
      (q + qi) ^ 6) := by
  obtain ⟨s1, s2, st2, st3, st4, st5, st6, -, -⟩ := qIntSum_two_mul_steps q qi hqi
  have p2 : qIntSum q qi 3 + qIntSum q qi 1 = (q + qi) ^ 2 := by
    linear_combination -st2 + (q + qi) * s2
  have p3 : qIntSum q qi 4 + 2 * qIntSum q qi 2 = (q + qi) ^ 3 := by
    linear_combination -st3 - (q + qi) * s1 + s2 + (q + qi) * p2
  have p4 : qIntSum q qi 5 + 3 * qIntSum q qi 3 + 2 * qIntSum q qi 1 = (q + qi) ^ 4 := by
    linear_combination -st4 - 2 * st2 + (q + qi) * p3
  have p5 : 1 * qIntSum q qi 6 + 4 * qIntSum q qi 4 + 5 * qIntSum q qi 2 = (q + qi) ^ 5 := by
    linear_combination -st5 - 3 * st3 - 2 * (q + qi) * s1 + 2 * s2 + (q + qi) * p4
  have p6 :
      1 * qIntSum q qi 7 + 5 * qIntSum q qi 5 + 9 * qIntSum q qi 3 + 5 * qIntSum q qi 1 =
        (q + qi) ^ 6 := by
    linear_combination -st6 - 4 * st4 - 5 * st2 + (q + qi) * p5
  exact ⟨p5, p6⟩

/-- **Quantum Schur–Weyl Character Decomposition on `(V₂)^{⊗7}` (`[CommRing R]`):**
`1·[8]_q + 6·[6]_q + 14·[4]_q + 14·[2]_q = (q + qi)^7` whenever `q * qi = 1`. -/
theorem h7_quantum_schur_weyl_decomp {R : Type*} [CommRing R] (q qi : R) (hqi : q * qi = 1) :
    1 * qIntSum q qi 8 + 6 * qIntSum q qi 6 + 14 * qIntSum q qi 4 + 14 * qIntSum q qi 2 =
      (q + qi) ^ 7 := by
  obtain ⟨s1, s2, -, st3, -, st5, -, st7, -⟩ := qIntSum_two_mul_steps q qi hqi
  have p6 := (h5_h6_quantum_schur_weyl_decomp q qi hqi).2
  linear_combination -st7 - 5 * st5 - 9 * st3 - 5 * (q + qi) * s1 + 5 * s2 + (q + qi) * p6

/-- **Quantum Schur–Weyl Character Decomposition on `(V₂)^{⊗8}` (`[CommRing R]`):**
`1·[9]_q + 7·[7]_q + 20·[5]_q + 28·[3]_q + 14·[1]_q = (q + qi)^8` whenever `q * qi = 1`. -/
theorem h8_quantum_schur_weyl_decomp {R : Type*} [CommRing R] (q qi : R) (hqi : q * qi = 1) :
    1 * qIntSum q qi 9 + 7 * qIntSum q qi 7 + 20 * qIntSum q qi 5 + 28 * qIntSum q qi 3 +
      14 * qIntSum q qi 1 = (q + qi) ^ 8 := by
  obtain ⟨-, -, st2, -, st4, -, st6, -, st8⟩ := qIntSum_two_mul_steps q qi hqi
  have p7 := h7_quantum_schur_weyl_decomp q qi hqi
  linear_combination -st8 - 6 * st6 - 14 * st4 - 14 * st2 + (q + qi) * p7

/-- Convention-D Markov parameter `z_D(q) = q³ / (q² + 1)`. -/
def zD {F : Type*} [Field F] (q : F) : F := q ^ 3 / (q ^ 2 + 1)

/-- Inverse-crossing Convention-D Markov parameter `z̄_D(q) = 1 / (q (q² + 1))`. -/
def zDBar {F : Type*} [Field F] (q : F) : F := 1 / (q * (q ^ 2 + 1))

/-- Bar-involution and skein difference on Convention-D Markov parameters:
`z_D(q⁻¹) = z̄_D(q)` and `z_D(q) - z̄_D(q) = q - q⁻¹`. -/
theorem zD_bar_and_skein_diff {F : Type*} [Field F] (q : F) (hq : q ≠ 0)
    (hq21 : q ^ 2 + 1 ≠ 0) :
    zD q⁻¹ = zDBar q ∧ zD q - zDBar q = q - q⁻¹ := by
  have h1q2 : 1 + q ^ 2 ≠ 0 := by
    intro h; exact hq21 (by linear_combination h)
  unfold zD zDBar
  constructor
  · have hrewrite : (q⁻¹) ^ 2 + 1 = (1 + q ^ 2) / q ^ 2 := by field_simp
    rw [hrewrite]
    field_simp
    ring
  · field_simp
    ring

/-- Non-vanishing of `[2]_q = q + q⁻¹` from `q ≠ 0` and `q² + 1 ≠ 0`. -/
theorem q_add_inv_ne_zero {F : Type*} [Field F] (q : F) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0) :
    q + q⁻¹ ≠ 0 := by
  intro h
  apply hq21
  have hmul : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
  rw [h, mul_zero] at hmul
  exact hmul.symm

/-- Closed-form Convention-D Ocneanu weight `w_{(N-k, k)}(q, z_D) = [N - 2k + 1]_q / (q + q⁻¹)^N`
on two-row blocks `(N - k, k) ⊢ N`. -/
def twoRowWeightD {F : Type*} [Field F] (q : F) (N k : ℕ) : F :=
  qIntSum q q⁻¹ (N - 2 * k + 1) / (q + q⁻¹) ^ N

/-- Any weighted sum over partitions of `N` weighted by `ocneanuWeight q (zD q)` kills every
diagram with `0 < μ.rowLen 2` (`ℓ(μ) ≥ 3`), leaving only the `ℓ(μ) ≤ 2` summands. -/
theorem ocneanu_conventionD_sum_restricts_to_twoRow {F : Type*} [Field F] {ι : Type*}
    (s : Finset ι) (μ : ι → YoungDiagram) (χ : ι → F) (q : F) (hq21 : q ^ 2 + 1 ≠ 0) :
    ∑ i ∈ s, ocneanuWeight q (zD q) (μ i) * χ i =
      ∑ i ∈ s.filter (fun i => (μ i).rowLen 2 = 0), ocneanuWeight q (zD q) (μ i) * χ i := by
  rw [Finset.sum_filter]
  refine Finset.sum_congr rfl fun i _ => ?_
  rcases Nat.eq_zero_or_pos ((μ i).rowLen 2) with h0 | hpos
  · simp [h0]
  · have hne : (μ i).rowLen 2 ≠ 0 := Nat.pos_iff_ne_zero.mp hpos
    simp only [hne, ↓reduceIte]
    unfold zD
    rw [ocneanuWeight_conventionD_eq_zero_of_three_rows q hq21 (μ i) hpos, zero_mul]

/-- **Normalized Two-Row Weight Sum on `H₇(q)` (`∑ d_λ w_λ = 1`):** -/
theorem h7_twoRowWeightD_sum_eq_one {F : Type*} [Field F] (q : F) (hq : q ≠ 0)
    (hq21 : q ^ 2 + 1 ≠ 0) :
    1 * twoRowWeightD q 7 0 + 6 * twoRowWeightD q 7 1 + 14 * twoRowWeightD q 7 2 +
      14 * twoRowWeightD q 7 3 = 1 := by
  have h2q : q + q⁻¹ ≠ 0 := q_add_inv_ne_zero q hq hq21
  have hpow : (q + q⁻¹) ^ 7 ≠ 0 := pow_ne_zero 7 h2q
  unfold twoRowWeightD
  simp only [Nat.reduceMul, Nat.reduceSub, Nat.reduceAdd]
  have hsw := h7_quantum_schur_weyl_decomp q q⁻¹ (mul_inv_cancel₀ hq)
  calc
    1 * (qIntSum q q⁻¹ 8 / (q + q⁻¹) ^ 7) + 6 * (qIntSum q q⁻¹ 6 / (q + q⁻¹) ^ 7) +
        14 * (qIntSum q q⁻¹ 4 / (q + q⁻¹) ^ 7) + 14 * (qIntSum q q⁻¹ 2 / (q + q⁻¹) ^ 7)
      = (1 * qIntSum q q⁻¹ 8 + 6 * qIntSum q q⁻¹ 6 + 14 * qIntSum q q⁻¹ 4 +
          14 * qIntSum q q⁻¹ 2) / (q + q⁻¹) ^ 7 := by ring
    _ = (q + q⁻¹) ^ 7 / (q + q⁻¹) ^ 7 := by rw [hsw]
    _ = 1 := div_self hpow

/-- **Normalized Two-Row Weight Sum on `H₈(q)` (`∑ d_λ w_λ = 1`):** -/
theorem h8_twoRowWeightD_sum_eq_one {F : Type*} [Field F] (q : F) (hq : q ≠ 0)
    (hq21 : q ^ 2 + 1 ≠ 0) :
    1 * twoRowWeightD q 8 0 + 7 * twoRowWeightD q 8 1 + 20 * twoRowWeightD q 8 2 +
      28 * twoRowWeightD q 8 3 + 14 * twoRowWeightD q 8 4 = 1 := by
  have h2q : q + q⁻¹ ≠ 0 := q_add_inv_ne_zero q hq hq21
  have hpow : (q + q⁻¹) ^ 8 ≠ 0 := pow_ne_zero 8 h2q
  unfold twoRowWeightD
  simp only [Nat.reduceMul, Nat.reduceSub, Nat.reduceAdd]
  have hsw := h8_quantum_schur_weyl_decomp q q⁻¹ (mul_inv_cancel₀ hq)
  calc
    1 * (qIntSum q q⁻¹ 9 / (q + q⁻¹) ^ 8) + 7 * (qIntSum q q⁻¹ 7 / (q + q⁻¹) ^ 8) +
        20 * (qIntSum q q⁻¹ 5 / (q + q⁻¹) ^ 8) + 28 * (qIntSum q q⁻¹ 3 / (q + q⁻¹) ^ 8) +
        14 * (qIntSum q q⁻¹ 1 / (q + q⁻¹) ^ 8)
      = (1 * qIntSum q q⁻¹ 9 + 7 * qIntSum q q⁻¹ 7 + 20 * qIntSum q q⁻¹ 5 +
          28 * qIntSum q q⁻¹ 3 + 14 * qIntSum q q⁻¹ 1) / (q + q⁻¹) ^ 8 := by ring
    _ = (q + q⁻¹) ^ 8 / (q + q⁻¹) ^ 8 := by rw [hsw]
    _ = 1 := div_self hpow

/-- **Two-Row Single-Generator Character Sum on `H₇(q)` (`∑ w_λ χ^λ(σ_i) = z_D` and `σ_i⁻¹ ↦ z̄_D`):**
On the four two-row blocks `(7,0), (6,1), (5,2), (4,3)`, column-removal branching gives exact
generator traces `(q, 5q - q⁻¹, 10q - 4q⁻¹, 9q - 5q⁻¹)`. Their Convention-D weighted sum collapses
identically to `z_D = q³ / (q² + 1)` (and to `z̄_D = 1 / (q(q² + 1))` for `σ_i⁻¹`). -/
theorem h7_twoRow_gen_trace_eq_zD {F : Type*} [Field F] (q : F) (hq : q ≠ 0)
    (hq21 : q ^ 2 + 1 ≠ 0) :
    (twoRowWeightD q 7 0 * q +
      twoRowWeightD q 7 1 * (5 * q - q⁻¹) +
      twoRowWeightD q 7 2 * (10 * q - 4 * q⁻¹) +
      twoRowWeightD q 7 3 * (9 * q - 5 * q⁻¹) = zD q) ∧
    (twoRowWeightD q 7 0 * (q - (q - q⁻¹)) +
      twoRowWeightD q 7 1 * ((5 * q - q⁻¹) - 6 * (q - q⁻¹)) +
      twoRowWeightD q 7 2 * ((10 * q - 4 * q⁻¹) - 14 * (q - q⁻¹)) +
      twoRowWeightD q 7 3 * ((9 * q - 5 * q⁻¹) - 14 * (q - q⁻¹)) = zDBar q) := by
  have h2q : q + q⁻¹ ≠ 0 := q_add_inv_ne_zero q hq hq21
  have hsw7 := h7_quantum_schur_weyl_decomp q q⁻¹ (mul_inv_cancel₀ hq)
  have hsw5 := (h5_h6_quantum_schur_weyl_decomp q q⁻¹ (mul_inv_cancel₀ hq)).1
  have hpos :
      twoRowWeightD q 7 0 * q +
        twoRowWeightD q 7 1 * (5 * q - q⁻¹) +
        twoRowWeightD q 7 2 * (10 * q - 4 * q⁻¹) +
        twoRowWeightD q 7 3 * (9 * q - 5 * q⁻¹) = zD q := by
    unfold twoRowWeightD zD
    simp only [Nat.reduceMul, Nat.reduceSub, Nat.reduceAdd]
    have hnum :
        qIntSum q q⁻¹ 8 * q + qIntSum q q⁻¹ 6 * (5 * q - q⁻¹) +
          qIntSum q q⁻¹ 4 * (10 * q - 4 * q⁻¹) + qIntSum q q⁻¹ 2 * (9 * q - 5 * q⁻¹) =
        q * (1 * qIntSum q q⁻¹ 8 + 6 * qIntSum q q⁻¹ 6 + 14 * qIntSum q q⁻¹ 4 +
          14 * qIntSum q q⁻¹ 2) -
        (q + q⁻¹) * (1 * qIntSum q q⁻¹ 6 + 4 * qIntSum q q⁻¹ 4 + 5 * qIntSum q q⁻¹ 2) := by ring
    calc
      qIntSum q q⁻¹ 8 / (q + q⁻¹) ^ 7 * q +
          qIntSum q q⁻¹ 6 / (q + q⁻¹) ^ 7 * (5 * q - q⁻¹) +
          qIntSum q q⁻¹ 4 / (q + q⁻¹) ^ 7 * (10 * q - 4 * q⁻¹) +
          qIntSum q q⁻¹ 2 / (q + q⁻¹) ^ 7 * (9 * q - 5 * q⁻¹)
        = (qIntSum q q⁻¹ 8 * q + qIntSum q q⁻¹ 6 * (5 * q - q⁻¹) +
            qIntSum q q⁻¹ 4 * (10 * q - 4 * q⁻¹) + qIntSum q q⁻¹ 2 * (9 * q - 5 * q⁻¹)) /
          (q + q⁻¹) ^ 7 := by ring
      _ = (q * (q + q⁻¹) ^ 7 - (q + q⁻¹) * (q + q⁻¹) ^ 5) / (q + q⁻¹) ^ 7 := by
            rw [hnum, hsw7, hsw5]
      _ = q ^ 3 / (q ^ 2 + 1) := by
            field_simp
            ring
  refine ⟨hpos, ?_⟩
  have h1 := h7_twoRowWeightD_sum_eq_one q hq hq21
  have hdiff := (zD_bar_and_skein_diff q hq hq21).2
  linear_combination hpos - (q - q⁻¹) * h1 + hdiff

/-- **Two-Row Single-Generator Character Sum on `H₈(q)` (`∑ w_λ χ^λ(σ_i) = z_D` and `σ_i⁻¹ ↦ z̄_D`):**
On the five two-row blocks `(8,0), (7,1), (6,2), (5,3), (4,4)`, column-removal branching gives
exact generator traces `(q, 6q - q⁻¹, 15q - 5q⁻¹, 19q - 9q⁻¹, 9q - 5q⁻¹)`. Their Convention-D
weighted sum collapses identically to `z_D` (and to `z̄_D` for `σ_i⁻¹`). -/
theorem h8_twoRow_gen_trace_eq_zD {F : Type*} [Field F] (q : F) (hq : q ≠ 0)
    (hq21 : q ^ 2 + 1 ≠ 0) :
    (twoRowWeightD q 8 0 * q +
      twoRowWeightD q 8 1 * (6 * q - q⁻¹) +
      twoRowWeightD q 8 2 * (15 * q - 5 * q⁻¹) +
      twoRowWeightD q 8 3 * (19 * q - 9 * q⁻¹) +
      twoRowWeightD q 8 4 * (9 * q - 5 * q⁻¹) = zD q) ∧
    (twoRowWeightD q 8 0 * (q - (q - q⁻¹)) +
      twoRowWeightD q 8 1 * ((6 * q - q⁻¹) - 7 * (q - q⁻¹)) +
      twoRowWeightD q 8 2 * ((15 * q - 5 * q⁻¹) - 20 * (q - q⁻¹)) +
      twoRowWeightD q 8 3 * ((19 * q - 9 * q⁻¹) - 28 * (q - q⁻¹)) +
      twoRowWeightD q 8 4 * ((9 * q - 5 * q⁻¹) - 14 * (q - q⁻¹)) = zDBar q) := by
  have h2q : q + q⁻¹ ≠ 0 := q_add_inv_ne_zero q hq hq21
  have hsw8 := h8_quantum_schur_weyl_decomp q q⁻¹ (mul_inv_cancel₀ hq)
  have hsw6 := (h5_h6_quantum_schur_weyl_decomp q q⁻¹ (mul_inv_cancel₀ hq)).2
  have hpos :
      twoRowWeightD q 8 0 * q +
        twoRowWeightD q 8 1 * (6 * q - q⁻¹) +
        twoRowWeightD q 8 2 * (15 * q - 5 * q⁻¹) +
        twoRowWeightD q 8 3 * (19 * q - 9 * q⁻¹) +
        twoRowWeightD q 8 4 * (9 * q - 5 * q⁻¹) = zD q := by
    unfold twoRowWeightD zD
    simp only [Nat.reduceMul, Nat.reduceSub, Nat.reduceAdd]
    have hnum :
        qIntSum q q⁻¹ 9 * q + qIntSum q q⁻¹ 7 * (6 * q - q⁻¹) +
          qIntSum q q⁻¹ 5 * (15 * q - 5 * q⁻¹) + qIntSum q q⁻¹ 3 * (19 * q - 9 * q⁻¹) +
          qIntSum q q⁻¹ 1 * (9 * q - 5 * q⁻¹) =
        q * (1 * qIntSum q q⁻¹ 9 + 7 * qIntSum q q⁻¹ 7 + 20 * qIntSum q q⁻¹ 5 +
          28 * qIntSum q q⁻¹ 3 + 14 * qIntSum q q⁻¹ 1) -
        (q + q⁻¹) * (1 * qIntSum q q⁻¹ 7 + 5 * qIntSum q q⁻¹ 5 + 9 * qIntSum q q⁻¹ 3 +
          5 * qIntSum q q⁻¹ 1) := by ring
    calc
      qIntSum q q⁻¹ 9 / (q + q⁻¹) ^ 8 * q +
          qIntSum q q⁻¹ 7 / (q + q⁻¹) ^ 8 * (6 * q - q⁻¹) +
          qIntSum q q⁻¹ 5 / (q + q⁻¹) ^ 8 * (15 * q - 5 * q⁻¹) +
          qIntSum q q⁻¹ 3 / (q + q⁻¹) ^ 8 * (19 * q - 9 * q⁻¹) +
          qIntSum q q⁻¹ 1 / (q + q⁻¹) ^ 8 * (9 * q - 5 * q⁻¹)
        = (qIntSum q q⁻¹ 9 * q + qIntSum q q⁻¹ 7 * (6 * q - q⁻¹) +
            qIntSum q q⁻¹ 5 * (15 * q - 5 * q⁻¹) + qIntSum q q⁻¹ 3 * (19 * q - 9 * q⁻¹) +
            qIntSum q q⁻¹ 1 * (9 * q - 5 * q⁻¹)) / (q + q⁻¹) ^ 8 := by ring
      _ = (q * (q + q⁻¹) ^ 8 - (q + q⁻¹) * (q + q⁻¹) ^ 6) / (q + q⁻¹) ^ 8 := by
            rw [hnum, hsw8, hsw6]
      _ = q ^ 3 / (q ^ 2 + 1) := by
            field_simp
            ring
  refine ⟨hpos, ?_⟩
  have h1 := h8_twoRowWeightD_sum_eq_one q hq hq21
  have hdiff := (zD_bar_and_skein_diff q hq hq21).2
  linear_combination hpos - (q - q⁻¹) * h1 + hdiff

end TwoRowWedderburnAccounting

/-! ## Section 2: Extending `WeightedTraceSide` to `H₇(q), H₈(q)` & Cross-Nucleon Pair Identities -/

section WeightedTraceExtension

variable {F : Type*} [Field F]

/-- Closing one right spectator strand of `Ř` (`H₇(q)` layout `L7e`) and normalizing by the
unlinked spectator weight `[2]_q = q + q⁻¹` yields the exact Convention-D scalar `z_D(q)`. -/
theorem rightTrace_R_norm_eq_zD (q : F) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0) (x x' : Fin 2) :
    rightTrace (Kw q) (R q) x x' / (q + q⁻¹) = if x = x' then zD q else 0 := by
  have h2q : q + q⁻¹ ≠ 0 := q_add_inv_ne_zero q hq hq21
  rw [rightTrace_R q hq]
  split_ifs
  · unfold zD; field_simp
  · simp

/-- Closing one right spectator strand of `Ř⁻¹` (`H₇(q)` layout `L7e`) and normalizing by `q + q⁻¹`
yields the exact inverse-crossing scalar `z̄_D(q) = 1 / (q (q² + 1))`. -/
theorem rightTrace_Rinv_norm_eq_zDBar (q : F) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (x x' : Fin 2) :
    rightTrace (Kw q) (Rinv q) x x' / (q + q⁻¹) = if x = x' then zDBar q else 0 := by
  have h2q : q + q⁻¹ ≠ 0 := q_add_inv_ne_zero q hq hq21
  rw [rightTrace_Rinv q hq]
  split_ifs
  · unfold zDBar; field_simp
  · simp

/-- Two-step right-spectator closure (`H₈(q)` layout `L8e`, closing strand 7 into strand 6 via `Y₂`
and strand 6 into strand 5 via `Y₁` with weight `K ⊗ K`). -/
def rightTrace2 (w : Fin 2 → F)
    (Y₁ Y₂ : Fin 2 → Fin 2 → Fin 2 → Fin 2 → F) (x x' : Fin 2) : F :=
  ∑ y, ∑ y', w y * Y₁ x y x' y' * rightTrace w Y₂ y y'

/-- **Two-Step Right Stabilization on `H₈(q)` (`Ř₅ Ř₆`):**
Normalized by `(q + q⁻¹)²`, closing two right spectators through `Ř₅ Ř₆` leaves the scalar
`z_D(q)²` on strand 5. -/
theorem rightTrace2_R_norm_eq_zD_sq (q : F) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (x x' : Fin 2) :
    rightTrace2 (Kw q) (R q) (R q) x x' / (q + q⁻¹) ^ 2 =
      if x = x' then (zD q) ^ 2 else 0 := by
  have h2q : q + q⁻¹ ≠ 0 := q_add_inv_ne_zero q hq hq21
  unfold rightTrace2
  simp only [rightTrace_R q hq, mul_ite, mul_zero, Finset.sum_ite_eq, Finset.mem_univ, ↓reduceIte]
  have hinner : ∑ y, Kw q y * R q x y x' y * q ^ 2 = rightTrace (Kw q) (R q) x x' * q ^ 2 := by
    unfold rightTrace; rw [Finset.sum_mul]
  rw [hinner, rightTrace_R q hq]
  split_ifs
  · unfold zD; field_simp
  · simp

/-- **Mixed Two-Step Right Stabilization on `H₈(q)` (`Ř₅ Ř₆⁻¹`):**
Normalized by `(q + q⁻¹)²`, closing two right spectators through `Ř₅ Ř₆⁻¹` leaves the bar-even
scalar `z_D(q) · z̄_D(q) = q² / (q² + 1)²` on strand 5. -/
theorem rightTrace2_R_Rinv_norm_eq_zD_mul_zDBar (q : F) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (x x' : Fin 2) :
    (rightTrace2 (Kw q) (R q) (Rinv q) x x' / (q + q⁻¹) ^ 2 =
      if x = x' then zD q * zDBar q else 0) ∧
    zD q * zDBar q = q ^ 2 / (q ^ 2 + 1) ^ 2 := by
  have h2q : q + q⁻¹ ≠ 0 := q_add_inv_ne_zero q hq hq21
  refine ⟨?_, ?_⟩
  · unfold rightTrace2
    simp only [rightTrace_Rinv q hq, mul_ite, mul_zero, Finset.sum_ite_eq, Finset.mem_univ,
      ↓reduceIte]
    have hinner :
        ∑ y, Kw q y * R q x y x' y * (q⁻¹) ^ 2 = rightTrace (Kw q) (R q) x x' * (q⁻¹) ^ 2 := by
      unfold rightTrace; rw [Finset.sum_mul]
    rw [hinner, rightTrace_R q hq]
    split_ifs
    · unfold zD zDBar; field_simp
    · simp
  · unfold zD zDBar; field_simp

/-- Iterated left-spectator partial-trace operator `L_m(q)` induced on the leading strand of block
`B` after tracing out a chain of `m` left spectator crossings (`m = 1` for `H₇(q)` `L7s`, `m = 2`
for `H₈(q)` `L8s`). -/
def leftChainOp (q : F) : ℕ → Fin 2 → Fin 2 → F
  | 0, x, x' => if x = x' then 1 else 0
  | m + 1, x, x' => leftTrace (fun y => Kw q y * leftChainOp q m y y) (R q) x x'

/-- **Exact Closed Form of `m + 1` Left Spectator Crossings (`H₇, H₈`, and All `N = 6 + m + 1`):**
Over any field `F` with `q ≠ 0`, tracing out `m + 1` left spectators leaves on the first strand of
the target block the exact diagonal weight-counting operator
`diag(1 + (q² + 1)(q^{2m} - q⁻²), 1)`. -/
theorem leftChainOp_succ_closed_form (q : F) (hq : q ≠ 0) (m : ℕ) (x x' : Fin 2) :
    leftChainOp q (m + 1) x x' =
      if x = x' then
        (if x = 0 then 1 + (q ^ 2 + 1) * (q ^ (2 * m) - (q⁻¹) ^ 2) else 1)
      else 0 := by
  induction m generalizing x x' with
  | zero =>
    rw [leftChainOp]
    simp only [leftChainOp, ↓reduceIte, mul_one]
    rw [leftTrace_R q hq]
    fin_cases x <;> fin_cases x'
    · simp; field_simp; ring
    · simp
    · simp
    · simp
  | succ m ih =>
    rw [leftChainOp]
    have hdiag0 : leftChainOp q (m + 1) 0 0 = 1 + (q ^ 2 + 1) * (q ^ (2 * m) - (q⁻¹) ^ 2) := by
      rw [ih]; simp
    have hdiag1 : leftChainOp q (m + 1) 1 1 = 1 := by
      rw [ih]; simp
    fin_cases x <;> fin_cases x' <;>
      simp [leftTrace, Fin.sum_univ_two, hdiag0, hdiag1, Kw, R]
    · have hexp : q ^ (2 * (m + 1)) = q ^ (2 * m) * q ^ 2 := by ring
      rw [hexp]
      field_simp
      ring
    · field_simp

/-- **`H₈`–`H₇` Left-Spectator Operator Collapse (`L₂(q) = (q² + 1) L₁(q) - q² I₂`):**
Adding a second spectator between the blocks (`H₈(q)` layout `L8s` vs `H₇(q)` layout `L7s`)
introduces no new operator direction: `leftChainOp q 2` is an exact `(q² + 1, -q²)` linear
combination of `leftChainOp q 1` and the identity `leftChainOp q 0`. -/
theorem leftChainOp_two_linear_comb (q : F) (hq : q ≠ 0) (x x' : Fin 2) :
    leftChainOp q 2 x x' =
      (q ^ 2 + 1) * leftChainOp q 1 x x' - q ^ 2 * leftChainOp q 0 x x' := by
  rw [leftChainOp_succ_closed_form q hq 1, leftChainOp_succ_closed_form q hq 0]
  unfold leftChainOp
  fin_cases x <;> fin_cases x'
  · simp; field_simp; ring
  · simp
  · simp
  · simp

/-- **Non-Scalarity of the `m + 1` Left-Spectator Operator (`H₇, H₈`, General `m`):**
Whenever `q ≠ 0`, `q² + 1 ≠ 0`, and `(q²)^{m+1} ≠ 1`, the left-closed spectator chain is strictly
non-scalar (`L_{m+1}(0,0) ≠ L_{m+1}(1,1)`), inserting a genuine weight-counting projector on the
receiving block. -/
theorem leftChainOp_succ_not_scalar (q : F) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0) (m : ℕ)
    (hpow : (q ^ 2) ^ (m + 1) ≠ 1) :
    leftChainOp q (m + 1) 0 0 ≠ leftChainOp q (m + 1) 1 1 := by
  have h00 : leftChainOp q (m + 1) 0 0 = 1 + (q ^ 2 + 1) * (q ^ (2 * m) - (q⁻¹) ^ 2) := by
    rw [leftChainOp_succ_closed_form q hq m]; simp
  have h11 : leftChainOp q (m + 1) 1 1 = 1 := by
    rw [leftChainOp_succ_closed_form q hq m]; simp
  rw [h00, h11]
  intro h
  have hprod : (q ^ 2 + 1) * (q ^ (2 * m) - (q⁻¹) ^ 2) = 0 := by linear_combination h
  rcases mul_eq_zero.mp hprod with h1 | h2
  · exact hq21 h1
  · apply hpow
    have hdiff : q ^ (2 * m) = (q⁻¹) ^ 2 := sub_eq_zero.mp h2
    have hmul : q ^ (2 * m) * q ^ 2 = (q⁻¹) ^ 2 * q ^ 2 := congrArg (· * q ^ 2) hdiff
    have hinv : (q⁻¹) ^ 2 * q ^ 2 = 1 := by field_simp
    have hexp : (q ^ 2) ^ (m + 1) = q ^ (2 * m) * q ^ 2 := by ring
    rw [hexp, hmul, hinv]

/-- Full `K`-trace consistency: closing the target strand of `leftChainOp q m` with `Kw q` gives
`(q + q⁻¹) * (q²)^m`, agreeing identically with right-closing all `m` crossings. -/
theorem full_trace_leftChainOp_eq_right (q : F) (hq : q ≠ 0) (m : ℕ) :
    (∑ x, Kw q x * leftChainOp q m x x) = (q + q⁻¹) * (q ^ 2) ^ m := by
  cases m with
  | zero =>
    simp [leftChainOp, Fin.sum_univ_two, Kw]
  | succ k =>
    have h00 : leftChainOp q (k + 1) 0 0 = 1 + (q ^ 2 + 1) * (q ^ (2 * k) - (q⁻¹) ^ 2) := by
      rw [leftChainOp_succ_closed_form q hq k]; simp
    have h11 : leftChainOp q (k + 1) 1 1 = 1 := by
      rw [leftChainOp_succ_closed_form q hq k]; simp
    rw [Fin.sum_univ_two, h00, h11]
    simp only [Kw, Matrix.cons_val_zero, Matrix.cons_val_one, mul_one]
    have hexp : (q ^ 2) ^ (k + 1) = q ^ (2 * k) * q ^ 2 := by ring
    rw [hexp]
    field_simp
    ring

/-- Numerator of the all-`q` six-strand/pinned cross-nucleon pair parameter `α₆(q)`. -/
def alphaSixNum (q : F) : F :=
  q ^ 2 * (q ^ 12 - 3 * q ^ 10 + q ^ 8 - 5 * q ^ 6 + 3 * q ^ 4 - 2 * q ^ 2 + 1)

/-- Palindromic degree-14 denominator of `α₆(q)`. -/
def alphaSixDen (q : F) : F :=
  q ^ 14 - 2 * q ^ 12 - q ^ 10 - 2 * q ^ 8 - 2 * q ^ 6 - q ^ 4 - 2 * q ^ 2 + 1

/-- Exact rational pair-term parameter `α₆(q)` shared by `L6`, `L7e`, `L7s`, `L8e`, `L8s`. -/
def alphaSix (q : F) : F := alphaSixNum q / alphaSixDen q

/-- Companion bar-involuted pair-term parameter `β₆(q) = α₆(q⁻¹)`. -/
def betaSix (q : F) : F := alphaSix q⁻¹

/-- Palindromicity `q¹⁴ · P(q⁻¹) = P(q)` and factored `(q² + 1)` form of `alphaSixDen`. -/
theorem alphaSixDen_palindromic_and_factored (q : F) (hq : q ≠ 0) :
    q ^ 14 * alphaSixDen q⁻¹ = alphaSixDen q ∧
    alphaSixDen q =
      (q ^ 2 + 1) * (q ^ 12 - 3 * q ^ 10 + 2 * q ^ 8 - 4 * q ^ 6 + 2 * q ^ 4 - 3 * q ^ 2 + 1) := by
  unfold alphaSixDen
  constructor
  · field_simp; ring
  · ring

/-- **All-`q` Cross-Nucleon Pair Identity (`α₆(q) + β₆(q) = 1` & Classical Value `1/2`):**
Over any field `F` with `q ≠ 0` and `alphaSixDen q ≠ 0`, `α₆(q) + α₆(q⁻¹) = 1`; at `q = 1`
(for `char F ≠ 2`), `α₆(1) = 1/2 ≠ 0`. -/
theorem alphaSix_add_betaSix (q : F) (hq : q ≠ 0) (hden : alphaSixDen q ≠ 0) :
    alphaSix q + betaSix q = 1 := by
  have hpal := (alphaSixDen_palindromic_and_factored q hq).1
  unfold betaSix alphaSix
  have hbeta :
      alphaSixNum q⁻¹ / alphaSixDen q⁻¹ = (q ^ 14 * alphaSixNum q⁻¹) / alphaSixDen q := by
    rw [← hpal, mul_div_mul_left _ _ (pow_ne_zero 14 hq)]
  rw [hbeta, ← add_div]
  have hsum : alphaSixNum q + q ^ 14 * alphaSixNum q⁻¹ = alphaSixDen q := by
    unfold alphaSixNum alphaSixDen
    field_simp
    ring
  rw [hsum, div_self hden]

theorem alphaSix_at_one (h2 : (2 : F) ≠ 0) : alphaSix (1 : F) = 1 / 2 := by
  have h8 : (8 : F) ≠ 0 := by
    rw [show (8 : F) = 2 * (2 * 2) by norm_num]
    exact mul_ne_zero h2 (mul_ne_zero h2 h2)
  have hn8 : (-8 : F) ≠ 0 := neg_ne_zero.mpr h8
  unfold alphaSix alphaSixNum alphaSixDen
  norm_num
  field_simp
  ring

/-- **All-`q` Exclusion of Pure Coulomb on `H₇(q)` and `H₈(q)` (`L7e, L7s, L8e, L8s`):**
In any bar-closed reachable pair-shift span (`σ : F ≃+* F` involutive) whose `Q_B`-centre `α` is
pinned to `α₆(q)`, no pure Coulomb pair term `c + κ Q_A Q_B` (`α = 0`, `κ ≠ 0`) is reachable. -/
theorem h7_h8_pinned_alphaSix_not_coulomb (Reach : Set (F → F → F)) (σ : F ≃+* F)
    (hσ : ∀ x, σ (σ x) = x)
    (hbar : ∀ f ∈ Reach, (fun x y => σ (f (1 - σ x) (1 - σ y))) ∈ Reach) (q : F)
    (hpin : ∀ c κ α β, κ ≠ 0 → pairTerm c κ α β ∈ Reach → α = alphaSix q)
    (c κ β : F) (hκ : κ ≠ 0) :
    pairTerm c κ 0 β ∉ Reach :=
  not_coulomb_of_pinned_alpha Reach σ hσ hbar (alphaSix q) hpin c κ β hκ

/-- **Cross-Cluster Skein Dressing Isovector Split & Zero Coulomb Curvature (`qou-vudb`):**
For two Borromean nucleon cores `C_A, C_B` (each with Convention-D trace `t_Bor`) joined across any
spectator factor `μ_spec` on `H₆(q), H₇(q), H₈(q)` by `pp` (`σ ↦ z_D`), `nn` (`σ⁻¹ ↦ z̄_D`), and
symmetric `pn` (`(σ + σ⁻¹)/2 ↦ (z_D + z̄_D)/2`), the `pp - nn` split is `(q - q⁻¹) μ_spec t_Bor²`
(vanishing at `q = 1`), while the Coulomb `Q_A Q_B` curvature `T_pp - 2 T_pn + T_nn` is identically
zero. -/
theorem crossCluster_skein_isovector_and_zero_coulomb (q μSpec tBor : F) (hq : q ≠ 0)
    (hq21 : q ^ 2 + 1 ≠ 0) (h2 : (2 : F) ≠ 0) :
    let Tpp := zD q * μSpec * tBor ^ 2
    let Tnn := zDBar q * μSpec * tBor ^ 2
    let Tpn := ((zD q + zDBar q) / 2) * μSpec * tBor ^ 2
    Tpp - Tnn = (q - q⁻¹) * μSpec * tBor ^ 2 ∧
    Tpp - 2 * Tpn + Tnn = 0 := by
  dsimp only
  have hdiff := (zD_bar_and_skein_diff q hq hq21).2
  refine ⟨?_, ?_⟩
  · calc
      zD q * μSpec * tBor ^ 2 - zDBar q * μSpec * tBor ^ 2
        = (zD q - zDBar q) * μSpec * tBor ^ 2 := by ring
      _ = (q - q⁻¹) * μSpec * tBor ^ 2 := by rw [hdiff]
  · field_simp
    ring

end WeightedTraceExtension

/-! ## Section 3: Coideal / Split-Bundle `F = V₂ ⊕ W₃*` Killing-Norm Hypercharge Slope `1/2` -/

section SplitBundleHyperchargeSlope

variable {K : Type*} [Field K] [CharZero K]

/-- Weak-isospin Cartan generator `T₃ = diag(+1/2, -1/2, 0, 0, 0)` on the 5-dimensional split
bundle `F = V₂ ⊕ W₃*`. -/
def splitT3 : Fin 5 → K := ![1 / 2, -1 / 2, 0, 0, 0]

/-- `SU(2) × SU(3)`-centralizer hypercharge generator `Y = diag(y₂, y₂, y₃, y₃, y₃)` on
`F = V₂ ⊕ W₃*`. -/
def splitY (y2 y3 : K) : Fin 5 → K := ![y2, y2, y3, y3, y3]

/-- Candidate electric charge `Q = T₃ + α_Y · Y` on `F = V₂ ⊕ W₃*`. -/
def splitQ (αY y2 y3 : K) (i : Fin 5) : K := splitT3 i + αY * splitY y2 y3 i

/-- **Weak-Isospin Traces on `F = V₂ ⊕ W₃*`:**
`Tr_F(T₃) = 0`, `Tr_F(T₃²) = 1/2`, and `Tr_F((2 T₃)²) = 2`. -/
theorem splitT3_traces :
    (∑ i : Fin 5, splitT3 (K := K) i = 0) ∧
    (∑ i : Fin 5, (splitT3 (K := K) i) ^ 2 = 1 / 2) ∧
    (∑ i : Fin 5, (2 * splitT3 (K := K) i) ^ 2 = 2) := by
  refine ⟨?_, ?_, ?_⟩ <;> (simp [Fin.sum_univ_five, splitT3]; try norm_num)

/-- **Exact Killing Orthogonality (`Tr_F(T₃ Y) = 0`):** -/
theorem splitT3_orthogonal_splitY (y2 y3 : K) :
    ∑ i : Fin 5, splitT3 i * splitY y2 y3 i = 0 := by
  simp [Fin.sum_univ_five, splitT3, splitY]
  ring

/-- **Traceless `su(5)` Hypercharge Ratio (`Tr_F(Y) = 0 ↔ y₃ = -(2/3) y₂`):** -/
theorem traceless_splitY_iff (y2 y3 : K) :
    (∑ i : Fin 5, splitY y2 y3 i = 0) ↔ y3 = -(2 / 3) * y2 := by
  have hsum_eq : (∑ i : Fin 5, splitY y2 y3 i) = 2 * y2 + 3 * y3 := by
    simp [Fin.sum_univ_five, splitY]
    ring
  rw [hsum_eq]
  constructor
  · intro h
    linear_combination h / 3
  · intro h
    rw [h]
    ring

/-- **Hypercharge Killing Norm `Tr_F((Y/2)²) = 5/6` on `F = V₂ ⊕ W₃*`:**
At the standard weak-doublet unit `y₂ = -1` (`y₃ = 2/3`), `Tr_F((Y/2)²) = 5/6` and
`Tr_F(Y²) = 10/3`. -/
theorem splitY_half_sq_trace :
    (∑ i : Fin 5, (splitY (-1 : K) (2 / 3) i / 2) ^ 2 = 5 / 6) ∧
    (∑ i : Fin 5, (splitY (-1 : K) (2 / 3) i) ^ 2 = 10 / 3) := by
  constructor <;> (simp [Fin.sum_univ_five, splitY]; norm_num)

/-- **Full Chiral SM Generation (`5̄ ⊕ 10`, 15 Weyl States) Killing Traces & `sin²θ_W⁰ = 3/8` (`qou-fbrp`):**
Across one complete chiral generation (`6` `Q_L`, `3` `u_R^c`, `3` `d_R^c`, `2` `L_L`, `1` `e_R^c`),
`Tr_G(T₃²) = 2` and `Tr_G((Y/2)²) = 10/3 = 4 · (5/6)`, giving the exact unrenormalized Weinberg
mixing ratio `3/8` on both `F = V₂ ⊕ W₃*` and `G = 5̄ ⊕ 10`. -/
theorem weinberg_trace_ratio_three_eighths :
    let trF_T3Sq : K := ∑ i : Fin 5, (splitT3 (K := K) i) ^ 2
    let trF_HalfYSq : K := ∑ i : Fin 5, (splitY (-1 : K) (2 / 3) i / 2) ^ 2
    let trG_T3Sq : K := 6 * (1 / 2) ^ 2 + 2 * (1 / 2) ^ 2
    let trG_HalfYSq : K :=
      6 * ((1 / 3 : K) / 2) ^ 2 + 3 * ((-4 / 3 : K) / 2) ^ 2 + 3 * ((2 / 3 : K) / 2) ^ 2 +
        2 * ((-1 : K) / 2) ^ 2 + 1 * ((2 : K) / 2) ^ 2
    trG_T3Sq = 2 ∧
    trG_HalfYSq = 10 / 3 ∧
    trG_HalfYSq = 4 * trF_HalfYSq ∧
    trF_T3Sq / (trF_T3Sq + trF_HalfYSq) = 3 / 8 ∧
    trG_T3Sq / (trG_T3Sq + trG_HalfYSq) = 3 / 8 := by
  dsimp only
  rw [splitT3_traces.2.1, splitY_half_sq_trace.1]
  refine ⟨?_, ?_, ?_, ?_, ?_⟩ <;> norm_num

/-- **Unconditional GMN Slope `α_Y = 1/2` from Coideal Highest-Weight Neutrality (`qou-20sx`):**
On `F = V₂ ⊕ W₃*` at `y₂ = -1`, tracelessness `Tr_F(Y) = 0` together with neutrality of the upper
weak-doublet ray `Q(ν_L) = splitQ α_Y (-1) y₃ 0 = 0` holds **iff** `α_Y = 1/2` and `y₃ = 2/3`. -/
theorem gmn_slope_half_iff (αY y3 : K) :
    (∑ i : Fin 5, splitY (-1 : K) y3 i = 0) ∧ splitQ αY (-1) y3 0 = 0 ↔
      αY = 1 / 2 ∧ y3 = 2 / 3 := by
  rw [traceless_splitY_iff (-1) y3]
  unfold splitQ splitT3 splitY
  simp only [Matrix.cons_val_zero]
  constructor
  · rintro ⟨hy3, hQ⟩
    exact ⟨by linear_combination -hQ, by linear_combination hy3⟩
  · rintro ⟨rfl, rfl⟩
    constructor <;> norm_num

/-- **GMN Slope `α_Y = ±1/2` from Killing-Norm Closure `Tr_F(Q²) = 4/3`:**
By Killing orthogonality `Tr_F(T₃ Y) = 0`, `Tr_F(Q²) = 1/2 + (10/3) α_Y²`, so `Tr_F(Q²) = 4/3`
(matching `Tr_F(T₃²) / Tr_F(Q²) = 3/8`) forces `α_Y² = 1/4` (`α_Y = ±1/2`), and `Q(ν_L) = 0`
selects `α_Y = 1/2` uniquely. -/
theorem gmn_slope_half_from_killing_norm (αY : K) :
    (∑ i : Fin 5, (splitQ αY (-1 : K) (2 / 3) i) ^ 2 = 4 / 3 ↔ αY = 1 / 2 ∨ αY = -1 / 2) ∧
    ((∑ i : Fin 5, (splitQ αY (-1 : K) (2 / 3) i) ^ 2 = 4 / 3 ∧
        splitQ αY (-1) (2 / 3) 0 = 0) ↔ αY = 1 / 2) := by
  have hquad :
      ∑ i : Fin 5, (splitQ αY (-1 : K) (2 / 3) i) ^ 2 = 1 / 2 + (10 / 3) * αY ^ 2 := by
    simp [Fin.sum_univ_five, splitQ, splitT3, splitY]
    ring
  rw [hquad]
  have hiff : (1 / 2 : K) + (10 / 3) * αY ^ 2 = 4 / 3 ↔ αY = 1 / 2 ∨ αY = -1 / 2 := by
    constructor
    · intro h
      have hfac : (αY - 1 / 2) * (αY + 1 / 2) = 0 := by
        linear_combination (3 / 10 : K) * h
      rcases mul_eq_zero.mp hfac with hminus | hplus
      · left; exact sub_eq_zero.mp hminus
      · right; linear_combination hplus
    · rintro (rfl | rfl) <;> norm_num
  refine ⟨hiff, ?_⟩
  rw [hiff]
  unfold splitQ splitT3 splitY
  simp only [Matrix.cons_val_zero]
  constructor
  · rintro ⟨_, h0⟩
    linear_combination -h0
  · rintro rfl
    exact ⟨Or.inl rfl, by norm_num⟩

/-- **Derived Quark Charges `(2/3, -1/3)`, Nucleon Charges `(1, 0)`, and Chiral Anomaly Cancellation:**
Exterior-square primitive coproduct `Y(Q_L) = (-y₂) + (-y₃) = 1 - 2/3 = 1/3` together with the
derived slope `α_Y = 1/2` pins `c = α_Y Y(Q_L) = 1/6` in `QuarkChargeReduction` (over `[CharZero K]`),
deriving `(q_u, q_d) = (2/3, -1/3)`, `(Q_p, Q_n) = (1, 0)`, and exact cancellation of gravitational
`Tr_G(Y)`, mixed `SU(2)² U(1)_Y`, and cubic `Tr_G(Y³)` anomalies. -/
theorem chiral_generation_anomaly_cancellation :
    let y2 : K := -1
    let y3 : K := 2 / 3
    let αY : K := 1 / 2
    let yQL : K := (-y2) + (-y3)
    let c : K := αY * yQL
    yQL = 1 / 3 ∧
    c = 1 / 6 ∧
    qu c = 2 / 3 ∧
    qd c = -1 / 3 ∧
    2 * qu c + qd c = 1 ∧
    qu c + 2 * qd c = 0 ∧
    (6 * yQL + 3 * (-2 * y3) + 3 * y3 + 2 * y2 + 1 * (-2 * y2) = 0) ∧
    (3 * yQL + 1 * y2 = 0) ∧
    (6 * yQL ^ 3 + 3 * (-2 * y3) ^ 3 + 3 * y3 ^ 3 + 2 * y2 ^ 3 + 1 * (-2 * y2) ^ 3 = 0) := by
  dsimp only
  have hc : (1 / 2 : K) * (-(-1) + -(2 / 3)) = 1 / 6 := by ring
  obtain ⟨hqu, hqd⟩ := charges_of_c ((1 / 2 : K) * (-(-1) + -(2 / 3))) hc
  refine ⟨by ring, hc, hqu, hqd, ?_, ?_, by ring, by ring, by ring⟩
  · rw [hqu, hqd]; ring
  · rw [hqu, hqd]; ring

end SplitBundleHyperchargeSlope

/-! ## Section 4: Separated-Hadron `Z`-Channel Removal (`CoulombNeedsZRemoval` Bridge & `< 10⁻²⁸⁰` Yukawa Suppression) -/

section ZChannelRemovalAlgebraic

variable {K : Type*} [Field K]

/-- In the unbroken `λ = 1` limit (`r → 0`), `CoulombNeedsZRemoval.exch` reduces to the Weyl-even
exchange `g² T T' + g'² / 4` and equates `pp = nn` (`(g² + g'²)/4`), exhibiting zero Coulomb
asymmetry between proton pairs and neutron pairs. -/
theorem exch_at_one_pp_eq_nn (g2 gp2 T T' : K) (hs : g2 + gp2 ≠ 0) (h2 : (2 : K) ≠ 0) :
    exch g2 gp2 1 T T' = g2 * T * T' + gp2 * (1 / 2) * (1 / 2) ∧
    exch g2 gp2 1 (1 / 2) (1 / 2) = exch g2 gp2 1 (-1 / 2) (-1 / 2) := by
  unfold exch QOU.QBeta.CoulombNeedsZRemoval.q
  constructor <;> (field_simp; ring)

/-- **Exact Closed-Form `Z`-Contamination Residuals on `(pp, pn, np, nn)`:**
For any surviving `Z`-fraction `lam`, the deviations of `exch g2 gp2 lam` from pure `e² Q Q'`
Coulomb (`(e², 0, 0, 0)`) are exact linear multiples of `lam`. -/
theorem exch_residuals_exact (g2 gp2 lam : K) (hs : g2 + gp2 ≠ 0) (h2 : (2 : K) ≠ 0) :
    let e2 := g2 * gp2 / (g2 + gp2)
    exch g2 gp2 lam (-1 / 2) (-1 / 2) = lam * (g2 + gp2) / 4 ∧
    exch g2 gp2 lam (1 / 2) (-1 / 2) = -lam * (g2 - gp2) / 4 ∧
    exch g2 gp2 lam (-1 / 2) (1 / 2) = -lam * (g2 - gp2) / 4 ∧
    exch g2 gp2 lam (1 / 2) (1 / 2) - e2 = lam * (g2 - gp2) ^ 2 / (4 * (g2 + gp2)) := by
  dsimp only
  have h4 : (4 : K) ≠ 0 := by rw [show (4 : K) = 2 * 2 by norm_num]; exact mul_ne_zero h2 h2
  unfold exch QOU.QBeta.CoulombNeedsZRemoval.q
  refine ⟨?_, ?_, ?_, ?_⟩ <;> (field_simp; ring)

/-- **Neutral Exchange at Unrenormalized `SU(5)` Mixing `g'² = (3/5) g²` (`sin²θ_W⁰ = 3/8`):**
At `g'² = (3/5) g²`, `(pp, pn, np, nn) = ((3/8) g² + (1/40) λ g², -(1/10) λ g², -(1/10) λ g², (2/5) λ g²)`,
collapsing at `λ = 0` to pure `e² = (3/8) g²` Coulomb (`1 : 0 : 0`). -/
theorem exch_at_weinberg_three_eighths [CharZero K] (g2 lam : K) (hg : g2 ≠ 0) :
    let gp2 := (3 / 5 : K) * g2
    exch g2 gp2 lam (1 / 2) (1 / 2) = (3 / 8) * g2 + (1 / 40) * lam * g2 ∧
    exch g2 gp2 lam (1 / 2) (-1 / 2) = -(1 / 10) * lam * g2 ∧
    exch g2 gp2 lam (-1 / 2) (-1 / 2) = (2 / 5) * lam * g2 ∧
    CoulombShape (exch g2 gp2 0) 0 ((3 / 8) * g2) := by
  dsimp only
  have hs : g2 + (3 / 5 : K) * g2 ≠ 0 := by
    have : g2 + (3 / 5 : K) * g2 = (8 / 5 : K) * g2 := by ring
    rw [this]
    exact mul_ne_zero (by norm_num) hg
  unfold CoulombShape exch QOU.QBeta.CoulombNeedsZRemoval.q
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> (field_simp; ring)

end ZChannelRemovalAlgebraic

section YukawaZDecouplingArchimedean

/-- Archimedean `ℝ` specialisation of `exch_residuals_exact` (prescribed `§7c` `_real` bridge). -/
theorem exch_residuals_exact_real (g2 gp2 lam : ℝ) (hs : g2 + gp2 ≠ 0) :
    let e2 := g2 * gp2 / (g2 + gp2)
    exch g2 gp2 lam (-1 / 2) (-1 / 2) = lam * (g2 + gp2) / 4 ∧
    exch g2 gp2 lam (1 / 2) (-1 / 2) = -lam * (g2 - gp2) / 4 ∧
    exch g2 gp2 lam (-1 / 2) (1 / 2) = -lam * (g2 - gp2) / 4 ∧
    exch g2 gp2 lam (1 / 2) (1 / 2) - e2 = lam * (g2 - gp2) ^ 2 / (4 * (g2 + gp2)) :=
  exch_residuals_exact (K := ℝ) g2 gp2 lam hs (by norm_num)

/-- Massive-`Z` Yukawa suppression factor `λ(x) = exp(-x)` at dimensionless Compton separation
`x = M_Z r / (ℏ c)`. -/
noncomputable def yukawaZ (x : ℝ) : ℝ := Real.exp (-x)

/-- Degree-4 Taylor lower bound `65 / 24 ≤ exp 1`. -/
theorem sixty_five_div_twenty_four_le_exp_one : (65 / 24 : ℝ) ≤ Real.exp 1 := by
  have h := Real.sum_le_exp_of_nonneg (by positivity : (0 : ℝ) ≤ 1) 5
  have hsum : (∑ i ∈ Finset.range 5, (1 : ℝ) ^ i / i.factorial) = 65 / 24 := by
    simp [Finset.sum_range_succ, Nat.factorial]
    norm_num
  linarith

/-- Elementary rational-power certificate `10²⁸² < exp 653` without numerical axioms. -/
theorem ten_pow_282_lt_exp_653 : (10 : ℝ) ^ (282 : ℕ) < Real.exp 653 := by
  have he1 : (65 / 24 : ℝ) ≤ Real.exp 1 := sixty_five_div_twenty_four_le_exp_one
  have h37 : (10 : ℝ) ^ (16 : ℕ) < (65 / 24 : ℝ) ^ (37 : ℕ) := by norm_num
  have h24 : (10 : ℝ) ^ (10 : ℕ) < (65 / 24 : ℝ) ^ (24 : ℕ) := by norm_num
  have h629 : ((10 : ℝ) ^ (16 : ℕ)) ^ (17 : ℕ) < ((65 / 24 : ℝ) ^ (37 : ℕ)) ^ (17 : ℕ) :=
    pow_lt_pow_left₀ h37 (by positivity) (by decide)
  have h282 : (10 : ℝ) ^ (282 : ℕ) < (65 / 24 : ℝ) ^ (653 : ℕ) := by
    calc
      (10 : ℝ) ^ (282 : ℕ) = ((10 : ℝ) ^ (16 : ℕ)) ^ (17 : ℕ) * (10 : ℝ) ^ (10 : ℕ) := by
            rw [← pow_mul, ← pow_add]
      _ < ((65 / 24 : ℝ) ^ (37 : ℕ)) ^ (17 : ℕ) * (65 / 24 : ℝ) ^ (24 : ℕ) :=
            mul_lt_mul'' h629 h24 (by positivity) (by positivity)
      _ = (65 / 24 : ℝ) ^ (653 : ℕ) := by
            rw [← pow_mul, ← pow_add]
  have hexp653 : (65 / 24 : ℝ) ^ (653 : ℕ) ≤ Real.exp 653 := by
    calc
      (65 / 24 : ℝ) ^ (653 : ℕ) ≤ (Real.exp 1) ^ (653 : ℕ) :=
            pow_le_pow_left₀ (by positivity) he1 653
      _ = Real.exp 653 := by
            rw [← Real.exp_nat_mul]
            norm_num
  exact lt_of_lt_of_le h282 hexp653

/-- **Exponential `Z`-Channel Suppression (`0 < λ(x) < 10⁻²⁸² < 10⁻²⁸⁰` for All `x ≥ 653`):**
Purely mathematical exponential decay bound for any dimensionless separation `x ≥ 653` (evaluated
against physical Compton separations strictly in the companion Python probe). -/
theorem yukawaZ_lt_ten_neg_282 {x : ℝ} (hx : 653 ≤ x) :
    0 < yukawaZ x ∧ yukawaZ x < (10 : ℝ) ^ (-282 : ℤ) ∧ yukawaZ x < (10 : ℝ) ^ (-280 : ℤ) := by
  unfold yukawaZ
  have hpos : 0 < Real.exp (-x) := Real.exp_pos (-x)
  have hgt : (10 : ℝ) ^ (282 : ℕ) < Real.exp x :=
    lt_of_lt_of_le ten_pow_282_lt_exp_653 (Real.exp_le_exp.mpr hx)
  have hlt282 : Real.exp (-x) < (10 : ℝ) ^ (-282 : ℤ) := by
    have hz : (10 : ℝ) ^ (-282 : ℤ) = ((10 : ℝ) ^ (282 : ℕ))⁻¹ := by
      rw [show (-282 : ℤ) = -(282 : ℕ) by rfl, zpow_neg, zpow_natCast]
    rw [Real.exp_neg, hz]
    exact inv_strictAnti₀ (by positivity) hgt
  have hp282 : 0 < (10 : ℝ) ^ (-282 : ℤ) := zpow_pos (by positivity) (-282)
  have h100_eq : (10 : ℝ) ^ (-280 : ℤ) = 100 * (10 : ℝ) ^ (-282 : ℤ) := by
    rw [show (-280 : ℤ) = -282 + 2 by norm_num, zpow_add₀ (by norm_num)]
    norm_num
    ring
  have h280 : (10 : ℝ) ^ (-282 : ℤ) < (10 : ℝ) ^ (-280 : ℤ) := by linarith
  exact ⟨hpos, hlt282, lt_trans hlt282 h280⟩

/-- **Separated-Hadron `> 280`-Digit Pure-Coulomb Isolation (`pp : pn : nn = 1 : 0 : 0`):**
For any electroweak couplings in the cone `(1/4) g² ≤ g'² ≤ g²` (containing the unrenormalized
`SU(5)` ratio `g'² = (3/5) g²`) and any dimensionless separation `x ≥ 653`, the photon coupling
`e² = g² g'² / (g² + g'²)` is strictly positive and all neutral-current `Z`-contamination terms in
`exch g2 gp2 (yukawaZ x)` are suppressed relative to `e²` below `10⁻²⁸⁰`:
`|(pp - e²)/e²| < 10⁻²⁸⁰`, `|pn/e²| < 10⁻²⁸⁰`, `|nn/e²| < 10⁻²⁸⁰`, and `|(pn - nn)/e²| < 10⁻²⁸⁰`. -/
theorem nuclear_z_channel_coulomb_isolation_280_digits {g2 gp2 x : ℝ}
    (hg : 0 < g2) (hlo : (1 / 4) * g2 ≤ gp2) (hhi : gp2 ≤ g2) (hx : 653 ≤ x) :
    let e2 := g2 * gp2 / (g2 + gp2)
    let lam := yukawaZ x
    0 < e2 ∧
    |exch g2 gp2 lam (1 / 2) (1 / 2) - e2| / e2 < (10 : ℝ) ^ (-280 : ℤ) ∧
    |exch g2 gp2 lam (1 / 2) (-1 / 2)| / e2 < (10 : ℝ) ^ (-280 : ℤ) ∧
    |exch g2 gp2 lam (-1 / 2) (-1 / 2)| / e2 < (10 : ℝ) ^ (-280 : ℤ) ∧
    |exch g2 gp2 lam (1 / 2) (-1 / 2) - exch g2 gp2 lam (-1 / 2) (-1 / 2)| / e2 <
      (10 : ℝ) ^ (-280 : ℤ) := by
  dsimp only
  have hgp : 0 < gp2 := by linarith
  have hs_pos : 0 < g2 + gp2 := by linarith
  have hs : g2 + gp2 ≠ 0 := hs_pos.ne'
  have h2 : (2 : ℝ) ≠ 0 := by norm_num
  set e2 : ℝ := g2 * gp2 / (g2 + gp2)
  have he2 : 0 < e2 := div_pos (mul_pos hg hgp) hs_pos
  obtain ⟨hlam_pos, hlam_lt, -⟩ := yukawaZ_lt_ten_neg_282 hx
  obtain ⟨hnn, hpn, -, hpp⟩ := exch_residuals_exact g2 gp2 (yukawaZ x) hs h2
  have hpnsub := QOU.QBeta.CoulombNeedsZRemoval.pn_sub_nn g2 gp2 (yukawaZ x) hs h2
  have he2_ge : g2 / 8 ≤ e2 := by
    unfold e2
    rw [le_div_iff₀ hs_pos]
    nlinarith
  have hsum_le : (g2 + gp2) / (4 * e2) ≤ 4 := by
    rw [div_le_iff₀ (by positivity)]
    nlinarith
  have hp282 : 0 < (10 : ℝ) ^ (-282 : ℤ) := zpow_pos (by positivity) (-282)
  have h100_eq : (10 : ℝ) ^ (-280 : ℤ) = 100 * (10 : ℝ) ^ (-282 : ℤ) := by
    rw [show (-280 : ℤ) = -282 + 2 by norm_num, zpow_add₀ (by norm_num)]
    norm_num
    ring
  have h100 : 4 * yukawaZ x < (10 : ℝ) ^ (-280 : ℤ) := by linarith
  have hdiff_nonneg : 0 ≤ g2 - gp2 := by linarith
  refine ⟨he2, ?_, ?_, ?_, ?_⟩
  · rw [hpp, abs_of_nonneg (by positivity)]
    have hle : yukawaZ x * (g2 - gp2) ^ 2 / (4 * (g2 + gp2)) / e2 ≤ 4 * yukawaZ x := by
      have hsq : (g2 - gp2) ^ 2 ≤ (g2 + gp2) ^ 2 := by nlinarith
      have hnum_le : yukawaZ x * (g2 - gp2) ^ 2 ≤ yukawaZ x * (g2 + gp2) ^ 2 :=
        mul_le_mul_of_nonneg_left hsq hlam_pos.le
      have hstep :
          yukawaZ x * (g2 - gp2) ^ 2 / (4 * (g2 + gp2)) ≤ yukawaZ x * (g2 + gp2) / 4 := by
        calc
          yukawaZ x * (g2 - gp2) ^ 2 / (4 * (g2 + gp2))
            ≤ yukawaZ x * (g2 + gp2) ^ 2 / (4 * (g2 + gp2)) :=
                div_le_div_of_nonneg_right hnum_le (by positivity)
          _ = yukawaZ x * (g2 + gp2) / 4 := by field_simp
      rw [div_le_iff₀ he2]
      calc
        yukawaZ x * (g2 - gp2) ^ 2 / (4 * (g2 + gp2))
          ≤ yukawaZ x * (g2 + gp2) / 4 := hstep
        _ = yukawaZ x * ((g2 + gp2) / (4 * e2)) * e2 := by field_simp
        _ ≤ yukawaZ x * 4 * e2 :=
              mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left hsum_le hlam_pos.le) he2.le
        _ = 4 * yukawaZ x * e2 := by ring
    exact lt_of_le_of_lt hle h100
  · rw [hpn, show -yukawaZ x * (g2 - gp2) / 4 = -(yukawaZ x * (g2 - gp2) / 4) by ring,
      abs_neg, abs_of_nonneg (by positivity)]
    have hle : yukawaZ x * (g2 - gp2) / 4 / e2 ≤ 4 * yukawaZ x := by
      rw [div_le_iff₀ he2]
      have h2' : yukawaZ x * (g2 - gp2) / 4 ≤ yukawaZ x * (g2 + gp2) / 4 := by nlinarith
      calc
        yukawaZ x * (g2 - gp2) / 4 ≤ yukawaZ x * (g2 + gp2) / 4 := h2'
        _ = yukawaZ x * ((g2 + gp2) / (4 * e2)) * e2 := by field_simp
        _ ≤ yukawaZ x * 4 * e2 :=
              mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left hsum_le hlam_pos.le) he2.le
        _ = 4 * yukawaZ x * e2 := by ring
    exact lt_of_le_of_lt hle h100
  · rw [hnn, abs_of_nonneg (by positivity)]
    have hle : yukawaZ x * (g2 + gp2) / 4 / e2 ≤ 4 * yukawaZ x := by
      rw [div_le_iff₀ he2]
      calc
        yukawaZ x * (g2 + gp2) / 4 = yukawaZ x * ((g2 + gp2) / (4 * e2)) * e2 := by field_simp
        _ ≤ yukawaZ x * 4 * e2 :=
              mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left hsum_le hlam_pos.le) he2.le
        _ = 4 * yukawaZ x * e2 := by ring
    exact lt_of_le_of_lt hle h100
  · rw [hpnsub, abs_neg, abs_of_nonneg (by positivity)]
    have hle : yukawaZ x * g2 / 2 / e2 ≤ 4 * yukawaZ x := by
      rw [div_le_iff₀ he2]
      nlinarith
    exact lt_of_le_of_lt hle h100

end YukawaZDecouplingArchimedean

end QOU.QBeta.CrossNucleonPairWedderburnZRemoval
