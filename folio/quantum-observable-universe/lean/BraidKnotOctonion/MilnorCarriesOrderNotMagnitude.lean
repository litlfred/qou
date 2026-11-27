/-
# Milnor's `μ̄` supplies order and sign, not magnitude

After `QOU.Mass.SU4CasimirIsAffineInPairCount` closed the SU(4) route to the
`b₃` magnitude, the remaining corpus candidate was the **Milnor triple linking
number** — on the reasoning that a Brunnian link has all pairwise linking
numbers zero while `μ̄(123) ≠ 0`, which is exactly the three-body-by-construction
structure `b₃ > 0` needs.

That reasoning is right about the *shape* and wrong about the *type*, and the
corpus's own scaffold already says so.

## What the corpus already establishes

`QOU.KnotTheory.Vassiliev.brunnian_exact_leadingOrder` (conditional on the
`BrunnianVassilievBridge` class) states that for an `A`-component Brunnian link
the first non-vanishing Vassiliev invariant sits at degree
`leadingOrder A = 2(A−1)` and takes the value **`±1`** there — and
`QOU.MassTheory.MilnorParitySignLaw` carries the companion sign law. So `μ̄` is a
**normalised** invariant. It is not a quantity with a size.

## Consequence 1 — `μ̄` cannot carry the magnitude

`muBar_no_magnitude`: if `b = c · m` with `m = ±1`, then `|b| = |c|`. Every bit
of the magnitude sits in `c`; `μ̄` contributes a sign and nothing else. So
"use `μ̄(123)` to supply the 21.4 % rise" is a category error in the same family
as the SU(4) Casimir one — an object with the right structure and the wrong type.

## Consequence 2 — the order law alone is refuted

What `μ̄` *does* supply is the **degree** at which the `A`-body term first
appears, `2(A−1)`. The minimal quantitative reading is that the `A`-body
cumulant enters as a coupling raised to that degree,

    b_A = s_A · g^{2(A−1)},        |s_A| = 1

Then `|b₂| = g²`, `|b₃| = g⁴`, `|b₄| = g⁶`, and eliminating `g` gives a
**division-free** test:

    b₃² = b₂ · b₄        (`geometric_order_forces_square`)

Measured, it fails by an order of magnitude — `b₃² = 2.034` against
`b₂·b₄ = 20.56` on the isospin-averaged convention, and `3.269` against `17.16`
on the Coulomb-corrected one (factors of 10.1 and 5.25). `not_geometric_order`
is the falsifiable form.

**Scope (a).** This refutes the *single-coupling order law*, not Milnor's
involvement. A multi-term closure in which `μ̄` fixes each term's sign and order
while separate coefficients carry the sizes is untouched — and is, on this
evidence, the only shape left for it.

Base ring is a linearly ordered commutative ring; the content is `|·|` and one
polynomial identity.

Bean `qou-edt7`; adjacent to `qou-brng` (the linking-vs-self-energy amplitude
question, which is a different bean and is not addressed here).
-/
import Mathlib.Algebra.Order.Ring.Abs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
set_option linter.unusedSectionVars false

namespace QOU.Mass.MilnorCarriesOrderNotMagnitude

variable {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **A `±1`-valued invariant carries no magnitude.** If the `A`-body term is
`c` times a Milnor invariant normalised to `±1`, the whole size is `c`'s. -/
theorem muBar_no_magnitude {b c m : R} (hm : m = 1 ∨ m = -1) (hb : b = c * m) :
    |b| = |c| := by
  rcases hm with h | h <;> subst h <;> simp [hb]

/-- **The order law forces a square relation.** If `b₂ = s₂g²`, `b₃ = s₃g⁴`,
`b₄ = s₄g⁶` with every `sᵢ = ±1` and the signs aligned so the products agree,
then `b₃² = b₂·b₄` — the coupling `g` is eliminated entirely, so the test needs
no knowledge of it. -/
theorem geometric_order_forces_square {g : R} {b₂ b₃ b₄ : R}
    (h₂ : b₂ = g ^ 2) (h₃ : b₃ = g ^ 4) (h₄ : b₄ = g ^ 6) :
    b₃ ^ 2 = b₂ * b₄ := by
  subst h₂; subst h₃; subst h₄; ring

/-- The same with an overall sign on each term, since `μ̄ = ±1`: squaring kills
`s₃`, and the right-hand side needs `s₂s₄ = 1`. Stated for the aligned case,
which is the one the measurement refutes. -/
theorem geometric_order_forces_square_signed {g s : R} {b₂ b₃ b₄ : R}
    (hs : s = 1 ∨ s = -1)
    (h₂ : b₂ = s * g ^ 2) (h₃ : b₃ = g ^ 4) (h₄ : b₄ = s * g ^ 6) :
    b₃ ^ 2 = b₂ * b₄ := by
  rcases hs with h | h <;> subst h <;> subst h₂ <;> subst h₃ <;> subst h₄ <;> ring

/-- **The falsifiable form.** A measured `b₃² ≠ b₂·b₄` refutes the single-coupling
order law, whatever the coupling is — `g` never appears in the hypothesis.

AME2020 gives `b₃² = 2.034` against `b₂·b₄ = 20.56` (isospin-averaged), so the
physical cumulants are not of this shape. -/
theorem not_geometric_order {b₂ b₃ b₄ : R} (h : b₃ ^ 2 ≠ b₂ * b₄) :
    ¬ ∃ g : R, b₂ = g ^ 2 ∧ b₃ = g ^ 4 ∧ b₄ = g ^ 6 := by
  rintro ⟨g, h₂, h₃, h₄⟩
  exact h (geometric_order_forces_square h₂ h₃ h₄)

/-- The measurement's shape, stated without the numerals: `b₂`, `b₃`, `b₄` all
positive with `b₃² < b₂·b₄` is enough to fire `not_geometric_order`. -/
theorem not_geometric_order_of_lt {b₂ b₃ b₄ : R} (h : b₃ ^ 2 < b₂ * b₄) :
    ¬ ∃ g : R, b₂ = g ^ 2 ∧ b₃ = g ^ 4 ∧ b₄ = g ^ 6 :=
  not_geometric_order (ne_of_lt h)

/-- **Step-difference proportionality under the single-coupling order law (`qou-ix0x`).**
If `b₂ = g ^ 2`, `b₃ = g ^ 4`, `b₄ = g ^ 6`, then `(b₄ - b₃) * b₂ = (b₃ - b₂) * b₃` and the
Hankel defect `b₂ * b₄ - b₃ ^ 2` vanishes identically. -/
theorem geometric_order_step_diff_and_hankel_zero {g : R} {b₂ b₃ b₄ : R}
    (h₂ : b₂ = g ^ 2) (h₃ : b₃ = g ^ 4) (h₄ : b₄ = g ^ 6) :
    (b₄ - b₃) * b₂ = (b₃ - b₂) * b₃ ∧ b₂ * b₄ - b₃ ^ 2 = 0 := by
  subst h₂; subst h₃; subst h₄
  constructor <;> ring

end QOU.Mass.MilnorCarriesOrderNotMagnitude
