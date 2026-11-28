import QOU.Nuclear.NucleonSplitGibbsEnergy
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.Analysis.Calculus.Deriv.Inv

/-!
# The Gibbs map of the nucleon split: the analytic part

Split off `QOU.Nuclear.NucleonSplitGibbsEnergy` at the transcendental boundary (bean `qou-gfsr`);
names and namespace unchanged. Here: `log Z` of the two sectors and its split for every common
factor (`logZ_split`, `logZ_split_hasDerivAt`), the free-energy split `fSplit` and `tsSplit`, the
derivatives of the four corpus temperatures, and the comparisons of the CAL-1 internal-energy
splits with their free-energy splits (`uT_lt_fT`, `uTower_lt_fTower`). The rational closed forms
of `uSplit` stay in `QOU.Nuclear.NucleonSplitGibbsEnergy`.
-/

namespace QOU.QBeta.NucleonSplitGibbsEnergy

open Real

/-- `log Z` of the proton (`K = q`) and neutron (`K = q⁻¹`) sectors with common factor `s`. -/
noncomputable def logZp (s : ℝ → ℝ) (q : ℝ) : ℝ := Real.log (q * s q)
noncomputable def logZn (s : ℝ → ℝ) (q : ℝ) : ℝ := Real.log (q⁻¹ * s q)

