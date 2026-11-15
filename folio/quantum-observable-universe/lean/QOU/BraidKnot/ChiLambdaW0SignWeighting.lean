import Mathlib.Tactic

/-!
# QOU.BraidKnot.ChiLambdaW0SignWeighting

Canonical Lean for content block
[`prop:chi-lambda-w0-sign-weighting`](../../../quantum-observable-universe/mass-theory/chi-lambda-w0-sign-weighting.md).

The substantive, derivable core of the proposition is the
**long-element character-weighting identity** at `S₃`: with the
standard irreducible-character values at the longest element
`w₀ ∈ S₃`, namely `χ_{(3)}(w₀) = 1`, `χ_{(2,1)}(w₀) = 0`,
`χ_{(1,1,1)}(w₀) = −1`, the character-weighted sum collapses to

  `S_k^{(w₀)} = c_k^{(3)} − c_k^{(1,1,1)}`.

This file derives that identity directly (`ring`), and discharges the
two witnessed sign facts at `k = 5, 6` by `norm_num` on the
witness-pinned `c_k^{(λ)}` values.  The previous canonical was an
empty `structure ChiLambdaW0SignWeighting where`, which stated nothing
(`proof-statement-integrity` failure); it is replaced by the genuine
statements below.

The *general* sign-agreement claim (empirical `c_k` matches
`S_k^{(w₀)}` in sign for **all** `k`) is not provable from `S₃`
character theory alone — it depends on the Wenzl-bridge Markov-trace
values — and remains open in the manuscript; only the `k = 5, 6`
witnessed instances are discharged here.

-- Ref: [leitner2026] quantum-observable-universe/mass-theory/chi-lambda-w0-sign-weighting.md
-/

namespace QOU.BraidKnot

/-! ## `S₃` irreducible character values at the long element `w₀`

`w₀ ∈ S₃` is the order-reversing involution `(1 3)`.  Standard `Sₙ`
character theory gives the three irreducible characters at `w₀`. -/

/-- `χ_{(3)}(w₀) = 1` (trivial representation). -/
def chiV3_w0 : ℝ := 1

/-- `χ_{(2,1)}(w₀) = 0` (standard 2-d representation; trace of a
reflection in dimension 2). -/
def chiV21_w0 : ℝ := 0

/-- `χ_{(1,1,1)}(w₀) = −1` (sign representation; `w₀` is odd). -/
def chiV111_w0 : ℝ := -1

/-- The long-element character-weighted sum at level `k`:
`S_k^{(w₀)} = χ_{(3)}(w₀)·c₃ + χ_{(2,1)}(w₀)·c₂₁ + χ_{(1,1,1)}(w₀)·c₁₁₁`. -/
def S_w0 (c3 c21 c111 : ℝ) : ℝ :=
  chiV3_w0 * c3 + chiV21_w0 * c21 + chiV111_w0 * c111

/-- **Long-element weighting identity.**
Since `χ_{(2,1)}(w₀) = 0`, the weighted sum collapses to
`S_k^{(w₀)} = c_k^{(3)} − c_k^{(1,1,1)}`. -/
-- Ref: [leitner2026] prop:chi-lambda-w0-sign-weighting (S_k^{(w₀)} = c_k^{(3)} − c_k^{(1,1,1)})
theorem S_w0_collapse (c3 c21 c111 : ℝ) :
    S_w0 c3 c21 c111 = c3 - c111 := by
  unfold S_w0 chiV3_w0 chiV21_w0 chiV111_w0
  ring

/-! ## Witness-pinned per-irrep coefficients (PR #672 probe at
`q = 1 + ε`).  Values lifted bit-exactly from
`computations/per-wedderburn-block-ck.witness.json`. -/

/-- `c₅^{(3)} = 1/4`. -/
noncomputable def c5_V3 : ℝ := 1 / 4
/-- `c₅^{(1,1,1)} = 533/2`. -/
noncomputable def c5_V111 : ℝ := 533 / 2
/-- `c₆^{(3)} = 1/4`. -/
noncomputable def c6_V3 : ℝ := 1 / 4
/-- `c₆^{(1,1,1)} = 955/2`. -/
noncomputable def c6_V111 : ℝ := 955 / 2

/-- **Witnessed sign at `k = 5`.**  `S₅^{(w₀)} = 1/4 − 533/2 < 0`,
matching the empirical `c₅ ≈ −395.41 < 0`. -/
-- Ref: [leitner2026] prop:chi-lambda-w0-sign-weighting (sign agreement at k = 5)
theorem S_w0_k5_neg : S_w0 c5_V3 0 c5_V111 < 0 := by
  rw [S_w0_collapse]; unfold c5_V3 c5_V111; norm_num

/-- **Witnessed sign at `k = 6`.**  `S₆^{(w₀)} = 1/4 − 955/2 < 0`,
matching the empirical `c₆ ≈ −45485 < 0`. -/
-- Ref: [leitner2026] prop:chi-lambda-w0-sign-weighting (sign agreement at k = 6)
theorem S_w0_k6_neg : S_w0 c6_V3 0 c6_V111 < 0 := by
  rw [S_w0_collapse]; unfold c6_V3 c6_V111; norm_num

end QOU.BraidKnot
