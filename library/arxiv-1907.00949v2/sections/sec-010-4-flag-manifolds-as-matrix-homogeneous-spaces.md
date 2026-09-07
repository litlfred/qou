---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-010-4-flag-manifolds-as-matrix-homogeneous-spaces
section_title: "Flag manifolds as matrix homogeneous spaces"
section_number: 4
pages: 9-16
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
We will discuss three representations of the ﬂag manifold as matrix homogeneous spaces , i.e.,
where a ﬂag is represented as an equivalence class of matrices:
Flag(n1,...,n d;n)∼= O(n)/
(
O(n1)× O(n2−n1)×···× O(nd−nd−1)× O(n−nd)
)
, (8)
Flag(n1,...,n d;n)∼= SO(n)/ S
(
O(n1)× O(n2−n1)×···× O(nd−nd−1)× O(n−nd)
)
, (9)
Flag(n1,...,n d;n)∼= V(nd,n )/
(
O(n1)× O(n2−n1)×···× O(nd−nd−1)
)
. (10)
The characterization (8) is standard [27, 11] and generalizes the well-known characterization of the
Grassmannian as Gr(k,n )∼= O(n)/
(
O(k)× O(n−k)
)
whereas the characterization (10) generalizes
another well-known characterization of the Grassmannian as Gr( k,n )∼= V(k,n )/ O(k).
Nevertheless, we will soon see that it is desirable to describe Flag(n1,...,n d;n) as a homogeneous
spaceG/H whereG is a connected Lie group — note that O(n) is not connected whereas V(nd,n )
is not a group, so (8) and (10) do not meet this criterion. With this in mind, we state and prove
(9) formally.
Proposition 4.1. Let 0 < n1 < ··· < nd < n be d positive integers. The ﬂag manifold
Flag(n1,...,n d;n) is diﬀeomorphic to the homogeneous space
SO(n)/ S
(
O(n1)× O(n2−n1)×···× O(nd−nd−1)× O(n−nd)
)
where S
(
O(n1)× O(n2−n1)×···× O(nd−nd−1)× O(n−nd)
)
is the subgroup of unit-determinant
block diagonal matrices with orthogonal blocks, i.e.,


Q1 0 ... 0
0 Q2 ... 0
... ... ... ...
0 0 ... Q d+1

∈ O(n), Q i∈ O(ni−ni−1), i = 1,...,d + 1,
d+1∏
i=1
det(Qi) = 1.
Proof. We start with the characterization (8), i.e., in this proof we assume ‘=’ in place of ‘ ∼=’ in
(8). We claim that the required diﬀeomorphism τ is given as in the commutative diagram below:
SO(n) O(n)
SO(n)/ S
(
O(n1)× O(n2−n1)×···× O(n−nd)
)
Flag(n1,...,n d;n)
j
π′ π
τ
Herej is the inclusion of SO(n) in O(n),π andπ′ the respective quotient maps, and τ the induced
map. Since
SO(n)∩
(
O(n1)× O(n2−n1)×···× O(n−nd)
)
= S
(
O(n1)× O(n2−n1)×···× O(n−nd)
)
,
10 K. YE, K. S.-W. WONG, AND L.-H. LIM
τ is injective. To show that it is surjective, let {Vi}d
i=1∈ Flag(n1,...,n d;n) be a ﬂag represented
by some A∈ O(n), i.e., π(A) ={Vi}d
i=1. If det(A) = 1, then we already have τ(π1(A)) ={Vi}d
i=1
by commutativity of the diagram. If det( A) =−1, take any A1∈ O(n1) with det(A1) =−1, set
B =A


A1 0 ··· 0
0 In2−n1 ··· 0
... ... ... ...
0 0 ··· In−nd

∈ SO(n),
and observe that τ(π1(B)) =π(B) =π(A). □
4.1. Orthogonal coordinates for the ﬂag manifold. An immediate consequence of Propo-
sition 4.1 is that the ﬂag manifold is connected. The characterization (9) says that a point on
Flag(n1,...,n d;n) may be represented by the equivalence class of matrices
JQK =


Q


