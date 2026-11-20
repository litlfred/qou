#!/usr/bin/env python3
"""
w1_dilation_no_lift_to_sigma_probe.py — bean qou-lmnq (follows qou-7fnr / #6738).

QUESTION. W1 (`qou-d8de`: construct the q-difference prolongation D_q from the colour
spectral curve Sigma) names as its first route a q-shift on the BASE, z -> q^2 z. Two
prior tranches excluded that route by the COEFFICIENT FIELD:

  * #6695 (qou-1z28): no rational q-connection on the z-line has the colour sheets as
    flat sections (the cubic is irreducible over K(z), each sheet is D-finite, and
    D-finite AND q-holonomic => rational, Bezivin / Ramis / Schaefke-Singer).
  * #6738 (qou-7fnr): the same exclusion survives passage to the ramified local chart
    t, where z = z_c + t^2.

#6738 closed by naming what those leave open: "coefficients not rational in a
coordinate, or an operator on Sigma". This probe settles the second alternative, and
it needs no rationality theorem at all.

THE ARGUMENT (scope-(b); the invariant is the branch sextic's own coefficients).
An automorphism sigma : Sigma -> Sigma covering the base dilation z -> lambda z is an
isomorphism of coverings up to the base automorphism, so it carries ramification points
to ramification points and therefore permutes the finite branch locus
B = { z : D(z) = 0 }, D = -disc_X P the branch sextic. D is squarefree and D(0) != 0
(both checked below), so "lambda . B = B" says exactly that D(lambda z) and D(z) have
the same root multiset, i.e.

    D(lambda z) = c . D(z)   for some constant c.

Comparing the CONSTANT term gives 16 = 16c, so c = 1; the LINEAR term then gives
24 lambda = 24, so lambda = 1. Hence the ONLY dilation admitting a lift to Sigma is the
identity — for every lambda, root of unity or not, at every q.

Lean: QOU.Mass.DilationBranchLocusRigidity.dilation_scaling_rigid (sorry-free, generic
char-0 field; characteristic zero is used only to invert 16 and 24).

WHAT IS CITED, NOT RE-DERIVED. The complementary half — Sigma -> P^1 has full S_3
covering monodromy, hence no single-valued algebraic branch, hence D_q "cannot be a
single-valued algebraic operator on the base; it lives on the 3-sheeted cover" — is
already held in `computations/qbeta/c3_w1_cover_monodromy.py`. Section 4 re-runs its two
premises as an independent confirmation and attributes the conclusion there; it does not
claim them as new. The composition is the point: that probe pushes D_q onto Sigma, and
this one says the dilation cannot follow it there.

SECTIONS
  1  D = -disc_X P; squarefree; D(0) = 16 != 0; six distinct finite branch points.
  2  The rigidity solve: D(lambda z) = c D(z) has the unique solution (lambda, c) = (1,1),
     and the weaker product-of-roots bound lambda^6 = 1 that would follow from
     lambda . B = B alone (recorded because it is the argument that survives if the low
     -order coefficients ever change).
  3  CONTROL: the same solve run on z^6 - 1, which IS scaling-invariant, correctly
     returns the six sixth-roots of unity. So the null result in section 2 is a property
     of D, not of the method.
  4  The S_3 premises, reproduced and attributed (irreducible; disc not a square).
  5  The substrate value lambda = q0^2 at the canonical proton pin: lambda != 1 and
     lambda^6 != 1, so neither the strong nor the weak bound admits it.

All exact (sympy over Q) except the substrate read-out, which is mpmath at the package
precision. No float64; no witness by design (a probe). Anti-fit: nothing is tuned, and
no number here is compared to an anchor.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import sympy as sp  # noqa: E402

X, z, lam, c = sp.symbols('X z lamda c')

P = X**3 + (z + 1) * X**2 + (z**2 + z + 1) * X + (z**3 + z**2 + z + 1)

HR = '=' * 78


def branch_sextic():
    """D(z) = -disc_X P — the corpus's `branchSextic` (ColorSpectralCubicGeometry)."""
    return sp.expand(-sp.discriminant(P, X))


