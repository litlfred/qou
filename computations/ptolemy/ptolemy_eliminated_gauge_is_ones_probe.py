#!/usr/bin/env python3
"""Diagnose my own NO-SOLUTION result: are the 6 eliminated coordinates simply 1?

WHAT THIS CORRECTS.  ptolemy_class1_full_assignment.py substitutes the 26 recorded
coordinates of L6a4-c1-ptolemy-in-K.json plus u into the UN-ELIMINATED variety (33
variables, 39 equations), leaves the remaining 6 symbolic, and solves.  Run 2026-09-07
it reported:

    known from the file: 27;  unknown: 6 -> ['c_0012_0', 'c_0012_1', 'c_0102_1',
                                             'c_0111_0', 'c_1002_0', 'c_2001_0']
    candidate solutions: 0
    NO candidate satisfies all equations.

That verdict was reported as a property of the DATA.  It is not: the point demonstrably
exists (a sibling session answered issue #7092 on it, main f7fee734c3).  So either the
producer is wrong or the recorded coordinates do not extend -- and those are very
different facts.

THE HYPOTHESIS, which is derivation not search.  snappy's eliminate_fixed_ptolemys=True
does not project or re-gauge; it SUBSTITUTES the fixed Ptolemy coordinates with the
value GGZ Remark 5.3 assigns them, namely 1.  If that is what it does, the eliminated
point IS an un-eliminated point whose 6 missing coordinates are each exactly 1 -- there
is nothing to solve, and a solver returning 0 candidates is a defect in the solver call,
not a fact about the point.

THE TEST.  Set all six to 1 and evaluate all 39 un-eliminated equations exactly in
K = Q[T]/(f).  No solving, no tolerance: each equation reduces to the zero polynomial or
it does not.  Also reports, per equation, which fail -- a partial failure would say the
elimination is not a plain substitution and would be the interesting outcome.

Exact arithmetic throughout (sympy Rationals mod f).  No floats.
"""
import json
import re
import warnings

warnings.filterwarnings('ignore')
import sympy as sp
import snappy

T = sp.Symbol('T')
SRC = 'computations/ptolemy/L6a4-c1-ptolemy-in-K.json'


def main():
    d = json.load(open(SRC))
    f = sp.sympify(d['field']['min_poly'].replace('t', 'T'))
    red = lambda e: sp.expand(sp.rem(sp.expand(e), f, T))
    co = {k: sp.expand(sp.sympify(re.sub(r'\bt\b', 'T', v)))
          for k, v in d['ptolemy'].items()}
    u = co['u']
    assert red(u ** 2 + u + 1) == 0, "u is not a primitive cube root of unity"

    M = snappy.Manifold(d['manifold'])
    V = M.ptolemy_variety(3, obstruction_class=d['obstruction_class'])
    allv = sorted({str(v) for v in V.variables})
    eqs = [str(e) for e in V.equations]
    print(f"un-eliminated variety: {len(allv)} variables, {len(eqs)} equations", flush=True)

    known = {k: v for k, v in co.items() if k in allv}
    unknown = [v for v in allv if v not in co]
    print(f"known from the file: {len(known)};  unknown: {len(unknown)} -> {unknown}",
          flush=True)

    # THE HYPOTHESIS: every eliminated coordinate is 1.
    subs = dict(known)
    for v in unknown:
        subs[v] = sp.Integer(1)
    subs['t'] = u          # snappy writes the obstruction cube root as t
    subs['u'] = u

    local = {k: sp.sympify(v) if not isinstance(v, sp.Expr) else v
             for k, v in subs.items()}
    local['T'] = T

    bad = []
    for e in eqs:
        expr = sp.sympify(e, locals=local)
        if red(expr) != 0:
            bad.append(e)

    print(f"\nequations vanishing exactly in K: {len(eqs) - len(bad)} / {len(eqs)}",
          flush=True)
    if not bad:
        print("\nALL 39 vanish with every eliminated coordinate = 1.")
        print("=> the elimination IS a plain substitution of 1, there was never")
        print("   anything to solve, and the producer's 'candidate solutions: 0'")
        print("   is a defect in ITS solver call -- not a fact about the point.")
    else:
        print(f"\n{len(bad)} equation(s) FAIL at all-ones.  First 5:")
        for e in bad[:5]:
            print("   ", e)
        print("\n=> the elimination is NOT a plain substitution of 1.  That is the")
        print("   interesting outcome and must be understood before any claim about")
        print("   the recorded 26 extending or failing to extend.")


if __name__ == '__main__':
    main()
