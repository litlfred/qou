"""SUPERSEDED, and its headline was WRONG.  Kept for the one measurement that survives.

WHAT THIS FILE CLAIMED.  It was titled "BLOCKED: the coboundary test needs the
UN-eliminated assignment, which the recorded artifact cannot supply."  Both halves of
that are false, and each was refuted by a different piece of work:

  * The coboundary test does NOT need the un-eliminated assignment.  A sibling session
    answered issue #7092 on this very point (main f7fee734c3) by taking the integer
    kernel of the gauge exponent lattice -- which uses only the ELIMINATED coordinates,
    because a kernel relation forces prod_t r_t^{n_t} = 1 with no unknowns at all.
    Verdict there: sigma_b's ratio IS a PGL(3)-gauge coboundary on the class-1 point,
    sigma_a's is not.

  * The recorded artifact CAN supply the un-eliminated assignment.
    ptolemy_class1_full_assignment.py recovers all six missing coordinates exactly in
    K -- five 1s and one u^2 -- because the six-unknown system is TRIANGULAR (each
    appears alone, to degree 1, in several equations), each pinned by 6 to 10
    independent equations, all 39 verified.  The identifications are never needed.

So this route was not blocked by the data; it was blocked by ITSELF.  Propagating along
identifications first was the wrong move, and the diagnosis below correctly says why --
it just drew the wrong conclusion from it, generalising "my route cannot be verified"
into "the test cannot be run."  A route being unverifiable is a fact about the route.

THE MEASUREMENT THAT STANDS, and it is why propagation was the wrong move.  snappy's
_ptolemy_equations_identified_coordinates gives 112 relations, and propagating along them
takes 26 known coordinates to 98.  But:

    identifications relating TWO coordinates I already know:  0

The recorded 26 are exactly one REPRESENTATIVE PER IDENTIFICATION CLASS -- that is what
the elimination does.  So not one propagated value can be cross-checked against the file,
and an inconsistent solve downstream cannot be attributed to any cause: not to the
identifications being the UNTWISTED ones (snappy returns only +-1 factors, while a
nontrivial generalized obstruction class twists them by cube roots of unity), not to an
orientation convention on the sign, not to anything else.  Prefer a route whose own
equations are the check.

The {1,1,1,0} starvation count also stands as measured -- at most 2 of the 8 coordinates
that formula needs are present on ANY tetrahedron -- but it bounds only that formula, not
the coboundary test, and reading it as the latter is the error above.

TWO BUGS OF MY OWN ON THE WAY, both found by the solve returning 0:
  1. The first propagation ignored the sign field entirely -- 8 of the 112 relations
     carry -1.  With signs honoured, all 12 fully-determined equations pass (0 non-zero);
     the earlier "10 non-zero" was contamination from setting the unknowns to 1.
  2. 'u' -- the cube root of unity, which is KNOWN -- was left in the unknowns list,
     so it was simultaneously solved for and substituted.  6 unknowns, not 7.

Neither bug was the blocker, and neither was the unverifiability: the route simply
was not needed.  Both are still worth recording -- a solver returning 0 solutions was
the symptom every time, and three separate causes produced it.

THE FIX, and it is at the producer, not here.  Re-run the exact-point producer with
eliminate_fixed_ptolemys=False (or record BOTH forms), so the full assignment is on disk
rather than inferred.  Then the coboundary test is straightforward: build the ratio
vector, take the integer left-kernel of the 128 x 6 exponent matrix -- kernel vectors give
consistency conditions with NO unknowns at all -- and check prod r_t^{n_t} = 1.

Exact arithmetic in K throughout; no floats.
"""
import json, re, warnings, itertools; warnings.filterwarnings('ignore')
import sympy as sp, snappy
T = sp.Symbol('T')
d = json.load(open('computations/ptolemy/L6a4-c1-ptolemy-in-K.json'))
f = sp.sympify(d['field']['min_poly'].replace('t','T'))
red = lambda e: sp.expand(sp.rem(sp.expand(e), f, T))
co = {k: sp.expand(sp.sympify(re.sub(r'\bt\b','T',v))) for k,v in d['ptolemy'].items()}
u = co['u']
M = snappy.Manifold('L6a4')
Vfull = M.ptolemy_variety(3, obstruction_class=1)
ident = M._ptolemy_equations_identified_coordinates(3)
eqs = [str(e) for e in Vfull.equations]

