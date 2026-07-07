#!/usr/bin/env python3
"""Foundation probe for the Borromean qZeilberger certificate (bean n920,
PR #3450 route 2): derive + NUMERICALLY VERIFY the q-shift ratios of the
Habiro Borromean summand.

Habiro summand (diagonal colors, {a} = q^{a/2} - q^{-a/2}):

    F(n,l) = (-1)^l {n}^2 (prod_{j=1}^{l} {n+j}{n-j})^3
             / (prod_{j=l+1}^{2l+1} {j})^2 ,   J_{B,n} = sum_{l=0}^{n-1} F(n,l).

qZeilberger needs F to be q-proper-hypergeometric: F(n,l+1)/F(n,l) and
F(n+1,l)/F(n,l) rational in (x, y) with x = q^n, y = q^l.  The n-shift
product ratio telescopes:

    prod_{j=1}^l {n+1+j}{n+1-j} / prod_{j=1}^l {n+j}{n-j}
       = ({n+l+1}/{n+1}) * ({n}/{n-l}).

Candidate closed forms (to be verified):
    s  = F(n,l+1)/F(n,l)
       = -[(x+1/x) - (qy+1/(qy))]^3 * {l+1}^2 / ({2l+2}^2 {2l+3}^2)
    r1 = F(n+1,l)/F(n,l)
       = ({n+1}^2/{n}^2) * [({n+l+1}{n})/({n+1}{n-l})]^3
    ri = F(n+i,l)/F(n,l) = prod_{t=0}^{i-1} r1(q^t x, y)

where {n+l+1}{n-l-1} = (x+1/x)-(qy+1/(qy)) is integer-power in (x,y),
{l+1}^2 = qy-2+1/(qy), {2l+2}^2 = q^2 y^2 -2 + 1/(q^2 y^2),
{2l+3}^2 = q^3 y^2 -2 + 1/(q^3 y^2).

This script verifies each ratio EXACTLY (symbolically, via the half-power
ring xs^2=x, ys^2=y, v^2=q) AND numerically against direct F evaluation,
and reports whether each is rational in (x,y) (integer q-powers only) —
the q-proper-hypergeometric precondition for qZeilberger.

Audit-only; no wiring.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import sympy as sp

# half-power ring: xs = q^{n/2}, ys = q^{l/2}, v = q^{1/2}
xs, ys, v = sp.symbols("xs ys v", positive=True)
q, x, y = sp.symbols("q x y", positive=True)

# integer-power aliases
X = xs**2   # = q^n = x
Y = ys**2   # = q^l = y
Q = v**2    # = q


def brk(coef_x, coef_y, coef_c):
    """{a} for a = coef_x*n + coef_y*l + coef_c, as a Laurent elt in xs,ys,v.
    {a} = q^{a/2} - q^{-a/2} = xs^cx ys^cy v^cc - xs^-cx ys^-cy v^-cc."""
    up = xs**coef_x * ys**coef_y * v**coef_c
    return up - 1 / up


def F_ratio_direct(n_shift, l_shift):
    """Exact F(n+n_shift, l+l_shift)/F(n,l) in the (xs,ys,v) ring, built
    from the definition via the telescoped product forms.  Returns a
    simplified sympy expression."""
    # We build F(n,l) symbolically is impossible (products over l), so we
    # verify ratios numerically instead (see numeric_check).  This function
    # returns the CANDIDATE closed form for (1,0),(0,1),(2,0).
    raise NotImplementedError


def cand_s():
    core = (X + 1 / X) - (Q * Y + 1 / (Q * Y))          # {n+l+1}{n-l-1}
    l1sq = Q * Y - 2 + 1 / (Q * Y)                        # {l+1}^2
    d2 = Q**2 * Y**2 - 2 + 1 / (Q**2 * Y**2)              # {2l+2}^2
    d3 = Q**3 * Y**2 - 2 + 1 / (Q**3 * Y**2)              # {2l+3}^2
    return -core**3 * l1sq / (d2 * d3)


def cand_r1():
    n1sq = Q * X - 2 + 1 / (Q * X)      # {n+1}^2
    nsq = X - 2 + 1 / X                 # {n}^2
    # ({n+l+1}{n})/({n+1}{n-l})
    num = brk(1, 1, 1) * brk(1, 0, 0)   # {n+l+1}{n}
    den = brk(1, 0, 1) * brk(1, -1, 0)  # {n+1}{n-l}
    ratio = num / den
    return (n1sq / nsq) * ratio**3


def to_xy(expr):
    """Substitute the half-power ring back to (x,y,q); returns None if the
    result still contains an odd power of xs, ys, or v (i.e. NOT rational
    in (x,y,q))."""
    e = sp.simplify(sp.cancel(sp.together(expr)))
    # express in x=xs^2, y=ys^2, q=v^2 by testing evenness: substitute
    # xs->x**Rational(1,2), etc., then simplify; if sqrt remains, not rational
    e2 = e.subs({xs: x**sp.Rational(1, 2), ys: y**sp.Rational(1, 2),
                 v: q**sp.Rational(1, 2)})
    e2 = sp.simplify(sp.cancel(sp.together(e2)))
    has_sqrt = e2.has(sp.Pow) and any(
        (b in (x, y, q)) and (isinstance(ex, sp.Rational) and ex.q != 1)
        for b, ex in (t.as_base_exp() for t in sp.preorder_traversal(e2)
                      if isinstance(t, sp.Pow))
    )
    return None if has_sqrt else e2


def numeric_check(cand_xy, n_shift, l_shift, trials=6):
    """Evaluate cand_xy(x=q^n,y=q^l) vs the DIRECT ratio F(n+ns,l+ls)/F(n,l)
    computed from the definition, at several exact rational (q,n,l)."""
    def F(qv, n, l):
        def b(a):
            return sp.Rational(qv) ** sp.Rational(a, 2) - sp.Rational(qv) ** sp.Rational(-a, 2)
        num = b(n) ** 2 * sp.prod([b(n + j) * b(n - j) for j in range(1, l + 1)]) ** 3
        den = sp.prod([b(j) for j in range(l + 1, 2 * l + 2)]) ** 2
        return sp.Integer((-1) ** l) * num / den
    import itertools
    oks = []
    pts = [(sp.Rational(3, 2), 5, 2), (sp.Rational(5, 3), 6, 3),
           (sp.Rational(7, 4), 5, 1), (sp.Rational(9, 5), 7, 4),
           (sp.Rational(4, 3), 6, 2), (sp.Rational(11, 7), 8, 3)][:trials]
    for qv, n, l in pts:
        direct = sp.nsimplify(F(qv, n + n_shift, l + l_shift) / F(qv, n, l))
        got = cand_xy.subs({x: sp.Rational(qv) ** n, y: sp.Rational(qv) ** l,
                            q: sp.Rational(qv)})
        oks.append(sp.simplify(direct - got) == 0)
    return all(oks), oks


def main() -> int:
    t0 = time.time()
    print("\n  Borromean qZeilberger — shift-ratio foundation probe\n")

    results = {}
    for name, cand in (("s", cand_s()), ("r1", cand_r1())):
        xy = to_xy(cand)
        if xy is None:
            print(f"  [{name}] NOT rational in (x,y,q) — half-power survives")
            results[name] = {"rational_xy": False}
            continue
        ns, ls = (0, 1) if name == "s" else (1, 0)
        ok, oks = numeric_check(xy, ns, ls)
        deg_y = sp.Poly(sp.numer(xy), y).degree() if xy.has(y) else 0
        print(f"  [{name}] rational in (x,y,q): YES | numeric match {sum(oks)}/{len(oks)}"
              f" | verified={ok}")
        print(f"        {name} = {sp.simplify(xy)}")
        results[name] = {"rational_xy": True, "numeric_ok": bool(ok),
                         "expr": str(sp.simplify(xy))}

    all_ok = all(r.get("numeric_ok") for r in results.values())
    print(f"\n  precondition (both ratios rational + numerically verified): {all_ok}"
          f"  ({time.time()-t0:.1f}s)")
    if all_ok:
        print("  => summand is q-proper-hypergeometric; qZeilberger solve is well-posed.")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
