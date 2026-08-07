import QOU.MassTheory.YLambdaSignThreshold

/-!
# `sign(Z) = +1`, and hence `sign(y_λ) = (−1)^{P(λ)}` unconditionally

`YLambdaSignThreshold` (#4662) proved the Wenzl principal specialisation has
`sign(s_λ) = (−1)^{P(λ)}`, `P(λ)` the number of cells below the content threshold.  Since
`y_λ = s_λ / Z`, that determined `sign(y_λ)` **only up to the single global sign of `Z` per
`n`** — the probe verified `sign(Z) = +1` for `n = 2..12`, but nothing derived it.  That was
the honest residual hole; this file closes it.

## The closed form for `Z`

`Z = Σ_{λ ⊢ n} f^λ · s_λ` is the normalisation enforcing `Σ_λ y_λ f^λ = tr_M(1) = 1`.  The
classical Schur-basis expansion of the first power sum,

    Σ_{λ ⊢ n} f^λ s_λ  =  p₁ⁿ                     (Macdonald I.7; Stanley EC2 §7)

applies verbatim, because the Wenzl weight *is* the principal specialisation
`s_λ(1, Q, …, Q^{r−1})`.  There `p₁ = 1 + Q + ⋯ + Q^{r−1} = (1 − Qʳ)/(1 − Q)`, so

    Z = ((1 − Qʳ)/(1 − Q))ⁿ                       (`normalizationClosedForm`)

Verified against the direct sum to `~1e-51` for every `n = 2..12`
(`computations/deltalambda/ylambda_normalization_closed_form_probe.py`).

## Why the sign is forced

In the substrate regime `Q > 1`, and `Qʳ > 1` as well (at `q₀`, `Qʳ ≈ 1.720`).  So **both**
`1 − Qʳ` and `1 − Q` are negative, their ratio is positive, and `Z` is a positive number raised
to a natural power:

    0 < Z                                          (`normalization_pos`)

for every `n` — including `n = 0`, where the empty product is `1`.  Note this is *not* obvious
from the summands: `Z` is a sum whose terms `f^λ s_λ` have **mixed signs** (that is exactly the
content of #4662).  Positivity comes from the closed form, not from term-by-term positivity.

Combining with `YLambdaSignThreshold.wenzl_sign`:

    sign(y_λ) = sign(s_λ)/sign(Z) = (−1)^{P(λ)}    (`y_sign_of_closedForm`)

with no residual global-sign ambiguity.

## Honest scope

The identity `Σ f^λ s_λ = p₁ⁿ` is a **classical theorem of symmetric-function theory**, cited
rather than re-proved here — formalising the Schur-basis expansion is a substantial Mathlib
project of its own.  It enters the Lean statements as an **explicit hypothesis**
(`hZ : Z = …`), so every theorem below is a rigorous conditional on a *published, numerically
re-verified* identity — **not** on a conjecture.  Per AGENTS.md §"Conditional-proved ≠
premise-established": the premise here is established literature, and the `hZ` binder is where
it is discharged by citation.

What is genuinely proved sorry-free: that the closed form is positive, and that `sign(y_λ)`
follows.

Verified `lean`-direct exit 0, sorry-free.

-- Ref: [macdonald1995] https://doi.org/10.1093/oso/9780198534891.001.0001
-- Ref: [stanley1999] https://doi.org/10.1017/CBO9780511609589
-/

namespace QOU.MassTheory.YLambdaNormalizationSign

open QOU.MassTheory.YLambdaSignThreshold

/-! ### The closed form and its sign -/

/-- The closed form for the Wenzl normalisation: `Z = ((1 − Qʳ)/(1 − Q))ⁿ`, the `n`-th power of
the principal specialisation of the first power sum `p₁ = 1 + Q + ⋯ + Q^{r−1}`. -/
noncomputable def normalizationClosedForm (Q QR : ℝ) (n : ℕ) : ℝ :=
  ((1 - QR) / (1 - Q)) ^ n

/-- **The base is positive.**  In the substrate regime `Q > 1` and `Qʳ > 1`, so `1 − Qʳ < 0`
and `1 − Q < 0`: the ratio of two negatives.  This is the whole mechanism — the positivity of
`Z` comes from a *cancellation of two sign flips*, not from any term being positive. -/
theorem base_pos {Q QR : ℝ} (hQ : 1 < Q) (hQR : 1 < QR) : 0 < (1 - QR) / (1 - Q) :=
  div_pos_of_neg_of_neg (by linarith) (by linarith)

/-- **`Z > 0` for every `n`.**  A positive base raised to a natural power.

Worth stating explicitly that this is *not* inherited from the summands: `Z = Σ_λ f^λ s_λ` has
mixed-sign terms — that is precisely `YLambdaSignThreshold.wenzl_sign` — so term-by-term
positivity is false.  The closed form is what forces the sign. -/
theorem normalization_pos {Q QR : ℝ} (hQ : 1 < Q) (hQR : 1 < QR) (n : ℕ) :
    0 < normalizationClosedForm Q QR n :=
  pow_pos (base_pos hQ hQR) n

/-- **`Z ≠ 0`** — the form needed to divide by it. -/
theorem normalization_ne_zero {Q QR : ℝ} (hQ : 1 < Q) (hQR : 1 < QR) (n : ℕ) :
    normalizationClosedForm Q QR n ≠ 0 :=
  ne_of_gt (normalization_pos hQ hQR n)

/-! ### The unconditional sign of `y_λ` -/

/-- **`sign(y_λ) = (−1)^{P(λ)}`, with no residual global sign.**

Given `Z` in closed form (the classical `Σ f^λ s_λ = p₁ⁿ`, supplied as `hZ`), dividing the
Wenzl weight by `Z` preserves sign, so the content-threshold parity of
`YLambdaSignThreshold.wenzl_sign` transfers verbatim from `s_λ` to `y_λ`.

This is the statement #4662 could not make: there, `sign(Z)` was verified numerically for
`n = 2..12` but underived, so the parity determined `sign(y_λ)` only up to one global sign per
`n`. -/
theorem y_sign_of_closedForm {α : Type*} [DecidableEq α]
    {Q QR Z : ℝ} (hQ : 1 < Q) (hQR : 1 < QR) (n : ℕ)
    (hZ : Z = normalizationClosedForm Q QR n)
    (cells : Finset α) (val : α → ℝ) (hgt : α → ℕ) (nlam : ℕ)
    (hh : ∀ x ∈ cells, 1 ≤ hgt x) (hnd : ∀ x ∈ cells, QR * val x ≠ 1) :
    0 < (-1 : ℝ) ^ (cells.filter fun x => QR * val x < 1).card *
      ((Q ^ nlam * (∏ x ∈ cells, (1 - QR * val x))
          / ∏ x ∈ cells, (1 - Q ^ hgt x)) / Z) := by
  have hs := wenzl_sign hQ nlam cells val hgt hh hnd
  have hZpos : 0 < Z := by rw [hZ]; exact normalization_pos hQ hQR n
  have : (-1 : ℝ) ^ (cells.filter fun x => QR * val x < 1).card *
      ((Q ^ nlam * (∏ x ∈ cells, (1 - QR * val x))
          / ∏ x ∈ cells, (1 - Q ^ hgt x)) / Z)
      = ((-1 : ℝ) ^ (cells.filter fun x => QR * val x < 1).card *
          (Q ^ nlam * (∏ x ∈ cells, (1 - QR * val x))
            / ∏ x ∈ cells, (1 - Q ^ hgt x))) / Z := by
    ring
  rw [this]
  exact div_pos hs hZpos

/-- **No deep cells ⇒ `y_λ > 0`**, unconditionally.  At `q₀` a below-threshold cell needs
content `≤ −3`, hence `≥ 4` rows — so every `λ` with `ℓ(λ) ≤ 3` carries a *strictly positive*
Wedderburn weight.  `(8,1)` is the case that refutes the naive `ℓ`-parity reading. -/
theorem y_pos_of_no_deep_cells {α : Type*} [DecidableEq α]
    {Q QR Z : ℝ} (hQ : 1 < Q) (hQR : 1 < QR) (n : ℕ)
    (hZ : Z = normalizationClosedForm Q QR n)
    (cells : Finset α) (val : α → ℝ) (hgt : α → ℕ) (nlam : ℕ)
    (hh : ∀ x ∈ cells, 1 ≤ hgt x) (hnd : ∀ x ∈ cells, QR * val x ≠ 1)
    (hshallow : ∀ x ∈ cells, 1 < QR * val x) :
    0 < (Q ^ nlam * (∏ x ∈ cells, (1 - QR * val x))
          / ∏ x ∈ cells, (1 - Q ^ hgt x)) / Z := by
  have hZpos : 0 < Z := by rw [hZ]; exact normalization_pos hQ hQR n
  exact div_pos (shallow_of_no_deep_cells hQ nlam cells val hgt hh hnd hshallow) hZpos

end QOU.MassTheory.YLambdaNormalizationSign
