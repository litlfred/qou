import Mathlib.Analysis.SpecialFunctions.Trigonometric.Inverse
import QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace
import QOU.QBeta.HolonomySpectrumSignObstruction

/-!
# Hyperbolic Full-Twist Framing & GPMT `(1^3)` Base Bridge for Convention-D `Q_β` (`qou-pdix` → `qou-cds1`)

This module formalizes the exact algebraic and real-analytic bridge theorems connecting the two
active candidate mechanisms for the Convention-D `Q_β` ladder & base gap (`qou-pdix` → `qou-cds1`):

## Section 1: Lever B — GPMT `(1^3)` Modified-Trace Completion of `tr_M^{z_D}` Where `w_{(1^3)}(z_D) = 0`
At Convention D (`z_D = q^3 / (q^2 + 1)`), the standard Markov weight on the antisymmetric
cubed-antifundamental sector `(1^3)` vanishes identically (`w_{(1^3)}(z_D) = 0`), while the
Geer–Patureau-Mirand–Turaev (GPMT) modified trace restores `(1^3)` with modified quantum dimension
`d_D(S^{(1^3)}) = -q^3 / ((q^2 + 1)(q^4 + q^2 + 1)) = -1 / ([2]_q [3]_q)` and positive magnitude
`|d_D(S^{(1^3)})| = -d_D(S^{(1^3)}) = +q^3 / ((q^2 + 1)(q^4 + q^2 + 1))`.
Main identities established in Section 1:
* `trM_conventionD_gpmtPos_eq_threeBlock_sum` and `trM_conventionD_gpmtSigned_eq_threeBlock_sum`:
  the exact 3-block Wedderburn character expansions of `tr_M^{D,GPMT±}(v) = tr_M^{z_D}(v) ∓ t_D^{(1^3)}(v)`.
* `chi3_nucleonDiffCoord`, `chi111_nucleonDiffCoord`, and
  `chi111_nucleonDiffCoord_eq_q_inv_pow_four_mul_chi3`:
  on the 11-crossing production `(n - p)` nucleon difference `neutronCoord - protonCoord` at
  `a = -(q - q⁻¹)/2`,
  `χ_{(3)}(n - p) = -(q^2 - 1)(q^2 + 1)^2 / (4 q)` and
  `χ_{(1^3)}(n - p) = -(q^2 - 1)(q^2 + 1)^2 / (4 q^5) = q^{-4} χ_{(3)}(n - p)`,
  so `χ_{(1^3)}(n - p)` and `χ_{(3)}(n - p)` have the **exact same sign** (`< 0` for `q > 1`).
* `chi3_deltaSNF`, `chi21_deltaSNF_eq_zero`, `chi111_deltaSNF`, `chi111_deltaSNF_eq_neg_chi3`,
  and `trM_conventionD_gpmtSigned_deltaSNF_ratio`:
  by contrast, on the single-crossing element `Δ_S = (h^2/2)·1 - (h/2)(σ_0 + σ_1)`,
  `χ_{(2,1)}(Δ_S) = 0` and `χ_{(1^3)}(Δ_S) = -χ_{(3)}(Δ_S) = (q^4 - 1)/(2 q^2)` has the
  **opposite sign** to `χ_{(3)}(Δ_S)`.

## Section 2: Lever A — 6-Crossing Full-Twist Hyperbolic Kohno–Drinfeld Character `C_KD^{(6)}(q)`
In `NucleonIdempotentModifiedTrace.lean` §2 (`chi3_fullTwist`, `chi111_fullTwist`), the 6-crossing
3-strand full-twist framing element `Δ_3^2 = w_0^2 = (σ_0 σ_1 σ_0)^2` acts with eigenvalues `q^{+6}`
on `(3)` and `q^{-6}` on `(1^3)`. Section 2 defines its bar-even / mirror-symmetrized Kohno–Drinfeld
hyperbolic character `C_KD^{(6)}(q) = (q^6 + q^{-6}) / 2` and establishes:
* `kdFullTwistChar_eq_avg_fullTwist`: `C_KD^{(6)}(q)` is the exact average of the full-twist
  characters `χ_{(3)}(Δ_3^2)` and `χ_{(1^3)}(Δ_3^2)` on `H_3(q)`.