def scaling_solutions(poly, var, deg):
    """All (lambda, c) with poly(lambda*var) = c*poly(var), as an exact solve over the
    coefficient system. Returns the solution list."""
    lhs = sp.Poly(sp.expand(poly.subs(var, lam * var)), var).all_coeffs()
    rhs = sp.Poly(sp.expand(c * poly), var).all_coeffs()
    eqs = [sp.expand(a - b) for a, b in zip(lhs, rhs)]
    return eqs, sp.solve(eqs, [lam, c], dict=True)


# ----------------------------------------------------------------------------
# §1  the branch locus
# ----------------------------------------------------------------------------
def section1():
    print(HR)
    print('§1  the branch locus of Sigma')
    print(HR)
    D = branch_sextic()
    coeffs = sp.Poly(D, z).all_coeffs()
    print(f'  D(z) = -disc_X P, coefficients (z^6..z^0): {coeffs}')
    matches_corpus = coeffs == [16, 24, 35, 50, 35, 24, 16]
    print(f'  matches ColorSpectralCubicGeometry.branchSextic: {matches_corpus}')
    sqfree = sp.simplify(sp.gcd(D, sp.diff(D, z))) == 1
    d0 = D.subs(z, 0)
    deg = sp.Poly(D, z).degree()
    print(f'  squarefree (gcd(D, D\') = 1): {sqfree}    D(0) = {d0}    deg D = {deg}')
    # product of the six roots = constant/leading (degree even, so no sign flip)
    prod_roots = sp.Rational(coeffs[-1], coeffs[0])
    print(f'  product of the six roots = {prod_roots}  (constant/leading)')
    palindromic = coeffs == coeffs[::-1]
    print(f'  palindromic (branchSextic_palindromic, z -> 1/z stable): {palindromic}')
    ok = bool(matches_corpus and sqfree and d0 != 0 and deg == 6 and prod_roots == 1)
    print(f'  §1 VERDICT six distinct finite branch points, none at z = 0: {ok}')
    return D, ok


# ----------------------------------------------------------------------------
# §2  scaling rigidity
# ----------------------------------------------------------------------------
def section2(D):
    print(HR)
    print('§2  D(lambda z) = c D(z): the rigidity solve')
    print(HR)
    eqs, sols = scaling_solutions(D, z, 6)
    print('  coefficient system (z^6 down to z^0):')
    for i, e in enumerate(eqs):
        print(f'     z^{6-i}: {sp.factor(e)}')
    print(f'  exact solutions over Qbar: {sols}')
    only_trivial = sols == [{lam: 1, c: 1}]
    print(f'  the ONLY solution is (lambda, c) = (1, 1): {only_trivial}')
    print('  reading: the constant term forces c = 1 (16 = 16c), and the linear term')
    print('           then forces lambda = 1 (24 lambda = 24).')
    # the weaker bound that lambda.B = B alone would give
    print('  weaker fallback bound, from the product of roots alone:')
    print('     lambda . B = B  =>  prod(lambda z_c) = prod(z_c)  =>  lambda^6 . 1 = 1')
    print('     so even without the low-order coefficients, lambda would be a 6th root')
    print('     of unity. Recorded because it survives if those coefficients change.')
    ok = bool(only_trivial)
    print(f'  §2 VERDICT no nontrivial dilation preserves the branch locus: {ok}')
    return ok


# ----------------------------------------------------------------------------
# §3  control — a sextic that IS scaling-invariant
# ----------------------------------------------------------------------------
def section3():
    print(HR)
    print('§3  CONTROL: the same solve on z^6 - 1, which IS scaling-invariant')
    print(HR)
    E = z**6 - 1
    eqs, sols = scaling_solutions(E, z, 6)
    lams = sorted({sp.simplify(s[lam]) for s in sols}, key=lambda t: (sp.re(t), sp.im(t)))
    print(f'  coefficient system: {[sp.factor(e) for e in eqs]}')
    print(f'  solutions: {len(sols)} — lambda ranges over {lams}')
    all_sixth = all(sp.simplify(s[lam]**6 - 1) == 0 for s in sols) and len(sols) == 6
    print(f'  all six are sixth roots of unity, and there are six of them: {all_sixth}')
    print('  So the method CAN return a nontrivial answer; §2 returning only (1,1) is a')
    print('  property of the branch sextic (its nonzero constant AND linear terms), not')
    print('  of the searcher.')
    print(f'  §3 VERDICT control passes: {all_sixth}')
    return all_sixth


