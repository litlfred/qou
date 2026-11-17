import QOU.Mass.DiprotonSecondOrder

/-!
# The γγ-selected diproton response in closed form — and it is FOURTH order, not second

Bean `qou-ales`, step 10. Step 9 left exactly one quantity measured: the trace-weighted
response

    r = tr(W·D) / tr(W),        D = (G³ − 1)/h²,   W = the two free 11-letter nucleon words,

carried there as a bare positive hypothesis. This file carries its **closed form**, obtained
by exact symbolic evaluation of the convention-D Markov trace on `H₆` over `ℚ(q)` — every
letter of both nucleon words and of the bond, all four weight-support blocks, no numerics and
no anchor. With

    P(q) = q¹⁸ − 3q¹⁶ + 7q¹⁴ − 8q¹² + 10q¹⁰ − 9q⁸ + 10q⁶ − 6q⁴ + 3q² − 1      (`nucleonPoly`)
    R(q) = q¹⁰ − q⁸ + 4q⁶ − 4q⁴ + 2q² − 1                                     (`responsePoly`)

the computation gives

    r(q) = (q² − 1)²·(q⁴ + q² + 1)·R(q) / ((q² + 1)·P(q)).

## The correction this forces on step 9

`(q² − 1)² = q²h²`, so **`r` itself carries a factor `h²`**:

    r(q) = h²·c(q),      c(q) = q²(q⁴ + q² + 1)R(q) / ((q² + 1)P(q)),

and therefore the interface ratio is

    μ − 1 = h²·r = h⁴·c(q),

so the binding magnitude is **`Θ(h⁴)`, not `Θ(h²)`**. Step 9's bracket is correct as stated —
`r` is a free hypothesis there — but its *headline order* is two powers too weak, and the
reason is precisely the one step 9's own correction considered and dismissed: it asserted that
`tr(W·D)` "carries no such cancellation". It does. Measured at the pin: `c = 0.5537297`, an
order-one number, and `h⁴c = 0.00105775` reproduces step 3's ratio `1.0010577525451598436`
to every digit it carries.

Three different orders are in play and conflating any two of them is the trap:

| quantity | order in `h` |
|---|---|
| the bond's **matrix** deviation `G³ − 1` | `h²`  (step 4, `vtx_three_sub_one`) |
| the bond's **character** deviation `χ_(2,1)(V³) − 2` | `h⁴`  (step 9, `bond_character_deviation`) |
| a **single block's** mixed response `(χ_λ(WG³) − χ_λ(W))/h²` | `h¹`  (one factor `q² − 1`) |
| the **`y`-weighted** response `r` | `h²` — the extra power appears only after weighting |

So the `h⁴` of the ratio and the `h⁴` of the bond's own character are *not the same fact*;
they arise from different cancellations and agree by arithmetic, not by mechanism.

## What is proved here (all sorry-free)

* `nucleonPoly_pos`, `responsePoly_pos` — `P(q) ≥ 4` and `R(q) ≥ 1` for every `q ≥ 1`, by
  re-expanding in `t = q − 1`: **every** coefficient of `P(1+t)` and `R(1+t)` is non-negative.
* `responseCoeff_pos` and `responseCoeff_le_one` — `0 < c(q) ≤ 1` for every `q ≥ 1`. The upper
  bound is the same mechanism: `(q²+1)P(q) − q²(q⁴+q²+1)R(q)` has non-negative coefficients in
  `t` with constant term `5`. Both bounds hold on the whole ray, with no interval hypothesis.
* `respPP_eq_hSq_mul_coeff` — the factorisation `r = h²c`, the step-9 correction in one line.
* **`diproton_unbound_of_response_closed_form`** — for **every** `q > 1` the γγ-selected
  diproton is unbound. No measurement, no interval: `c > 0` forces `μ > 1` forces `B < 0`.
* **`binding_magnitude_fourth_order`** — the step-9 bracket at the derived response, with both
  ends carrying `h⁴`.