* `kdFullTwistChar_sub_one`: `C_KD^{(6)}(q) - 1 = (q^6 - 1)^2 / (2 q^6)`.
* `one_lt_kdFullTwistChar` and `kdSingleWrap_lt_kdFullTwistChar`: for real `q > 1`,
  `1 < (q + q⁻¹) / 2 < (q^6 + q^{-6}) / 2`.
* `subunit_remaining_factor_of_kdFullTwist_boost` and
  `exists_elliptic_eigenphase_of_kdFullTwist_boost`:
  when a bare base `0 < Q_base` sits below `Q_target` (`F_req = Q_target / Q_base > 1`),
  multiplying the base by `C_KD^{(6)}(q)` such that `Q_target ≤ Q_base · C_KD^{(6)}(q)` moves the
  remaining ladder factor `F_rem = Q_target / (Q_base · C_KD^{(6)}(q))` into `(0, 1]`, restoring
  existence of a real elliptic eigenphase `θ ∈ [0, π]` with `cos θ = F_rem`.

Compute companion: `computations/qbeta/qbeta_pdix_cds1_cosh_gpmt_bridge_probe.py`
Witness: `computations/qbeta/qbeta-pdix-cds1-cosh-gpmt-bridge.witness.json`
-/

namespace QOU.QBeta.CoshHolonomyAndGPMTBaseBridge

open Matrix
open QOU.Machinery.H3
open QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace

/-! ## Section 1: Lever B — GPMT `(1^3)` Modified-Trace Completion of `tr_M^{z_D}` -/

section GPMTConventionDBridge

variable {K : Type*} [Field K]

/-- Positive magnitude `|d_D(S^{(1^3)})| = -d_D(S^{(1^3)}) = q^3 / ((q^2 + 1)(q^4 + q^2 + 1))`
of the Geer–Patureau-Mirand–Turaev modified quantum dimension on the Convention-D killed `(1^3)` sector. -/
def dMod111Abs (q : K) : K := -dMod111 q

/-- Explicit rational formula for `dMod111Abs q`. -/
theorem dMod111Abs_eq_div (q : K) :
    dMod111Abs q = q ^ 3 / ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1)) := by
  unfold dMod111Abs dMod111
  ring

/-- Positive-weight GPMT-completed Convention-D trace functional:
`tr_M^{D,GPMT+}(v) = tr_M^{z_D}(v) - t_D^{(1^3)}(v) = tr_M^{z_D}(v) + |d_D(S^{(1^3)})| · χ_{(1^3)}(v)`. -/
def trM_conventionD_gpmtPos (q : K) (v : Fin 6 → K) : K :=
  trM (zD q) (q - q⁻¹) v - tMod111 q v

/-- Signed GPMT-completed Convention-D trace functional:
`tr_M^{D,GPMT-}(v) = tr_M^{z_D}(v) + t_D^{(1^3)}(v) = tr_M^{z_D}(v) + d_D(S^{(1^3)}) · χ_{(1^3)}(v)`. -/
def trM_conventionD_gpmtSigned (q : K) (v : Fin 6 → K) : K :=
  trM (zD q) (q - q⁻¹) v + tMod111 q v

/-- **Three-Block Positive-Weight Wedderburn Decomposition of `tr_M^{D,GPMT+}`**:
Restoring the Convention-D killed `(1^3)` sector with positive modified quantum dimension magnitude
`|d_D(S^{(1^3)})| = q^3 / ((q^2 + 1)(q^4 + q^2 + 1))` yields a three-sector positive-weight trace sum. -/
theorem trM_conventionD_gpmtPos_eq_threeBlock_sum (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) (v : Fin 6 → K) :
    trM_conventionD_gpmtPos q v =
      (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 * chi3 q v +
      q ^ 2 / (q ^ 2 + 1) ^ 2 * chi21 q v +
      q ^ 3 / ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1)) * chi111 q v := by
  unfold trM_conventionD_gpmtPos tMod111 dMod111
  rw [trM_conventionD_eq_twoRow_sum q hq hq2 hq4 v]
  ring

