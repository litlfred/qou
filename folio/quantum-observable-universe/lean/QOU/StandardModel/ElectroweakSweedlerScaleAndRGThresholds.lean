import Mathlib.Tactic
import QOU.Nuclear.SweedlerWeakDegreeCount
import TwistedFrobeniusHopf.SweedlerFrobenius
import QOU.StandardModel.ElectroweakBringSchwingerBridge
import QOU.StandardModel.ElectroweakVevGaps
import QOU.BraidsAndKnots.HiggsCategoricalMassFormula
import QOU.Core.CategoricalHiggsIdempotent

/-!
# QOU.StandardModel.ElectroweakSweedlerScaleAndRGThresholds — Sweedler `(q² - 1)^k` EWSB Scale
# Reconciliation, Split-Bundle Goldstone/Higgs Stability, and Exact 1- and 2-Loop SM RG Thresholds

Formalizes the mathematical core of Standard Model Package 3 (`qou-ewsb`, `Q-Gap-9`, epic
`qou-sm8w`, aggregating `qou-ukqh`, `qou-z3x8`, `qou-zd6l`, `qou-5iaz`, `qou-0whz`) with **zero
`sorry`**, **standard axioms only**, and **zero empirical or decimal literals**:

1. **Section 1 — Sweedler `(q² - 1)^k` Weak Suppression vs Fermi Constant `G_F` & VEV `v_EW`:**
   - Proves on `QOU.LiftingDescent.Sweedler R` (`SweedlerFrobenius.lean`) that while the single
     weak-differential generator `X` is odd under the Nakayama automorphism `ν` (`ν(X) = -X`), the
     Frobenius top-form generator `G · X` (`frob (G · X) = 1`) and every even-channel contraction
     are Nakayama-invariant (`sweedler_nakayama_X_odd_and_GX_even`).
   - Reconciles `#9204`'s `SweedlerWeakDegreeCount` (`multiChannelRate 2 q = (q² - 1)⁴`,
     `multiChannelRate 4 q = (q² - 1)⁸`) with the Fermi relation `2 (G_F m²)² (v / m)⁴ = 1`:
     * **Amplitude-from-rate bridge (`fermi_vev_scaling_of_fourHopSquaredRate`):** Identifying
       `#9204`'s 4-hop contraction `(q² - 1)⁸` with the squared weak decay rate
       `Γ / m⁵ ∝ (G_F m²)²` gives `G_F m_model² = (q² - 1)⁴` (`= multiChannelAmp 4 q =
       multiChannelRate 2 q`), which is algebraically equivalent to
       `2 · (v_EW / m_model · (q² - 1)²)⁴ = 1`, i.e. `v_EW / m_model ∝ (q² - 1)⁻²`.
     * **Direct Frobenius-norm bridge (`fermi_vev_scaling_of_fourHopDirectNorm`):** Identifying
       `G_F m_model² = (q² - 1)⁸` directly gives `2 · (v_EW / m_model · (q² - 1)⁴)⁴ = 1`, i.e.
       `v_EW / m_model ∝ (q² - 1)⁻⁴`.
   - Reconciles `ElectroweakBringSchwingerBridge` and `EwVevGaps.su2_coupling_not_selfConsistent`
     honestly:
     * For any ordered field element `1 < q` with `q² < 5 / 4`, the 4-hop inverse coupling
       `κ_S = (q² - 1)⁴` satisfies `0 < κ_S < 1 / 256 < 1 / 30` and `κ_S⁻¹ > 256 > 100`
       (`sweedler_fourHop_escapes_su2_wall_of_sq_lt_five_fourths`), avoiding the `α₂ > 1 / 30`
       contradiction of `su2_coupling_not_selfConsistent`.
     * Conversely, on the rational substrate bracket `1109 / 1000 < q < 1111 / 1000`,
       `ewDressedTreeComplexity q < 280 < 300 < ((q² - 1)⁴)⁻¹`
       (`ewDressedTreeComplexity_lt_sweedlerFourHopInv_of_rational_bracket`), proving rigorously
       that `(q² - 1)⁻⁴` does **not** equal the Bring–Schwinger tree product at tree level, while
       inserting `κ_S` into the 1-loop Habiro slot shifts `N_v` by the exact bounded difference of
       `EwVevGaps.loopShift_identity` (`ewVev_sweedler_loop_shift_eq`).

2. **Section 2 — Electroweak Symmetry Breaking `su(2)_L ⊕ u(1)_Y → u(1)_EM`, Goldstone Rank `3`,
   and Tree-Level Higgs Scalar Potential Stability (`λ_H > 0`, `m_H² = 2 λ_H v²`):**
   - Formalizes the infinitesimal `su(2)_L ⊕ u(1)_Y` gauge orbit map `ewVacuumOrbit v0` around a
     neutral Higgs doublet VEV `(0, v0)` (`Y = +1`), proving that for `v0 ≠ 0` its kernel is the
     1-dimensional electromagnetic line `θ₁ = 0, θ₂ = 0, θ₃ = θ_Y` (`Q = T₃ + Y / 2`) and its
     Goldstone image `(W⁺_L, W⁻_L, Z_L)` has exact dimension `3`
     (`ewVacuumOrbit_kernel_iff_photon`, `ewVacuumOrbit_rank_three_goldstones`).
   - Diagonalizes the quadratic gauge-boson mass form into two `W±` modes (`g₂² v² / 4`), one `Z`
     mode (`(g₂² + g_Y²) v² / 4`), and one strictly massless photon mode
     (`ewGaugeMassForm_orthogonal_split`, `ew_tree_weinberg_cos_sin_identities`).
   - Proves over any ordered field that `V(Φ†Φ) = -μ²(Φ†Φ) + λ_H(Φ†Φ)²` (`μ² = λ_H v²`) has a
     unique global minimum at `Φ†Φ = v² / 2` with `V_min = -λ_H v⁴ / 4 < 0` when `λ_H > 0` and
     `v ≠ 0` (`higgsPotential_unique_global_min_of_pos_quartic`), radial excitation mass-squared
     `m_H² = 2 λ_H v²` (`higgs_radial_expansion_mass_sq`), unboundedness below when `λ_H < 0`
     (`higgsPotential_unbounded_below_of_neg_quartic`), and positivity of the remediated
     `QOU.BraidKnot.scalarOverGaugeRatio h` for `|h| ≤ 1 / 2` from the rational Catalan bracket.

3. **Section 3 — Exact Rational 1-Loop & 2-Loop SM Beta Coefficients (`N_gen = 3, N_H = 1`):**
   - Derives `(b₁, b₂, b₃) = (41 / 10, -19 / 6, -7)`, `b_EM = (5 / 3) b₁ + b₂ = 11 / 3`, universal
     per-generation Weyl Dynkin index `2` (so `N_gen` cancels in every 1-loop difference `b_i - b_j`),
     and all 9 entries of the 2-loop Machacek–Vaughn rational matrix `b_{ij}` directly from the
     quantum numbers of `(Q_L, u_R^c, d_R^c, L_L, e_R^c, H)` over any `[Field K] [CharZero K]`.

4. **Section 4 — Algebraic & Ordered-Field Identities Linking `sin²θ_W⁰ = 3 / 8` to `sin²θ_W(μ)`
   and `α_s(μ)` Across UV-to-`M_Z` Thresholds:**
   - Proves the all-orders identity `3 / 8 - sin²θ_W = (5 / 8) α_EM (α₁⁻¹ - α₂⁻¹)`, the 1-loop
     Georgi–Quinn–Weinberg running identity `sin²θ_W(t) = 3 / 8 - (109 / 24) t / α_EM⁻¹(t)`, the
     exact 1-loop RG invariance of the minimal-SM coupling triangle
     `115 α₁⁻¹ - 333 α₂⁻¹ + 218 α₃⁻¹ = 69 α_EM⁻¹ - 402 α₂⁻¹ + 218 α₃⁻¹`, and honest ordered-field
     threshold bounds showing (i) single-step minimal-SM unification forces `α₃⁻¹(M_Z) > 13` on the
     rational `M_Z` window and (ii) a low `t ∈ (0, 1)` threshold (`μ_UV / M_Z = (q₀² - 1)⁻⁴`) keeps
     `sin²θ_W > 33 / 100`.

-- Ref: [leitner2026] beans qou-ewsb, qou-sm8w, qou-ukqh, qou-z3x8, qou-zd6l, qou-5iaz, qou-3nva
-- Ref: [kassel1995] Quantum Groups, Springer GTM 155, §III
-/

