/-
Copyright (c) 2026 QOU Authors. All rights reserved.
Formalization for beans under qou-10v9:
  - qou-e58e: Bar-involution interface defect d(q) + d(1/q) numerator and extensive/intensive mirror split
  - qou-gcmn: EM-linking B_pp decline with A and additive log-slope confound identity
  - qou-vbyi: Spin-singlet tensor-operator S_12(n) = 3(1 - |n|^2) scalar invariance and triplet level repulsion
  - qou-vtlj: Neutron Hopf-link crossing ladder C(k) = 9 + 2k (k=1 gives 11, not 13) and 4 distinct Delta_net values
  - qou-xy5f: Canonical ordering DOF z_mig(q) = q^3/(q^2+1) vs z_D(q) = q^2/(q^2+1) convention shift
-/

namespace QOU.Eightfold.BarParityIsospinSplitBppConfoundSingletTensorInvarianceDeltaFourValuesAndOrderingDofShift

/-!
## 1. Bean `qou-e58e`: Bar-Involution Interface Defect and Extensive/Intensive Mirror Split
Under bar involution (`q ↦ 1/q`), the colour-weighted interface shift `d(q) = -h(q) * (1/2 - f(q)/4)`
fails to be bar-odd because `f(1/q) = -q^2 * f(q)`, leaving the exact positive bar-parity defect
`d(q) + d(1/q) = (q - 1)^4 * (q + 1)^2 * (q^2 + 1)^2 / (12 * q^5)`. Moreover, the free mirror log-ratio
`S_free(A, c) = A * c` is purely extensive (first difference `c`), while the atom mirror log-ratio
`S_atom(A, c, δ) = A * c - 2 * δ` has the same first difference `c` and constant intensive offset `2 * δ`.
-/

/-- Homogeneous numerator `(q - S)^4 * (q + S)^2 * (q^2 + S^2)^2` of `12 * q^5 * (d(q) + d(1/q))`. -/
def barParityInterfaceDefectNumerator (scale q : Int) : Int :=
  ((q - scale) * (q - scale)) * ((q - scale) * (q - scale)) *
    ((q + scale) * (q + scale)) * ((q * q + scale * scale) * (q * q + scale * scale))

/-- Free mirror log-ratio `S_free(A, c) = A * c`. -/
def mirrorLogRatioFree (massNumberA slopeC : Int) : Int :=
  massNumberA * slopeC

/-- Atom mirror log-ratio `S_atom(A, c, δ) = A * c - 2 * δ`. -/
def mirrorLogRatioAtom (massNumberA slopeC delta : Int) : Int :=
  massNumberA * slopeC - 2 * delta

/-- Universal extensive/intensive split theorem: both `S_free` and `S_atom` have identical first
    difference `slopeC` in `A`, and their difference `S_free(A) - S_atom(A)` is the `A`-independent
    intensive constant `2 * δ`. -/
theorem mirror_log_ratio_extensive_intensive_split (massNumberA slopeC delta : Int) :
    mirrorLogRatioFree (massNumberA + 1) slopeC - mirrorLogRatioFree massNumberA slopeC = slopeC ∧
    mirrorLogRatioAtom (massNumberA + 1) slopeC delta -
      mirrorLogRatioAtom massNumberA slopeC delta = slopeC ∧
    mirrorLogRatioFree massNumberA slopeC - mirrorLogRatioAtom massNumberA slopeC delta =
      2 * delta := by
  refine ⟨?_, ?_, ?_⟩
  · dsimp [mirrorLogRatioFree]
    rw [Int.add_mul, Int.one_mul]
    omega
  · dsimp [mirrorLogRatioAtom]
    rw [Int.add_mul, Int.one_mul]
    omega
  · dsimp [mirrorLogRatioFree, mirrorLogRatioAtom]
    omega

/-- Concrete verification that the bar-parity interface defect numerator vanishes at `q = S` (`q = 1`)
    and is strictly positive at `q_0 = 1109980` (`S = 1000000`). -/
theorem bar_parity_interface_defect_vanishes_at_one_and_pos_at_q0 :
    barParityInterfaceDefectNumerator 1000000 1000000 = 0 ∧
    0 < barParityInterfaceDefectNumerator 1000000 1109980 := by
  decide

/-!
## 2. Bean `qou-gcmn`: EM-Linking `B_pp` Confound Decline and Additive Log-Slope Identity
For `κ = F(α)`, `α ~ A^p`, and `B_pp ~ A^(-δ)`, the observed mirror log-slope is the sum
`slope_obs = s * p + δ`. Because `B_pp(A)` strictly declines with `A` (`2.128360946 → 1.966342608 → 1.851585614` MeV
at `A = 2, 3, 4`), `δ > 0` acts as an additive positive bias so `s * p = slope_obs - δ < slope_obs`,
with local drift `δ(3 → 4) = 0.20903` exceeding `80%` of `slope_obs = 0.26050`.
-/

