import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Polyrith
import QOU.Archimedean.BringFaddeevH4LinkingWeight

/-!
# Bring color-tube — closed forms in q (no `heckeH`)

Provides **q-rational closed forms** for the Bring color-tube
linking_weight component and the Faddeev h⁴ component. The original
definitions in `BringFaddeevH4LinkingWeight.lean` use the parameter
`heckeH q = q − q⁻¹`; here we eliminate `heckeH` and express
everything as a rational function in `q` only.

Why: rational-in-q forms unblock several downstream proofs:

| theorem | unlocked by |
|---|---|
| Polynomial identity tests via `ring` | q-rational form |
| Numerical bounds at `q₀ ≈ 1.110` via `norm_num` on rationals | q-rational form |
| h-expansion via formal-power-series substitution | q-rational form + power-series infra (next file) |
| Cross-comparison with Family A's `(3q² + 4 + 3q⁻²)/4` | q-rational form |

## The closed forms

**Bring color-tube**:
```
1 / (1 - h_q · q^10)  =  1 / (1 - (q - q⁻¹) · q^{10})
                       =  1 / (1 - q^{11} + q^9)
                       =  q⁰ / (1 + q^9 - q^{11})
```

**Faddeev h⁴**:
```
1 / (1 - h_q⁴)  =  1 / (1 - (q - q⁻¹)⁴)
                =  q⁴ / (q⁴ - (q - q⁻¹)⁴ · q⁴)
                =  q⁴ / (q⁴ · 1 - (q² - 1)⁴ / q⁴ · q⁴)         (multiply by q⁴/q⁴)
                =  q⁴ / (q⁴ - (q² - 1)⁴ / q⁰)
```

We give the first one directly (clean integer polynomial denominator);
the second is handled via the expanded `(q - q⁻¹)⁴ = (q² - 1)⁴ / q⁴`
auxiliary.

## References

- [`docs/audits/2026-05-25-m-p-m-n-full-chain-audit.md`](../../../../../docs/audits/2026-05-25-m-p-m-n-full-chain-audit.md) §4a
- [`folio-assistant/computations/m_p_bring_plus_faddeev_h4_probe.py`](../../../../../folio-assistant/computations/m_p_bring_plus_faddeev_h4_probe.py)
-/

namespace QOU.Archimedean

open Real

/-! ## §1  Polynomial denominator of Bring color-tube -/

/-- The polynomial denominator of `bringColorTube q` in `q`:
    `bringColorTubeDen q := 1 + q^9 − q^{11}`.

    This is the result of expanding `1 − (q − q⁻¹) · q^{10}` and
    multiplying through by 1 (no clearing needed; the `q⁻¹` cancels
    cleanly against `q^{10}`):

      1 − (q − q⁻¹) · q^{10}
      = 1 − q · q^{10} + q⁻¹ · q^{10}
      = 1 − q^{11} + q^9
      = 1 + q^9 − q^{11}.
    -/
noncomputable def bringColorTubeDen (q : ℝ) : ℝ := 1 + q ^ 9 - q ^ 11

/-- **Closed-form identity (Bring denominator).** For any `q ≠ 0`,

      `1 − heckeH q · q^{10} = (1 + q^9 − q^{11}) / 1 = bringColorTubeDen q`.

    No `q⁻¹` survives; this is a polynomial identity in `q`. -/
theorem one_sub_heckeH_pow_ten_eq_bringDen (q : ℝ) (hq : q ≠ 0) :
    1 - heckeH q * q ^ 10 = bringColorTubeDen q := by
  unfold heckeH bringColorTubeDen
  field_simp
  ring

/-- **Bring color-tube in q-rational form (no `heckeH`).**

    For `q ≠ 0` (so `heckeH` is well-defined) and `bringColorTubeDen
    q ≠ 0` (so the reciprocal exists):

      `bringColorTube q = 1 / (1 + q^9 − q^{11})`.

    This is the production formula stripped of all `heckeH`
    references — a clean rational function in `q`. -/
theorem bringColorTube_q_form (q : ℝ) (hq : q ≠ 0)
    (hden : bringColorTubeDen q ≠ 0) :
    bringColorTube q = 1 / bringColorTubeDen q := by
  unfold bringColorTube
  rw [one_sub_heckeH_pow_ten_eq_bringDen q hq]

/-! ## §2  Polynomial form of `(q - q⁻¹)⁴` -/

/-- The expanded form of `(q − q⁻¹)⁴` as a Laurent polynomial in q:

      `(q − q⁻¹)⁴ = q⁴ − 4q² + 6 − 4q⁻² + q⁻⁴`.

    Cleared denominator (× q⁴):

      `q⁴ · (q − q⁻¹)⁴ = q^8 − 4q^6 + 6q⁴ − 4q² + 1`.
    -/
theorem heckeH_fourth_clear (q : ℝ) (hq : q ≠ 0) :
    q ^ 4 * (heckeH q) ^ 4 = q ^ 8 - 4 * q ^ 6 + 6 * q ^ 4 - 4 * q ^ 2 + 1 := by
  unfold heckeH
  field_simp
  ring

/-- The polynomial denominator of `faddeevH4 q` after clearing `q⁻¹`:

      `q⁴ · (1 − (q − q⁻¹)⁴) = q^4 − (q^8 − 4q^6 + 6q^4 − 4q² + 1)
                              = −q^8 + 4q^6 − 5q⁴ + 4q² − 1`.

    Multiplied by `−1` for sign cleanliness:

      `faddeevH4Den q := q^8 − 4q^6 + 5q⁴ − 4q² + 1`.
    -/
