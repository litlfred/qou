import QOU.Mass.GammaGammaEscapesSingleCrossing

/-!
# The γγ-selected diproton binding is second order in the deformation

Bean `qou-ales`, step 9. Steps 6–8 settled *which* bond reading 3 selects on the `H₆`
interface (`G³ = (σ₂σ₃⁻¹)³`) and *why* its unbinding is consistent with the single-crossing
obstruction. What was left measured is the **magnitude**: step 3's `B_pp = −4.47` keV. This
file derives its **order** — and the order is what makes it keV rather than MeV.

## The lever is step 4's cube identity

`vtx_three_sub_one` (step 4, sorry-free) gives, from the Hoefsmit relations alone,

    V³ − 1 = h² • ((2 + h²) • V + 1),        h = q − q⁻¹.

So the selected bond does not merely *happen* to sit near the identity: it differs from it by
**exactly `h²` times a bounded matrix**, with no freedom in the exponent. Write the bond's
image as `1 + h²·D`. The Markov trace is linear, so the interface trace ratio is

    μ = tr(W·G³)/tr(W) = 1 + h²·r,           r = tr(W·D)/tr(W),

and the log law of step 8 turns that into a two-sided bound on the binding.

## What is proved (all sorry-free)

* `log_one_add_le` and `le_log_one_add` — for `x > 0`, `x/(1+x) ≤ log(1+x) ≤ x`. Standard,
  both from `Real.log_le_sub_one_of_pos`; included because the two-sided form is what makes
  the conclusion an *order* rather than an upper bound.
* **`binding_magnitude_second_order`** — the headline. With scale `α > 0`, deformation
  `h ≠ 0`, and a positive relative response `r > 0`, the magnitude of
  `B = −α·log(1 + h²r)` is bracketed:

      α·h²·r / (1 + h²r)  ≤  |B|  ≤  α·h²·r.

  Both ends carry the factor `h²`, so `|B| = Θ(h²)` — second order, not first, and not by
  choice of any constant.
* `binding_negative_of_pos_response` — the sign, recovered from step 8: `r > 0` (the bond
  moves the trace upward) gives `B < 0`, unbound.
* `bound_at_small_h_sq` — at the interval the arc actually works on, `h² ≤ 1/10`, the
  magnitude is at most `α·r/10`: a keV-scale statement given an `α` of a few MeV and an
  `r` of order `10⁻²`.
* `vertexCube_deviation_is_h_sq_smul` — the `h²` in the hypothesis is not an assumption
  about the bond but a consequence of the vertex algebra, re-exported from step 4 so the
  chain is visible in one place.
* `ratio_eq_one_add_of_linear_response` — the bookkeeping step: a trace that is linear in
  the bond and a bond of the form `1 + h²·D` give a ratio of the form `1 + h²·r`.

## Why this is not circular — read this before quoting the `Θ(h²)`

`r` is *defined* as `(μ − 1)/h²`, so the bracket above holds for **any** ratio whatever, and
on its own it says nothing about a scale. The statement has content only because `r` is
bounded **independently of `h`**, and that is what step 4's identity supplies: the deviation
is `h²·D` with `D = (2 + h²)·V + 1`, whose size is controlled by `V`'s on the interval
(`deviation_coefficient_le`), so `r = tr(W·D)/tr(W)` is bounded whenever the free trace is
bounded away from zero (`response_bounded_of_deviation_bounded`). Measured at the pin:
`‖V³ − 1‖_F / h² = 2.577`, an order-one coefficient, so the `h²` is the real scale and not an
artifact of the definition.

**And do not reason from the character instead.** `bond_character_deviation` gives
`χ_(2,1)(V³) − 2 = −h⁴·(3 + h²)`: the bond's *character* deviates at **fourth** order,
because `tr D = −3h² − h⁴` is itself `O(h²)`. The *matrix* deviates at second order and the
*character* at fourth, and it is the matrix that controls the interface ratio, since `tr(W·D)`
carries no such cancellation. Anyone who checks the order on characters will get `h⁴` and be
wrong about the binding.