Q1 0 ... 0
0 Q2 ... 0
... ... ... ...
0 0 ... Q d+1

 :Qi∈ O(ni−ni−1), i= 1,...,d + 1,
d+1∏
i=1
detQi = 1


 (11)
for someQ∈ SO(n). We will call such a representation orthogonal coordinates for the ﬂag manifold.
The Lie algebra of S
(
O(n1)× O(n2−n1)×···× O(n−nd)
)
is simply so(n1)× so(n2−n1)×
···× so(n−nd), which we will regard as a Lie subalgebra of block diagonal matrices,
h =





A1 0 ... 0
0 A2 ... 0
... ... ... ...
0 0 ... A d+1

∈ so(n) : A1∈ so(n1),A 2∈ so(n2−n1),...
...,A d+1∈ so(n−nd)


. (12)
Let m be the natural complement of h in so(n),
m =





0 B1,2 ... B 1,d+1
−BT
1,2 0 ... B 2,d+1
... ... ... ...
−BT
1,d+1−BT
2,d+1 ... 0

∈ so(n) : Bij∈ R(ni−ni−1)×(nj−nj−1),
1≤i<j ≤d + 1



. (13)
In particular, we have the direct sum decomposition so(n) = h⊕ m as vector spaces.
The groups O(n) and O(n1)× O(n2−n1)×···× O(n−nd) have the same Lie algebras as SO(n)
and S
(
O(n1)×O(n2−n1)×···× O(n−nd)
)
, namely, so(n) and so(n1)×so(n2−n1)×···× so(n−nd)
respectively. The tangent space of a homogeneous space G/H at any point is a translation of the
tangent space at the identity element JHK∈G/H, which depends only on the Lie algebras g and
h of G and H respectively:
TJHKG/H≃ g/h,
a fact that we will use in the proof of Proposition 4.3. As such we do not need to distinguish the
two homogeneous space structures (8) and (9) when we discuss geometric quantities associated with
tangent spaces, e.g., geodesic, gradient, Hessian, parallel transport. In the sequel we will make free
use of this ﬂexibility in switching between (8) and (9).
Proposition 4.2. Let h and m be as in (12) and (13) andH = O(n1)×O(n2−n1)×···× O(n−nd).
Then the subspace m is AdH-invariant, i.e., Ad(a)(X)∈ m for every a∈H and X∈ m.
Proof. We need to show that Ad(a)(X)∈ m whenevera∈H andX∈ m. For notational simplicity,
we assume d = 2. Let
a =
[
A1 0 0
0 A2 0
0 0 A3
]
and X =
[ 0 B1,2 B1,3
−BT
1,2 0 B2,3
−BT
1,3−BT
2,3 0
]
,
OPTIMIZATION ON FLAG MANIFOLDS 11
where Ai ∈ O(ni−ni−1), i = 1, 2, 3, and Bij ∈ R(ni−ni−1)×(nj−nj−1), 1 ≤ i < j≤ 3. Then
Ad(a)(X) =aXa−1 =aXa T since a is an orthogonal matrix; and we have
aXa T =
[
A1 0 0
0 A2 0
0 0 A3
][ 0 B1,2 B1,3
−BT
1,2 0 B2,3
−BT
1,3−BT
2,3 0
][
AT
1 0 0
0 AT
2 0
0 0 AT
3
]
=
[ 0 A1B1,2AT
2 A1B1,3AT
3
−A2BT
1,2AT
1 0 A2B2,3AT
3
−A3BT
1,3AT
1−A3BT
2,3AT
2 0
]
∈ m
as required. □
We now have all the ingredients necessary for deriving closed-form analytic expressions for the
tangent space, metric, geodesic, geodesic distance, and parallel transport on a ﬂag manifold in
orthogonal coordinates. We begin with the representation of a tangent space as a vector space of
matrices.
Proposition 4.3 (Tangent space I). Let JQK∈ Flag(n1,...,n d;n) = O(n)/
(
O(n1)× O(n2−n1)×
···× O(nd−nd−1)× O(n−nd)
)
be represented by Q∈ O(n). Its tangent space at JQK is given by
TJQK Flag(n1,...,n d;n) ={QB∈ Rn×n :B∈ m}
=



