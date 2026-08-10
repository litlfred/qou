/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Algebra.BigOperators.Ring.Finset

/-!
# Markov normalisation of the Jones–Markov weights (convention D, n = 3)

The Jones–Markov weights `y_λ` on `H_n(q)` are characterised by the
normalisation

  `∑_{λ ⊢ n} y_λ · dim V_λ = 1`

This file proves that identity at `n = 3` for the **convention-D** weights,
as an identity of rational functions in `q` — not a numerical check at any
particular `q₀`.

## Why this file exists

The convention-D weights were validated three ways before this: agreement
with the Rust `trace_weights_n` engine (1.2e-15), the vanishing of every
weight on a partition with three or more rows, and agreement between two
independently generated numeric tables (~1e-50). Each of those compares the
weights against *another implementation or a shared convention*. None tests
the defining property.

Eight hypotheses were raised and refuted chasing a residual in the
Schur–Weyl identity before anyone checked whether `∑ y_λ · dim = 1` held at
all. It does — symbolically, for `n = 2, …, 6`. This is the `n = 3` case
made machine-checkable.

## Convention D

`z = q³/(q²+1)`, which forces `r = 2` in the Wenzl bridge
`q·z = Q^r(1-Q)/(1-Q^r)` with `Q = q²`. Since `r` is the number of variables
in the Schur principal specialisation, `r = 2` is a two-dimensional fibre,
and a Schur polynomial in two variables vanishes on any partition with a
third row. Hence `y_{(1,1,1)} = 0` below is forced, not imposed.

## Base ring

Stated over a generic `[Field R]` per the §7c base-ring convention: this is
q-deformation combinatorics with no archimedean content, so specialising to
`ℝ` would be gratuitous. The only hypothesis is `q^2 + 1 ≠ 0`, which is what
makes the weights well-defined.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [wenzl1988] https://doi.org/10.1007/BF01393695
-/

namespace QOU.MathlibExt.MarkovNormalisation

variable {R : Type*} [Field R]

/-- The convention-D Jones–Markov weight on the trivial partition `(3) ⊢ 3`. -/
noncomputable def yTriv (q : R) : R := (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2

/-- The convention-D Jones–Markov weight on the standard partition
`(2,1) ⊢ 3`. -/
noncomputable def yStd (q : R) : R := q ^ 2 / (q ^ 2 + 1) ^ 2

/-- The convention-D Jones–Markov weight on the sign partition `(1,1,1) ⊢ 3`.

Zero because `r = 2`: a Schur polynomial in two variables vanishes on a
partition with three rows. This is the structural content of convention D,
and the property that distinguishes it from convention C, where the
corresponding weight is nonzero. -/
noncomputable def ySign (_q : R) : R := 0

/-- **Markov normalisation at `n = 3`, convention D.**

`∑_{λ ⊢ 3} y_λ · dim V_λ = 1`, with `dim V_{(3)} = 1`, `dim V_{(2,1)} = 2`,
`dim V_{(1,1,1)} = 1`.

An identity of rational functions in `q`, hypothesised only on
`q^2 + 1 ≠ 0` — no substrate value is involved. -/
theorem markov_normalisation_three (q : R) (hq : q ^ 2 + 1 ≠ 0) :
    yTriv q * 1 + yStd q * 2 + ySign q * 1 = 1 := by
  unfold yTriv yStd ySign
  field_simp
  ring

/-! ### Why the sign weight vanishes

`ySign := 0` above is a *definition*, so any lemma concluding `ySign q = 0`
by `rfl` would prove nothing about convention D — it would restate the
definition. The content is that convention D **forces** that zero, and that
is what the next lemma derives.

In the Wenzl bridge the weight of `λ` carries the factor `∏_{x ∈ λ} (1 - X ·
Q^{c(x)})` with `Q = q²` and `X = Q^r`. Convention D pins `r = 2`, so
`X = Q²`. A partition with a third row has a cell at `(i,j) = (2,0)`, whose
content is `c = j - i = -2`, contributing the factor `1 - Q² · Q^{-2} = 0`
and annihilating the whole product. -/
theorem wenzl_factor_vanishes_on_third_row (Q : R) (hQ : Q ≠ 0) :
    1 - Q ^ 2 * Q ^ (-2 : ℤ) = 0 := by
  rw [zpow_neg, zpow_ofNat, mul_inv_cancel₀ (pow_ne_zero 2 hQ), sub_self]

/-- **The vanishing, for any partition shape.**

The Wenzl-bridge weight of `λ` carries `∏_{x ∈ λ} (1 - X · Q^{c(x)})` over the
cells of `λ`. Under convention D, `X = Q²`. This says: if *any* cell has
content `-2`, the whole product is zero — so the conclusion does not depend on
the shape of `λ` beyond it having such a cell.

Every partition with three or more rows has one, at `(i,j) = (2,0)` where
`c = j - i = -2`. Cells are left abstract (`s : Finset ι` with contents
`c : ι → ℤ`) precisely so the lemma is about the *content*, not about a
particular encoding of Young diagrams. -/
theorem wenzl_prod_vanishes_of_content_neg_two {ι : Type*} (s : Finset ι)
    (c : ι → ℤ) (Q : R) (hQ : Q ≠ 0) (x₀ : ι) (hx₀ : x₀ ∈ s)
    (hc : c x₀ = -2) :
    ∏ x ∈ s, (1 - Q ^ 2 * Q ^ (c x)) = 0 := by
  refine Finset.prod_eq_zero hx₀ ?_
  rw [hc]
  exact wenzl_factor_vanishes_on_third_row Q hQ

/-- Convention C does **not** vanish there. With `z = 1/(q^{1/2} + q^{-1/2})`
the bridge solves to a non-integer `r`, so `X ≠ Q²` and the `(2,0)` factor
`1 - X·Q^{-2}` is nonzero — which is why every convention-C weight on a
three-row partition is live. Stated as the contrapositive so it is
falsifiable rather than definitional. -/
theorem wenzl_factor_nonzero_of_ne (Q X : R) (hQ : Q ≠ 0) (hX : X ≠ Q ^ 2) :
    1 - X * Q ^ (-2 : ℤ) ≠ 0 := by
  rw [zpow_neg, zpow_ofNat]
  intro h
  apply hX
  field_simp at h
  rw [mul_zero, sub_eq_zero] at h
  exact h.symm

end QOU.MathlibExt.MarkovNormalisation
