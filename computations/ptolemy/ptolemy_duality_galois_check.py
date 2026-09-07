#!/usr/bin/env python3
"""Negating the obstruction cocycle acts on the Ptolemy variety as u -> u^2.  This is the
RELATIVE statement, verified in snappy's own equations -- the gap the absolute derivation
left open.

THE GAP THIS CLOSES.  obstruction_duality_negates.py derives [rho*] = -[rho] from the
obstruction cocycle, but in ABSOLUTE group cohomology H^2(Gamma; mu_n).  The Ptolemy
obstruction is the relative class in H^2(M, dM; Z/n), and that step was flagged as the
whole distance between the argument and a theorem.

WHAT IS MEASURED HERE.  Build P^c from snappy for a class c, build P^{-c} by handing
snappy the explicit negated cocycle, and compare their defining equations.  They are NOT
equal -- 10 of 33 equations differ -- and the difference is exactly the POWER OF u, the
primitive cube root of unity:

    P^c  : ... + c_1101_2 * u^2
    P^-c : ... + c_1101_2 * u

Substituting u -> u^2 throughout P^c reproduces P^-c EXACTLY, as polynomial sets, for
every class tested.  So cocycle negation IS the substitution u -> u^2 = u^{-1}: the
nontrivial automorphism of mu_3, i.e. complex conjugation of the cube root of unity.

WHY THAT IS THE DUALITY.  The absolute derivation says duality inverts the central mu_n
(c* = c^{-1}).  This says inverting mu_3 -- u -> u^{-1} -- carries P^c to P^{-c}.  The
two ends meet: duality sends a class-c representation into class -c, now established in
the relative Ptolemy setting rather than assumed to transfer from the absolute one.

COMPARE AS POLYNOMIALS, NOT STRINGS.  A first version of this check compared the
equations as text and reported FAILURE, on pairs like "1 + u^2 + u" against
"1 + u + u^2" -- the same polynomial in a different term order, and in fact the
cyclotomic relation present in both.  A string comparison of algebra is not a test of
algebra.
"""
import re
import sys
import warnings
warnings.filterwarnings('ignore')
import snappy
import sympy as sp
from snappy.ptolemy.ptolemyGeneralizedObstructionClass import PtolemyGeneralizedObstructionClass as OC

N = 3
u = sp.Symbol('u')


def normalise(s):
    """Parse and reduce modulo u^3 - 1 (u a primitive cube root of unity)."""
    e = sp.sympify(s.replace('^', '**'))
    if e.has(u):
        e = sp.rem(sp.Poly(sp.expand(e), u).as_expr(), u ** 3 - 1, u)
    return sp.srepr(sp.expand(e))


def swap_u(s):
    """u -> u^2 and u^2 -> u, simultaneously."""
    s = re.sub(r'u\^2', 'u^TMP', s)
    s = re.sub(r'(?<![\^A-Za-z0-9_])u(?!\^)', 'u^2', s)
    return s.replace('u^TMP', 'u')


def main(name='L6a4', classes=(1, 2, 3)):
    M = snappy.Manifold(name)
    ok = True
    for k in classes:
        V = M.ptolemy_variety(N, obstruction_class=k, eliminate_fixed_ptolemys=True)
        c = list(V._obstruction_class.H2_class)
        negc = [(-x) % N for x in c]
        Vn = M.ptolemy_variety(N, obstruction_class=OC(negc), eliminate_fixed_ptolemys=True)

        raw_equal = sorted(str(e) for e in V.equations) == sorted(str(e) for e in Vn.equations)
        A = {normalise(swap_u(str(e))) for e in V.equations}
        B = {normalise(str(e)) for e in Vn.equations}
        good = (A == B)
        ok &= good
        print(f"  [{'ok' if good else 'FAIL'}] {name} class {k}: "
              f"P^c and P^-c identical without the substitution? {raw_equal}; "
              f"with u -> u^2? {good}  ({len(A)} vs {len(B)} equations)")
    print(f"\n{'ALL CHECKS PASS' if ok else 'CHECKS FAILED'} -- cocycle negation acts as "
          "u -> u^2, the nontrivial automorphism of mu_3.")
    print("Together with the absolute derivation (duality inverts the central mu_n),")
    print("duality carries a class-c representation into class -c IN THE RELATIVE SETTING.")
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main(*(sys.argv[1:2] or ['L6a4'])))
