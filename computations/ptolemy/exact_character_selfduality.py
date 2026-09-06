"""Decide self-duality of a boundary-unipotent PGL(3,C) representation DIRECTLY, by
exact character arithmetic in the Ptolemy number field K = Q[t]/(f).

WHY THIS EXISTS.  PR #6815 concluded complex type for the L6a4 obstruction-class-1
representations via the OBSTRUCTION ARGUMENT -- duality negates the obstruction class,
isomorphism preserves it, so 2*sigma = 0 forces sigma = 0 in Z/3.  Its two topological
inputs are carried as GGZ HYPOTHESES, not proofs.  A character computation needs
neither: a representation is self-dual iff its character is invariant under
g -> g^-1.  Agreement corroborates the hypotheses on this manifold; disagreement means
one of the two routes is wrong, which is worth more than either.

PGL, NOT SL -- and this is the whole subtlety.  A non-trivial obstruction class is
exactly the statement that the representation does NOT lift to SL(3,C), so
evaluate_word returns a matrix well-defined only up to a cube root of unity, and
chi(g) is well-defined only up to mu_3.  Scaling the generator's matrix by lambda
scales chi(g) by lambda and chi(g^-1) by lambda^-1, so the bare comparison
chi(g) == chi(g^-1) is NOT a PGL-invariant statement and must not be reported as one.
What IS invariant when lambda^3 = 1 is the comparison of CUBES: chi(g)^3 vs
chi(g^-1)^3, since the ambiguity enters as lambda^3 = 1 and lambda^-3 = 1 -- and
self-duality of the projective representation forces the cubes to agree.  So
chi(g)^3 != chi(g^-1)^3 for a single g is a sound certificate of complex type, while
chi(g) != chi(g^-1) alone is not.  Both are reported; only the cube test is a verdict.

The test is FIELD-THEORETIC, not numerical.  chi(g) and chi(g^-1) are elements of K
and are compared as such -- no complex embedding is chosen, so "how close to real"
never arises and no tolerance is involved.

NO FLOAT64: sympy over QQ and in K throughout.  float() appears nowhere.
"""
import json
import pathlib
import sys

import snappy
import sympy as sp
from snappy.ptolemy.coordinates import PtolemyCoordinates

HERE = pathlib.Path(__file__).resolve().parent
T = sp.Symbol('T')          # field generator; deliberately NOT `t`, which is the
                            # name snappy gives the non-zero-condition variable.


def make_reducer(fe):
    fpoly = sp.Poly(fe, T)

    def red(e):
        n, dn = sp.fraction(sp.together(sp.expand(e)))
        n = sp.rem(sp.Poly(sp.expand(n), T), fpoly).as_expr()
        dn = sp.rem(sp.Poly(sp.expand(dn), T), fpoly).as_expr()
        if dn == 0:
            raise ZeroDivisionError("denominator vanishes in K")
        if dn == 1:
            return n
        inv = sp.invert(sp.Poly(dn, T), fpoly).as_expr()
        return sp.rem(sp.Poly(sp.expand(n * inv), T), fpoly).as_expr()
    return red


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else 'L6a4'
    kcls = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    src = HERE / f'{name}-c{kcls}-ptolemy-in-K.json'
    d = json.loads(src.read_text())
    fe = sp.sympify(d['field']['min_poly']).subs(sp.Symbol('t'), T)
    red = make_reducer(fe)
    pt = {k: sp.sympify(v).subs(sp.Symbol('t'), T) for k, v in d['ptolemy'].items()}

    M = snappy.Manifold(name)
    V = M.ptolemy_variety(3, obstruction_class=kcls, eliminate_fixed_ptolemys=True)
    dd = dict(pt)
    dd['1'] = sp.Integer(1)
    C = PtolemyCoordinates(
        dd, is_numerical=False,
        py_eval_section=eval(V.py_eval_section()),
        manifold_thunk=lambda: M,
        non_trivial_generalized_obstruction_class=(kcls != 0))
    G = M.fundamental_group()
    gens = G.generators()
    print(f"{name} c{kcls}: K = Q[T]/({fe}), degree {sp.Poly(fe, T).degree()}")
    print(f"  fundamental group generators: {gens}")

    rows = []
    for g in gens:
        Mg = C.evaluate_word(g)
        Mi = C.evaluate_word(g.upper())
        tr = red(sum(Mg[i][i] for i in range(3)))
        tri = red(sum(Mi[i][i] for i in range(3)))
        prod = [[red(sum(Mg[i][k] * Mi[k][j] for k in range(3))) for j in range(3)]
                for i in range(3)]
        offdiag_zero = all(prod[i][j] == 0 for i in range(3) for j in range(3) if i != j)
        scalar = prod[0][0] if offdiag_zero and prod[0][0] == prod[1][1] == prod[2][2] else None
        eq_bare = red(tr - tri) == 0
        eq_cube = red(tr**3 - tri**3) == 0
        rows.append({
            "generator": g,
            "chi": str(tr), "chi_inv": str(tri),
            "chi_eq_chi_inv": bool(eq_bare),
            "chi_cubed_eq": bool(eq_cube),
            "g_times_g_inv_is_scalar": scalar is not None,
            "scalar": str(scalar) if scalar is not None else None,
        })
        print(f"\n  g = {g}")
        print(f"    chi(g)      = {tr}")
        print(f"    chi(g^-1)   = {tri}")
        print(f"    chi(g) == chi(g^-1)        : {eq_bare}      (NOT PGL-invariant)")
        print(f"    chi(g)^3 == chi(g^-1)^3    : {eq_cube}      <- the verdict test")
        print(f"    g*g^-1 scalar in PGL       : {scalar is not None}"
              + (f"  = {scalar}" if scalar is not None else ""))

    witnesses = [r["generator"] for r in rows if not r["chi_cubed_eq"]]
    verdict = "COMPLEX TYPE (not self-dual)" if witnesses else "no obstruction found on the generators"
    print(f"\n  VERDICT: {verdict}")
    if witnesses:
        print(f"    certified by generator(s) {witnesses}: chi^3 differs in K")
    else:
        print("    NOTE: this is NOT a proof of self-duality -- the generators are a"
              " finite sample.\n    A self-duality claim needs a conjugating matrix,"
              " not the absence of a witness.")

    out = HERE / f'{name}-c{kcls}-character-selfduality.json'
    out.write_text(json.dumps({
        "manifold": name, "obstruction_class": kcls,
        "field": d["field"], "generators": gens,
        "rows": rows,
        "complex_type_witnesses": witnesses,
        "verdict": verdict,
        "method": "exact character in K; cube test is the PGL-invariant one",
    }, indent=2) + "\n")
    print(f"  wrote {out.name}")
    return 0 if witnesses else 2


if __name__ == '__main__':
    sys.exit(main())