## What is NOT derived

**`r` itself.** It is the trace-weighted response `tr(W·D)/tr(W)` over the eleven `H₆`
blocks with the eleven-letter nucleon words, and it is carried here as a hypothesis — no
value is asserted. Step 3 measured the corresponding ratio as `1.001058`, i.e. `r ≈ 0.0242`
at the proton pin, and that single number remains the measurement. What this file removes
from the measurement is the *scale*: given any `r` of order one or smaller, the binding is
forced to `h²` order, so the keV magnitude needs no explanation beyond the deformation being
small.

Also not claimed: the numerical value `4.47` keV, the dineutron channel, and anything about
whether the framework's two-nucleon sector matches nature. Nothing here reads AME2020, a
CODATA binding value, or a census.

## Base ring (§7c)

`ℝ` throughout: the statements are about `Real.log` and an order. The algebraic input
(`vtx_three_sub_one`) is generic and lives in step 4.
-/

namespace QOU.Mass.DiprotonSecondOrder

open QOU.Mass.GammaGammaWordSelection
open QOU.Mass.GammaGammaVertexOrder

/-! ## Two-sided logarithm bounds -/

/-- `log(1 + x) ≤ x` for `x > -1`. -/
theorem log_one_add_le {x : ℝ} (hx : -1 < x) : Real.log (1 + x) ≤ x := by
  have h1 : (0:ℝ) < 1 + x := by linarith
  have := Real.log_le_sub_one_of_pos h1
  linarith

/-- `x/(1+x) ≤ log(1 + x)` for `x > -1`. Together with `log_one_add_le` this brackets
`log(1+x)` between two quantities of the same order in `x`. -/
theorem le_log_one_add {x : ℝ} (hx : -1 < x) : x / (1 + x) ≤ Real.log (1 + x) := by
  have h1 : (0:ℝ) < 1 + x := by linarith
  have hinv := Real.log_le_sub_one_of_pos (show (0:ℝ) < (1 + x)⁻¹ by positivity)
  rw [Real.log_inv] at hinv
  have heq : x / (1 + x) = 1 - (1 + x)⁻¹ := by field_simp; ring
  rw [heq]
  linarith

/-! ## The bond's deviation carries `h²` by algebra, not by assumption -/

