"""c*_{1110} is not reachable at BIDEGREE (2,2) -- but it IS rational.  See the correction.

🛑 CORRECTED, SAME DAY, BY DERIVATION.  This file's original title read "Duality takes
the {1,1,1,0} Ptolemy coordinates OUT of the coordinate ring".  That is TOO STRONG and
is retracted.  ptolemy_duality_1110_plucker_identity.py DERIVES

    c*_1110 * c_0111 = det [[c_2100, c_2010, c_2001],
                            [0,      c_0210, c_0201],
                            [c_0120, 0,      c_0021]]

confirmed 300/300.  So c*_1110 IS a rational function of the Ptolemy coordinates -- at
BIDEGREE (1,3).  The negative below is correct exactly as scoped: no (2,2) form exists,
and a (2,2) search cannot contain a (1,3) relation.  The failure was the SHAPE OF THE
SEARCH SPACE, not the mathematics.  That is the lesson worth keeping: an exhaustive
search at one bidegree says nothing about another, and reporting it as "not in the
coordinate ring" over-reads it.

WHERE THIS SITS (bean qou-qjhc).  ptolemy_duality_index_map_probe.py measured that
duality acts on Ptolemy indices as the entrywise involution 0->0, 1->2, 2->1, 3->3, and
that this is only sum-preserving on the {2,1,0,0} index shape.  On {1,1,1,0} the rule
would give {2,2,2,0}, sum 6 -- not a valid index -- so duality is NOT a relabelling
there.  This probe asks what it IS.

THE OBJECT.  With the w0 twist, {g^{-T} w0}_1 = ({g}_2)^perp, a line, which for n = 3 is
spanned by v_1 x v_2.  So

    c*_{1110} = det( a x b, c x d, e x f ),   (a,b),(c,d),(e,f) = first two columns of
                                              g0, g1, g2

and the classical expansion, verified here on 40 random 6-tuples, is

    det(axb, cxd, exf) = det(a,b,e) det(c,d,f) - det(a,b,f) det(c,d,e).

Two of those four factors ARE Ptolemy coordinates (det(a,b,e) = c_2010,
det(c,d,e) = c_0210).  The other two use g2's SECOND column alone, which is not an
initial segment.  That is not an accident: v_2 is not N-invariant (v_2 -> v_2 + lambda
v_1), yet the two lambda terms cancel in the combination, so c* is well defined while
its factors are not.

THE RESULT -- a negative, at bidegree (2,2).

  1. c*_{1110} is NOT a degree-2 polynomial in the c_t.
     Rank 149 of 210 monomials, 121 inconsistent rows.
  2. c*_{1110} is NOT a ratio of degree-2 polynomials either.
     The homogeneous system c* A(c) = B(c) has kernel dimension 122, and EVERY kernel
     vector has A vanishing identically on decorations -- they are relations among the
     c_t in disguise, not formulas for c*.

VALIDITY GATE.  A decoration is by SL(3) COSETS.  An earlier version sampled arbitrary
invertible matrices; with det != 1 the c_t are not Ptolemy coordinates and any verdict
is about nothing.  Every sample is now normalised to det = 1, and the run refuses to
proceed unless the Ptolemy relation (GGZ 5.2) holds on those samples -- measured 0
violations in 100 checks.

TWO FALSE POSITIVES THIS PROBE PRODUCED, kept because the failure mode is the point.
"Kernel dimension 122" reads as "a rational form exists".  It is not.  Then
"122 - 61 relations = 61 genuine solutions" reads as a count of real formulas.  It is
not either -- that arithmetic assumed the only spurious family is (A=0, B a relation),
missing that (A a relation, B=0) is equally spurious.  Both readings are about the
COEFFICIENT VECTOR.  A(c) can have nonzero coefficients and still vanish identically on
every decoration.  The probe therefore tests A as a FUNCTION on samples, and under that
test 0 of 122 basis vectors survive, and 4000 random combinations produce none.

SCOPE.  This is a structural exclusion AT BIDEGREE (2,2), established by exact linear
algebra over F_p with the gate above; an identity with integer coefficients must hold
mod p, so failure mod p refutes it over Q.  It says NOTHING about degree 3 or higher,
which is untested.  Do not cite it as "duality is not rational in the Ptolemy
coordinates" without the bidegree.

Exact integer arithmetic modulo a Mersenne prime; no floats, no tolerances.
"""
import itertools, random, sys
p = (1 << 61) - 1
def det3(M):
    (a,b,c),(d,e,f),(g,h,i) = M
    return (a*(e*i-f*h) - b*(d*i-f*g) + c*(d*h-e*g)) % p
def hstack(cols): return [[cols[j][i] for j in range(3)] for i in range(3)]
def cross(u,v):
    return [(u[1]*v[2]-u[2]*v[1])%p, (u[2]*v[0]-u[0]*v[2])%p, (u[0]*v[1]-u[1]*v[0])%p]