Q


0 B1,2 ... B 1,d+1
−BT
1,2 0 ... B 2,d+1
... ... ... ...
−BT
1,d+1−BT
2,d+1 ... 0

∈ Rn×n : Bi,j∈ R(ni−ni−1)×(nj−nj−1),
1≤i<j ≤d + 1



.
In particular, the dimension of a ﬂag manifold is given by
dim Flag(n1,...,n d;n) =
∑
1≤i<j≤d+1
(ni−ni−1)(nj−nj−1).
Proof. Let M = Flag(n1,...,n d;n). For Q = I, the identity matrix, this follow from TJIKM ≃
g/h≃ m. For Q arbitrary, the left translationLQ :M→M is a diﬀeomorphism, which means that
(dLQ)JIK : TJIKM→ TJQKM is an isomorphism. The result then follows from ( dLQ)JIK(X) = QX
for all X∈TJIKM. □
There are several ways to equip Flag( n1,...,n d;n) with a Riemannian metric but there is a
distinguished choice that is given by a negative multiple of the Killing form of so(n), although we
will not need to introduce this concept.
Proposition 4.4 (Riemannian metric I). The metric g on Flag(n1,...,n d;n) deﬁned by
gJQK(X,Y ) = 1
2 tr(X TY ) (14)
for all X,Y ∈TJQK Flag(n1,...,n d;n) is an SO(n)-invariant metric. If we write
X =Q


0 B1,2 ... B 1,d+1
−BT
1,2 0 ... B 2,d+1
... ... ... ...
−BT
1,d+1−BT
2,d+1 ... 0

, Y =Q


0 C1,2 ... C 1,d+1
−CT
1,2 0 ... C 2,d+1
... ... ... ...
−CT
1,d+1−CT
2,d+1 ... 0

∈ Rn×n,
whereBij,Cij∈ R(ni−ni−1)×(nj−nj−1), 1≤i<j ≤d, then g may be expressed as
gJQK(X,Y ) =
∑
1≤i<j≤d+1
tr(BT
ijCij). (15)
Proof. We will ﬁrst need to establish an Ad SO(n)-invariant inner product on so(n). It is a standard
fact [31] that bi-invariant metrics on a Lie group G are in one-to-one correspondence with Ad G-
invariant inner products on its Lie algebra g. In our case, G = SO(n), g = so(n), and Ad SO(n) :
SO(n)→ GL(so(n)). Since SO(n) is compact, by Proposition 2.4 it has a bi-invariant metric, which
corresponds to an Ad SO(n)-invariant inner product on so(n).
12 K. YE, K. S.-W. WONG, AND L.-H. LIM
Whenn⁄= 2, 4, so(n) is a simple Lie algebra and so the AdSO(n)-invariant inner product is unique
up to a scalar multiple. When n = 2, SO(2) is one-dimensional and thus abelian, so the bi-invariant
metric on SO(2) is unique up to a scalar. When n = 4, SO(4) ≃ SO(3)× SO(3) as Lie groups,
so it has a two-dimensional family of bi-invariant metrics. For all values of n, we may take our
AdSO(n)-invariant inner product (the choice is unique for all n⁄= 4) as
⟨X,Y⟩ := 1
2 tr(X TY ) (16)
for all X,Y ∈ so(n).
LetG = SO(n) andH = S
(
O(n1)×O(n2−n1)×···× O(n−nd)
)
. We will use the characterization
of a ﬂag manifold in (9), i.e., Flag( n1,...,n d;n) = G/H. Since m is a subspace of so(n), the
restriction of⟨·,·⟩ in (16) to m, denoted by⟨·,·⟩m, is an inner product on m. It is easy to verify that
⟨·,·⟩m is AdH-invariant. Taken together with Propositions 2.3, 2.4, and 4.2, we have that ⟨·,·⟩m
uniquely determines a G-invariant metricg on G/H, as required. □
Unsurprisingly the metric g in Proposition 4.4 coincides with the canonical metric on Grass-
mannian (d = 1) introduced in [16]. It also follows from Theorem 2.5 that, with this metric g,
Flag(n1,...,n d;n) is not merely a Riemannian manifold but also a geodesic orbit space. In fact,
g is the only choice of a metric that makes Flag( n1,...,n d;n) into a geodesic orbit space [3].
We will next derive explicit analytic expressions for geodesic (Propositions 4.5 and 4.7), arclength
(Corollary 4.6), geodesic distance (Proposition 4.8), and parallel transport (Proposition 4.9).
Proposition 4.5 (Geodesic I). Let JQK∈ Flag(n1,...,n d;n) = O(n)/
(
O(n1)×···× O(n−nd)
)
and g be the metric in (15). Every geodesic on Flag(n1,...,n d;n) passing through JQK takes the
form
JQ(t)K =