/-- **Three-Block Signed Wedderburn Decomposition of `tr_M^{D,GPMT-}`**:
Adding the signed GPMT modified trace `+t_D^{(1^3)}(v)` subtracts
`q^3 / ((q^2 + 1)(q^4 + q^2 + 1)) · χ_{(1^3)}(v)` from the two-row Convention-D trace. -/
theorem trM_conventionD_gpmtSigned_eq_threeBlock_sum (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) (v : Fin 6 → K) :
    trM_conventionD_gpmtSigned q v =
      (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 * chi3 q v +
      q ^ 2 / (q ^ 2 + 1) ^ 2 * chi21 q v -
      q ^ 3 / ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1)) * chi111 q v := by
  unfold trM_conventionD_gpmtSigned tMod111 dMod111
  rw [trM_conventionD_eq_twoRow_sum q hq hq2 hq4 v]
  ring

/-- The 11-crossing production nucleon `(n - p)` normal-form difference vector
`Δ_nuc11 = neutronCoord h a - protonCoord h a` in `H_3(q)`. -/
def nucleonDiffCoord (h a : K) : Fin 6 → K :=
  neutronCoord h a - protonCoord h a

/-- Linearity of `chiNF` on vector differences `u - v`. -/
theorem chiNF_sub (x : K) (u v : Fin 6 → K) :
    chiNF x (u - v) = chiNF x u - chiNF x v := by
  unfold chiNF
  simp [Pi.sub_apply]
  ring

