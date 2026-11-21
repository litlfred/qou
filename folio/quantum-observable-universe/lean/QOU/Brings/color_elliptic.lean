import Mathlib.Algebra.GroupWithZero.Basic
import Mathlib.Algebra.Group.Basic
import Mathlib.Tactic.Ring

/-!
# QOU.Brings.color_elliptic

Canonical Lean declaration for content block referenced by
`qou:QOU.Brings.color_elliptic`.

After eliminating $x_0, x_1$ in favour of the projective ratio
$z = x_0/x_1$ subject to $x_0 + x_1 = C$, the power-sum conditions on the
color variable $X = (x_2, x_3, x_4)$ reduce at each fixed $z$ to the
*color-elliptic cubic*

$$
  X^3 + (z+1)X^2 + (z^2+z+1)X + (z^3+z^2+z+1) = 0 .
$$

## Lean structure

* `color_elliptic z X` **names** the cubic constraint as a `Prop`
  (the admissible-color-root condition at `z`); it is not asserted
  for all `X` — no Mathlib structure makes it tautologous.
* `colorCubic_key_identity` (**proved**): the elimination identity
  `(X − z) · cubic = P(X) − P(z)` with `P(t) = t⁴ + t³ + t² + t` —
  the cubic is exactly the difference quotient of the power-sum
  quartic, which is the algebraic content of the reduction step.
* `color_elliptic_of_powerSum` (**proved**): over an integral domain,
  a color root `X ≠ z` satisfying the *same* power-sum condition
  `P(X) = P(z)` as the spacetime ratio satisfies the color-elliptic
  cubic.  This **derives** the .md's elimination claim from the
  power-sum hypothesis instead of assuming the cubic.

The genuinely open remainder — that for generic `z` the cubic defines
an elliptic curve `ℰ_z` whose `j`-invariant varies as a rational
function of `z`, with monodromy recovering the trefoil holonomy —
requires elliptic-curve machinery not wired to this cubic model and
stays narrative (see the .md).

Stated over a generic `CommRing R` (domain only where cancellation is
used) per AGENTS.md §7c: the reduction is purely algebraic — no
archimedean construct is required.
-/

namespace QOU.Brings

/-- **Color-elliptic cubic** (named constraint).

For a projective spacetime ratio `z` and a color root `X` over a
commutative ring `R`, `color_elliptic z X` is the proposition that
`X` satisfies the color-elliptic cubic

`X³ + (z+1)·X² + (z²+z+1)·X + (z³+z²+z+1) = 0`.

This names the admissible-color-root condition at `z`; it is *not*
asserted globally.  An inhabitant is produced from the power-sum
condition by `color_elliptic_of_powerSum` below. -/
-- Ref: [leitner2026] quantum-observable-universe/brings-surface/color-elliptic.md
def color_elliptic {R : Type*} [CommRing R] (z X : R) : Prop :=
    X ^ 3 + (z + 1) * X ^ 2 + (z ^ 2 + z + 1) * X +
      (z ^ 3 + z ^ 2 + z + 1) = 0

/-- The power-sum quartic `P(t) = t⁴ + t³ + t² + t` whose difference
    quotient is the color-elliptic cubic. -/
-- Ref: [leitner2026] quantum-observable-universe/brings-surface/color-elliptic.md
def powerSumQuartic {R : Type*} [CommRing R] (t : R) : R :=
  t ^ 4 + t ^ 3 + t ^ 2 + t

/-- **Elimination identity (proved).**  The color-elliptic cubic is
    the difference quotient of the power-sum quartic:

    `(X − z) · (X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1)) = P(X) − P(z)`.

    This is the algebraic core of the reduction of the power-sum
    conditions to the cubic at fixed `z`. -/
-- Ref: [leitner2026] quantum-observable-universe/brings-surface/color-elliptic.md
theorem colorCubic_key_identity {R : Type*} [CommRing R] (z X : R) :
    (X - z) * (X ^ 3 + (z + 1) * X ^ 2 + (z ^ 2 + z + 1) * X +
      (z ^ 3 + z ^ 2 + z + 1)) = powerSumQuartic X - powerSumQuartic z := by
  unfold powerSumQuartic
  ring

/-- **Proposition** ([`prop:color-elliptic`], elimination step,
    proved): over an integral domain, a color root `X` distinct from
    the spacetime ratio `z` and subject to the same power-sum
    condition `P(X) = P(z)` satisfies the color-elliptic cubic.

    Derived (not assumed): the elimination identity turns the
    power-sum hypothesis into `(X − z) · cubic = 0`, and `X ≠ z`
    cancels the linear factor. -/
-- Ref: [leitner2026] quantum-observable-universe/brings-surface/color-elliptic.md
theorem color_elliptic_of_powerSum {R : Type*} [CommRing R] [IsDomain R]
    {z X : R} (hne : X ≠ z)
    (hps : powerSumQuartic X = powerSumQuartic z) :
    color_elliptic z X := by
  have h := colorCubic_key_identity z X
  rw [hps, sub_self] at h
  rcases mul_eq_zero.mp h with h1 | h2
  · exact absurd (sub_eq_zero.mp h1) hne
  · exact h2

end QOU.Brings
