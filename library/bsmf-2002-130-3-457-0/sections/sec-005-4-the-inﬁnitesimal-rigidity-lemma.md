---
doc_id: bsmf-2002-130-3-457-0
doc_title: "Hyperideal polyhedra in hyperbolic 3-space"
section_id: sec-005-4-the-inﬁnitesimal-rigidity-lemma
section_title: "The Inﬁnitesimal Rigidity Lemma"
section_number: 4
pages: 15-25
source_pdf: BSMF_2002__130_3_457_0.pdf
source_sha256: 63f79235d0c13ba8
toc_source: inferred
doc_brief: "Hyperideal polyhedra in hyperbolic 3-space — — A hyperideal polyhedron is a non-compact polyhedron in the hyperbolic 3-space 3 which, in the projective model for 3 ⊂ 3, is just the intersection of 3"
---
This section is devoted to the proof of the Inﬁnitesimal Rigidity Lemma of
Proposition 10. The proof follows the general lines of the famous arguments of
Cauchy [5] on the deformations of convex polyhedra in E3 (see also [15][7]), as
adapted to hyperbolic polyhedra by Andreev [2] and Rivin [12]. For polyhedra
which are strictly hyperideal, namely whose vertices are all outside of the clo-
sure of H3, this proof is essentially contained in [12, §4] if we use the truncated
polyhedron introduced in §1.
Recall that we have a map %Θ : U →RE∪E′, deﬁned on a neighborhood U
of Φ(P) in (RP3)V , which to x ∈U associates the hyperbolic external dihedral
angles of the polyhedron Px whose vertices are the coordinates of x and whose
combinatorial type is that of &P Proj
0
. We also have a map G : PO(3, 1) →(RP3)V
deﬁned by g ,→gΦ(P). We want to show that the kernel of the tangent map
TΦ(P ) %Θ : TΦ(P )(RP3)V →RE∪E′ is equal to the image of
TIdG : TIdPO(3, 1) −→TΦ(P )(RP3)V .
Let ˙x ∈TΦ(P )(RP3)V be a vector which is contained in the kernel of TΦ(P ) %Θ.
We want to show that ˙x is in the image of TIdG, namely is tangent to an
inﬁnitesimal deformation of Φ(P) by an inﬁnitesimal element of PO(3, 1).
Lemma 12. — If, for a given v ∈V , the vertex of P Proj corresponding to v
is located on the sphere at inﬁnity ∂∞H3 ⊂RP3, then the coordinate vector ˙xv
of ˙x corresponding to v is tangent to ∂∞H3 in RP3.
Proof. — Let e1, e2, . . . , en ∈E ∪E′ be the edges of &P Proj
0
that are adjacent to
the vertex v. Let ϕ : U →R be the function deﬁned by ϕ(x) = !n
i=1 %Θei(x).
Note that the vector ˙x is contained in the kernel of the tangent map TΦ(P )ϕ,
since it is contained in the kernel of TΦ(P ) %Θ.
By Proposition 5 and Lemma 7, ϕ(x) = 2π whenever the coordinate xv of
x ∈U ⊂(RP3)V corresponding to v belongs to ∂∞H3. It follows that the
kernel of TΦ(P )ϕ contains all those vectors ˙y ∈TΦ(P )(RP3)V whose coordinate
˙yv is tangent to ∂∞H3. The lemma will be proved if we show that the kernel of
TΦ(P )ϕ consists only of these ˙y with ˙yv tangent to ∂∞H3. For this, it suﬃces
to show that TΦ(P )ϕ is non-trivial.
Modifying P by an element of PO(3, 1) if necessary, we can arrange that the
projective polyhedron P Proj is contained in R3 ⊂RP3 and contains the origin
0 ∈H3 ⊂R3 in its interior.
Let t ,→xt ∈U ⊂(RP3)V , t ∈] −ε, ε[, be a curve such that x0 = Φ(P),
such that the coordinate xt
v′ is equal to x0
v′ for every v′̸ = v and every t, and
BULLETIN DE LA SOCI´ET´E MATH´EMATIQUE DE FRANCE
472
BAO (X.) & BONAHON (F.)
such that the curve t ,→xt
v ∈RP3 is tangent to the outer unit normal vector
of ∂∞H3 ⊂R3 ⊂RP3 at t = 0. If ˙x0 denotes the tangent vector of t ,→xt at
t = 0, we will use a little bit of euclidean geometry to estimate TΦ(P )ϕ( ˙x0) =
dϕ(xt)/dt|t=0.
Consider the projective polyhedron Pxt associated to xt ∈(RP3)V , namely
with vertex set xt and with the combinatorial type of &P Proj
0
. For t ≥0, the
intersection of Pxt with ∂∞H3 has one component At which is near x0
v ∈∂∞H3.
This component At is a polygon on the sphere ∂∞H3, reduced to a point when
t = 0. Remember that, if Π and Π′ are two projective planes which meet H3,
the hyperbolic dihedral angle between the hyperbolic planes Π∩H3 and Π′∩H3
is equal to the euclidean angle between the two circles Π∩∂∞H3 and Π′∩∂∞H3,
for the euclidean metric on the sphere ∂∞H3 ⊂R3. Applying the Gauss-Bonnet
formula to At, we conclude that
ϕ(xt) =
n
'
i=1
%Θei(xt) = 2π −
(
∂At
κ −area(At)
where κ is the geodesic curvature of the boundary ∂At in ∂∞H3.
Let us diﬀerentiate in t at t = 0. The area term is bounded by a quantity of
order 2 in t, and therefore does not contribute to the derivative. Because we
arranged that the point 0 is in the interior of P, the curvature κ is negative
bounded away from 0 on each side of At. On the other hand, because the
component ˙x0
v of the tangent vector ˙x0 is equal to the outer unit normal vector
of ∂∞H3, the length of ∂At has a positive derivative with respect to t at t = 0.
It follows that TΦ(P )ϕ( ˙x0) = dϕ(xt)/dt|t=0 is strictly positive. (Note that we
do not need to worry about the derivative of κ since ∂A0 has length 0.)
This proves that T(p,x)ϕ is non-trivial. As a consequence, its kernel consists
of those vectors ˙y ∈TΦ(P )(RP3)V whose coordinate ˙yv is tangent to ∂∞H3.
Since ˙x belongs to this kernel, this completes the proof of Lemma 12.
Let t ,→xt, t ∈] −ε, ε[, be a smooth curve in (RP3)V such that x0 = Φ(P)
and dxt/dt|t=0 = ˙x. By Lemma 12, we can choose this curve so that, whenever
the coordinate x0
v of x0 = Φ(P) is in the sphere ∂∞H3, the corresponding
coordinate xt
v of xt remains in ∂∞H3 for every t. In particular, for t suﬃciently
small, all coordinates xt
v of xt are in the complement of H3 in RP3.
Again, let Pxt be the projective polyhedron associated to xt ∈(RP3)V ,
namely with vertex set xt and with the combinatorial type of &P Proj
0
.
As in §1, consider the truncated polyhedron P Trun
xt
obtained from Pxt by
chopping oﬀits intersection with the interiors of disjoint half-spaces and
horoballs Ht
v where, for each v ∈V , Ht
v is a half-space delimited by the hyper-
bolic plane H3 ∩(xt
v)⊥if the vertex xt
v of Pxt is strictly hyperideal and Ht
v is
a horoball centered at xt
v if this vertex is ideal. From its construction, P Trun
xt
inherits a natural polyhedron structure where its faces are of three types:
tome 130 – 2002 – no 3
HYPERIDEAL POLYHEDRA IN HYPERBOLIC 3-SPACE
473
(i) the intersection of a face of Pxt with the complement in H3 of the interiors
of all the Ht
v; such a face is a polygon contained in a hyperbolic plane, whose
sides are either geodesic or horocyclic, and whose internal angles are all equal
to 1
2π.
(ii) the intersection of Pxt with the hyperbolic plane ∂Ht
v associated to a
strictly hyperideal vertex xt
v; such a face is a hyperbolic polygon with geodesic
sides and, at each of its vertices, its internal angle is equal to the dihedral angle
of the corresponding edge of Pxt ∩H3.
(iii) the intersection of Pxt with the horosphere ∂Ht
v associated to an ideal
vertex xt
v; such a face is a euclidean polygon with geodesic sides and, at each
of its vertices, its internal angle is equal to the internal dihedral angle of the
corresponding edge of Pxt ∩H3.
Recall that in the construction of P Trun
xt
we have a degree of freedom in the
choice of the horospherical Ht
v associated to the ideal vertices of Pxt. We will
use this freedom to impose an additional condition on the faces of type (iii).
By adjusting the height of the corresponding horospheres ∂Ht
v, we can always
arrange that the area of each face of type (iii) is constant, independent of t.
Note that the polyhedra P Trun
xt
all have the combinatorial type of the polyhe-
dron &P Trun
0
obtained by truncating the polyhedron &P Proj
0
(which, as a reminder,
was deﬁned by subdividing the faces of P Proj
0
into triangles).
Consider now the unsubdivided polyhedron P Proj
0
, and truncate it to P Trun
0
.
Each vertex v of P Trun
0
is also a vertex of &P Trun
0
, and is therefore associated to
a vertex vt of P Trun
xt
.
For each edge e of P Trun
0
, look at its end vertices v1, v2, and consider the
hyperbolic distance d(vt
1, vt
2) between the corresponding vertices vt
1, vt
2 of P Trun
xt
.
Label the edge e by the symbol +, 0 or −according to whether the derivative
of d(vt
1, vt
2) at t = 0 is positive, zero or negative.
Our goal is to show that all the edges are actually labelled by 0. This will
require a few preparatory lemmas.
If Q is a polygon with each of its edges labelled by a symbol +, 0 or −, deﬁne
the number of sign changes of ∂Q as the minimum number of vertices v1, . . . , vn
which one needs to remove from ∂Q so that the edges in each component
of ∂Q −{v1, . . . , vn} have the same sign, namely are either all in {+, 0} or all
in {−, 0}. Note that the number of sign changes is always even.
We will ﬁrst show that, for each face f of P Trun
0
, either all the edges of f
are labelled by 0, or it admits at least 4 sign changes in its boundary. In other
words, there cannot be 0 or 2 sign changes in the boundary of f, unless all the
edges of f are labelled by 0.
We begin with faces of Type (iii), contained in horospheres. The argument
uses the following euclidean geometry lemma, which is an inﬁnitesimal and
simpler version of Lemma M3 of [15] (a result attributed there to A.D. Alek-
sandrov).
BULLETIN DE LA SOCI´ET´E MATH´EMATIQUE DE FRANCE
474
BAO (X.) & BONAHON (F.)
Lemma 13. — In the euclidean plane R2, let Qt, t ∈]−ε, ε[, be a diﬀerentiable
family of strictly convex polygons with straight sides. Suppose that, at t = 0,
the derivative of the angle of Qt at each of its vertices is equal to 0, and that
the derivative of the area of Qt is also equal to 0. Label each edge of Q0 by the
symbol +, 0, or −according to whether the derivative of its length at t = 0 is
positive, zero or negative. Then, either all edges are labelled by 0, or there are
at least 4 sign changes in ∂Q0.
Here, “strictly convex” means that the internal angle of Qt at each of its
vertices is strictly between 0 and π.
Proof. — (Compare [15, Lemma M3].)
Suppose, in search of a contradic-
tion, that there are exactly 2 sign changes.
We can then index the edges
of Qt as et
1, . . . , et
q, et
q+1, . . . , et
r, et
r+1 = et
1, going counterclockwise in this order
around ∂Qt, in such a way that et
i is labelled by + or 0 if 1 ≤i ≤q, and
by −or 0 if q + 1 ≤i ≤r. Let vt
i be the vertex intersection of et
i and et
i+1, and
set vt
0 = vt
r for consistency of the notation. Finally, let T t
i be the unit tangent
vector of the edge et
i, oriented by the counterclockwise orientation of ∂Qt, and
let ℓt
i be the length of et
i. Then, for 1 ≤i < j ≤r,
vt
j −vt
i =
j
'
k=i+1
ℓt
kT t
k = −
i
'
k=1
ℓt
kT t
k −
r
'
k=j+1
ℓt
kT t
k.
Let αt
i ∈]0, π[ be the angle from T t
i to T t
i+1, namely the external angle
of Qt at the vertex vt
i. Note that !r
i=1 α0
i = 2π. Replacing t by −t if necessary
(which exchanges the labels + and −), we can assume without loss of generality
that !r
i=q+1 α0
i ≤π. Pick an index p with 1 ≤p ≤q such that !p−1
i=1 α0
i < π
and !q
i=p+1 α0
i < π.
Composing Qt by an isometry depending diﬀerentiably on t, we can arrange
that the vertex vt
p is ﬁxed, and that the tangent vector T t
p is constant. By
our hypothesis that the angles of Qt have derivative 0 at t = 0, it follows that
dT t
i /dt|t=0 = 0 for every i. As a consequence, if ˙ℓ0
i = dℓt
i/dt|t=0 denotes the
derivative of the length ℓt
i at t = 0, the vector ˙v0
i = dvt
i/dt|t=0 is equal to
˙v0
i =
)
+ !i
j=p+1 ˙ℓ0
jT 0
j
if p + 1 ≤i ≤r,
−!p
j=i+1 ˙ℓ0
jT 0
j
if 1 ≤i ≤p −1.
We will consider the direction in which the edges et
i move.
We will say
that et
i weakly moves towards (resp. away from) Q0 if either the vector ˙v0
i−1 =
dvt
i−1/dt|t=0 is equal to 0 or if the angle from ˙v0
i−1 to T 0
i is in the closed interval
[−π, 0] (resp. [0, π]); note that we can consider the vector ˙v0
i = ˙v0
i−1 + ˙ℓ0
i T 0
i
instead of ˙v0
i−1 for this property. The edge et
i strictly moves towards (resp.
away from) Q0 if ˙v0
i−1 = dvt
i−1/dt|t=0 is non-zero and the angle from ˙v0
i−1
to T 0
i is in the open interval ] −π, 0[ (resp. ]0, π[).
tome 130 – 2002 – no 3
HYPERIDEAL POLYHEDRA IN HYPERBOLIC 3-SPACE
475
For p + 1 ≤j ≤i −1 ≤q, the derivative ˙ℓ0
j is non-negative and the angle
from T 0
j to T 0
i is in the interval ]0, π[, by choice of the indexing. It follows
that the angle from ˙v0
i−1 = !i−1
j=p+1 ˙ℓ0
jT 0
j to T 0
i is in [0, π], unless ˙v0
i−1 = 0.
In other words, every edge et
i with p + 2 ≤i ≤q + 1 weakly moves away
from Q0.
In addition, et
i strictly moves away from Q0 if there is a j with
p + 1 ≤j ≤i −1 ≤q −1 and ˙ℓ0
j > 0, namely such that e0
j is labelled by the
symbol +.
For 1 ≤i ≤p −1, the same argument applied to ˙v0
i = −!p
j=i+1 ˙ℓ0
jT 0
j shows
that et
i moves away from Q0, and does so strictly if there is a j with i+1 ≤j ≤p
such that e0
j is labelled by the symbol +.
In particular, for 1 ≤i ≤q+1, the edge et
i moves away from Q0. In addition,
since there is at least one edge labelled by the symbol +, at least one of the
two edges et
1 and et
q+1 strictly moves away from Q0. Since the areas of Qt
is inﬁnitesimally constant, we conclude that there must be an index i0, with
q + 2 ≤i0 ≤r, such that et
i0 strictly moves towards of Q0. We can choose
this i0 so that et
i0+1 moves away from Q0 (using the convention that et
r+1 = et
1
when i0 = r).
Because et
i0 strictly moves towards Q0 and et
i0+1 moves away from Q0, the
vector ˙v0
i0 is in the angular sector from T 0
i0 to T 0
i0+1. Since !r
i=q+1 α0
i ≤π,
we conclude that the angle from ˙v0
i0 to Tq+1 is in ] −π, 0[.
Remembering
that ˙ℓ0
j ≤0 for all j with q + 1 ≤j ≤r, we conclude that the angle from
˙v0
q+1 = ˙v0
i0 −!i0
j=q+2 ˙ℓ0
jT 0
j to Tq+1 is in ] −π, 0[. However, this contradicts our
earlier conclusion that et
q+1 moves away from Q0.
This contradiction shows that there cannot be 2 sign changes around Q0.
A similar but simpler argument shows that there cannot be 0 sign change,
unless all edges are labelled by 0. Therefore, either all edges are labelled by 0,
or there must be at least 4 sign changes around Q0.
Lemma 14. — For every face Q of type (iii) of the truncated polyhedron P Trun
0
,
either all the edges of ∂Q are labelled by 0, or there are at least 4 sign changes
in ∂Q.
Proof. — There is a face &Qt of the truncated polyhedron P Trun
xt
which is as-
sociated to Q and is contained in a horosphere ∂Ht. Note that the vertices
of &Qt correspond to the edges of Pxt that are adjacent to the vertex of Pxt fac-
ing &Qt. In particular, some vertices of &Qt are naturally associated to vertices of
Q and other vertices are not. In the horosphere ∂Ht endowed with its euclidean
metric, let Qt be the convex hull of those vertices of &Qt which correspond to
vertices of Q.
For an edge e of Q, with end vertices v1 and v2, the hyperbolic distance
d(vt
1, vt
2) between the corresponding vertices vt
1, vt
2 of P Trun
xt
in H3 is a strictly
BULLETIN DE LA SOCI´ET´E MATH´EMATIQUE DE FRANCE
476
BAO (X.) & BONAHON (F.)
increasing function of the length of the edge et of Qt corresponding to e. It fol-
lows that, in our labelling of the edges of P Trun
0
, the edge e is labelled by +, 0,
or −exactly when the derivative of the length of et at t = 0 is positive, zero
or negative, respectively.
Because the vector ˙x ∈TΦ(P )(RP3)V tangent to t ,→xt is contained in
the kernel of the tangent map TΦ(P ) %Θ, all the angles of &Qt have derivative 0
at t = 0. In particular, because &Q0 = Q0, the distance from each vertex of &Qt
to ∂Qt has derivative 0 at t = 0. This provides two important conclusions:
First, the angles of Qt have derivative 0 at t = 0; second, the area of Qt has
the same derivative as the area of &Qt at t = 0, namely 0 since the area of &Qt is
constant by choice of the truncated polyhedron P Trun
xt
.
We can therefore apply Lemma 13 to the polyhedron Qt, which provides the
conclusion of Lemma 14.
For faces of Type (i) of P Trun
0
, we use the following lemma.
Lemma 15. — In the hyperbolic plane H2, let Qt, t ∈]−ε, ε[, be a diﬀerentiable
family of convex hyperideal polygons such that, for every vertex v of QProj
t
which is on the circle at inﬁnity ∂∞H2, the corresponding vertex vt is also on
∂∞H2 for every t. Let QTrun
t
be obtained by truncating Qt, chosen to depend
diﬀerentiably on t (remember that the truncation is not uniquely determined at
the ideal vertices of Qt). Label each edge of QTrun
0
by the symbol +, 0, or −
according to whether the derivative of its length at t = 0 is positive, zero or
negative. Then, either all edges are labelled by 0, or there are at least 4 sign
changes in QTrun
0
.
Proof. — If there are fewer than 4 sign changes, we can then index the edges
of QTrun
t
as et
1, . . . , et
p, et
p+1, . . . , et
q, et
q+1 = et
1, going counterclockwise in this
order around ∂QTrun
t
, in such a way that e0
i is labelled by + or 0 if 2 ≤i ≤p−1,
and by −or 0 if p+1 ≤i ≤q. In addition, replacing them by suitable neighbors
if necessary, we can arrange that et
1 and et
p are both contained in edges of the
original untruncated polyhedron Qt.
We use the projective model for the hyperbolic plane H2 ⊂R2 ⊂RP2,
with isometry group PO(2, 1). For each i, let T u
i ∈PO(2, 1) be the hyperbolic
isometry which acts by translation of u ∈R along the geodesic or horocycle that
contains e0
i , for the orientation coming from the counterclockwise orientation
of ∂QTrun
0
. Let gt
i be the geodesic or horocycle of H2 that contains the edge et
i,
transversely oriented by the outer normal orientation of ∂QTrun
0
. Finally, let N t
1
and N t
p ∈R3 be the unit normal vectors of the transversely oriented geodesics
gt
1 and gt
p, as deﬁned (for the 3-dimensional case) in §1.
Composing Qt by an isometry depending diﬀerentiably on t if necessary, we
can arrange that et
1 stays in a ﬁxed geodesic of H2, and that the vertex sepa-
rating et
1 from et
2 is constant. Since all the angles of QTrun
t
remain equal to 1
2π,
tome 130 – 2002 – no 3
HYPERIDEAL POLYHEDRA IN HYPERBOLIC 3-SPACE
477
we conclude that N t
p = T ℓt
2−ℓ0
2
2
T ℓt
3−ℓ0
3
3
. . . T
ℓt
p−1−ℓ0
p−1
p−1
N 0
p where ℓt
i denotes the
length of et
i. Using dots to demote derivatives with respect to t, as usual, this
gives ˙N 0
p = !p−1
i=2 ˙ℓ0
i ˙T 0
i N 0
p for the inﬁnitesimal isometry ˙T 0
i = dT u
i /du|t=0 ∈
TIdPO(3, 1).
We claim that B(N 0
1 , ˙T 0
i N 0
p) ≥0, and that the inequality is strict in all but
one case.
For this, ﬁrst consider the case where e0
i is geodesic.
Composing by an
isometry of H2, we can arrange that g0
i is equal to the geodesic going from
(−1, 0) to (+1, 0) in H2 ⊂R2 ⊂RP2, and that QTrun
0
is locally above this
geodesic. We still have a degree of freedom through hyperbolic translations
along this geodesic. Composing with such a translation, we can arrange that
the point (0, 0) is located on g0
i between the point which is closest to g0
1 and the
point which is closest to g0
p. Then, because e0
1, e0
i and e0
p arise in this order for
the counterclockwise orientation of ∂QTrun
0
, the vector N 0
1 = (a1, b1, c1) points
to the left of (0, 0) and N 0
p = (ap, bp, cp) points to the right in the sense that
a1 > 0, b1 < 0, ap > 0, bp > 0. (There are several cases to consider, according
to whether g0
1 and g0
p meet g0
i or not). An easy computation now gives that ˙T 0
i
is given by the matrix
* 0 1 0
1 0 0
0 0 0
+
so that B(N 0
1 , ˙T 0
i N 0
p) = a1bp −apb1 > 0.
Similarly, when e0
i is horocyclic, we can arrange by an isometry of H2 that
the horocyle g0
i is centered at the point (−1, 0), namely touches ∂∞H2 at that
point. We now have to distinguish subcases.
If the geodesics g0
1 and g0
p are not asymptotic, we can arrange that the point
(0, 0) is located in the interior of the shortest geodesic arc joining g0
1 to g0
p.
Then N 0
1 = (a1, b1, c1) and N 0
p = (ap, bp, cp) are such that a1 > 0, b1 = 0,
c1 > 0, ap > 0, bp = 0 and cp < 0. Also, ˙T 0
i is given by the matrix
* 0 0
λ
0 0 −λ
λ λ
0
+
for some λ > 0. Then, B(N 0
1 , ˙T 0
i N 0
p) = −λa1cp + λapc1 > 0.
If g0
1 and g0
p are asymptotic but their common end point is diﬀerent from
(−1, 0), we can arrange that this common end point is (1, 0).
Then N 0
1 =
(a1, b1, c1) and N 0
p = (ap, bp, cp) are both orthogonal to the line of R3 corre-
sponding to (1, 0) ∈R2 ⊂RP2, and a1 > 0, b1 = a1, c1 > 0, ap > 0, bp = ap,
cp < 0. Then,
B(N 0
1 , ˙T 0
i N 0
p) = −λa1cp −λb1cp + λapc1 + λbpc1 > 0.
Finally, consider the case where g0
1 and g0
p both have (−1, 0) as an end point.
Note that this can happen only if i = 2 and p = 3. Then, N 0
1 = (a1, b1, c1)
and N 0
p = (ap, bp, cp) are both orthogonal to the line of R3 corresponding to
(−1, 0) ∈R2 ⊂RP2, and a1 > 0, b1 = −a1, c1 > 0, ap > 0, bp = −ap, cp < 0.
Then,
B(N 0
1 , ˙T 0
i N 0
p) = −λa1cp −λb1cp + λapc1 + λbpc1 = 0.
BULLETIN DE LA SOCI´ET´E MATH´EMATIQUE DE FRANCE
478
BAO (X.) & BONAHON (F.)
Therefore, B(N 0
1 , ˙T 0
i N 0
p) ≥0 in all cases, with equality only in the last case
above.
By choice of the indexing, the derivative ˙ℓ0
i is non-negative for every i
with 2 ≤i ≤p −1. We conclude that B(N 0
1 , ˙N 0
p) ≥0. Furthermore, the
inequality is strict if at least one edge e0
i with 2 ≤i ≤p −1 is labelled by +,
unless p = 3 and e0
2 is horocyclic.
For a geometric interpretation of this inequality, note that B(N 0
1 , ˙N 0
p) is
the derivative of B(N t
1, N t
p) with respect to t since we arranged that N t
1 is
constant, and that B(N t
1, N t
p) is equal to cosh of the distance between the
geodesics respectively containing et
1 and et
p.
Now, considering the other side of ∂QTrun
t
, we see that
˙N 0
p = −˙ℓ0
1 ˙T 0
1 N 0
p −
q
'
j=p+1
˙ℓ0
j ˙T 0
j N 0
p.
The same argument as above shows that B(N 0
1 , ˙T 0
j N 0
p) < 0 for every j with
p + 1 ≤j ≤q, unless p + 1 = j = q and e0
j is horocyclic, in which case
B(N 0
1 , ˙T 0
j N 0
p) = 0. Also,
B(N 0
1 , ˙T 0
1 N 0
p) = −B( ˙T 0
1 N 0
1 , N 0
p) = −B(0, N 0
p) = 0.
Since ˙ℓ0
j ≤0 for every p + 1 ≤j ≤q, we conclude that B(N 0
1 , ˙N 0
p) ≤0, and
that the inequality is strict if at least one edge e0
j with p + 1 ≤j ≤q is labelled
by −, unless p + 1 = q and e0
p+1 is horocyclic.
These inequalities can be reconciled only when one of the following holds:
(a) every edge e0
i with i̸ = 1, p is labelled by 0;
(b) p = 3 and every edge e0
i with p + 1 ≤i ≤q is labelled by 0;
(c) p = q −1 and every edge e0
i with 2 ≤i ≤p −1 is labelled by 0.
If any edge e0
i was labelled by + or −, it would be possible to rechoose the
indexing of the edges of QTrun
0
so Properties (a), (b) and (c) all fail, while the
conditions imposed at the beginning of the proof still hold. (Use the fact that
the untruncated polyhedron Q0 has at least 3 edges.) As this would lead to a
contradiction, we conclude that every edge of QTrun
0
is labelled by 0.
Lemma 16. — For every face Q of type (i) of the truncated polyhedron P Trun
0
,
either all the edges of ∂Q are labelled by 0, or there are at least 4 sign changes
in ∂Q.
Proof. — The face Q corresponds to a face Q′ of the projective polyhe-
dron P Proj
0
.
However, the vertices of Pxt associated to the vertices of Q′
are not necessarily coplanar any more.
Nevertheless, because the vector
˙x ∈TΦ(P )(RP3)V tangent to t ,→xt is contained in the kernel of the tangent
map TΦ(P ) %Θ, they are inﬁnitesimally coplanar in the following sense: we can
tome 130 – 2002 – no 3
HYPERIDEAL POLYHEDRA IN HYPERBOLIC 3-SPACE 479

find a projective plane Il, in RP? such that, for every vertex v of Q’, the
distance from the vertex x!, of P,+ corresponding to v to the plane II; is 0
and has derivative 0 at t = 0, for an arbitrary riemannian metric on RP?. In
addition, we can choose the plane II; so that it depends differentiably on t. For
instance, we can take I, to be the plane passing through three predetermined
such vertices of P+.

For each vertex v of Q’, choose a point y! € I, depending differentiably
on t, such that y9 = x° and the distance from y/, to x!, has derivative 0 at t = 0.
In addition, we can choose y!, so that it belongs to the sphere at infinity 0..H?
whenever 2!, does, namely whenever «° does by our choice of the curve t > a! €
(RP?)”. Let Q; be the convex projective polygon in II, whose vertices are the
points y!, associated to the vertices v of Q’, and which is uniquely determined
by the property that it depends continuously on t and that Qo = P,o N Ho
(namely Qo is the face of PP?°) = P,o corresponding to Q’). Note that Q;
is a hyperideal polygon in the projective plane H,; = RP? with respect to the
hyperbolic plane H; NH? & H?, for t¢ sufficiently small.

