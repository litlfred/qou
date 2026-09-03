/-
# The bond decay rates are the transfer matrix's spectral ratio

Bean `qou-cds1`, Step 28. Computed in
`computations/qbeta/qbeta_bond_decay_rates_from_transfer_spectrum_probe.py` (5/5).

Step 27 stopped because an all-pairs nucleon coupling needs a falloff rate per
bond type, and three fitted rates would be three free parameters. They are not
free. `chi_monotone_transfer._alpha_beta` reduces each fine-Bratteli transfer
step by Cayley–Hamilton,

    O_g = ∏_j (σ_g + d_j·1) = α·σ_g + β·I ,
    E₁ = ∏_j (q + d_j) ,   E₂ = ∏_j (−1/q + d_j) ,

so `E₁, E₂` **are** the step's spectrum and the falloff carried across one bond
is the spectral ratio `E₂/E₁`. For the corpus's own single-letter bond templates
that is a closed form in `q`, proved below:

| bond | template | offset `d` | `E₂/E₁` |
|---|---|---|---|
| p–p | `σ` | `0` | `−1/q²` |
| n–n | `σ⁻¹` | `−h` | `−q²` |
| p–n | average | `−h/2` | `−1` exactly |

## They are not independent

`rates_dependent`: `r_pp · r_nn = r_pn²`, and `rate_ratio`: `r_nn / r_pp = q⁴`.
One exact relation among three rates, so **one** degree of freedom — `q²` — not
three. An all-pairs coupling built on these adds no parameter to the framework.

## They are sector-indexed, by bar parity

`interaction-sector-taxonomy.md` classifies the three interaction sectors by the
bar involution `q ↦ 1/q`: strong is bar-even (cosh channel), weak bar-odd (sinh),
and electromagnetic is provably the cell admitting no pure parity. The rates
reproduce it. `bar_exchange`: p–p and n–n swap under the bar, while `bar_fixed`
says p–n does not move. Hence their **product** is bar-even (strong) and their
**ratio** bar-odd (weak).

The p–n bond sits at the intertwiner point, and `pn_departure_in_q` says what
moves it off `−1`: the colour weight `d = −h(½ − δ/4)` gives

    1 − |r_pn| = 2δ(q²−1) / (δ(q²−1) + 2q² + 2)  =  tanh(ln q)·δ + O(δ²),

because `tanh_log_eq`: `tanh(ln q) = (q²−1)/(q²+1)`.

> **🛑 The electromagnetic reading of that coefficient is WITHDRAWN
> (2026-09-01, bean `qou-i9gk`).** This file previously said `tanh(ln q₀) =
> 0.103963710` is "exactly the odd-to-even ratio the taxonomy derives for the
> electromagnetic coupling", implying a link. It is a **triviality**, three ways:
> a census finds 5 of 12 unrelated corpus `q`-quantities have that ratio and
> **`q` alone is one of them** (every quantum integer is bar-even, so
> `[9]_q[10]_q` divides out of the taxonomy's coupling and contributes nothing to
> the number); `X = q·B` with `B` bar-even gives the ratio identically for *any*
> `B`; and `tanh(ln q)` **is** `h/(q+1/q)`, the ratio of the most basic bar-odd
> and bar-even quantities — which is exactly how it arises here (numerator `h`
> from the offset, denominator `q+1/q` from the averaged eigenvalue). The two
> "matching" expressions are one expression written twice. The discriminator
> settles it: the taxonomy's *dressed* ratio is `0.10356`, differing from the
> bare by `54×` the measured residual, and the match lands on the **bare**
> value — the algebraic form, not the physical coupling.
>
> `tanh_log_eq` and `pn_departure_*` below are unaffected; only the gloss changes.
> Measured in `computations/qbeta/qbeta_tanh_em_match_is_formal_probe.py` (4/4).

## What is not here

That `δ = flavor_split_leading(q)` vanishes to order `h³` — CAL-3's order, the
pion decay width's — is a **measurement** (`2.99999` in the probe) and belongs in
the witness. So does the coupling word: a non-adjacent nucleon pair has no single
generator to sit on, `σ_g` coupling strands `g` and `g+1` only, so building the
all-pairs braid remains a construction. What is removed here is only the
three-free-parameter objection.
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.QBeta

