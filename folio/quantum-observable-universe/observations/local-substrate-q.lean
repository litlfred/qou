import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real


/-!
# QOU.Experimental.local_substrate_q — Local value of q

In any sufficiently small neighbourhood U ⊂ M, the substrate
parameter q satisfies:

  q|_U = 1.1097 ± 0.001

More precisely, q|_U is the unique real root q > 1 of:

  (1 - q⁻¹)² = Vol(4₁) / (m_μ/m_e)

where Vol(4₁) ≈ 2.02988 and m_μ/m_e = 206.7682830 (CODATA 2022).
Witness: computations/knot-volumes.witness.json (SnapPy 3.3.2, all passed).

LaTeX label: `prop:local-substrate-q`

## References

- CODATA 2018 recommended values
- [leitner2026] §11-experimental-evidence/local-substrate-q

**Ground ring**: `ℝ` (archimedean realisation).
Evaluates formal results at q₀ ≈ 1.1098 for comparison with
experimental data. NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Experimental

/-- **Local substrate parameter determination**.

    The substrate parameter q is determined by requiring that the
    lepton mass ratio prediction matches the CODATA value.

    q is the unique real root > 1 of:
    `(1 - q⁻¹)² = Vol(4₁) / (m_μ/m_e)` -/
-- Ref: CODATA 2018, [leitner2026] §11
structure LocalSubstrateQ where
  /-- Hyperbolic volume of the figure-eight knot.
      `Vol(4₁) = 2 Cl₂(π/3) = 6 Λ(π/3) ≈ 2.02988` — two regular ideal
      tetrahedra, each of volume `Cl₂(π/3) = 3 Λ(π/3)`. -/
  vol_figure_eight : ℝ
  /-- The CODATA muon-electron mass ratio. -/
  muon_electron_ratio : ℝ
  /-- The derived substrate parameter. -/
  q : ℝ
  /-- q > 1. -/
  q_gt_one : 1 < q
  /-- The defining equation: `(1 - q⁻¹)² = Vol(4₁)/(m_μ/m_e)`. -/
  defining_eq : (1 - q⁻¹) ^ 2 = vol_figure_eight / muon_electron_ratio
  /-- q ≈ 1.1097 within experimental uncertainty. -/
  q_approx : |q - 1.1097| < 0.001

/-- Uniqueness: the equation `(1 - q⁻¹)² = c` for `c > 0` has a
    unique solution `q > 1`.

    From `(1 - q⁻¹)² = c`, taking positive square root:
    `1 - q⁻¹ = √c`, so `q⁻¹ = 1 - √c`, i.e. `q = 1/(1 - √c)`.
    For q > 1 we need `0 < √c < 1`, i.e. `0 < c < 1`. -/
-- Ref: [leitner2026] §11
theorem unique_q_solution (c : ℝ) (hc_pos : 0 < c) (hc_lt : c < 1) :
    ∃! (q : ℝ), 1 < q ∧ (1 - q⁻¹) ^ 2 = c := by
  use (1 - Real.sqrt c)⁻¹
  constructor
  · constructor
    · have hsqrt_pos : 0 < Real.sqrt c := Real.sqrt_pos.mpr hc_pos
      have hsqrt_lt : Real.sqrt c < 1 := by
        rw [show (1:ℝ) = Real.sqrt 1 by simp]
        exact Real.sqrt_lt_sqrt hc_pos.le hc_lt
      have h1 : 0 < 1 - Real.sqrt c := by linarith
      rw [one_lt_inv_iff₀]
      exact ⟨h1, by linarith⟩
    · rw [inv_inv]
      rw [sub_sq, one_pow, mul_one]
      ring_nf
      rw [Real.sq_sqrt hc_pos.le]
  · intro q' ⟨hq'_gt, hq'_eq⟩
    have hq'_pos : 0 < q' := by linarith
    have h_hbar : 0 < 1 - q'⁻¹ := by
      have : q'⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq'_gt
      linarith
    have h_sqrt : 1 - q'⁻¹ = Real.sqrt c := by
      rw [← Real.sqrt_sq h_hbar.le, hq'_eq]
    have : q'⁻¹ = 1 - Real.sqrt c := by linarith
    rw [← inv_inv q']
    congr 1

/-- The CODATA ratio Vol(4₁)/(m_μ/m_e) is in (0,1), ensuring
    a unique q > 1 solution exists. -/
-- Ref: [codata2022] CODATA 2022
theorem codata_ratio_in_range :
    0 < (2.02988 : ℝ) / 206.7682827 ∧ (2.02988 : ℝ) / 206.7682827 < 1 := by
  constructor
  · positivity
  · rw [div_lt_one (by positivity : (0:ℝ) < 206.7682827)]
    norm_num

end QOU.Experimental
