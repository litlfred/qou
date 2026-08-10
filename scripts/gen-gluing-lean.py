#!/usr/bin/env python3
"""Generator for QOU/Knot/GeneratedGluing.lean -- see bean `qou-glnl`.

Usage:  python3 scripts/gen-gluing-lean.py 4_1 5_2 6_1 ...   (emits Lean to stdout)

Every emitted proof is one `linear_combination` whose cofactor came from EXACT
polynomial division, and every non-vanishing lemma from a Bezout certificate
(`sympy.invert`). Both are asserted exact before emission, so a wrong candidate
fails here rather than producing a Lean file that does not compile.

The equations are emitted with DENOMINATORS CLEARED. The natural quotient form
would need `field_simp`, whose normal form is not predictable and therefore
cannot be code-generated -- the lesson from the hand-written 4_1/5_2 proofs.
"""
"""Generate a Lean module proving the edge gluing equations, with exact certificates."""
import warnings; warnings.filterwarnings("ignore")
import sys
import sympy as sp
from cypari import pari
import snappy

pari.allocatemem(1 << 31, silent=True)
MAXDEG, PREC_LO, PREC_HI, HEIGHT_CAP, BITS = 20, 150, 600, 25, 6000
x = sp.Symbol("x")


def _h(p): return max(len(str(abs(int(c)))) for c in pari.Vec(p))
def _ad(zr, zi, d, dig):
    pari.set_real_precision(dig); return pari.algdep(pari(f"({zr}) + ({zi})*I"), d)


def identify(zr, zi):
    for d in range(2, MAXDEG + 1):
        a, b = _ad(zr, zi, d, PREC_LO), _ad(zr, zi, d, PREC_HI)
        if str(a) != str(b) or _h(b) > HEIGHT_CAP: continue
        if not bool(pari.polisirreducible(b)): continue
        return d, str(b)
    return None


def express(shapes, deg, dig):
    pari.set_real_precision(dig)
    th = pari(f"({shapes[0].real()}) + ({shapes[0].imag()})*I")
    return [[int(c) for c in pari.lindep(
        [pari(f"({s.real()}) + ({s.imag()})*I")] + [th ** k for k in range(deg)])]
        for s in shapes]


def lean_expr(p, var="t"):
    """sympy poly in x -> Lean ℂ expression in `t`, rational coefficients."""
    p = sp.expand(p)
    if p == 0: return "0"
    terms = []
    P = sp.Poly(p, x)
    for k in range(P.degree(), -1, -1):
        c = sp.Rational(P.coeff_monomial(x ** k) if k else P.coeff_monomial(1))
        if c == 0: continue
        n, d = c.p, c.q
        cs = f"({n} / {d})" if d != 1 else (f"({n})" if n < 0 else f"{n}")
        if k == 0: terms.append(cs)
        elif k == 1: terms.append(f"{cs} * {var}")
        else: terms.append(f"{cs} * {var} ^ {k}")
    return " + ".join(terms)


def build(name):
    M = snappy.Manifold(name)
    n = M.num_tetrahedra()
    if "positively oriented" not in M.solution_type():
        return None
    shapes = M.tetrahedra_shapes("rect", bits_prec=BITS)
    got = identify(shapes[0].real(), shapes[0].imag())
    if got is None: return None
    deg, pstr = got
    P = sp.expand(sp.sympify(pstr.replace("^", "**")))
    rels = express(shapes, deg, PREC_HI)
    if rels != express(shapes, deg, PREC_LO): return None
    Z = [sp.expand(-sum(sp.Integer(r[k + 1]) * x ** k for k in range(len(r) - 1))
                   / sp.Integer(r[0])) for r in rels]
    rows = [[int(v) for v in r] for r in M.gluing_equations()][:n]

    # Bezout certificates for z_j != 0 and 1 - z_j != 0
    certs = []
    for Q in Z:
        for R in (Q, sp.expand(1 - Q)):
            u = sp.expand(sp.invert(sp.Poly(R, x), sp.Poly(P, x)).as_expr())
            v, rem = sp.div(sp.Poly(sp.expand(1 - u * R), x), sp.Poly(P, x))
            assert sp.expand(rem.as_expr()) == 0
            assert sp.expand(u * R + v.as_expr() * P) == 1
            certs.append((u, sp.expand(v.as_expr())))

    # cleared-form edge equations
    eqs = []
    for row in rows:
        lhs, rhs, lp, rp = sp.Integer(1), sp.Integer(1), [], []
        for j in range(n):
            a, b, c = row[3 * j], row[3 * j + 1], row[3 * j + 2]
            assert a >= 0 and b >= 0 and c >= 0
            if a: lhs *= Z[j] ** a; lp.append((f"z{j}", a))
            if c: lhs *= (Z[j] - 1) ** c; lp.append((f"(z{j} - 1)", c))
            if b: rhs *= (1 - Z[j]) ** b; rp.append((f"(1 - z{j})", b))
            if c: rhs *= Z[j] ** c; rp.append((f"z{j}", c))
        q, r = sp.div(sp.Poly(sp.expand(lhs - rhs), x), sp.Poly(P, x))
        assert sp.expand(r.as_expr()) == 0, f"{name}: RESIDUAL NONZERO"
        eqs.append((row, lp, rp, sp.expand(q.as_expr())))
    return dict(name=name, n=n, deg=deg, P=P, pstr=pstr, Z=Z, eqs=eqs, certs=certs)


