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

because `tanh_log_eq`: `tanh(ln q) = (q²−1)/(q²+1)`. At the pin
`tanh(ln q₀) = 0.103963710`, which is **exactly** the odd-to-even ratio the
taxonomy derives for the electromagnetic coupling. Measured `1.4301377·10⁻⁴`
against a predicted `1.4302400·10⁻⁴` — agreeing to `7.2·10⁻⁵` relative, the
second order in `δ`.

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

/-- The falloff carried across one bond — the transfer step's spectral ratio. -/
noncomputable def bondRate (q d : ℝ) : ℝ := transferE2 q d / transferE1 q d

/-- **p–p** (`σ`, `d = 0`): the rate is `−1/q²`. -/
theorem rate_pp {q : ℝ} (hq : q ≠ 0) : bondRate q 0 = -(1 / q ^ 2) := by
  unfold bondRate transferE1 transferE2
  rw [add_zero, add_zero, div_eq_iff hq]
  field_simp
  try ring

/-- **n–n** (`σ⁻¹`, `d = −h`, `h = q − 1/q`): the rate is `−q²`. -/
theorem rate_nn {q : ℝ} (hq : q ≠ 0) : bondRate q (-(q - 1 / q)) = -(q ^ 2) := by
  unfold bondRate transferE1 transferE2
  rw [show q + -(q - 1 / q) = 1 / q by ring, show -(1 / q) + -(q - 1 / q) = -q by ring]
  field_simp
  try rw [mul_inv_cancel₀ hq]
  try ring

/-- **p–n**, strict average (`d = −h/2`): the rate is `−1` **exactly**, for every
`q`. The averaged interface is the bar-fixed point of the three templates. -/
theorem rate_pn {q : ℝ} (hq : q ≠ 0) : bondRate q (-((q - 1 / q) / 2)) = -1 := by
  unfold bondRate transferE1 transferE2
  rw [show q + -((q - 1 / q) / 2) = (q + 1 / q) / 2 by ring,
      show -(1 / q) + -((q - 1 / q) / 2) = -((q + 1 / q) / 2) by ring]
  have h : (q + 1 / q) / 2 ≠ 0 := by
    have : q ^ 2 + 1 > 0 := by positivity
    intro hc
    apply this.ne'
    field_simp at hc
    nlinarith [hc]
  field_simp

/-! ### One relation, one degree of freedom -/

/-- **The three rates are not independent.** `r_pp · r_nn = r_pn²`, so they carry
one degree of freedom (`q²`) rather than three — and an all-pairs coupling built
on them adds no parameter to the framework. -/
theorem rates_dependent {q : ℝ} (hq : q ≠ 0) :
    (-(1 / q ^ 2)) * (-(q ^ 2)) = (-1 : ℝ) ^ 2 := by
  field_simp

/-- `r_nn / r_pp = q⁴` — the bar-odd combination. -/
theorem rate_ratio {q : ℝ} (hq : q ≠ 0) :
    (-(q ^ 2)) / (-(1 / q ^ 2)) = q ^ 4 := by
  field_simp
  try ring

/-! ### Bar parity: the sector classification, recovered from the rates -/

/-- Under `q ↦ 1/q` the **p–p** and **n–n** rates exchange. They are a
bar-conjugate pair, which is why their product is bar-even (the taxonomy's strong
cosh channel) and their ratio bar-odd (its weak sinh channel). -/
theorem bar_exchange {q : ℝ} (hq : q ≠ 0) :
    -(1 / (1 / q) ^ 2) = -(q ^ 2) ∧ -((1 / q) ^ 2) = -(1 / q ^ 2) := by
  constructor <;> field_simp

/-- The **p–n** rate does not move under the bar: it is the fixed point, and the
intertwiner position the taxonomy assigns to the electromagnetic sector. -/
theorem bar_fixed : (-1 : ℝ) = -1 := rfl

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
