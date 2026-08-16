---
doc_id: arxiv-math-0611504v1
doc_title: "QUANTUM HYPERBOLIC GEOMETRY"
section_id: sec-004-23-qhg-universal-functor
section_title: "QHG universal functor"
section_number: 2.3
pages: 9-14
source_pdf: 0611504v1.pdf
source_sha256: a33d2771c873a97e
doc_brief: "Quantum hyperbolic geometry STEPHANE BASEILHAC RICCARDO BENEDETTI — 19 sections: Introduction; Universal QHG; Building blocks"
duplicate_of: "agt-v7-n2-p13-s"
---
pseudomanifold (Z, T ) a trace tensor HN (T ), as follows. Deﬁne an N -state of T as a function that
gives every 2-simplex an index, with values in {0,...,N − 1}. Every N -state determines an entry
for each matrix dilogarithm RN (∆ ,b,w,f,c ). As two tetrahedra induce opposite orientations on a
common 2-face, an index is down for the RN of one tetrahedron while it is up for the other (see Figure
1). By summing over repeated indices we get the total contraction of the tensors {RN (∆ ,b,w,f,c )},
that we denote ∏
∆ ⊂T RN (∆ ,b,w,f,c ). Let vI and vδ be the number of vertices of T \∂T and ∂T ,
respectively, that correspond to manifold points. We set
(11) HN (T ) = N −(vδ/2+vI ) ∏
∆ ⊂T
RN (∆ ,b,w,f,c )
The type of a trace tensor HN (T ) depends on the b-signs of the boundary triangles of ( T,b ). The
matrix dilogarithms themselves are special instances of trace tens ors.
We have
Proposition 2.5. For every odd N ≥ 1, up to sign and multiplication by N th roots of unity the trace
tensor HN (T ) is invariant up to QHG isomorphism.
This result is a restatement of Theorem 2.1 (2) and Lemma 6.7 of [5], an d summarizes the fundamental
functional relations satisﬁed by the matrix dilogarithms. In particu lar those corresponding to 2 ↔ 3
QHG transits are usually called ﬁve terms identities . In Figure 5 we show one instance in dual terms.
The normalization factor N −vI in (11) is due to the bubble move, that changes by 1 the number of
internal vertices.
y
x2
x
x3
x1
=
Figure 5. A 2 ↔ 3 QHG move ( x1 = y/x, x2 = y(1 −x)/x(1 −y), and x3 =
(1 −x)/(1 −y)).
The notions of “boundary” (also allowing only portions of the standa rd boundary - see eg. [30]),
bordism, and bordism gluing are well deﬁned for the category of QHG triangulated pseudomanifolds
considered up to QHG isomorphisms . Hence, for every odd N ≥ 1, the association of the trace tensor
to each bordism deﬁnes a functor. Note that the identities betwee n trace tensors hold up to the phase
ambiguity of Proposition 2.5. Also, the normalization factor N −vδ/2 in (11) compensates the change
in the number of internal vertices when gluing along complete connected components of the (usual)
boundary (this is easily adapted to more general gluings).
10 ST ´EPHANE BASEILHAC 1 AND RICCARDO BENEDETTI 2
Any bordism is the gluing of ﬂat/charged I-tetrahedra, considered as elementary bordisms between
the couples of 2-faces having b-sign equal to −1 or +1. The matrix dilogarithms can be interpreted as
the amplitudes of a diagonal exchange that relates two quadrilater al triangulations (recall the above
discussion about the geometric quantization derivation of matrix dilo garithms.)
2.4. T owards geometric specializations. The category of QHG triangulated pseudomanifolds is
built ad hoc on the functional properties of the matrix dilogarithms. In order t o eventually get
specializations with a geometric content, such as QHFT, it is necessa ry to reﬁne more and more our
rough ﬂat/charged I-triangulations. In fact we have to impose some global constraints that would
be preserved by (possibly reﬁned) QHG isomorphisms. It is useful t o recall at once some of these
reﬁnements, and related matter. We adopt the notations introdu ced above.
Deﬁnition 2.6. A triple T = (T,b,w ) is an I-triangulation if at each edge e not contained in ∂T
we have the edge compatibility relation WT (e) = 1. We say that T = ( T,b,w,f ) is a ﬂattened
I-triangulation (and f a global ﬂattening ) if moreover LT (e) = 0.
It is easily seen that the collection of cross-ratio moduli of an I-triangulation T of a pseudomanifold
Z deﬁnes a PL pseudo developing map d : ˜Z → H
3
, unique up to post composition with the action
of PSL (2, C), and a holonomy representation h :π1(Z) →PSL (2, C) such that d(γ(y)) = h(γ)(d(y))
for every γ ∈π1(Z), y ∈ ˜Z.
Our main tool for producing I-triangulations is the following idealization procedure:
Deﬁnition 2.7. Let T = (T,b,z ) be a branched triangulation of a pseudomanifold Z equipped with
a PSL (2, C)-valued 1-cocycle z, where the cocycle relation is z(e0)z(e1)z(e2)−1 = 1 on a branched
triangle with edges e0,e1 ande2. A 3-simplex ∆ of ( T,b,z ) with vertices x0,x 1,x 2,x 3 is idealizable if
(12) u0 = 0, u1 =z(x0x1)(0), u2 =z(x0x2)(0), u3 =z(x0x3)(0)
are four distinct points in C ⊂ CP1 = ∂H
3
. The convex hull is a hyperbolic ideal tetrahedron
with ordered vertices, denoted ( u0,u 1,u 2,u 3). Let us give each edge e of ∆ the cross-ratio modulus
w(e) ∈ C\{0, 1} of the corresponding edge in ( u0,u 1,u 2,u 3), and put w = (w0,w 1,w 2) ∈ (C\{0, 1})3.
We call (∆ ,b,w ) the idealization of (∆ ,b,z ). If all 3-simplices of ( T,b,z ) are idealizable we say that
TI = (T,b,w ) is the idealization of T .
Note that the idealization includes the choice of a base point (ie. 0 in De ﬁnition 2.7; we make this
choice once for ever). The idealization of each single 3-simplex stron gly depends on this choice, but
taking a diﬀerent base point is equivalent to conjugating the cocycle z. Not all branched triangulations
support idealizable cocycles (for example an ideal triangulation of a k not inS3 only supports the trivial
constant cocycle). However, when it exists we have:
Lemma 2.8. ([4], section 2.4) The idealization TI is an I-triangulation of Z.
The following fact will be important below (a version of it was implicitely us ed in [4]; see (3), Lemma
2.12 and §3.2 in that paper):
Lemma 2.9. The idealization TI is canonically ﬂattened by taking for each 3-simplex the log-branches
(with the notations of Deﬁnition 2.7):
l0 := log(u2 −u1) + log(u3) − log(u2) − log(u3 −u1)
l1 := log(u2) + log(u3 −u1) − log(u0) − log(u3 −u2) +
√
−1π
l2 := log(u3 −u2) + log(u0) − log(u3) − log(u2 −u1) −
√
−1π.
Moreover, replacing at each edge of TI the standard log with any other log determination still makes
it ﬂattened.
Proof. These expressions are just (corrected) signed sums of the stan dard logs of the edge vectors
in the cross-ratio moduli w0 = (u2 −u1)u3/u2(u3 −u1), w1 = u2(u3 −u1)/u0(u3 −u2) and w2 =
−(u3 −u2)u0/(u2 −u1)u3. They clearly deﬁne triples of log-branches. The idealizations for tw o
distinct branchings with the same b-orientation are related by an element in PSL (2, C), that is, a
conformal transformation of CP 1. We deduce that triples (l 0, l1, l2) are invariant under a change of
QUANTUM HYPERBOLIC GEOMETRY 11
branching, because the angle formed by any pair of vectors is pres erved (for instance u2 −u1 and u2,
or u3 and u3 −u1). Then, the edge compatibility relations LT (e) = 0 follow easily by developing the
tetrahedra around e with branchings such that e =e0, similarly as for Lemma 2.8. For the last claim
we note that any log correction appears for each 3-simplex in two dis tinct lj, with opposite signs. ✷
Distinguished ﬂat/charged I-triangulations. Given an arbitrary non empty and properly embed-
ded tangle L inZ, we say that ( T,H ) and T = (T,H,b,w,f,c ) are distinguished ifH is a subcomplex
of the 1-skeleton of T isotopic to L and passing through all the vertices that are manifold points, and
containing no singular vertices (we say that H is Hamiltonian).
Deﬁnition 2.10. A distinguished I-triangulation T = (T,H,b,w,f,c ) is ﬂat/charged iff is a global
ﬂattening, and
(13) CT (e) =
{
0
2
if e ⊂H
if e ⊂T \ (H ∪∂T )
In such a case c is said a global charge.
The existence of global ﬂattenings of an arbitrary I-triangulation with empty boundary, and of global
charges (such that CT (e) = 2 at all edges e) on any topological ideal triangulation of an oriented 3-
manifold whose boundary consists of tori, was proved by Neumann in [25], section 9, and [24], section
6, respectively. This last result is easily adapted to the existence of global charges on distinguished
triangulations (T,H ) (see [4], Theorem 4.7).
We have to reﬁne the QHG isomorphisms in order to deal with distinguis hed ﬂat/charged I-
triangulations. First we have to incorporate the Hamiltonian tangles into the bare moves. Any
positive 2 → 3 move T → T ′ naturally specializes to a move ( T,H ) → (T ′,H ′); in fact H ′ = H is
still Hamiltonian. For positive bubble moves, we assume that an edge e of H lies in the boundary
of the involved 2-simplex f ; then e lies in the boundary of a unique 2-simplex f ′ of T ′ containing
the new vertex of T ′. We deﬁne the Hamiltonian subcomplex H ′ of T ′ just by replacing e with the
other two edges of f ′. The inverse moves are deﬁned in the same way; in particular, for ne gative
3 → 2 moves we require that the edge disappearing in T belongs to T ′ \H ′. The 2 ↔ 3 QHG transit
specializes verbatim. For the bubble transit we just impose that the marked edge e (see section 2.2)
coincides with the above edge of H. Thanks to (9) and (10) we see that distinguished ﬂat/charged
I-triangulations are closed under such reﬁned QHG transits.
Remark 2.11. The residue mod(2
√
−1πN ) of the classical log-branches of a ﬂattened I-triangulation
are equivalently given byN th rootsw′(h) of the cross-ratio moduli w(h) such thatw′(e1)w′(e2)w′(e3) =
1 at each 3-simplex and ∏
h∈ǫ−1
T (e)w′(h)∗b = 1 at each edge, with the notations of (7). For level N
quantum log-branches of distinguished ﬂat/charged I-triangulations this is replaced with
w′(e1)w′(e2)w′(e3) = exp( − ∗b
√
−1π/N)
and ∏
h∈ǫ−1
T (e)
w′(h)∗b =
{ 1
exp(−2
√
−1π/N)
if e ⊂H
otherwise.
Cohomological weights and structural facts. Given an I-triangulation T = (T,b,w ) without
boundary, letT0 be the complement of an open cone neighborhood of each 0-simplex. This is a disjoint
union of triangulated closed oriented surfaces, the links of the ver tices in T . To each ﬂattening f of
T a class γ(f ) ∈ H 1(∂T0; C) is associated as follows. Represent any non zero integral 1-homo logy
class a of ∂T0 by “normal paths”, that is, a disjoint union of oriented essential s imple closed curves
transverse to the triangulation and such that no component ente rs and exits from the same face of
a 2-simplex. Such a curve selects a vertex for each 2-simplex. The v alue γ(f )(a) is deﬁned as the
signed sum of the log-branches of the edges ending at the vertices selected by a. For each vertex v the
sign is ∗b if the path goes in the direction given by the orientation of ∂T0 as viewed from v, and −∗b
otherwise. Using the edge compatibility relations of Deﬁnition 2.6 it is ea sily checked that γ(f ) does
not depend on the choice of normal path representative. If the h olonomy of T is trivial or parabolic
about each (non manifold) point this class takes values in 2 Z ([25], Proposition 5.2). Similarly we can
12 ST ´EPHANE BASEILHAC 1 AND RICCARDO BENEDETTI 2
deﬁne γ2(f ) ∈H 1(T0; Z/2Z) by using normal paths in T0 and taking modulo 2 sum of the ﬂattenings
we meet along the paths. We call ( γ(f ),γ 2(f )) the (cohomological) weight of f . These deﬁnitions
extend immediately to global charge, replacing log-branches with ch arges; then branchings are not
needed to compute the signed sums (ie. put ∗b = 1).
In [24], section 4 (see also [25], section 9), Neumann deﬁnes an integr al chain complex J such that
global charges are deﬁned from cycles at level 3. The maps γ and γ2 above are well-deﬁned on the
third homology group H3(J ) and satisfy:
Theorem 2.12. ([24], Theorem 5.1) The sequence
0 →H3(J )
(γ2,γ)
− →H 1(T0; Z/2Z) ⊕H 1(∂T0; Z)
i∗−r
− →H 1(∂T0; Z/2Z) → 0
is exact, where r : H 1(∂T0; Z) → H 1(∂T0; Z/2Z) is the coeﬃcient map and i∗ : H 1(T0; Z/2Z) →
H 1(∂T0; Z/2Z) is induced by the inclusion ∂T0 →T0.
In particular, any pair ( h,k ) ∈ H 1(T0; Z/2Z) ×H 1(∂T0; Z) with r(k) = i∗(h) is a weight for some
global charges. This fact extends to log-branches as follows. Ass ume that the holonomy of T restricted
to each component of ∂T0 takes values in a Borel subgroup of PSL (2, C), so that it ﬁxes some point in
∂H
3
. Let γ′ be deﬁned as above, except that for each 3-simplex log-branches are taken with ﬂattenings
f0 =f1 = 0. It can be checked that γ′(a) is the logarithm of the derivative of the holonomy of a (a
similarity), up to multiples of 2
√
−1π. Then, any pair ( h,k ) ∈H 1(T0; Z/2Z) ×H 1(∂T0; C) such that
(14)
{
(k −γ′)/
√
−1π ∈H 1(∂T0; Z)
r((k −γ′)/
√
−1π) = i∗(h)
is a weight for some ﬂattening. For instance, when γ′(a) ∈ 2
√
−1πZ for all a the ﬁrst condition means
that k is integral.
Finally, the structure of the spaces of ﬂattenings and integral ch arges is given by Theorem 2.4 in
[24]. For each ﬁxed weight ( h,k ) they form an aﬃne space over an integral lattice. Generators ha ve
the following combinatorial realization: for each 3-simplex in the star of an edge e, add +1 to the
ﬂat/charges of one of the two other pairs of opposite edges, and −1 for the other pair, so that the
total log-branches or charges stay equal everywhere. In part icular, for ﬂattenings of an idealization TI
any generator is obtained by adding +1 to the log determination at so me edge. Hence any ﬂattening
of TI inducing the weight of the canonical ﬂattening of Lemma 2.9 diﬀers fr om it as described in the
statement.
We note that the above reﬁned QHG isomorphisms preserve the weig hts (see eg. Lemma 4.12 in
[4]). The diﬀerence in considering global ﬂattenings or charges with d iﬀerent mod(2) weights in
H 1(T0; Z/2Z) seems to carry not so essential information (see Theorem 5.4 and Remark 5.5). This
contrasts with boundary weights in H 1(∂T0; Z), which play a key role in surgery formulae (see [25],
theorems 14.5 and 14.7, and section 6.2 below). We note that a proce ss involving 2-handle surgery
allows to deﬁne explicit isomorphisms between lattices of ﬂat/charge s with diﬀerent boundary weights
(see [25], section 11, p. 457).
3. Parameters for PSL (2, C)-characters of surfaces
Fix a compact closed oriented surface S of genus g with a non empty set V = {v1,... ,v r} of marked
points, and negative Euler characteristic χ(S \V )< 0. Denote by π the fundamental group of S \V ,
and by
R(g,r ) = Hom(π,PSL (2, C))/PSL (2, C)
the set of all conjugacy classes of PSL (2, C)-valued representations of π. The group π is free of rank
κ = 2g+r−1. Any choice of free generators of π identiﬁes the set Hom(π,PSL (2, C)) withPSL (2, C)κ.
Diﬀerent such identiﬁcations are related by algebraic automorphism s of PSL (2, C)κ. Moreover, the
isomorphism PSL (2, C) ∼
= SO(3, C) induced by the adjoint action Ad : PSL (2, C) → Aut(sl(2, C))
implies that Hom(π,PSL (2, C)) is an aﬃne complex algebraic set, with the complex algebraic action
of PSL (2, C) by conjugation.
QUANTUM HYPERBOLIC GEOMETRY 13
As the rough topological quotient space R(g,r ) is not Hausdorﬀ, it is more convenient to consider the
algebro-geometric quotient
X(π) = Hom(π,PSL (2, C))//PSL (2, C)
of invariant theory, called the variety of PSL (2, C)-characters (see eg. [19]). Recall that X(π) is a
complex aﬃne algebraic set such that there exists a surjective reg ular map
t : Hom(π,PSL (2, C)) →X(π)
inducing an isomorphism t∗ between the regular functions on X(π) and the regular functions on
Hom(π,PSL (2, C)) invariant by conjugation. In general t(γ) = t(σ) does not imply that γ and σ are
conjugate, but this is true if we restrict to irreducible representations: we have Homirr(π,PSL (2, C)) =
t−1(Xirr(π)), where Xirr(π) = t(Homirr(π,PSL (2, C)), so that the (restricted) rough quotient
R(g,r )irr and the algebraic quotient Xirr(π) coincide.
We can deal with the whole of R(g,r ) to construct the QHFT. Hence below we treat the complex di-
mension of subsets of R(g,r ) somewhat formally, as everything can be substantiated in terms o fX(π),
or by restriction to Xirr(π). For instance, as PSL (2, C) has trivial centre and complex dimension 3
we say that the complex dimension of R(g,r ) is 3κ − 3 = −3χ(F ).
3.1. Eﬃcient triangulations. Fix a surface F withr boundary components, obtained by removing
from S the interior of small 2-disks Di such that vi ∈∂Di.
A triangulation T ′ of S with the set of vertices equal to V is called a topological ideal triangulation
of S \V . Given such a T ′, we need a marking of corners of the 2-simplices. The best suited to
3-dimensional extension are induced by global branchings b′ of T ′, and it is known that pairs ( T ′,b ′)
always exist. Then, as in section 2, we have a sign function σ = σ(T ′,b′). A corner map v ↦→cv
associates to each vertex v of T ′ the corner at v of a triangle, say tv, in its star. We say that v ↦→cv
is t-injective if v ↦→tv is injective.
Lemma 3.1. For every (g,r ) ⁄= (0, 3), every triangulation T ′ of S with r vertices admits t-injective
corner maps.
Proof. For (g,r ) = (0 , 4) or g > 0 and r = 1, it is immediate to construct such a triangulation.
Subdividing a triangle by taking the cone from an interior point preser ves the existence of t-injective
corner maps. By induction on r we deduce that for every ( g,r ) ⁄= (0, 3) there exist triangulations of
S as in the statement.
In Figure 6 the corner selection is speciﬁed by a ∗, and the rows show all the possible ﬂip moves on
triangulations of S, up to obvious symmetries, that preserve the injectivity of corne r maps. Consider
triangulations T ′, T ′′ of S with r vertices, such that T ′′ supports a t-injective corner map. It is well
known that T ′′ is connected to T ′ via a ﬁnite sequence of ﬂips. The t-injective corner map for T ′′
yields a t-injective corner map for T ′ by decorating these ﬂips as in Figure 6. ✷
*
*
*
*
*
*
*
*
*
*
Figure 6. The ﬂips with marked corners.
14 ST ´EPHANE BASEILHAC 1 AND RICCARDO BENEDETTI 2
There are no obstructions to use arbitrary corners maps in what f ollows. Specializing to injective ones
just simpliﬁes the exposition. For ( g,r ) = (0 , 3), triangulations have two 2-simplices, one with two
selected corners. From now on, we assume that ( g,r ) ⁄= (0, 3), the extension to the (0 , 3) case being
straightforward.
Given a pair ( g,r ) ⁄= (0, 3) and (T ′,b ′) as in Lemma 3.1, ﬁx a t-injective corner map v ↦→cv. In the
interior of each triangle tv consider a bigon Dv with one vertex at v, and call v′ the other vertex.
Remove from tv the interior of Dv, and triangulate the resulting cell sv =tv \ Int(Dv) by taking the
cone with base v′. Repeating this procedure for each tv, we get a triangulation T ofF with 2r vertices
and p + 2r triangles, where p denotes the number of triangles of T ′. The set of edges of T , E(T ),
containsE(T ′) in a natural way, and |E(T )| = |E(T ′)| + 4r. We extend b′ to a branching b onT as in
in Figure 7, and the sign function σ(T ′,b′) to the triangles of ( T,b ) in the natural way. Note that the
ﬁgure shows only one of the possible branching conﬁguration. In ge neral we extend b′ tob so that we
can recover (T ′,b ′) from ( T,b ) by “zipping” and “collapsing”, as suggested at the bottom of Figur e
7. In what follows, for simplicity we will refer to this conﬁguration, as the treatment of the others is
similar.
v
v v v
T T" T’
zip
Figure 7. The branched triangulated cell sv.
Deﬁnition 3.2. We call the pair ( T,b ) an eﬃcient triangulation (for short: e-triangulation) of F .
For each vertex v, the preferred innner triangle at v is the triangle τv insv with an edge on ∂F whose
b-orientation coincides with the boundary orientation of F .
