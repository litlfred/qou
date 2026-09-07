#!/usr/bin/env python3
"""Recover the FULL (un-eliminated) class-1 Ptolemy assignment for L6a4, exactly.

WHY.  Issue #7092 needs the coboundary test: does the duality/sigma ratio equal
prod_k z_k^{M[t][k]} for gauge scalars z, with M snappy's 128 x 6
_ptolemy_equations_action_by_decoration_change?  The test itself needs NO unknowns --
any integer vector in the LEFT KERNEL of M forces prod_t r_t^{n_t} = 1 whatever the
gauge is -- but it needs the FULL assignment, and the recorded artifact
L6a4-c1-ptolemy-in-K.json has only 26 coordinates (eliminate_fixed_ptolemys=True).
Measured: at most 2 of the 8 coordinates the {1,1,1,0} duality formula needs are present
on ANY tetrahedron.

HOW -- and this corrects my own previous attempt.  The earlier try
(ptolemy_full_assignment_reconstruction_blocked.py) propagated snappy's 112
IDENTIFICATIONS first, taking 26 known coordinates to 98, then solved for the remainder.
That was unverifiable: ZERO identifications relate two coordinates the file already
knows -- the recorded 26 are one representative per identification class -- so not a
single propagated value could be cross-checked, and the resulting inconsistent solve
could not be attributed.

The identifications are not needed.  The UN-ELIMINATED variety has 33 variables and 39
equations.  The file supplies 26 of them plus u, leaving 6 unknowns, over-determined by
39 equations.  Solve THAT directly: no propagation, nothing unverifiable, and the 39
equations are themselves the check.

VERIFICATION.  A solution is accepted only if ALL 39 un-eliminated equations reduce to
the zero polynomial in K = Q[T]/(f).  Over-determination (39 equations, 6 unknowns) means
a wrong solution is overwhelmingly unlikely to pass, and the emitted assignment carries
the count so a reader need not take it on trust.

Exact arithmetic in K throughout: sympy Rationals reduced modulo f.  No floats, no
tolerances -- an equation vanishes or it does not.

Output: computations/ptolemy/L6a4-c1-ptolemy-FULL.json
"""
import json
import re
import sys
import warnings

warnings.filterwarnings('ignore')
import sympy as sp
import snappy

T = sp.Symbol('T')
SRC = 'computations/ptolemy/L6a4-c1-ptolemy-in-K.json'
OUT = 'computations/ptolemy/L6a4-c1-ptolemy-FULL.json'


def main():
    d = json.load(open(SRC))
    f = sp.sympify(d['field']['min_poly'].replace('t', 'T'))
    red = lambda e: sp.expand(sp.rem(sp.expand(e), f, T))
    co = {k: sp.expand(sp.sympify(re.sub(r'\bt\b', 'T', v)))
          for k, v in d['ptolemy'].items()}
    u = co['u']
    assert red(u ** 2 + u + 1) == 0, "u is not a primitive cube root of unity"
    print(f"loaded {len(co)} recorded coordinates; u verified primitive", flush=True)

    M = snappy.Manifold(d['manifold'])
    V = M.ptolemy_variety(3, obstruction_class=d['obstruction_class'])   # NOT eliminated
    allv = sorted({str(v) for v in V.variables})
    eqs = [str(e) for e in V.equations]
    print(f"un-eliminated variety: {len(allv)} variables, {len(eqs)} equations", flush=True)

    known = {k: v for k, v in co.items() if k in allv}
    unknown = [v for v in allv if v not in co and v not in ('t',)]
    print(f"known from the file: {len(known)};  unknown: {len(unknown)} -> {unknown}",
          flush=True)
    if not unknown:
        print("nothing to solve -- the file already covers every variable")
        return 0

    X = {name: sp.Symbol('X_%d' % i) for i, name in enumerate(unknown)}
    sub_known = {sp.Symbol(k): v for k, v in known.items()}
    locs = {k: sp.Symbol(k) for k in allv}
    locs['u'] = sp.Symbol('u')

    polys = []
    for e in eqs:
        ex = sp.sympify(e.replace('^', '**'), locals=locs)
        ex = ex.subs(sub_known).subs(sp.Symbol('u'), u)
        ex = ex.subs({sp.Symbol(k): s for k, s in X.items()})
        ex = sp.expand(ex)
        if ex.free_symbols & set(X.values()):
            polys.append(ex)
    print(f"equations constraining the unknowns: {len(polys)}", flush=True)

    print("solving (over-determined; the equations are their own check) ...", flush=True)
    sols = sp.solve(polys, list(X.values()), dict=True)
    print(f"candidate solutions: {len(sols)}", flush=True)

    for si, s in enumerate(sols):
        full = dict(known)
        if not all(sym in s for sym in X.values()):
            print(f"  candidate {si}: under-determined, skipped", flush=True)
            continue
        for name, sym in X.items():
            full[name] = red(s[sym])
        full['u'] = u
        bad = 0
        for e in eqs:
            ex = sp.sympify(e.replace('^', '**'), locals=locs)
            r = red(sp.expand(ex.subs({sp.Symbol(k): v for k, v in full.items()})))
            if r != 0:
                bad += 1
        print(f"  candidate {si}: ALL {len(eqs)} equations -> non-zero {bad}", flush=True)
        if bad == 0:
            json.dump({
                'manifold': d['manifold'],
                'obstruction_class': d['obstruction_class'],
                'field': d['field'],
                'eliminated': False,
                'provenance': {
                    'derived_from': SRC,
                    'method': 'solve the 6 un-eliminated unknowns directly from the 39 '
                              'un-eliminated equations; identifications NOT used',
                    'equations_verified': len(eqs),
                    'nonzero': 0,
                },
                'ptolemy': {k: str(v) for k, v in full.items()},
            }, open(OUT, 'w'), indent=2)
            print(f"\nFULL ASSIGNMENT RECOVERED -- {len(full)} coordinates, "
                  f"all {len(eqs)} equations vanish exactly in K")
            print(f"wrote {OUT}")
            return 0

    print("\nNO candidate satisfies all equations.  The full assignment is NOT recovered;")
    print("do not proceed to the coboundary test on a partial or unverified assignment.")
    return 1


if __name__ == '__main__':
    sys.exit(main())
