/-
# Gell-Mann–Okubo is an identity, not a prediction

The eightfold-way chapter records the meson relation

    4 m_K²  =  3 m_η²  +  m_π²

as something the framework should *derive* from the crossing-energy splitting
pattern, and compares its ~6% experimental deviation against a ~3.3% number
obtained from the `q`-deformation of the adjoint quantum dimension.

**Both halves of that framing are wrong, and this file proves the first half.**

## What GMO actually tests

First-order `SU(3)` breaking means the mass operator is a singlet plus a piece
transforming in the octet like `λ₈` — i.e. `m²` is an affine function of the
hypercharge `Y` and the isospin Casimir:

    m²(I, Y)  =  a  +  b·Y  +  c·( I(I+1) − Y²/4 )

for *some* constants `a, b, c`.  Evaluating on the pseudoscalar octet —
`π` at `(I,Y) = (1,0)`, `K` at `(1/2, ±1)`, `η` at `(0,0)`, with the two kaon
hypercharges averaged as usual — the GMO combination collapses:

    4·m²_K  −  3·m²_η  −  m²_π  =  0     for ALL a, b, c.

`gmo_identity` below is exactly that statement, proved by `ring`.  The
coefficients cancel: **no choice of `a, b, c` can violate GMO**, so the relation
carries no information about the dynamics that produced them.

## The consequence for the chapter

GMO is a consequence of the *form* of the breaking (octet, first order), not of
any particular mechanism.  Therefore:

* If the QOU crossing-energy splitting is first-order octet, GMO holds
  **automatically and exactly**, and reproducing it is **not evidence** for the
  framework — every first-order octet model reproduces it equally.
* The only testable content is the ~6% **deviation**, which measures the
  *failure* of first-order breaking (second-order terms, and `η`–`η′` singlet
  mixing).  The framework has not derived a second-order term, so it currently
  predicts deviation `0`, not `3.3%`.

So the honest comparison is not "6% observed vs 3.3% predicted, factor 2 apart".
It is "6% observed vs **nothing derived**".  And the 3.3% figure is not a
competing prediction at all — it is the `q`-deformation of `dim_q(adjoint)`,
which is a *dimension*, not a mass splitting, and is not the kind of quantity
that could appear on either side of GMO.  Comparing them was a category error.

## Scope

Scope-(a).  This does not refute any QOU mechanism; it establishes that GMO
**cannot discriminate** between mechanisms, and relocates the open question to
the second-order term.  Bean `qou-8pl2`.

## Base ring (§7c)

Generic `[CommRing R]` — the cancellation is an algebraic identity in the
parameters and needs no ordering, no `ℝ`, and no archimedean content.  Masses
enter only as the squared values `m²`, so nothing here presumes positivity.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic

namespace QOU.Eightfold.GellMannOkuboIdentity

variable {R : Type*} [CommRing R]

/-- The first-order `SU(3)`-breaking mass operator, evaluated on a state of
isospin Casimir `I(I+1)` and hypercharge `Y`:

    m²(I, Y)  =  a  +  b·Y  +  c·( I(I+1) − Y²/4 ).

Multiplied through by `4` to stay division-free over a general `CommRing`, and
parametrised by `fourCasimir = 4·I(I+1)` (an integer on every octet state), so
this returns `4 m²`.  GMO is homogeneous, so the overall factor is immaterial. -/
def massSqQuadrupled (a b c fourCasimir Y : R) : R :=
  4 * a + 4 * b * Y + c * (fourCasimir - Y ^ 2)

/-- The pion: isospin `I = 1`, so `4·I(I+1) = 8`; hypercharge `Y = 0`. -/
def pionMassSq (a b c : R) : R := massSqQuadrupled a b c 8 0

/-- The eta: isospin `I = 0`, so `4·I(I+1) = 0`; hypercharge `Y = 0`. -/
def etaMassSq (a b c : R) : R := massSqQuadrupled a b c 0 0

/-- The kaon at `Y = +1`: isospin `I = 1/2`, so `4·I(I+1) = 3`. -/
def kaonPlusMassSq (a b c : R) : R := massSqQuadrupled a b c 3 1

/-- The kaon at `Y = -1` (the anti-kaon doublet). -/
def kaonMinusMassSq (a b c : R) : R := massSqQuadrupled a b c 3 (-1)

/-- The hypercharge-averaged kaon mass-squared as GMO uses it, doubled to avoid
dividing by two over a general ring: `= 2 · (4 m²_K)`. -/
def kaonAvgMassSqDoubled (a b c : R) : R :=
  kaonPlusMassSq a b c + kaonMinusMassSq a b c

/-- **Gell-Mann–Okubo is an identity of the first-order octet ansatz.**

    4 m²_K  =  3 m²_η  +  m²_π

holds for **every** choice of the breaking parameters `a, b, c`, over any
commutative ring.  (In the normalisation above: `2 · kaonAvgMassSqDoubled`
is `4 · (4 m²_K)`, matching `3 · (4 m²_η) + (4 m²_π)` on the right.)

The parameters cancel identically — `b`, the entire hypercharge dependence and
hence the whole content of an `SU(3)`-breaking mechanism, does not survive.
Consequently GMO constrains only the *form* of the breaking (octet, first
order) and has **no** power to discriminate between mechanisms sharing that
form.  Reproducing GMO is therefore not evidence for any particular dynamics,
QOU's included. -/
theorem gmo_identity (a b c : R) :
    2 * kaonAvgMassSqDoubled a b c = 3 * etaMassSq a b c + pionMassSq a b c := by
  unfold kaonAvgMassSqDoubled kaonPlusMassSq kaonMinusMassSq etaMassSq pionMassSq
    massSqQuadrupled
  ring

/-- The combination form: `4 m²_K − 3 m²_η − m²_π = 0`. -/
theorem gmo_combination_vanishes (a b c : R) :
    2 * kaonAvgMassSqDoubled a b c - (3 * etaMassSq a b c + pionMassSq a b c) = 0 := by
  rw [gmo_identity]; ring

/-- **The parameters are invisible to GMO.**  Two entirely different breaking
patterns `(a,b,c)` and `(a',b',c')` — arbitrarily far apart, hence arbitrarily
different physics — give the *same* value of the GMO combination, namely zero.

This is the discriminating-power statement: GMO cannot tell them apart. -/
theorem gmo_cannot_discriminate (a b c a' b' c' : R) :
    2 * kaonAvgMassSqDoubled a b c - (3 * etaMassSq a b c + pionMassSq a b c)
      = 2 * kaonAvgMassSqDoubled a' b' c'
        - (3 * etaMassSq a' b' c' + pionMassSq a' b' c') := by
  rw [gmo_combination_vanishes, gmo_combination_vanishes]

/-- The breaking strength `b` drops out of the GMO combination exactly, so GMO
says nothing whatever about how strong the `SU(3)` breaking is. -/
theorem gmo_independent_of_breaking_strength (a c b b' : R) :
    2 * kaonAvgMassSqDoubled a b c - (3 * etaMassSq a b c + pionMassSq a b c)
      = 2 * kaonAvgMassSqDoubled a b' c
        - (3 * etaMassSq a b' c + pionMassSq a b' c) :=
  gmo_cannot_discriminate a b c a b' c

end QOU.Eightfold.GellMannOkuboIdentity