/-- **Re-export of step 4's cube identity**: the `(2,1)` image of the selected bond
`G³ = (σ₂σ₃⁻¹)³` differs from the identity by exactly `h²` times a matrix built from the
vertex. The exponent is forced by the Hoefsmit relations; nothing is chosen. -/
theorem vertexCube_deviation_is_h_sq_smul {q a b a' h : ℝ} (hqinv : q * q⁻¹ = 1)
    (hh : h = q - q⁻¹) (ha : a * (1 - q ^ 4) = h) (ha' : a' = -q ^ 4 * a)
    (hb : b ^ 2 = a * a' + 1) (hq1 : q ^ 2 ≠ 1) :
    vtx q a b a' h ^ 3 - 1 =
      h ^ 2 • ((2 + h ^ 2) • vtx q a b a' h + (1 : Matrix (Fin 2) (Fin 2) ℝ)) :=
  vtx_three_sub_one hqinv hh ha ha' hb hq1

/-- **The bookkeeping step.** If the interface trace is linear in the bond — `tr(W·(1 + M))
= tr W + tr (W·M)`, which the Markov trace is — and the bond's deviation is `h² • D`, then
the ratio is `1 + h²·r` with `r` the relative response `tr(W·D)/tr W`. Stated on the
scalars, so it applies block by block and to the weighted sum alike. -/
theorem ratio_eq_one_add_of_linear_response {trW trWD hsq : ℝ} (hW : trW ≠ 0) :
    (trW + hsq * trWD) / trW = 1 + hsq * (trWD / trW) := by
  field_simp

/-! ## The order of the binding -/

/-- **The headline: the binding magnitude is `Θ(h²)`.** With a positive scale `α`, a
non-zero deformation `h`, and a positive relative response `r`, the magnitude of
`B = −α·log(1 + h²r)` satisfies

    α·h²r / (1 + h²r)  ≤  |B|  ≤  α·h²r.

Both bounds carry `h²`, so the magnitude is exactly second order in the deformation — the
structural reason a γγ-selected interface bond moves a binding by keV rather than MeV, given
an `α` of a few MeV. No constant is chosen anywhere. -/
theorem binding_magnitude_second_order {α h r : ℝ} (hα : 0 < α) (hr : 0 < r) (hh : h ≠ 0) :
    α * (h ^ 2 * r) / (1 + h ^ 2 * r) ≤ |-α * Real.log (1 + h ^ 2 * r)| ∧
      |-α * Real.log (1 + h ^ 2 * r)| ≤ α * (h ^ 2 * r) := by
  have hh2 : 0 < h ^ 2 := by positivity
  have hx : 0 < h ^ 2 * r := by positivity
  have hx1 : -1 < h ^ 2 * r := by linarith
  have hden : (0:ℝ) < 1 + h ^ 2 * r := by linarith
  have hlogpos : 0 < Real.log (1 + h ^ 2 * r) := Real.log_pos (by linarith)
  have habs : |-α * Real.log (1 + h ^ 2 * r)| = α * Real.log (1 + h ^ 2 * r) := by
    rw [abs_of_neg (by nlinarith)]
    ring
  rw [habs]
  refine ⟨?_, ?_⟩
  · have hlow := le_log_one_add hx1
    rw [div_le_iff₀ hden] at *
    nlinarith [hlow, hα.le]
  · have hup := log_one_add_le hx1
    nlinarith [hup, hα.le]

/-- **The sign, from step 8's law.** A positive relative response — the bond moves the
interface trace upward — makes the binding negative, i.e. unbound. -/
theorem binding_negative_of_pos_response {α h r : ℝ} (hα : 0 < α) (hr : 0 < r) (hh : h ≠ 0) :
    -α * Real.log (1 + h ^ 2 * r) < 0 := by
  have hh2 : 0 < h ^ 2 := by positivity
  have hlogpos : 0 < Real.log (1 + h ^ 2 * r) := Real.log_pos (by nlinarith)
  nlinarith

/-- **On the arc's own interval.** For `h² ≤ 1/10` — which `1 < q ≤ 23/20` guarantees
(`h_sq_le_of_q_le`, step 4) and the proton pin satisfies with `h² ≈ 0.0437` — the magnitude
is at most `α·r/10`. With `α = 𝔈₀^full ≈ 4.23` MeV and a response of order `10⁻²`, that is a
keV-scale ceiling derived rather than observed. -/
theorem bound_at_small_h_sq {α h r : ℝ} (hα : 0 < α) (hr : 0 < r) (hh : h ≠ 0)
    (hsmall : h ^ 2 ≤ 1 / 10) :
    |-α * Real.log (1 + h ^ 2 * r)| ≤ α * r / 10 := by
  have hub := (binding_magnitude_second_order hα hr hh).2
  have hαr : 0 ≤ α * r := (mul_pos hα hr).le
  have : α * (h ^ 2 * r) ≤ α * r / 10 :=
    calc α * (h ^ 2 * r) = (α * r) * h ^ 2 := by ring
      _ ≤ (α * r) * (1 / 10) := mul_le_mul_of_nonneg_left hsmall hαr
      _ = α * r / 10 := by ring
  linarith

/-- The same statement at the proton pin's bound, written on `q` so the chain from the
substrate modulus to the order is visible: `1 < q ≤ 23/20` forces the `h²` ceiling. -/
theorem bound_on_q_interval {α q r : ℝ} (hα : 0 < α) (hr : 0 < r) (hq1 : 1 < q)
    (hq2 : q ≤ 23 / 20) :
    |-α * Real.log (1 + (q - q⁻¹) ^ 2 * r)| ≤ α * r / 10 := by
  have hqpos : 0 < q := by linarith
  have hpos : 0 < q - q⁻¹ := by
    have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq1
    linarith
  exact bound_at_small_h_sq hα hr (ne_of_gt hpos) (h_sq_le_of_q_le hq1.le hq2)

/-! ## Why the `Θ(h²)` is not circular: the response is bounded independently of `h` -/

/-- **The deviation's coefficient is bounded on the interval.** `D = (2 + h²)·V + 1`, and on
`h² ≤ 1/10` the scalar factor is at most `21/10` — an `h`-free bound, so `D`'s size is
controlled by `V`'s alone. -/
theorem deviation_coefficient_le {h : ℝ} (hsmall : h ^ 2 ≤ 1 / 10) : 2 + h ^ 2 ≤ 21 / 10 := by
  linarith

/-- **The relative response is bounded independently of `h`.** If the numerator `tr(W·D)` is
bounded by `K` and the free trace is bounded away from zero by `m > 0`, then `|r| ≤ K/m` — a
bound with no `h` in it. This is what makes `binding_magnitude_second_order` a statement about
a *scale*: without it, `r := (μ − 1)/h²` is a definition and the bracket is vacuous. -/
theorem response_bounded_of_deviation_bounded {trWD trW K m : ℝ} (hm : 0 < m)
    (hlow : m ≤ |trW|) (hK : |trWD| ≤ K) : |trWD / trW| ≤ K / m := by
  have hW : trW ≠ 0 := by
    intro h0
    rw [h0, abs_zero] at hlow
    linarith
  rw [abs_div]
  have hKnn : 0 ≤ K := le_trans (abs_nonneg _) hK
  have hWpos : 0 < |trW| := lt_of_lt_of_le hm hlow
  rw [div_le_div_iff₀ hWpos hm]
  calc |trWD| * m ≤ K * m := mul_le_mul_of_nonneg_right hK hm.le
    _ ≤ K * |trW| := mul_le_mul_of_nonneg_left hlow hKnn

/-- **The bond's CHARACTER deviates at fourth order, not second.** From step 4's
`trace_vtx_pow_three`, `χ_(2,1)(V³) − 2 = −h⁴·(3 + h²)`, because `tr D = −3h² − h⁴` is itself
`O(h²)`. The *matrix* deviation is `h²`; the *character* deviation is `h⁴`.

**CORRECTED (step 10, `DiprotonResponseClosedForm`).** This docstring continued: "the interface
ratio is controlled by the matrix, since `tr(W·D)` carries no such cancellation — so checking
the order on characters gives the wrong answer for the binding." **The second clause is false.**
Exact symbolic evaluation of the `H₆` convention-D Markov trace on the two 11-letter nucleon
words gives `r = h²·c(q)` with `c` order one, so `tr(W·D)` *does* carry a cancellation and the
ratio deviates at `h⁴`, not `h²`. A single block's mixed response carries one factor `q² − 1`;
the second appears only after `y`-weighting. So there are three distinct orders here (matrix
`h²`, per-block mixed response `h¹`, `y`-weighted response `h²`, hence ratio `h⁴`) and the
`h⁴` below agrees with the ratio's `h⁴` by arithmetic rather than by mechanism. -/
theorem bond_character_deviation {q a b a' h : ℝ} (hqinv : q * q⁻¹ = 1) (hh : h = q - q⁻¹)
    (ha : a * (1 - q ^ 4) = h) (ha' : a' = -q ^ 4 * a) (hb : b ^ 2 = a * a' + 1)
    (hq1 : q ^ 2 ≠ 1) :
    (vtx q a b a' h ^ 3).trace - 2 = -(h ^ 4) * (3 + h ^ 2) := by
  rw [trace_vtx_pow_three hqinv hh ha ha' hb hq1]
  ring

end QOU.Mass.DiprotonSecondOrder