* **`binding_ceiling_on_interval`** — on `1 < q ≤ 23/20`, `|B| ≤ α/100`. Since `α` is a closed
  form in `q` and CAL-1 `m_e`, this is a **fully derived keV ceiling**: at the pin
  `α/100 = 42.27` keV against the actual `4.469` keV. The deformation alone forces the scale.
* `ResponseClosedForm` — the one hypothesis that remains: that the `H₆` convention-D Markov
  trace of these words *is* the rational function above. That is a statement about the
  Hoefsmit/branching machinery, verified by the probe to 60 dps against two independent code
  paths (symbolic `ℚ(q)` and the mpmath seminormal path of step 3), not proved in Lean.
* `nucleonTrace` and the `ResponseClosedForm.free_eq` field — the free trace factorises as the
  square of the single nucleon's `H₃` trace, disjoint-union multiplicativity, recorded because
  it is what makes the denominator of `c` a *nucleon* quantity rather than a two-body one.

## Scope

The word is step 3's: the canonical 11-letter nucleon element (which, since `7db032fb48`,
opens with `β_Bor = (σ₀σ₁⁻¹)³`) on generators `(0,1)` and `(3,4)`, with the colour-blind
`−h/2` interface letters, and the bond `G³ = (σ₂σ₃⁻¹)³` on `(2,3)`. Nothing here reads AME2020,
a CODATA binding value, or a census. The dineutron channel and the `p`–`n` asymmetry are
untouched.
-/

namespace QOU.Mass.DiprotonResponseClosedForm

open QOU.Mass.DiprotonSecondOrder
open QOU.Mass.GammaGammaVertexOrder

/-! ## The two polynomials, and their positivity on `q ≥ 1` -/

/-- `P(q)`: the numerator of the single nucleon's `H₃` convention-D Markov trace on the
canonical 11-letter element. -/
def nucleonPoly (q : ℝ) : ℝ :=
  q ^ 18 - 3 * q ^ 16 + 7 * q ^ 14 - 8 * q ^ 12 + 10 * q ^ 10 - 9 * q ^ 8 + 10 * q ^ 6
    - 6 * q ^ 4 + 3 * q ^ 2 - 1

/-- `R(q)`: the numerator of the `G³` response. -/
def responsePoly (q : ℝ) : ℝ :=
  q ^ 10 - q ^ 8 + 4 * q ^ 6 - 4 * q ^ 4 + 2 * q ^ 2 - 1

/-- **`P` re-expanded at `q = 1 + t`: every coefficient is non-negative.** This is the whole
positivity argument; the constant term is `4`. -/
theorem nucleonPoly_shifted (q : ℝ) :
    nucleonPoly q =
      4 + 42 * (q - 1) + 217 * (q - 1) ^ 2 + 796 * (q - 1) ^ 3 + 2261 * (q - 1) ^ 4
        + 5218 * (q - 1) ^ 5 + 10027 * (q - 1) ^ 6 + 16320 * (q - 1) ^ 7
        + 22650 * (q - 1) ^ 8 + 26654 * (q - 1) ^ 9 + 26223 * (q - 1) ^ 10
        + 21172 * (q - 1) ^ 11 + 13733 * (q - 1) ^ 12 + 6986 * (q - 1) ^ 13
        + 2707 * (q - 1) ^ 14 + 768 * (q - 1) ^ 15 + 150 * (q - 1) ^ 16
        + 18 * (q - 1) ^ 17 + (q - 1) ^ 18 := by
  unfold nucleonPoly; ring

/-- **`R` re-expanded at `q = 1 + t`**, constant term `1`, all coefficients non-negative. -/
theorem responsePoly_shifted (q : ℝ) :
    responsePoly q =
      1 + 14 * (q - 1) + 55 * (q - 1) ^ 2 + 128 * (q - 1) ^ 3 + 196 * (q - 1) ^ 4
        + 220 * (q - 1) ^ 5 + 186 * (q - 1) ^ 6 + 112 * (q - 1) ^ 7 + 44 * (q - 1) ^ 8
        + 10 * (q - 1) ^ 9 + (q - 1) ^ 10 := by
  unfold responsePoly; ring