# ----------------------------------------------------------------------------
# §4  the S_3 premises — reproduced, attributed to c3_w1_cover_monodromy.py
# ----------------------------------------------------------------------------
def section4(D):
    print(HR)
    print('§4  the S_3 half — REPRODUCED, NOT NEW (computations/qbeta/c3_w1_cover_monodromy.py)')
    print(HR)
    irreducible = bool(sp.Poly(P, X).is_irreducible)
    _, factors = sp.factor_list(-D)          # -D = disc_X P
    disc_is_square = bool(factors) and all(m % 2 == 0 for _, m in factors)
    monodromy = 'S3' if (irreducible and not disc_is_square) else ('A3' if irreducible else 'reducible')
    print(f'  cubic irreducible over Q(z): {irreducible}')
    print(f'  disc_X P a square in C(z): {disc_is_square}  (squarefree of positive degree cannot be)')
    print(f'  => covering monodromy: {monodromy}')
    print('  That conclusion is the cited probe\'s, not this one\'s. Its consequence —')
    print('  "D_q cannot be a single-valued algebraic operator on the base; it lives on')
    print('  the 3-sheeted cover" — is what makes §2 load-bearing: the dilation cannot')
    print('  follow D_q onto that cover.')
    ok = monodromy == 'S3'
    print(f'  §4 VERDICT premises reproduce: {ok}')
    return ok


# ----------------------------------------------------------------------------
# §5  the substrate value
# ----------------------------------------------------------------------------
def section5():
    print(HR)
    print('§5  the substrate dilation lambda = q0^2 (canonical PROTON pin)')
    print(HR)
    import mpmath as mp
    from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP
    mp.mp.dps = 60
    q0 = Q_MP
    lam_val = q0**2
    print(f'  q0 (proton pin, 50-digit)  = {mp.nstr(q0, 25)}')
    print(f'  lambda = q0^2              = {mp.nstr(lam_val, 25)}')
    ne1 = abs(lam_val - 1) > mp.mpf(10) ** (-40)
    ne_root = abs(lam_val**6 - 1) > mp.mpf(10) ** (-40)
    print(f'  lambda != 1: {ne1}    lambda^6 != 1: {ne_root}')
    print('  lambda is real and > 1, so it is not a root of unity of any order; both the')
    print('  strong bound (lambda = 1) and the weak one (lambda^6 = 1) exclude it.')
    ok = bool(ne1 and ne_root)
    print(f'  §5 VERDICT the substrate dilation is excluded: {ok}')
    return ok


def main():
    D, ok1 = section1()
    ok2 = section2(D)
    ok3 = section3()
    ok4 = section4(D)
    ok5 = section5()
    print(HR)
    print('CONCLUSION')
    print(HR)
    print('  * The branch sextic is scaling-rigid: D(lambda z) = c D(z) only for')
    print('    (lambda, c) = (1, 1). Lean: QOU.Mass.DilationBranchLocusRigidity, sorry-free.')
    print('  * An automorphism of Sigma covering z -> lambda z would permute the branch')
    print('    locus and so force that identity. Hence NO nontrivial base dilation lifts')
    print('    to Sigma — scope (b), the invariant being the sextic\'s own coefficients.')
    print('  * This is complementary to Bezivin-Ramis rather than dependent on it: it')
    print('    constrains no coefficient field, and it holds for lambda a root of unity')
    print('    too, which is exactly the case that theorem does not cover.')
    print('  * Combined with the held S_3 result, the dilation route is now closed in')
    print('    all three places it could have lived: the base coordinate (#6695), the')
    print('    ramified local coordinate (#6738), and Sigma itself (here).')
    print('  * NOT excluded: a q-difference operator whose base map is not a dilation,')
    print('    and route 2 (root-of-unity FIBRE monodromy), which acts on the fibre and')
    print('    is untouched by any statement about maps of the z-line. D_q is NOT')
    print('    constructed.')
    allok = ok1 and ok2 and ok3 and ok4 and ok5
    print(f'  ALL CHECKS PASS: {allok}')
    return 0 if allok else 1


if __name__ == '__main__':
    raise SystemExit(main())
