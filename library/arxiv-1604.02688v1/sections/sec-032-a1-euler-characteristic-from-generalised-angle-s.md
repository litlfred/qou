---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-032-a1-euler-characteristic-from-generalised-angle-s
section_title: "A.1. Euler characteristic from generalised angle structures"
section_number: null
pages: 51-55
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
toc_source: outline
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
shows how to compute the Euler characteristic of an embedded spun normal surface using
52 STAVROS GAROUFALIDIS, CRAIG D. HODGSON, NEIL R. HOFFMAN, AND J. HYAM RUBINSTEIN
any generalised angle structure. This result is well-known for closed normal surfaces; see for
example [LT08, Lemma 15].
Proposition A.3. Let T be an ideal triangulation of a cusped 3-manifold M, and let α :
□→R be a generalised angle structure on T. Then the Euler characteristic of any embedded
spun normal surface S ∈Q(T; R) is given by
χ(S) = −
X
q
α(q)xq
π
+ ρα(∂S)
2π
,
(34)
where the sum is over all normal classes q in T, xq is the normal coordinate of q, α(q) ∈R
denotes the angle assigned to the two edges facing q, and ρα(∂S) denotes the sum of the
rotational holonomies of the boundary components of S, oriented as in [∂S].
This result follows from a combinatorial version of the Gauss-Bonnet theorem, as used by
Thurston in [Thu77, Section 13.7]. Let S be a compact surface, possibly with boundary and
let C be a cell decomposition of S into ﬁnitely many polygons. Then a formal angle structure
(or combinatorial angle structure) on C is an assignment of real numbers (“angles”) to the
corners of the polygons such that the sum of angles is 2π at each internal vertex.
We compute the Euler characteristic of S as χ(S) = v −e + f, where v, e, f are the
numbers of vertices, edges and faces in the cell decomposition. Now each n-gon P contributes
1
2π(sum of corner angles) to v, n × 1
2 = n/2 to e and 1 to f, so contributes a local Euler
characteristic
χP = 1
2π(sum of corner angles in P) −n
2 + 1
(35)
to χ(S) = v −e + f.
Adding up the terms χP over all polygons P gives a contribution to χ(S) of +1 for each
internal vertex, −1 for each internal edge and +1 for each face. Assume that there are
also k boundary vertices and, hence, k boundary edges. Then to obtain χ(S) we need to
add additional contributions of
1
2π(2π −θi) where θi is the sum of internal angles at the ith
boundary vertex and −1/2 for each boundary edge. This gives
χ(S) =
X
P
χP + 1
2π
k
X
i=1
(2π −θi) −k
2 =
X
P
χP + 1
2π
k
X
i=1
(π −θi),
and last term
kg(∂S) =
k
X
i=1
(π −θi)
(36)
represents the total geodesic curvature of the boundary of S. Hence
Proposition A.4 (Combinatorial Gauss-Bonnet). Let S be a compact surface with a ﬁnite
cell decomposition C equipped with a formal angle structure. Then the Euler characteristic
of S is given by
χ(S) =
X
P
χP + kg(∂S)
2π
,
(37)
summed over all polygons P, where χP is deﬁned by (35) and where kg(∂S) denotes the total
geodesic curvature of ∂S.
THE 3D-INDEX AND NORMAL SURFACES
53
Proof of Proposition A.3. Let S be a (non-compact) embedded spun normal surface in T
and choose a compact subsurface S0 consisting of all quads and a ﬁnite number of normal
triangles such that S \S0 is a collection of annuli spiralling out to the cusps of M. By adding
an additional layer of triangles, if necessary, we can assume that there is a neighbourhood of
∂S0 consisting entirely of triangles. Projecting these normal triangles to a horosphere gives
a layer of Euclidean triangles to the left of the boundary, and the rotational holonomy of
∂S0 is the sum
ρα(∂S) = ρα(∂S0) =
k
X
i=1
(π −θi),
where θi is the sum of triangle angles at the ith vertex on the boundary.
Now S0 has a cell decomposition into quads and triangles, and a generalised angle structure
α on T assigns an “angle” (in R) to each corner of each 2-cell in this decomposition, giving
a formal angle structure on this cell decomposition. Now each 2-cell gives a contribution to
the Euler characteristic as follows:
• Each quad q contributes χ(q) =
1
2π(angle sum)−1. But the sum of angles in the quad
is 2π minus twice the angle α(q) on the two edges facing q, so we have χ(q) = −α(q)/π.
• Each triangle t contributes χ(t) =
1
2π(angle sum)2 −3/2 + 1 = 0.
Hence the combinatorial Gauss-Bonnet theorem gives
χ(S) = χ(S0) = −
X
q
α(q)xq
π
+ 1
2π
k
X
i=1
(π −θi) = −
X
q
α(q)xq
π
+ ρα(∂S)
2π
.
□
Since the boundary term vanishes for any angle structure with vanishing peripheral rota-
tional holonomy, this gives the following convenient way of computing the Euler character-
istic:
Corollary A.5. Let T be an ideal triangulation of a cusped 3-manifold M, and let α : □→R
be a generalised angle structure on T with vanishing peripheral rotational holonomy. Then
the Euler characteristic of any embedded spun normal surface S ∈Q(T; R) is given by
χ(S) = −
X
q
α(q)xq
π
.
(38)
Deﬁnition A.6. For a general Q-normal class S ∈Q(T; R) we take the formula (34) as the
deﬁnition of the formal Euler characteristic of S. This is a linear function χ : Q(T; R) →R.
Remark A.7. The independence of choice of angle structure follows directly from [LT08,
Lemma 15]. For the angle structures in this paper, (A, κ) = (0, 0) and our α(q) is equal to
one half of A(q) as in [LT08].
Another consequence of these results is
54 STAVROS GAROUFALIDIS, CRAIG D. HODGSON, NEIL R. HOFFMAN, AND J. HYAM RUBINSTEIN
Corollary A.8. Each peripheral curve solution has vanishing formal Euler characteristic.
Hence
χ
 X
