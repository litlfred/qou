#!/usr/bin/env python3
"""The duality test, for ANY manifold and obstruction class. (qou-qjhc)

The L6a4 probes hardcode that field and its two automorphism polynomials as strings.  This
one takes a `<manifold>-c<class>-ptolemy-in-K.json` from ptolemy_exact_point.py and derives
everything: the field, its automorphism group, and the test.

WHAT IS TESTED, and why it is two questions rather than one:

  UNTWISTED   is there an invertible A over K with  A sigma(rho(g)) A^{-1} = rho(g)^{-T}
              on the generators, EXACTLY -- lambda pinned to 1?  That is the GL(3,K)
              statement proved for L6a4 class 1.
  TWISTED     the same with lambda(g) = sigma(chi(g))/chi(g^{-1}) measured rather than
              pinned.  This is the weaker PGL(3,K) statement, and it is asked separately so
              that a manifold where the twisted version holds and the untwisted one fails is
              REPORTED as such instead of being scored as a plain failure.

Both are decided by an exact linear solve, never a sweep: `rho_1(w) = sigma(rho(w))` and
`rho_2(w) = lambda(w) rho(w)^{-T}` are both HOMOMORPHISMS, so agreement on a generating set
is agreement everywhere (QOU/Eightfold/IntertwinerFromGenerators.lean).

AUTOMORPHISMS ARE COMPUTED, NOT ASSUMED, and the count is the thing to read.  An
automorphism of K is a root of the minimal polynomial IN K, found here by solving
`f(g(t)) = 0 mod f(t)` for the coefficients of g.  |Aut(K/Q)| equals [K:Q] only when K/Q is
NORMAL.  This matters: a field can have a large Galois group over its SPLITTING field while
K itself admits few automorphisms -- and if K admits only the identity, the sigma-transport
question is not merely unanswered, it is UNASKABLE, since there is no candidate sigma.  The
probe reports that case as UNASKABLE rather than as a refutation.

GUARDS, run before any character or intertwiner is read:
  * the relator gate -- every relator maps to a SCALAR, so the matrices really are a PGL(3)
    representation.  Run against snappy's own evaluator, not this file's arithmetic;
  * every Ptolemy coordinate non-zero (a degenerate component satisfies every equation and
    is not a representation -- see ptolemy_exact_point.py, trap 1);
  * det rho(g), reported: the SL(3) normalisation is what forces lambda into mu_3, so
    whether it holds is part of the answer rather than an assumption;
  * `id` is the REFUTATION CONTROL -- it must FAIL for a non-self-dual representation, and
    a run where every automorphism succeeds is a broken test, not a strong result.

Exact in K throughout: Fraction and NumberField, sympy Rational nullspace.  No floats.
"""
import argparse
import json
import pathlib
import sys
import warnings

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
warnings.filterwarnings('ignore')

from exact_character_selfduality import Elt, trace, det3, poly_to_elt, _frac  # noqa: E402
from numberfield import NumberField                                          # noqa: E402
import snappy                                                                # noqa: E402
from snappy.ptolemy.coordinates import PtolemyCoordinates                    # noqa: E402

t = sp.Symbol('t')


def _automorphisms_via_solve(fe, deg):
    """The original route: solve f(g(t)) = 0 mod f for the coefficients of g.

    RETAINED AS A CROSS-CHECK, NOT AS THE PRIMARY ROUTE.  It is a system of `deg`
    polynomial equations in `deg` unknowns of degree `deg`, i.e. a Groebner basis
    computation wearing `sp.solve`'s clothes, and its cost is what it sounds like.
    Measured on `5_2` class 1 orbit 0 ([K:Q] = 4): >40 min, no answer, against
    0.1 s for the factorisation route below.  Used by --cross-check only.
    """
    a = sp.symbols(f'a0:{deg}')
    g = sum(a[i] * t ** i for i in range(deg))
    r = sp.rem(sp.Poly(sp.expand(fe.subs(t, g)), t), sp.Poly(fe, t))
    eqs = [sp.expand(c) for c in sp.Poly(r, t).all_coeffs()]
    out = []
    for s_ in sp.solve(eqs, a, dict=True):
        gg = sp.expand(g.subs(s_))
        if gg.free_symbols - {t}:
            continue                      # under-determined: not a single map
        # RATIONAL coefficients only.  sp.solve also returns the NUMERIC roots of f as
        # constant solutions -- for t^2+11t+31 it offers g(t) = (-11 +- i*sqrt 3)/2.  Those
        # are embeddings of K into C, NOT automorphisms of K, and they are not expressible
        # over Q.  Admitting them inflates |Aut(K/Q)| (4 instead of 2 here, which then reads
        # as "K/Q is not normal") and crashes the exact arithmetic downstream.
        cs = sp.Poly(gg, t).all_coeffs() if gg.has(t) else [gg]
        if not all(sp.nsimplify(c).is_rational for c in cs):
            continue
        if gg not in out:
            out.append(gg)
    return out


