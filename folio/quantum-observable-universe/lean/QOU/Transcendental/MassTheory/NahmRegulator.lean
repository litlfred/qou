import QOU.MassTheory.TwistKnotNahm
import QOU.Transcendental.MassTheory.BlochGroupComplex
import QOU.Transcendental.MassTheory.Cl2PentagonFromBlochWigner

/-!
# The regulator of the 4₁ and 5₂ Nahm classes

Bean `qou-35a8` (item 4 of epic `qou-dk7p`). The Bloch-group classes of the
figure-eight knot `4₁` and of `5₂` are algebraic and live outside the
transcendental boundary: `PreArchimedeanBloch.fig8Class` and
`TwistKnotNahm.twistClass` are defined over any field, and their membership in
`B(F)` is proved there with no analysis.

This file is the one place where those classes meet a transcendental function.
It evaluates them under the Bloch–Wigner regulator `D : P(ℂ) →+ ℝ`
(`BlochGroupComplex.blochWignerRegulator`, induced by the proved five-term
relation). Nothing else is evaluated here:

* `pentagonSubgroup_complex_eq`: the generic `P(F)` at `F = ℂ` is the `P(ℂ)` on
  which the regulator is defined (`rfl`).
* `regulator_fig8Class`: `D(2[e^{iπ/3}]) = 2·Cl₂(π/3)`, the corpus's `Vol(4₁)`.
* `regulator_twistClass`: `D(3[X] − [XY] − [X/Y]) = 3D(X) − D(XY) − D(X/Y)` at
  any `5₂` saddle, the regulator half of the 5₂ volume.

The regulator is a single evaluation, not a limit, so no `[Coev E]` instance is
spent here. The located-cut comparison with a numerical volume belongs with the
cut of `Cl₂(π/3)` and is not stated in this file. No empirical value appears.
-/

namespace QOU.Archimedean.NahmRegulator

open Complex QOU.Archimedean.PreArchimedeanBloch QOU.Archimedean.TwistKnotNahm
open QOU.Archimedean.FiveTermProof QOU.MathlibExt

noncomputable section

/-- The generic pre-Bloch group at `ℂ` is the one the regulator is defined on. -/
theorem pentagonSubgroup_complex_eq :
    PreArchimedeanBloch.pentagonSubgroup ℂ = BlochGroupComplex.pentagonSubgroup := rfl

/-- **The Bloch–Wigner regulator** on the generic `P(ℂ)`. -/
def regulator : PreBloch ℂ →+ ℝ := BlochGroupComplex.blochWignerRegulator

theorem regulator_mk_gen {z : ℂ} (h0 : z ≠ 0) (h1 : z ≠ 1) :
    regulator (QuotientAddGroup.mk (PreArchimedeanBloch.gen z)) = blochD z :=
  BlochGroupComplex.blochWignerRegulator_mk_gen h0 h1

/-- `e^{iπ/3}` is a root of `ζ² − ζ + 1`, the 4₁ Nahm equation. -/
theorem zeta6_phi6 : exp ((Real.pi / 3 : ℝ) * I) ^ 2 - exp ((Real.pi / 3 : ℝ) * I) + 1 = 0 := by
  set ζ := exp ((Real.pi / 3 : ℝ) * I) with hζ
  have h3 : ζ ^ 3 = -1 := by
    rw [hζ, ← Complex.exp_nat_mul]
    have : ((3 : ℕ) : ℂ) * ((Real.pi / 3 : ℝ) * I) = Real.pi * I := by push_cast; ring
    rw [this, Complex.exp_pi_mul_I]
  have hne : ζ + 1 ≠ 0 := by
    intro h
    have hre := congrArg Complex.re h
    simp only [hζ, Complex.add_re, Complex.one_re, Complex.zero_re] at hre
    rw [Complex.exp_ofReal_mul_I_re] at hre
    have : Real.cos (Real.pi / 3) = 1 / 2 := Real.cos_pi_div_three
    linarith
  have : (ζ + 1) * (ζ ^ 2 - ζ + 1) = 0 := by linear_combination h3
  exact (mul_eq_zero.1 this).resolve_left hne

/-- **The 4₁ regulator.** The figure-eight Nahm class at `ζ = e^{iπ/3}` has
regulator `2·Cl₂(π/3)`. -/
theorem regulator_fig8Class :
    regulator (fig8Class (exp ((Real.pi / 3 : ℝ) * I))) = 2 * Cl_2 (Real.pi / 3) := by
  have h := phi6_facts zeta6_phi6
  have h0 : exp ((Real.pi / 3 : ℝ) * I) ≠ 0 := Complex.exp_ne_zero _
  have h1 : exp ((Real.pi / 3 : ℝ) * I) ≠ 1 := by
    intro h1; have := zeta6_phi6; rw [h1] at this; norm_num at this
  rw [fig8Class, map_nsmul, regulator_mk_gen h0 h1,
    QOU.Archimedean.Cl2PentagonFromBlochWigner.blochD_exp]
  simp [two_smul, two_mul]

/-- **The 5₂ (twist-knot) regulator.** At a saddle `(X, Y)`, with `X ≠ 1`, the
twist-knot class has regulator `3D(X) − D(XY) − D(X/Y)`. -/
theorem regulator_twistClass {p : ℤ} {X Y : ℂ} (s : TwistSaddle p X Y) (hX1 : X ≠ 1) :
    regulator (twistClass X Y) = 3 * blochD X - blochD (X * Y) - blochD (X / Y) := by
  have hXY0 : X * Y ≠ 0 := mul_ne_zero s.X_ne_zero s.Y_ne_zero
  have hXd0 : X / Y ≠ 0 := div_ne_zero s.X_ne_zero s.Y_ne_zero
  have hXd1 : X / Y ≠ 1 := fun h => s.X_ne_Y ((div_eq_one_iff_eq s.Y_ne_zero).1 h)
  rw [twistClass, QuotientAddGroup.mk_sub, QuotientAddGroup.mk_sub, map_sub, map_sub,
    QuotientAddGroup.mk_nsmul, map_nsmul, regulator_mk_gen s.X_ne_zero hX1,
    regulator_mk_gen hXY0 s.XY_ne_one, regulator_mk_gen hXd0 hXd1]
  simp [nsmul_eq_mul]

/-- The `5₂` regulator at a root `t` of the 5₂ cubic. -/
theorem regulator_fiveTwo {t : ℂ} (ht : t ^ 3 - t ^ 2 + 2 * t - 1 = 0) :
    regulator (twistClass (1 + t) t)
      = 3 * blochD (1 + t) - blochD ((1 + t) * t) - blochD ((1 + t) / t) := by
  have ht0 : t ≠ 0 := by rintro rfl; norm_num at ht
  exact regulator_twistClass (fiveTwo_saddle_of_cubic ht (by norm_num))
    (fun h => ht0 (by linear_combination h))

end

end QOU.Archimedean.NahmRegulator
