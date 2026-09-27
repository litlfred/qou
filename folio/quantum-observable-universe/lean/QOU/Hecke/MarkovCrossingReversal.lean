/-
# The Markov trace of the crossing reversal, and which parameter reproduces the flavour split

## What this file is about

`conj:flavor-split-habiro-derivation`
(`content/quantum-observable-universe/mass-theory/flavor-split-habiro-derivation.md`)
carries the nucleon flavour split in two sections that do not connect, and this
file measures the gap and then closes half of it.

**Its narrative half** ("Topological parity and the Hopf antipode") computes the
crossing reversal at `k = 3`,

    σ₁³ - σ₁⁻³ = 3h + h³ = q³ - q⁻³,

and concludes: *"The bare topological difference is thus a central scalar: the
chiral σ₁ terms cancel identically."*  That is correct, and
`QOU.Hecke.CrossingReversalParity.reversal_rec` places it in the general pattern
— the reversal is central exactly at ODD `k`.

**Its formula half** ("The X(q) baseline coupling") then displays

    X_baseline(q) = (q-1)²(1 - q⁻⁴)/3,

which is `ℏ_q²·(q² - q⁻²)/3` — the reversal at `k = 2`.  The two halves are
different objects: `ℏ_q²(q³-q⁻³)/3 = 0.00208228` is **+51.17 %** against the
measured split, where the displayed baseline is **-0.128 %**.  They differ by
`(q²-q+1)(q²+q+1)/(q(q²+1)) ≈ 1.5136`, a factor the block neither states nor
derives (`k3_ne_k2_ratio`, `k3_ratio_ne_one`).

So the quantity the block actually uses sits at `k = 2`, where — by
`CrossingReversalParity.reversal_two` — the reversal is **not** central:
`σ² - σ⁻² = h·(σ + σ⁻¹)`.  It is an algebra element, not a number, and turning
it into a number needs either a channel projection or a trace.  This file does
the trace.

## The result

The Markov trace is fixed on this element by two facts and nothing else:
`tr(1) = 1` and `tr(σ) = z`.  Since the reversal is `2hσ - h²` (`reversal_two`
plus `σ + σ⁻¹ = 2σ - h`),

    tr_z(σ² - σ⁻²) = 2hz - h²                                  `markovReversal`

— and this is exactly `h·(b_pp + b_nn)`, `h` times the sum of the corpus's own
two like-pair bond letters `b_pp = z`, `b_nn = z - h`
(`markovReversal_eq_h_mul_bondSum`; the letters are
`QOU.Hecke.BondLetterIdentification.tr_bond_interp` at `t = 0, 1`).

Evaluated at the two admissible Markov parameters of `qou-99qc`:

| parameter | `tr_z(σ² - σ⁻²)` | `ℏ_q²·(that)/3` |
|---|---|---|
| augmentation `z = q` | `q² - q⁻²` exactly | **= X_baseline exactly** |
| convention D `z_D = q³/(q²+1)` | `α·(q² - q⁻²)` | `α·X_baseline` |

with `α = (q⁴+1)/(q²+1)²`, and `1/2 < α < 1` strictly for every `q > 1`
(`alpha_lt_one`, `alpha_gt_half`).  At the proton `q₀` that is `α = 0.505404`.

**`α` is not a new constant.**  It is the same `α` AGENTS.md records in the
2026-09-08 `Q_β` ruling — *"the augmentation cell is the other admissible point
and is proportional to `z_D`'s (`α = (q⁴+1)/(q²+1)²`)"*.  The same two Markov
parameters, the same ratio between them, in a second observable.

## What is derived and what is NOT

**Derived, and in this file:** everything in the table.  `markovReversal` follows
from `tr(1) = 1`, `tr(σ) = z` and a ring identity; the two evaluations are ring
identities; the `α` bounds are elementary.

**NOT derived, and stated here so it is not read as closed:** that the flavour
split *is* `ℏ_q²·tr_z(σ² - σ⁻²)/3` for any `z`.  The prefactor `ℏ_q²/3` is the
block's, is unexplained there, and is unexplained here.  What this file
establishes is that GIVEN that shape, the parameter is pinned — and pinned to
`z = q`, not to the canonical `z_D`.

**Do not read the exactness at `z = q` as evidence FOR the augmentation.**
AGENTS.md §"NO FITTING" is explicit that selecting a branch because it
reproduces the measured value is fitting even with no continuous parameter, and
that accuracy is never a tie-breaker.  The content here is the *fork* and its
exact size, not a recommendation: under the owner-ruled `z_D` this construction
predicts `α·X_baseline`, i.e. a model flavour split **half** the observed one,
and that is a falsifiable consequence of the ruling rather than an argument
against it.  Bean `qou-qqm4`; the `Q_β` half of the same fork is `qou-99qc`.

## Scope of the negatives