Q exp(tB)


Q1 0 ... 0
0 Q2 ... 0
... ... ... ...
0 0 ... Q d+1

∈ O(n) :Qi∈ O(ni−ni−1), i= 1,...,d + 1


,
for some direction
B =


0 B1,2 ... B 1,d+1
−BT
1,2 0 ... B 2,d+1
... ... ... ...
−BT
1,d+1−BT
2,d+1 ... 0

∈ Rn×n, Bij∈ R(ni−ni−1)×(nj−nj−1),
1≤i<j ≤d + 1. (17)
Proof. Since Flag(n1,...,n d;n) with the metric g in Proposition 4.4 is a geodesic orbit space, the
result follows immediately from Theorem 2.6. □
Corollary 4.6 (Arclength I). The arclength of a geodesic γ(t) = JQ(t)K passing through Q in the
directionB is given by
‖γ(t)‖ =t
[∑
1≤i<j≤d+1
tr(BT
ijBij)
]1/2
=t
√
tr(BTB)
2 ,
whereB is as in (17).
Proof. This follows from the deﬁnition of arclength
‖γ(t)‖ :=
∫ t
0
√
gJQK(γ′(x),γ′(x))dx
and the expressions for g in (14) and (15). □
OPTIMIZATION ON FLAG MANIFOLDS 13
Proposition 4.7 (Geodesic II). Letγ be a geodesic in Flag(n1,...,n d;n) = O(n)/
(
O(n1)×···×
O(n−nd)
)
with γ(0) = JQK for some Q∈ O(n) and γ′(0) = H∈ TJQK Flag(n1,...,n d;n). Let
QTH =VDV T with V ∈ O(n) and
D = diag
([
0 −λ1
λ1 0
]
,...,
[
0 −λr
λr 0
]
, 0n−2r
)
∈ so(n), (18)
where 2r = rank(QTH) and λ1,...,λ r are positive real numbers. Then γ(t) = JUΣ(t)V TK where
U =QV ∈ O(n) and
Σ(t) = diag
([
costλ1 − sintλ1
sintλ1 costλ1
]
,...,
[
costλr − sintλr
sintλr costλr
]
,In−2r
)
∈ O(n). (19)
Proof. By Proposition 4.5, the geodesic γ takes the form γ(t) = JQ exp(tB)K for some B∈ so(n)
and Q∈ O(n) representing γ(0). Hence we have H = γ′(0) = QB and QTH = B. Since B is a
skew-symmetric and thus a normal matrix, by the spectral theorem [5, Theorem 7.25], B =VDV T
for some V ∈ O(n) and D of the form in (18), with 2r = rank(B) = rank(QTH) and λ1,...,λ r are
positive reals as they are singular values of B. Therefore,
Q exp(tB) =UΣ(t)V T,
where U =QV and Σ(t) is as in (19). □
Proposition 4.8 (Geodesic distance). The geodesic distance with respect to the metric g between
JP K, JQK∈ Flag(n1,...,n d;n) = O(n)/
(
O(n1)×···× O(n−nd)
)
is
d(JP K, JQK) =
√∑r
i=1
λ2
i, (20)
whereλ1,...,λ r are positive real numbers such that P TQ =V ΣV T with V ∈ O(n) and
Σ = diag
([
cosλ1 − sinλ1
sinλ1 cosλ1
]
,...,
[
cosλr − sinλr
sinλr cosλr
]
, 0n−2r
)
.
Proof. By Proposition 3.2(iii), we may regard Flag(n1,...,n d;n) as a closed, and therefore compact,
submanifold of Gr(n1,n )×···× Gr(nd,n ). By Theorem 2.7, there is a distance minimizing geodesic
JP exp(tB)K connecting JP K and JQK. By Corollary 4.6, we get (20) with λ1,λ 1,...,λ r,λr the
nonzero singular values of B. Lastly, by Proposition 4.7, we get the decomposition P TQ =V ΣV T
for some V ∈ O(n). □
Let m be as in (13). For B∈ m, we deﬁne a map
ϕB : m→ m, X ↦→ 1
2[B,X ]m := 1
2 projm([B,X ]), (21)
where proj m : so(n)→ m is the projection from so(n) = h⊕ m to m. For example, if d = 2 and
B =


