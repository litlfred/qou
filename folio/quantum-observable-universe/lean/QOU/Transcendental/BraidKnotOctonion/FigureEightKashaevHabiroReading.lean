import QCalculus.HabiroCyclotomicSeries
import QOU.Transcendental.BraidKnotOctonion.FigureEightVolume
import Mathlib.RingTheory.Polynomial.Cyclotomic.Roots
import Mathlib.RingTheory.RootsOfUnity.Complex

/-!
# QOU.Transcendental.BraidKnotOctonion.FigureEightKashaevHabiroReading

Bean `qou-28qh`, phase 3 (first step). The archimedean comparison for the
figure-eight Kashaev invariant, kept behind the transcendental boundary.

`QOU.Knot.FigureEightVolume.kashaev N = ∑_{k<N} ∏_{j=1}^{k} (2 - 2 cos(2πj/N))`
is the real-valued definition the volume-conjecture files use. This file proves
that it is the value of the single algebraic element
`QCalculus.HabiroSeries.figureEight ∈ ℤ̂[q]` under the evaluation ring map at
`ζ_N = exp(2πi/N)`:

  `(kashaev N : ℂ) = evalRoot ζ_N figureEight`.

So everything about `kashaev N` that does not use the embedding into `ℂ` can be
stated and proved about `figureEight` on the algebraic side, and the only
transcendental input is the identity `ζ^j + ζ^{-j} = 2 cos(2πj/N)`, which lives
here. Moving the existing consumers of `FigureEightVolume` onto the algebraic
element is the later strangler step, to be coordinated with the knot-volume
work on those files.

No empirical value enters this file.
-/

namespace QOU.Transcendental.FigureEightKashaevHabiroReading

open Polynomial Finset Complex QCalculus.HabiroSeries

/-- `ζ_N = exp(2πi/N)`. -/
noncomputable def zeta (N : ℕ) : ℂ := Complex.exp (2 * Real.pi * I / N)

theorem aeval_zeta_cyclotomic {N : ℕ} (hN : N ≠ 0) :
    aeval (zeta N) (cyclotomic N ℤ) = 0 := by
  have h := (Complex.isPrimitiveRoot_exp N hN).isRoot_cyclotomic (Nat.pos_of_ne_zero hN)
  simpa [aeval_def, eval₂_eq_eval_map, IsRoot.def] using h

/-- One factor: `(1 - ζ^{-j})(1 - ζ^j) = 2 - 2 cos(2πj/N)`. -/
theorem factor_eq (N j : ℕ) :
    (1 - (zeta N)⁻¹ ^ j) * (1 - zeta N ^ j) =
      ((2 - 2 * Real.cos (2 * Real.pi * j / N) : ℝ) : ℂ) := by
  have hj : zeta N ^ j = Complex.exp ((2 * Real.pi * j / N : ℝ) * I) := by
    rw [zeta, ← Complex.exp_nat_mul]; congr 1; push_cast; ring
  have hji : (zeta N)⁻¹ ^ j = Complex.exp (-(2 * Real.pi * j / N : ℝ) * I) := by
    rw [inv_pow, hj, ← Complex.exp_neg]; congr 1; ring
  have hprod : zeta N ^ j * (zeta N)⁻¹ ^ j = 1 := by
    rw [hj, hji, ← Complex.exp_add]; simp
  push_cast at hj hji ⊢
  rw [Complex.two_cos, ← hj, ← hji]
  linear_combination hprod

/-- **The archimedean reading.** For `N ≠ 0`, the real figure-eight Kashaev sum
    is the value of the Habiro element `figureEight` at `ζ_N = exp(2πi/N)`. -/
theorem kashaev_eq_evalRoot_figureEight {N : ℕ} (hN : N ≠ 0) :
    ((QOU.Knot.FigureEightVolume.kashaev N : ℝ) : ℂ) =
      evalRoot hN (zeta N) (aeval_zeta_cyclotomic hN) (figureEight (R := ℤ)) := by
  rw [evalRoot_figureEight_field, QOU.Knot.FigureEightVolume.kashaev]
  push_cast
  refine sum_congr rfl fun k _ => ?_
  rw [QOU.Knot.FigureEightVolume.kashaevProd, poch, poch, ← prod_mul_distrib]
  push_cast
  have hIcc : Icc 1 k = Ico 1 (k + 1) := rfl
  rw [hIcc, prod_Ico_eq_prod_range, Nat.add_sub_cancel]
  refine prod_congr rfl fun i _ => ?_
  rw [factor_eq]
  push_cast
  rw [add_comm (1 : ℂ) (i : ℂ)]

end QOU.Transcendental.FigureEightKashaevHabiroReading