i
xiEi +
X
i
yjTj +
X
k
(pkMk + qkLk)
!
= −
X
i
2xi −
X
j
yj,
(39)
since χ(Ei) = −2 and χ(Tj) = −1.
Proof. Let α be a generalised angle structure on T, and let S be the peripheral curve solution
given by a curve with homology class c ∈H1(∂M; Z). Then we have ∂S = 2c (see Section
7.1). and, by deﬁnition, ρα(c) = P
q α(q)xq where xq are the quad coordinates of S. Hence
χ(S) = −
X
q
α(q)xq
π
+ ρα(∂S)
2π
= −ρα(c)
π
+ ρα(∂S)
2π
= 0.
□
Remark A.9. We could also use the formula (39) to deﬁne the formal Euler characteristic of
a general Q-normal class S ∈Q(T; R).
Example A.10. For the ﬁgure eight knot complement with its triangulation given in Ex-
ample 4.1, the angle structure equations have general solution of the form
α = (α0 + t1α1 + t2α2 + t3α3)π, with ti ∈R
where α0 = (−1, 2, 0, 1, 0, 0), α1 = (2, −2, 0, −1, 0, 1), α2 = (1, −1, 0, −1, 1, 0), α3 = (1, −2, 1, 0, 0, 0).
This gives rotational holonomies for the meridian and longitude
ρα(M) = (−1 + t1 + t2 + t3)π and ρα(L) = (2 −4t1 −2t2)π.
Now there is an embedded spun normal once punctured Klein bottle with quad coordinates
K = (0, 0, 2, 0, 1, 0) with boundary ∂K = 4µ + 1λ. The general formula (34) for the Euler
characteristic gives
χ(K) = −
X
q
α(q)
π
+ ρα(∂S)
2π
= −1
πα·K+ 1
2πα·(4M +L) = (−t2−2t3)+(−1+t2+2t3) = −1
as expected.
Alternatively we can write K = 2M + 1
2L + 1T2, hence χ(K) = −1 by formula (39).
In fact, ﬁnding angle structures can be seen as a dual problem to the existence of surfaces
of non-negative Euler characteristic. To make this precise, we ﬁrst remind the reader of a
key tool, Farkas’ Lemma.
Theorem A.11 (Farkas’ Lemma). If A is a real m × n matrix and b ∈Rm, and · the
standard Euclidean inner product on Rm, then the following holds:
{x ∈Rn | Ax = b, x > 0} is non-empty if and only if for all z ∈Rm such that ATz̸ = 0
and ATz ≥0, z · b > 0.
Here x ≥0 (respectively x > 0) indicates that all coordinates of x are non-negative (re-
spectively positive).
THE 3D-INDEX AND NORMAL SURFACES
55
By using Farkas’ Lemma, we can mimic the above argument for Theorem A.2 to get
necessary and suﬃcient conditions for the existence of strict angle structures with vanishing
peripheral rotational holonomy.
Proposition A.12. Let T be an ideal triangulation of a compact manifold M with boundary
consisting of tori. Then there exist a strict angle structure on T with vanishing peripheral
rotational holonomy if and only if there exists no Q-normal class 0̸ = Q ∈Q(T; R+) with
χ(S) ≥0 if and only if 0̸ = Q ∈Q(T; R+) implies χ(S) < 0.
Proof. We closely follow the argument of Theorem A.2 (and Lemma 10 in [LT08]). Using
the notation from the proof of Theorem A.2, a vector x ∈R3n deﬁnes a strict angle structure
with vanishing peripheral rotational holonomy if and only if
Ax = b and x > 0.
By Farkas’ Lemma, this is equivalent to the condition that
for all z ∈R2n+2r such that ATz̸ = 0 and ATz ≥0, z · b > 0.
Now if z =
xi
yj
pk
qk

then S = ATz = P
i xiEi + P
j yjTj + P
k pkMk + P
k qkLk
represents a Q-normal class in Q(T; R). But ATz̸ = 0 and ATz ≥0 iﬀS̸ = 0 and S has all
quad coordinates ≥0, i.e. S ∈Q(T; R+). Further, z · b = P
i 2xi + P
j yj = −χ(S). So the
result follows.
□
