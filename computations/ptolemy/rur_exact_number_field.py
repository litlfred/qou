"""Lift the char-0 RUR of L6a4 obstruction class 1 into K = Q[t]/(f) and verify the
saturated system EXACTLY -- no floating point anywhere.

PR #6815 verified a class-1 point in GF(32003^2).  This does the same over Q, which
is what the char-0 msolve run makes possible: the RUR expresses every coordinate as a
rational function of t, f is the degree-4 eliminating polynomial, so all 13 coordinates
live in K and the equations are checked by exact polynomial arithmetic modulo f.

The RUR sign/multiplier convention is NOT assumed -- it is PINNED by the verification.
Only one candidate makes the whole system vanish in K.  Do not carry a convention
across manifolds: msolve's output shape varies, and on 4_1 the same file needed a
different reading.

TRAP, and it cost a run here.  An msolve RUR carries one FEWER coordinate block than
it has variables when the linear form is a single variable: that variable IS the
parameter, so x_j = t and msolve emits no block for it.  Here varnames has 13 entries
and the parametrization has 12, with linear form [0,...,0,1] selecting `u`.  A bare
zip(varnames, coords) truncates silently, leaves `u` unbound, and 18 of 19 equations
still vanish -- so the failure surfaces as ONE stubborn equation (the saturation
equation u*prod(x) - 1) rather than as an error.  Check len(coords) against
len(varnames) before zipping.

NO FLOAT64: every quantity is a sympy Rational or a Poly over QQ.  float() appears
nowhere, and no result is compared to a tolerance -- the residuals are exactly 0 in K.
"""
import ast
import json
import pathlib
import sys

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
t = sp.Symbol('t')


def parse_rur(path):
    """msolve -P 1 char-0 output -> (varnames, linform, f, f', [(num_i, mult_i)])."""
    raw = pathlib.Path(path).read_text().strip().rstrip(':')
    data = ast.literal_eval(raw)
    if data[0] != 0:
        raise SystemExit(f"msolve did not return a zero-dimensional RUR: marker {data[0]}")
    body = data[1]
    varnames, linform, param = body[3], body[4], body[5]
    if param[0] != 1:
        raise SystemExit(f"unexpected parametrization marker {param[0]}")
    blk = param[1]
    poly = lambda cs: sp.Poly(list(reversed(cs)), t, domain='QQ')
    f = poly(blk[0][1])
    fp = poly(blk[1][1])
    coords = [(poly(e[0][1]), sp.Integer(e[1])) for e in blk[2]]
    return varnames, linform, f, fp, coords


def parse_ms(path):
    """msolve .ms input -> (varnames, {name: Symbol}, [sympy exprs])."""
    lines = [l.strip() for l in pathlib.Path(path).read_text().splitlines() if l.strip()]
    varnames = [v.strip() for v in lines[0].split(',')]
    syms = {v: sp.Symbol(v) for v in varnames}
    polys = [sp.sympify(l.rstrip(',').strip().replace('^', '**'), locals=syms)
             for l in lines[2:] if l.rstrip(',').strip()]
    return varnames, syms, polys


def lift(varnames, linform, f, fp, coords):
    """Return {name: element of K as a canonical rep in Q[t] of degree < deg f}."""
    fe = f.as_expr()
    fpoly = sp.Poly(fe, t)
    red = lambda e: sp.rem(sp.Poly(sp.expand(e), t), fpoly).as_expr()

    if sp.gcd(fpoly, sp.Poly(fp.as_expr(), t)).as_expr() != 1:
        raise SystemExit("f is not squarefree -- f' is not invertible in K")
    inv_fp = sp.invert(sp.Poly(fp.as_expr(), t), fpoly).as_expr()

    # The linear-form variable, if the form is a single variable, IS the parameter.
    param_var = None
    if len(coords) == len(varnames) - 1:
        hot = [i for i, c in enumerate(linform) if c != 0]
        if len(hot) != 1 or linform[hot[0]] != 1:
            raise SystemExit(f"one block short but linear form is not a bare variable: {linform}")
        param_var = varnames[hot[0]]
    elif len(coords) != len(varnames):
        raise SystemExit(f"{len(coords)} blocks for {len(varnames)} variables")

    plain = [v for v in varnames if v != param_var]
    vals = {v: red(-num.as_expr() * red(inv_fp * sp.Rational(1, int(mult))))
            for v, (num, mult) in zip(plain, coords)}
    if param_var is not None:
        vals[param_var] = t
    return vals, red, param_var


def main():
    rur_path = HERE / 'L6a4-c1-saturated-rur-charzero.res'
    ms_path = HERE / 'L6a4-c1-saturated-charzero.ms'
    varnames, linform, f, fp, coords = parse_rur(rur_path)
    fe = f.as_expr()
    fl = sp.factor_list(fe)
    irred = len(fl[1]) == 1 and fl[1][0][1] == 1
    print(f"RUR: {len(varnames)} variables, {len(coords)} parametrized blocks, "
          f"deg f = {f.degree()}")
    print(f"  f(t) = {fe}")
    print(f"  f irreducible over Q: {irred}   (factorization {fl})")

    msvars, syms, polys = parse_ms(ms_path)
    if msvars != varnames:
        raise SystemExit(f"variable order differs: {msvars} vs {varnames}")
    print(f"system: {len(msvars)} variables, {len(polys)} equations")

    vals, red, param_var = lift(varnames, linform, f, fp, coords)
    if param_var:
        print(f"  linear form is the bare variable {param_var!r}: {param_var} = t")

    subs = {syms[v]: vals[v] for v in varnames}
    nonzero = [i for i, p in enumerate(polys)
               if red(sp.expand(p.subs(subs, simultaneous=True))) != 0]
    print(f"  equations NONZERO in K: {len(nonzero)} of {len(polys)}"
          + (f"  {nonzero}" if nonzero else ""))
    if nonzero:
        print("  NOT verified -- do not report a lift.")
        return 1

    # A coordinate that is zero in K is not a Ptolemy point; the saturation is
    # supposed to have removed exactly those, so check rather than assume.
    zero = [v for v in varnames if vals[v] == 0]
    print(f"  zero coordinates: {zero if zero else 'NONE'}")
    if zero:
        return 1

    out = HERE / 'L6a4-c1-charzero-pinned.json'
    out.write_text(json.dumps({
        "manifold": "L6a4",
        "obstruction_class": 1,
        "source_rur": rur_path.name,
        "source_system": ms_path.name,
        "field": {"generator": "t", "min_poly": str(fe), "degree": int(f.degree()),
                  "irreducible_over_Q": bool(irred)},
        "convention": {"sign": -1, "divide_by_multiplier": True,
                       "parameter_variable": param_var},
        "values": {v: str(vals[v]) for v in varnames},
        "verified": {"equations": len(polys), "nonzero_in_K": 0, "zero_coordinates": 0},
    }, indent=2) + "\n")
    print(f"  VERIFIED over Q.  wrote {out.name}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
