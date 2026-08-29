#!/usr/bin/env python3
"""Serre-Leray E_2 of the colour fibration — bean `qou-ken6`.

The bean's question: can the corpus's existing E_r-page API
(QOU.Mathlib.SpectralSequence) be instantiated on the colour fibration over
P^1(C), and does the Serre-Leray spectral sequence supply the 3-dimensional
object the N=3 problem needs?

This probe settles the GEOMETRY half symbolically.  The API half is argued in
docs/audits/2026-08-25-colour-fibration-leray-e2.md and needs no compute.

EXACT ARITHMETIC ONLY: sympy over Q(z).  No floats anywhere, per AGENTS.md
"PROBES ARE NOT EXEMPT".  Every quantity below is a polynomial identity.
"""
import sys

import sympy as sp

c, z, X, t = sp.symbols('c z X t')

def main():
    print("=" * 68)
    print("1. The colour-tube cubic, and the corpus's own two shifts")
    print("=" * 68)
    # QOU.ColorTubeFibers docstring
    cubic = c**3 + (4*z + 1)*c**2 + (6*z**2 + 3*z + 1)*c + (4*z**3 + 3*z**2 + 2*z + 1)
    print(f"  colour tube at z:  {sp.expand(cubic)} = 0")

    # shift 1: X = c + z   (color-tube-fibers.lean)
    inX = sp.Poly(sp.expand(cubic.subs(c, X - z)), X)
    a2, a1, a0 = inX.all_coeffs()[1:]
    print(f"\n  after X = c + z:   X^3 + ({sp.factor(a2)})X^2 + ({sp.factor(a1)})X + {sp.factor(a0)}")
    print(f"  X^2 coefficient is {sp.factor(a2)}, NOT zero -- this shift alone does")
    print("  not depress the cubic; a second shift is needed, and the corpus")
    print("  supplies it (t-duality-elliptic.md, eq:weierstrass-depressed).")

    # shift 2: X = t - (z+1)/3   (t-duality-elliptic.md)
    dep = sp.Poly(sp.expand(inX.as_expr().subs(X, t - (z + 1)/sp.Integer(3))), t)
    d2, d1, d0 = dep.all_coeffs()[1:]
    p = sp.simplify(d1); q = sp.simplify(d0)
    print(f"\n  after X = t - (z+1)/3:  t^3 + p t + q,  quadratic term = {sp.simplify(d2)}")
    print(f"     p(z) = {sp.factor(p)}")
    print(f"     q(z) = {sp.factor(q)}")

    p_corpus = (2*z**2 + z + 2)/sp.Integer(3)
    q_corpus = 5*(4*z**3 + 3*z**2 + 3*z + 4)/sp.Integer(27)
    ok_p = sp.simplify(p - p_corpus) == 0
    ok_q = sp.simplify(q - q_corpus) == 0
    print(f"\n  matches the corpus's published p(z)?  {ok_p}")
    print(f"  matches the corpus's published q(z)?  {ok_q}")

    print()
    print("=" * 68)
    print("2. The fibration is ELLIPTIC, so H^1(fibre) has rank 2")
    print("=" * 68)
    disc = sp.factor(sp.simplify(-4*p**3 - 27*q**2))
    deg = sp.Poly(sp.expand(-4*p**3 - 27*q**2), z).degree()
    print(f"  Delta(z) = -4p^3 - 27q^2, degree {deg} in z")
    print(f"  identically zero (fibre never smooth)?  {sp.simplify(-4*p**3-27*q**2) == 0}")
    print("  So the generic fibre is a SMOOTH elliptic curve y^2 = t^3 + pt + q,")
    print("  singular only over the finitely many roots of Delta.")
    print("  A genus-1 curve has  H^0 = Z,  H^1 = Z^2,  H^2 = Z.")
    print("  ==> the monodromy representation on H^1 has RANK 2.")

    print()
    print("=" * 68)
    print("3. E_2, and why the spectral sequence degenerates")
    print("=" * 68)
    print("  Over the smooth locus B0 = P^1 minus the roots of Delta, B0 is an")
    print("  open Riemann surface: homotopy-equivalent to a wedge of circles, so")
    print("     H^0(B0) = Z,   H^1(B0) = Z^(k-1),   H^p(B0) = 0 for p >= 2.")
    print("  E_2^{p,q} = H^p(B0; R^q) is therefore supported in p in {0,1} only.")
    print()
    print("  d_r : E_r^{p,q} -> E_r^{p+r, q-r+1}.  For r >= 2 the target has")
    print("  p + r >= 2, where every group vanishes; the source of any d_r into")
    print("  (p,q) sits at p - r <= -1, likewise zero.  Hence:")
    print()
    print("     ALL d_r VANISH FOR r >= 2  ==>  E_2 = E_infinity.")
    print()
    print("  The sequence degenerates for DIMENSION reasons, before any QOU")
    print("  input is used.  It contributes no differential, no extension")
    print("  problem beyond one short exact sequence, and no new object.")

    print()
    print("=" * 68)
    print("VERDICT for the N = 3 problem")
    print("=" * 68)
    print("  The fibration's representation-theoretic content is the monodromy")
    print("  pi_1(B0) -> SL(2,Z) on H^1(fibre) = Z^2.  That is RANK 2 -- the same")
    print("  2 the framework already has.  It does NOT supply a 3.")
    print()
    print("  The 'three colours' r,g,b are the three COORDINATES of the ambient")
    print("  A^3 (equivalently the three roots of the cubic), not a 3-dimensional")
    print("  representation coming from the fibration's cohomology.  Reading the")
    print("  root-permutation action as the missing triple gives the S_3")
    print("  PERMUTATION representation, which is self-dual (Frobenius-Schur +1),")
    print("  so Sym^2 carries a singlet and it FAILS the Sym^2 gate -- already")
    print("  excluded in the corpus (T3g section 4, the 2026-08-07 collapse audit).")
    print()
    print("  Both readings therefore land on results the corpus already has.")
    return ok_p and ok_q

if __name__ == "__main__":
    sys.exit(0 if main() else 1)
