import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic

/-!
# QOU.Eightfold.MirrorSwapCompatibility — the Borromean tension is not a contradiction

`AmphichiralHolonomyIsSelfDual` left one question open, and it decided whether
route E closes on every knot of the particle dictionary or survives on one:

* the classical literature calls the Borromean rings **amphichiral**;
* `observations/time-reversal-energy-barrier.md:17` asserts the opposite for the
  corpus's `𝓑₃` — *"the Milnor triple linking number `μ̄(123) = ±1` distinguishes
  the Borromean link `𝓑₃` from its mirror `𝓑₃^σ`. No Reidemeister sequence
  connects them."*

**Both are true, of different objects, and this file is why.**

## The mechanism

`μ̄(123)` is negated by **two** independent operations:

* **mirroring** — `μ̄(σL) = −μ̄(L)`;
* **transposing two components** — `μ̄` of length three is cyclically symmetric
  and antisymmetric under a transposition, `μ̄(123) = −μ̄(213)`.

So the composite `mirror ∘ swap` **preserves** it (`negBoth_comp_fixes`), and an
invariant that both operations negate is **blind** to the difference between `L`
and `mirror (swap L)` (`cannot_distinguish_mirror_swap`). That is exactly how the
Borromean rings are amphichiral: the mirror image is isotopic to the original
*after exchanging two components*.

## What this settles

The corpus's claim is correct **for the ordered, oriented link** — with the
labels fixed, `μ̄` does distinguish `𝓑₃` from `𝓑₃^σ`. It does **not** contradict
amphichirality of the **unordered** link, nor of the **complement**.

Route E's object is the complement's holonomy, a representation of
`π₁(S³∖𝓑₃)`, which does not see component labels. The complement therefore
admits an orientation-reversing self-homeomorphism, and by **Mostow rigidity**
(already used in the corpus — `swampland-island-of-consistency.md:11`,
`approach-to-exceptional-divisor.md:11`) the discrete faithful representation is
unique up to conjugation and complex conjugation. Hence
`ρ̄_geom ≅ ρ_geom ∘ φ ≅ ρ_geom` — **self-dual**, and
`AmphichiralHolonomyIsSelfDual` prunes it.

**So route E is closed on all three knots of the dictionary — for geometric
holonomies.** `4₁` by amphichirality, `3₁` for having no hyperbolic holonomy at
all, `𝓑₃` by this argument. Together with `SymSquareHolonomyIsRealType`, which
prunes every `Sym²`-induced representation regardless of knot, what survives is
**only a genuinely non-geometric `PGL(3,ℂ)` representation** — a Fock–Goncharov
deformation away from the `PGL(2)` locus.

That is a route, not a construction. Nobody has built one.

## Scope

**Scope-(a).** This file proves the *compatibility*: that an invariant negated by
two operations cannot separate a thing from its double image. It does **not**
prove the Borromean rings are amphichiral — that is the classical fact, cited —
and it does not prove Mostow rigidity, which the corpus already cites.

What it removes is the appearance of a contradiction between the corpus and the
literature. There was none: the two statements quantify over different objects,
and reading the corpus's ordered-link claim as a claim about the complement is
the ambient-vs-instance conflation this arc keeps correcting.

## Base ring (§7c)

A commutative ring with negation, an involution, and nothing else.  No ordering, no
archimedean content.

-- Ref: [milnor1957] (μ̄ invariants; cyclic symmetry and antisymmetry in the
-- length-three case).
-- Ref: [leitner2026] `observations/time-reversal-energy-barrier.md` §1;
-- `docs/audits/2026-09-05-route-e-the-induced-pgl3-rep-is-real-type.md` §3.
-/

namespace QOU.Eightfold.MirrorSwapCompatibility

variable {L R : Type*} [CommRing R]

/-- An operation negates the invariant `mu`. -/
def Negates (op : L → L) (mu : L → R) : Prop := ∀ x, mu (op x) = - mu x

/-- **Two negations compose to a fixed point.**  If both `mirror` and `swap`
negate `mu`, their composite preserves it. -/
theorem negBoth_comp_fixes {mirror swap : L → L} {mu : L → R}
    (hm : Negates mirror mu) (hs : Negates swap mu) (x : L) :
    mu (mirror (swap x)) = mu x := by
  rw [hm (swap x), hs x, neg_neg]

/-- **The invariant is blind to the double image.**  `mu` takes the same value
on `x` and on `mirror (swap x)`, so it cannot be used to separate them — which
is precisely the configuration in which a link is amphichiral while an ordered
invariant still distinguishes it from its bare mirror. -/
theorem cannot_distinguish_mirror_swap {mirror swap : L → L} {mu : L → R}
    (hm : Negates mirror mu) (hs : Negates swap mu) (x : L) :
    mu (mirror (swap x)) = mu x ∧ ¬ (mu (mirror (swap x)) ≠ mu x) := by
  refine ⟨negBoth_comp_fixes hm hs x, ?_⟩
  simp [negBoth_comp_fixes hm hs x]

/-- **And it DOES separate `x` from its bare mirror, whenever it is nonzero.**
The corpus's claim, in the same breath as its compatibility: the two facts sit
together without tension, on different arguments. -/
theorem distinguishes_bare_mirror [NoZeroDivisors R] [CharZero R]
    {mirror : L → L} {mu : L → R}
    (hm : Negates mirror mu) {x : L} (hx : mu x ≠ 0) :
    mu (mirror x) ≠ mu x := by
  rw [hm x]
  intro h
  apply hx
  have : (2 : R) * mu x = 0 := by linear_combination -h
  rcases mul_eq_zero.mp this with h2 | h2
  · exact absurd h2 (two_ne_zero)
  · exact h2

end QOU.Eightfold.MirrorSwapCompatibility
