import Mathlib.Analysis.Complex.Trigonometric
import Mathlib.Tactic

/-!
# A unit-modulus monodromy eigenvalue is never the real pin `q₀` (Step-2 option C, the prune)

Option **C-prune** of `docs/audits/2026-09-06-step-2-plan-hecke-monodromy.md`. The corpus's prose
says the substrate connection is Knizhnik–Zamolodchikov, "flat at `q₀`", with monodromy the
`U_q(su₂)` R-matrix and `q = e^{2πi/(k+2)}` (`mass-theory/lifted-crossing-locality.md:15`,
`vertex-operator-dictionary.md:1,3`). Kohno–Drinfeld monodromy of a KZ connection at a **real**
level has eigenvalues of the form `exp(iθ)`, `θ ∈ ℝ`, hence of **modulus one**; the substrate pin
`q₀ ≈ 1.11` is real and greater than one. So no such eigenvalue equals `q₀`: either the level is
imaginary (a non-unitary KZ connection) or the substrate connection is not KZ. The corpus wording
must name a non-unitary level or be reworded; that edit is the owner's call and is not made here.

Only the one-line analytic fact is proved (`Complex.norm_exp_ofReal_mul_I`); the identification of
the framework's connection with KZ is *not* asserted. Archimedean by nature (`ℂ`, moduli,
`1 < q`), hence its own file per §7c; the generic-field shadow lemmas are in
`QOU/Mass/HeckeQuadraticClassicalShadow.lean`.

-- Ref: [kohno1987] Kohno, Ann. Inst. Fourier 37 (1987) — KZ monodromy factors through the Hecke
--      algebra, with `q` a root of unity at rational level.
-- Ref: [leitner2026] docs/audits/2026-09-06-step-2-plan-hecke-monodromy.md §2C
-/

namespace QOU.Mass.KZUnitModulusPrune

/-- **C-prune.** A monodromy eigenvalue of the form `exp(iθ)` with `θ` real has modulus one, so it
is never a real number greater than one — in particular never the substrate pin `q₀ ≈ 1.11`. -/
theorem unit_modulus_ne_real_gt_one (θ : ℝ) {q : ℝ} (hq : 1 < q) :
    ‖Complex.exp (θ * Complex.I)‖ ≠ q := by
  rw [Complex.norm_exp_ofReal_mul_I]
  exact ne_of_lt hq

/-- The same statement as an inequality on the complex number itself: `exp(iθ) ≠ q` for real
`q > 1`. -/
theorem exp_I_ne_real_gt_one (θ : ℝ) {q : ℝ} (hq : 1 < q) :
    Complex.exp (θ * Complex.I) ≠ (q : ℂ) := by
  intro h
  have := congrArg (fun w : ℂ => ‖w‖) h
  simp only [Complex.norm_exp_ofReal_mul_I, Complex.norm_real, Real.norm_eq_abs] at this
  rw [abs_of_pos (lt_trans zero_lt_one hq)] at this
  exact (ne_of_lt hq) this


/-- **Strict norm gap between unit-circle KZ monodromy and real substrate `q > 1` (`qou-qqyb`).**
For any real phase `θ` and real substrate parameter `q > 1`, `‖Complex.exp (θ * Complex.I)‖ < q`. -/
theorem unit_modulus_lt_real_gt_one (θ : ℝ) {q : ℝ} (hq : 1 < q) :
    ‖Complex.exp (θ * Complex.I)‖ < q := by
  rw [Complex.norm_exp_ofReal_mul_I]
  exact hq

end QOU.Mass.KZUnitModulusPrune
