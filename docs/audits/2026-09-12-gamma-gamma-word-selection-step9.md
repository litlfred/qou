# γγ word selection, step 9 — the diproton magnitude is second order in the deformation

**Bean:** `qou-ales`. Steps 6–8 settled *which* bond reading 3 selects on the `H₆` interface
and *why* its unbinding is consistent with the single-crossing obstruction. What was left
measured is the **magnitude**, step 3's `B_pp = −4.469` keV. This step derives its **order**,
which is what makes it keV rather than MeV.

**Lean:** `content/quantum-observable-universe/lean/QOU/Mass/DiprotonSecondOrder.lean`
(8 declarations; `#print axioms` clean of `sorryAx`; `lean -DautoImplicit=false -s 65536`
exit 0). **Probe:** `computations/probes/diproton_second_order_probe.py` (+ witness, 5/5;
proton pin, 60 dps; reads the ratio from the step-3 witness rather than hardcoding it).

Nothing below reads AME2020, a CODATA *binding* value, or a census.

## 1. The lever is step 4's cube identity

`vtx_three_sub_one` (step 4, sorry-free) gives, from the Hoefsmit relations alone,

    V³ − 1 = h² · ((2 + h²) · V + 1),      h = q − q⁻¹.

The selected bond does not merely *happen* to sit near the identity — it differs from it by
**exactly `h²` times a bounded matrix, with no freedom in the exponent**. Writing the bond's
image as `1 + h²·D` and using linearity of the Markov trace, the interface ratio is
`μ = 1 + h²·r` with `r = tr(W·D)/tr(W)`, and step 8's log law turns that into a bound.

## 2. The two-sided bound: `|B| = Θ(h²)`

`binding_magnitude_second_order` — for `α > 0`, `h ≠ 0`, `r > 0`:

    α·h²r / (1 + h²r)  ≤  |B|  ≤  α·h²r,      B = −α·log(1 + h²r).

Both ends carry `h²`, so the magnitude is **exactly second order**, bounded above *and*
below. That is the point: an upper bound alone would leave the magnitude possibly much
smaller, and the lower bound is what makes "second order" a statement about the size rather
than a ceiling. Supporting lemmas `log_one_add_le` and `le_log_one_add` give
`x/(1+x) ≤ log(1+x) ≤ x`.

Also proved: `binding_negative_of_pos_response` (the sign, from step 8 — a bond that moves
the trace upward unbinds), `bound_at_small_h_sq` (`h² ≤ 1/10 ⇒ |B| ≤ α·r/10`),
`bound_on_q_interval` (the same stated on `q`, so the chain from the substrate modulus to the
order is visible: `1 < q ≤ 23/20` forces the ceiling), `vertexCube_deviation_is_h_sq_smul`
(step 4's identity re-exported so the `h²` is visibly algebra, not assumption), and
`ratio_eq_one_add_of_linear_response` (the bookkeeping from a linear trace to `1 + h²r`).

## 3. Measured at the pin — the bracket is tight, and it holds

The probe reads the ratio from the step-3 witness (`pp_binding`, the `G³` row) and derives
everything else:

| quantity | value | status |
|---|---|---|
| `h²` at the proton pin | `0.0437062085` | derived from the pin |
| `α = 𝔈₀^full` | `4.227483356` MeV | derived closed form in `q` and CAL-1 `m_e` |
| ratio `tr_atom/tr_free` | `1.0010577525451598436` | **measured** (step 3) |
| `r = (ratio − 1)/h²` | `0.024201425396` | from the measurement |
| `\|B\|` via the log law | `4.469268006` keV | `2.0e−59` MeV from the step-3 `B_pp` |
| proved lower bound | `4.466906397` keV | |
| proved upper bound | `4.471631279` keV | |
| bracket width | `0.004725` keV — **0.106 %** of `\|B\|` | |
| ceiling `α·r/10` from `h² ≤ 1/10` | `10.231` keV | keV scale from the interval alone |

So the bracket contains the measurement and pins it to a tenth of a percent *given `r`*.

**The accounting that matters.** The magnitude is `α·h²·r` to within 0.1 %, and of those
three factors **two are derived** — `α` is a closed form in `q` and the CAL-1 electron mass,
`h²` follows from the pin — while **one is measured**, the relative response `r`. What step 9
removes from the measurement is the *scale*: for any `r` of order `10⁻²` or smaller the
binding is forced to keV. For contrast the probe records that a *first*-order deviation would
give `α·h·r = 21.389` keV, `4.79 ×` larger — the `h²` is what buys the keV.

## 4. Why the `Θ(h²)` is not circular — a correction to this record's own first draft

**This section was missing when step 9 was first committed (`ca33a5971b`), and its absence
was a real defect in the framing, not a presentational gap.** `r` is *defined* as
`(μ − 1)/h²`, so the bracket in §2 holds for **any** ratio whatever. Stated alone it says
nothing about a scale, and the first draft of this record — and of PR #7233's body — asserted
that step 9 "removes the scale from the measurement" without saying what that rests on.

What it rests on: `r` is bounded **independently of `h`**. Step 4's identity gives the
deviation as `h²·D` with `D = (2 + h²)·V + 1`, whose scalar factor is at most `21/10` on the
interval (`deviation_coefficient_le`), so `D`'s size is controlled by `V`'s alone; then
`r = tr(W·D)/tr(W)` is bounded whenever the free trace is bounded away from zero
(`response_bounded_of_deviation_bounded`, giving `|r| ≤ K/m` with no `h` in it). Measured at
the pin, `‖V³ − 1‖_F / h² = 2.577` — an order-one coefficient, so the `h²` is the real scale
rather than an artifact of the definition.

**And do not check the order on the character.** `bond_character_deviation` gives

    χ_(2,1)(V³) − 2 = −h⁴·(3 + h²),

because `tr D = −3h² − h⁴` is itself `O(h²)`. So the bond's **matrix** deviates at second
order while its **character** deviates at fourth. The interface ratio is controlled by the
matrix, since `tr(W·D)` carries no such cancellation — anyone verifying the order on
characters will get `h⁴` and be wrong about the binding by two powers of `h`. This is the
sharpest trap in the step and it is worth the line.

**What the correction contaminated, and what it did not.** The Lean theorem
`binding_magnitude_second_order` was and is correct — `r` is a free positive hypothesis there,
so nothing proved needed changing; the three lemmas above are additions. The defect was in
this record's §3 wording and in the PR body, both of which claimed the scale result without
its condition; both are corrected, and the bean entry for step 9 carries the correction. The
probe's numbers are unaffected.

## 5. What is NOT derived

* **`r` itself.** It is the trace-weighted response over the eleven `H₆` blocks with the
  eleven-letter nucleon words, carried as a hypothesis in the Lean; no value is asserted
  there. Deriving `r` is the remaining open item of the magnitude question.
* The numerical `4.469` keV as a *prediction*: it is `α·h²·r` with `r` measured.
* The dineutron channel, and anything about whether the two-nucleon sector matches nature.
  `SingleCrossingAlwaysBinds`'s own subject stands as recorded (step 8 §5).

## 6. Verification

Shadow compile, exit 0; `#print axioms` on all 8 declarations clean. Probe 5/5, with the
log-law reproduction of the step-3 `B_pp` at `2.0e−59` MeV as the calibration that the ratio
and the scale are the only inputs. Two mechanical slips on the first attempt, both fixed:
`field_simp` left `x = 1 + x − 1` (needed `ring`), and one `nlinarith` over a product of
three positives was replaced by an explicit `calc` through `mul_le_mul_of_nonneg_left`.
