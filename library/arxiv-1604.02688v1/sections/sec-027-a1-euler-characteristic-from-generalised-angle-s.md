---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-027-a1-euler-characteristic-from-generalised-angle-s
section_title: "A.1. Euler characteristic from generalised angle structures"
section_number: null
pages: 51-55
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
shows how to compute the Euler characteristic of an embedded spun normal surface using
52 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, NEIL R. HOFFMAN, AND J. HYAM RUBINSTEIN
any generalised angle structure. This result is well-known for closed normal surfaces; see for
example [LT08, Lemma 15].
Proposition A.3. Let T be an ideal triangulation of a cusped 3-manifoldM, and letα :
□→ R be a generalised angle structure onT. Then the Euler characteristic of any embedded
spun normal surfaceS∈Q(T; R) is given by
χ(S) =−
∑
q
α(q)xq
π + ρα(∂S)
2π , (34)
where the sum is over all normal classesq in T, xq is the normal coordinate ofq, α(q)∈ R
denotes the angle assigned to the two edges facingq, and ρα(∂S) denotes the sum of the
rotational holonomies of the boundary components ofS, oriented as in[∂S].
This result follows from a combinatorial version of the Gauss-Bonnet theorem, as used by
Thurston in [Thu77, Section 13.7]. LetS be a compact surface, possibly with boundary and
let C be a cell decomposition ofS into ﬁnitely many polygons. Then aformal angle structure
(or combinatorial angle structure) on C is an assignment of real numbers (“angles”) to the
corners of the polygons such that the sum of angles is2π at each internal vertex.
We compute the Euler characteristic ofS as χ(S) = v−e +f, where v,e,f are the
numbers of vertices, edges and faces in the cell decomposition. Now eachn-gonP contributes
1
2π(sum of corner angles) tov, n× 1
2 = n/2 to e and 1 to f, so contributes alocal Euler
characteristic
χP = 1
2π(sum of corner angles inP)− n
2 + 1 (35)
to χ(S) =v−e +f.
Adding up the termsχP over all polygonsP gives a contribution toχ(S) of +1 for each
internal vertex,−1 for each internal edge and +1 for each face. Assume that there are
also k boundary vertices and, hence,k boundary edges. Then to obtainχ(S) we need to
add additional contributions of 1
2π(2π−θi) where θi is the sum of internal angles at theith
boundary vertex and−1/2 for each boundary edge. This gives
χ(S) =
∑
P
χP + 1
2π
k∑
i=1
(2π−θi)− k
2 =
∑
P
χP + 1
2π
k∑
i=1
(π−θi),
and last term
kg(∂S) =
k∑
i=1
(π−θi) (36)
represents thetotal geodesic curvatureof the boundary ofS. Hence
Proposition A.4(Combinatorial Gauss-Bonnet). LetS be a compact surface with a ﬁnite
cell decomposition C equipped with a formal angle structure. Then the Euler characteristic
of S is given by
χ(S) =
∑
P
χP + kg(∂S)
2π , (37)
summed over all polygonsP, whereχP is deﬁned by (35) and wherekg(∂S) denotes the total
geodesic curvature of∂S.
THE 3D-INDEX AND NORMAL SURF ACES 53
Proof of Proposition A.3.Let S be a (non-compact) embedded spun normal surface in T
and choose a compact subsurfaceS0 consisting of all quads and a ﬁnite number of normal
triangles such thatS\S0 is a collection of annuli spiralling out to the cusps ofM. By adding
an additional layer of triangles, if necessary, we can assume that there is a neighbourhood of
∂S0 consisting entirely of triangles. Projecting these normal triangles to a horosphere gives
a layer of Euclidean triangles to the left of the boundary, and the rotational holonomy of
∂S0 is the sum
ρα(∂S) =ρα(∂S0) =
k∑
i=1
(π−θi),
where θi is the sum of triangle angles at theith vertex on the boundary.
NowS0 has a cell decomposition into quads and triangles, and a generalised angle structure
α on T assigns an “angle” (inR) to each corner of each 2-cell in this decomposition, giving
a formal angle structure on this cell decomposition. Now each 2-cell gives a contribution to
the Euler characteristic as follows:
• Each quadq contributesχ(q) = 1
2π(angle sum)−1. But the sum of angles in the quad
is 2π minustwicetheangle α(q)onthetwoedgesfacing q, sowehave χ(q) =−α(q)/π.
• Each trianglet contributesχ(t) = 1
2π(angle sum)2− 3/2 + 1 = 0.
Hence the combinatorial Gauss-Bonnet theorem gives
χ(S) =χ(S0) =−
∑
q
α(q)xq
π + 1
2π
k∑
i=1
(π−θi) =−
∑
q
α(q)xq
π + ρα(∂S)
2π .
□
Since the boundary term vanishes for any angle structure with vanishing peripheral rota-
tional holonomy, this gives the following convenient way of computing the Euler character-
istic:
Corollary A.5.Let T be an ideal triangulation of a cusped 3-manifoldM, and letα : □→ R
be a generalised angle structure onT with vanishing peripheral rotational holonomy. Then
the Euler characteristic of any embedded spun normal surfaceS∈Q(T; R) is given by
χ(S) =−
∑
q
α(q)xq
π . (38)
Deﬁnition A.6.For a general Q-normal classS∈Q(T; R) we take the formula (34) as the
deﬁnition of theformal Euler characteristicofS. This is a linear functionχ :Q(T; R)→ R.
Remark A.7. The independence of choice of angle structure follows directly from [LT08,
Lemma 15]. For the angle structures in this paper,(A,κ ) = (0, 0) and ourα(q) is equal to
one half ofA(q) as in [LT08].
Another consequence of these results is
54 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, NEIL R. HOFFMAN, AND J. HYAM RUBINSTEIN
Corollary A.8. Each peripheral curve solution has vanishing formal Euler characteristic.
Hence
χ
(∑
i
xiEi +
∑
i
yjTj +
∑
k
(pkMk +qkLk)
)
=−
∑
i
2xi−
∑
j
yj, (39)
sinceχ(Ei) =−2 and χ(Tj) =−1.
Proof. Letα be a generalised angle structure onT, and letS be the peripheral curve solution
given by a curve with homology classc∈ H1(∂M ; Z). Then we have∂S = 2c (see Section
7.1). and, by deﬁnition,ρα(c) =∑
qα(q)xq where xq are the quad coordinates ofS. Hence
χ(S) =−
∑
q
α(q)xq
π + ρα(∂S)
2π =−ρα(c)
π + ρα(∂S)
2π = 0.
□
Remark A.9. We could also use the formula (39) to deﬁne the formal Euler characteristic of
a generalQ-normal classS∈Q(T; R).
Example A.10. For the ﬁgure eight knot complement with its triangulation given in Ex-
ample 4.1, the angle structure equations have general solution of the form
α = (α0 +t1α1 +t2α2 +t3α3)π, with ti∈ R
whereα0 = (−1, 2, 0, 1, 0, 0),α 1 = (2,−2, 0,−1, 0, 1),α 2 = (1,−1, 0,−1, 1, 0),α 3 = (1,−2, 1, 0, 0, 0).
This gives rotational holonomies for the meridian and longitude
ρα(M) = (−1 +t1 +t2 +t3)π and ρα(L) = (2− 4t1− 2t2)π.
Now there is an embedded spun normal once punctured Klein bottle with quad coordinates
K = (0, 0, 2, 0, 1, 0) with boundary∂K = 4µ + 1λ. The general formula (34) for the Euler
characteristic gives
χ(K) =−
∑
q
α(q)
π +ρα(∂S)
2π =− 1
πα·K+ 1
2πα·(4M +L) = (−t2−2t3)+(−1+t2+2t3) =−1
as expected.
Alternatively we can writeK = 2M + 1
2L + 1T2, henceχ(K) =−1 by formula (39).
In fact, ﬁnding angle structures can be seen as a dual problem to the existence of surfaces
of non-negative Euler characteristic. To make this precise, we ﬁrst remind the reader of a
key tool, Farkas’ Lemma.
Theorem A.11 (Farkas’ Lemma). If A is a realm×n matrix and b∈ Rm, and· the
standard Euclidean inner product onRm, then the following holds:
{x∈ Rn| Ax = b,x > 0} is non-empty if and only if for allz∈ Rm such thatATz⁄= 0
and ATz≥ 0, z·b> 0.
Here x≥ 0 (respectivelyx >0) indicates that all coordinates ofx are non-negative (re-
spectively positive).
THE 3D-INDEX AND NORMAL SURF ACES 55
By using Farkas’ Lemma, we can mimic the above argument for Theorem A.2 to get
necessary and suﬃcient conditions for the existence of strict angle structures with vanishing
peripheral rotational holonomy.
Proposition A.12.Let T be an ideal triangulation of a compact manifoldM with boundary
consisting of tori. Then there exist a strict angle structure onT with vanishing peripheral
rotational holonomy if and only if there exists no Q-normal class0⁄= Q∈ Q(T; R+) with
χ(S)≥ 0 if and only if0⁄=Q∈Q(T; R+) implies χ(S)< 0.
Proof. We closely follow the argument of Theorem A.2 (and Lemma 10 in [LT08]). Using
the notation from the proof of Theorem A.2, a vectorx∈ R3n deﬁnes a strict angle structure
with vanishing peripheral rotational holonomy if and only if
Ax =b and x> 0.
By Farkas’ Lemma, this is equivalent to the condition that
for allz∈ R2n+2r such thatATz⁄= 0 and ATz≥ 0, z·b> 0.
Now if z =
[xi yj pk qk
]
then S = ATz = ∑
ixiEi +∑
jyjTj +∑
kpkMk +∑
kqkLk
represents a Q-normal class inQ(T; R). But ATz⁄= 0 and ATz≥ 0 iﬀS⁄= 0 and S has all
quad coordinates≥ 0, i.e. S∈Q(T; R+). Further,z·b =∑
i 2xi +∑
jyj =−χ(S). So the
result follows. □