/-- **Symmetric `(3)` Character on the 11-Crossing Nucleon Difference `n - p`**:
At `a = -(q - q⁻¹)/2`, `χ_{(3)}(neutronCoord - protonCoord) = -(q^2 - 1)(q^2 + 1)^2 / (4 q)`. -/
theorem chi3_nucleonDiffCoord (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    chi3 q (nucleonDiffCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) =
      -(q ^ 2 - 1) * (q ^ 2 + 1) ^ 2 / (4 * q) := by
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by norm_num
    rw [this]; exact mul_ne_zero h2 h2
  unfold nucleonDiffCoord chi3
  rw [chiNF_sub]
  change chi3 q (neutronCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) -
      chi3 q (protonCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) = _
  rw [chi3_neutronCoord q hq h2, chi3_protonCoord q hq h2]
  field_simp
  ring

/-- **Antisymmetric `(1^3)` Character on the 11-Crossing Nucleon Difference `n - p`**:
At `a = -(q - q⁻¹)/2`, `χ_{(1^3)}(neutronCoord - protonCoord) = -(q^2 - 1)(q^2 + 1)^2 / (4 q^5)`. -/
theorem chi111_nucleonDiffCoord (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    chi111 q (nucleonDiffCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) =
      -(q ^ 2 - 1) * (q ^ 2 + 1) ^ 2 / (4 * q ^ 5) := by
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by norm_num
    rw [this]; exact mul_ne_zero h2 h2
  unfold nucleonDiffCoord chi111
  rw [chiNF_sub]
  change chi111 q (neutronCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) -
      chi111 q (protonCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) = _
  rw [chi111_neutronCoord q hq h2, chi111_protonCoord q hq h2]
  field_simp
  ring

/-- **Same-Sign Extremal Sector Scaling on the 11-Crossing Nucleon Difference `n - p`**:
On the 11-crossing production nucleon difference, `χ_{(1^3)}(n - p) = q^{-4} · χ_{(3)}(n - p)`,
proving that the Convention-D killed `(1^3)` sector carries the **exact same sign** as `(3)`
for all `q > 0`. -/
theorem chi111_nucleonDiffCoord_eq_q_inv_pow_four_mul_chi3 (q : K) (hq : q ≠ 0)
    (h2 : (2 : K) ≠ 0) :
    chi111 q (nucleonDiffCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) =
      q⁻¹ ^ 4 * chi3 q (nucleonDiffCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) := by
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by norm_num
    rw [this]; exact mul_ne_zero h2 h2
  rw [chi111_nucleonDiffCoord q hq h2, chi3_nucleonDiffCoord q hq h2]
  field_simp

/-- The single-crossing linear generator element `Δ_S = (h^2/2)·1 - (h/2)(σ_0 + σ_1)` in the
6-element normal-form basis `[1, σ_0, σ_1, σ_1 σ_0, σ_0 σ_1, σ_0 σ_1 σ_0]` of `H_3(q)`. -/
def deltaSNF (h : K) : Fin 6 → K :=
  ![h ^ 2 / 2, -h / 2, -h / 2, 0, 0, 0]

@[simp] theorem deltaSNF_5 (h : K) : deltaSNF h 5 = 0 := rfl

/-- Symmetric `(3)` character of `Δ_S`: `χ_{(3)}(Δ_S) = -(q^4 - 1) / (2 q^2)`. -/
theorem chi3_deltaSNF (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    chi3 q (deltaSNF (q - q⁻¹)) = -(q ^ 4 - 1) / (2 * q ^ 2) := by
  unfold chi3 chiNF
  rw [deltaSNF_5]
  simp only [deltaSNF, cons_val_zero, cons_val_one, cons_val_two, cons_val_three,
    cons_val_four, head_cons, tail_cons]
  field_simp
  ring

/-- Mixed-symmetry `(2,1)` character of `Δ_S` vanishes identically in `H_3(q)`: `χ_{(2,1)}(Δ_S) = 0`. -/
theorem chi21_deltaSNF_eq_zero (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (h2 : (2 : K) ≠ 0) :
    chi21 q (deltaSNF (q - q⁻¹)) = 0 := by
  rw [chi21, chiM_eq_closed q hq hq2]
  unfold deltaSNF
  simp only [cons_val_zero, cons_val_one, cons_val_two, cons_val_three,
    cons_val_four, head_cons, tail_cons]
  field_simp
  ring

/-- Antisymmetric `(1^3)` character of `Δ_S`: `χ_{(1^3)}(Δ_S) = +(q^4 - 1) / (2 q^2)`. -/
theorem chi111_deltaSNF (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    chi111 q (deltaSNF (q - q⁻¹)) = (q ^ 4 - 1) / (2 * q ^ 2) := by
  unfold chi111 chiNF
  rw [deltaSNF_5]
  simp only [deltaSNF, cons_val_zero, cons_val_one, cons_val_two, cons_val_three,
    cons_val_four, head_cons, tail_cons]
  field_simp
  ring

/-- **Opposite-Sign Extremal Sector Identity on `Δ_S`**:
Unlike the 9- and 11-crossing odd-length nucleon words (where `χ_{(1^3)}` and `χ_{(3)}` have the
same sign), on the linear element `Δ_S` the `(1^3)` character has the **exact opposite sign**
to `χ_{(3)}(Δ_S)`: `χ_{(1^3)}(Δ_S) = -χ_{(3)}(Δ_S)`. -/
theorem chi111_deltaSNF_eq_neg_chi3 (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    chi111 q (deltaSNF (q - q⁻¹)) = -chi3 q (deltaSNF (q - q⁻¹)) := by
  rw [chi111_deltaSNF q hq h2, chi3_deltaSNF q hq h2]
  ring

/-- Exact multiplicative enhancement factor of the signed GPMT trace `tr_M^{D,GPMT-}` on `Δ_S`:
because `χ_{(2,1)}(Δ_S) = 0` and `χ_{(1^3)}(Δ_S) = -χ_{(3)}(Δ_S)`, adding `+t_D^{(1^3)}(Δ_S)`
multiplies `tr_M^{z_D}(Δ_S)` by `1 + q^3 (q^2 + 1) / ((q^4 + 1)(q^4 + q^2 + 1))`. -/
theorem trM_conventionD_gpmtSigned_deltaSNF_ratio (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) (hq41 : q ^ 4 + 1 ≠ 0) (h2 : (2 : K) ≠ 0) :
    trM_conventionD_gpmtSigned q (deltaSNF (q - q⁻¹)) =
      (1 + q ^ 3 * (q ^ 2 + 1) / ((q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1))) *
        trM (zD q) (q - q⁻¹) (deltaSNF (q - q⁻¹)) := by
  rw [trM_conventionD_gpmtSigned_eq_threeBlock_sum q hq hq2 hq4,
      trM_conventionD_eq_twoRow_sum q hq hq2 hq4,
      chi21_deltaSNF_eq_zero q hq hq2 h2,
      chi111_deltaSNF_eq_neg_chi3 q hq h2]
  field_simp
  ring

end GPMTConventionDBridge

/-! ## Section 2: Lever A — 6-Crossing Full-Twist Hyperbolic Kohno–Drinfeld Character `C_KD^{(6)}(q)` -/

section FullTwistHyperbolicHolonomyBridge

variable {K : Type*} [Field K]

/-- The 6-crossing full-twist Kohno–Drinfeld hyperbolic character
`C_KD^{(6)}(q) = (q^6 + q^{-6}) / 2` (= `cosh(6 ln q)` for real `q > 0`), corresponding to the
6-crossing 3-strand full-twist framing element `Δ_3^2 = w_0^2 = (σ_0 σ_1 σ_0)^2`. -/
def kdFullTwistChar (q : K) : K :=
  (q ^ 6 + q⁻¹ ^ 6) / 2

/-- **Full-Twist Framing Character Average Identity on `H_3(q)`**:
`kdFullTwistChar q` is the exact average of the Aiston–Morton full-twist framing characters
`χ_{(3)}(Δ_3^2) = q^6` and `χ_{(1^3)}(Δ_3^2) = q^{-6}` on the extremal Wedderburn pair `{(3), (1^3)}`. -/
theorem kdFullTwistChar_eq_avg_fullTwist (q : K) (hq : q ≠ 0) :
    (chi3 q (fullTwistNF (q - q⁻¹)) + chi111 q (fullTwistNF (q - q⁻¹))) / 2 =
      kdFullTwistChar q := by
  unfold chi3 chi111 kdFullTwistChar
  rw [chi3_fullTwist q hq, chi111_fullTwist q hq]

/-- Exact rational square identity for the excess of `C_KD^{(6)}(q)` above `1`:
`(q^6 + q^{-6}) / 2 - 1 = (q^6 - 1)^2 / (2 q^6)`. -/
theorem kdFullTwistChar_sub_one (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    kdFullTwistChar q - 1 = (q ^ 6 - 1) ^ 2 / (2 * q ^ 6) := by
  unfold kdFullTwistChar
  field_simp
  ring

/-- Exact difference between the 6-crossing full-twist hyperbolic character `(q^6 + q^{-6}) / 2`
and the 1-crossing single-wrap character `(q + q⁻¹) / 2`:
`C_KD^{(6)}(q) - C_KD^{(1)}(q) = (q^5 - 1) (q^7 - 1) / (2 q^6)`. -/
theorem kdFullTwistChar_sub_singleWrap (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    kdFullTwistChar q - (q + q⁻¹) / 2 =
      (q ^ 5 - 1) * (q ^ 7 - 1) / (2 * q ^ 6) := by
  unfold kdFullTwistChar
  field_simp
  ring

end FullTwistHyperbolicHolonomyBridge

/-! ## Section 3: Real Positivity & Elliptic Cosine-Reachability Restoration over `ℝ` -/

section RealCosineReachabilityRestoration

/-- For every real `q > 0`, the 6-crossing full-twist character satisfies `1 ≤ C_KD^{(6)}(q)`. -/
theorem one_le_kdFullTwistChar {q : ℝ} (hq : 0 < q) :
    1 ≤ kdFullTwistChar q := by
  have hsub : kdFullTwistChar q - 1 = (q ^ 6 - 1) ^ 2 / (2 * q ^ 6) :=
    kdFullTwistChar_sub_one q (ne_of_gt hq) two_ne_zero
  have hpos : 0 ≤ (q ^ 6 - 1) ^ 2 / (2 * q ^ 6) :=
    div_nonneg (sq_nonneg _) (mul_nonneg (by norm_num) (pow_nonneg hq.le 6))
  linarith

/-- For every real `q > 1`, the 6-crossing full-twist character satisfies `1 < C_KD^{(6)}(q)`
and strictly exceeds the single-wrap Kohno–Drinfeld character `(q + q⁻¹) / 2`. -/
theorem kdSingleWrap_lt_kdFullTwistChar {q : ℝ} (hq : 1 < q) :
    (q + q⁻¹) / 2 < kdFullTwistChar q := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have hdiff : kdFullTwistChar q - (q + q⁻¹) / 2 =
      (q ^ 5 - 1) * (q ^ 7 - 1) / (2 * q ^ 6) :=
    kdFullTwistChar_sub_singleWrap q (ne_of_gt hq0) two_ne_zero
  have hq5 : 1 < q ^ 5 := one_lt_pow₀ hq (by norm_num)
  have hq7 : 1 < q ^ 7 := one_lt_pow₀ hq (by norm_num)
  have hnum : 0 < (q ^ 5 - 1) * (q ^ 7 - 1) :=
    mul_pos (sub_pos.mpr hq5) (sub_pos.mpr hq7)
  have hden : 0 < 2 * q ^ 6 := mul_pos (by norm_num) (pow_pos hq0 6)
  have hpos : 0 < kdFullTwistChar q - (q + q⁻¹) / 2 := by
    rw [hdiff]
    exact div_pos hnum hden
  linarith

/-- **Sub-Unit Remaining Factor Restoration via 6-Crossing Full-Twist Hyperbolic Boost**:
If a positive base prediction `0 < qBase` undershoots a positive target `0 < qTarget`
(so the bare required factor `qTarget / qBase > 1` is unreachable by an elliptic cosine `cos θ ≤ 1`),
but the 6-crossing full-twist hyperbolic framing factor `kdFullTwistChar q` lifts the base at least
to `qTarget` (`qTarget ≤ qBase * kdFullTwistChar q`), then the remaining factor
`F_rem = qTarget / (qBase * kdFullTwistChar q)` lies strictly in `(0, 1]`. -/
theorem subunit_remaining_factor_of_kdFullTwist_boost {qBase qTarget q : ℝ}
    (hBase : 0 < qBase) (hTarget : 0 < qTarget) (hq : 0 < q)
    (hBoost : qTarget ≤ qBase * kdFullTwistChar q) :
    0 < qTarget / (qBase * kdFullTwistChar q) ∧
      qTarget / (qBase * kdFullTwistChar q) ≤ 1 := by
  have hkd : 1 ≤ kdFullTwistChar q := one_le_kdFullTwistChar hq
  have hkd_pos : 0 < kdFullTwistChar q := lt_of_lt_of_le zero_lt_one hkd
  have hDen : 0 < qBase * kdFullTwistChar q := mul_pos hBase hkd_pos
  exact ⟨div_pos hTarget hDen, (div_le_one hDen).mpr hBoost⟩

/-- **Elliptic Eigenphase Existence After 6-Crossing Full-Twist Hyperbolic Boost**:
Under the hypotheses of `subunit_remaining_factor_of_kdFullTwist_boost`, there exists a real
elliptic eigenphase `θ ∈ [0, π]` such that `cos θ = qTarget / (qBase * kdFullTwistChar q)`,
removing the `cos θ ≤ 1` obstruction on the full-twist framed Convention-D base. -/
theorem exists_elliptic_eigenphase_of_kdFullTwist_boost {qBase qTarget q : ℝ}
    (hBase : 0 < qBase) (hTarget : 0 < qTarget) (hq : 0 < q)
    (hBoost : qTarget ≤ qBase * kdFullTwistChar q) :
    ∃ θ : ℝ, 0 ≤ θ ∧ θ ≤ Real.pi ∧
      Real.cos θ = qTarget / (qBase * kdFullTwistChar q) := by
  obtain ⟨hPos, hLeOne⟩ :=
    subunit_remaining_factor_of_kdFullTwist_boost hBase hTarget hq hBoost
  refine ⟨Real.arccos (qTarget / (qBase * kdFullTwistChar q)),
    Real.arccos_nonneg _, Real.arccos_le_pi _, ?_⟩
  exact Real.cos_arccos (by linarith) hLeOne

end RealCosineReachabilityRestoration

end QOU.QBeta.CoshHolonomyAndGPMTBaseBridge