- `k3_ratio_ne_one` — scope (b).  The block's two halves are different numbers
  for every `q > 1`; the invariant is that `(q²-q+1)(q²+q+1) ≠ q(q²+1)` away
  from `q = 1`.  This excludes reading the `k = 3` paragraph as a derivation of
  the `k = 2` formula, and nothing else.
- `channelAverage_eq_zero` — scope (b) for the averaged reading.  The
  `2026-06-17` three-channel decomposition
  (`docs/audits/2026-06-17-hecke-channel-chirality-binding.md`) carries
  `w_sym = w_alt = q²/(q⁴+4q²+1)`, and the two channel values are exact
  negatives (`CrossingReversalParity.alternating_eq_neg_symmetric`), so their
  weighted sum vanishes identically.  The split therefore cannot be a
  sym/alt-weighted average under equal weights; it excludes nothing about the
  standard channel and nothing about unequal weights.

## A framing of my own that this file RETRACTS

PR #7320 said the conjecture's *own stated channel* gives the flavour split the
wrong sign, reading its "the weak interaction is strictly left-handed, so it
projects onto the fully alternating channel" as a claim about the split itself.
**That conflated the block's two levels.**  The alternating channel is claimed
there for the *residual* — the ≈ 1.76e-6, 0.128 % Schwinger-analogue refinement
on top of the baseline — not for the baseline.  The mathematics of #7320 is
untouched (`alternatingSplit_neg` and `splits_sum_zero` are correct and are used
below); only that interpretive sentence was wrong, and it is corrected in
`CrossingReversalParity.lean`'s header and in
`crossing_reversal_parity_probe.py` in the same commit.

## Base ring

The main section is generic `Field R` — no ordering, no `Real.sqrt`, no
archimedean construct — because every identity here is rational-function algebra.
`CharZero` appears only where a statement divides by 3.  The `α` bounds need an
ordering and live in the `Archimedean` section over `ℝ`, after the wall (§7c).

Probe: `computations/qbeta/flavour_split_baseline_is_augmentation_trace_probe.py`
-/

import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

namespace QOU.Hecke.MarkovCrossingReversal

variable {R : Type*} [Field R]

/-- `h = q - q⁻¹`, the Hecke deformation parameter. -/
noncomputable def hOf (q : R) : R := q - q⁻¹

/-- The Markov trace of the `k = 2` crossing reversal, at Markov parameter `z`.

Derivation, using nothing but `tr(1) = 1` and `tr(σ) = z`:
`σ² - σ⁻² = h·(σ + σ⁻¹)` (`CrossingReversalParity.reversal_two`) and
`σ + σ⁻¹ = 2σ - h` (`inv_eq`), so the element is `2hσ - h²` and its trace is
`2hz - h²`. -/
noncomputable def markovReversal (h z : R) : R := 2 * h * z - h ^ 2

/-- The trace is `h` times the sum of the two like-pair bond letters
`b_pp = z` and `b_nn = z - h` (`BondLetterIdentification.tr_bond_interp` at
`t = 0` and `t = 1`).  Nothing beyond the corpus's own letters enters. -/
theorem markovReversal_eq_h_mul_bondSum (h z : R) :
    markovReversal h z = h * (z + (z - h)) := by
  unfold markovReversal; ring

/-- The symmetric-channel value of the reversal, `q² - q⁻²`.  Matches
`CrossingReversalParity.symmetricValue`. -/
noncomputable def symValue (q : R) : R := q ^ 2 - (q ^ 2)⁻¹

/-- **At the augmentation `z = q` the Markov trace IS the symmetric-channel
value**, exactly.  No approximation, no prefactor. -/
theorem markovReversal_augmentation {q : R} (hq : q ≠ 0) :
    markovReversal (hOf q) q = symValue q := by
  unfold markovReversal hOf symValue
  field_simp
  ring

/-- The convention-D Markov parameter `z_D = q³/(q²+1)`. -/
noncomputable def zD (q : R) : R := q ^ 3 / (q ^ 2 + 1)