/-- **The common factor drops out at every order:** `log Z_n − log Z_p = −2 log q`. -/
theorem logZ_split (s : ℝ → ℝ) (q : ℝ) (hq : 0 < q) (hs : 0 < s q) :
    logZn s q - logZp s q = -2 * Real.log q := by
  unfold logZn logZp
  rw [Real.log_mul (inv_ne_zero hq.ne') hs.ne', Real.log_mul hq.ne' hs.ne', Real.log_inv]
  ring

/-- **Its derivative is `−2/q`, whatever `s` is** (positive on a neighbourhood of `q`). -/
theorem logZ_split_hasDerivAt (s : ℝ → ℝ) (q : ℝ) (hq : 0 < q)
    (hs : ∀ᶠ x in nhds q, 0 < s x) :
    HasDerivAt (fun x => logZn s x - logZp s x) (-2 / q) q := by
  have hpos : ∀ᶠ x in nhds q, 0 < x := lt_mem_nhds hq
  have heq : (fun x => logZn s x - logZp s x) =ᶠ[nhds q] fun x => -2 * Real.log x := by
    filter_upwards [hs, hpos] with x hsx hx
    exact logZ_split s x hx hsx
  have hd : HasDerivAt (fun x => -2 * Real.log x) (-2 * q⁻¹) q :=
    (Real.hasDerivAt_log hq.ne').const_mul (-2)
  have : (-2 : ℝ) * q⁻¹ = -2 / q := by ring
  rw [this] at hd
  exact hd.congr_of_eventuallyEq heq

/-- Internal-energy split `ΔU = −d(log Z_n − log Z_p)/dβ = −(−2/q)/b'(q)` on `ℝ`. -/
noncomputable def uSplit (b' q : ℝ) : ℝ := -(-2 / q) / b'

theorem uNat_eq (q : ℝ) (hq : 1 < q) :
    uSplit (-1 / (q - 1) ^ 2) q = -2 * (q - 1) ^ 2 / q := by
  have h1 : q - 1 ≠ 0 := by linarith
  have h0 : q ≠ 0 := by linarith
  unfold uSplit; field_simp

theorem uNat_neg (q : ℝ) (hq : 1 < q) : uSplit (-1 / (q - 1) ^ 2) q < 0 := by
  rw [uNat_eq q hq]
  have h1 : 0 < q - 1 := by linarith
  have h0 : 0 < q := by linarith
  have : 0 < 2 * (q - 1) ^ 2 / q := div_pos (by positivity) h0
  linarith [show -2 * (q - 1) ^ 2 / q = -(2 * (q - 1) ^ 2 / q) by ring]

theorem uT_eq (q : ℝ) (hq : 1 < q) : uSplit (2 * q - 1) q = 2 / (q * (2 * q - 1)) := by
  have h0 : q ≠ 0 := by linarith
  have h2 : 2 * q - 1 ≠ 0 := by linarith
  unfold uSplit; field_simp

theorem uTower_eq (q : ℝ) (hq : 1 < q) :
    uSplit ((2 * q ^ 2 - 1) / q ^ 2) q = 2 * q / (2 * q ^ 2 - 1) := by
  have h0 : q ≠ 0 := by linarith
  have h2 : 2 * q ^ 2 - 1 ≠ 0 := by nlinarith
  unfold uSplit; field_simp

/-- Free-energy split `ΔF = −(log Z_n − log Z_p)/β` with `β = b`. -/
noncomputable def fSplit (b q : ℝ) : ℝ := -(-2 * Real.log q) / b

/-- Sign convention: `F = U − TS`, so `TΔS = ΔU − ΔF`. -/
noncomputable def tsSplit (b b' q : ℝ) : ℝ := uSplit b' q - fSplit b q

/-! ## The four corpus temperatures, with their derivatives checked -/

theorem hasDerivAt_bD (q : ℝ) (hq : 0 < q) : HasDerivAt Real.log (1 / q) q := by
  simpa [one_div] using Real.hasDerivAt_log hq.ne'

theorem hasDerivAt_bNat (q : ℝ) (hq : 1 < q) :
    HasDerivAt (fun x => x / (x - 1)) (-1 / (q - 1) ^ 2) q := by
  have h1 : q - 1 ≠ 0 := by linarith
  have := (hasDerivAt_id q).div ((hasDerivAt_id q).sub_const 1) h1
  convert this using 1
  simp only [id]
  field_simp
  ring

theorem hasDerivAt_bT (q : ℝ) : HasDerivAt (fun x => x * (x - 1)) (2 * q - 1) q := by
  have := (hasDerivAt_id q).mul ((hasDerivAt_id q).sub_const 1)
  convert this using 1
  simp only [id]
  ring

theorem hasDerivAt_bTower (q : ℝ) (hq : 0 < q) :
    HasDerivAt (fun x => (x - 1) * (2 * x - 1) / x) ((2 * q ^ 2 - 1) / q ^ 2) q := by
  have hn : HasDerivAt (fun x => (x - 1) * (2 * x - 1)) (1 * (2 * q - 1) + (q - 1) * 2) q := by
    have := ((hasDerivAt_id q).sub_const 1).mul (((hasDerivAt_id q).const_mul 2).sub_const 1)
    convert this using 1
    simp [id]
  have := hn.div (hasDerivAt_id q) hq.ne'
  convert this using 1
  simp only [id]
  field_simp
  ring

/-- **Dictionary temperature `β = log q`: `ΔU = ΔF = 2` and `TΔS = 0`.** -/
theorem dictionary_U_eq_F (q : ℝ) (hq : 1 < q) :
    uSplit (1 / q) q = 2 ∧ fSplit (Real.log q) q = 2 ∧ tsSplit (Real.log q) (1 / q) q = 0 := by
  have hq0 : q ≠ 0 := by linarith
  have hl : Real.log q ≠ 0 := (Real.log_pos hq).ne'
  have hU : uSplit (1 / q) q = 2 := by unfold uSplit; field_simp
  have hF : fSplit (Real.log q) q = 2 := by unfold fSplit; field_simp
  refine ⟨hU, hF, ?_⟩
  unfold tsSplit; rw [hU, hF]; ring

/-- `log q > 1 − 1/q` for `q > 1`. -/
theorem log_gt_one_sub_inv (q : ℝ) (hq : 1 < q) : 1 - q⁻¹ < Real.log q := by
  have hq0 : 0 < q := by linarith
  have hi : 0 < q⁻¹ := inv_pos.mpr hq0
  have hne : q⁻¹ ≠ 1 := by
    intro h; have := inv_lt_one_of_one_lt₀ hq; linarith
  have := Real.log_lt_sub_one_of_pos hi hne
  rw [Real.log_inv] at this
  linarith

/-- **Order-zero CAL-1: `ΔU < ΔF`, i.e. `TΔS < 0`, for every `q > 1`.** -/
theorem uT_lt_fT (q : ℝ) (hq : 1 < q) :
    uSplit (2 * q - 1) q < fSplit (q * (q - 1)) q := by
  rw [uT_eq q hq]
  have hq0 : 0 < q := by linarith
  have h1 : 0 < q - 1 := by linarith
  have h2 : 0 < 2 * q - 1 := by linarith
  have hl := log_gt_one_sub_inv q hq
  unfold fSplit
  rw [show -(-2 * Real.log q) / (q * (q - 1)) = 2 * Real.log q / (q * (q - 1)) by ring,
    div_lt_div_iff₀ (by positivity) (by positivity)]
  have key : q - 1 < (2 * q - 1) * Real.log q := by
    have e : (2 * q - 1) * (1 - q⁻¹) = (q - 1) * (2 - q⁻¹) := by field_simp
    have hi : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
    have : q - 1 < (2 * q - 1) * (1 - q⁻¹) := by rw [e]; nlinarith
    nlinarith
  nlinarith

/-- **Tower CAL-1: `ΔU < ΔF`, i.e. `TΔS < 0`, for every `q > 1`.** -/
theorem uTower_lt_fTower (q : ℝ) (hq : 1 < q) :
    uSplit ((2 * q ^ 2 - 1) / q ^ 2) q < fSplit ((q - 1) * (2 * q - 1) / q) q := by
  rw [uTower_eq q hq]
  have hq0 : 0 < q := by linarith
  have h1 : 0 < q - 1 := by linarith
  have h2 : 0 < 2 * q - 1 := by linarith
  have h3 : 0 < 2 * q ^ 2 - 1 := by nlinarith
  have hl := log_gt_one_sub_inv q hq
  unfold fSplit
  rw [show -(-2 * Real.log q) / ((q - 1) * (2 * q - 1) / q)
      = 2 * q * Real.log q / ((q - 1) * (2 * q - 1)) by field_simp,
    div_lt_div_iff₀ (by positivity) (by positivity)]
  -- need (q-1)(2q-1) < (2q²-1) log q
  have e : (2 * q ^ 2 - 1) * (1 - q⁻¹) = (q - 1) * (2 * q - 1) + (q - 1) * (1 - q⁻¹) := by
    field_simp; ring
  have hi : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  have hpos : 0 < (q - 1) * (1 - q⁻¹) := by nlinarith
  have key : (q - 1) * (2 * q - 1) < (2 * q ^ 2 - 1) * Real.log q := by nlinarith
  nlinarith

end QOU.QBeta.NucleonSplitGibbsEnergy