/-- Observed mirror log-slope `s * p + δ` in scaled integer units. -/
def observedMirrorLogSlope (spProduct deltaDrift : Int) : Int :=
  spProduct + deltaDrift

/-- Universal theorem: whenever the `B_pp` decline exponent `δ > 0`, the true geometric exponent
    product `s * p = slope_obs - δ` is strictly smaller than `slope_obs`. -/
theorem bpp_decline_biases_observed_log_slope_upward (spProduct deltaDrift : Int)
    (hDelta : 0 < deltaDrift) :
    observedMirrorLogSlope spProduct deltaDrift - deltaDrift = spProduct ∧
    spProduct < observedMirrorLogSlope spProduct deltaDrift := by
  dsimp [observedMirrorLogSlope]
  omega

/-- Concrete verification of the strict decline of `B_pp(A)` at `A = 2, 3, 4` (`10^9`-scaled MeV:
    `2128360946 > 1966342608 > 1851585614`), strict increase of `κ_corr(A)` (`10823957827 < 11494801700`),
    and that `δ(3 → 4) = 20903` exceeds `4 / 5` (`80%`) of `slope_obs = 26050`. -/
theorem bpp_per_bond_decline_and_eighty_percent_confound_share :
    (2128360946 : Int) > 1966342608 ∧
    (1966342608 : Int) > 1851585614 ∧
    (10823957827 : Int) < 11494801700 ∧
    5 * (20903 : Int) > 4 * 26050 ∧
    (26050 : Int) - 20903 = 5147 := by
  decide

/-!
## 3. Bean `qou-vbyi`: Spin-Singlet Tensor Invariance and Triplet Level Repulsion
On the spin singlet `|ud⟩ - |du⟩` (`S = 0`), `σ₁ · σ₂ = -3` and `(σ₁ · n)(σ₂ · n) = -|n|^2`, so
`S₁₂(n) = 3 * (σ₁ · n)(σ₂ · n) - (σ₁ · σ₂) = 3 * (1 - |n|^2)`, which vanishes identically for every
unit vector `|n|^2 = 1`. On the spin triplet (`S = 1`), any `2 × 2` symmetric mixing `t ≠ 0` between
`E_S` and `E_D` has positive off-diagonal square `t^2 > 0`, shifting the ground level downward.
-/

/-- Action of the tensor operator `S₁₂(n)` on the spin singlet in scale `S_norm = |n|^2`:
    `3 * (-normSq) - (-3 * unitSq) = 3 * (unitSq - normSq)`. -/
def singletTensorOperatorScalar (unitSq normSq : Int) : Int :=
  3 * (-normSq) - (-3 * unitSq)

/-- Off-diagonal level-repulsion product `(E_S - λ) * (E_D - λ) - t^2` of the coupled `2 × 2`
    `${}^3S_1$–${}^3D_1` characteristic polynomial. -/
def coupledTripletSecularResidual (eS eD t lam : Int) : Int :=
  (eS - lam) * (eD - lam) - t * t

/-- Universal theorem: on the unit sphere (`normSq = unitSq`), `S₁₂(n)` acts as `0` on the spin
    singlet for every direction `n`. -/
theorem singlet_tensor_operator_vanishes_on_unit_sphere (unitSq normSq : Int)
    (hUnit : normSq = unitSq) :
    singletTensorOperatorScalar unitSq normSq = 0 := by
  dsimp [singletTensorOperatorScalar]
  rw [hUnit]
  omega

/-- Universal theorem: at the uncoupled `${}^3S_1` energy `λ = E_S`, the secular residual is `-t^2`,
    which is strictly negative whenever `t ≠ 0` (proving that `λ = E_S` is no longer an eigenvalue
    and the coupled ground eigenvalue is pushed strictly below `E_S`). -/
theorem triplet_secular_residual_negative_at_uncoupled_energy (eS eD t : Int)
    (ht : t ≠ 0) :
    coupledTripletSecularResidual eS eD t eS = -(t * t) ∧
    coupledTripletSecularResidual eS eD t eS < 0 := by
  have hId : coupledTripletSecularResidual eS eD t eS = -(t * t) := by
    dsimp [coupledTripletSecularResidual]
    have hZero : eS - eS = 0 := by omega
    rw [hZero, Int.zero_mul]
    omega
  refine ⟨hId, ?_⟩
  rw [hId]
  have hSqPos : 0 < t * t := by
    rcases Int.lt_trichotomy t 0 with hNeg | rfl | hPos
    · exact Int.mul_pos_of_neg_of_neg hNeg hNeg
    · contradiction
    · exact Int.mul_pos hPos hPos
  omega

