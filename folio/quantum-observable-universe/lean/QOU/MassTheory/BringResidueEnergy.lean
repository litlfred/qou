/-
# The residue dependence of the Bring energy

Owner, 2026-10-12: "derive the residue dependence of the Bring energy" (bean `qou-jfx8`). Inputs, all
already on record: the canonical fibre linking residue `ℓ = −1/6` (geodesic ruling,
`BringUTContactChirality` §9), the convolution flow `σ^t = q^t P_S + q^{−t} e^{iπt} P_A` with branch
`σ ↔ e^{+iπ}` (`ConvolutionFlowFibre`), the single-segment collision state (Part A of
`SegmentCollisionDatum`: the collision sees only the Markov value of the bridge letter), and the
convention-D channel weights `w_S = (q⁴+q²+1)/(q²+1)²`, `w_A = q²/(q²+1)²` (Part B).

## Where the residue enters (the modelling step, stated)

A full twist `σ²` adds linking number `1` between two strands. Two fibre strands of `UT(Σ₄)` have
ambient linking `ℓ`, so in the local braid model the ambient linking enters as the fractional twist
`σ^{2ℓ}`, i.e. the convolution flow at time `t = 2ℓ`. For the abelian (linking/writhe) part this is
exact: linking is additive and a local twist and an ambient linking contribute the same way. Using
the Hecke flow `σ^t` for the full non-abelian part is the identification made here; it is a
modelling step, not a theorem. **Tested (owner request 2026-10-12, `fractional_twist_consistency_probe.py`,
7/7):** on every H₃/H₆ block the fractional twist obeys the group law, `(σ^{2ℓ})⁶ = σ^{−2}`, far
commutativity, and the trace-level Markov property (`σ^t ∈ span{1, σ}`); but the BRAID RELATION FAILS for
fractional `t` on the 2-dim block `(2,1)` (defect 0.569 at `t = ±1/3`, exactly 0 at `t = 1`). So `σ^{2ℓ}` is
consistent as a single-bridge object and is NOT a braid-group action: fractional twists on two adjacent
pairs at once are not defined by this step. Consistency (`six_pairs_full_twist`): `e·ℓ = 6·(−1/6) = −1`, so the
six fibre pairs in the torsion class make one full negative twist, `σ^{−2}`.

## The energy (derived, given that step)

With the bridge state of Part A, the Bring term is `E(ℓ) = −log μ(2ℓ)` with the real Markov value

    μ(t) = q^t w_S + q^{−t} cos(π t) w_A