/-- The ratio between the two admissible cells, `α = (q⁴+1)/(q²+1)²`.  This is
the same `α` as the 2026-09-08 `Q_β` ruling's augmentation-to-`z_D` factor. -/
noncomputable def alphaOf (q : R) : R := (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2

/-- **At `z_D` the Markov trace is `α` times the augmentation's**, exactly. -/
theorem markovReversal_zD {q : R} (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    markovReversal (hOf q) (zD q) = alphaOf q * symValue q := by
  unfold markovReversal hOf zD alphaOf symValue
  field_simp
  ring

/-- The block's displayed baseline coupling `X_baseline(q) = (q-1)²(1-q⁻⁴)/3`. -/
noncomputable def baselineX (q : R) : R := (q - 1) ^ 2 * (1 - (q ^ 4)⁻¹) / 3

/-- `ℏ_q = 1 - q⁻¹`. -/
noncomputable def hbarOf (q : R) : R := 1 - q⁻¹

section CharZeroSection

variable [CharZero R]

/-- The displayed baseline is the `k = 2` form: `X_baseline = ℏ_q²(q²-q⁻²)/3`.
This is the identity that locates the block's formula at `k = 2`, against its
narrative's `k = 3`. -/
theorem baselineX_eq_hbarSq_symValue_div_three {q : R} (hq : q ≠ 0) :
    baselineX q = hbarOf q ^ 2 * symValue q / 3 := by
  unfold baselineX hbarOf symValue
  field_simp

/-- **The block's displayed baseline is exactly the augmentation's Markov
trace**, dressed by the block's own `ℏ_q²/3`. -/
theorem baselineX_eq_augmentation_trace {q : R} (hq : q ≠ 0) :
    baselineX q = hbarOf q ^ 2 * markovReversal (hOf q) q / 3 := by
  rw [markovReversal_augmentation hq, baselineX_eq_hbarSq_symValue_div_three hq]

/-- **Under the canonical `z_D` the same construction gives `α` times the
baseline** — a model flavour split scaled by `α`, which is `< 1`. -/
theorem zD_trace_eq_alpha_mul_baseline {q : R} (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    hbarOf q ^ 2 * markovReversal (hOf q) (zD q) / 3 = alphaOf q * baselineX q := by
  rw [markovReversal_zD hq hq2, baselineX_eq_hbarSq_symValue_div_three hq]
  ring

end CharZeroSection

/-- The `k = 3` reversal value, `q³ - q⁻³` — the block's narrative half. -/
noncomputable def k3Value (q : R) : R := q ^ 3 - (q ^ 3)⁻¹

/-- The two halves differ by `(q²-q+1)(q²+q+1)/(q(q²+1))`. -/
theorem k3_ne_k2_ratio {q : R} (hq : q ≠ 0) :
    k3Value q * (q * (q ^ 2 + 1))
      = symValue q * ((q ^ 2 - q + 1) * (q ^ 2 + q + 1)) := by
  unfold k3Value symValue
  field_simp
  ring

section Archimedean

/-- `α < 1` for every real `q ≠ 0`: `1 - α = 2q²/(q²+1)² > 0`. -/
theorem alpha_lt_one {q : ℝ} (hq : q ≠ 0) : alphaOf q < 1 := by
  have hpos : (0 : ℝ) < (q ^ 2 + 1) ^ 2 := by positivity
  have hq2 : (0 : ℝ) < q ^ 2 := by positivity
  rw [alphaOf, div_lt_one hpos]
  nlinarith [hq2]

/-- `1/2 < α` for every real `q > 1`: `α - 1/2 = (q-1)²(q+1)²/(2(q²+1)²) > 0`. -/
theorem alpha_gt_half {q : ℝ} (hq : 1 < q) : 1 / 2 < alphaOf q := by
  have hpos : (0 : ℝ) < (q ^ 2 + 1) ^ 2 := by positivity
  have hq1 : (0 : ℝ) < (q - 1) ^ 2 * (q + 1) ^ 2 := by
    have h1 : q - 1 ≠ 0 := by linarith
    have h2 : q + 1 ≠ 0 := by linarith
    positivity
  rw [alphaOf, lt_div_iff₀ hpos]
  nlinarith [hq1]

/-- **The block's two halves are different numbers for every `q > 1`** — the
`k = 3` narrative does not derive the `k = 2` formula.  Scope (b) for exactly
that reading; the invariant is `(q²-q+1)(q²+q+1) ≠ q(q²+1)` away from `q = 1`. -/
theorem k3_ratio_ne_one {q : ℝ} (hq : 1 < q) :
    (q ^ 2 - q + 1) * (q ^ 2 + q + 1) ≠ q * (q ^ 2 + 1) := by
  have h : (0 : ℝ) < (q - 1) ^ 2 * (q + 1) := by
    have h1 : q - 1 ≠ 0 := by linarith
    have h2 : (0 : ℝ) < q + 1 := by linarith
    positivity
  nlinarith [h]

/-- The three-channel average of the reversal **vanishes identically** when the
symmetric and alternating weights are equal — which they are in the corpus's own
decomposition, `w_sym = w_alt = q²/(q⁴+4q²+1)`
(`docs/audits/2026-06-17-hecke-channel-chirality-binding.md`).  Uses only that
the alternating value is the negative of the symmetric one
(`CrossingReversalParity.alternating_eq_neg_symmetric`). -/
theorem channelAverage_eq_zero (w s : ℝ) : w * s + w * (-s) = 0 := by ring

/-- The same statement in the form it is used: equal weights on values that sum
to zero contribute nothing, whatever the weight is. -/
theorem channelAverage_eq_zero' (w sVal aVal : ℝ) (hsum : sVal + aVal = 0) :
    w * sVal + w * aVal = 0 := by
  have : aVal = -sVal := by linarith
  rw [this]; ring

end Archimedean

end QOU.Hecke.MarkovCrossingReversal
