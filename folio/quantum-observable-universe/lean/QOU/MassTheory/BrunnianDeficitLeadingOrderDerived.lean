import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# QOU.MassTheory.BrunnianDeficitLeadingOrderDerived — the A=4 leg, derived

Companion to `QOU.MassTheory.MilnorParitySignLaw` (#4389), which formalised the
A-indexed Brunnian cluster law

  leading Milnor order `= 2(A−1)`,  deficit sign `= (−1)^(A−1)`

with a deliberate **epistemic split**: A=3 PROVED (closed form
`1 − τ_Borr = h⁴(3+h²)/(h²+4)`), A=4 only **MEASURED**
(`tauL4Measured = 1.000145898`, slope-estimated order `≈ 6.06`, recorded as a
`def` precisely so no theorem would restate a measured input as a premise).

This file records the **derived** replacement for that A=4 leg.

## What was computed (exactly, not measured)

`computations/deltalambda/a4_brunnian_deficit_closed_form.py`
(witness `a4-brunnian-deficit-closed-form.witness.json`) derives the closed form
of the perblock deficit `1 − τ_A` for the genuine Brunnian words — the band
commutator `w₃ = [A₀₁, A₁₂]` and the iterated `w₄ = [[A₀₁, A₁₂], A₂₃]` (the same
words the measuring probe used; the band factors are asserted against that
probe's recorded witness) — by exact symbolic algebra over `ℚ(s)`, `s = √q`:

* `χ_λ` from the **symbolic** Hoefsmit seminormal form (exact in `q`);
* `y_λ` the symbolic Jones–Markov weights;
* `|χ_λ|` resolved by exact-rational sign verification on a `q`-grid spanning
  `(1, q₀]` — every `χ_λ` is strictly positive there, as the pure-braid argument
  predicts (`χ_λ(q=1) = dim_λ > 0`);
* leading order by **numerator valuation** at `s = 1` (exact multiplicity of the
  root, no floating-point series);
* deficit sign by **exact rational arithmetic** at a rational pin `s₀` (so
  `q = s₀²` is an exact rational agreeing with `q₀` to ~20 digits).

Results — both legs through the identical pipeline:

| A | leading `(q−1)`-order | leading `(q−1)` coeff | deficit sign at `q₀` | `τ_A(q₀)` |
|---|---|---|---|---|
| 3 | **4** `= 2(3−1)` | `+12` | `+` (exact) | `0.998366623` |
| 4 | **6** `= 2(4−1)` | `−96` | `−` (exact) | `1.000145898` |

The A=4 value `τ_L₄(q₀) = 1.000145898` **reproduces the independent f64
`pyhecke_native` measurement** to the recorded precision, and the A=3 leg
reproduces the corpus's proved Borromean behaviour — two independent checks that
the pipeline is sound.

## The epistemic upgrade (what this file may and may not claim)

* The order law `2(A−1)` is now **exact at both known A** — at A=4 it was a
  log-log slope estimate `≈ 6.06`; it is now the exact valuation `6`.
* The A=4 sign is now **derived**: the leading coefficient is `−96 < 0` at even
  order `6`, so `1 − τ₄ < 0` on a punctured neighbourhood of `q = 1`
  (`(q−1)⁶ > 0` there), *and* the sign is exactly negative at the substrate pin.
  Previously the sign entered only as the measured `tauL4Measured > 1`.
* **Not claimed:** the closed form itself is not re-derived inside Lean — it is a
  degree-34 rational function in `s` produced by the witness-backed symbolic
  computation. This file records the **derived leading data** and proves the
  arithmetic of the law from it. The general-`A` law remains a conjecture (no
  third data point); `MilnorParitySignLaw.MilnorParitySignConjecture` still
  carries it, and no instance is provided here.

-- Ref: [leitner2026] docs/audits/2026-08-01-a4-brunnian-deficit-closed-form.md
-/

namespace QOU.MassTheory.BrunnianDeficitLeadingOrderDerived

/-! ## Two INDEPENDENT sides: witnessed data vs the law's formula

The declarations below are split deliberately, so that the theorems relating them
are **falsifiable** rather than definitional.

* `witnessedOrder` / `witnessedLeadingCoeff` are **DATA** — transcribed from the
  witness `a4-brunnian-deficit-closed-form.witness.json`. They assert nothing;
  they are a Lean-side record of what the symbolic computation produced.
* `leadingOrder` / `paritySign` are **THE LAW** — the closed formulas
  `2(A−1)` and `(−1)^(A−1)` posited by `MilnorParitySignLaw`, defined without
  reference to the data.

Because the two sides are defined independently, a theorem asserting that they
agree **can fail**: had the derivation returned order `5`, or a *positive* A=4
coefficient, `law_reproduces_witnessed_order` / `law_matches_witnessed_sign`
would not compile. That is the content — and it is the actual scientific claim
(the law predicts what the computation found).

Anti-pattern deliberately avoided (AGENTS.md §8): a statement like
`leadingCoeff 4 < 0 := by decide` is **not** a theorem — `leadingCoeff 4` is
*defined* to be `−96`, so it is true by unfolding and says nothing about the
physics. Such statements are notation, not proofs, and are not written here. -/

/-- **DATA (witness transcription).** Leading `(q−1)`-order of `1 − τ_A` as
produced by the exact symbolic derivation, per
`a4-brunnian-deficit-closed-form.witness.json`. `0` marks "not computed" — the
law has exactly two data points. Asserts nothing on its own. -/
def witnessedOrder : ℕ → ℕ
  | 3 => 4
  | 4 => 6
  | _ => 0

/-- **DATA (witness transcription).** Leading `(q−1)`-coefficient of `1 − τ_A`
from the same witness (A=3 `+12`, A=4 `−96`). Asserts nothing on its own. -/
def witnessedLeadingCoeff : ℕ → ℤ
  | 3 => 12
  | 4 => -96
  | _ => 0

/-- **THE LAW.** The Milnor order law `2(A−1)`, defined independently of the
data. -/
def leadingOrder (A : ℕ) : ℕ := 2 * (A - 1)

/-- **THE LAW.** The parity sign `(−1)^(A−1)`: odd `A ↦ +1`, even `A ↦ −1`,
defined independently of the data. -/
def paritySign (A : ℕ) : ℤ := (-1) ^ (A - 1)

/-! ## The falsifiable agreement theorems -/

/-- **The law reproduces the witnessed orders.** At both computed `A`, the
independently-defined formula `2(A−1)` equals the order the symbolic derivation
actually returned. This is falsifiable: a witnessed order of `5` at `A = 4`
would break it. (At A=4 the witnessed value is the *exact* valuation `6`,
replacing the earlier log-log slope estimate `≈ 6.06`.) -/
theorem law_reproduces_witnessed_order :
    witnessedOrder 3 = leadingOrder 3 ∧ witnessedOrder 4 = leadingOrder 4 := by
  constructor <;> rfl

/-- **The law reproduces the witnessed signs.** At both computed `A`, the sign of
the witnessed leading coefficient equals the independently-defined parity sign
`(−1)^(A−1)`. Falsifiable: a *positive* witnessed A=4 coefficient would break it.
At A=3 this recovers the corpus's proved Borromean positivity; at A=4 it is the
new content — previously the sign entered only as a measured `τ_L₄ > 1`. -/
theorem law_matches_witnessed_sign :
    Int.sign (witnessedLeadingCoeff 3) = paritySign 3 ∧
    Int.sign (witnessedLeadingCoeff 4) = paritySign 4 := by
  constructor <;> rfl

/-- **The witnessed orders are even.** Needed because it is what makes the
deficit's sign near `q = 1` be carried entirely by the leading coefficient
(`(q−1)^even ≥ 0`). Stated on the *witnessed* orders, so it is a fact about the
computation's output, not about the formula. -/
theorem witnessedOrder_even_at_known_A :
    Even (witnessedOrder 3) ∧ Even (witnessedOrder 4) := by
  constructor <;> decide

/-- The law's order is even at **every** `A` — a genuine `∀`-statement about the
formula (not a data check), so it also covers the un-computed `A`. -/
theorem leadingOrder_even (A : ℕ) : Even (leadingOrder A) :=
  ⟨A - 1, by unfold leadingOrder; ring⟩

/-- **Sign is carried by the leading coefficient.** Over a linear ordered ring,
if the leading coefficient is negative and the leading power is nonnegative (which
an even order guarantees), the leading term `c · xⁿ` is nonpositive for every `x`
— the structural reason the A=4 deficit `1 − τ₄` is negative near `q = 1`
(`x = q − 1`), independently of the pin. -/
theorem leadingTerm_nonpos_of_neg_coeff {R : Type*}
    [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
    (c x : R) (n : ℕ) (hc : c < 0) (hx : 0 ≤ x ^ n) : c * x ^ n ≤ 0 := by
  nlinarith [hc, hx]

/-- The A=4 leading power `x⁶` is nonnegative (it is `(x³)²`). -/
theorem pow_six_nonneg {R : Type*}
    [CommRing R] [LinearOrder R] [IsStrictOrderedRing R] (x : R) : 0 ≤ x ^ 6 := by
  have h := sq_nonneg (x ^ 3)
  calc (0 : R) ≤ (x ^ 3) ^ 2 := h
    _ = x ^ 6 := by ring

/-- **A=4 leading term is nonpositive.** Instantiating the above at the derived
A=4 witnessed data (`c = −96 < 0`, witnessed order `6`, even): the leading term of `1 − τ₄` in `(q−1)`
is nonpositive for every `q`. With the nonvanishing leading coefficient this is
the derived statement behind `τ_L₄ > 1` near `q = 1` — replacing the measured
antecedent of `MilnorParitySignLaw.sign_law_A4_measured`. -/
theorem a4_leadingTerm_nonpos {R : Type*}
    [CommRing R] [LinearOrder R] [IsStrictOrderedRing R] (x : R) :
    ((-96 : R)) * x ^ 6 ≤ 0 :=
  leadingTerm_nonpos_of_neg_coeff _ _ _ (by norm_num) (pow_six_nonneg x)

end QOU.MassTheory.BrunnianDeficitLeadingOrderDerived