/-- `4 ≤ P(q)` for every `q ≥ 1`. -/
theorem four_le_nucleonPoly {q : ℝ} (hq : 1 ≤ q) : 4 ≤ nucleonPoly q := by
  have ht : (0:ℝ) ≤ q - 1 := by linarith
  have h1 := pow_nonneg ht 2
  have h2 := pow_nonneg ht 3
  have h3 := pow_nonneg ht 4
  have h4 := pow_nonneg ht 5
  have h5 := pow_nonneg ht 6
  have h6 := pow_nonneg ht 7
  have h7 := pow_nonneg ht 8
  have h8 := pow_nonneg ht 9
  have h9 := pow_nonneg ht 10
  have h10 := pow_nonneg ht 11
  have h11 := pow_nonneg ht 12
  have h12 := pow_nonneg ht 13
  have h13 := pow_nonneg ht 14
  have h14 := pow_nonneg ht 15
  have h15 := pow_nonneg ht 16
  have h16 := pow_nonneg ht 17
  have h17 := pow_nonneg ht 18
  rw [nucleonPoly_shifted]
  linarith

/-- `0 < P(q)` for every `q ≥ 1`. -/
theorem nucleonPoly_pos {q : ℝ} (hq : 1 ≤ q) : 0 < nucleonPoly q :=
  lt_of_lt_of_le (by norm_num) (four_le_nucleonPoly hq)

/-- `1 ≤ R(q)` for every `q ≥ 1`. -/
theorem one_le_responsePoly {q : ℝ} (hq : 1 ≤ q) : 1 ≤ responsePoly q := by
  have ht : (0:ℝ) ≤ q - 1 := by linarith
  have h1 := pow_nonneg ht 2
  have h2 := pow_nonneg ht 3
  have h3 := pow_nonneg ht 4
  have h4 := pow_nonneg ht 5
  have h5 := pow_nonneg ht 6
  have h6 := pow_nonneg ht 7
  have h7 := pow_nonneg ht 8
  have h8 := pow_nonneg ht 9
  have h9 := pow_nonneg ht 10
  rw [responsePoly_shifted]
  linarith

/-- `0 < R(q)` for every `q ≥ 1`. -/
theorem responsePoly_pos {q : ℝ} (hq : 1 ≤ q) : 0 < responsePoly q :=
  lt_of_lt_of_le (by norm_num) (one_le_responsePoly hq)

/-! ## The response and its order-one coefficient -/

/-- **`c(q)`**: the order-one coefficient of the response. -/
noncomputable def responseCoeff (q : ℝ) : ℝ :=
  q ^ 2 * (q ^ 4 + q ^ 2 + 1) * responsePoly q / ((q ^ 2 + 1) * nucleonPoly q)

/-- **`r(q)`**: the trace-weighted response `tr(W·D)/tr(W)` in closed form. -/
noncomputable def respPP (q : ℝ) : ℝ :=
  (q ^ 2 - 1) ^ 2 * (q ^ 4 + q ^ 2 + 1) * responsePoly q / ((q ^ 2 + 1) * nucleonPoly q)

/-- The denominator is positive on `q ≥ 1`. -/
theorem denom_pos {q : ℝ} (hq : 1 ≤ q) : 0 < (q ^ 2 + 1) * nucleonPoly q := by
  have h1 : (0:ℝ) < q ^ 2 + 1 := by positivity
  exact mul_pos h1 (nucleonPoly_pos hq)

/-- **`0 < c(q)` for every `q ≥ 1`** — with no interval hypothesis. -/
theorem responseCoeff_pos {q : ℝ} (hq : 1 ≤ q) : 0 < responseCoeff q := by
  have hqpos : (0:ℝ) < q := by linarith
  have hnum : 0 < q ^ 2 * (q ^ 4 + q ^ 2 + 1) * responsePoly q := by
    have hq2 : (0:ℝ) < q ^ 2 := pow_pos hqpos 2
    have hq4 : (0:ℝ) < q ^ 4 + q ^ 2 + 1 := by positivity
    exact mul_pos (mul_pos hq2 hq4) (responsePoly_pos hq)
  unfold responseCoeff
  exact div_pos hnum (denom_pos hq)

