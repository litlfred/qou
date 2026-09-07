"""The trace field of a Ptolemy solution, and WHY the generators cannot witness
complex type on this manifold.

Three exact measurements over K = Q[T]/(f), each of which is an independent check on
the rest of the pipeline rather than a new claim:

  1. The number of REAL roots of f.  A real-type (self-dual) representation has real
     character; a totally imaginary trace field is consistent with complex type and
     inconsistent with the character being real under any embedding.
  2. The Q-span of chi(w) over many words -- i.e. is the trace field all of K, or a
     proper subfield?  The Ptolemy field can be strictly larger than the trace field
     (Garoufalidis-Goerner-Zickert study exactly this), so this is measured, not
     assumed.
  3. The minimal polynomial of each generator's character, and whether the generator's
     matrix is a SCALAR times a unipotent.

Point 3 is the one that matters, because it converts an empirical blind spot into a
structural fact.  On L6a4 class 1 EVERY generator turns out to be zeta * unipotent for
some zeta in mu_3: b and c with zeta = 1, and a with zeta a primitive cube root -- so
chi(a) = 3*zeta_3, with minimal polynomial x^2 + 3x + 9.  For such a matrix the
character ratio chi(g)/chi(g^-1) is forced into mu_3 no matter what the representation
does, so the PGL-invariant test chi^3/det can NEVER fail on a generator.  The
generators-only test does not merely happen to miss the obstruction here; it is
incapable of seeing it.  That is why the verdict in exact_character_selfduality.py is
taken from a word sweep.

It is also the expected picture for a NON-TRIVIAL obstruction class: boundary-unipotent
in PSL(3,C) means each meridian is unipotent projectively, and the obstruction to
making them all unipotent in SL(3,C) simultaneously is exactly the mu_3 discrepancy
seen here.

NO FLOAT64: Fraction and K only; sympy over QQ for the minimal polynomials.
"""
import itertools
import json
import pathlib
import sys

import snappy
import sympy as sp
from snappy.ptolemy.coordinates import PtolemyCoordinates

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import exact_character_selfduality as X          # noqa: E402
from numberfield import NumberField              # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
T = sp.Symbol('T')


def to_poly(e):
    return sum(sp.Rational(c.numerator, c.denominator) * T**k for k, c in enumerate(e.v))


