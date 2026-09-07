"""What does DUALITY do to a Ptolemy index?  Measured on generic decorations.

THE QUESTION (bean qou-qjhc).  PtolemyTwist.lean proves that a ring map inverting the
cube root of unity carries P^c to P^-c, and ptolemy_galois_point_transport.py confirms
an exact class-1 point crosses.  What is NOT established is that the DUALITY involution
rho -> rho^{-T} is the map doing it.  This probe attacks the first half of that: what
duality does to Ptolemy coordinates at all.

THE SETUP, from the primary source.  GGZ (arXiv:1207.6711) Lemma 8.8 defines

    c_t = det( {g0}_{t0} u {g1}_{t1} u {g2}_{t2} u {g3}_{t3} ),    sum t_i = n,

where {g}_i is the first i COLUMNS of the decoration matrix g.  Duality sends g -> g^{-T},
whose columns are the DUAL BASIS to those of g (w_i^T v_j = (g^-1 g)_ij = delta_ij), so
{g^{-T}}_k spans the annihilator of span(v_{k+1},...,v_n).  But g^{-T} carries upper-
unipotent N to LOWER-unipotent, so g^{-T}N is not a coset of G/N: the map must be
g -> g^{-T} w0 with w0 order-reversing, giving {g^{-T}w0}_k = ({g}_{n-k})^perp.

WHAT IS MEASURED.  Both Ptolemy assignments are computed on a generic decoration over Q
and the index pairs with |c*_t / c_s| = 1 are collected.  A ratio of 1 on ONE decoration
can be coincidence, so the run intersects the pairs over SIX independent decorations --
that intersection is what separates structure from luck, and it does: 1110 -> 0210
appears on a single decoration and does NOT survive.

THE RESULT.  Ten indices acquire a unique surviving partner, the map is an involution,
and every one of the ten obeys a single rule:

    0 -> 0,   1 -> 2,   2 -> 1,   3 -> 3      applied entrywise

For n = 3 the index shapes are {3,0,0,0}, {2,1,0,0} and {1,1,1,0}.  The rule preserves
sum t_i = 3 exactly on the middle shape (one 1 and one 2 exchange), which is the ten.
The vertex points {3,0,0,0} all equal 1 by GGZ Remark 5.3, so they are degenerate and
carry no information.  On {1,1,1,0} the rule would give {2,2,2,0}, sum 6 -- NOT A VALID
INDEX -- so those coordinates have no partner, and that is a fact about the map rather
than a gap in the measurement.

SO DUALITY IS NOT A RELABELLING OF THE WHOLE VARIETY.  It is one on the {2,1,0,0}
coordinates and provably cannot be on the {1,1,1,0} ones.  That is a partial negative and
it is the sharpest statement this probe supports.

WHAT THIS IS NOT.  Not a proof: six random generic decorations over Q are structural
evidence, not a theorem.  Not sign-resolved: det(w0) = -1 for n = 3, so the dual
decoration has determinant -1 and the |ratio| = 1 test is deliberately sign-blind -- the
index map stands, the signs are unnormalised.  And 2 of the 12 {2,1,0,0} indices drop out
where a coordinate vanishes on some decoration.

Exact rational arithmetic throughout; no floats, no tolerances.
"""
import itertools, random, warnings; warnings.filterwarnings('ignore')
import sympy as sp
n = 3
W0 = sp.Matrix([[0,0,1],[0,1,0],[1,0,0]])
idx = [t for t in itertools.product(range(n+1), repeat=4) if sum(t) == n]

def sl3(rnd):
    while True:
        M = sp.Matrix(3, 3, lambda i, j: sp.Rational(rnd.randint(-5, 5)))
        d = M.det()
        if d != 0:
            M[:, 0] = M[:, 0] / d
            return M

def ptolemy(dec, t):
    cols = [dec[i][:, k] for i in range(4) for k in range(t[i])]
    return sp.Matrix.hstack(*cols).det()

inter = None
for trial in range(6):
    rnd = random.Random(1000 + trial)
    G = [sl3(rnd) for _ in range(4)]
    D = [(g.inv().T) * W0 for g in G]
    c  = {t: sp.nsimplify(ptolemy(G, t)) for t in idx}
    cs = {t: sp.nsimplify(ptolemy(D, t)) for t in idx}
    nz = [t for t in idx if c[t] != 0 and cs[t] != 0]
    pairs = set()
    for t in nz:
        for s in nz:
            if sp.simplify(sp.Abs(cs[t] / c[s]) - 1) == 0:
                pairs.add((t, s))
    inter = pairs if inter is None else (inter & pairs)
    print(f"trial {trial}: {len(nz)} usable indices, {len(pairs)} ratio-1 pairs, "
          f"intersection now {len(inter)}", flush=True)

print(f"\npairs surviving ALL {6} decorations: {len(inter)}")
m = {}
for t, s in sorted(inter): m.setdefault(t, []).append(s)
for t in sorted(m):
    print(f"   {''.join(map(str,t))} -> {[''.join(map(str,s)) for s in m[t]]}")
uniq = {t: v[0] for t, v in m.items() if len(v) == 1}
print(f"\nindices with a UNIQUE surviving partner: {len(uniq)}")
inv = all(uniq.get(s) == t for t, s in uniq.items())
print(f"is that map an involution? {inv}")
if uniq:
    print("value-swap reading (does it swap the 1 and the 2, fixing zeros)?")
    for t, s in sorted(uniq.items()):
        pred = tuple({0:0, 1:2, 2:1, 3:3}[x] for x in t)
        print(f"   {''.join(map(str,t))} -> {''.join(map(str,s))}   "
              f"{'MATCHES 1<->2' if pred == s else 'differs from 1<->2 ('+''.join(map(str,pred))+')'}")