/-! ### The transfer step's spectrum, and the rate it carries -/

/-- `E₁` of a one-letter transfer step with offset `d`: the `σ`-eigenvalue `q`
shifted by `d`. -/
def transferE1 (q d : ℝ) : ℝ := q + d

/-- `E₂` of the same step: the `σ`-eigenvalue `−1/q` shifted by `d`. -/
noncomputable def transferE2 (q d : ℝ) : ℝ := -(1 / q) + d

/-- The falloff carried across one bond — the transfer step's **spectral gap**,
`|λ₂/λ₁|` with `λ₁` the LARGER-magnitude eigenvalue.

⚠️ **Corrected 2026-09-01.** This first read `E₂/E₁` in the fixed `(q, −1/q)`
order, which is the reciprocal of the gap whenever `|E₂| > |E₁|` — as it is for
`n–n`. `σ⁻¹` has `σ`'s spectrum up to sign, so the gap is `1/q²` for **both**
like-nucleon bonds, not `1/q²` and `q²`. Independently derived on `main` by
bean `qou-brng` (`computations/probes/spectral_gap_bond_decay_probe.py`), which
had it right; the two claims this file built on the wrong ordering — an exact
relation `r_pp·r_nn = r_pn²` and a bar-exchange giving a strong/weak sector
split — are **withdrawn**, not restated. -/
noncomputable def bondRate (q d : ℝ) : ℝ :=
  min |transferE1 q d| |transferE2 q d| / max |transferE1 q d| |transferE2 q d|

/-- **p–p** (`σ`, `d = 0`): the rate is `−1/q²`. -/
theorem rate_pp {q : ℝ} (hq : 1 < q) :
    |transferE2 q 0| / |transferE1 q 0| = 1 / q ^ 2 := by
  have hq0 : (0:ℝ) < q := lt_trans zero_lt_one hq
  unfold transferE1 transferE2
  rw [add_zero, add_zero, abs_of_pos hq0, abs_neg,
      abs_of_pos (by positivity : (0:ℝ) < 1 / q)]
  field_simp

/-- **n–n** (`σ⁻¹`, `d = −h`, `h = q − 1/q`): the rate is `−q²`. -/
theorem rate_nn {q : ℝ} (hq : 1 < q) :
    |transferE1 q (-(q - 1 / q))| / |transferE2 q (-(q - 1 / q))| = 1 / q ^ 2 := by
  have hq0 : (0:ℝ) < q := lt_trans zero_lt_one hq
  unfold transferE1 transferE2
  rw [show q + -(q - 1 / q) = 1 / q by ring, show -(1 / q) + -(q - 1 / q) = -q by ring,
      abs_of_pos (by positivity : (0:ℝ) < 1 / q), abs_neg, abs_of_pos hq0]
  field_simp

/-- **p–n**, strict average (`d = −h/2`): the rate is `−1` **exactly**, for every
`q`. The averaged interface is the bar-fixed point of the three templates. -/
theorem rate_pn {q : ℝ} (hq : q ≠ 0) :
    transferE2 q (-((q - 1 / q) / 2)) / transferE1 q (-((q - 1 / q) / 2)) = -1 := by
  unfold transferE1 transferE2
  rw [show q + -((q - 1 / q) / 2) = (q + 1 / q) / 2 by ring,
      show -(1 / q) + -((q - 1 / q) / 2) = -((q + 1 / q) / 2) by ring]
  have h : (q + 1 / q) / 2 ≠ 0 := by
    have : q ^ 2 + 1 > 0 := by positivity
    intro hc
    apply this.ne'
    field_simp at hc
    nlinarith [hc]
  field_simp

/-! ### The two claims that the ordering error cost -/

/-- **WITHDRAWN 2026-09-01.** With the gap correctly magnitude-ordered, `r_pp`
and `r_nn` are *both* `1/q²`, so the exact relation `r_pp · r_nn = r_pn²` this
file previously proved is false as stated (the product is `1/q⁴`, not `1`), and
the bar-exchange that carried the strong/weak sector split is vacuous — equal
rates do not exchange. Recorded as a deletion rather than a restatement: nothing
replaces them.

