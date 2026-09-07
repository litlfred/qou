#!/usr/bin/env python3
"""Does the SAME K-point solve P^c at one cube root of unity and P^{-c} at the other?

WHAT THIS TESTS.  `QOU.Eightfold.Ptolemy.TwistedEq.eval_negTwist` (Lean, sorry-free)
says that applying a ring map with sigma(u) = u^2 to a point of the c-twisted Ptolemy
system evaluates the (-c)-twisted system.  Read on the other side -- with the
substitution acting on the COEFFICIENT rather than on the point -- that is:

    x solves P^c  at  u = u_1      <==>      x solves P^{-c}  at  u = u_2

where u_1, u_2 are the two primitive cube roots of unity, u_2 = u_1^2 = -1 - u_1.
This script checks that on the one L6a4 class where an exact point is known.

WHY THIS IS A DIFFERENT MEASUREMENT FROM ptolemy_duality_galois_check.py.  That script
compared the two systems of EQUATIONS as polynomial sets and found them related by
u -> u^2.  This one holds the equations fixed and evaluates a genuine SOLUTION in them.
An equation-level identity says the varieties are abstractly related; a point-level
check says a specific solution actually crosses.  The second does not follow from the
first without knowing the point is defined over a field where both u_i live -- which is
the fact established below.

WHAT IS NOT TESTED HERE.  Nothing about representations.  In particular this does NOT
show that the duality involution rho -> rho^{-T} induces this crossing; that
identification is open, bean qou-qjhc.  What it shows is that the crossing HAPPENS, on
real data, for the reason the Lean theorem gives.

THE RESULT (L6a4 class 1, the one class with an exact point):

               u = u_1     u = u_2
      P^c        9/34        0/34
      P^-c       0/34        9/34

Perfectly antisymmetric, and the SAME nine equations fail in the mirrored cells -- the
nine that carry a nontrivial power of u.  The point solves P^c at u_2 and P^-c at
u_1 = u_2^2.  That is eval_negTwist on real data.

A BUG THAT PRODUCED A CONFIDENT WRONG ANSWER, recorded because the guard against it is
the interesting part.  The coordinate file records the cube root of unity it used under
the key "u", alongside the 27 Ptolemy coordinates.  Substituting the whole dict at once
therefore pinned u to the RECORDED root before this script's own u_1/u_2 was applied --
so both columns silently evaluated at the same root, and the table came out

               u = u_1     u = u_2
      P^c        0/34        0/34        <- WRONG
      P^-c       9/34        9/34        <- WRONG

which is not merely wrong but ALGEBRAICALLY IMPOSSIBLE: A*u^2 = B at two distinct cube
roots forces A = 0, and A is not 0.  The impossibility is what exposed it.

The guard in place at the time checked that NO symbol was left unsubstituted.  It passed
-- because the bug was OVER-substitution, not under-substitution.  A guard against a
missing substitution is structurally blind to an extra one.  Both directions are now
asserted: `u` is excluded from the coordinate map, and that exclusion is an assert.

EXACT ARITHMETIC ONLY.  Every quantity is a sympy Rational or a polynomial over Q
reduced modulo the minimal polynomial f.  No floats, no tolerances: an equation either
reduces to the zero polynomial or it does not.
"""
import json
import re
import sys
import warnings

warnings.filterwarnings('ignore')
import sympy as sp

T = sp.Symbol('T')


def load(path):
    """Parse the exact point.  SEPARATES the cube root of unity from the Ptolemy
    coordinates -- the file records BOTH under one dict, and substituting them together
    silently pins u to the recorded root before this script's own u ever gets a chance.
    That bug produced a confident wrong answer here once; see the module docstring."""
    d = json.load(open(path))
    f = sp.sympify(d['field']['min_poly'].replace('t', 'T'))
    coords, recorded_u = {}, None
    for k, v in d['ptolemy'].items():
        val = sp.expand(sp.sympify(re.sub(r'\bt\b', 'T', v)))
        if k == 'u':
            recorded_u = val
        else:
            coords[k] = val
    return d, f, coords, recorded_u


def redmod(expr, f):
    """Reduce a polynomial in T modulo f, exactly.  Coefficients may carry symbols."""
    return sp.expand(sp.rem(sp.expand(expr), f, T))


