import QCalculus.HabiroCyclotomicSeries
import QOU.Core.TarskiSignKashaev

/-!
# QOU.Core.KashaevHabiroBridge — the figure-eight Kashaev sum is a Habiro value

Bean `qou-28qh`, phase 1. `QOU.Core.TarskiSignKashaev.kashaevFigureEight c N`
is the integer polynomial in `c = ζ + ζ⁻¹` whose value is `⟨4₁⟩_N`, used by the
sign certificates of `qou-pc7n`. This file shows that, at a root `ζ` of `Φ_N` in
any field `K`, it is exactly the image of the single Habiro element
`QCalculus.HabiroSeries.figureEight ∈ R̂[q]` under the evaluation ring map:

  `evalRoot ζ figureEight = kashaevFigureEight (ζ + ζ⁻¹) N`.

So the per-`N` values of `TarskiSignKashaev` are the cyclotomic shadows of one
algebraic object, and the dependence on `N` is the choice of ring map, not a
new definition per `N`. Algebraic, any base ring `R`, any field `K`, no
analytic API, no empirical value.
-/

namespace QOU.Core.KashaevHabiroBridge

open Polynomial Finset QCalculus.HabiroSeries QOU.Core.TarskiSignKashaev

/-- **The bridge.** At a root `ζ` of `Φ_N` (`N ≠ 0`) in a field `K`, the image
    of the Habiro element `figureEight` is the figure-eight Kashaev polynomial
    evaluated at `ζ + ζ⁻¹`. -/
theorem evalRoot_figureEight_eq_kashaevFigureEight {R K : Type*} [CommRing R] [Field K]
    [Algebra R K] {N : ℕ} (hN : N ≠ 0) {ζ : K} (hζ : aeval ζ (cyclotomic N R) = 0) :
    evalRoot hN ζ hζ (figureEight (R := R)) = kashaevFigureEight (ζ + ζ⁻¹) N := by
  have h1 := evalRoot_q_mul_qInv hN hζ (R := R)
  have hz : ζ ≠ 0 := left_ne_zero_of_mul_eq_one h1
  rw [evalRoot_figureEight_field, kashaevFigureEight]
  refine sum_congr rfl fun k _ => ?_
  rw [poch, poch, ← prod_mul_distrib]
  refine prod_congr rfl fun j _ => ?_
  rw [mul_comm, kashaev_factor hz]

end QOU.Core.KashaevHabiroBridge
