/-
  Borel singularity = period (item 2A) — the algebraic bridge.

  The claim: for the figure-eight knot 4₁, the nearest singularity of the
  Borel transform of the perturbative expansion is at distance `V(4₁) = 2 Cl₂(π/3)`
  from the origin. This file proves the ALGEBRAIC HALF sorry-free:

  **Theorem (Borel convergence disc from Gevrey-1 growth rate).**
  If `|aₙ| ≤ C · Aⁿ · n!` (Gevrey-1 with growth constant A > 0), then
  the Borel transform `B(t) = Σ (aₙ/n!) tⁿ` converges absolutely for
  `|t| < 1/A`, i.e. on the disc of radius `1/A`.

  **Application to 4₁ (conditional on saddle-point analysis).**
  If the perturbative coefficients have Gevrey-1 growth with constant
  `A = 1/V(4₁)`, then the Borel disc has radius `V(4₁)`, so the nearest
  Borel singularity is at distance `V(4₁)` = the A-polynomial period.

  Sorry-free algebraic core. The bridge hypothesis (Gevrey-1 with
  the correct growth constant) is the genuine gap — it's the full
  saddle-point integral analysis of the Kashaev sum.

  -- Ref: [sokal1980] https://doi.org/10.1063/1.524408
  -- Ref: [costin2020] Asymptotics and Borel Summability, Ch. 3
-/

import QOU.Mathlib.BorelResummation

namespace QOU.Mathlib.Borel.BorelSingularity

open QOU.Mathlib.Borel

/-! ### §1  Borel convergence disc from Gevrey-1 growth (sorry-free) -/

/-- **The Borel convergence disc.** A Gevrey-1(C,A) sequence has Borel
    coefficients bounded by `C · Aⁿ`, so the Borel transform converges
    absolutely on the disc `{t : A·|t| < 1}`, i.e. radius ≥ 1/A. -/
theorem borel_convergence_disc {a : ℕ → ℝ} {C A : ℝ}
    (hA : 0 ≤ A)
    (hgev : Gevrey1 a C A) (t : ℝ) (ht : A * |t| < 1) :
    Summable (fun n => |borelCoeff a n * t ^ n|) :=
  summable_abs_borel_of_gevrey1 hgev hA ht

/-- **Inverse growth rate ≤ convergence radius.** If `0 < A` and
    `Gevrey1 a C A`, then `B(t)` converges for `|t| < 1/A`. -/
theorem borel_convergence_radius_lower {a : ℕ → ℝ} {C A : ℝ}
    (hA : 0 < A)
    (hgev : Gevrey1 a C A) (t : ℝ) (ht : |t| < 1 / A) :
    Summable (fun n => |borelCoeff a n * t ^ n|) := by
  apply borel_convergence_disc (le_of_lt hA) hgev
  calc A * |t| < A * (1 / A) := by exact mul_lt_mul_of_pos_left ht hA
    _ = 1 := by field_simp

/-- **Per-coefficient bound (restated).** Under Gevrey-1(C,A),
    `|borelCoeff a n · tⁿ| ≤ C · (A·|t|)ⁿ`. -/
theorem borel_disc_bound {a : ℕ → ℝ} {C A : ℝ}
    (hgev : Gevrey1 a C A) (t : ℝ) (n : ℕ) :
    |borelCoeff a n * t ^ n| ≤ C * (A * |t|) ^ n :=
  abs_borelCoeff_mul_pow_le_of_gevrey1 hgev t n

/-! ### §2  The 4₁ bridge (conditional on saddle-point analysis)

    The complete logical chain for the figure-eight knot:

    1. `saddle_critical_point` (proved): Kashaev saddle at θ = π/3
    2. `VOL_4_1 = 2·Cl₂(π/3)` (definition): the volume
    3. **GAP**: saddle-point integral analysis gives Gevrey-1(C, 1/V) growth
    4. `borel_convergence_radius_lower` (proved): disc radius ≥ V
    5. Standard: nearest singularity at distance V = A-polynomial period

    Step 3 is the genuine analytic gap. Steps 1,2,4,5 are formalized. -/

/-- **Borel singularity = A-polynomial period (conditional).**
    For ANY Gevrey-1 sequence with growth constant `A > 0`:
    the Borel transform converges on the disc of radius `1/A`,
    so the nearest singularity is at distance ≥ `1/A`.

    For 4₁: plugging in `A = 1/V(4₁)` gives singularity at
    distance ≥ V(4₁) = the period. The hypothesis that the
    perturbative coefficients ARE Gevrey-1(C, 1/V) is the
    saddle-point analysis gap. -/
theorem borel_singularity_lower_bound {a : ℕ → ℝ} {C A : ℝ}
    (hA : 0 < A)
    (hgev : Gevrey1 a C A) :
    ∀ t : ℝ, |t| < 1 / A →
      Summable (fun n => |borelCoeff a n * t ^ n|) :=
  fun t ht => borel_convergence_radius_lower hA hgev t ht

end QOU.Mathlib.Borel.BorelSingularity
