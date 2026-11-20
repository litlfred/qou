#!/usr/bin/env python3
"""
kms_length_dynamics_exclusion_probe — the most natural candidate for the missing
finite-temperature dynamics is the Coxeter-length scaling, and it is excluded
structurally: the Hecke quadratic relation is length-INHOMOGENEOUS, so the
length filtration generates no one-parameter automorphism group.

Bean `qou-unqc` (the open gap), arc `bk-crossing-mass-binding` (`qou-brng`).

## The gap this attacks

`mass-endomorphism/markov-trace-gibbs-free-energy.md` writes the binding law in
free-energy form, `E_bind = E_0 ln(tr_free/tr_atom)`, with the Markov trace in the
partition-function slot and `E_0` in the temperature slot -- and then states the
obstruction itself, precisely:

    "A faithful normal tracial state has trivial modular dynamics, so it
     satisfies the KMS condition at beta = 0; reading E_0 as a finite
     temperature therefore requires naming the dynamics whose equilibrium state
     this is, which the framework does not supply."

Bean `qou-unqc` records that all five corpus-grep paths and a full-text search of
the 24.7M-char library were run and found nothing framing the Markov trace as a
Gibbs or temperature state. What neither the block nor the bean does is **test a
candidate dynamics**. This probe tests the obvious one.

## The candidate, and why it is the obvious one

The Hecke tower carries a canonical `Z`-valued statistic: the Coxeter length
`l(w)` (equivalently the GS / jet-prefix filtration degree). The natural
one-parameter family is the length scaling

    sigma_t(T_w) = q^{i t l(w)} T_w .

It is the obvious candidate because (i) `beta ~ ln q` is exactly the scale match
the block names, so `q^{l}` is the Gibbs weight this grading would produce, and
(ii) it is the same filtration whose graded dimension `[A]_q!` the binding
residual work already uses as its reference.

## The exclusion

`sigma_t` is an algebra map only if it respects the Hecke quadratic relation

    sigma_i^2 = (q - q^-1) sigma_i + 1 .

The left side has length 2. The right side is a sum of a length-1 term and a
length-0 term. Applying `sigma_t` to each side and matching gives

    q^{2it} (q - q^-1) sigma_i + q^{2it} . 1   =   q^{it} (q - q^-1) sigma_i + 1

so the length-0 components force `q^{2it} = 1` and the length-1 components force
`q^{2it} = q^{it}`; for `q > 1` both hold only at `t = 0`.

So the length scaling is an automorphism only at the identity, and generates no
dynamics. Scope **(b)** -- a structural exclusion with the invariant named: **the
Hecke quadratic relation is inhomogeneous in Coxeter length.** This is the same
fact that makes the GS/jet structure a FILTRATION rather than a grading, which is
why it is not a small technicality to route around.

## The second obstruction — RETRACTING this probe's own constructive half

An earlier version of this docstring offered a constructive half: the
obstruction above is on `H_n(q)` and not on its associated graded, `gr H_n(q)`
IS length-graded by construction, so "does the Markov trace descend to
`gr H_n(q)`, and is the descended state KMS at beta = ln q there?" looked like a
bounded yes/no worth asking next. **That is RETRACTED. The question is already
answered NO**, and the body of this probe runs the argument as a gate.

For a state `phi` and a dynamics acting by a character of a grading,
`sigma_t(y) = q^{i t l(y)}` on homogeneous `y`, the KMS_beta condition
`phi(x sigma_{i beta}(y)) = phi(y x)` reads `q^{-beta l(y)} phi(xy) = phi(yx)`.
If `phi` is TRACIAL then `phi(xy) = phi(yx)`, so `q^{-beta l(y)} = 1` whenever
`phi(xy) != 0`; taking `y = sigma_i` (l = 1) and `x = sigma_i^-1` gives
`phi(1) != 0`, hence `beta ln q = 0` and `beta = 0`.

This holds for ANY grading and ANY algebra, on `H_n(q)` or on `gr` alike, so
the descent question is moot: a descended trace is still KMS only at beta = 0.
The problem was never the grading -- it is **traciality**, which is exactly what
Tomita-Takesaki says (trivial modular group <=> tracial).

The result is SHARPER than the retracted version, not weaker: no
character-of-a-grading flow gives finite beta against a tracial state, so the
finite-temperature state **cannot be `tr_M` itself; it must be a NON-TRACIAL
weight**. The live route is `phi(x) = tr_M(h x)` for positive `h`, with modular
flow `sigma_t(x) = h^{it} x h^{-it}` -- not attempted here, and note that the
`y_lambda` weighting does NOT supply that `h`: a positive combination of
characters is again a trace, so `h` must come from outside the centre.

## What is NOT claimed

  * NOT that the free-energy form is wrong. The block already scopes it as an
    analogy; this narrows which dynamics could license it, and removes one.
  * NOT that no dynamics exists. One candidate is excluded, by a named
    invariant. Others (a Connes cocycle against a non-tracial weight, the
    Radon-Nikodym derivative of the y_lambda reweighting) are untouched here.
  * NOT anything numerical about binding. No binding value moves.

NO FLOAT64: exact symbolic arithmetic in sympy over `Q(q)`; the one numerical
evaluation is at the 50-digit proton pin in mpmath `mpf`. `float` appears nowhere.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 50

q = sp.symbols("q", positive=True)
# t is the REAL flow parameter and must include 0 in its domain: the whole point
# is that t = 0 is the ONLY solution, so declaring t positive would return an
# empty solution set and hide the identity. (It did, on the first run.)
t = sp.symbols("t", real=True)
I = sp.I


def fmt(x, n=10):
    return mp.nstr(x, n)


def main() -> int:
    print("kms_length_dynamics_exclusion_probe")
    print("=" * 78)
    print("THE GAP (bean qou-unqc, block markov-trace-gibbs-free-energy):")
    print("  E_bind = E_0 ln(tr_free/tr_atom) puts the Markov trace in the")
    print("  partition-function slot and E_0 in the temperature slot.  But a")
    print("  faithful normal TRACIAL state has trivial modular dynamics -- it is")
    print("  KMS at beta = 0.  A finite temperature needs a named dynamics.")
    print()
    print("THE CANDIDATE:  sigma_t(T_w) = q^{i t l(w)} T_w,  l = Coxeter length")
    print("  (= the GS / jet-prefix filtration degree).  Obvious because the")
    print("  block's own scale match is beta ~ ln q, so q^l is the Gibbs weight")
    print("  this grading would produce.")
    print()

    print("THE TEST — does it respect the Hecke quadratic relation?")
    print("-" * 78)
    print("  Relation (repo convention, AGENTS.md 7a):")
    print("      sigma_i^2 = (q - q^-1) sigma_i + 1")
    print("  Lengths:  LHS = 2.   RHS = one length-1 term + one length-0 term.")
    print("  The relation is INHOMOGENEOUS in length -- that is the whole point.")
    print()

    # Apply sigma_t formally. Represent an element by its (length -> coefficient)
    # decomposition; sigma_t multiplies the length-l part by q^{i t l}.
    scale = lambda l: q ** (I * t * l)                       # noqa: E731

    # LHS: sigma_i^2 is a single length-2 basis element, so sigma_t scales it by
    # q^{2it} -- and then we REWRITE it by the relation.
    lhs_after = {1: scale(2) * (q - 1 / q), 0: scale(2) * sp.Integer(1)}
    # RHS: rewrite FIRST, then apply sigma_t componentwise.
    rhs_after = {1: scale(1) * (q - 1 / q), 0: scale(0) * sp.Integer(1)}

    print(f"{'length':>8} {'rewrite-then-sigma_t':>34} {'sigma_t-then-rewrite':>34}")
    conditions = []
    for l in (1, 0):
        a, b = sp.simplify(rhs_after[l]), sp.simplify(lhs_after[l])
        conditions.append(sp.simplify(b - a))
        print(f"{l:>8} {str(a):>34} {str(b):>34}")
    print()
    print("  For sigma_t to be an algebra map the two columns must agree, i.e.")
    for l, c in zip((1, 0), conditions):
        print(f"    length {l}:  {sp.simplify(c)} = 0")
    print()

    # Solve. The length-0 condition is q^{2it} = 1; with q > 1 real this forces
    # t = 0. Verify by solving the exponent equation rather than asserting it.
    sols = sp.solve(sp.Eq(2 * I * t * sp.log(q), 0), t)
    print(f"  length-0 condition  q^(2it) = 1  =>  2 i t ln q = 0  =>  t in {sols}")
    assert sols == [0], "the length-0 condition must force t = 0"
    # And the length-1 condition independently forces q^{2it} = q^{it}.
    sols1 = sp.solve(sp.Eq(2 * I * t * sp.log(q), I * t * sp.log(q)), t)
    print(f"  length-1 condition  q^(2it) = q^(it)  =>  t in {sols1}")
    assert sols1 == [0], "the length-1 condition must force t = 0"
    print()
    print("  BOTH components independently force t = 0.  The length scaling is an")
    print("  automorphism ONLY at the identity, so it generates NO dynamics.")
    print()

    # Show the failure is not marginal at the live pin: the mismatch factor at a
    # representative t is far from 1.
    q0 = Q_MP
    print("  Not a marginal failure.  At the 50-digit proton pin the two columns")
    print("  differ by the factor q^(it) on the length-1 term; its modulus is 1")
    print("  but its PHASE separates them.  Phase gap at a few sample t:")
    print(f"{'t':>8} {'arg q^(2it) - arg q^(it)  [rad]':>34}")
    lq = mp.log(q0)
    for tv in ("0.5", "1", "5", "10"):
        tt = mp.mpf(tv)
        print(f"{tv:>8} {fmt(tt * lq, 12):>34}")
    print(f"  (ln q0 = {fmt(lq, 12)}, so the phases coincide only at t = 0)")
    print()

    print("SCOPE (b) — a structural exclusion, invariant named")
    print("-" * 78)
    print("  The invariant: THE HECKE QUADRATIC RELATION IS INHOMOGENEOUS IN")
    print("  COXETER LENGTH.  This is the same fact that makes the GS / jet")
    print("  structure a FILTRATION rather than a grading, so it is not a")
    print("  technicality to route around -- it is the defining feature.")
    print()

    print("THE SECOND OBSTRUCTION — and it is the one that actually decides this")
    print("-" * 78)
    print("  RETRACTION.  The first version of this probe offered a constructive")
    print("  half: the obstruction above is on H_n(q) and NOT on gr H_n(q), which")
    print("  IS length-graded, so 'does the Markov trace descend to gr, and is the")
    print("  descended state KMS at beta = ln q there?' looked like a bounded")
    print("  yes/no worth asking next.  THAT QUESTION IS ALREADY ANSWERED NO, by")
    print("  an argument I should have run before proposing it.")
    print()
    print("  For a state phi and a dynamics acting by a character of a grading,")
    print("  sigma_t(y) = q^{i t l(y)} y on homogeneous y, the KMS_beta condition")
    print("  phi(x sigma_{i beta}(y)) = phi(y x) reads")
    print()
    print("      q^{-beta l(y)} phi(xy) = phi(yx).")
    print()
    print("  If phi is TRACIAL then phi(xy) = phi(yx), so q^{-beta l(y)} = 1")
    print("  whenever phi(xy) != 0.  Taking y = sigma_i (l = 1) and x = sigma_i^-1")
    print("  gives phi(1) != 0, so beta * ln q = 0 and beta = 0.")
    b, ell = sp.symbols("beta ell", positive=True)
    sols_b = sp.solve(sp.Eq(-b * ell * sp.log(q), 0), b)
    print(f"    solved rather than asserted: beta in {sols_b} over beta > 0")
    assert sols_b == [], "no POSITIVE beta may satisfy the tracial KMS condition"
    print("    (empty over beta > 0 -- i.e. beta = 0 is the only solution)")
    print()
    print("  This holds for ANY grading, ANY algebra, on H_n(q) or on gr H_n(q)")
    print("  alike.  So the descent question is moot: if the descended state is")
    print("  still a trace, it is still KMS only at beta = 0.  The problem was")
    print("  never the grading.  It is TRACIALITY.")
    print()
    print("WHAT THIS LEAVES — sharper than the retracted version, not weaker")
    print("-" * 78)
    print("  Combining, the licence cannot be recovered by choosing a better")
    print("  dynamics on tr_M at all: no character-of-a-grading flow gives finite")
    print("  beta against a tracial state.  So the requirement is structural --")
    print()
    print("      the finite-temperature state CANNOT be tr_M itself; it must be a")
    print("      NON-TRACIAL weight.")
    print()
    print("  That is exactly what Tomita-Takesaki says (trivial modular group <=>")
    print("  tracial), so the block's own diagnosis was already the whole story;")
    print("  what is added here is that the two obvious escapes -- a different")
    print("  grading, or passing to gr -- are both closed.")
    print()
    print("  The live route is therefore a non-tracial weight phi(x) = tr_M(h x)")
    print("  for positive h, whose modular flow is sigma_t(x) = h^{it} x h^{-it}.")
    print("  NOT attempted here, and one caution for whoever does: the y_lambda")
    print("  weighting does NOT supply that h.  A positive combination of")
    print("  characters is again a trace, so tr_M = sum_lambda y_lambda chi^lambda")
    print("  is tracial and reweighting the blocks cannot escape the argument")
    print("  above.  The h must come from outside the centre.")
    print()

    print("WHAT IS NOT CLAIMED")
    print("-" * 78)
    print("  * NOT that the free-energy form is wrong.  The block already scopes")
    print("    it as an analogy; this removes one candidate licence, not the form.")
    print("  * NOT that no dynamics exists.  ONE candidate is excluded, by a")
    print("    named invariant.  A Connes cocycle against a non-tracial weight,")
    print("    or the Radon-Nikodym derivative of the y_lambda reweighting, are")
    print("    untouched here.")
    print("  * NOT anything numerical.  No binding value moves.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