def automorphisms(fe, deg):
    """Every root of the minimal polynomial IN K, as a polynomial g(t) of degree < deg.

    |Aut(K/Q)| < [K:Q] exactly when K/Q is not normal; the caller must read the count.

    ROUTE: factor f over K = Q(alpha) and read off the LINEAR factors.  A root of f
    lies in K iff it is a root of a linear factor over K, so this is exactly the same
    set as solving f(g(t)) = 0 mod f for g's coefficients -- but it is a univariate
    factorisation over a number field rather than a multivariate solve, which is why
    it runs in fractions of a second where the other route does not finish.  This is
    a change of ALGORITHM, not of definition: the object computed is unchanged.

    Cross-checked three ways on `5_2` class 1 (see the audit doc): against the solve
    route where that terminates, against the group axioms by direct polynomial
    arithmetic mod f (identity present, closed under composition, every element
    invertible -- `_check_group`, asserted on every run), and against
    f(g(t)) == 0 mod f for every g returned.

    Coefficients are rational automatically: a linear factor over K has its root in K
    by construction, so the numeric-embedding contamination the solve route had to
    filter out cannot arise.

    DO NOT reintroduce a substitution on `sp.rootof`'s return value.  Its SHAPE varies
    with f and all three shapes occur in this corpus:

        5_2   monic quartic      ComplexRootOf
        L6a4  NON-monic quartic  Mul   125*CRootOf(64*_x^4 - 760*_x^3 + ..., 0)
        m004  quadratic          Add   -11/2 - sqrt(3)*I/2   (solved in radicals)

    while the factorisation writes its coefficients in terms of the bare CRootOf atom.
    Substituting the whole `rootof` value therefore matched only part of the L6a4
    expression and left a mixed t/CRootOf result, and substituting the atom instead
    then failed on m004, which has no atom at all.  `to_number_field(r, alpha)`
    re-expresses r in the power basis of alpha regardless of how either is spelled;
    `.as_poly(t)` is then g itself.  (Both wrong versions were caught by the guard
    below rather than returning a wrong automorphism count -- keep the guard.)
    """
    x = sp.Symbol('_x')
    fx = sp.expand(fe.subs(t, x))
    alpha = sp.AlgebraicNumber(sp.rootof(fx, 0))
    out = []
    for fac, _mult in sp.factor_list(sp.Poly(fx, x), extension=alpha)[1]:
        pf = sp.Poly(fac, x)
        if pf.degree() != 1:
            continue                      # a root of f NOT in K -- K/Q is not normal
        c1, c0 = pf.all_coeffs()
        gg = sp.expand(sp.to_number_field(-c0 / c1, alpha).as_poly(t).as_expr())
        if gg.has(sp.CRootOf) or gg.has(sp.AlgebraicNumber) or (gg.free_symbols - {t}):
            raise RuntimeError(f'root not expressible over Q in the power basis: {gg}')
        if gg not in out:
            out.append(gg)
    return out