def propagate(orient):
    val = {k: v for k, v in co.items() if k.startswith('c_')}
    for _ in range(60):
        ch = False
        for s0, s1, a, b in ident:
            a, b = str(a), str(b)
            sgn = sp.Integer(s0)
            # orient 0:  a = sgn * b     orient 1:  sgn * a = b
            if orient == 0:
                if a in val and b not in val: val[b] = red(val[a]/sgn); ch = True
                elif b in val and a not in val: val[a] = red(sgn*val[b]); ch = True
            else:
                if a in val and b not in val: val[b] = red(sgn*val[a]); ch = True
                elif b in val and a not in val: val[a] = red(val[b]/sgn); ch = True
        if not ch: break
    return val

for orient in (0, 1):
    val = propagate(orient)
    allv = sorted({str(v) for v in Vfull.variables})
    missing = [v for v in allv if v not in val and v not in ('t','u')]
    # count how many uneliminated equations are already satisfied on the KNOWN part
    sym = {k: sp.Symbol(k) for k in val}
    bad = ok = skip = 0
    for e in eqs:
        ex = sp.sympify(e.replace('^','**'), locals={**sym, 'u': sp.Symbol('u')})
        if set(map(str, ex.free_symbols)) - set(val) - {'u'}: skip += 1; continue
        r = red(sp.expand(ex.subs({sp.Symbol(k): v for k,v in val.items()}).subs(sp.Symbol('u'), u)))
        if r == 0: ok += 1
        else: bad += 1
    print(f"orientation {orient}: known {len(val)}, still-unknown vars {len(missing)}, "
          f"equations fully-determined {ok+bad} -> ok {ok}, NON-ZERO {bad}, skipped {skip}")

print("\nsolving the 7 remaining coordinates from the 27 equations that involve them")
val = propagate(0)
allv = sorted({str(v) for v in Vfull.variables})
missing = [v for v in allv if v not in val and v not in ('t','u')]
print("unknowns:", missing)
unk = {m_: sp.Symbol('X'+str(i)) for i, m_ in enumerate(missing)}
known = {sp.Symbol(k): v for k, v in val.items()}
polys = []
for e in eqs:
    ex = sp.sympify(e.replace('^','**'),
                    locals={**{k: sp.Symbol(k) for k in list(val)+missing}, 'u': sp.Symbol('u')})
    ex = ex.subs(known).subs(sp.Symbol('u'), u).subs({sp.Symbol(k): s for k, s in unk.items()})
    ex = sp.expand(ex)
    if ex.free_symbols & set(unk.values()):
        polys.append(ex)
print(f"equations in the unknowns: {len(polys)}")
sols = sp.solve(polys, list(unk.values()), dict=True)
print(f"solutions: {len(sols)}")
for si, s in enumerate(sols):
    full = dict(val); good = True
    for k, sym_ in unk.items():
        if sym_ not in s: good = False; break
        full[k] = red(s[sym_])
    if not good:
        print(f"  sol {si}: underdetermined"); continue
    bad = 0
    for e in eqs:
        ex = sp.sympify(e.replace('^','**'),
                        locals={**{k: sp.Symbol(k) for k in full}, 'u': sp.Symbol('u')})
        if red(sp.expand(ex.subs({sp.Symbol(k): v for k,v in full.items()}).subs(sp.Symbol('u'), u))) != 0:
            bad += 1
    print(f"  sol {si}: ALL {len(eqs)} equations -> non-zero {bad}"
          f"  {'FULL ASSIGNMENT RECOVERED' if bad == 0 else 'inconsistent'}")
    if bad == 0:
        json.dump({k: str(v) for k, v in full.items()}, open('/tmp/full_assignment.json','w'))
        print(f"     wrote /tmp/full_assignment.json  ({len(full)} coordinates)")
        break
