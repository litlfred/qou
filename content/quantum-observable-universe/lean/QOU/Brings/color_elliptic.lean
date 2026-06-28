import Mathlib.Algebra.Ring.Defs

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

This cubic is a genuine algebraic **constraint** defining the admissible
color roots $X$ at a given $z$ — it is not an identity holding for all
$X$, and no Mathlib structure makes it tautologous.  We therefore
**name** the conditional conjecture as a `Prop` (pattern C of the
vacuity-fix playbook): `color_elliptic z X` is the proposition that
$X$ satisfies the cubic at $z$.  The self-assuming `claim_color_elliptic`
carrier field of the old encoding is removed; asserting the proposition
is the open conditional claim, not faked by a projection.

Stated over a generic `CommRing R` per AGENTS.md §7c (the cubic is purely
algebraic — no archimedean construct is required).
-/

namespace QOU.Brings

/-- **Color-elliptic cubic** (named conditional conjecture).

For a projective spacetime ratio `z` and a color root `X` over a
commutative ring `R`, `color_elliptic z X` is the proposition that
`X` satisfies the color-elliptic cubic

`X³ + (z+1)·X² + (z²+z+1)·X + (z³+z²+z+1) = 0`.

This names the conditional claim (pattern C): it is *not* asserted; an
inhabitant is the open color-root constraint at `z`. -/
-- Ref: [manuscript] quantum-observable-universe/archimedean-universe/color-elliptic.ts
def color_elliptic {R : Type*} [CommRing R] (z X : R) : Prop :=
    X ^ 3 + (z + 1) * X ^ 2 + (z ^ 2 + z + 1) * X +
      (z ^ 3 + z ^ 2 + z + 1) = 0

end QOU.Brings