In the hyperbolic plane H; MH3, let QF" be the truncated polygon associ-
ated to the hyperideal polygon Q;. Note that there is a natural identification
between the vertices of QP" and those of the face Q of PI". Because the
distance (for an arbitrary riemannian metric on RP?) from the vertex y!, of Q;
to the corresponding vertex x!, of Pz: is infinitesimally 0, the hyperbolic dis-
tance between two vertices of Q/"” is infinitesimally equal to the hyperbolic
distance between the corresponding vertices of Pin, In particular, if we la-
bel the edges of QZ" = Q as above Lemma 13, the labelling is the same as
that induced on the face Q by our original labelling of P/*™"". Lemma 16 then
follows from Lemma 15. oO

Finally, we consider faces of Type (ii) of P™", contained in hyperbolic
planes which are dual to strictly hyperideal vertices of PP’),

LEMMA 17. — In the hyperbolic plane H?, let Q:, t € |—e, ¢[, be a differentiable
family of compact strictly convex polygons with geodesic sides. Suppose that, at
t =0, the derivative of the angle of Q, at each of its vertices is equal to 0. Label
each edge of Qo by the symbol +, 0 or — according to whether the derivative
of its length at t = 0 is positive, zero or negative. Then, either all edges are
labelled by 0, or there are at least 4 sign changes in OQo.

Proof. — The proof is essentially the same as that of Lemma 15 (with no
horocyclic sides). The reader familiar with [12] will also recognize here an
infinitesimal (and simpler) version of [12, Lemma 4.11], which provided the
inspiration for our proof of Lemma 15. oOo

BULLETIN DE LA SOCIETE MATHEMATIQUE DE FRANCE
480
BAO (X.) & BONAHON (F.)
Lemma 18. — For every face Q of P Trun
0
which corresponds to a face of
type (ii) of the truncated polyhedron P Trun
0
, either all the edges of ∂Q are
labelled by 0, or there are at least 4 sign changes in ∂Q.
Proof. — The proof is identical to that of Lemma 16, using Lemma 17 instead
of Lemma 15.
We now conclude with a purely combinatorial argument.
Lemma 19. — Label each edge of P Trun
0
by a sign +, 0 or −in such a way
that, for each face Q of P Trun
0
, either all the edges of Q are labelled by 0 or
there are at least 4 sign changes in ∂Q. Then, all the edges are labelled by 0.
Proof. — This is Cauchy’s famous combinatorial lemma [5]; see also [15,
Lemma T]. Since it is fairly simple, we include a proof for the sake of
completeness.
Let G be the 1-skeleton of the dual cell decomposition of ∂P Trun
0
.
Note
that G is a combinatorial graph, in the sense that an edge has two distinct
end vertices and no two edges have the same end vertices. Label each edge
of G with the label of the dual edge of P Trun
0
. The sign condition for the faces
of &P Trun
0
translates to a similar sign condition for each vertex v of G: either
all the edges adjacent to v are labelled by 0, or one encounters at last 4 sign
changes as one goes around v.
Lemma 19 then follows from the following statement.
Sublemma 20. — Let G be a graph embedded in S2 with each edge of G labelled
by a sign +, 0 or −in such a way that, for each vertex v of G, either all the
edges adjacent to v are labelled by 0, or one encounters at least 4 sign changes
as we go around v. Then, all the edges of G are labelled by 0.
Proof of Sublemma 20. — Suppose that there is a graph G for which the prop-
erty fails. Erasing from G all the edges labelled by 0 (which does not disturb
the sign change condition) and restricting attention to a connected component
of the remaining graph, we can assume that all edges are labelled by + or −,
and that G is connected and non-empty. Adding edges labelled by + if neces-
sary (which again does not disturb the sign change condition), we can assume
that the complement of G in S2 consists of triangles.
For i = 0, 2, let Fi be the number of triangles in the complement of G
with i sign changes in their boundary. Then, if V and E respectively denote
the number of vertices and edges of G, the hypothesis that there are at least 4
sign changes at each vertex implies that 4V ≤2F2. Since we arranged that
the complement of G consists of triangles, counting edge sides in two diﬀerent
ways gives 3(F0 + F2) = 2E, while the Euler characteristic equation shows
that V −E + F0 + F2 = 2. Combining these three relations, we obtain that
F0 + 4 ≤0, a contradiction.
tome 130 – 2002 – no 3
HYPERIDEAL POLYHEDRA IN HYPERBOLIC 3-SPACE
481
This completes the proof of Lemma 19.
We are now ready to complete the proof of the Inﬁnitesimal Rigidity Lemma
of Proposition 10.
Proof of Proposition 10. — By Lemmas 14, 16 and 18, all the edges of P Trun
0
are labelled by 0. This means that if, for each edge e of P Trun
0
, we consider the
geodesic arc et joining the vertices vt
1, vt
2 of P Trun
xt
corresponding to the end
vertices v1, v2 of e, the length of et has derivative 0 at t = 0. In addition, if
two edges e1 and e2 of P Trun
0
meet at the vertex v, the angle between et
1 and et
2
at vt also has derivative 0 at t = 0, because the tangent vector ˙x = dxt/dt|t=0
is contained in the kernel of the tangent map TΦ(P ) %Θ (compare the polygons
Qt which we used in the proofs of Lemmas 14, 16 and 18). Finally, we already
saw in the proof of Lemma 16 that, for every face Q of P Trun
0
that corresponds
to a face of P Proj
0
, the vertices of P Trun
xt
corresponding to the vertices of Q are
inﬁnitesimally coplanar near t = 0. If, among these faces Q of P Trun
0
corre-
sponding to faces of P Proj
0
, we successively go from one to the other by crossing
one edge at a time, we conclude that there exists an isometry gt ∈PO(3, 1) of
H3, depending diﬀerentiably on t and with g0 = Id, such that dgt(vt)/dt|t=0 = 0
for every vertex vt of P Trun
xt
corresponding to a vertex v of P Trun
0
.
Note that the vertices of the projective polyhedron Pxt, namely the coordi-
nates of xt, can be completely recovered from the vertices of P Trun
xt
that corre-
spond to vertices of P Trun
0
, as intersection of projective lines passing through
these points. It follows that dgt(xt)/dt|t=0 = 0. We conclude that
0 = dgt(xt)/dt|t=0 = dgt(x0)/dt|t=0 + dxt/dt|t=0,
= dgt
"
Φ(P)
#
/dt|t=0 + ˙x
since g0 = Id, x0 = Φ(P), and dxt/dt|t=0 = ˙x.
In particular, the vector ˙x = −dgt(Φ(P))/dt|t=0 = dg−1
t
(Φ(P))/dt|t=0
is tangent to the curve t ,→g−1
t
(Φ(P)) at t = 0. As a consequence, ˙x is in
the image of the tangent map at Id of the map PO(3, 1) →(RP3)V deﬁned
by g ,→g(Φ(P)).
This is exactly what we needed to complete the proof of Proposition 10.