/-!
## 4. Bean `qou-vtlj`: Neutron Hopf-Link Crossing Ladder and Four Distinct `Delta_net` Values
Built from `B_3 = (σ_0(σ_1 - h))^3` (`6` base crossings), `3` typed quark shifts, and `k` Hopf links
(`2 * k` gluon crossings), the total crossing count is `C(k) = 9 + 2 * k`. Thus `k = 1` (which
reproduces the stated neutron net `+0.7975664`) has `C(1) = 11` crossings, whereas `C(2) = 13`
gives `1.235859`. Furthermore, the four corpus `Delta_net` values (`-1872072`, `-2089000`,
`-2137638`, `-2331977` in `10^-7` units) are strictly ordered and pairwise distinct.
-/

/-- Total crossing count `C(k) = 6 + 3 + 2 * k = 9 + 2 * k` for `k` Hopf links. -/
def neutronHopfLadderCrossings (hopfCountK : Int) : Int :=
  6 + 3 + 2 * hopfCountK

/-- Universal theorem: each additional Hopf link adds `2` crossings (`C(k + 1) - C(k) = 2`). -/
theorem neutron_hopf_ladder_step_two (hopfCountK : Int) :
    neutronHopfLadderCrossings (hopfCountK + 1) - neutronHopfLadderCrossings hopfCountK = 2 := by
  dsimp [neutronHopfLadderCrossings]
  rw [Int.mul_add]
  omega

/-- Concrete verification that `C(0) = 9`, `C(1) = 11` (not `13`), `C(2) = 13`, `C(3) = 15`,
    and that the four corpus `Delta_net` values in `10^-7` units are strictly ordered with total
    spread `2331977 - 1872072 = 459905`. -/
theorem neutron_crossing_count_eleven_and_four_delta_net_spread :
    neutronHopfLadderCrossings 0 = 9 ∧
    neutronHopfLadderCrossings 1 = 11 ∧
    neutronHopfLadderCrossings 1 ≠ 13 ∧
    neutronHopfLadderCrossings 2 = 13 ∧
    neutronHopfLadderCrossings 3 = 15 ∧
    (-2331977 : Int) < -2137638 ∧
    (-2137638 : Int) < -2089000 ∧
    (-2089000 : Int) < -1872072 ∧
    (-1872072 : Int) - (-2331977) = 459905 := by
  decide

/-!
## 5. Bean `qou-xy5f`: Canonical Ordering DOF `z_mig(q) = q^3/(q^2+1)` vs `z_D(q) = q^2/(q^2+1)` Shift
In `canonical_ordering_dof_probe.py` Part 6, the closed form migrated to `z_mig(q) = q^3 / (q^2 + 1)`
while the eight full-trace readings remained at their pre-migration values. Over common denominator
`S * (q^2 + S^2)`, the numerator difference between `z_mig(q)` and `z_D(q)` is `q^2 * (q - S)`,
which is strictly positive for all `q > S > 0`.
-/

/-- Numerator `q^3` of `z_mig(q) = q^3 / (q^2 + 1)` over `S * (q^2 + S^2)`. -/
def zMigratedNumerator (q : Int) : Int :=
  q * (q * q)

/-- Numerator `S * q^2` of `z_D(q) = q^2 / (q^2 + 1)` over `S * (q^2 + S^2)`. -/
def zCanonicalDNumerator (scale q : Int) : Int :=
  scale * (q * q)

/-- Universal factorization: `zMigratedNumerator q - zCanonicalDNumerator S q = (q - S) * q^2`. -/
theorem z_migrated_minus_canonical_d_factorization (scale q : Int) :
    zMigratedNumerator q - zCanonicalDNumerator scale q = (q - scale) * (q * q) := by
  dsimp [zMigratedNumerator, zCanonicalDNumerator]
  rw [Int.sub_mul]

/-- Concrete verification at `q_0 = 1109980` (`S = 1000000`) that `z_mig > z_D` and that in Part 6
    the two full-trace pipelines agree with each other within `24` (`T_npn_over_pnn`: `136037 - 136013 = 24`)
    and `14` (`He3_pnp_over_ppn`: `79080 - 79066 = 14`) while differing from the migrated closed form
    (`125898` and `82939`) by `10115` and `3859` (`> 250x` the inter-pipeline spread). -/
theorem ordering_dof_part6_pipeline_agreement_vs_closed_form_shift :
    0 < zMigratedNumerator 1109980 - zCanonicalDNumerator 1000000 1109980 ∧
    (136037 : Int) - 136013 = 24 ∧
    (136013 : Int) - 125898 = 10115 ∧
    400 * ((136037 : Int) - 136013) < (136013 : Int) - 125898 ∧
    (79080 : Int) - 79066 = 14 ∧
    (82939 : Int) - 79080 = 3859 ∧
    250 * ((79080 : Int) - 79066) < (82939 : Int) - 79080 := by
  decide

end QOU.Eightfold.BarParityIsospinSplitBppConfoundSingletTensorInvarianceDeltaFourValuesAndOrderingDofShift