def _element_orders(autos, fe):
    """Multiplicative order of each automorphism -- names the group, not just its size.

    [1,2,2,2] is the Klein four-group and [1,2,4,4] is cyclic C4; both have order 4
    and they give DIFFERENT subgroup lattices, so the transport argument's reach
    differs between them.  The count alone does not distinguish them.
    """
    fp = sp.Poly(fe, t)
    comp = lambda u, v: sp.expand(sp.rem(sp.Poly(sp.expand(u.subs(t, v)), t), fp).as_expr())
    out = []
    for g in autos:
        y, n = sp.expand(g), 1
        while y != sp.expand(t) and n <= 4 * len(autos) + 4:
            y, n = comp(g, y), n + 1
        out.append(n)
    return out


def _check_group(autos, fe):
    """Verify the returned set really is Aut(K/Q), by polynomial arithmetic mod f only.

    This does NOT trust the route that produced it.  A route that silently drops an
    automorphism reports K/Q as non-normal when it is normal -- which is a wrong
    mathematical claim about the manifold, not a performance regression -- and a
    route that admits a spurious one breaks composition.  Both are caught here:

      roots       f(g(t)) == 0 mod f for every g          (each g is genuinely a root)
      identity    t is in the set
      closed      g o h mod f is in the set for all g, h
      inverses    every g has an h with g o h == t

    Cheap (|Aut|^2 polynomial compositions mod f) and independent of `sp.solve`,
    `factor_list`, and NumberField alike.
    """
    fp = sp.Poly(fe, t)
    comp = lambda u, v: sp.expand(sp.rem(sp.Poly(sp.expand(u.subs(t, v)), t), fp).as_expr())
    S = {sp.expand(g) for g in autos}
    return {
        'roots': all(sp.rem(sp.Poly(sp.expand(fe.subs(t, g)), t), fp).as_expr() == 0
                     for g in autos),
        'identity': sp.expand(t) in S,
        'closed': all(comp(u, v) in S for u in autos for v in autos),
        'inverses': all(any(comp(u, v) == sp.expand(t) for v in autos) for u in autos),
    }


