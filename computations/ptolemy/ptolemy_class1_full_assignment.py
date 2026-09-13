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
    -- 27 such equations, all deg 1.  Each Ptolemy relation is a sum of products of
    two coordinates, and no relation pairs two eliminated coordinates, so the whole
    system is LINEAR in the 6.

So this is exact linear algebra over K, not a nonlinear solve, and it is settled by a
rank computation rather than by a search.  Gaussian elimination is done in K directly
(inverses via sympy.invert modulo the minimal polynomial); nothing is done over Q(T)
and reduced afterwards, which would answer a generic question rather than this one.

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

    # --- build the linear system A x = b over K --------------------------------
    live = [p for p in parsed if set(Xs) & p.free_symbols]
    A, b = [], []
    for p in live:
        poly = sp.Poly(p, *Xs)
        for mon in poly.monoms():
            assert max(mon) <= 1 and sum(mon) <= 1, \
                f"equation is not linear in the unknowns: {p}"
        row = [red(p.coeff(x, 1)) for x in Xs]
        const = red(p.subs({x: 0 for x in Xs}))
        A.append(row)
        b.append(red(-const))
    print(f"linear system over K: {len(A)} equations, {len(Xs)} unknowns; "
          f"homogeneous: {all(c == 0 for c in b)}", flush=True)

    # --- Gaussian elimination in K ---------------------------------------------
    n = len(Xs)
    rows = [list(r) + [bb] for r, bb in zip(A, b)]
    piv_col = []
    r = 0
    for c in range(n):
        p = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        s = inv(rows[r][c])
        rows[r] = [red(x * s) for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                fac = rows[i][c]
                rows[i] = [red(a - fac * bb) for a, bb in zip(rows[i], rows[r])]
        piv_col.append(c)
        r += 1
        if r == len(rows):
            break
    rank = len(piv_col)
    free_col = [c for c in range(n) if c not in piv_col]
    incons = [i for i in range(rank, len(rows))
              if all(x == 0 for x in rows[i][:n]) and rows[i][n] != 0]
    print(f"rank {rank} / {n}; free columns {[unknown[c] for c in free_col]}; "
          f"inconsistent rows: {len(incons)}", flush=True)
    if incons:
        print("\nThe system is INCONSISTENT over K: the recorded 26 do not extend.")
        print("That is a real finding about the artifact, not a solver artifact --")
        print("the 30 unknown-free equations already passed.")
        return 1

    # --- solve; a free column is the residual decoration gauge -----------------
    if len(free_col) > 1:
        print(f"\n{len(free_col)} free columns -- the solution is not determined up to")
        print("a single scale.  Report rather than pick one.")
        return 1
    sol = {}
    if free_col:
        fc = free_col[0]
        print(f"\none free column: {unknown[fc]} is the residual gauge; "
              f"normalising it to 1.", flush=True)
        sol[unknown[fc]] = sp.Integer(1)
        for i, c in enumerate(piv_col):
            sol[unknown[c]] = red(rows[i][n] - rows[i][fc])
    else:
        for i, c in enumerate(piv_col):
            sol[unknown[c]] = red(rows[i][n])

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
            'gauge': ('one free column, normalised to 1'
                      if free_col else 'determined, no free column'),
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