(the corpus's binding form `−α log tr`; the real part is the branch-independent part). Then:

* `mirror_eq_bar` — **orientation reversal is the bar involution**: `μ_q(−t) = μ_{q⁻¹}(t)`. This is the
  joint symmetry (orientation, `q ↦ q⁻¹`), now proved for this energy.
* `classical_limit_achiral` — at `q = 1` the energy is even in `ℓ`: there is no chirality in the
  classical limit.
* `chiral_split` — **the chiral part factors**: `μ(t) − μ(−t) = (q^t − q^{−t})(w_S − cos(πt) w_A)`.
* `chiral_factor_pos_conventionD` — under convention D, `w_S − c·w_A > 0` for every `c ≤ 1`, so the
  chirality vanishes only when `q^t = q^{−t}`: **for every `q > 0, q ≠ 1` and `ℓ ≠ 0` the Bring
  energy is chiral**, with the sign of `μ(2ℓ) − μ(−2ℓ)` equal to the sign of `ℓ·ln q`.

At the canonical point (`q₀ > 1`, `ℓ = −1/6`, `t = −1/3`), `μ(−1/3) < μ(+1/3)`, so `E(−1/6) > E(+1/6)`.
Values are in `bring_residue_energy_probe.py`. Nothing is fitted: no parameter is adjusted, and the
only inputs are `q₀`, the two convention-D weights, and `ℓ`.

**Not derived:** the angle dependence `E(θ, ℓ)` at the collision (which crossing angle realises which
`t`), and the overall scale `α`.

§7c: over `ℝ` (real powers, `cos`, order).

-- Ref: [manuscript] bean qou-jfx8; BringUTContactChirality §6–9; ConvolutionFlowFibre;
   SegmentCollisionDatum Parts A, B, G. Linking additivity: standard.
-/
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Analysis.SpecialFunctions.ExpDeriv

namespace QOU.MassTheory.BringResidueEnergy

open Real

/-- **Six fibre pairs make one full negative twist**: `e·ℓ = 6·(−1/6) = −1`, i.e. `6·(2ℓ) = −2`. -/
theorem six_pairs_full_twist : (6 : ℚ) * (2 * (-1 / 6)) = -2 := by norm_num

/-- The real Markov value of the convolution-flow letter `σ^t` at the bridge. -/
noncomputable def mu (q wS wA t : ℝ) : ℝ := q ^ t * wS + q ^ (-t) * cos (π * t) * wA

/-- **Orientation reversal is the bar involution**: `μ_q(−t) = μ_{q⁻¹}(t)`. -/
theorem mirror_eq_bar (q wS wA t : ℝ) (hq : 0 < q) : mu q wS wA (-t) = mu q⁻¹ wS wA t := by
  unfold mu
  rw [neg_neg, Real.inv_rpow hq.le, Real.inv_rpow hq.le, Real.rpow_neg hq.le, inv_inv, mul_neg,
    cos_neg]

/-- **No chirality at `q = 1`.** -/
theorem classical_limit_achiral (wS wA t : ℝ) : mu 1 wS wA (-t) = mu 1 wS wA t := by
  unfold mu; simp [Real.one_rpow, cos_neg]

/-- **The chiral part factors**: `μ(t) − μ(−t) = (q^t − q^{−t})(w_S − cos(πt) w_A)`. -/
theorem chiral_split (q wS wA t : ℝ) :
    mu q wS wA t - mu q wS wA (-t) = (q ^ t - q ^ (-t)) * (wS - cos (π * t) * wA) := by
  unfold mu; rw [neg_neg, mul_neg, cos_neg]; ring

/-- **Under convention D the second factor is positive** for every `c ≤ 1`:
`w_S − c w_A = (q⁴ + (1 − c) q² + 1)/(q² + 1)²`. -/
theorem chiral_factor_pos_conventionD (q c : ℝ) (hc : c ≤ 1) :
    0 < (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 - c * (q ^ 2 / (q ^ 2 + 1) ^ 2) := by
  have hd : 0 < (q ^ 2 + 1) ^ 2 := by positivity
  rw [← mul_div_assoc, div_sub_div_same]
  apply div_pos _ hd
  nlinarith [sq_nonneg (q ^ 2), sq_nonneg q]

/-- **The first factor has the sign of `t · ln q`**: for `q > 1` and `t < 0`, `q^t − q^{−t} < 0`. -/
theorem chiral_sign_canonical (q t : ℝ) (hq : 1 < q) (ht : t < 0) : q ^ t - q ^ (-t) < 0 := by
  have h1 : q ^ t < q ^ (-t) := Real.rpow_lt_rpow_of_exponent_lt hq (by linarith)
  linarith

/-- **At the canonical point the Bring energy is chiral**: under convention D, for `q > 1` and
`t = 2ℓ < 0`, `μ(t) < μ(−t)` (so `E(ℓ) = −log μ(2ℓ)` is the larger of the two). -/
theorem canonical_mu_lt_mirror (q t : ℝ) (hq : 1 < q) (ht : t < 0) :
    mu q ((q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2) (q ^ 2 / (q ^ 2 + 1) ^ 2) t
      < mu q ((q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2) (q ^ 2 / (q ^ 2 + 1) ^ 2) (-t) := by
  have hs := chiral_split q ((q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2) (q ^ 2 / (q ^ 2 + 1) ^ 2) t
  have h1 := chiral_sign_canonical q t hq ht
  have h2 := chiral_factor_pos_conventionD q (cos (π * t)) (cos_le_one _)
  nlinarith [mul_neg_of_neg_of_pos h1 h2]

/-! ## The relative minimum (owner's principle): a preferred twist direction

Owner (2026-10-12): the collision takes the twist that makes the rotational energy a relative minimum.
The ambient residue supplies flow time `2ℓ`; the collision adds `s`, total `t = s + 2ℓ`; minimising
`E = −log μ` maximises `μ`.

* `hasDerivAt_mu_zero`: `μ'(0) = ln q · (w_S − w_A)`.
* `mu_increasing_at_zero_conventionD`: under convention D, `w_S − w_A = (q⁴+1)/(q²+1)² > 0`, so for
  `q > 1` `μ` is increasing at `t = 0`. The relative minimum of `E` therefore sits at a positive flow
  time `t* > 0`: a PREFERRED twist direction (the `σ` side in the canonical orientation), and it
  vanishes at `q = 1` (`mu_deriv_zero_classical`). The location `t* ∈ (0, 1/2)` and its value are
  computed in `bring_residue_energy_probe.py`.
* Through `ConvolutionFlowFibre` (a flow time `s` turns the relative direction by `π s`), the
  collision's turning angle is `π (t* − 2ℓ)`. That reading is the modelling identification of that
  file, restated, not new. -/

/-- `μ` in exponential form, `q > 0`. -/
theorem mu_exp_form (q wS wA t : ℝ) (hq : 0 < q) :
    mu q wS wA t = exp (log q * t) * wS + exp (-(log q * t)) * cos (π * t) * wA := by
  unfold mu
  rw [Real.rpow_def_of_pos hq, Real.rpow_def_of_pos hq]
  ring_nf

/-- **`μ'(0) = ln q · (w_S − w_A)`.** -/
theorem hasDerivAt_mu_zero (q wS wA : ℝ) (hq : 0 < q) :
    HasDerivAt (mu q wS wA) (log q * (wS - wA)) 0 := by
  have hf : (mu q wS wA) = fun t => exp (log q * t) * wS + exp (-(log q * t)) * cos (π * t) * wA := by
    funext t; exact mu_exp_form q wS wA t hq
  rw [hf]
  have h1 : HasDerivAt (fun t : ℝ => exp (log q * t)) (exp (log q * 0) * log q) 0 :=
    ((hasDerivAt_id 0).const_mul (log q)).exp.congr_deriv (by simp)
  have h2 : HasDerivAt (fun t : ℝ => exp (-(log q * t))) (exp (-(log q * 0)) * (-log q)) 0 :=
    (((hasDerivAt_id 0).const_mul (log q)).neg).exp.congr_deriv (by simp)
  have h3 : HasDerivAt (fun t : ℝ => cos (π * t)) (-sin (π * 0) * π) 0 :=
    (((hasDerivAt_id 0).const_mul π).cos).congr_deriv (by simp)
  have := ((h1.mul_const wS).add ((h2.mul h3).mul_const wA))
  convert this using 1
  simp; ring

/-- **Increasing at `t = 0` under convention D for `q > 1`.** -/
theorem mu_increasing_at_zero_conventionD (q : ℝ) (hq : 1 < q) :
    0 < log q * ((q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 - q ^ 2 / (q ^ 2 + 1) ^ 2) := by
  apply mul_pos (Real.log_pos hq)
  rw [div_sub_div_same]
  apply div_pos _ (by positivity)
  nlinarith [sq_nonneg (q ^ 2)]

/-- **No preferred direction at `q = 1`.** -/
theorem mu_deriv_zero_classical (wS wA : ℝ) : log 1 * (wS - wA) = 0 := by simp

end QOU.MassTheory.BringResidueEnergy
