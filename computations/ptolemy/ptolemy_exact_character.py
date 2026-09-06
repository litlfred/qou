"""Lift a char-0 RUR solution to ALL Ptolemy coordinates in K = Q[T]/(f) and round-trip
it against the ORIGINAL Ptolemy equations.

The RUR gives only the coordinates that survived the FKR 1307.6697 sec 6.1 elimination.
This replays the recorded substitutions in REVERSE to recover the rest, then checks the
lifted point against the equations snappy actually produced -- not against the reduced
system, which is the one place a reduction bug cannot be seen.  That check is what the
retraction in PR #6815 was missing.

TRAP, and it cost a false negative here.  snappy names the non-zero-condition variable
`t`, which is also the natural name for the field generator.  A round-trip written with
STRING substitution, replacing coordinate names shortest-last, therefore rewrites `t`
INSIDE values already inserted -- it reported 30 of 34 equations failing on a lift that
is in fact exact.  Substitute with sympy on distinct symbols; the generator here is `T`.

NO FLOAT64.  All arithmetic is sympy over QQ or in K.  float() appears nowhere and
nothing is compared against a tolerance -- residuals are exactly 0 in K.
"""
import json
import pathlib
import re
import sys

import snappy
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
T = sp.Symbol('T')      # NOT 't' -- see the TRAP note above.


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


def lift_through_subs(vals, subs_order, red):
    """Undo the elimination.  subs_order records eliminations in the order APPLIED, so
    it is replayed in REVERSE: the last variable eliminated is expressed in terms of
    what was still free then, which is exactly what is known once the later ones are
    back."""
    known = dict(vals)
    for name, expr in reversed(subs_order):
        e = sp.sympify(expr)
        missing = {str(s) for s in e.free_symbols} - set(known)
        if missing:
            raise SystemExit(f"cannot lift {name}: still unknown {sorted(missing)}")
        val = e.subs({sp.Symbol(k): v for k, v in known.items()}, simultaneous=True)
        known[name] = red(val)
    return known


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else 'L6a4'
    kcls = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    d = json.loads((HERE / f'{name}-c{kcls}-charzero-pinned.json').read_text())
    sub = json.loads((HERE / f'{name}_c{kcls}_subs.json').read_text())

    fe = sp.sympify(d["field"]["min_poly"]).subs(sp.Symbol('t'), T)
    red = make_reducer(fe)
    vals = {k: sp.sympify(v).subs(sp.Symbol('t'), T)
            for k, v in d["values"].items() if k != d["convention"]["parameter_variable"]}

    ptolemy_names, vars_original = sub['ptolemy_names'], sub['vars_original']
    name_of = dict(zip(vars_original, ptolemy_names))
    print(f"{name} c{kcls}: K = Q[T]/({fe}), degree {sp.Poly(fe, T).degree()}")
    print(f"  {len(vals)} coordinates from the RUR, {len(sub['subs_order'])} eliminated,"
          f" {len(ptolemy_names)} Ptolemy coordinates total")

    known = lift_through_subs(vals, sub['subs_order'], red)
    missing = [v for v in vars_original if v not in known]
    print(f"  lifted: {len(known)} of {len(vars_original)}"
          + (f"  MISSING {missing}" if missing else ""))
    if missing:
        return 1
    zero = [name_of[v] for v in vars_original if known[v] == 0]
    print(f"  zero Ptolemy coordinates: {zero if zero else 'NONE'}")
    if zero:
        return 1

    # THE ROUND TRIP.  Against snappy's own equations, symbolically.
    M = snappy.Manifold(name)
    V = M.ptolemy_variety(3, obstruction_class=kcls, eliminate_fixed_ptolemys=True)
    xsym = {p: sp.Symbol(x) for p, x in zip(ptolemy_names, vars_original)}

    def conv(s):
        for p in sorted(ptolemy_names, key=len, reverse=True):
            s = re.sub(r'\b%s\b' % re.escape(p), str(xsym[p]), s)
        return s

    orig = [sp.sympify(conv(str(e)).replace('^', '**'))
            for e in V.equations_with_non_zero_condition]
    valmap = {sp.Symbol(v): known[v] for v in vars_original}
    bad = []
    for i, e in enumerate(orig):
        ex = e.subs(valmap, simultaneous=True)
        if {str(x) for x in ex.free_symbols} - {'T'}:
            bad.append(i)
            continue
        num, _ = sp.fraction(sp.together(ex))
        if red(sp.expand(num)) != 0:
            bad.append(i)
    print(f"  ORIGINAL Ptolemy equations: {len(orig)}; NONZERO in K: {len(bad)}"
          + (f"  {bad}" if bad else ""))
    if bad:
        print("  ROUND TRIP FAILED -- do not report a lift or anything downstream of it.")
        return 1

    out = HERE / f'{name}-c{kcls}-ptolemy-in-K.json'
    out.write_text(json.dumps({
        "manifold": name, "obstruction_class": kcls,
        "field": d["field"],
        "roundtrip": {"original_equations": len(orig), "nonzero_in_K": 0,
                      "zero_coordinates": 0},
        "ptolemy": {name_of[v]: str(known[v]).replace('T', 't') for v in vars_original},
    }, indent=2) + "\n")
    print(f"  ROUND TRIP CLEAN over Q.  wrote {out.name}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
