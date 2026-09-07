"""DERIVED (not fitted): c*_1110 * c_0111 is a 3x3 determinant of Ptolemy coordinates.

THE ANSWER to what duality does on the {1,1,1,0} coordinates, where it is not a
relabelling (see ptolemy_duality_index_map_probe.py).

DERIVATION.  With the w0 twist {g^{-T}w0}_1 = ({g}_2)^perp, so for n = 3 that line is
spanned by v_1 x v_2, and c*_1110 = det(A, C, E) with A = a^b, C = c^d, E = e^f regarded
as covectors via Lambda^2 V = V*.  For covectors there is the exact identity

    det(A,C,E) * det(x,y,z) = det( <A,x> <A,y> <A,z> ; <C,...> ; <E,...> ),
    where  <A,x> = det(a,b,x).

Choose x,y,z to be the FIRST COLUMNS of g1, g2, g3 (call them c, e, g).  Then every
pairing is a Ptolemy coordinate, and det(x,y,z) = det(c,e,g) = c_0111:

    <A,c>=c_2100   <A,e>=c_2010   <A,g>=c_2001
    <C,c>=0        <C,e>=c_0210   <C,g>=c_0201
    <E,c>=c_0120   <E,e>=0        <E,g>=c_0021

Two zeros fall out for free: C annihilates c, and E annihilates e.  Hence

    c*_1110 * c_0111 = det [[c_2100, c_2010, c_2001],
                            [0,      c_0210, c_0201],
                            [c_0120, 0,      c_0021]]

CONFIRMED 300/300 on SL(3) decorations, 0 refutations, with GGZ (5.2) gated at 0/100
violations on the same samples.

NOTHING HERE IS FITTED.  The identity is written down from the Plucker pairing and then
checked.  No hypothesis class is searched, no coefficient is solved for, no object is
selected because it matched.

WHY IT MATTERS THAT THE BIDEGREE IS (1,3).  The companion probe
ptolemy_duality_1110_not_rational_probe.py searched bidegree (2,2) exhaustively and found
nothing -- correctly, since a (2,2) space cannot contain a (1,3) relation.  So that
negative was sound and its ORIGINAL HEADLINE ("out of the coordinate ring") over-read it.
An exhaustive search at one bidegree is silent about every other, and the derivation --
not a wider search -- is what settled it.

Exact integer arithmetic modulo a Mersenne prime; no floats, no tolerances.
"""
import itertools, random
p = (1 << 61) - 1
def det3(M):
    (a,b,c),(d,e,f),(g,h,i) = M
    return (a*(e*i-f*h) - b*(d*i-f*g) + c*(d*h-e*g)) % p
def hs(cols): return [[cols[j][i] for j in range(3)] for i in range(3)]
def cross(u,v):
    return [(u[1]*v[2]-u[2]*v[1])%p,(u[2]*v[0]-u[0]*v[2])%p,(u[0]*v[1]-u[1]*v[0])%p]
idx = [t for t in itertools.product(range(4), repeat=4) if sum(t)==3]
def sample(rnd):
    while True:
        G=[[[rnd.randrange(p) for _ in range(3)] for _ in range(3)] for _ in range(4)]
        if not all(det3(g)%p for g in G): continue
        for g in G:
            inv=pow(det3(g),p-2,p)
            for i in range(3): g[i][0]=(g[i][0]*inv)%p
        Gc=[[[g[i][j] for i in range(3)] for j in range(3)] for g in G]; break
    c={t:det3(hs([Gc[i][k] for i in range(4) for k in range(t[i])])) for t in idx}
    st=det3(hs([cross(Gc[0][0],Gc[0][1]),cross(Gc[1][0],Gc[1][1]),cross(Gc[2][0],Gc[2][1])]))
    return c, st

def add(a,b): return tuple(x+y for x,y in zip(a,b))
rnd=random.Random(2718); gate=0
for _ in range(25):
    c,_s=sample(rnd)
    for s in [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]:
        if (c[add(s,(1,0,0,1))]*c[add(s,(0,1,1,0))]+c[add(s,(1,1,0,0))]*c[add(s,(0,0,1,1))]-
            c[add(s,(1,0,1,0))]*c[add(s,(0,1,0,1))])%p: gate+=1
print(f"validity gate -- Ptolemy relation violations: {gate} of 100")
assert gate==0

T=lambda k: tuple(int(x) for x in k)
ok=bad=0; rnd2=random.Random(1618)
for _ in range(300):
    c, st = sample(rnd2)
    M=[[c[T("2100")], c[T("2010")], c[T("2001")]],
       [0,            c[T("0210")], c[T("0201")]],
       [c[T("0120")], 0,            c[T("0021")]]]
    if (st*c[T("0111")] - det3(M)) % p == 0: ok+=1
    else: bad+=1
print(f"\nDERIVED IDENTITY  c*_1110 * c_0111 = det[[c_2100,c_2010,c_2001],[0,c_0210,c_0201],[c_0120,0,c_0021]]")
print(f"   confirmed on {ok} samples, refuted on {bad}")
print("   " + ("HOLDS -- derived, then checked.  bidegree (1,3)."
               if bad==0 else "FAILS -- the derivation is wrong somewhere (signs?)."))
