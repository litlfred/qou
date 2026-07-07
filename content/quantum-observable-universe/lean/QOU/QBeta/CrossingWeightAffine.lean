import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# Q_β crossing-weight affine narrowing — the ladder-factor bar-parity split

Sharpens `QOU.Interactions.QBetaCounitTrace` (registry KC18): KC18 decomposed the
**numerator** of the evaluation map `E(w) = h²/2 − h·w` into a bar-even identity
term `h²/2` and a bar-odd crossing/loop term `−h·w`. Here we analyse the object
where the `c_k` actually live — the **ladder factor** `L(w) = E(w)/E(w₀)` — and
show its bar-odd (decay) part is *linear* in the crossing-weight departure
`(w − w₀)` times a **fixed** bar-odd kernel `2h/(4w₀² − h²)`.

Bar involution: `q ↦ q⁻¹` acts as `h ↦ −h` (`h = q − q⁻¹` is bar-ODD); the
crossing weights `w, w₀` are bar-EVEN (`z` is bar-even, `QOU.QBeta.z_bar_invariant`,
KC13). So the bar image of `L(w)` is `L̄(w) = E₋(w)/E₋(w₀)` with
`E₋(w) = h²/2 + h·w`, and the even/odd parts are `(L ± L̄)/2`.

All statements hold over an arbitrary field of characteristic ≠ 2 (the
substrate→archimedean wall is not crossed: no ordering, no `Real.sqrt`).
See AGENTS.md §7c. Companion probe:
`computations/qbeta/qbeta_crossing_weight_affine_probe.py` (12/12, sympy-exact).

**No `c_k` value is produced; nothing is wired (registry §8 flip-flop guard).**
-/

namespace QOU.QBeta.CrossingWeightAffine

variable {R : Type*} [Field R]

/-- The Q_β evaluation map on the `N=0` nucleon NF difference, as a function of
    the crossing weight `w`: `E(w) = h²/2 − h·w` (`w = 1` → counit `ε`,
    `w = z` → Markov trace `tr_M`). -/
def evalMap (h w : R) : R := h ^ 2 / 2 - h * w

/-- Its bar image (`h ↦ −h`, `w` fixed): `E₋(w) = h²/2 + h·w`. -/
def evalMapBar (h w : R) : R := h ^ 2 / 2 + h * w

@[simp] theorem evalMapBar_eq (h w : R) : evalMap (-h) w = evalMapBar h w := by
  unfold evalMap evalMapBar; ring

/-- **Affine in the crossing weight.** The evaluation map differs only by the
    linear term `−h·(w − w₀)`; in particular it introduces no nonlinearity in
    `w` (`∂E/∂w = −h` is constant). Unconditional. -/
theorem evalMap_affine (h w w0 : R) :
    evalMap h w - evalMap h w0 = -h * (w - w0) := by
  unfold evalMap; ring

/-- Nonvanishing of `E(w₀) = h²/2 − h·w₀ = h(h − 2w₀)/2` from the factor
    hypotheses. -/
private theorem evalMap_ne (h w0 : R) (hh : h ≠ 0) (htwo : (2 : R) ≠ 0)
    (hw0m : h - 2 * w0 ≠ 0) : evalMap h w0 ≠ 0 := by
  unfold evalMap
  have : h ^ 2 / 2 - h * w0 = h * (h - 2 * w0) / 2 := by field_simp
  rw [this]
  exact div_ne_zero (mul_ne_zero hh hw0m) htwo

/-- **Ladder factor in lowest terms.** Multiplying `E(w)/E(w₀)` top and bottom
    by `2/h` (`h ≠ 0`) collapses the `h²/2` to the clean fractional-linear
    (Möbius) form `L(w) = (h − 2w)/(h − 2w₀)`. -/