What survives is below, and it is the part that did not depend on the ordering:
`r_pn = 1` exactly for the averaged interface (equal magnitudes either way), and
its colour-weighted departure carrying `tanh(ln q)`.

**And `like_nucleon_rates_coincide` was empty until 2026-09-03.** The withdrawal
above left it stated as

    theorem like_nucleon_rates_coincide {q : ℝ} (_hq : 1 < q) :
        (1 : ℝ) / q ^ 2 = 1 / q ^ 2 := rfl

— literally `X = X`, closed by `rfl`, with the hypothesis bound under a `_`
because nothing used it. It named the surviving claim and asserted none of it:
`1/q² = 1/q²` holds for every real `q` and says nothing about nucleon bonds. That
is the tautological conclusion AGENTS.md §5 bans, and it was found by
`proof-no-unused-hypothesis-rfl` in the repo's vacuity audit.

It now states what the name says: that the p–p and n–n rates — reached through
**different** expressions, `|E₂|/|E₁|` at `d = 0` versus `|E₁|/|E₂|` at
`d = −h` — are equal. That is falsifiable (the two sides are different terms; the
ordering error this file records made them `1/q²` and `q²`), and the proof
composes `rate_pp` and `rate_nn`, so it genuinely needs `1 < q`. -/
theorem like_nucleon_rates_coincide {q : ℝ} (hq : 1 < q) :
    |transferE2 q 0| / |transferE1 q 0|
      = |transferE1 q (-(q - 1 / q))| / |transferE2 q (-(q - 1 / q))| := by
  rw [rate_pp hq, rate_nn hq]

/-! ### The electromagnetic ratio -/

/-- `tanh(ln q) = (q² − 1)/(q² + 1)` for `q > 0`. This is the coefficient that
turns the colour weight `δ` into the p–n bond's departure from `−1`, and at the
substrate pin it is `0.103963710` — the odd-to-even ratio
`interaction-sector-taxonomy.md` derives for the electromagnetic coupling. -/
theorem tanh_log_eq {q : ℝ} (hq : 0 < q) :
    Real.tanh (Real.log q) = (q ^ 2 - 1) / (q ^ 2 + 1) := by
  rw [Real.tanh_eq_sinh_div_cosh, Real.sinh_eq, Real.cosh_eq, Real.exp_log hq,
      Real.exp_neg, Real.exp_log hq]
  have h2 : q ^ 2 + 1 > 0 := by positivity
  field_simp
  try ring

/-- The colour-weighted p–n bond's departure from `−1`, exactly. With
`x = (q + 1/q)/2` and `y = hδ/4`, `|r| = (x − y)/(x + y)` and the departure is
`2y/(x + y)`. -/
theorem pn_departure_exact {x y : ℝ} (h : x + y ≠ 0) :
    1 - (x - y) / (x + y) = 2 * y / (x + y) := by
  field_simp
  ring

/-- Its leading coefficient in `δ` is `(q² − 1)/(q² + 1) = tanh(ln q)`: the
departure is `tanh(ln q)·δ + O(δ²)`. Stated as the exact rational form whose
`δ → 0` limit gives that coefficient. -/
theorem pn_departure_in_q {q δ : ℝ} (hq : q ≠ 0)
    (hD : δ * (q ^ 2 - 1) + 2 * q ^ 2 + 2 ≠ 0) :
    2 * ((q - 1 / q) * δ / 4) / ((q + 1 / q) / 2 + (q - 1 / q) * δ / 4)
      = 2 * δ * (q ^ 2 - 1) / (δ * (q ^ 2 - 1) + 2 * q ^ 2 + 2) := by
  have hx : (q + 1 / q) / 2 + (q - 1 / q) * δ / 4
      = (δ * (q ^ 2 - 1) + 2 * q ^ 2 + 2) / (4 * q) := by
    field_simp; ring
  have hy : 2 * ((q - 1 / q) * δ / 4) = (2 * δ * (q ^ 2 - 1)) / (4 * q) := by
    field_simp
    try ring
  have h4 : (4 : ℝ) * q ≠ 0 := by
    intro hc
    exact hq (by linarith [hc] : q = 0)
  rw [hx, hy, div_div_div_eq]
  field_simp

end QOU.QBeta
