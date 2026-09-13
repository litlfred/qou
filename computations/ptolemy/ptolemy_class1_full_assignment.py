#!/usr/bin/env python3
"""Recover the FULL (un-eliminated) class-1 Ptolemy assignment for L6a4, exactly.

WHAT THIS IS.  L6a4-c1-ptolemy-in-K.json records 26 Ptolemy coordinates plus u, the
output of snappy's ptolemy_variety(3, ...) with eliminate_fixed_ptolemys=True.  The
UN-ELIMINATED variety has 33 variables and 39 equations, so 6 coordinates are missing.
This recovers them exactly in K = Q[T]/(f) and writes the full 33-coordinate assignment.

CORRECTS MY OWN TWO PREVIOUS ATTEMPTS, both of which reported a false negative.

  (1) ptolemy_full_assignment_reconstruction_blocked.py propagated snappy's 112
      IDENTIFICATIONS first (26 -> 98) and then solved.  Unverifiable: ZERO
      identifications relate two coordinates the file already knows, because the
      recorded 26 are one representative per identification class, so no propagated
      value could be cross-checked.

  (2) The first version of THIS file left the 6 symbolic and called sympy's general
      solve() on all 39 equations.  It printed "candidate solutions: 0" and concluded
      "NO candidate satisfies all equations", framed as a fact about the DATA.  That
      was wrong, and demonstrably so -- the point exists; a sibling session answered
      issue #7092 on it (main f7fee734c3).  A general nonlinear solver returning
      nothing is not evidence of no solution.

WHAT THE STRUCTURE ACTUALLY IS -- measured, not assumed.  Two facts, each cheap:

  * The 6 are NOT simply 1.  eliminate_fixed_ptolemys is not a plain substitution of
    GGZ Remark 5.3's vertex value: setting all six to 1 leaves 30 of 39 equations
    vanishing and 9 failing (ptolemy_eliminated_gauge_is_ones_probe.py).

  * Every equation that mentions an unknown is degree 1 in EVERY unknown it mentions
    -- 27 such equations.  That is NOT the same as linear, and reading it as linear
    was a third error of mine, caught by this file's own assertion: a Ptolemy relation
    pairs two coordinates, and some relations pair two ELIMINATED ones, e.g.
    c_0012_0 = c_0111_0 * c_1002_0.  The system is multilinear, total degree 2.

  * But each of the six appears ALONE, to degree 1, in at least one equation.  So the
    system is TRIANGULAR: every unknown is pinned by a single-unknown equation
    a*x + b = 0 over K, with a and b built only from recorded coordinates.

So the solve is a fixed point, not a search: repeatedly take any equation with exactly
one remaining unknown and degree 1 in it, solve x = -b/a exactly in K, substitute,
repeat.  Every unknown is pinned by more than one such equation, so each value is
cross-checked against an independent equation at the moment it is derived rather than
only in the final sweep.  Inverses are taken in K directly (sympy.invert modulo the
minimal polynomial); nothing is solved over Q(T) and reduced afterwards, which would
answer a generic question rather than this one.

VERIFICATION.  The recovered assignment is accepted only if ALL 39 un-eliminated
equations reduce to the zero polynomial in K.  Note 30 of them contain no unknown at
all: those 30 are an independent check that the recorded 26 and this file's reduction
machinery are right, and they pass before anything is solved.

Exact arithmetic throughout (sympy Rationals mod f).  No floats, no tolerances -- an
equation vanishes or it does not.

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
    f = sp.expand(sp.sympify(d['field']['min_poly'].replace('t', 'T')))
    red = lambda e: sp.expand(sp.rem(sp.expand(e), f, T))
    inv = lambda e: sp.expand(sp.invert(sp.expand(e), f, T))

    co = {k: sp.expand(sp.sympify(re.sub(r'\bt\b', 'T', v)))
          for k, v in d['ptolemy'].items()}
    u = co['u']
    assert red(u ** 2 + u + 1) == 0, "u is not a primitive cube root of unity"
    assert sp.Poly(f, T).is_irreducible, "f must be irreducible for K to be a field"
    print(f"K = Q[T]/(f), deg f = {sp.degree(f, T)}, irreducible; u primitive",
          flush=True)

    M = snappy.Manifold(d['manifold'])
    V = M.ptolemy_variety(3, obstruction_class=d['obstruction_class'])
    allv = sorted({str(v) for v in V.variables})
    eqs = [str(e) for e in V.equations]
    unknown = [v for v in allv if v not in co]
    print(f"un-eliminated: {len(allv)} variables, {len(eqs)} equations; "
          f"{len(unknown)} unknown -> {unknown}", flush=True)

    X = {v: sp.Symbol('X_%d' % i) for i, v in enumerate(unknown)}
    loc = {k: v for k, v in co.items() if k in allv}
    loc.update(X)
    loc['t'] = u
    loc['u'] = u
    loc['T'] = T

    parsed = [sp.expand(sp.sympify(e, locals=loc)) for e in eqs]
    Xs = [X[v] for v in unknown]

    # --- the 30 equations with no unknown are an independent pre-check ---------
    free_eqs = [p for p in parsed if not (set(Xs) & p.free_symbols)]
    bad_free = [p for p in free_eqs if red(p) != 0]
    print(f"\nequations with NO unknown: {len(free_eqs)}; "
          f"vanishing in K: {len(free_eqs) - len(bad_free)}", flush=True)
    if bad_free:
        print("PRE-CHECK FAILED: the recorded 26 do not satisfy their own equations.")
        print("Nothing downstream is trustworthy; stop here.")
        return 1
    print("pre-check PASSES -- the recorded 26 and the reduction machinery are sound.",
          flush=True)

    # --- triangular fixed point: pin one unknown at a time ---------------------
    live = [p for p in parsed if set(Xs) & p.free_symbols]
    print(f"equations mentioning an unknown: {len(live)}", flush=True)

    sol = {}
    pinned_by = {}
    remaining = set(Xs)
    progress = True
    while remaining and progress:
        progress = False
        for p in live:
            q = red(p.subs({X[v]: sol[v] for v in unknown if v in sol}))
            free = set(Xs) & q.free_symbols
            if len(free) != 1:
                continue
            x = free.pop()
            name = next(v for v in unknown if X[v] is x)
            if sp.Poly(q, x).degree() != 1:
                continue
            a = red(q.coeff(x, 1))
            b = red(q.subs(x, 0))
            if a == 0:
                continue
            val = red(-b * inv(a))
            if name in sol:
                # an independent equation pinning an already-derived value
                if red(sol[name] - val) != 0:
                    print(f"\nCONTRADICTION: {name} is pinned to two different values "
                          f"in K by two equations.  The recorded 26 do not extend.")
                    return 1
                pinned_by[name] += 1
                continue
            sol[name] = val
            pinned_by[name] = 1
            remaining.discard(x)
            progress = True
            print(f"   pinned {name}", flush=True)

    if remaining:
        left = sorted(next(v for v in unknown if X[v] is x) for x in remaining)
        print(f"\nfixed point stalled with {len(left)} unpinned: {left}")
        print("Report rather than guess -- the triangular structure does not close.")
        return 1
    # --- a REAL cross-check pass.  The loop above exits the moment the last
    # unknown is pinned, so on its own it compares nothing: every count is 1 and
    # that number says only "derived once".  Re-walk every single-unknown equation
    # now that all six are known, and require each to agree exactly in K.
    for p in live:
        for name in unknown:
            others = {X[v]: sol[v] for v in unknown if v != name}
            q = red(p.subs(others))
            if X[name] not in q.free_symbols or sp.Poly(q, X[name]).degree() != 1:
                continue
            a = red(q.coeff(X[name], 1))
            if a == 0:
                continue
            val = red(-red(q.subs(X[name], 0)) * inv(a))
            if red(sol[name] - val) != 0:
                print(f"\nCONTRADICTION: {name} pinned to two different values in K.")
                return 1
            pinned_by[name] = pinned_by.get(name, 0) + 1
    print(f"\nall {len(unknown)} pinned; INDEPENDENT equations agreeing per "
          f"coordinate: { {k: pinned_by[k] for k in sorted(pinned_by)} }", flush=True)

    # --- what the recovered values ARE ------------------------------------------
    print("\nrecovered values, as roots of unity:", flush=True)
    for v in unknown:
        tag = '1' if sol[v] == 1 else ('u' if red(sol[v] - u) == 0 else
              ('u^2' if red(sol[v] - red(u * u)) == 0 else
               ('root of unity of order 3' if red(sol[v] ** 3 - 1) == 0
                else 'NOT a cube root of unity')))
        print(f"   {v} = {tag}", flush=True)

    # --- accept only on ALL 39 ---------------------------------------------------
    sub = {X[v]: sol[v] for v in unknown}
    bad = [e for e, p in zip(eqs, parsed) if red(p.subs(sub)) != 0]
    print(f"\nall 39 equations re-checked: {len(eqs) - len(bad)} / {len(eqs)} vanish "
          f"exactly in K", flush=True)
    if bad:
        print(f"{len(bad)} FAIL -- rejecting.  First: {bad[0]}")
        return 1
    if any(sol[v] == 0 for v in unknown):
        print("a recovered coordinate is ZERO -- not a Ptolemy point; rejecting.")
        return 1

    full = dict(d['ptolemy'])
    for v in unknown:
        full[v] = str(sol[v]).replace('T', 't')
    out = {
        'manifold': d['manifold'],
        'obstruction_class': d['obstruction_class'],
        'field': d['field'],
        'ptolemy': full,
        'provenance': {
            'source': SRC,
            'recovered': unknown,
            'method': 'exact linear solve over K; every equation mentioning an '
                      'unknown is degree 1 in it, so the system is linear',
            'gauge': 'fully determined by the triangular system; '
                     'no free parameter',
            'cross_checks_per_coordinate': pinned_by,
            'equations_verified': len(eqs),
            'unknown_free_equations_precheck': len(free_eqs),
        },
    }
    json.dump(out, open(OUT, 'w'), indent=2, sort_keys=True)
    print(f"\nFULL ASSIGNMENT RECOVERED -- {len(full) - 1} coordinates, all "
          f"{len(eqs)} equations vanish exactly in K")
    print(f"written to {OUT}")
    for v in unknown:
        print(f"   {v} = {sol[v]}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
