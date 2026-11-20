#!/usr/bin/env python3
"""The flavour split's `1/3` IS the q=1 value of the corpus's own three-channel weight.

WHAT THIS ESTABLISHES
---------------------
Two prior probes on this arc identified the `(q^2 - q^-2)` factor of
`conj:flavor-split-habiro-derivation`'s baseline as a Markov trace, and
constrained the `hbar_q^2` by bar-parity and vanishing order.  Both recorded that
**the `/3` was untouched** -- parity cannot see it (3 is bar-invariant) and
neither can the order argument.  This probe identifies it.

`docs/audits/2026-06-17-hecke-channel-chirality-binding.md` carries three
substrate weights per crossing,

    w_sym = w_alt = q^2/(q^4+4q^2+1),    w_std = (q^2+1)^2/(q^4+4q^2+1)

and section 1 below shows those ARE the q-deformed Plancherel measure of H_3: at
q = 1 they are 1/6, 2/3, 1/6, which is `(f^lam)^2/n!` for the partitions
(3), (2,1), (1^3) with f^lam = 1, 2, 1 and n! = 6.

The k=2 crossing reversal is `2h*sigma - h^2` (proved: reversal_two + inv_eq), so
in the audit's (c,d) parametrisation c = 2h, d = -h^2, and the channel values are

    sym   c*q   + d  =  q^2 - q^-2  =  R
    std   c*z_D + d  =  alpha * R          alpha = (q^4+1)/(q^2+1)^2
    alt  -c/q   + d  =  -R

The sym and alt terms cancel under w_sym = w_alt, leaving

    w_sym*R + w_std*(alpha*R) + w_alt*(-R)  =  (q^4+1)/(q^4+4q^2+1) * R

and that weight ratio at q = 1 is EXACTLY 1/3.

**So the block's `1/3` is the q=1 value of its own three-channel weight.**  The
constant is identified; it was never a free number.

WHAT THIS DOES NOT SETTLE
-------------------------
Identifying where the 1/3 comes from is not establishing that 1/3 is the right
object.  The corpus's expression pairs a CLASSICAL (q=1) measure with q-DEFORMED
channel values and a q-deformed hbar_q^2.  Three numbers are in play at the proton
q0 and all three differ (section 4).  The corpus uses the fully classical one.

AGENTS.md's notation register states the governing rule directly: "Three
partition-weight families ... are distinct at q != 1 and coincide at q = 1; never
conflate."  This is an instance, and here it is not cosmetic: 1.45 % on the
weight, moving the baseline from -0.128 % to +1.32 % against the measured split.

Which of the three is correct is a MODELLING question this probe does not answer,
and per NO-FITTING it must not be answered by residual -- note that the LEAST
deformed option is the MOST accurate, so choosing by accuracy would keep 1/3 for
the wrong reason.  What is delivered is the identification and the exact size of
the fork.

A CORRECTION MADE IN AUTHORING, recorded because it is the point of
formalize-first: the condition for the deformed weight to equal 1/3 was first
written as `q^4 = 2q^2`.  `lean` rejected it.  The truth is `q^4 + 1 = 2q^2`,
i.e. `(q^2-1)^2 = 0`, i.e. **q^2 = 1 and nothing else** -- which is the notation
register's rule made exact for this weight, and a stronger statement than the
one I set out to prove.

Lean: `QOU/Hecke/FlavourSplitThreeChannelWeight.lean` (10 decls, lean-direct
exit 0 / 0 warnings, #print axioms clean).

Run: python3 computations/qbeta/flavour_split_three_channel_weight_probe.py
"""

from __future__ import annotations

import sys

import sympy as sp
from mpmath import mp

mp.dps = 60

_q = sp.symbols("q", positive=True)

H = _q - 1 / _q
Z_D = _q**3 / (_q**2 + 1)
HBAR = 1 - 1 / _q
R = _q**2 - _q**-2
ALPHA = (_q**4 + 1) / (_q**2 + 1) ** 2
DEN = _q**4 + 4 * _q**2 + 1
W_SYM = _q**2 / DEN
W_STD = (_q**2 + 1) ** 2 / DEN
WEIGHT_RATIO = (_q**4 + 1) / DEN
X_BASELINE = (_q - 1) ** 2 * (1 - _q**-4) / 3