def cube_roots_of_unity(f):
    """The two primitive cube roots of unity inside K = Q[T]/(f), exactly."""
    a, b, c, d = sp.symbols('a b c d', rational=True)
    u = a + b * T + c * T ** 2 + d * T ** 3
    r = sp.Poly(redmod(u ** 2 + u + 1, f), T)
    sols = sp.solve(r.all_coeffs(), [a, b, c, d], dict=True)
    out = []
    for s in sols:
        if len(s) != 4 or not all(v.is_rational for v in s.values()):
            continue
        cand = sp.expand(u.subs(s))
        if redmod(cand ** 2 + cand + 1, f) != 0 or cand == 1:
            continue
        if any(redmod(cand - w, f) == 0 for w in out):   # sp.solve repeats solutions
            continue
        out.append(cand)
    return out


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'L6a4-c1-ptolemy-in-K.json'
    d, f, coords, recorded_u = load(path)
    name, kcls = d['manifold'], d['obstruction_class']
    print(f"{name} class {kcls}: {len(coords)} exact Ptolemy coordinates in "
          f"K = Q[T]/({d['field']['min_poly']})")
    assert 'u' not in coords, "u must NOT be substituted as a coordinate"
    if recorded_u is not None:
        print(f"  the file also records its own cube root of unity; kept OUT of the "
              f"coordinate substitution")

    us = cube_roots_of_unity(f)
    print(f"\nprimitive cube roots of unity inside K: {len(us)} found")
    if len(us) != 2:
        print("  EXPECTED 2 -- K must contain zeta_3 for this test to mean anything.")
        return 1
    for i, uu in enumerate(us, 1):
        tag = ""
        if recorded_u is not None and redmod(uu - recorded_u, f) == 0:
            tag = "   <- the root the producer used"
        print(f"  u_{i} = {sp.nsimplify(uu)}{tag}")
    assert redmod(us[0] + us[1] + 1, f) == 0, "u_1 + u_2 must be -1"
    assert redmod(us[0] ** 2 - us[1], f) == 0 or redmod(us[1] ** 2 - us[0], f) == 0, \
        "each must be the other's square"
    print("  checked: u_1 + u_2 = -1 and each is the other's square")

    import snappy
    from snappy.ptolemy.ptolemyGeneralizedObstructionClass import (
        PtolemyGeneralizedObstructionClass as OC)
    M = snappy.Manifold(name)
    V = M.ptolemy_variety(3, obstruction_class=kcls, eliminate_fixed_ptolemys=True)
    cvec = list(V._obstruction_class.H2_class)
    negc = [(-x) % 3 for x in cvec]
    Vn = M.ptolemy_variety(3, obstruction_class=OC(negc),
                           eliminate_fixed_ptolemys=True)
    print(f"\ncocycle c = {cvec}   ->   -c = {negc}")

    usym = sp.Symbol('u')
    csym = {k: sp.Symbol(k) for k in coords}

    def polys(variety):
        out = []
        for e in variety.equations_with_non_zero_condition:
            s = str(e).replace('^', '**')
            out.append(sp.sympify(s, locals={**csym, 'u': usym}))
        return out

    sub_map = {sp.Symbol(k): v for k, v in coords.items()}
    assert usym not in sub_map, "u leaked into the coordinate substitution"

    def residuals(ps, uval):
        """Count non-vanishing equations.  GUARDS AGAINST ITS OWN BLIND SPOT: an
        unsubstituted coordinate symbol would make an equation look non-zero for a
        reason that has nothing to do with the mathematics, so it is a hard error."""
        bad = 0
        for p in ps:
            sub = p.subs(sub_map).subs(usym, uval)
            if usym in p.free_symbols and usym not in sub_map:
                pass  # u is supplied separately, below
            leftover = sp.expand(sub).free_symbols - {T}
            if leftover:
                raise SystemExit(
                    f"HARNESS ERROR: {sorted(map(str, leftover))} were never substituted. "
                    f"The coordinate file does not cover this equation set -- fix the "
                    f"variety construction, do not report a residual.")
            if redmod(sp.expand(sub), f) != 0:
                bad += 1
        return bad

    table = {}
    for label, variety in (('P^c', V), ('P^-c', Vn)):
        ps = polys(variety)
        for i, uu in enumerate(us, 1):
            table[(label, i)] = (residuals(ps, uu), len(ps))

    print("\n  non-vanishing equations (0 = the point solves the system):\n")
    print("            u = u_1     u = u_2")
    for label in ('P^c', 'P^-c'):
        a = table[(label, 1)]
        b = table[(label, 2)]
        print(f"  {label:6s}    {a[0]:3d}/{a[1]:<3d}     {b[0]:3d}/{b[1]:<3d}")

    crossed = ((table[('P^c', 1)][0] == 0 and table[('P^-c', 2)][0] == 0
                and table[('P^c', 2)][0] != 0 and table[('P^-c', 1)][0] != 0) or
               (table[('P^c', 2)][0] == 0 and table[('P^-c', 1)][0] == 0
                and table[('P^c', 1)][0] != 0 and table[('P^-c', 2)][0] != 0))
    solves_c = table[('P^c', 1)][0] == 0 or table[('P^c', 2)][0] == 0

    print()
    if not solves_c:
        print("INCONCLUSIVE -- the recorded point does not solve P^c at either cube root,")
        print("so this file cannot test the crossing.  Check the point, not the theorem.")
        return 1
    if crossed:
        print("CROSSING CONFIRMED -- the same exact point solves P^c at one primitive cube")
        print("root of unity and P^-c at the other.  This is eval_negTwist on real data:")
        print("swapping u for u^2 IS negating the obstruction cocycle.")
        return 0
    print("CROSSING NOT OBSERVED -- the point solves P^c but not P^-c at the other root.")
    print("That would contradict the equation-level measurement; investigate before")
    print("trusting either.")
    return 1


if __name__ == '__main__':
    sys.exit(main())