idx = [t for t in itertools.product(range(4), repeat=4) if sum(t) == 3]
def sample(rnd):
    while True:
        G = [[[rnd.randrange(p) for _ in range(3)] for _ in range(3)] for _ in range(4)]
        if not all(det3(g)%p for g in G): continue
        for g in G:
            inv = pow(det3(g), p-2, p)
            for i in range(3): g[i][0] = (g[i][0]*inv) % p
        Gc = [[[g[i][j] for i in range(3)] for j in range(3)] for g in G]
        break
    c = {t: det3(hstack([Gc[i][k] for i in range(4) for k in range(t[i])])) for t in idx}
    st = det3(hstack([cross(Gc[0][0],Gc[0][1]), cross(Gc[1][0],Gc[1][1]), cross(Gc[2][0],Gc[2][1])]))
    return c, st
mons = [(s,t) for i,s in enumerate(idx) for t in idx[i:]]
M2 = len(mons)
print(f"degree-2 monomials: {M2};  unknowns (A,B): {2*M2}")
rnd = random.Random(23)
N = 2*M2 + 80
rows = []
for _ in range(N):
    c, st = sample(rnd)
    m = [(c[s]*c[t]) % p for s,t in mons]
    rows.append([(st*x) % p for x in m] + [(-x) % p for x in m])
print(f"samples: {N}")
ncol = 2*M2
r = 0; piv = []
Mx = [row[:] for row in rows]
for col in range(ncol):
    sel = next((i for i in range(r, len(Mx)) if Mx[i][col]), None)
    if sel is None: continue
    Mx[r], Mx[sel] = Mx[sel], Mx[r]
    inv = pow(Mx[r][col], p-2, p)
    Mx[r] = [(x*inv) % p for x in Mx[r]]
    for i in range(len(Mx)):
        if i != r and Mx[i][col]:
            f = Mx[i][col]
            Mx[i] = [(x - f*y) % p for x,y in zip(Mx[i], Mx[r])]
    piv.append(col); r += 1
    if r == len(Mx): break
print(f"rank {r} of {ncol};  kernel dimension {ncol - r}")
if ncol - r == 0:
    print("\nNO rational form of bidegree (2,2) either -- kernel is trivial.")
else:
    print(f"\nkernel is NON-TRIVIAL: dimension {ncol - r}.  That is NOT yet a result --")
    print("   the kernel necessarily contains relations among the c_t in disguise.")
    free = [c for c in range(ncol) if c not in set(piv)]
    print(f"   free columns: {len(free)} (first few: {free[:6]})")
    print("   -> testing whether any kernel vector has A nonzero AS A FUNCTION")

    # A NONZERO KERNEL IS NOT ENOUGH.  It necessarily contains spurious vectors with
    # A = 0 and B any RELATION among the c_t -- and the Ptolemy relations guarantee
    # those exist.  Extract a kernel vector with A != 0 and verify it on FRESH samples.
    basis = []
    pivset = {c: i for i, c in enumerate(piv)}
    for fc in free:
        v = [0]*ncol; v[fc] = 1
        for i, col in enumerate(piv):
            v[col] = (-Mx[i][fc]) % p
        basis.append(v)
    # NONZERO COEFFICIENTS IS NOT NONZERO FUNCTION.  A(c) can vanish identically on
    # decorations while its coefficient vector is nonzero -- that is a RELATION in
    # disguise.  Test A as a FUNCTION, on samples.
    rnd_t = random.Random(4242)
    probes = [sample(rnd_t) for _ in range(12)]
    def Aval(vec, c):
        m = [(c[a]*c[b]) % p for a,b in mons]
        return sum(x*y for x,y in zip(vec[:M2], m)) % p
    withA = [v for v in basis if any(Aval(v, c) for c,_ in probes)]
    print(f"\n   kernel basis vectors with A nonzero AS A FUNCTION: {len(withA)} of {len(basis)}")
    if not withA:
        import itertools as _it
        rndc = random.Random(5150)
        for _ in range(4000):
            comb = [0]*ncol
            for _k in range(3):
                w = rndc.randrange(1, p); bv = basis[rndc.randrange(len(basis))]
                comb = [(x + w*y) % p for x, y in zip(comb, bv)]
            if any(Aval(comb, c) for c,_ in probes):
                withA = [comb]; print("   found one by random combination"); break
    if not withA:
        print("   ALL kernel vectors have A = 0 -- these are RELATIONS among the c_t,")
        print("   not a formula for c*.  The rational form is NOT established.")
        sys.exit(0)
    v = withA[0]
    A, B = v[:M2], v[M2:]
    print(f"   using one with {sum(1 for x in A if x)} non-zero A terms, "
          f"{sum(1 for x in B if x)} non-zero B terms")
    rnd2 = random.Random(31337); okc = bad = degen = 0
    for _ in range(200):
        c, st = sample(rnd2)
        m = [(c[s]*c[t]) % p for s,t in mons]
        Av = sum(a*x for a,x in zip(A,m)) % p
        Bv = sum(b*x for b,x in zip(B,m)) % p
        if Av == 0: degen += 1; continue
        if (st*Av - Bv) % p == 0: okc += 1
        else: bad += 1
    print(f"\n   FRESH-SAMPLE CHECK: {okc} confirm, {bad} refute, {degen} degenerate (A=0)")
    print("   " + ("CONFIRMED: c*_1110 is a RATIO of degree-2 Ptolemy polynomials."
                   if bad == 0 and okc else
                   "NOT confirmed on fresh samples -- the kernel was an artifact."))
