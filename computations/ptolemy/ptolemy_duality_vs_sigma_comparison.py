"""Does DUALITY equal the SIGMA-TRANSPORT?  INCONCLUSIVE -- and the reason is the point.

THE TEST.  On {2,1,0,0}-shaped indices duality is the relabelling pi (entrywise 1<->2,
0 and 3 fixed).  The sigma-transport sends each coordinate to its Galois conjugate.  If
the two maps agree then sigma(x_t) = x_{pi(t)} up to gauge, on the same tetrahedron.
Both sides are exactly computable: sigma from ptolemy_class1_galois_group.py, x from
L6a4-c1-ptolemy-in-K.json.

THE RESULT, AND WHY IT DECIDES NOTHING.

    sigma_0 and sigma_1 alike:
        c_1002_5, c_2001_5   ratio exactly 1
        c_1002_1, c_2001_1   ratio not a root of unity
        c_1002_3, c_2001_3   ratio not a root of unity
        5 of 11 coordinates had no pi-partner present at all

That is STRUCTURED -- tetrahedron 5 agrees exactly, tetrahedra 1 and 3 do not -- but it
is NOT a refutation, because a Ptolemy assignment is only defined up to GAUGE.  Rescaling
the decoration at each vertex sends c_t -> (prod_i lambda_{v_i}^{t_i}) c_t, so ratios
legitimately vary coordinate by coordinate and need NOT be roots of unity.  A ratio of 1
on one tetrahedron and not on another is exactly what a non-trivial gauge looks like.

Three further reasons the test cannot decide:

  1. The recorded point comes from `eliminate_fixed_ptolemys=True`, which IS ALREADY a
     gauge choice -- and snappy may make a different one for P^c and for P^-c.
  2. Only 6 of 11 {2,1,0,0} coordinates have their pi-partner present; the other 5 were
     eliminated.
  3. The first version compared up to +-1.  That is the SL(2) gauge; for SL(3) the gauge
     is mu_3.  Testing +- and calling the rest disagreement was too rigid by construction.

THE OPPOSITE HAZARD, stated so it is not walked into.  With per-vertex gauge freedom,
ANY discrepancy can be attributed to gauge, which would make "duality = sigma-transport"
unfalsifiable.  That is not an argument for it.  The falsifiable form of the question is
whether the observed ratio is a COBOUNDARY: do vertex scalars lambda exist with
ratio(t) = prod lambda_{v_i}^{t_i}?  That is a definite yes/no and it needs snappy's
vertex-incidence data, which this probe does not pull.

SO: bean qou-qjhc stays OPEN, and this file records an inconclusive test rather than a
result.  Reporting the six mismatches as a refutation would have been wrong in exactly
the direction this corpus keeps paying for.

Exact arithmetic in K = Q[T]/(f) throughout; no floats, no tolerances.
"""
import json, re, warnings; warnings.filterwarnings('ignore')
import sympy as sp
T = sp.Symbol('T')
d = json.load(open('computations/ptolemy/L6a4-c1-ptolemy-in-K.json'))
f = sp.sympify(d['field']['min_poly'].replace('t','T'))
red = lambda e: sp.expand(sp.rem(sp.expand(e), f, T))
co = {k: sp.expand(sp.sympify(re.sub(r'\bt\b','T',v))) for k,v in d['ptolemy'].items()}

SIG = [sp.sympify("-64*T**3/101015625 - T + 760000/1293"),
       sp.sympify("-T**3/625000 + 19*T**2/8000 - 1293*T/512 + 11875/8")]
u2 = co['u']; u1 = red(-1-u2)
for i, g in enumerate(SIG):
    assert red(f.subs(T, g)) == 0, f"sigma_{i} is not an automorphism"
    assert red(u1.subs(T, g) - u2) == 0, f"sigma_{i} does not invert zeta_3"
print("both sigma verified: automorphism of K, inverts zeta_3\n")

def sig(x, g): return red(sp.expand(x).subs(T, g))
SWAP = {0:0, 1:2, 2:1, 3:3}
pat = re.compile(r'^c_(\d)(\d)(\d)(\d)_(\d+)$')

rows = []
for name in co:
    m = pat.match(name)
    if not m: continue
    t = tuple(int(m.group(i)) for i in range(1,5)); tet = m.group(5)
    if sorted(t) != [0,0,1,2]: continue           # the shape where duality relabels
    pt = tuple(SWAP[x] for x in t)
    partner = f"c_{''.join(map(str,pt))}_{tet}"
    rows.append((name, partner, partner in co))
print(f"{{2,1,0,0}}-shaped coordinates present: {len(rows)}")
print(f"   of which the pi-partner is also present: {sum(1 for _,_,ok in rows if ok)}\n")

for si, g in enumerate(SIG):
    agree = disagree = missing = 0
    ex = []
    for name, partner, ok in rows:
        if not ok: missing += 1; continue
        lhs = sig(co[name], g); rhs = co[partner]
        if red(lhs - rhs) == 0 or red(lhs + rhs) == 0: agree += 1
        else:
            disagree += 1
            if len(ex) < 3: ex.append((name, partner))
    print(f"sigma_{si}:  agree {agree}   DISAGREE {disagree}   partner-absent {missing}")
    for a,b in ex: print(f"     e.g. sigma({a}) != +-{b}")
print("\nreading: agreement on all testable coordinates would be strong evidence that")
print("duality IS the sigma-transport; any disagreement refutes the identification")
print("in the naive coordinate-matching form.")

print("\n" + "="*70)
print("REFINEMENT: a Ptolemy assignment is defined only up to GAUGE -- rescaling the")
print("decoration at each vertex.  For SL(3) that gauge group is mu_3, the very group")
print("the obstruction class lives in.  So sigma(x_t) = zeta * x_pi(t) with zeta a cube")
print("root of unity is AGREEMENT, not disagreement.  What are the ratios?")
for si, g in enumerate(SIG):
    print(f"\nsigma_{si}: ratios sigma(x_t) / x_pi(t)")
    for name, partner, ok in rows:
        if not ok: continue
        lhs = sig(co[name], g); rhs = co[partner]
        if red(rhs) == 0: print(f"   {name:14s} partner is ZERO"); continue
        # ratio in K: solve rhs * r = lhs for r in K
        r0,r1,r2,r3 = sp.symbols('r0 r1 r2 r3')
        R = r0 + r1*T + r2*T**2 + r3*T**3
        sol = sp.solve(sp.Poly(red(sp.expand(rhs*R) - lhs), T).all_coeffs(), [r0,r1,r2,r3], dict=True)
        if not sol: print(f"   {name:14s} -> no ratio in K"); continue
        rr = sp.expand(R.subs(sol[0]))
        cube = red(rr**3 - 1) == 0
        one  = red(rr - 1) == 0
        mone = red(rr + 1) == 0
        tag = ("1" if one else "-1" if mone else
               "PRIMITIVE CUBE ROOT of unity" if cube else "not a root of unity")
        print(f"   {name:14s} -> {tag}")
