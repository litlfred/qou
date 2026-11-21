import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic


/-!
# QOU.Archimedean.skein_coulomb_enhancement — Coulomb enhancement from electron-proton Skein crossings

The Fermi function F_q(Z,E) = 2πη_q / (1 - e^{-2πη_q}) arises from
evaluating the Skein polynomial on the full outgoing link (electron ∪
nucleus) rather than the nucleus alone. Each electron-proton crossing
carries Skein weight q, and the coherent product of Z such crossings
gives the Sommerfeld factor.

LaTeX label: `prop:skein-coulomb-enhancement`

## References
- [leitner2026] §6/skein-coulomb-enhancement

**Ground ring**: `ℝ` (geometric/analytic realisation).
Uses ℝ-specific analysis (trig, norms, real powers).
NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Archimedean

/-- The q-deformed Sommerfeld parameter: η_q = α_q · Z / β_e
    where α_q = (q - q⁻¹) · λ_α is the fine structure constant
    from the crossing asymmetry. -/
-- Ref: [leitner2026] §6/skein-coulomb-enhancement
noncomputable def sommerfeldParam (q : ℝ) (lambda_alpha : ℝ) (Z : ℕ) (beta_e : ℝ) : ℝ :=
  (q - 1/q) * lambda_alpha * Z / beta_e

/-- The Skein-Coulomb enhancement factor:
    F_q(Z, E) = 2πη / (1 - e^{-2πη}). -/
-- Ref: [leitner2026] §6/skein-coulomb-enhancement
noncomputable def skeinCoulombFactor (eta : ℝ) : ℝ :=
  2 * Real.pi * eta / (1 - Real.exp (-2 * Real.pi * eta))

/-- The enhancement factor is ≥ 1 for η > 0 (β⁻ decay).
    The Coulomb field of the daughter nucleus attracts the emitted
    electron, increasing the wave function overlap. -/
-- Ref: [leitner2026] §6/skein-coulomb-enhancement
theorem skeinCoulombFactor_ge_one (eta : ℝ) (heta : 0 < eta) :
    1 ≤ skeinCoulombFactor eta := by
  unfold skeinCoulombFactor
  -- Let x = 2πη > 0.  We need x/(1 - e^{-x}) ≥ 1, i.e. x ≥ 1 - e^{-x}.
  rw [show (-2 * Real.pi * eta) = -(2 * Real.pi * eta) by ring]
  set x := 2 * Real.pi * eta with hx_def
  have hpi : 0 < Real.pi := Real.pi_pos
  have hx_pos : 0 < x := by rw [hx_def]; exact mul_pos (mul_pos (by norm_num) hpi) heta
  -- Denominator: 1 - e^{-x} > 0 since e^{-x} < 1 for x > 0
  have hexp_neg : Real.exp (-x) < 1 := by
    rw [Real.exp_lt_one_iff]; linarith
  have hdenom_pos : 0 < 1 - Real.exp (-x) := by linarith
  -- Rewrite: 1 ≤ x/(1-e^{-x}) ↔ 1-e^{-x} ≤ x (since denom > 0)
  rw [le_div_iff₀ hdenom_pos]
  -- Need: 1 - e^{-x} ≤ x, equivalently 1 - x ≤ e^{-x}.
  -- Mathlib: add_one_le_exp gives t + 1 ≤ e^t. Set t = -x:
  -- -x + 1 ≤ e^{-x}, i.e. 1 - x ≤ e^{-x}, i.e. 1 - e^{-x} ≤ x.
  have h := Real.add_one_le_exp (-x)
  linarith

/-- At η = 0 the formula gives 0/0, which Lean evaluates to 0 by
    convention (division by zero returns 0 in ℝ).  The physically
    meaningful statement is the limit lim_{η→0⁺} F(η) = 1, proved
    in `skeinCoulombFactor_limit_one` below. -/
-- Ref: [leitner2026] §6/skein-coulomb-enhancement
theorem skeinCoulombFactor_at_zero :
    skeinCoulombFactor 0 = 0 := by
  unfold skeinCoulombFactor
  simp [Real.exp_zero, mul_zero, zero_div]

/-- The physical statement: lim_{η→0⁺} F_q(η) = 1.
    This is the correct formulation of F(0) = 1 since the pointwise
    evaluation gives 0/0 = 0 in Lean. -/