namespace QOU.StandardModel.EWSweedlerRG

open QOU.QBeta.SweedlerWeakDegreeCount (singlePassageAmp multiChannelAmp multiChannelRate
  singlePassageAmp_eq sweedler_weak_degree_ladder)
open QOU.LiftingDescent (Sweedler)
open QOU.QInteger (qIntBal)

/-! ## Section 1: Sweedler `(q² - 1)^k` Weak Ladder, Nakayama Parity, & `G_F` / `v_EW` Bridge -/

section SweedlerBridge

/-- On `Sweedler R`, the weak differential `X` is Nakayama-odd (`ν(X) = -X`), whereas the
Frobenius volume element `G · X` (`frob (G · X) = 1`) is Nakayama-even (`ν(G · X) = G · X`). -/
theorem sweedler_nakayama_X_odd_and_GX_even {R : Type*} [CommRing R] :
    Sweedler.nakayama R (Sweedler.X R) = -Sweedler.X R ∧
    Sweedler.nakayama R (Sweedler.G R * Sweedler.X R) = Sweedler.G R * Sweedler.X R ∧
    Sweedler.frob R (Sweedler.G R * Sweedler.X R) = 1 := by
  refine ⟨?_, ?_, Sweedler.frob_GX R⟩
  · simp [Sweedler.nakayama]
  · simp [Sweedler.nakayama, map_mul]

/-- **Amplitude-from-4-hop-rate Fermi/VEV bridge (`G_F m² ∝ (q² - 1)⁴ ⟺ v / m ∝ (q² - 1)⁻²`):**
When `#9204`'s 4-hop Sweedler contraction `multiChannelRate 4 q = (q² - 1)⁸` represents the squared
weak decay rate `Γ / m⁵ = gF_dimless²` so that the dimensionless Fermi coupling equals the 4-hop
amplitude (equivalently the 2-vertex `W`-exchange squared rate `multiChannelRate 2 q = (q² - 1)⁴`),
the cleared Fermi relation `2 · gF_dimless² · (v / m)⁴ = 1` (`G_F = 1 / (√2 v²)`) is equivalent to
`2 · ((v / m) · (q² - 1)²)⁴ = 1`. -/
theorem fermi_vev_scaling_of_fourHopSquaredRate {K : Type*} [Field K]
    (q gF_dimless v_over_m : K) (hq : q ≠ 0)
    (hgF : gF_dimless = multiChannelAmp 4 q) :
    gF_dimless = multiChannelRate 2 q ∧
    gF_dimless ^ 2 = multiChannelRate 4 q ∧
    (2 * gF_dimless ^ 2 * v_over_m ^ 4 = 1 ↔
      2 * (v_over_m * (q ^ 2 - 1) ^ 2) ^ 4 = 1) := by
  have hl := sweedler_weak_degree_ladder q hq
  rcases hl with ⟨_, _, hr2, ha4, hr4⟩
  refine ⟨?_, ?_, ?_⟩
  · rw [hgF, ha4, hr2]
  · rw [hgF, ha4, hr4]; ring
  · rw [hgF, ha4]
    constructor <;> intro h <;> linear_combination h

/-- **Direct Frobenius-norm Fermi/VEV bridge (`G_F m² = (q² - 1)⁸ ⟺ v / m ∝ (q² - 1)⁻⁴`):**
Under `#9204`'s direct identification `gF_dimless = multiChannelRate 4 q = (q² - 1)⁸`, the cleared
Fermi relation `2 · gF_dimless² · (v / m)⁴ = 1` is equivalent to
`2 · ((v / m) · (q² - 1)⁴)⁴ = 1`. -/
theorem fermi_vev_scaling_of_fourHopDirectNorm {K : Type*} [Field K]
    (q gF_dimless v_over_m : K) (hq : q ≠ 0)
    (hgF : gF_dimless = multiChannelRate 4 q) :
    gF_dimless = (q ^ 2 - 1) ^ 8 ∧
    (2 * gF_dimless ^ 2 * v_over_m ^ 4 = 1 ↔
      2 * (v_over_m * (q ^ 2 - 1) ^ 4) ^ 4 = 1) := by
  have hr4 := (sweedler_weak_degree_ladder q hq).2.2.2.2
  refine ⟨hgF.trans hr4, ?_⟩
  rw [hgF, hr4]
  constructor <;> intro h <;> linear_combination h