def emit(d):
    nm = d["name"]; ident = nm.replace("_", "").replace("-", "")
    L = []
    A = L.append
    A(f"/-! ### `{nm}` — {d['n']} tetrahedra, shape field of degree {d['deg']}\n")
    A(f"Minimal polynomial `{d['pstr']}`. -/\n")
    A(f"namespace K{ident}\n")
    A(f"/-- The shape field's minimal polynomial, as a polynomial function. -/")
    A(f"noncomputable def minpoly (t : ℂ) : ℂ := {lean_expr(d['P'])}\n")
    for j, Q in enumerate(d["Z"]):
        A(f"/-- Shape `z{j}` of `{nm}`, as an element of `ℚ(θ)`. -/")
        A(f"noncomputable def z{j} (t : ℂ) : ℂ := {lean_expr(Q)}\n")
    for j, Q in enumerate(d["Z"]):
        u0, v0 = d["certs"][2 * j]
        u1, v1 = d["certs"][2 * j + 1]
        A(f"theorem z{j}_ne_zero {{t : ℂ}} (ht : minpoly t = 0) : z{j} t ≠ 0 := by")
        A(f"  intro h")
        A(f"  simp only [minpoly] at ht")
        A(f"  simp only [z{j}] at h")
        A(f"  have : (1 : ℂ) = 0 := by")
        A(f"    linear_combination ({lean_expr(u0)}) * h + ({lean_expr(v0)}) * ht")
        A(f"  exact absurd this one_ne_zero\n")
        A(f"theorem one_sub_z{j}_ne_zero {{t : ℂ}} (ht : minpoly t = 0) :"
          f" 1 - z{j} t ≠ 0 := by")
        A(f"  intro h")
        A(f"  simp only [minpoly] at ht")
        A(f"  simp only [z{j}] at h")
        A(f"  have : (1 : ℂ) = 0 := by")
        A(f"    linear_combination ({lean_expr(u1)}) * h + ({lean_expr(v1)}) * ht")
        A(f"  exact absurd this one_ne_zero\n")
    for k, (row, _lp, _rp, q) in enumerate(d["eqs"]):
        lparts, rparts = [], []
        for j in range(d["n"]):
            a, b, c = row[3 * j], row[3 * j + 1], row[3 * j + 2]
            if a: lparts.append(f"z{j} t ^ {a}")
            if c: lparts.append(f"(z{j} t - 1) ^ {c}")
            if b: rparts.append(f"(1 - z{j} t) ^ {b}")
            if c: rparts.append(f"z{j} t ^ {c}")
        lhs = " * ".join(lparts) or "1"
        rhs = " * ".join(rparts) or "1"
        # only the shapes this equation actually mentions -- otherwise Lean's linter
        # flags every unused `simp only` argument.
        used = sorted({j for j in range(d["n"])
                       if any(row[3 * j + k] for k in range(3))})
        A(f"/-- **Edge {k}** of `{nm}`, exponents `{row}`, denominators cleared. -/")
        A(f"theorem edge_{k} {{t : ℂ}} (ht : minpoly t = 0) :")
        A(f"    {lhs} = {rhs} := by")
        A(f"  simp only [minpoly] at ht")
        A(f"  simp only [{', '.join(f'z{j}' for j in used)}]")
        A(f"  linear_combination ({lean_expr(q)}) * ht\n")
    A(f"end K{ident}\n")
    return "\n".join(L)


if __name__ == "__main__":
    for nm in sys.argv[1:]:
        d = build(nm)
        print(emit(d) if d else f"-- {nm}: skipped")