0 B12 B13
−BT
12 0 B23
−BT
13 −BT
23 0

∈ m, X =


0 X12 X13
−X T
12 0 X23
−X T
13 −X T
23 0

∈ m,
where Bij,Xij∈ R(ni−ni−1)×(nj−nj−1), 1≤i<j ≤ 3, then
ϕB(X) =


0 −B12X T
23 +X12BT
23 B11X23−X11B23
X23BT
12−B23X T
12 0 −B11X T
12 +X11BT
12
−X T
23BT
11 +BT
23X T
11 X12BT
11−B12X T
11 0

∈ m.
Proposition 4.9 (Parallel transport I) . Let B,X ∈ TJIK Flag(n1,...,n d;n) ∼= m and JQK ∈
Flag(n1,...,n d;n). The parallel transport of QX ∈ TJQK Flag(n1,...,n d;n) along the geodesic
JQ exp(tB)K is
X(t) =Q exp(tB)e−ϕtB(X), (22)
14 K. YE, K. S.-W. WONG, AND L.-H. LIM
wheree−ϕB : m→ m, for ϕB as in (21), is deﬁned by
e−ϕB =
∞∑
k=0
(−1)k
k! ϕk
B. (23)
Proof. This follows from applying [36, Lemma 3.1] to Flag( n1,...,n d;n). □
For the d = 1 case, i.e., Flag( k;n) = Gr(k,n ), it is straightforward to verify that [ B,X ]m = 0
for all B,X ∈ m. So the expression for parallel transport in (22) reduces to X(t) = Q exp(tB)X,
which is the well-known expression for parallel transport on the Grassmannian [16].
4.2. Stiefel coordinates for the ﬂag manifold. We next discuss the characterization of a ﬂag
manifold as a quotient of the Stiefel manifold (10) and discuss its consequences. This characteri-
zation will give our coordinates of choice for use in our optimization algorithms (see Section 6).
Proposition 4.10. Let 0 < n1 < ··· < nd < n be d positive integers. The ﬂag manifold
Flag(n1,...,n d;n) is diﬀeomorphic to the homogeneous space
V(nd,n )/
(
O(n1)× O(n2−n1)×···× O(nd−nd−1)
)
(24)
where V(nd,n ) is the Stiefel manifold of orthonormal nd-frames in n.
Proof. This follows from the standard characterization of V(nd,n ) is a homogeneous space ofO(n),
V(nd,n )∼= O(n)/ O(n−nd), together with (8). □
For the rest of this article, we will regard the Stiefel manifold V( k,n ) as the set of all n×k
matrices whose column vectors are orthonormal. With this identiﬁcation, Proposition 4.10 allows
us to represent a ﬂag {Vi}d
i=1∈ Flag(n1,...,n d;n) by a matrix Y = [y1,...,y nd]∈ Rn×nd with
orthonormal y1,...,y nd∈ Rn and where the ﬁrst ni of them span the subspace Vi, i = 1,...,d .
This representation is not unique but if Y′∈ Rn×nd is another such matrix, then
Y′ =Y


Q1 0 ... 0
0 Q2 ... 0
... ... ... ...
0 0 ... Q d

, Q i∈ O(ni−ni−1), i = 1,...,d. (25)
Hence{Vi}d
i=1∈ Flag(n1,...,n d;n) may be represented by the equivalence class of matrices
JY K =