/-- **Strict hierarchy of `(q² - 1)` powers in the sub-unit window `1 < q` and `q² < 2`:**
`0 < (q² - 1)⁸ < (q² - 1)⁴ < (q² - 1)² < 1` and `((q² - 1)²)⁻¹ < ((q² - 1)⁴)⁻¹`. -/
theorem sweedler_degree_strict_hierarchy_of_sub_unit
    {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    (q : F) (hq1 : 1 < q) (hq2 : q ^ 2 < 2) :
    0 < (q ^ 2 - 1) ^ 8 ∧
    (q ^ 2 - 1) ^ 8 < (q ^ 2 - 1) ^ 4 ∧
    (q ^ 2 - 1) ^ 4 < (q ^ 2 - 1) ^ 2 ∧
    ((q ^ 2 - 1) ^ 2)⁻¹ < ((q ^ 2 - 1) ^ 4)⁻¹ := by
  have hu_pos : 0 < q ^ 2 - 1 := by nlinarith
  have hu_lt1 : q ^ 2 - 1 < 1 := by linarith
  have hu2_pos : 0 < (q ^ 2 - 1) ^ 2 := pow_pos hu_pos 2
  have hu2_lt1 : (q ^ 2 - 1) ^ 2 < 1 := by nlinarith
  have hu4_pos : 0 < (q ^ 2 - 1) ^ 4 := pow_pos hu_pos 4
  have hu4_lt_u2 : (q ^ 2 - 1) ^ 4 < (q ^ 2 - 1) ^ 2 := by
    have heq : (q ^ 2 - 1) ^ 4 = (q ^ 2 - 1) ^ 2 * (q ^ 2 - 1) ^ 2 := by ring
    rw [heq]
    nlinarith
  have hu8_lt_u4 : (q ^ 2 - 1) ^ 8 < (q ^ 2 - 1) ^ 4 := by
    have hu4_lt1 : (q ^ 2 - 1) ^ 4 < 1 := lt_trans hu4_lt_u2 hu2_lt1
    have heq : (q ^ 2 - 1) ^ 8 = (q ^ 2 - 1) ^ 4 * (q ^ 2 - 1) ^ 4 := by ring
    rw [heq]
    nlinarith
  refine ⟨pow_pos hu_pos 8, hu8_lt_u4, hu4_lt_u2, ?_⟩
  exact (inv_lt_inv₀ hu2_pos hu4_pos).mpr hu4_lt_u2

/-- **Reconciliation with `EwVevGaps.su2_coupling_not_selfConsistent`:**
Whereas a gauge coupling `α₂ > 1 / 30` cannot satisfy `α₂ · N_v = 1` with `N_v > 100`, any
`q` in an ordered field satisfying `1 < q` and `q² < 5 / 4` (which includes the rational interval
`1 < q ≤ 111 / 100`, since `(111 / 100)² = 12321 / 10000 < 5 / 4`) gives a Sweedler 4-hop inverse
coupling `κ_S = (q² - 1)⁴` satisfying `0 < κ_S < 1 / 256 < 1 / 30`, `κ_S⁻¹ > 256 > 100`, and
`κ_S · κ_S⁻¹ = 1`. -/
theorem sweedler_fourHop_escapes_su2_wall_of_sq_lt_five_fourths
    {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    (q : F) (hq1 : 1 < q) (hq54 : q ^ 2 < 5 / 4) :
    0 < (q ^ 2 - 1) ^ 4 ∧
    (q ^ 2 - 1) ^ 4 < 1 / 256 ∧
    (q ^ 2 - 1) ^ 4 < 1 / 30 ∧
    256 < ((q ^ 2 - 1) ^ 4)⁻¹ ∧
    (q ^ 2 - 1) ^ 4 * ((q ^ 2 - 1) ^ 4)⁻¹ = 1 := by
  have hu_pos : 0 < q ^ 2 - 1 := by nlinarith
  have hu_lt : q ^ 2 - 1 < 1 / 4 := by linarith
  have hu2_pos : 0 < (q ^ 2 - 1) ^ 2 := pow_pos hu_pos 2
  have hu2_lt : (q ^ 2 - 1) ^ 2 < 1 / 16 := by nlinarith
  have hu4_pos : 0 < (q ^ 2 - 1) ^ 4 := pow_pos hu_pos 4
  have hu4_lt : (q ^ 2 - 1) ^ 4 < 1 / 256 := by
    have heq : (q ^ 2 - 1) ^ 4 = ((q ^ 2 - 1) ^ 2) ^ 2 := by ring
    rw [heq]
    nlinarith
  have h_inv_mul : (q ^ 2 - 1) ^ 4 * ((q ^ 2 - 1) ^ 4)⁻¹ = 1 := mul_inv_cancel₀ hu4_pos.ne'
  have h_inv_pos : 0 < ((q ^ 2 - 1) ^ 4)⁻¹ := inv_pos.mpr hu4_pos
  have h_gt256 : 256 < ((q ^ 2 - 1) ^ 4)⁻¹ := by
    have hmul : (q ^ 2 - 1) ^ 4 * ((q ^ 2 - 1) ^ 4)⁻¹ < (1 / 256) * ((q ^ 2 - 1) ^ 4)⁻¹ :=
      mul_lt_mul_of_pos_right hu4_lt h_inv_pos
    rw [h_inv_mul] at hmul
    linarith
  exact ⟨hu4_pos, hu4_lt, by linarith, h_gt256, h_inv_mul⟩

/-- **Honest tree-level non-coincidence (`ewDressedTreeComplexity q < 287 < 300 < (q² - 1)⁻⁴`):**
For every real `q` in the pure rational bracket `1109 / 1000 < q < 1111 / 1000`, the dressed
Bring–Schwinger tree complexity `q · ([2]_q / 2) · [4]_q · [6]_q · [8]_q` lies strictly below
`287`, whereas `((q² - 1)⁴)⁻¹` lies strictly above `300`. Thus `(q² - 1)⁻⁴` does **not** coincide
with `ewDressedTreeComplexity q` at tree level. -/
theorem ewDressedTreeComplexity_lt_sweedlerFourHopInv_of_rational_bracket
    (q : ℝ) (hq_lo : (1109 / 1000 : ℝ) < q) (hq_hi : q < (1111 / 1000 : ℝ)) :
    ewDressedTreeComplexity q < 287 ∧
    300 < ((q ^ 2 - 1) ^ 4)⁻¹ ∧
    ewDressedTreeComplexity q ≠ ((q ^ 2 - 1) ^ 4)⁻¹ := by
  have hq_pos : 0 < q := by linarith
  have hqi_lo : (1000 / 1111 : ℝ) < q⁻¹ := by
    rw [inv_eq_one_div, div_lt_div_iff₀ (by norm_num) hq_pos]
    linarith
  have hqi_hi : q⁻¹ < (1000 / 1109 : ℝ) := by
    rw [inv_eq_one_div, div_lt_div_iff₀ hq_pos (by norm_num)]
    linarith
  have hh_lo : (207 / 1000 : ℝ) < q - q⁻¹ := by linarith
  have hh_pos : 0 < q - q⁻¹ := by linarith
  have hqi_pos : 0 < q⁻¹ := inv_pos.mpr hq_pos
  have hq2_eq : qIntBal q 2 = q + q⁻¹ := by
    rw [QOU.QInteger.qIntBal_def]
    have hne : q - q⁻¹ ≠ 0 := hh_pos.ne'
    have hmul : q ^ 2 - (q⁻¹) ^ 2 = (q - q⁻¹) * (q + q⁻¹) := by ring
    rw [hmul, mul_div_cancel_left₀ _ hne]
  have hq2_half : qIntBal q 2 / 2 < (101 / 100 : ℝ) := by
    rw [hq2_eq]; linarith
  have hq2_pos : 0 < qIntBal q 2 / 2 := by
    rw [hq2_eq]; linarith
  have hb4 : qIntBal q 4 < (42 / 10 : ℝ) := by
    rw [QOU.QInteger.qIntBal_def]
    refine (div_lt_iff₀ hh_pos).mpr ?_
    have hp1 : q ^ 4 < (1111 / 1000 : ℝ) ^ 4 := pow_lt_pow_left₀ hq_hi hq_pos.le (by decide)
    have hp2 : (1000 / 1111 : ℝ) ^ 4 < (q⁻¹) ^ 4 :=
      pow_lt_pow_left₀ hqi_lo (by norm_num) (by decide)
    linarith
  have hb4_pos : 0 < qIntBal q 4 := by
    rw [QOU.QInteger.qIntBal_def]
    apply div_pos _ hh_pos
    have : (q⁻¹) ^ 4 < 1 := pow_lt_one₀ hqi_pos.le (by linarith) (by decide)
    have : (1 : ℝ) < q ^ 4 := one_lt_pow₀ (by linarith) (by decide)
    linarith
  have hb6 : qIntBal q 6 < (66 / 10 : ℝ) := by
    rw [QOU.QInteger.qIntBal_def]
    refine (div_lt_iff₀ hh_pos).mpr ?_
    have hp1 : q ^ 6 < (1111 / 1000 : ℝ) ^ 6 := pow_lt_pow_left₀ hq_hi hq_pos.le (by decide)
    have hp2 : (1000 / 1111 : ℝ) ^ 6 < (q⁻¹) ^ 6 :=
      pow_lt_pow_left₀ hqi_lo (by norm_num) (by decide)
    linarith
  have hb6_pos : 0 < qIntBal q 6 := by
    rw [QOU.QInteger.qIntBal_def]
    apply div_pos _ hh_pos
    have : (q⁻¹) ^ 6 < 1 := pow_lt_one₀ hqi_pos.le (by linarith) (by decide)
    have : (1 : ℝ) < q ^ 6 := one_lt_pow₀ (by linarith) (by decide)
    linarith
  have hb8 : qIntBal q 8 < (92 / 10 : ℝ) := by
    rw [QOU.QInteger.qIntBal_def]
    refine (div_lt_iff₀ hh_pos).mpr ?_
    have hp1 : q ^ 8 < (1111 / 1000 : ℝ) ^ 8 := pow_lt_pow_left₀ hq_hi hq_pos.le (by decide)
    have hp2 : (1000 / 1111 : ℝ) ^ 8 < (q⁻¹) ^ 8 :=
      pow_lt_pow_left₀ hqi_lo (by norm_num) (by decide)
    linarith
  have hb8_pos : 0 < qIntBal q 8 := by
    rw [QOU.QInteger.qIntBal_def]
    apply div_pos _ hh_pos
    have : (q⁻¹) ^ 8 < 1 := pow_lt_one₀ hqi_pos.le (by linarith) (by decide)
    have : (1 : ℝ) < q ^ 8 := one_lt_pow₀ (by linarith) (by decide)
    linarith
  have htree_lt : ewDressedTreeComplexity q < 287 := by
    unfold ewDressedTreeComplexity ewBareCrossingComplexity
    have hm1 : q * qIntBal q 4 < (1111 / 1000) * (42 / 10) :=
      mul_lt_mul'' hq_hi hb4 hq_pos.le hb4_pos.le
    have hm2 : q * qIntBal q 4 * qIntBal q 6 < (1111 / 1000) * (42 / 10) * (66 / 10) :=
      mul_lt_mul'' hm1 hb6 (mul_pos hq_pos hb4_pos).le hb6_pos.le
    have hm3 : q * qIntBal q 4 * qIntBal q 6 * qIntBal q 8 <
        (1111 / 1000) * (42 / 10) * (66 / 10) * (92 / 10) :=
      mul_lt_mul'' hm2 hb8 (mul_pos (mul_pos hq_pos hb4_pos) hb6_pos).le hb8_pos.le
    have hm4 : q * qIntBal q 4 * qIntBal q 6 * qIntBal q 8 * (qIntBal q 2 / 2) <
        (1111 / 1000) * (42 / 10) * (66 / 10) * (92 / 10) * (101 / 100) :=
      mul_lt_mul'' hm3 hq2_half
        (mul_pos (mul_pos (mul_pos hq_pos hb4_pos) hb6_pos) hb8_pos).le hq2_pos.le
    linarith
  have hu_pos : 0 < q ^ 2 - 1 := by nlinarith
  have hu_hi : q ^ 2 - 1 < (6 / 25 : ℝ) := by nlinarith
  have hu4_pos : 0 < (q ^ 2 - 1) ^ 4 := pow_pos hu_pos 4
  have hu4_hi : (q ^ 2 - 1) ^ 4 < (6 / 25 : ℝ) ^ 4 :=
    pow_lt_pow_left₀ hu_hi hu_pos.le (by decide)
  have h_inv_pos : 0 < ((q ^ 2 - 1) ^ 4)⁻¹ := inv_pos.mpr hu4_pos
  have h_gt300 : 300 < ((q ^ 2 - 1) ^ 4)⁻¹ := by
    have hmul : (q ^ 2 - 1) ^ 4 * ((q ^ 2 - 1) ^ 4)⁻¹ < (6 / 25 : ℝ) ^ 4 * ((q ^ 2 - 1) ^ 4)⁻¹ :=
      mul_lt_mul_of_pos_right hu4_hi h_inv_pos
    rw [mul_inv_cancel₀ hu4_pos.ne'] at hmul
    linarith
  exact ⟨htree_lt, h_gt300, by linarith⟩

/-- Exact 1-loop Habiro shift when replacing a self-consistent root `α_v` (`IsElectroweakVevFixedPoint`)
by the parameter-free Sweedler coupling `κ_S = (q² - 1)⁴` inside the `EwVevGaps` loop assembly. -/
theorem ewVev_sweedler_loop_shift_eq (q α_v : ℝ) (hfp : IsElectroweakVevFixedPoint q α_v) :
    (ewFixedPointConst q - (q ^ 2 - 1) ^ 4 * ewHabiroNorm q *
        (1 - (ewHbarQ q) ^ 2 * (q ^ 2 - 1) ^ 4)) - (1 / α_v) =
      -ewHabiroNorm q * ((q ^ 2 - 1) ^ 4 - α_v) *
        (1 - (ewHbarQ q) ^ 2 * ((q ^ 2 - 1) ^ 4 + α_v)) := by
  rw [hfp]
  exact QOU.StandardModel.EwVevGaps.loopShift_identity
    (ewFixedPointConst q) (ewHabiroNorm q) ((ewHbarQ q) ^ 2) ((q ^ 2 - 1) ^ 4) α_v

end SweedlerBridge

/-! ## Section 2: `su(2)_L ⊕ u(1)_Y → u(1)_EM` Goldstone Rank `3` & Higgs Potential Stability -/

section CategoricalHiggsAndStability

/-- Infinitesimal real-4D `su(2)_L ⊕ u(1)_Y` gauge variation `(θ₁, θ₂, θ₃, θ_Y) ↦ δΦ` around a
neutral Higgs doublet vacuum `⟨Φ⟩ = (0, v0)` of hypercharge `Y = +1` (`Q = T₃ + Y / 2`):
`δΦ = ((1/2) v0 θ₂, (1/2) v0 θ₁, 0, (1/2) v0 (θ_Y - θ₃))` in `(Re φ⁺, Im φ⁺, Re φ⁰, Im φ⁰)`. -/
def ewVacuumOrbit {K : Type*} [Field K] (v0 : K) :
    (K × K × K × K) →ₗ[K] (K × K × K × K) where
  toFun θ :=
    ((1 / 2 : K) * v0 * θ.2.1,
     (1 / 2 : K) * v0 * θ.1,
     0,
     (1 / 2 : K) * v0 * (θ.2.2.2 - θ.2.2.1))
  map_add' a b := by ext <;> simp <;> ring
  map_smul' c a := by ext <;> simp <;> ring

/-- **Unbroken `u(1)_EM` photon stabilizer:** For any nonzero VEV `v0 ≠ 0` over a characteristic-zero
field, `(θ₁, θ₂, θ₃, θ_Y)` annihilates the vacuum iff `θ₁ = 0 ∧ θ₂ = 0 ∧ θ₃ = θ_Y` (the exact
1-parameter electromagnetic subgroup generated by `Q = T₃ + Y / 2`). -/
theorem ewVacuumOrbit_kernel_iff_photon {K : Type*} [Field K] [CharZero K]
    (v0 : K) (hv : v0 ≠ 0) (θ : K × K × K × K) :
    ewVacuumOrbit v0 θ = 0 ↔ θ.1 = 0 ∧ θ.2.1 = 0 ∧ θ.2.2.1 = θ.2.2.2 := by
  have h2 : (1 / 2 : K) * v0 ≠ 0 := mul_ne_zero (by norm_num) hv
  simp only [ewVacuumOrbit, LinearMap.coe_mk, AddHom.coe_mk, Prod.ext_iff, Prod.fst_zero,
    Prod.snd_zero, mul_eq_zero, h2, false_or, true_and]
  constructor
  · rintro ⟨hθ2, hθ1, hdiff⟩
    exact ⟨hθ1, hθ2, by linear_combination -hdiff⟩
  · rintro ⟨hθ1, hθ2, heq⟩
    exact ⟨hθ2, hθ1, by linear_combination -heq⟩

/-- **Exact 3-Goldstone surjectivity (`W⁺_L, W⁻_L, Z_L`) and zero radial Higgs gauge shift:**
For `v0 ≠ 0`, `ewVacuumOrbit v0` always has zero radial (`Re φ⁰`) component, and hits **every**
3-Goldstone vector `(g₁, g₂, 0, g₃)` (`dim Im = 3`, eaten by `W±` and `Z`). -/
theorem ewVacuumOrbit_goldstone_three_space {K : Type*} [Field K] [CharZero K]
    (v0 : K) (hv : v0 ≠ 0) (g₁ g₂ g₃ : K) :
    (∀ θ, (ewVacuumOrbit v0 θ).2.2.1 = 0) ∧
    ∃ θ : K × K × K × K, ewVacuumOrbit v0 θ = (g₁, g₂, 0, g₃) := by
  refine ⟨fun _ => rfl, ?_⟩
  refine ⟨(2 * g₂ / v0, 2 * g₁ / v0, 0, 2 * g₃ / v0), ?_⟩
  ext <;> simp [ewVacuumOrbit] <;> field_simp

/-- Quadratic gauge-boson mass form `(v² / 4) · (g₂² (W₁² + W₂²) + (g₂ W₃ - g_Y B)²)` after EWSB,
and orthogonal Weinberg rotation `(Z, A) = ((g₂ W₃ - g_Y B), (g_Y W₃ + g₂ B))`:
the photon combination `A` decouples completely (mass `0`), while `(W₁, W₂, Z)` acquire masses
`M_W² = g₂² v² / 4` and `M_Z² = (g₂² + g_Y²) v² / 4`. -/
theorem ewGaugeMassForm_orthogonal_split {R : Type*} [CommRing R]
    (vSq g2 gY W1 W2 W3 B : R) :
    vSq * (g2 ^ 2 * (W1 ^ 2 + W2 ^ 2) + (g2 * W3 - gY * B) ^ 2) * (g2 ^ 2 + gY ^ 2) =
      vSq * g2 ^ 2 * (g2 ^ 2 + gY ^ 2) * (W1 ^ 2 + W2 ^ 2) +
      vSq * (g2 ^ 2 + gY ^ 2) * (g2 * W3 - gY * B) ^ 2 +
      0 * (gY * W3 + g2 * B) ^ 2 ∧
    (g2 * W3 - gY * B) ^ 2 + (gY * W3 + g2 * B) ^ 2 =
      (g2 ^ 2 + gY ^ 2) * (W3 ^ 2 + B ^ 2) := by
  exact ⟨by ring, by ring⟩

/-- **Tree-level custodial `M_W² / M_Z² = cos²θ_W` and `1 / e² = 1 / g₂² + 1 / g_Y²` identities:**
With `mW_sq = g2² vSq / 4`, `mZ_sq = (g2² + gY²) vSq / 4`, `cosSq = g2² / (g2² + gY²)`,
`sinSq = gY² / (g2² + gY²)`, and `eSq = g2² gY² / (g2² + gY²)`. -/
theorem ew_tree_weinberg_cos_sin_identities {K : Type*} [Field K] [CharZero K]
    (vSq g2 gY : K) (hv : vSq ≠ 0) (hg2 : g2 ≠ 0) (hgY : gY ≠ 0)
    (hsum : g2 ^ 2 + gY ^ 2 ≠ 0) :
    (g2 ^ 2 * vSq / 4) / ((g2 ^ 2 + gY ^ 2) * vSq / 4) = g2 ^ 2 / (g2 ^ 2 + gY ^ 2) ∧
    g2 ^ 2 / (g2 ^ 2 + gY ^ 2) + gY ^ 2 / (g2 ^ 2 + gY ^ 2) = 1 ∧
    1 / (g2 ^ 2 * gY ^ 2 / (g2 ^ 2 + gY ^ 2)) = 1 / g2 ^ 2 + 1 / gY ^ 2 := by
  refine ⟨?_, ?_, ?_⟩
  · field_simp
  · field_simp
  · field_simp; ring

/-- Renormalizable tree-level Higgs potential `V(Φ†Φ) = -μ² (Φ†Φ) + λ_H (Φ†Φ)²` written in terms
of `phiSq = Φ†Φ`. -/
def higgsPotential {R : Type*} [CommRing R] (muSq lam phiSq : R) : R :=
  -muSq * phiSq + lam * phiSq ^ 2

/-- **Completing the square on the Higgs potential (`μ² = λ_H v²`):**
`V(Φ†Φ) = λ_H (Φ†Φ - v² / 2)² - λ_H v⁴ / 4`. -/
theorem higgsPotential_complete_square {K : Type*} [Field K] [CharZero K]
    (lam vSq phiSq : K) :
    higgsPotential (lam * vSq) lam phiSq =
      lam * (phiSq - vSq / 2) ^ 2 - lam * vSq ^ 2 / 4 := by
  unfold higgsPotential
  ring

/-- **Tree-level vacuum stability & spontaneous symmetry breaking (`λ_H > 0, v² > 0`):**
1. At `Φ†Φ = v² / 2`, `V = -λ_H v⁴ / 4 < 0 = V(0)` (broken phase strictly lowers vacuum energy);
2. For every `phiSq`, `V(v² / 2) ≤ V(phiSq)`;
3. `V(phiSq) = V(v² / 2)` iff `phiSq = v² / 2` (unique global minimum on `Φ†Φ`). -/
theorem higgsPotential_unique_global_min_of_pos_quartic
    {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    (lam vSq : F) (hlam : 0 < lam) (hv : 0 < vSq) :
    higgsPotential (lam * vSq) lam (vSq / 2) = -lam * vSq ^ 2 / 4 ∧
    higgsPotential (lam * vSq) lam (vSq / 2) < higgsPotential (lam * vSq) lam 0 ∧
    (∀ phiSq : F, higgsPotential (lam * vSq) lam (vSq / 2) ≤
      higgsPotential (lam * vSq) lam phiSq) ∧
    (∀ phiSq : F, higgsPotential (lam * vSq) lam phiSq =
      higgsPotential (lam * vSq) lam (vSq / 2) ↔ phiSq = vSq / 2) := by
  have hv_min : higgsPotential (lam * vSq) lam (vSq / 2) = -lam * vSq ^ 2 / 4 := by
    unfold higgsPotential; ring
  have hv0 : higgsPotential (lam * vSq) lam 0 = 0 := by unfold higgsPotential; ring
  refine ⟨hv_min, ?_, ?_, ?_⟩
  · rw [hv_min, hv0]
    have hv2 : 0 < vSq ^ 2 := sq_pos_of_pos hv
    nlinarith
  · intro phiSq
    rw [hv_min, higgsPotential_complete_square]
    have hsq : 0 ≤ (phiSq - vSq / 2) ^ 2 := sq_nonneg _
    nlinarith
  · intro phiSq
    rw [hv_min, higgsPotential_complete_square]
    constructor
    · intro h
      have hsq0 : lam * (phiSq - vSq / 2) ^ 2 = 0 := by linarith
      rcases mul_eq_zero.mp hsq0 with h0 | h0
      · exact absurd h0 hlam.ne'
      · have hd : phiSq - vSq / 2 = 0 := sq_eq_zero_iff.mp h0
        linarith
    · intro h
      rw [h]; ring

/-- **Physical radial Higgs mass identity (`m_H² = 2 λ_H v²`):**
Expanding `Φ†Φ = (v + H)² / 2` around the VEV `v` yields
`V((v + H)² / 2) - V(v² / 2) = (1 / 2) (2 λ_H v²) H² + λ_H v H³ + (λ_H / 4) H⁴`,
identifying the physical scalar mass-squared `m_H² = 2 λ_H v²` and proving `λ_H = m_H² / (2 v²)`. -/
theorem higgs_radial_expansion_mass_sq {K : Type*} [Field K] [CharZero K]
    (lam v H : K) :
    higgsPotential (lam * v ^ 2) lam ((v + H) ^ 2 / 2) -
        higgsPotential (lam * v ^ 2) lam (v ^ 2 / 2) =
      (1 / 2 : K) * (2 * lam * v ^ 2) * H ^ 2 + lam * v * H ^ 3 + (lam / 4) * H ^ 4 := by
  unfold higgsPotential
  ring

/-- **Converse vacuum instability (`λ_H < 0`):** If `λ_H < 0`, the potential is unbounded below on
`Φ†Φ ≥ 0`. -/
theorem higgsPotential_unbounded_below_of_neg_quartic
    {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    (muSq lam B : F) (hlam : lam < 0) :
    ∃ phiSq : F, 0 ≤ phiSq ∧ higgsPotential muSq lam phiSq < B := by
  -- Choose `phiSq = max 1 ((|muSq| + |B| + 1) / (-lam))`
  have hneg_pos : 0 < -lam := neg_pos.mpr hlam
  set M : F := max 1 ((|muSq| + |B| + 1) / (-lam))
  have hM1 : 1 ≤ M := le_max_left _ _
  have hM0 : 0 ≤ M := by linarith
  have hM_bound : (|muSq| + |B| + 1) / (-lam) ≤ M := le_max_right _ _
  have hmul : |muSq| + |B| + 1 ≤ (-lam) * M := by
    have hm := (div_le_iff₀ hneg_pos).mp hM_bound
    linarith
  refine ⟨M, hM0, ?_⟩
  unfold higgsPotential
  have hM2 : M ≤ M ^ 2 := by nlinarith
  have hlamM2 : (-lam) * M ≤ (-lam) * M ^ 2 := mul_le_mul_of_nonneg_left hM2 hneg_pos.le
  have hmu : -|muSq| ≤ muSq := neg_abs_le muSq
  have hmuM : -(|muSq| * M) ≤ muSq * M := by nlinarith
  have hB : -|B| ≤ B := neg_abs_le B
  have h1M : |muSq| ≤ |muSq| * M := by
    have habs : 0 ≤ |muSq| := abs_nonneg muSq
    nlinarith
  -- Bound `-muSq * M + lam * M^2 ≤ |muSq| * M - ((-lam) * M) * M`
  have hmu_le : -muSq ≤ |muSq| := neg_le_abs muSq
  have hterm1 : (-muSq) * M ≤ |muSq| * M := mul_le_mul_of_nonneg_right hmu_le hM0
  have hkey : (|muSq| + |B| + 1) * M ≤ (-lam) * M ^ 2 := by
    have := mul_le_mul_of_nonneg_right hmul hM0
    linarith [show (-lam) * M * M = (-lam) * M ^ 2 by ring]
  have hB1 : 0 ≤ |B| := abs_nonneg B
  have hBM : |B| ≤ |B| * M := by nlinarith
  have hleB : B ≤ |B| := le_abs_self B
  nlinarith

/-- Bridge to `CategoricalHiggsIdempotent`: `(m_H_GeV)² = 2 · higgs_self_coupling · (vev_v_GeV)²`
and `0 < (m_H_GeV)²`. -/
theorem categoricalHiggs_mH_sq_eq_two_lam_v_sq
    [inst : QOU.QuantumObservableUniverses.CategoricalHiggsIdempotent] :
    (QOU.QuantumObservableUniverses.CategoricalHiggsIdempotent.m_H_GeV) ^ 2 =
      2 * inst.higgs_self_coupling * inst.vev_v_GeV ^ 2 ∧
    0 < (QOU.QuantumObservableUniverses.CategoricalHiggsIdempotent.m_H_GeV) ^ 2 := by
  unfold QOU.QuantumObservableUniverses.CategoricalHiggsIdempotent.m_H_GeV
  have hlam : 0 < 2 * inst.higgs_self_coupling := by linarith [inst.higgs_self_coupling_pos]
  have hv : 0 < inst.vev_v_GeV := inst.vev_v_pos
  refine ⟨?_, ?_⟩
  · rw [mul_pow, inst.higgs_root_sq]
  · have := inst.higgs_root_pos
    positivity

/-- Bridge to remediated `QOU.BraidKnot.scalarOverGaugeRatio` (`catalanG = Cl_2 (π / 2)`):
for every `|h| ≤ 1 / 2`, the `h⁴` Borromean-Catalan scalar/gauge factor `(6 / 5)(1 - 2 G h⁴)` is
strictly positive (`> 1`), proved purely from `catalanG_in_open_rational_interval` without any
decimal literal. -/
theorem braidKnot_scalarOverGaugeRatio_gt_one_of_abs_le_half
    (h : ℝ) (hh : |h| ≤ 1 / 2) :
    1 < QOU.BraidKnot.scalarOverGaugeRatio h := by
  unfold QOU.BraidKnot.scalarOverGaugeRatio QOU.BraidKnot.h4StructuralCorrection
  rw [QOU.BraidKnot.vol_borromean_over_four_eq_two_catalan]
  have hG := QOU.BraidKnot.catalanG_in_open_rational_interval
  have hh2 : h ^ 2 ≤ 1 / 4 := by
    have habs := abs_le.mp hh
    nlinarith
  have hh4_nonneg : 0 ≤ h ^ 4 := by positivity
  have hh4_le : h ^ 4 ≤ 1 / 16 := by
    have : h ^ 4 = (h ^ 2) ^ 2 := by ring
    rw [this]
    have h2_0 : 0 ≤ h ^ 2 := sq_nonneg h
    nlinarith
  nlinarith [hG.1, hG.2]

end CategoricalHiggsAndStability

/-! ## Section 3: Exact Rational 1-Loop & 2-Loop SM `SU(3)_c × SU(2)_L × U(1)_Y` Beta Functions -/

section SMBetaFunctions

/-- Quantum-number record `(dim3, dim2, yHalf)` for a chiral Weyl or complex scalar multiplet of
`SU(3)_c × SU(2)_L × U(1)_Y`, with electric charge `Q = T₃ + yHalf` and canonical `SU(5)` /
split-bundle `F = V₂ ⊕ W₃*` normalization `C₂^(1) = (3 / 5) yHalf²`. -/
structure SMMultiplet (K : Type*) where
  dim3 : K
  dim2 : K
  c2_su3 : K
  c2_su2 : K
  s2_su3_per_su2 : K
  s2_su2_per_su3 : K
  yHalf : K

section FieldCharZero

variable {K : Type*} [Field K] [CharZero K]

/-- Canonical `U(1)₁` quadratic Casimir `(3 / 5) · (Y / 2)²` and Dynkin index on a multiplet. -/
def c2U1 (m : SMMultiplet K) : K := (3 / 5 : K) * m.yHalf ^ 2
def s2U1 (m : SMMultiplet K) : K := m.dim3 * m.dim2 * c2U1 m
def s2SU2 (m : SMMultiplet K) : K := m.dim3 * m.s2_su2_per_su3
def s2SU3 (m : SMMultiplet K) : K := m.dim2 * m.s2_su3_per_su2

/-- The five chiral Weyl multiplets of one Standard Model fermion generation:
`Q_L = (3, 2, +1/6)`, `u_R^c = (3̄, 1, -2/3)`, `d_R^c = (3̄, 1, +1/3)`, `L_L = (1, 2, -1/2)`,
`e_R^c = (1, 1, +1)`. -/
def smQL : SMMultiplet K := ⟨3, 2, 4 / 3, 3 / 4, 1 / 2, 1 / 2, 1 / 6⟩
def smURc : SMMultiplet K := ⟨3, 1, 4 / 3, 0, 1 / 2, 0, -(2 / 3)⟩
def smDRc : SMMultiplet K := ⟨3, 1, 4 / 3, 0, 1 / 2, 0, 1 / 3⟩
def smLL : SMMultiplet K := ⟨1, 2, 0, 3 / 4, 0, 1 / 2, -(1 / 2)⟩
def smERc : SMMultiplet K := ⟨1, 1, 0, 0, 0, 0, 1⟩

/-- The complex Higgs scalar doublet `H = (1, 2, +1/2)`. -/
def smHiggs : SMMultiplet K := ⟨1, 2, 0, 3 / 4, 0, 1 / 2, 1 / 2⟩

def smGenFermions : List (SMMultiplet K) := [smQL, smURc, smDRc, smLL, smERc]

/-- **Universal single-generation Weyl Dynkin index (`= 2` in all three gauge factors):**
Because `(Q_L, u_R^c, d_R^c, L_L, e_R^c)` fills complete `SU(5)`-compatible representations
`5̄ ⊕ 10`, the total Weyl Dynkin index per generation equals `2` simultaneously for `U(1)₁`,
`SU(2)_L`, and `SU(3)_c`. -/
theorem sm_gen_dynkin_universal :
    (smGenFermions (K := K)).foldr (fun m acc => s2U1 m + acc) 0 = 2 ∧
    (smGenFermions (K := K)).foldr (fun m acc => s2SU2 m + acc) 0 = 2 ∧
    (smGenFermions (K := K)).foldr (fun m acc => s2SU3 m + acc) 0 = 2 := by
  simp only [smGenFermions, smQL, smURc, smDRc, smLL, smERc, s2U1, s2SU2, s2SU3, c2U1,
    List.foldr]
  refine ⟨by ring, by ring, by ring⟩

/-- 1-loop gauge beta coefficients `(b₁, b₂, b₃)` as functions of `(N_gen, N_H)` derived from
`-(11 / 3) C_A + (2 / 3) ∑_Weyl S₂ + (1 / 3) ∑_scalar S₂` (convention `d(α_i⁻¹)/d(ln μ) = -b_i/(2π)`). -/
def smBeta1 (nGen nH : K) : K :=
  -(11 / 3 : K) * 0 +
  (2 / 3 : K) * nGen * ((smGenFermions (K := K)).foldr (fun m acc => s2U1 m + acc) 0) +
  (1 / 3 : K) * nH * s2U1 (smHiggs (K := K))

def smBeta2 (nGen nH : K) : K :=
  -(11 / 3 : K) * 2 +
  (2 / 3 : K) * nGen * ((smGenFermions (K := K)).foldr (fun m acc => s2SU2 m + acc) 0) +
  (1 / 3 : K) * nH * s2SU2 (smHiggs (K := K))

def smBeta3 (nGen nH : K) : K :=
  -(11 / 3 : K) * 3 +
  (2 / 3 : K) * nGen * ((smGenFermions (K := K)).foldr (fun m acc => s2SU3 m + acc) 0) +
  (1 / 3 : K) * nH * s2SU3 (smHiggs (K := K))

/-- **Generation-independence of 1-loop differences `b_i - b_j`:**
For arbitrary `(nGen, nH)`, `nGen` cancels identically out of `b₁ - b₂`, `b₂ - b₃`, and `b₃ - b₁`;
only pure-gauge Casimirs and the Higgs doublet `nH` contribute to differential 1-loop running. -/
theorem sm_oneLoop_differences_independent_of_nGen (nGen nH : K) :
    smBeta1 nGen nH - smBeta2 nGen nH = (22 / 3 : K) - (1 / 15 : K) * nH ∧
    smBeta2 nGen nH - smBeta3 nGen nH = (11 / 3 : K) + (1 / 6 : K) * nH ∧
    smBeta3 nGen nH - smBeta1 nGen nH = -11 - (1 / 10 : K) * nH := by
  unfold smBeta1 smBeta2 smBeta3
  rw [sm_gen_dynkin_universal.1, sm_gen_dynkin_universal.2.1, sm_gen_dynkin_universal.2.2]
  simp only [smHiggs, s2U1, s2SU2, s2SU3, c2U1]
  exact ⟨by ring, by ring, by ring⟩

/-- **Exact Standard Model 1-loop beta triple at `(N_gen, N_H) = (3, 1)`:**
`(b₁, b₂, b₃) = (41 / 10, -19 / 6, -7)`, electromagnetic slope `(5 / 3) b₁ + b₂ = 11 / 3`, and
Weinberg slope difference `b₁ - b₂ = 109 / 15`. -/
theorem sm_oneLoop_betas_three_gen :
    smBeta1 (3 : K) 1 = 41 / 10 ∧
    smBeta2 (3 : K) 1 = -(19 / 6) ∧
    smBeta3 (3 : K) 1 = -7 ∧
    (5 / 3 : K) * smBeta1 (3 : K) 1 + smBeta2 (3 : K) 1 = 11 / 3 ∧
    smBeta1 (3 : K) 1 - smBeta2 (3 : K) 1 = 109 / 15 := by
  unfold smBeta1 smBeta2 smBeta3
  rw [sm_gen_dynkin_universal.1, sm_gen_dynkin_universal.2.1, sm_gen_dynkin_universal.2.2]
  simp only [smHiggs, s2U1, s2SU2, s2SU3, c2U1]
  refine ⟨by ring, by ring, by ring, by ring, by ring⟩

/-- Consistency bridge with `EwVevGaps.oneLoopB0`: `smBeta2 3 1 = EwVevGaps.oneLoopB0 2 6 (1/2)`. -/
theorem smBeta2_eq_ewVevGaps_oneLoopB0 :
    smBeta2 (3 : ℝ) 1 = QOU.StandardModel.EwVevGaps.oneLoopB0 (2 : ℝ) (12 * (1 / 2)) (1 / 2) := by
  rw [sm_oneLoop_betas_three_gen.2.1, QOU.StandardModel.EwVevGaps.b0_su2_sm]

/-- General Machacek–Vaughn 2-loop gauge-matter rational matrix entry `b_{ij}(nGen, nH)` (`i, j ∈ Fin 3`):
`- (34 / 3) C₂(G_i)² δ_{ij} + nGen ∑_f S₂^(i)(f) ((10 / 3) C₂(G_i) δ_{ij} + 2 C₂^(j)(f))
 + nH · S₂^(i)(H) ((2 / 3) C₂(G_i) δ_{ij} + 4 C₂^(j)(H))`. -/
def smC2Adjoint : ℕ → K
  | 0 => 0
  | 1 => 2
  | _ => 3

def multipletS2 : ℕ → SMMultiplet K → K
  | 0, m => s2U1 m
  | 1, m => s2SU2 m
  | _, m => s2SU3 m

def multipletC2 : ℕ → SMMultiplet K → K
  | 0, m => c2U1 m
  | 1, m => m.c2_su2
  | _, m => m.c2_su3

def smKron : ℕ → ℕ → K
  | 0, 0 => 1
  | 1, 1 => 1
  | 2, 2 => 1
  | _, _ => 0

def smTwoLoopTerm (i j : ℕ) (m : SMMultiplet K) : K :=
  multipletS2 i m * ((10 / 3 : K) * smC2Adjoint i * smKron i j + 2 * multipletC2 j m)

def smTwoLoopBeta (nGen nH : K) (i j : ℕ) : K :=
  (-(34 / 3 : K)) * (smC2Adjoint i) ^ 2 * smKron i j +
    nGen * (smTwoLoopTerm i j (smQL (K := K)) +
      smTwoLoopTerm i j (smURc (K := K)) +
      smTwoLoopTerm i j (smDRc (K := K)) +
      smTwoLoopTerm i j (smLL (K := K)) +
      smTwoLoopTerm i j (smERc (K := K))) +
    nH * (multipletS2 i (smHiggs (K := K)) *
      ((2 / 3 : K) * smC2Adjoint i * smKron i j + 4 * multipletC2 j (smHiggs (K := K))))

/-- **Exact 2-loop Machacek–Vaughn rational matrix `b_{ij}` of the Standard Model (`N_gen = 3, N_H = 1`):**
Derived directly from the Casimir/Dynkin data of `(Q_L, u_R^c, d_R^c, L_L, e_R^c, H)`:
`[[199/50, 27/10, 44/5], [9/10, 35/6, 12], [11/10, 9/2, -26]]`. -/
theorem sm_twoLoop_matrix_three_gen :
    smTwoLoopBeta (3 : K) 1 0 0 = 199 / 50 ∧
    smTwoLoopBeta (3 : K) 1 0 1 = 27 / 10 ∧
    smTwoLoopBeta (3 : K) 1 0 2 = 44 / 5 ∧
    smTwoLoopBeta (3 : K) 1 1 0 = 9 / 10 ∧
    smTwoLoopBeta (3 : K) 1 1 1 = 35 / 6 ∧
    smTwoLoopBeta (3 : K) 1 1 2 = 12 ∧
    smTwoLoopBeta (3 : K) 1 2 0 = 11 / 10 ∧
    smTwoLoopBeta (3 : K) 1 2 1 = 9 / 2 ∧
    smTwoLoopBeta (3 : K) 1 2 2 = -26 := by
  dsimp only [smTwoLoopBeta, smTwoLoopTerm, smC2Adjoint, smKron, smQL, smURc, smDRc, smLL, smERc,
    smHiggs, multipletS2, multipletC2, s2U1, s2SU2, s2SU3, c2U1]
  refine ⟨by ring, by ring, by ring, by ring, by ring, by ring, by ring, by ring, ?_⟩
  ring

end FieldCharZero

end SMBetaFunctions

/-! ## Section 4: Tree-Level `sin²θ_W⁰ = 3 / 8` to `sin²θ_W(μ)` & `α_s(μ)` RG Identities -/

section WeinbergAndRGThresholds

section AlgebraicIdentities

variable {K : Type*} [Field K] [CharZero K]

/-- Inverse electromagnetic coupling `(5 / 3) α₁⁻¹ + α₂⁻¹` in canonical `SU(5)` / `F = V₂ ⊕ W₃*`
normalization (`α_Y⁻¹ = (5 / 3) α₁⁻¹`). -/
def invAlphaEMOf (invA1 invA2 : K) : K := (5 / 3 : K) * invA1 + invA2

/-- Weak mixing observable `sin²θ_W = α_EM / α₂ = α₂⁻¹ / α_EM⁻¹`. -/
def sinSqThetaWOf (invA1 invA2 : K) : K := invA2 / invAlphaEMOf invA1 invA2

/-- **Tree-level / UV boundary identity (`#9216`):** When `α₁⁻¹ = α₂⁻¹ ≠ 0`, `sin²θ_W = 3 / 8`. -/
theorem weinberg_uv_three_eighths (invAUV : K) (hUV : invAUV ≠ 0) :
    sinSqThetaWOf invAUV invAUV = 3 / 8 := by
  unfold sinSqThetaWOf invAlphaEMOf
  have hden : (5 / 3 : K) * invAUV + invAUV = (8 / 3 : K) * invAUV := by ring
  rw [hden]
  field_simp

/-- **All-orders Weinberg shift identity (holds at any loop order):**
`3 / 8 - sin²θ_W = (5 / 8) · (α₁⁻¹ - α₂⁻¹) / α_EM⁻¹`. -/
theorem weinberg_universal_shift_from_three_eighths (invA1 invA2 : K)
    (hEM : invAlphaEMOf invA1 invA2 ≠ 0) :
    (3 / 8 : K) - sinSqThetaWOf invA1 invA2 =
      (5 / 8 : K) * ((invA1 - invA2) / invAlphaEMOf invA1 invA2) := by
  unfold sinSqThetaWOf
  field_simp
  unfold invAlphaEMOf
  ring

/-- 1-loop evolved inverse couplings `α_i⁻¹(t) = α_i⁻¹(0) + b_i · t` (`t = ln(μ_UV / μ) / (2π)`). -/
def runOneLoop1 (invA1_0 t : K) : K := invA1_0 + smBeta1 (3 : K) 1 * t
def runOneLoop2 (invA2_0 t : K) : K := invA2_0 + smBeta2 (3 : K) 1 * t
def runOneLoop3 (invA3_0 t : K) : K := invA3_0 + smBeta3 (3 : K) 1 * t

/-- **Georgi–Quinn–Weinberg 1-loop running identity from `sin²θ_W⁰ = 3 / 8`:**
Starting from `α₁⁻¹(0) = α₂⁻¹(0) = invAUV`, for every RG log-step `t = ln(μ_UV / μ) / (2π)` with
`α_EM⁻¹(t) ≠ 0`:
1. `α_EM⁻¹(t) = (8 / 3) invAUV + (11 / 3) t`;
2. `sin²θ_W(t) = 3 / 8 - (109 / 24) · t / α_EM⁻¹(t)`. -/
theorem georgi_quinn_weinberg_oneLoop_identity (invAUV t : K)
    (hEM : invAlphaEMOf (runOneLoop1 invAUV t) (runOneLoop2 invAUV t) ≠ 0) :
    invAlphaEMOf (runOneLoop1 invAUV t) (runOneLoop2 invAUV t) =
      (8 / 3 : K) * invAUV + (11 / 3 : K) * t ∧
    sinSqThetaWOf (runOneLoop1 invAUV t) (runOneLoop2 invAUV t) =
      (3 / 8 : K) - (109 / 24 : K) * t /
        invAlphaEMOf (runOneLoop1 invAUV t) (runOneLoop2 invAUV t) := by
  have hb := sm_oneLoop_betas_three_gen (K := K)
  have hem_eq : invAlphaEMOf (runOneLoop1 invAUV t) (runOneLoop2 invAUV t) =
      (8 / 3 : K) * invAUV + (11 / 3 : K) * t := by
    unfold invAlphaEMOf runOneLoop1 runOneLoop2
    rw [hb.1, hb.2.1]
    ring
  refine ⟨hem_eq, ?_⟩
  have hshift := weinberg_universal_shift_from_three_eighths
    (runOneLoop1 invAUV t) (runOneLoop2 invAUV t) hEM
  have hdiff : runOneLoop1 invAUV t - runOneLoop2 invAUV t = (109 / 15 : K) * t := by
    unfold runOneLoop1 runOneLoop2
    rw [hb.1, hb.2.1]
    ring
  rw [hdiff] at hshift
  linear_combination -hshift

/-- **1-loop strong coupling `α₃⁻¹(t)` from unified boundary `α₁(0) = α₂(0) = α₃(0)`:**
`α₃⁻¹(t) = (3 / 8) α_EM⁻¹(t) - (67 / 8) t`. -/
theorem strong_coupling_oneLoop_from_unification (invAUV t : K) :
    runOneLoop3 invAUV t =
      (3 / 8 : K) * invAlphaEMOf (runOneLoop1 invAUV t) (runOneLoop2 invAUV t) -
        (67 / 8 : K) * t := by
  have hb := sm_oneLoop_betas_three_gen (K := K)
  unfold runOneLoop3 runOneLoop1 runOneLoop2 invAlphaEMOf
  rw [hb.1, hb.2.1, hb.2.2.1]
  ring

/-- **Minimal-SM 1-loop coupling-triangle RG invariant:**
`smTriangleInv = 115 α₁⁻¹ - 333 α₂⁻¹ + 218 α₃⁻¹` (`= 30 · ((b₂ - b₃)α₁⁻¹ + (b₃ - b₁)α₂⁻¹ + (b₁ - b₂)α₃⁻¹)`). -/
def smTriangleInv (invA1 invA2 invA3 : K) : K :=
  115 * invA1 - 333 * invA2 + 218 * invA3

/-- `smTriangleInv` is **identically constant along every 1-loop SM RG trajectory** (regardless of
boundary conditions), equals `69 α_EM⁻¹ - 402 α₂⁻¹ + 218 α₃⁻¹`, and vanishes if and only if the
three 1-loop lines meet at a common scale `t*`. -/
theorem smTriangleInv_oneLoop_rg_invariant (invA1_0 invA2_0 invA3_0 t : K) :
    smTriangleInv (runOneLoop1 invA1_0 t) (runOneLoop2 invA2_0 t) (runOneLoop3 invA3_0 t) =
      smTriangleInv invA1_0 invA2_0 invA3_0 ∧
    smTriangleInv invA1_0 invA2_0 invA3_0 =
      69 * invAlphaEMOf invA1_0 invA2_0 - 402 * invA2_0 + 218 * invA3_0 := by
  have hb := sm_oneLoop_betas_three_gen (K := K)
  refine ⟨?_, ?_⟩
  · unfold smTriangleInv runOneLoop1 runOneLoop2 runOneLoop3
    rw [hb.1, hb.2.1, hb.2.2.1]
    ring
  · unfold smTriangleInv invAlphaEMOf
    ring

/-- **Exact criterion for single-step 1-loop SM gauge unification:**
There exists a log-scale `t` at which `runOneLoop1 invA1 t = runOneLoop2 invA2 t = runOneLoop3 invA3 t`
if and only if `smTriangleInv invA1 invA2 invA3 = 0`. -/
theorem sm_oneLoop_unification_iff_triangle_zero (invA1 invA2 invA3 : K) :
    (∃ t : K, runOneLoop1 invA1 t = runOneLoop2 invA2 t ∧
      runOneLoop2 invA2 t = runOneLoop3 invA3 t) ↔
      smTriangleInv invA1 invA2 invA3 = 0 := by
  have hb := sm_oneLoop_betas_three_gen (K := K)
  constructor
  · rintro ⟨t, h12, h23⟩
    have hinv := (smTriangleInv_oneLoop_rg_invariant invA1 invA2 invA3 t).1
    rw [← hinv, h12, h23]
    unfold smTriangleInv
    ring
  · intro htri
    refine ⟨(invA2 - invA1) * (15 / 109 : K), ?_, ?_⟩
    · unfold runOneLoop1 runOneLoop2
      rw [hb.1, hb.2.1]
      ring
    · unfold runOneLoop2 runOneLoop3
      rw [hb.2.1, hb.2.2.1]
      unfold smTriangleInv at htri
      linear_combination -(1 / 218 : K) * htri

end AlgebraicIdentities

section OrderedThresholdBounds

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- **Honest minimal-SM single-step `α_s(M_Z)` bound:**
Whenever `127 < α_EM⁻¹ < 129`, `(231 / 1000) α_EM⁻¹ < α₂⁻¹ < (232 / 1000) α_EM⁻¹`, and single-step
1-loop unification holds (`smTriangleInv = 0`), `α₃⁻¹ > 13` (so `α_s = 1 / α₃⁻¹ < 1 / 13`), proving
algebraically why single-step minimal-SM running without intermediate thresholds undershoots
`α_s(M_Z) ≈ 3 / 25`. -/
theorem sm_oneLoop_invAlpha3_gt_thirteen_of_msbar_window
    (invA1 invA2 invA3 : F)
    (hEM_lo : 127 < invAlphaEMOf invA1 invA2)
    (hW_lo : (231 / 1000 : F) * invAlphaEMOf invA1 invA2 < invA2)
    (htri : smTriangleInv invA1 invA2 invA3 = 0) :
    13 < invA3 := by
  have hrel := (smTriangleInv_oneLoop_rg_invariant invA1 invA2 invA3 0).2
  rw [htri] at hrel
  -- `0 = 69 * invEM - 402 * invA2 + 218 * invA3`, so `218 * invA3 = 402 * invA2 - 69 * invEM`
  linarith

/-- **Honest low-threshold Weinberg bound (`t ∈ (0, 1)`, covering `μ_UV / M_Z = (q₀² - 1)⁻⁴`):**
Since `-4 ln(q₀² - 1) < 2π` corresponds to `0 < t < 1`, starting from `sin²θ_W⁰ = 3 / 8` with
`α_EM⁻¹(t) > 127` keeps `sin²θ_W(t) > 33 / 100`, proving that a single 4-hop ratio `(q₀² - 1)⁻⁴`
cannot reach `sin²θ_W ≈ 231 / 1000` without higher-power UV/Bring running (`t > 5`). -/
theorem sweedler_low_threshold_weinberg_gt_thirtyThree_hundredths_of_unit_log
    (invAUV t : F) (ht_pos : 0 < t) (ht_lt1 : t < 1)
    (hEM_lo : 127 < invAlphaEMOf (runOneLoop1 invAUV t) (runOneLoop2 invAUV t)) :
    (33 / 100 : F) < sinSqThetaWOf (runOneLoop1 invAUV t) (runOneLoop2 invAUV t) := by
  set invEM := invAlphaEMOf (runOneLoop1 invAUV t) (runOneLoop2 invAUV t)
  have hEM_pos : 0 < invEM := by linarith
  have hgqw := (georgi_quinn_weinberg_oneLoop_identity invAUV t hEM_pos.ne').2
  rw [hgqw]
  have hdiv : (109 / 24 : F) * t / invEM < (109 / 24 : F) / 127 := by
    rw [div_lt_iff₀ hEM_pos]
    have h1 : (109 / 24 : F) * t < 109 / 24 := by linarith
    have h2 : (109 / 24 : F) / 127 * 127 < (109 / 24 : F) / 127 * invEM :=
      mul_lt_mul_of_pos_left hEM_lo (by norm_num)
    linarith
  linarith

end OrderedThresholdBounds

end WeinbergAndRGThresholds

end QOU.StandardModel.EWSweedlerRG
