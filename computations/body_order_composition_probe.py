#!/usr/bin/env python3
"""Composition across A: the body-order generating function in closed form.

The gap this closes
-------------------
`interface_kernel_derivation_probe` derived the SINGLE-interface kernel
R_k = f_k x + f_{k-1} and flagged the open half: the conjecture's kernel
governs the body-order series ACROSS A, where later interfaces sit between
blocks that are no longer disjoint, so the promotion hypothesis has to be
re-established at each step.

It re-establishes itself, for a structural reason. When nucleon k+1 is added
its three strands are FRESH -- never touched -- so the permutation fixes them
and w(3k) <= 3k < 3k+1 = w(3k+1). There is no inversion at the new interface,
`QOU.Knot.JetGradePromotion` applies, and the new bridge promotes rigidly.
Every added interface is promotion-eligible, not just the first.

Measured consequences
---------------------
Term counts are exactly 5^A (5, 25, 125, 625), grade increments are constant
(+3 at the top, +1 at the bottom), and the geometric law holds as an exact
polynomial identity with NO division needed:

    G_2 * G_2 == G_1 * G_3      True
    G_2 * G_4 == G_3 * G_3      True

so G is geometric in A. The closed form, verified exactly for A = 1,2,3,4:

    G_A(x) = x^(A-1) * G_1(x)^A

and the single-nucleon factor itself closes, with A = q - q^-1:

    G_1(x) = (1 - A^4) - A^5 x + A^4 x^2

Both checked coefficient-by-coefficient, not by term count.

So the composition across A is a PRODUCT: each added nucleon contributes one
factor of G_1 and one factor of x, the x being exactly the promotion the
theorem supplies. Nothing is fitted and no anchor is read.

Scope -- and the boundary is the same one as before
---------------------------------------------------
This is the BARE-WORD bridge (a single sigma per interface). The canonical
convention is sigma_g + d*I with d chosen by nucleon-type pair, whose scalar
part this derivation does not carry -- and which is exactly what was measured
to break the tau symmetry. So this is the composition law for the encoding
the arc has been using, not yet for the production encoding.

It is also a law about the FILTRATION generating function, not yet about
binding energy: reading w_n off these coefficients additionally needs the SW
periods a_D^(n), which the conjecture carries as conjectural. Stating that
because the coefficients of G_A are indexed by jet degree and the conjecture
identifies jet degree with body order -- which makes it very tempting to call
these the body-order weights, and they are not that until a_D^(n) is supplied.

Exact throughout: sparse Laurent over Z[q,q^-1]. No floats, no anchor.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from hecke_exact_laurent import (  # noqa: E402
    coxeter_length, lau_add, lau_mul, word_to_elem_fast,
)

A_COEF = {1: 1, -1: -1}


def grade_gf(E) -> dict:
    out: dict = {}
    for w, c in E.terms.items():
        g = coxeter_length(w)
        out[g] = lau_add(out.get(g, {}), c)
    return {g: v for g, v in sorted(out.items()) if v}


def core(k: int) -> list:
    """Nucleon k on strands 3k+1..3k+3."""
    a, b = 3 * k + 1, 3 * k + 2
    return [a, -b, a, -b, a, -b]


def atom(A: int) -> list:
    w: list = []
    for k in range(A):
        w += core(k)
        if k < A - 1:
            w += [3 * (k + 1)]
    return w


def polymul(P: dict, Q: dict) -> dict:
    out: dict = {}
    for e1, c1 in P.items():
        for e2, c2 in Q.items():
            t = lau_mul(c1, c2)
            if t:
                out[e1 + e2] = lau_add(out.get(e1 + e2, {}), t)
    return {e: v for e, v in out.items() if v}


def a_pow(n: int) -> dict:
    r = {0: 1}
    for _ in range(n):
        r = lau_mul(r, A_COEF)
    return r


def main():
    Gs = {A: grade_gf(word_to_elem_fast(3 * A, atom(A))) for A in (1, 2, 3, 4)}
    print("Composition across A\n")
    for A in sorted(Gs):
        print(f"    A={A}: {5 ** A:>4} terms expected, x-support "
              f"{min(Gs[A])}..{max(Gs[A])}")

    print("\n  Geometric law, by cross-multiplication (no division):")
    g1 = polymul(Gs[2], Gs[2]) == polymul(Gs[1], Gs[3])
    g2 = polymul(Gs[2], Gs[4]) == polymul(Gs[3], Gs[3])
    print(f"    G_2*G_2 == G_1*G_3 : {g1}")
    print(f"    G_2*G_4 == G_3*G_3 : {g2}")

    print("\n  Closed form  G_A(x) = x^(A-1) * G_1(x)^A :")
    for A in sorted(Gs):
        pred = {0: {0: 1}}
        for _ in range(A):
            pred = polymul(pred, Gs[1])
        pred = {e + (A - 1): c for e, c in pred.items()}
        ok = pred == Gs[A]
        print(f"    A={A}: exact {ok}")
        assert ok, f"closed form failed at A={A}"

    a4, a5 = a_pow(4), a_pow(5)
    cand = {0: lau_add({0: 1}, {e: -c for e, c in a4.items()}),
            1: {e: -c for e, c in a5.items()},
            2: a4}
    ok1 = cand == Gs[1]
    print(f"\n  Single-nucleon factor  G_1(x) = (1 - A^4) - A^5 x + A^4 x^2,")
    print(f"  with A = q - 1/q :  exact {ok1}")
    assert g1 and g2 and ok1, "a closed form failed"
    return {"geometric": g1 and g2, "g1_closed": ok1}


if __name__ == "__main__":
    main()