/-- **The upper bound's mechanism**: `(q²+1)P − q²(q⁴+q²+1)R` re-expanded at `q = 1 + t` has
every coefficient non-negative, with constant term `5`. -/
theorem coeff_gap_shifted (q : ℝ) :
    (q ^ 2 + 1) * nucleonPoly q - q ^ 2 * (q ^ 4 + q ^ 2 + 1) * responsePoly q =
      5 + 38 * (q - 1) + 167 * (q - 1) ^ 2 + 692 * (q - 1) ^ 3 + 2645 * (q - 1) ^ 4
        + 8376 * (q - 1) ^ 5 + 21204 * (q - 1) ^ 6 + 43408 * (q - 1) ^ 7
        + 73160 * (q - 1) ^ 8 + 102618 * (q - 1) ^ 9 + 120133 * (q - 1) ^ 10
        + 117028 * (q - 1) ^ 11 + 94209 * (q - 1) ^ 12 + 62050 * (q - 1) ^ 13
        + 32999 * (q - 1) ^ 14 + 13920 * (q - 1) ^ 15 + 4542 * (q - 1) ^ 16
        + 1104 * (q - 1) ^ 17 + 188 * (q - 1) ^ 18 + 20 * (q - 1) ^ 19
        + (q - 1) ^ 20 := by
  unfold nucleonPoly responsePoly; ring

/-- **`c(q) ≤ 1` for every `q ≥ 1`** — again with no interval hypothesis. -/
theorem responseCoeff_le_one {q : ℝ} (hq : 1 ≤ q) : responseCoeff q ≤ 1 := by
  have ht : (0:ℝ) ≤ q - 1 := by linarith
  have h1 := pow_nonneg ht 2
  have h2 := pow_nonneg ht 3
  have h3 := pow_nonneg ht 4
  have h4 := pow_nonneg ht 5
  have h5 := pow_nonneg ht 6
  have h6 := pow_nonneg ht 7
  have h7 := pow_nonneg ht 8
  have h8 := pow_nonneg ht 9
  have h9 := pow_nonneg ht 10
  have h10 := pow_nonneg ht 11
  have h11 := pow_nonneg ht 12
  have h12 := pow_nonneg ht 13
  have h13 := pow_nonneg ht 14
  have h14 := pow_nonneg ht 15
  have h15 := pow_nonneg ht 16
  have h16 := pow_nonneg ht 17
  have h17 := pow_nonneg ht 18
  have h18 := pow_nonneg ht 19
  have h19 := pow_nonneg ht 20
  have hgap : q ^ 2 * (q ^ 4 + q ^ 2 + 1) * responsePoly q ≤ (q ^ 2 + 1) * nucleonPoly q := by
    have := coeff_gap_shifted q
    linarith
  unfold responseCoeff
  exact (div_le_one (denom_pos hq)).mpr hgap

/-- **The factorisation — the step-9 correction in one line.** `r = h²·c`, because
`(q² − 1)² = q²·h²`. -/
theorem respPP_eq_hSq_mul_coeff {q : ℝ} (hq : 1 ≤ q) :
    respPP q = (q - q⁻¹) ^ 2 * responseCoeff q := by
  have hqpos : (0:ℝ) < q := by linarith
  have hq0 : q ≠ 0 := ne_of_gt hqpos
  have hD : (q ^ 2 + 1) * nucleonPoly q ≠ 0 := ne_of_gt (denom_pos hq)
  unfold respPP responseCoeff
  field_simp

/-- `0 < r(q)` for every `q > 1`. -/
theorem respPP_pos {q : ℝ} (hq : 1 < q) : 0 < respPP q := by
  have hq1 : (1:ℝ) ≤ q := hq.le
  have hh : 0 < q - q⁻¹ := by
    have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
    linarith
  rw [respPP_eq_hSq_mul_coeff hq1]
  exact mul_pos (pow_pos hh 2) (responseCoeff_pos hq1)