theorem evalMap_ratio (h w w0 : R) (hh : h ≠ 0) (htwo : (2 : R) ≠ 0)
    (hw0m : h - 2 * w0 ≠ 0) :
    evalMap h w / evalMap h w0 = (h - 2 * w) / (h - 2 * w0) := by
  rw [div_eq_div_iff (evalMap_ne h w0 hh htwo hw0m) hw0m]
  unfold evalMap; field_simp

/-- Bar image `L̄(w) = E₋(w)/E₋(w₀) = (h + 2w)/(h + 2w₀)`. -/
theorem evalMapBar_ratio (h w w0 : R) (hh : h ≠ 0) (htwo : (2 : R) ≠ 0)
    (hw0p : h + 2 * w0 ≠ 0) :
    evalMapBar h w / evalMapBar h w0 = (h + 2 * w) / (h + 2 * w0) := by
  have hnegm : -h - 2 * w0 ≠ 0 := by
    rw [show -h - 2 * w0 = -(h + 2 * w0) from by ring]
    exact neg_ne_zero.mpr hw0p
  simp only [← evalMapBar_eq]
  rw [evalMap_ratio (-h) w w0 (neg_ne_zero.mpr hh) htwo hnegm,
      div_eq_div_iff hnegm hw0p]
  ring

/-- **Ladder-factor odd part.** With the reference weight `w₀`, the bar-odd
    (decay/swing) part of `L(w) = E(w)/E(w₀)` is exactly the fixed bar-odd
    kernel `2h/(4w₀² − h²)` times the crossing-weight departure `(w − w₀)`:
    LINEAR in `(w − w₀)`, no self-interaction. -/
theorem ladder_odd_part (h w w0 : R) (hh : h ≠ 0) (htwo : (2 : R) ≠ 0)
    (hw0m : h - 2 * w0 ≠ 0) (hw0p : h + 2 * w0 ≠ 0) :
    (evalMap h w / evalMap h w0 - evalMapBar h w / evalMapBar h w0) / 2
      = 2 * h * (w - w0) / (4 * w0 ^ 2 - h ^ 2) := by
  rw [evalMap_ratio h w w0 hh htwo hw0m, evalMapBar_ratio h w w0 hh htwo hw0p,
      show 4 * w0 ^ 2 - h ^ 2 = -((h - 2 * w0) * (h + 2 * w0)) from by ring]
  field_simp
  ring

/-- **Ladder-factor even part.** The bar-even (shadow/mass) part of `L(w)` is
    `(4·w·w₀ − h²)/(4w₀² − h²)` — bar-even, carrying the shadow. -/
theorem ladder_even_part (h w w0 : R) (hh : h ≠ 0) (htwo : (2 : R) ≠ 0)
    (hw0m : h - 2 * w0 ≠ 0) (hw0p : h + 2 * w0 ≠ 0) :
    (evalMap h w / evalMap h w0 + evalMapBar h w / evalMapBar h w0) / 2
      = (4 * w * w0 - h ^ 2) / (4 * w0 ^ 2 - h ^ 2) := by
  rw [evalMap_ratio h w w0 hh htwo hw0m, evalMapBar_ratio h w w0 hh htwo hw0p,
      show 4 * w0 ^ 2 - h ^ 2 = -((h - 2 * w0) * (h + 2 * w0)) from by ring]
  field_simp
  ring

/-- **`c₂ = −1` reference identity.** At the counit reference `w₀ = 1`, the
    ladder factor minus one is `−2·(w − 1)/(h − 2)` — the fixed anchor-free
    map from the crossing-weight departure `(w − 1)` into the ladder. -/
theorem ladder_counit_ref (h w : R) (hh : h ≠ 0) (htwo : (2 : R) ≠ 0)
    (hh2 : h - 2 ≠ 0) :
    evalMap h w / evalMap h 1 - 1 = -2 * (w - 1) / (h - 2) := by
  have hh2' : h - 2 * 1 ≠ 0 := by rw [mul_one]; exact hh2
  rw [evalMap_ratio h w 1 hh htwo hh2', mul_one]
  field_simp
  ring

end QOU.QBeta.CrossingWeightAffine