def main() -> int:
    ok = True

    print("1. THE AUDIT'S WEIGHTS ARE THE q-DEFORMED PLANCHEREL MEASURE OF H_3")
    print("   partitions of 3: (3) f=1, (2,1) f=2, (1^3) f=1;  sum f^2 = 6 = 3!")
    for lbl, w, f in (("(3)   sym", W_SYM, 1), ("(2,1) std", W_STD, 2),
                      ("(1^3) alt", W_SYM, 1)):
        lim = sp.limit(w, _q, 1)
        cls = sp.Rational(f * f, 6)
        good = lim == cls
        ok &= good
        print(f"   {lbl}: w(1) = {lim}   classical (f^lam)^2/n! = {cls}   "
              f"{'MATCH' if good else 'MISMATCH'}")
    s = sp.simplify(W_SYM + W_STD + W_SYM)
    ok &= s == 1
    print(f"   sum of the three w(q) = {s}   (a probability measure at every q)")

    print()
    print("2. THE THREE CHANNEL VALUES OF sigma^2 - sigma^-2   (c,d) = (2h, -h^2)")
    c, d = 2 * H, -H**2
    checks = (("sym  c*q   + d", c * _q + d, R, "R"),
              ("std  c*z_D + d", c * Z_D + d, ALPHA * R, "alpha*R"),
              ("alt -c/q   + d", c * (-1 / _q) + d, -R, "-R"))
    for lbl, got, want, wl in checks:
        diff = sp.simplify(got - want)
        ok &= diff == 0
        print(f"   {lbl} - ({wl}) = {diff}   {'EXACT' if diff == 0 else 'MISMATCH'}")

    print()
    print("3. THE WEIGHTED COMBINATION COLLAPSES, AND ITS q=1 VALUE IS 1/3")
    full = W_SYM * R + W_STD * (ALPHA * R) + W_SYM * (-R)
    coll = sp.simplify(full - WEIGHT_RATIO * R)
    ok &= coll == 0
    print(f"   w_sym*R + w_std*alpha*R + w_alt*(-R) - weightRatio*R = {coll}   "
          f"{'EXACT' if coll == 0 else 'MISMATCH'}")
    print(f"   weightRatio = {sp.factor(WEIGHT_RATIO)}")
    lim = sp.limit(WEIGHT_RATIO, _q, 1)
    ok &= lim == sp.Rational(1, 3)
    print(f"   weightRatio at q = 1 = {lim}   "
          f"{'IS EXACTLY 1/3' if lim == sp.Rational(1, 3) else 'NOT 1/3'}")
    sol = sp.solve(sp.Eq(WEIGHT_RATIO, sp.Rational(1, 3)), _q**2)
    print(f"   and weightRatio(q) = 1/3 solves to q^2 = {sol}   "
          f"-- (q^2-1)^2 = 0, the classical point and nothing else")

    print()
    print("4. THREE DIFFERENT NUMBERS AT q0, AND THE CORPUS USES THE CLASSICAL ONE")
    from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP        # noqa: PLC0415
    q0 = Q_MP

    def at(e):
        return mp.mpf(str(sp.N(e.subs(_q, sp.Float(str(q0), 50)), 45)))

    mixed = sp.Rational(1, 6) * 1 + sp.Rational(2, 3) * ALPHA + sp.Rational(1, 6) * (-1)
    rows = (("fully deformed  w(q) x value(q)", WEIGHT_RATIO),
            ("classical w(1)  x value(q)", mixed),
            ("the corpus's 1/3", sp.Rational(1, 3)))
    vals = []
    for lbl, e in rows:
        v = at(e) if e != sp.Rational(1, 3) else mp.mpf(1) / 3
        vals.append(v)
        print(f"   {lbl:34s} = {mp.nstr(v, 14)}")
    ok &= (vals[0] != vals[1]) and (vals[1] != vals[2])
    print(f"   deformed vs 1/3: rel {mp.nstr((vals[0]-vals[2])/vals[2], 6)}   "
          f"(all three distinct: {vals[0] != vals[1] != vals[2]})")

    print()
    print("5. WHAT THAT DOES TO THE BASELINE  (reported, NOT used to choose)")
    tgt = mp.mpf("0.0013774698046076")
    for lbl, e in (("with 1/3 (the corpus's)", X_BASELINE),
                   ("with the deformed weight", HBAR**2 * WEIGHT_RATIO * R),
                   ("with classical w(1) x value(q)", HBAR**2 * mixed * R)):
        v = at(e)
        print(f"   {lbl:32s} = {mp.nstr(v, 14)}   rel {mp.nstr((v-tgt)/tgt, 6):>12s}")
    print("   -> the LEAST deformed option is the MOST accurate, so choosing by")
    print("      residual would keep 1/3 for the wrong reason.  Per NO-FITTING the")
    print("      residuals are recorded and are NOT the argument.  Which measure is")
    print("      correct is a modelling question and is OPEN.")

    print()
    print("6. THE `/3` AND THE k=3 / k=2 GAP ARE ONE DEFECT")
    K3 = _q**3 - _q**-3
    cen = sp.simplify(3 * H + H**3 - K3)
    ok &= cen == 0
    print(f"   sigma^3 - sigma^-3 = 3h + h^3 - (q^3-q^-3) = {cen}   central scalar")
    print("   A central element needs NO measure: the weights sum to 1, so the")
    print("   channel average returns it unchanged (Lean: central_value_unweighted).")
    print("   So the narrative object, read as its OWN centrality argument dictates,")
    print("   carries no 1/3 at all.  Four cells, against the measured split:")
    cells = (("k=3, no measure (centrality dictates)", HBAR**2 * K3),
             ("k=3, with a 1/3 anyway", HBAR**2 * K3 / 3),
             ("k=2, classical 1/3 (the corpus)", X_BASELINE),
             ("k=2, deformed weight(q)", HBAR**2 * WEIGHT_RATIO * R))
    for lbl, e in cells:
        v = at(e)
        print(f"      {lbl:38s} = {mp.nstr(v, 12):>16s}  rel {mp.nstr((v-tgt)/tgt, 6):>12s}")
    print("   -> the two halves are different KINDS of object, not two numbers for")
    print("      one object: a central scalar (no measure) vs an algebra element")
    print("      (needs one).  The 1/3 is the FINGERPRINT of the switch -- it can")
    print("      only appear on the side that needs a measure.  Scope (a): a")
    print("      measured negative about what the block's own argument yields, with")
    print("      no invariant excluding a k=3 route that normalises some other way.")

    print()
    print("VERDICT:", "PASS -- the 1/3 is the q=1 value of the corpus's own "
          "three-channel weight, which is the Plancherel measure of H_3; the "
          "classical-vs-deformed choice is identified and left open"
          if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