Y


Q1 0 ... 0
0 Q2 ... 0
... ... ... ...
0 0 ... Q d

∈ Rn×nd : Y ∈ V(nd,n ), span{y1,...,y ni} = Vi,
Qi∈ O(ni−ni−1), i= 1,...,d


. (26)
We will call such a representation Stiefel coordinates for the ﬂag manifold.
In the following, for any k<n , we write
In,k :=
[
Ik
0
]
∈ Rn×k,
i.e., the n×k matrix comprising the ﬁrst k columns of the n×n identity matrix In. Thus for any
A = [a1,...,a n]∈ Rn×n, AIn,k = [a1,...,a k]∈ Rn×k gives us the ﬁrst k columns of A.
For a ﬂag{Vi}d
i=1, it is easy to convert between its orthogonal coordinates, i.e., JQK in (11) with
Q∈ O(n), and its Stiefel coordinates, i.e., JY K in (26) withY ∈ V(nd,n ). Given Q∈ O(n), one just
takes its ﬁrstnd columns to getY =QIn,nd; note thatQIn,ni is automatically an orthonormal basis
for the subspace Vi,i = 1,...,d . Given Y ∈ V(nd,n ), take any orthonormal basisY⊥∈ V(n−nd,n )
of the orthogonal complement of im(Y ) to get Q = [Y,Y ⊥]∈ O(n).
We now derive expressions for tangent space, metric, arclength, geodesic, and parallel transport
in Stiefel coordinates.
OPTIMIZATION ON FLAG MANIFOLDS 15
Proposition 4.11 (Tangent space II). Let JY K∈ Flag(n1,...,n d;n) = V(nd,n )/
(
O(n1)× O(n2−
n1)×···× O(nd−nd−1)
)
be represented by Y ∈ V(nd,n ). Its tangent space at JY K is given by
TJY K Flag(n1,...,n d;n) ={[Y,Y ⊥]BIn,nd∈ Rn×nd :B∈ m},
whereY⊥∈ V(n−nd,n ) is such that [Y,Y ⊥]∈ O(n) and m is as in (13).
Proof. The calculation is straightforward and details can be found in [29]. Essentially it follows
from diﬀerentiating a curveτ(t) in Flag(n1,...,n d;n) withτ(0) = JY K and noting that the tangent
vectorτ′(0) is perpendicular to h in (12), whose orthogonal complement is precisely m. □
The description of TJY K Flag(n1,...,n d;n) in Proposition 4.11 is a parametric one (like the de-
scription of the unit circle as{(cosθ, sinθ) :θ∈ [0, 2π)}). We may also derive an implicit description
of TJY K Flag(n1,...,n d;n) (like the description of the unit circle as {(x,y ) :x2 +y2 = 1}).
Corollary 4.12 (Tangent space III). Let JY K∈ Flag(n1,...,n d;n) = V(nd,n )/
(
O(n1)× O(n2−
n1)×···× O(nd−nd−1)
)
be represented by Y ∈ V(nd,n ). Let Y be partition as
Y = [Y1,...,Y d], Y i∈ V(ni−ni−1,n ), i = 1,...,d.
Then its tangent space at JY K is given by
TJY K Flag(n1,...,n d;n) ={[X1,...,X d]∈ Rn×nd :Xi∈ Rn×(ni−ni−1),
Y T
i Xj +X T
iYj = 0, YT
i Xi = 0, 1≤i,j ≤d}. (27)
Equivalently, the matrix [X1,...,X d] can be expressed as
[X1,...,X d] = [Y1,...,Y d,Y ⊥]


0 B1,2 ... B 1,d
−BT
1,2 0 ... B 2,d
... ...
... ...
−BT
1,d −BT
2,d ... 0
−BT
1,d+1−BT
2,d+1 ... −BT
d,d+1

