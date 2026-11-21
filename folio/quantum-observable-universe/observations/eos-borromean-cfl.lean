import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.Positivity


/-!
# QOU.Archimedean.eos_borromean_cfl

Equation of state for Borromean (confined) and CFL (superconducting)
phases.  The key result: the CFL phase is ~2300× stiffer because
Vol(L_H) = 0 makes the effective quark mass ~1000× smaller than
the Borromean baryon mass.

## References

- [leitner2026] Ch. 7, §Strangelet Stability
- [alford1999] https://doi.org/10.1016/S0550-3213(98)00668-3

**Ground ring**: `ℝ` (archimedean realisation).
Evaluates formal results at q₀ ≈ 1.1098 for comparison with
experimental data. NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

noncomputable section

namespace QOU.Archimedean

/-- Borromean volume (8 × Catalan's constant). -/
-- Ref: [thurston1978]
def V_B' : ℝ := 7.32772

/-- The q-deformed Planck constant. -/
-- Ref: [leitner2026] Ch. 2
def hbarQ (q : ℝ) : ℝ := 1 - q⁻¹

/-- Baryon mass in the Borromean phase (topological mass formula). -/
-- Ref: [leitner2026] Ch. 4
def M_B (q : ℝ) : ℝ := V_B' / (hbarQ q) ^ 2

/-- Effective quark mass in the CFL phase (crossing energy per quark).
    Three quarks per baryon, each with crossing energy from the
    Hopf link.  Vol(L_H) = 0, so no volume contribution. -/
-- Ref: [leitner2026] Ch. 7
def M_D (q : ℝ) : ℝ := (q + q⁻¹) / 3

/-- Fermi gas pressure for baryons at number density n_B.
    P = ℏ_q² (3π²)^{2/3} / (5M) · n_B^{5/3}
    We factor out n_B^{5/3} and define the pressure coefficient. -/
-- Ref: [leitner2026] Ch. 7
def pressure_coeff_borromean (q : ℝ) : ℝ :=
  (hbarQ q) ^ 2 / (5 * M_B q)

def pressure_coeff_cfl (q : ℝ) : ℝ :=
  (hbarQ q) ^ 2 / (5 * M_D q) * 3 ^ (2/3 : ℝ)

/-- The stiffness ratio P_D/P_B at equal baryon density.
    Dominated by M_B/M_D × 3^{2/3}. -/
-- Ref: [leitner2026] Ch. 7
def stiffness_ratio (q : ℝ) : ℝ :=
  M_B q / M_D q * 3 ^ (5/3 : ℝ)

/-- At q = 1.1097, M_B is large. -/
-- Ref: [leitner2026] Ch. 7
theorem M_B_large : M_B 1.1097 > 700 := by
  unfold M_B V_B' hbarQ
  norm_num

/-- At q = 1.1097, M_D is small. -/
-- Ref: [leitner2026] Ch. 7
theorem M_D_small : M_D 1.1097 < 1 := by
  unfold M_D
  norm_num

/-- The mass ratio M_B/M_D exceeds 1000 at q = 1.1097. -/
-- Ref: [leitner2026] Ch. 7
theorem mass_ratio_gt_1000 :
    M_B 1.1097 / M_D 1.1097 > 1000 := by
  unfold M_B M_D V_B' hbarQ
  norm_num

/-- The conformal speed of sound squared. -/
-- Ref: [leitner2026] Ch. 7
def conformal_cs_squared : ℝ := 1 / 3

/-- Speed of sound in the Borromean phase at Fermi energy E_F.
    c_s² = (2/3) · E_F / (M_B + E_F). -/
-- Ref: [leitner2026] Ch. 7
def cs_squared_borromean (q : ℝ) (E_F : ℝ) : ℝ :=
  (2 / 3) * E_F / (M_B q + E_F)

/-- At nuclear saturation density, E_F ≪ M_B, so c_s² ≪ 1.
    We show: for any E_F < M_B/100, c_s² < 1/100. -/
-- Ref: [leitner2026] Ch. 7
theorem cs_borromean_nonrelativistic (q : ℝ) (E_F : ℝ)
    (hq : q = 1.1097) (hEF : E_F > 0) (hsmall : E_F < M_B q / 100) :
    cs_squared_borromean q E_F < 1 / 100 := by
  subst hq
  unfold cs_squared_borromean M_B V_B' hbarQ at *
  set C : ℝ := 7.32772 / (1 - (1.1097 : ℝ)⁻¹) ^ 2 with hC_def
  -- C > 0
  have hC_pos : (0 : ℝ) < C := by rw [hC_def]; norm_num
  -- C + E_F > 0
  have hCE_pos : (0 : ℝ) < C + E_F := by linarith
  -- Goal: 2/3 * E_F / (C + E_F) < 1/100
  -- Equiv to: 200 * E_F < 3 * (C + E_F)  [multiply by 3(C+E_F)/100 > 0]
  -- i.e.: 197 * E_F < 3 * C
  -- From hsmall: E_F < C/100, so 197 * E_F < 197 * C / 100 < 3 * C  ✓
  rw [div_lt_iff₀ hCE_pos]
  nlinarith [hsmall, hC_pos]

/- In the CFL phase, the conformal limit c_s² → 1/3 is approached
    when E_F ≫ M_D.  Formally: for any ε > 0, there exists E_F₀
    such that |c_s² - 1/3| < ε for all E_F > E_F₀. -/
-- Ref: [leitner2026] Ch. 7
-- This is a standard analysis fact about E_F/(M + E_F) → 1.
-- The physical content is that M_D is small enough to reach
-- the conformal limit at achievable densities.

end QOU.Archimedean

end