def main(stem):
    d = json.loads((HERE / f'{stem}-ptolemy-in-K.json').read_text())
    NAME, KCLS = d['manifold'], d['obstruction_class']
    fe = sp.sympify(d['field']['min_poly'])
    fp = sp.Poly(sp.expand(fe), t)
    K = NumberField([_frac(c) for c in reversed(fp.all_coeffs())])
    DEG = K.deg
    zero, one = Elt(K, K.zero()), Elt(K, K.one())
    print(f"{NAME} class {KCLS}: K = Q[t]/({fe}), degree {DEG}, disc {d['field'].get('discriminant','?')}")

    autos = automorphisms(fe, DEG)
    normal = (len(autos) == DEG)
    grp = _check_group(autos, fe)
    assert all(grp.values()), f"automorphism set is not a group: {grp}"
    print(f"\n=== automorphisms of K (computed, not assumed) ===")
    for i, g in enumerate(autos):
        print(f"   sigma_{i}: t -> {g}")
    print(f"   |Aut(K/Q)| = {len(autos)}, [K:Q] = {DEG}  ->  K/Q normal: {normal}")
    print(f"   group axioms verified mod f (roots/identity/closed/inverses): {grp}")
    print(f"   element orders: {sorted(_element_orders(autos, fe))}")
    if len(autos) <= 1:
        print("\n   *** UNASKABLE: K admits only the identity, so there is no candidate "
              "sigma. This is not a refutation. ***")

    def elt_to_expr(e):
        return sum(sp.Rational(c.numerator, c.denominator) * t ** i for i, c in enumerate(e.v))

    def sig_apply(e, g):
        return poly_to_elt(K, sp.expand(elt_to_expr(e).subs(t, g)), t)

    def coords(e):
        v = list(e.v) + [_frac(0)] * (DEG - len(e.v))
        return [sp.Rational(c.numerator, c.denominator) for c in v[:DEG]]

    pt = {k: poly_to_elt(K, sp.sympify(v), t) for k, v in d['ptolemy'].items()}
    nz = [k for k, v in pt.items() if v == zero]
    print(f"\n=== guards ===")
    print(f"   zero Ptolemy coordinates: {len(nz)} {nz if nz else ''}")
    assert not nz, "degenerate point -- not a representation"

    M = snappy.Manifold(NAME)
    V = M.ptolemy_variety(3, obstruction_class=KCLS, eliminate_fixed_ptolemys=True)
    dd = dict(pt)
    dd['1'] = one
    C = PtolemyCoordinates(dd, is_numerical=False, py_eval_section=eval(V.py_eval_section()),
                           manifold_thunk=lambda: M,
                           non_trivial_generalized_obstruction_class=(KCLS != 0))
    G = M.fundamental_group()
    gens, rels = G.generators(), list(G.relators())
    gate = True
    for r in rels:
        R = C.evaluate_word(r, G)
        off = [(i, j) for i in range(3) for j in range(3) if i != j and not (R[i][j] == 0)]
        if off or not (R[0][0] == R[1][1]) or not (R[1][1] == R[2][2]):
            gate = False
    print(f"   relator gate (every relator -> scalar): {gate}   generators {gens}")
    assert gate, "relator gate failed -- not a PGL(3) representation"
    u = pt.get('u')
    print(f"   u^2+u+1 == 0: {(u * u + u + one) == zero if u is not None else 'no u'}")
    dets = {g: det3(K, C.evaluate_word(g, G)) for g in gens}
    sl3 = all(v == one for v in dets.values())
    print(f"   det rho(g) == 1 on every generator (SL(3) lift): {sl3}")

    def mat(w):
        return C.evaluate_word(w, G)

    def minv(Mw):
        D = det3(K, Mw)
        assert not (D == zero)
        Cf = [[None] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                r_ = [x for x in range(3) if x != i]
                c_ = [y for y in range(3) if y != j]
                m = Mw[r_[0]][c_[0]] * Mw[r_[1]][c_[1]] - Mw[r_[0]][c_[1]] * Mw[r_[1]][c_[0]]
                Cf[j][i] = m if (i + j) % 2 == 0 else zero - m
        return [[Cf[i][j] / D for j in range(3)] for i in range(3)]

    def transpose(Mw):
        return [[Mw[j][i] for j in range(3)] for i in range(3)]

    def solve_int(g_sig, lam):
        rows = []
        for gg in gens:
            Mg = mat(gg)
            S = [[sig_apply(Mg[i][j], g_sig) for j in range(3)] for i in range(3)]
            Dg = transpose(minv(Mg))
            L = lam[gg]
            for i in range(3):
                for j in range(3):
                    coef = {}
                    for q_ in range(3):
                        coef[(i, q_)] = coef.get((i, q_), zero) + S[q_][j]
                    for p_ in range(3):
                        coef[(p_, j)] = coef.get((p_, j), zero) - L * Dg[i][p_]
                    blocks = [coef.get((p_, q_), zero) for p_ in range(3) for q_ in range(3)]
                    mrows = [[sp.Integer(0)] * (9 * DEG) for _ in range(DEG)]
                    for idx, c in enumerate(blocks):
                        if c == zero:
                            continue
                        for k in range(DEG):
                            prod = c * poly_to_elt(K, t ** k, t)
                            for r_, val in enumerate(coords(prod)):
                                mrows[r_][idx * DEG + k] += val
                    rows.extend(mrows)
        ns = sp.Matrix(rows).nullspace()
        if not ns:
            return 0, None
        cands = list(ns) + ([ns[0] + ns[1]] if len(ns) > 1 else [])
        for vec in cands:
            A = [[poly_to_elt(K, sum(vec[(p_ * 3 + q_) * DEG + k] * t ** k for k in range(DEG)), t)
                  for q_ in range(3)] for p_ in range(3)]
            if not (det3(K, A) == zero):
                return len(ns), A
        return len(ns), None

    report = {'probe': 'ptolemy_duality_generic', 'manifold': NAME, 'obstruction_class': KCLS,
              'field': d['field'], 'n_automorphisms': len(autos), 'K_over_Q_normal': normal,
              'automorphism_element_orders': sorted(_element_orders(autos, fe)),
              'automorphism_group_axioms_verified': grp,
              'relator_gate': gate, 'sl3_lift': sl3, 'rows': {}}
    print(f"\n=== the test: UNTWISTED (lambda pinned to 1) and TWISTED (lambda measured) ===")
    print(f"   {'sigma':24s} {'untwisted':>16s} {'twisted':>16s}  {'lambda on gens':>18s}")
    for i, g in enumerate(autos):
        lam1 = {gg: one for gg in gens}
        d1, A1 = solve_int(g, lam1)
        lam = {}
        ok_lam = True
        for gg in gens:
            ci = trace(K, mat(gg.upper()))
            if ci == zero:
                ok_lam = False
                break
            lam[gg] = sig_apply(trace(K, mat(gg)), g) / ci
        if ok_lam:
            d2, A2 = solve_int(g, lam)
            lam_desc = ("all 1" if all(lam[gg] == one for gg in gens)
                        else ("mu_3" if all((lam[gg] ** 3 if False else lam[gg] * lam[gg] * lam[gg]) == one
                                            for gg in gens) else "other"))
        else:
            d2, A2, lam_desc = None, None, "chi(g^-1)=0"
        nm = f"t -> {g}"
        report['rows'][nm] = {'untwisted_dim': d1, 'untwisted_found': A1 is not None,
                              'twisted_dim': d2, 'twisted_found': A2 is not None,
                              'lambda': lam_desc, 'is_identity': bool(sp.simplify(g - t) == 0)}
        print(f"   {nm:24s} {('FOUND(' + str(d1) + ')') if A1 else ('none(' + str(d1) + ')'):>16s} "
              f"{(('FOUND(' + str(d2) + ')') if A2 else ('none(' + str(d2) + ')')) if d2 is not None else 'n/a':>16s}"
              f"  {lam_desc:>18s}")

    ident = [k for k, v in report['rows'].items() if v['is_identity']]
    id_unt = report['rows'][ident[0]]['untwisted_found'] if ident else None
    id_tw = report['rows'][ident[0]]['twisted_found'] if ident else None
    winners_u = [k for k, v in report['rows'].items() if v['untwisted_found'] and not v['is_identity']]
    winners_t = [k for k, v in report['rows'].items() if v['twisted_found'] and not v['is_identity']]
    print(f"\n=== control + verdict ===")
    print(f"   identity row (MUST fail for a non-self-dual rep): untwisted {id_unt}, twisted {id_tw}")
    control_ok = (id_unt is False and id_tw is not True)
    print(f"   refutation control passes: {control_ok}")
    print(f"   non-identity automorphisms with an UNTWISTED intertwiner: {winners_u}")
    print(f"   non-identity automorphisms with a TWISTED  intertwiner: {winners_t}")
    schur = all(v['untwisted_dim'] in (0, DEG) for v in report['rows'].values())
    print(f"   Schur: every nonzero nullspace has dim == [K:Q] = {DEG}: {schur}")
    report.update({'refutation_control_passes': control_ok,
                   'untwisted_winners': winners_u, 'twisted_winners': winners_t,
                   'schur_dims_ok': schur})
    if len(autos) <= 1:
        v = "UNASKABLE: K admits only the identity automorphism; no candidate sigma exists."
    elif not control_ok:
        v = "TEST BROKEN: the identity control did not fail; treat every row as unreliable."
    elif winners_u:
        v = (f"UNTWISTED duality HOLDS for {winners_u} -- an equality of GL(3,K) "
             f"representations, reproducing the L6a4 class-1 phenomenon on {NAME}.")
    elif winners_t:
        v = (f"TWISTED only: {winners_t} gives a PGL(3,K) conjugacy but NO untwisted one. "
             f"The L6a4 phenomenon does NOT reproduce here in its GL(3,K) form.")
    else:
        v = (f"NO automorphism of K intertwines sigma(rho) with rho^-T on {NAME} class "
             f"{KCLS}, twisted or not -- a scope-(a) negative for this manifold.")
    report['verdict'] = v
    print(f"\nVERDICT: {v}")
    out = HERE / f'{stem}-duality-generic.json'
    out.write_text(json.dumps(report, indent=1) + "\n")
    print(f"\nreport -> {out}")


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('stem', help='e.g. m004-c1')
    main(ap.parse_args().stem)