,
whereY⊥∈ V(n−nd,n ) is such that [Y,Y ⊥]∈ O(n) and Bij∈ R(ni−ni−1)×(nj−nj−1), 1≤i<j ≤
d + 1.
Proof. Since [Y1,...,Y d]∈ V(nd,n ) and Yi∈ V(ni−ni−1,n ), the Yi’s are characterized by
Y T
i Yi =Ini−ni−1, Y T
i Yj = 0, i ⁄=j = 1,...,d. (28)
Diﬀerentiating (28) gives us the ﬁrst relation in (27). On the other hand, by Proposition 4.11 we
notice that a tangent vector in TJY K Flag(n1,...,n d;n) is written as [Y,Y ⊥]BIn,nd for some B∈ m,
from which we may easily verify the second relation in (27). □
Comparing Propositions 4.3 and 4.11, for a tangent vector QB ∈ TJQK Flag(n1,...,n d;n) in
orthogonal coordinates Q∈ O(n), its corresponding tangent vector in Stiefel coordinates Y =
QIn,nd∈ V(nd,n ) is simply given byQBIn,nd∈TJY K Flag(n1,...,n d;n). Conversely, [Y,Y ⊥]BIn,nd∈
TJY K Flag(n1,...,n d;n) in Stiefel coordinates corresponds to QB∈ TJQK Flag(n1,...,n d;n) in or-
thogonal coordinates where Q = [Y,Y ⊥]. Note that from the matrix BIn,nd, i.e., just the ﬁrst nd
columns of B∈ m, the full matrix B can be easily and uniquely recovered by its skew symmetry.
The straightforward translation between orthogonal and Stiefel coordinate representations of
points and tangent vectors on a ﬂag manifold allows us to immediately deduce analogues of Propo-
sitions 4.4, 4.5, 4.9, and Corollary 4.6.
Proposition 4.13 (Riemannian metric II) . The metric g at a point JY K∈ Flag(n1,...,n d;n) =
V(nd,n )/
(
O(n1)× O(n2−n1)×···× O(nd−nd−1)
)
is given by
gJY K(W,Z ) =
∑
1≤i<j≤d+1
tr(BT
ijCij), (29)
16 K. YE, K. S.-W. WONG, AND L.-H. LIM
whereW,Z∈TJY K Flag(n1,...,n d;n) are
W = [Y,Y ⊥]


0 B1,2 ... B 1,d
−BT
1,2 0 ... B 2,d
... ... ... ...
−BT
1,d −BT
2,d ··· 0
−BT
1,d+1−BT
2,d+1 ... −BT
d,d+1

, Z = [Y,Y ⊥]


0 C1,2 ... C 1,d
−CT
1,2 0 ... C 2,d
... ... ... ...
−CT
1,d −CT
2,d ··· 0
−CT
1,d+1−CT
2,d+1 ... −CT
d,d+1

∈ Rn×nd.
Proposition 4.14 (Arclength II, Geodesics III). Let JY K∈ Flag(n1,...,n d;n) = V(nd,n )/
(
O(n1)×
O(n2−n1)×···× O(nd−nd−1)
)
andg be the metric in (29). Every geodesic γ on Flag(n1,...,n d;n)
passing through JY K takes the form
γ(t) = JY (t)K =



[Y,Y ⊥] exp(tB)


Q1 0 ... 0
0 Q2 ... 0
... ... ... ...
0 0 ... Q d
0 0 ... 0

∈ V(nd,n ) : Qi∈ O(ni−ni−1),
i = 1,...,d



,
where [Y,Y ⊥]∈ O(n) and B∈ m. In particular, the arclength of γ(t) is
‖γ(t)‖ =t
[∑
1≤i<j≤d+1
tr(BT
ijBij)
]1/2
.
Proposition 4.15 (Parallel transport II). Let JY K∈ Flag(n1,...,n d;n) and
[Y,Y ⊥]BIn,nd, [Y,Y ⊥]XIn,nd∈TJY K Flag(n1,...,n d;n).
The parallel transport of [Y,Y ⊥]XIn,nd along the geodesic J[Y,Y ⊥] exp(tB)In,ndK is given by
X(t) = [Y,Y ⊥] exp(tB)e−ϕtB(X)In,nd, (30)
with e−ϕtB deﬁned as in (21) and (23).
While is also straightforward to obtain analogues of Proposition 4.7 and 4.8 in Stiefel coordinates,
we omit them as the expressions are more involved and we will not need them in the sequel.