-- Ref: [leitner2026] §6/skein-coulomb-enhancement
theorem skeinCoulombFactor_limit_one :
    ∀ ε > 0, ∃ δ > 0, ∀ eta : ℝ, 0 < eta → eta < δ →
    |skeinCoulombFactor eta - 1| < ε := by
  -- For small x = 2πη > 0:
  --   F(η) = x/(1 - e^{-x})
  --   1 - e^{-x} = x - x²/2 + ... so F ≈ x/x = 1 for small x.
  -- More precisely: x ≤ 1-e^{-x} + x²/2 (from Taylor) gives
  --   |F - 1| = |x - (1-e^{-x})| / (1-e^{-x}) ≤ x²/2 / (x - x²/2) ≤ x for x < 1.
  -- So δ = ε/(2π) works.
  --
  -- Strategy: From add_one_le_exp(x): 1+x ≤ e^x, so (1+x)e^{-x} ≤ 1,
  -- hence 1-e^{-x} ≥ x/(1+x), so F(η) = x/(1-e^{-x}) ≤ 1+x.
  -- Combined with F ≥ 1, |F-1| ≤ x = 2πη. Choose δ = ε/(2π+1).
  -- Ref: [leitner2026] §6/skein-coulomb-enhancement
  intro ε hε
  refine ⟨ε / (2 * Real.pi + 1), div_pos hε (by linarith [Real.pi_pos]), ?_⟩
  intro eta heta heta_lt
  set x := 2 * Real.pi * eta with hx_def
  have hpi : 0 < Real.pi := Real.pi_pos
  have hx_pos : 0 < x := by rw [hx_def]; exact mul_pos (mul_pos (by norm_num) hpi) heta
  have hexp_neg : Real.exp (-x) < 1 := by
    rw [Real.exp_lt_one_iff]; linarith
  have hdenom_pos : 0 < 1 - Real.exp (-x) := by linarith
  have hF_ge_one : 1 ≤ skeinCoulombFactor eta := skeinCoulombFactor_ge_one eta heta
  rw [abs_of_nonneg (by linarith)]
  -- Key bound: (1+x)e^{-x} ≤ 1 from add_one_le_exp
  have hx_pos' : 0 < 1 + x := by linarith
  have hx_ne : (1 : ℝ) + x ≠ 0 := ne_of_gt hx_pos'
  have hbound : (1 + x) * Real.exp (-x) ≤ 1 := by
    have h1 : (1 : ℝ) + x ≤ Real.exp x := by have := Real.add_one_le_exp x; linarith
    have h2 : Real.exp (-x) * (1 + x) ≤ Real.exp (-x) * Real.exp x :=
      mul_le_mul_of_nonneg_left h1 (le_of_lt (Real.exp_pos (-x)))
    rw [← Real.exp_add, neg_add_cancel, Real.exp_zero] at h2
    linarith
  -- Therefore 1 - e^{-x} ≥ x/(1+x)
  have hdenom_ge : x / (1 + x) ≤ 1 - Real.exp (-x) := by
    -- From hbound: (1+x)*e^{-x} ≤ 1, so e^{-x} ≤ 1/(1+x)
    have hexp_le_inv : Real.exp (-x) ≤ 1 / (1 + x) := by
      rw [le_div_iff₀ hx_pos']
      linarith [mul_comm (1 + x) (Real.exp (-x))]
    -- x/(1+x) = 1 - 1/(1+x) ≤ 1 - e^{-x}
    have hne : (1 : ℝ) + x ≠ 0 := ne_of_gt hx_pos'
    have : x / (1 + x) = 1 - 1 / (1 + x) := by
      field_simp
      ring
    linarith
  -- F ≤ 1 + x
  have hF_le : skeinCoulombFactor eta ≤ 1 + x := by
    unfold skeinCoulombFactor
    rw [show (-2 * Real.pi * eta) = -x by rw [hx_def]; ring,
        show (2 * Real.pi * eta) = x from hx_def.symm,
        div_le_iff₀ hdenom_pos]
    -- Need: x ≤ (1+x) * (1 - e^{-x})
    -- From hdenom_ge: x/(1+x) ≤ 1-e^{-x}, multiply by (1+x) > 0
    rw [div_le_iff₀ hx_pos'] at hdenom_ge
    linarith
  -- x = 2πη < 2π · ε/(2π+1) < ε
  have hx_lt : x < ε := by
    calc x = 2 * Real.pi * eta := rfl
      _ < 2 * Real.pi * (ε / (2 * Real.pi + 1)) :=
          mul_lt_mul_of_pos_left heta_lt (by positivity)
      _ = 2 * Real.pi * ε / (2 * Real.pi + 1) := by ring
      _ < ε := by rw [div_lt_iff₀ (by linarith [Real.pi_pos])]; nlinarith [Real.pi_pos]
  linarith

/-- The Sommerfeld parameter is positive when q > 1, Z > 0, β_e > 0. -/
-- Ref: [leitner2026] §6/skein-coulomb-enhancement
theorem sommerfeldParam_pos (q : ℝ) (hq : 1 < q) (lambda_alpha : ℝ)
    (hla : 0 < lambda_alpha) (Z : ℕ) (hZ : 0 < Z) (beta_e : ℝ)
    (hb : 0 < beta_e) :
    0 < sommerfeldParam q lambda_alpha Z beta_e := by
  unfold sommerfeldParam
  have hq0 : (0 : ℝ) < q := by linarith
  have hqq : 0 < q - 1 / q := by
    have h1q : 1 / q < 1 := by rw [div_lt_one hq0]; linarith
    have : (1 : ℝ) / q < q := by linarith
    linarith
  have hZ' : (0 : ℝ) < (Z : ℝ) := Nat.cast_pos.mpr hZ
  apply div_pos
  · exact mul_pos (mul_pos hqq hla) hZ'
  · exact hb

/-- The enhancement factor grows with Z (more protons = stronger
    Coulomb field = larger enhancement). -/
-- Ref: [leitner2026] §6/skein-coulomb-enhancement
theorem skeinCoulombFactor_monotone_eta (eta1 eta2 : ℝ)
    (h1 : 0 < eta1) (h2 : eta1 < eta2) :
    skeinCoulombFactor eta1 < skeinCoulombFactor eta2 := by
  -- Cross-multiplication: need x1*(1-e^{-x2}) < x2*(1-e^{-x1}).
  -- Write e^{-x2} = e^{-x1}·e^{-d} where d = x2-x1 > 0.
  -- Reduces to: d*(1-e^{-x1}) > x1*e^{-x1}*(1-e^{-d}).
  -- Divide by d*e^{-x1}: (e^{x1}-1) > x1*(1-e^{-d})/d.
  -- RHS < x1 (since (1-e^{-d})/d < 1 by add_one_lt_exp(-d)).
  -- LHS > x1 (since e^{x1}-1 > x1 by add_one_lt_exp(x1)).
  -- Ref: [leitner2026] §6/skein-coulomb-enhancement
  unfold skeinCoulombFactor
  rw [show (-2 * Real.pi * eta1) = -(2 * Real.pi * eta1) by ring,
      show (-2 * Real.pi * eta2) = -(2 * Real.pi * eta2) by ring]
  set x1 := 2 * Real.pi * eta1 with hx1_def
  set x2 := 2 * Real.pi * eta2 with hx2_def
  have hpi : 0 < Real.pi := Real.pi_pos
  have hx1_pos : 0 < x1 := by rw [hx1_def]; exact mul_pos (mul_pos (by norm_num) hpi) h1
  have hx2_pos : 0 < x2 := by rw [hx2_def]; exact mul_pos (mul_pos (by norm_num) hpi) (lt_trans h1 h2)
  have hx_lt : x1 < x2 := by
    simp only [hx1_def, hx2_def]
    exact mul_lt_mul_of_pos_left h2 (by positivity)
  have hdiff_pos : 0 < x2 - x1 := by linarith
  have hexp1 : Real.exp (-x1) < 1 := by rw [Real.exp_lt_one_iff]; linarith
  have hexp2 : Real.exp (-x2) < 1 := by rw [Real.exp_lt_one_iff]; linarith
  have hd1 : 0 < 1 - Real.exp (-x1) := by linarith
  have hd2 : 0 < 1 - Real.exp (-x2) := by linarith
  rw [div_lt_div_iff₀ hd1 hd2]
  -- Need: x1 * (1 - exp(-x2)) < x2 * (1 - exp(-x1))
  set d := x2 - x1 with hd_def
  -- e^{x1} - 1 > x1 (strict exp bound for x1 > 0)
  have hx1_ne : x1 ≠ 0 := hx1_pos.ne'
  have hd_ne : d ≠ 0 := hdiff_pos.ne'
  have hexp_x1_gt : x1 < Real.exp x1 - 1 := by
    have := Real.add_one_lt_exp hx1_ne
    linarith
  -- 1 - e^{-d} < d (strict exp bound for d > 0)
  have hexp_d_lt : 1 - Real.exp (-d) < d := by
    have hnd_ne : -d ≠ 0 := neg_ne_zero.mpr hd_ne
    have := Real.add_one_lt_exp hnd_ne
    linarith
  -- (1-e^{-d})/d < 1
  have honed_lt : (1 - Real.exp (-d)) / d < 1 := by
    rw [div_lt_one hdiff_pos]; exact hexp_d_lt
  -- Combine: x1 * (1-e^{-d})/d < x1 < e^{x1}-1
  have hkey : x1 * (1 - Real.exp (-d)) / d < Real.exp x1 - 1 :=
    calc x1 * (1 - Real.exp (-d)) / d
        = x1 * ((1 - Real.exp (-d)) / d) := by ring
      _ < x1 * 1 := mul_lt_mul_of_pos_left honed_lt hx1_pos
      _ = x1 := mul_one x1
      _ < Real.exp x1 - 1 := hexp_x1_gt
  -- Multiply by d > 0: x1*(1-e^{-d}) < d*(e^{x1}-1)
  have hstep6 : x1 * (1 - Real.exp (-d)) < d * (Real.exp x1 - 1) := by
    -- From hkey: x1*(1-e^{-d})/d < e^{x1}-1, multiply by d > 0
    rw [div_lt_iff₀ hdiff_pos] at hkey; linarith
  -- Multiply by e^{-x1} > 0: x1*e^{-x1}*(1-e^{-d}) < d*(1-e^{-x1})
  have hexp_x1_pos : 0 < Real.exp (-x1) := Real.exp_pos _
  have hstep7 : x1 * Real.exp (-x1) * (1 - Real.exp (-d)) <
      d * (1 - Real.exp (-x1)) := by
    have h6' : Real.exp (-x1) * (x1 * (1 - Real.exp (-d))) <
        Real.exp (-x1) * (d * (Real.exp x1 - 1)) :=
      mul_lt_mul_of_pos_left hstep6 hexp_x1_pos
    -- Simplify RHS: e^{-x1} * d * (e^{x1} - 1) = d * (1 - e^{-x1})
    have hrw : Real.exp (-x1) * (d * (Real.exp x1 - 1)) =
        d * (1 - Real.exp (-x1)) := by
      have : Real.exp (-x1) * Real.exp x1 = 1 := by
        rw [← Real.exp_add, neg_add_cancel, Real.exp_zero]
      nlinarith
    rw [hrw] at h6'; linarith
  -- e^{-x2} = e^{-x1} · e^{-d}
  have hexp_split : Real.exp (-x2) = Real.exp (-x1) * Real.exp (-d) := by
    rw [← Real.exp_add]; congr 1; rw [hd_def]; ring
  -- Final: x1*(1-e^{-x2}) < x2*(1-e^{-x1})
  -- After rewriting e^{-x2} = e^{-x1}*e^{-d}, need:
  -- x1*(1 - e^{-x1}*e^{-d}) < x2*(1 - e^{-x1})
  -- Since x2 = x1 + d, this expands to x1*e^{-x1}*(1-e^{-d}) < d*(1-e^{-x1})
  -- which is hstep7.
  rw [hexp_split]
  have hx2_eq : x2 = x1 + d := by linarith [hd_def]
  nlinarith [hstep7, hd1, hd2, hexp_x1_pos, mul_pos hx1_pos hd1]

/-- Top-level alias matching the manifest declaration. -/
-- Ref: [leitner2026] §6/skein-coulomb-enhancement
noncomputable def skein_coulomb_enhancement (q : ℝ) (lambda_alpha : ℝ)
    (Z : ℕ) (beta_e : ℝ) : ℝ :=
  skeinCoulombFactor (sommerfeldParam q lambda_alpha Z beta_e)

end QOU.Archimedean