/-- **`μ − 1 = h⁴·c`**: the interface ratio deviates at FOURTH order in the deformation. -/
theorem ratio_deviation_is_fourth_order {q : ℝ} (hq : 1 ≤ q) :
    (q - q⁻¹) ^ 2 * respPP q = (q - q⁻¹) ^ 4 * responseCoeff q := by
  rw [respPP_eq_hSq_mul_coeff hq]; ring

/-! ## The binding at the derived response -/

/-- **The headline.** Step 9's bracket instantiated at the derived `r`: both ends carry `h⁴`,
so the γγ-selected diproton binding is `Θ(h⁴)`. -/
theorem binding_magnitude_fourth_order {α q : ℝ} (hα : 0 < α) (hq : 1 < q) :
    α * ((q - q⁻¹) ^ 4 * responseCoeff q) / (1 + (q - q⁻¹) ^ 4 * responseCoeff q)
        ≤ |-α * Real.log (1 + (q - q⁻¹) ^ 2 * respPP q)|
      ∧ |-α * Real.log (1 + (q - q⁻¹) ^ 2 * respPP q)|
        ≤ α * ((q - q⁻¹) ^ 4 * responseCoeff q) := by
  have hh : 0 < q - q⁻¹ := by
    have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
    linarith
  have hbr := binding_magnitude_second_order hα (respPP_pos hq) (ne_of_gt hh)
  rw [ratio_deviation_is_fourth_order hq.le] at hbr ⊢
  exact hbr

/-- **For EVERY `q > 1` the γγ-selected diproton is unbound.** Derived: `c > 0` on the whole
ray forces `μ > 1`, and step 8's log law turns that into `B < 0`. No measurement enters. -/
theorem diproton_unbound_of_response_closed_form {α q : ℝ} (hα : 0 < α) (hq : 1 < q) :
    -α * Real.log (1 + (q - q⁻¹) ^ 2 * respPP q) < 0 := by
  have hh : 0 < q - q⁻¹ := by
    have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
    linarith
  exact binding_negative_of_pos_response hα (respPP_pos hq) (ne_of_gt hh)

/-- **A fully derived keV ceiling.** On `1 < q ≤ 23/20` the magnitude is at most `α/100`:
`h⁴ ≤ 1/100` from the interval and `c ≤ 1` from the polynomial gap. Nothing measured enters —
`α` is a closed form in `q` and the CAL-1 electron mass. -/
theorem binding_ceiling_on_interval {α q : ℝ} (hα : 0 < α) (hq1 : 1 < q) (hq2 : q ≤ 23 / 20) :
    |-α * Real.log (1 + (q - q⁻¹) ^ 2 * respPP q)| ≤ α / 100 := by
  have hupper := (binding_magnitude_fourth_order hα hq1).2
  have hsq : (q - q⁻¹) ^ 2 ≤ 1 / 10 := h_sq_le_of_q_le hq1.le hq2
  have hsqnn : (0:ℝ) ≤ (q - q⁻¹) ^ 2 := sq_nonneg _
  have hfour : (q - q⁻¹) ^ 4 ≤ 1 / 100 := by
    have : (q - q⁻¹) ^ 4 = ((q - q⁻¹) ^ 2) ^ 2 := by ring
    rw [this]
    nlinarith [hsqnn, hsq]
  have hc0 : 0 < responseCoeff q := responseCoeff_pos hq1.le
  have hc1 : responseCoeff q ≤ 1 := responseCoeff_le_one hq1.le
  have hprod : (q - q⁻¹) ^ 4 * responseCoeff q ≤ 1 / 100 := by
    have h4nn : (0:ℝ) ≤ (q - q⁻¹) ^ 4 := by positivity
    calc (q - q⁻¹) ^ 4 * responseCoeff q ≤ (q - q⁻¹) ^ 4 * 1 :=
          mul_le_mul_of_nonneg_left hc1 h4nn
      _ = (q - q⁻¹) ^ 4 := by ring
      _ ≤ 1 / 100 := hfour
  calc |-α * Real.log (1 + (q - q⁻¹) ^ 2 * respPP q)|
        ≤ α * ((q - q⁻¹) ^ 4 * responseCoeff q) := hupper
    _ ≤ α * (1 / 100) := mul_le_mul_of_nonneg_left hprod hα.le
    _ = α / 100 := by ring