def min_poly_over_Q(alpha, K, fe):
    """Minimal polynomial of an element of K, by linear algebra on its powers."""
    fpoly = sp.Poly(fe, T)
    red = lambda e: sp.rem(sp.Poly(sp.expand(e), T), fpoly).as_expr()
    rows, cur = [], sp.Integer(1)
    for _ in range(K.deg + 1):
        p = sp.Poly(cur, T)
        rows.append([p.coeff_monomial(T**i) for i in range(K.deg)])
        cur = red(cur * alpha)
    ns = sp.Matrix(rows).T.nullspace()
    if not ns:
        return None
    v = ns[0]
    lcm = sp.ilcm(*[sp.denom(sp.Rational(c)) for c in v]) if len(v) > 1 else 1
    x = sp.Symbol('x')
    return sp.factor(sp.expand(sum(sp.Rational(v[k]) * lcm * x**k for k in range(len(v)))))


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else 'L6a4'
    kcls = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    maxlen = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    d = json.loads((HERE / f'{name}-c{kcls}-ptolemy-in-K.json').read_text())
    gen = sp.Symbol('t')
    fe_t = sp.sympify(d['field']['min_poly'])
    fe = fe_t.subs(gen, T)
    K = NumberField([X._frac(c)
                     for c in reversed(sp.Poly(sp.expand(fe_t), gen).all_coeffs())])
    Elt = X.Elt
    one, zeroE = Elt(K, K.one()), Elt(K, K.zero())

    real_roots = len(sp.Poly(fe_t, gen).real_roots())
    print(f"{name} c{kcls}: f = {fe_t}")
    print(f"  degree {K.deg}, real roots {real_roots} of {K.deg}"
          f"  ({'TOTALLY IMAGINARY' if real_roots == 0 else 'has real embeddings'})")

    pt = {k: X.poly_to_elt(K, sp.sympify(v), gen) for k, v in d['ptolemy'].items()}
    M = snappy.Manifold(name)
    V = M.ptolemy_variety(3, obstruction_class=kcls, eliminate_fixed_ptolemys=True)
    dd = dict(pt)
    dd['1'] = one
    C = PtolemyCoordinates(dd, is_numerical=False,
                           py_eval_section=eval(V.py_eval_section()),
                           manifold_thunk=lambda: M,
                           non_trivial_generalized_obstruction_class=(kcls != 0))
    G = M.fundamental_group()
    gens = G.generators()

    # mu_3 in K.  Do NOT ask sympy to solve z^2 + z + 1 = 0 symbolically over the
    # field -- it returns nested radicals in sqrt(-3) and sqrt(5) that are not usable
    # as K elements.  Instead take the candidates the data hands you, chi(g)/3 (a
    # scalar-times-unipotent generator has chi = 3*zeta), and VERIFY each by
    # z^2 + z + 1 == 0 in K.  Candidates that fail are simply dropped.
    zetas, seen_z = [], set()
    third = Elt(K, K.inv(K.const(3)))
    for g in gens:
        cand = X.trace(K, C.evaluate_word(g, G)) * third
        if (cand * cand + cand + one) == 0 and cand.v not in seen_z:
            seen_z.add(cand.v)
            zetas.append(cand)
    print(f"  primitive cube roots of unity in K: {len(zetas)}"
          + (f"   e.g. {zetas[0]}" if zetas else "")
          + "   (verified by z^2 + z + 1 = 0)")

    rows = []
    for g in gens:
        Mg = C.evaluate_word(g, G)
        chi = X.trace(K, Mg)
        mp = min_poly_over_Q(to_poly(chi), K, fe)
        scalar, kind = None, "neither"
        for lbl, z in [("1", one)] + [(f"zeta_{i}", z) for i, z in enumerate(zetas)]:
            N = [[Mg[i][j] - (z if i == j else zeroE) for j in range(3)] for i in range(3)]
            if all(N[i][j] == zeroE for i in range(3) for j in range(3)):
                scalar, kind = lbl, "scalar (M = zeta*I)"
                break
            N2 = [[sum((N[i][k] * N[k][j] for k in range(3)), zeroE) for j in range(3)]
                  for i in range(3)]
            N3 = [[sum((N2[i][k] * N[k][j] for k in range(3)), zeroE) for j in range(3)]
                  for i in range(3)]
            if all(N3[i][j] == zeroE for i in range(3) for j in range(3)):
                scalar, kind = lbl, "zeta * unipotent"
                break
        rows.append({"generator": g, "chi": repr(chi), "chi_min_poly": str(mp),
                     "scalar": scalar, "shape": kind})
        print(f"  {g}: chi = {chi}")
        print(f"      min poly over Q: {mp}")
        print(f"      shape: {kind}" + (f", zeta = {scalar}" if scalar else ""))

    # trace field: the Q-span of chi(w)
    letters = list(gens) + [g.upper() for g in gens]
    span, nwords = [], 0
    for L in range(1, maxlen + 1):
        for tup in itertools.product(letters, repeat=L):
            w = ''.join(tup)
            if any(w[i].swapcase() == w[i + 1] for i in range(len(w) - 1)):
                continue
            nwords += 1
            p = sp.Poly(to_poly(X.trace(K, C.evaluate_word(w, G))), T)
            span.append([p.coeff_monomial(T**i) for i in range(K.deg)])
    rk = sp.Matrix(span).rank()
    print(f"\n  Q-span of chi(w) over {nwords} words (length <= {maxlen}):"
          f" dimension {rk} of {K.deg}")
    print(f"  trace field == Ptolemy field K: {rk == K.deg}")

    all_scalar_unipotent = all(r["shape"] == "zeta * unipotent" for r in rows)
    if all_scalar_unipotent:
        print("\n  EVERY generator is zeta * unipotent, zeta in mu_3.  For such a matrix")
        print("  chi(g)/chi(g^-1) lies in mu_3 whatever the representation does, so the")
        print("  PGL-invariant test chi^3/det CANNOT fail on a generator.  A")
        print("  generators-only self-duality test is not unlucky here -- it is blind.")

    out = HERE / f'{name}-c{kcls}-trace-field.json'
    out.write_text(json.dumps({
        "manifold": name, "obstruction_class": kcls, "field": d["field"],
        "real_roots": real_roots, "totally_imaginary": real_roots == 0,
        "primitive_cube_roots_in_K": len(zetas),
        "generators": rows,
        "trace_field": {"words": nwords, "max_length": maxlen, "span_dimension": rk,
                        "equals_ptolemy_field": bool(rk == K.deg)},
        "generators_all_scalar_times_unipotent": all_scalar_unipotent,
    }, indent=2) + "\n")
    print(f"  wrote {out.name}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