noncomputable def faddeevH4Den (q : ℝ) : ℝ :=
  q ^ 8 - 4 * q ^ 6 + 5 * q ^ 4 - 4 * q ^ 2 + 1

/-- Recurrence identity for `faddeevH4Den`: it equals `-q⁴ · (1 − h⁴)`
    when expanded:

      `faddeevH4Den q = q^4 · h^4 − q^4 + 0 = q^4 · ((q-q⁻¹)^4 − 1)`.

    More usefully:

      `q^4 · (1 − (q − q⁻¹)^4) = −faddeevH4Den q + 2 · q^4`

    No wait — let me redo: `q^4 · (1 − h^4) = q^4 − q^4 · h^4
                                              = q^4 − (q^8 − 4q^6 + 6q^4 − 4q^2 + 1)
                                              = −q^8 + 4q^6 − 5q^4 + 4q^2 − 1
                                              = −(q^8 − 4q^6 + 5q^4 − 4q^2 + 1)
                                              = −faddeevH4Den q`. -/
theorem q4_one_sub_heckeH4 (q : ℝ) (hq : q ≠ 0) :
    q ^ 4 * (1 - (heckeH q) ^ 4) = -(faddeevH4Den q) := by
  rw [mul_sub_one, heckeH_fourth_clear q hq]
  unfold faddeevH4Den
  ring

/-- **Faddeev h⁴ in q-rational form (no `heckeH`).**

    For `q ≠ 0` and `faddeevH4Den q ≠ 0`:

      `faddeevH4 q = -q^4 / faddeevH4Den q`.

    Note the negative sign: `q^4 · (1 − h⁴) = −faddeevH4Den q`, so
    `1 / (1 − h⁴) = q^4 / (q^4 (1 − h⁴)) = q^4 / (−faddeevH4Den q)
                = −q^4 / faddeevH4Den q`. -/
theorem faddeevH4_q_form (q : ℝ) (hq : q ≠ 0)
    (hden : faddeevH4Den q ≠ 0)
    (h1mh4 : 1 - (heckeH q) ^ 4 ≠ 0) :
    faddeevH4 q = -(q ^ 4) / faddeevH4Den q := by
  unfold faddeevH4
  have h_q4_ne : q ^ 4 ≠ 0 := pow_ne_zero 4 hq
  rw [show (1 : ℝ) / (1 - (heckeH q) ^ 4) =
    q ^ 4 / (q ^ 4 * (1 - (heckeH q) ^ 4)) by
    rw [mul_div_mul_left _ _ h_q4_ne]]
  rw [q4_one_sub_heckeH4 q hq]
  field_simp

/-! ## §3  Values at q = 1 -/

/-- At `q = 1`, `bringColorTubeDen = 1 + 1 − 1 = 1`. -/
theorem bringColorTubeDen_at_one : bringColorTubeDen 1 = 1 := by
  unfold bringColorTubeDen
  norm_num

theorem bringColorTubeDen_at_one_ne_zero : bringColorTubeDen 1 ≠ 0 := by
  rw [bringColorTubeDen_at_one]; exact one_ne_zero

/-- At `q = 1`, `faddeevH4Den = 1 − 4 + 5 − 4 + 1 = −1`.

    Note: this is non-zero (= −1), and the negative reciprocal
    `−1 / (−1) = 1` recovers `faddeevH4 1 = 1` ✓. -/
theorem faddeevH4Den_at_one : faddeevH4Den 1 = -1 := by
  unfold faddeevH4Den
  norm_num

theorem faddeevH4Den_at_one_ne_zero : faddeevH4Den 1 ≠ 0 := by
  rw [faddeevH4Den_at_one]; norm_num

/-- Cross-check: q-form at q=1 recovers `bringColorTube_at_one`. -/
example : (1 : ℝ) / bringColorTubeDen 1 = 1 := by
  rw [bringColorTubeDen_at_one]; norm_num

/-- Cross-check: q-form at q=1 recovers `faddeevH4_at_one`. -/
example : -(((1 : ℝ)) ^ 4) / faddeevH4Den 1 = 1 := by
  rw [faddeevH4Den_at_one]; norm_num

/-! ## §4  Polynomial form of the combined linking_weight -/

/-- The combined `linkingWeightBringFaddeevH4` written as a SINGLE
    rational function in `q` (no `heckeH`, no separate components):

      `linkingWeightBringFaddeevH4 q = (faddeevH4Den q − q^4 · bringColorTubeDen q − bringColorTubeDen q · faddeevH4Den q)`
                                       `/ (bringColorTubeDen q · faddeevH4Den q)`.

    This is the algebraic substrate of the candidate; downstream proofs
    (numerical bounds at q₀, comparison with Reading-A's `5/2 − G·h²`,
    h-expansion coefficient theorems) all flow through this form. -/
theorem linkingWeightBringFaddeevH4_q_form (q : ℝ) (hq : q ≠ 0)
    (hb : bringColorTubeDen q ≠ 0)
    (hf : faddeevH4Den q ≠ 0)
    (h1mh4 : 1 - (heckeH q) ^ 4 ≠ 0) :
    linkingWeightBringFaddeevH4 q =
      (1 / bringColorTubeDen q) + (-(q ^ 4) / faddeevH4Den q) - 1 := by
  unfold linkingWeightBringFaddeevH4
  rw [bringColorTube_q_form q hq hb, faddeevH4_q_form q hq hf h1mh4]

end QOU.Archimedean