/-! ## The single remaining hypothesis: that these rational functions ARE the traces -/

/-- The single nucleon's `H₃` convention-D Markov trace on the canonical 11-letter element. -/
noncomputable def nucleonTrace (q : ℝ) : ℝ :=
  (q ^ 4 + 1) * nucleonPoly q / (4 * q ^ 9 * (q ^ 2 + 1) ^ 2)

/-- **The closed-form carrier.** `trFree` and `trAtom` are the `H₆` convention-D Markov traces
of the two-nucleon word without and with the bond. Both fields are verified by the probe
against two independent code paths; neither is proved in Lean. -/
structure ResponseClosedForm (q trFree trAtom : ℝ) : Prop where
  /-- The free trace factorises as the square of the single-nucleon `H₃` trace: disjoint-union
  multiplicativity of the Markov trace. -/
  free_eq : trFree = nucleonTrace q ^ 2
  /-- The bond moves the trace by exactly the derived response. -/
  ratio_eq : trAtom / trFree = 1 + (q - q⁻¹) ^ 2 * respPP q

/-- `0 < tr(W_free)` on `q > 1`, so the ratio is well posed. -/
theorem nucleonTrace_pos {q : ℝ} (hq : 1 < q) : 0 < nucleonTrace q := by
  have hq0 : (0:ℝ) < q := by linarith
  have hnum : 0 < (q ^ 4 + 1) * nucleonPoly q :=
    mul_pos (by positivity) (nucleonPoly_pos hq.le)
  have hden : (0:ℝ) < 4 * q ^ 9 * (q ^ 2 + 1) ^ 2 := by
    have h9 : (0:ℝ) < q ^ 9 := pow_pos hq0 9
    have hs : (0:ℝ) < (q ^ 2 + 1) ^ 2 := by positivity
    have : (0:ℝ) < 4 * q ^ 9 := by linarith
    exact mul_pos this hs
  unfold nucleonTrace
  exact div_pos hnum hden

/-- **What the carrier buys**: given the closed form, the binding computed from the measured
traces *is* the derived `Θ(h⁴)` quantity, so the ceiling above applies to it. -/
theorem binding_of_closedForm {α q trFree trAtom : ℝ} (hα : 0 < α) (hq1 : 1 < q)
    (hq2 : q ≤ 23 / 20) (hcf : ResponseClosedForm q trFree trAtom) :
    |-α * Real.log (trAtom / trFree)| ≤ α / 100 := by
  rw [hcf.ratio_eq]
  exact binding_ceiling_on_interval hα hq1 hq2


/-- **Classical `q = 1` evaluations of `nucleonPoly`, `responsePoly`, `responseCoeff`, `respPP`, and `nucleonTrace` (`qou-ales`).**
At `q = 1`, `nucleonPoly 1 = 4`, `responsePoly 1 = 1`, `responseCoeff 1 = 3 / 8`, `respPP 1 = 0`,
and `nucleonTrace 1 = 1 / 2`. -/
theorem classical_values_at_one :
    nucleonPoly 1 = 4 ∧
      responsePoly 1 = 1 ∧
      responseCoeff 1 = 3 / 8 ∧
      respPP 1 = 0 ∧
      nucleonTrace 1 = 1 / 2 := by
  refine ⟨by unfold nucleonPoly; norm_num,
          by unfold responsePoly; norm_num,
          by unfold responseCoeff responsePoly nucleonPoly; norm_num,
          by unfold respPP responsePoly nucleonPoly; norm_num,
          by unfold nucleonTrace nucleonPoly; norm_num⟩

end QOU.Mass.DiprotonResponseClosedForm
