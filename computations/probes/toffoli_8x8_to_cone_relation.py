"""Question (b) of bean qou-ahu3 is VACUOUS as posed — the 8x8 entries generate
all of Q(q), so a rational relation to the cone condition exists trivially.

WHAT WAS ASKED.  The Toffoli arc established that the LP cone condition is a
single constraint with numerator q^10 + q^6 - q^4 + q^2 - 1 over the Hecke NF
basis, while P_77/P_76 are entries of an 8x8 matrix indexed by strand-type
orderings.  No map between the index sets was recorded, and I posed the
remaining question as: "is there ANY relation between the 8x8 entries and the
cone condition?"

THAT QUESTION HAS NO CONTENT.  Measured below: the entries include

    M33 = q(q^2+1)/4                M44 = (q^2+1)/(4 q^3)
    M00 = (q^4+1)/(q^3 (q^2+1)^2)   M77 = q^3 (q^4+1)/(q^2+1)^2

and therefore

    M33/M44 = q^4 ,   M77/M00 = q^6 ,   so (M77/M00)/(M33/M44) = q^2 ,
    and  4 M33 / (q^2 + 1) = q .

q itself is a rational expression in four of the entries, so they generate the
whole field Q(q).  Every rational function of q -- the cone numerator included
-- is then a rational expression in them, trivially and uninformatively.  The
content of any such relation has to lie in its FORM, not in its existence.

A CORRECTION I OWE.  My first pass at this concluded the opposite, from the
observation (still true, verified below) that the cone numerator divides NO
entry's numerator.  I inferred "therefore no rational expression in them equals
the cone condition".  That inference is WRONG: e1 - e2 can vanish where neither
e1 nor e2 does, so the zero set of a rational expression is not confined to the
union of its constituents' zeros.

What the divisibility result DOES support, and all it supports:

    NO MONOMIAL -- product or quotient -- of the 8x8 entries equals the cone
    condition, because for a monomial the zero set IS the union of numerator
    zeros minus denominator zeros, and q_c is a zero of none of them.

WHY THE EARLIER REFUTATION IS UNAFFECTED.  prop:toffoli-lp-stability reduces
the cone condition to "P_77 . W_std with the appropriate sign from P_76" -- a
monomial times a sign, which is exactly the case the divisibility argument
covers.  The zero-set refutation recorded in that block stands; only my broader
claim about arbitrary rational expressions was over-reached.

Exact symbolic arithmetic; no floating point.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import sympy as sp                                          # noqa: E402
from toffoli_nf_coordinates_and_lp_feasibility import (     # noqa: E402
    chain_element, decode, q as qs,
)

Z = qs ** 3 / (qs ** 2 + 1)                    # convention D
CONE = qs ** 10 + qs ** 6 - qs ** 4 + qs ** 2 - 1

CHECKS: list[tuple[str, bool]] = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"         {detail}")


def V(i, o):
    a, b = chain_element(i, o)
    return sp.cancel(Z * a + b)


def tout(k):
    b1, b2, b3 = decode(k)
    return (b1 << 2) | (b2 << 1) | (b3 ^ (b1 & b2))


def entries():
    E = {}
    for k in range(8):
        o = decode(k)
        E[f"M{k}{k}"] = sp.cancel(V(0, o) * V(1, o))
        m = tout(k)
        if m != k:
            om = decode(m)
            Vp = [V(i, o) for i in range(2)]
            Vd = [V(i, om) for i in range(2)]
            E[f"M{m}{k}"] = sp.cancel(sum(
                sp.prod([Vp[j] for j in range(2) if j != c]) * (Vp[c] - Vd[c])
                for c in range(2)))
    return E


def main() -> int:
    E = entries()
    print("=" * 74)
    print("  QUESTION (b) IS VACUOUS AS POSED")
    print("=" * 74)
    print()
    for n, e in sorted(E.items()):
        print(f"    {n:<6} = {sp.factor(e)}")
    print()

    # 1. the divisibility fact -- true, and narrower than I first claimed
    div = [n for n, e in E.items()
           if sp.div(sp.Poly(sp.expand(sp.numer(sp.cancel(e))), qs),
                     sp.Poly(CONE, qs))[1].is_zero]
    check("the cone numerator divides NO entry's numerator",
          not div,
          f"entries divisible: {div or 'none'} -> no MONOMIAL in the entries "
          f"equals the cone condition")

    # 2. but the entries generate all of Q(q)
    q4 = sp.cancel(E["M33"] / E["M44"])
    q6 = sp.cancel(E["M77"] / E["M00"])
    q2 = sp.cancel(q6 / q4)
    q1 = sp.cancel(4 * E["M33"] / (q2 + 1))
    check("M33/M44 = q^4", sp.simplify(q4 - qs ** 4) == 0, f"= {sp.simplify(q4)}")
    check("M77/M00 = q^6", sp.simplify(q6 - qs ** 6) == 0, f"= {sp.simplify(q6)}")
    check("q is a rational expression in the entries",
          sp.simplify(q1 - qs) == 0,
          "4*M33/((M77/M00)/(M33/M44) + 1) = q")
    check("therefore the cone numerator is expressible (trivially)",
          sp.simplify((q1 ** 10 + q1 ** 6 - q1 ** 4 + q1 ** 2 - 1) - CONE) == 0,
          "every rational function of q is; the question has no content")

    print()
    n = sum(1 for _, ok in CHECKS if ok)
    print("=" * 74)
    print(f"  {n}/{len(CHECKS)} assertions")
    print("=" * 74)
    print()
    print("  VERDICT.  Question (b) must be RE-POSED.  'Does a relation exist' is")
    print("  answered trivially yes.  A meaningful successor asks for a relation")
    print("  of a RESTRICTED FORM -- e.g. is the cone condition a monomial in the")
    print("  entries (NO, proved above), or a Z-linear combination of them, or")
    print("  expressible without reconstructing q first.")
    return 0 if n == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
