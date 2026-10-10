import Mathlib.Tactic
import Mathlib.Data.Rat.Defs

/-!
# QOU.BraidKnot.MarkovParameterRecursion

**Pre-archimedean recursion for the Markov-parameter Taylor coefficients**
— the explicit q-difference / holonomic recursion underlying the Q_β
precision ladder (PR #1739).

## Provenance (pre-archimedean, exact)

The Markov parameter `z(q) = √q / (1 + q)` is the building block of
`τ_M(T_β)(q)` (the β-decay knot operator's Markov trace, per
`qbeta-decay-sdp-knot-operator.witness.json`).  Setting `w = q − 1`,
`z` is **algebraic**, satisfying the first-order ODE

    (4 + 6w + 2w²) · z'(w) + w · z(w) = 0

(verified symbolically in `qbeta_prearchimedean_z_recursion.py`).
Writing `z = Σ aₙ wⁿ` and collecting the coefficient of `wⁿ` gives the
explicit **3-term recursion**

    4(n+1)·a_{n+1} + 6n·a_n + (2n−1)·a_{n−1} = 0,    a₀ = 1/2, a₁ = 0.

This is the discrete shadow of `z`'s q-difference equation (the
"recursion ↔ PDE" identity).  It is **pre-archimedean** (formal `q`,
exact ℚ) and generates the full sequence to all orders with no `q₀`
and no CODATA fitting — answering "can we extend c_k for k ≫ 10".

## What this file proves (sorry-free)

`markovParamCoeff` is the recursion-defined sequence over ℚ; the
theorems pin its first values exactly and state the defining
recursion relation.  All proofs are kernel-checked (`norm_num`),
no `sorry`.

## What this file does NOT claim

This is the recursion for the **bare** `z`.  The full
`τ_M(T_β) = A(q) + B(q)·z(q)` carries q-dependent rational weights
`A, B` (so its `a₁ ≠ 0`), and the Q_β precision-ladder `c_k` descend
from `τ_M` via the `Q_A·cos` reparametrisation in the variable
`u = b·ℏ_q²` — that map (the open "f") is NOT formalised here.  The
full bridge to `QbetaHabiroTaylorBridgeClass`
(`habiro-precision-ladder-equivalence.lean`) remains conditional.
-/

namespace QOU.BraidKnot

/-- Taylor coefficients `aₙ` of the Markov parameter `z(q) = √q/(1+q)`
    expanded around `q = 1` (`w = q − 1`), defined by the holonomic
    recursion derived from `(4 + 6w + 2w²) z' + w z = 0`:

      `a₀ = 1/2`, `a₁ = 0`,
      `4(n+2)·a_{n+2} = −(6(n+1)·a_{n+1} + (2n+1)·a_n)`.

    Pre-archimedean: every value is an exact rational. -/
def markovParamCoeff : ℕ → ℚ
  | 0 => 1 / 2
  | 1 => 0
  | (n + 2) =>
      -(6 * ((n : ℚ) + 1) * markovParamCoeff (n + 1)
        + (2 * (n : ℚ) + 1) * markovParamCoeff n)
      / (4 * ((n : ℚ) + 2))

@[simp] theorem markovParamCoeff_zero : markovParamCoeff 0 = 1 / 2 := rfl

@[simp] theorem markovParamCoeff_one : markovParamCoeff 1 = 0 := rfl

/-- `a₂ = −1/16` — first nontrivial coefficient, matching the
    symbolic series of `√q/(1+q)`. -/
theorem markovParamCoeff_two : markovParamCoeff 2 = -1 / 16 := by
  norm_num [markovParamCoeff]

/-- `a₃ = 1/16`. -/
theorem markovParamCoeff_three : markovParamCoeff 3 = 1 / 16 := by
  norm_num [markovParamCoeff]

/-- `a₄ = −13/256`. -/
theorem markovParamCoeff_four : markovParamCoeff 4 = -13 / 256 := by
  norm_num [markovParamCoeff]

/-- **The defining recursion**, in the index-shifted form used by the
    definition: for every `n`,

      `4(n+2)·a_{n+2} + 6(n+1)·a_{n+1} + (2n+1)·a_n = 0`.

    This is the holonomic / q-difference recursion the Markov-parameter
    coefficients satisfy — the categorical object whose archimedean
    evaluation at `q₀` feeds the Q_β precision ladder. -/
theorem markovParamCoeff_recursion (n : ℕ) :
    4 * ((n : ℚ) + 2) * markovParamCoeff (n + 2)
      + 6 * ((n : ℚ) + 1) * markovParamCoeff (n + 1)
      + (2 * (n : ℚ) + 1) * markovParamCoeff n = 0 := by
  have hpos : (0 : ℚ) < 4 * ((n : ℚ) + 2) := by positivity
  simp only [markovParamCoeff]
  field_simp [hpos.ne']
  ring

end QOU.BraidKnot
