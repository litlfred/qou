---
doc_id: 0307092v2
doc_title: "Extended Bloch group and the Cheeger-Chern-Simons class"
section_id: sec-002-3-parameters-for-ideal-hyperbolic-simplices
section_title: "Parameters for ideal hyperbolic simplices"
section_number: 3
pages: 8-14
source_pdf: 0307092v2.pdf
source_sha256: de2f7ddec49b2ce6
doc_brief: "Extended Bloch group and the Cheeger-Chern-Simons class — We deﬁne an extended Bloch group and show it is naturally isom orphic to H3(PSL(2, C)δ; Z)."
---
In this section we shall interpret ˆC as a space of parameters for what we call
“combinatorial ﬂattenings” of ideal hyperbolic simplices . We need this to deﬁne
the above map λ. It also gives a geometric interpretation of the lifted ﬁve t erm
relation.
We shall denote the standard compactiﬁcation of H3 by
H
3
= H3 ∪ CP 1 . An
ideal simplex ∆ with vertices z0, z1, z2, z3 ∈ CP 1 is determined up to congru-
ence by the cross-ratio
z = [z0 : z1 : z2 : z3] = (z2 − z1)(z3 − z0)
(z2 − z0)(z3 − z1) .
Permuting the vertices by an even (ie, orientation preservi ng) permutation re-
places z by one of
z, z ′ = 1
1 − z , or z′′ = 1 − 1
z .
The parameter z lies in the upper half plane of C if the orientation induced
by the given ordering of the vertices agrees with the orienta tion of H3 . But
we allow simplices whose vertex ordering does not agree with their orientation.
We also allow degenerate ideal simplices whose vertices lie in one plane, so
the parameter z is real. However, we always require that the vertices are
distinct. Thus the parameter z of the simplex lies in C − {0, 1} and every such
z corresponds to an ideal simplex.
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class 421
There is another way of describing the cross-ratio paramete r z = [z0 : z1 : z2 : z3]
of a simplex. The group of orientation preserving isometrie s of H3 ﬁxing the
points z0 and z1 is isomorphic to C∗ and the element of this C∗ that takes z2
to z3 is z (equivalently: if we position z0, z1 at 0 , ∞ in the upper half-space
model of H3 then z3 = zz2 ). Thus the cross-ratio parameter z is associated
with the edge z0z1 of the simplex 1. The parameter associated in this way with
the other two edges z0z3 and z0z2 out of z0 are z′ and z′′ respectively, while
the edges z2z3 , z1z2 , and z1z3 have the same parameters z , z′ , and z′′ as their
opposite edges. See Figure 1.
PSfrag replacements
z z
z0
z1z2
z3 z′
z′
z′′
z′′
Figure 1
Note that zz ′z′′ = −1, so the sum
log z + log z′ + log z′′
is an odd multiple of πi , depending on the branches of log used. In fact, if we
use standard branch of log then this sum is πi or −πi depending on whether
z is in the upper or lower half plane.
The imaginary parts of log z , log z′ , and log z′′ are the dihedral angles of the
ideal simplex (resp. their negatives if the vertex ordering does not agree with
the orientation the simplex inherits from H3 ). We now consider certain “ad-
justments” of these angles by multiples of π .
Deﬁnition 3.1 We shall call any triple of the form
w = (w0, w1, w2) = (log z + pπi, log z′ + qπi, log z′′ + rπi)
with
p, q, r ∈ Z and w0 + w1 + w2 = 0
1It is associated with the unoriented edge since there is an orientation preserving
symmetry of the simplex exchanging z0 and z1 (it also exchanges z2 and z3 and acts
on C∗ by z ↦→1/z ).
Geometry & Topology, Volume 8 (2004)
422 Walter D Neumann
a combinatorial ﬂattening for our simplex.
Each edge E of ∆ is assigned one of the components wi of w, with opposite
edges being assigned the same component. We call wi the log-parameter for
the edge E and denote it lE(∆ , w).
This combinatorial ﬂattening can be written
ℓ(z; p, q) := (log z + pπi, − log(1 − z) + qπi, log(1 − z) − log z − (p + q)πi),
and ℓ is then a map of ˆC to the set of combinatorial ﬂattenings of simplices.
Lemma 3.2 This map ℓ is a bijection, so ˆC may be identiﬁed with the set of
all combinatorial ﬂattenings of ideal tetrahedra.
Proof We must show that we can recover ( z; p, q) from ( w0, w1, w2)=ℓ(z; p, q).
It clearly suﬃces to recover z . But z = ±ew0 and 1 − z = ±e−w1 , and the
knowledge of both z and 1 − z up to sign determines z .
We can give a geometric interpretation of the choice of param eters in the ﬁve
term relation (2). If z0, . . . , z4 are ﬁve distinct points of ∂H
3
, then each choice of
four of ﬁve points z0, . . . , z4 gives an ideal simplex. We denote the simplex which
omits vertex zi by ∆ i . The cross ratio parameters xi = [ z0 : . . . : ˆzi : . . . : z4]
of these simplices can be expressed in terms of x := x0 and y := x1 as follows:
x0 = [z1 : z2 : z3 : z4] =: x
x1 = [z0 : z2 : z3 : z4] =: y
x2 = [z0 : z1 : z3 : z4] = y
x
x3 = [z0 : z1 : z2 : z4] = 1 − x−1
1 − y−1
x4 = [z0 : z1 : z2 : z3] = 1 − x
1 − y
The lifted ﬁve term relation has the form
4∑
i=0
(−1)i(xi; pi, qi) = 0 (4)
with certain relations on the pi and qi . We will give a geometric interpretation
of these relations.
Using the map of Lemma 3.2, each summand in this relation (4) r epresents a
choice ℓ(xi; pi, qi) of combinatorial ﬂattening for one of the ﬁve ideal simplic es.
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class 423
For each 1–simplex E connecting two of the points zi we get a corresponding
linear combination
4∑
i=0
(−1)ilE(∆ i, ℓ(xi; pi, qi)) (5)
of log-parameters (Deﬁnition 3.1), where we put lE(∆ i, ℓ(xi; pi, qi)) = 0 if the
line E is not an edge of ∆ i . This linear combination has just three non-zero
terms corresponding to the three simplices that meet at the e dge E . One easily
checks that the real part is zero and the imaginary part can be interpreted
(with care about orientations) as the sum of the “adjusted an gles” of the three
ﬂattened simplices meeting at E .
Deﬁnition 3.3 We say that the ( xi; pi, qi) satisfy the ﬂattening condition if
each of the above linear combinations (5) of log-parameters is equal to zero.
That is, the adjusted angle sum of the three simplices meetin g at each edge is
zero.
Lemma 3.4 Relation (4) is an instance of the lifted ﬁve term relation (2 ) if
and only if the (xi; pi, qi) satisfy the ﬂattening condition.
Proof We ﬁrst consider the case that ( x0, . . . , x4) ∈ FT+ . Recall this means
that each xi is in H. Geometrically, this implies that each of the above ﬁve
tetrahedra is positively oriented by the ordering of its ver tices. This implies
the conﬁguration of Figure 2 with z1 and z3 on opposite sides of the plane
of the triangle z0z2z4 and the line from z1 to z3 passing through the interior
PSfrag replacements
z0
z1
z2
z3
z4
Figure 2
Geometry & Topology, Volume 8 (2004)
424 Walter D Neumann
of this triangle. Denote the combinatorial ﬂattening of the ith simplex by
ℓ(xi; pi, qi). If we consider the log-parameters at the edge z3z4 for example,
they are log x + p0πi , log y + p1πi , and log( y/x) + p2πi and the condition
is that (log x + p0πi) − (log y + p1πi) + (log( y/x) + p2πi) = 0. This implies
p2 = p1 − p0 . Similarly the other edges lead to other relations among the pi
and qi , namely:
z0z1: p2 − p3 + p4 = 0 z0z2: −p1 + p3 + q3 − p4 − q4 = 0
z1z2: p0 − q3 + q4 = 0 z1z3: −p0 − q0 + q2 − p4 − q4 = 0
z2z3: q0 − q1 + p4 = 0 z2z4: −p0 − q0 + p1 + q1 − p3 = 0
z3z4: p0 − p1 + p2 = 0 z3z0: p1 + q1 − p2 − q2 + q4 = 0
z4z0: −q1 + q2 − q3 = 0 z4z1: q0 − p2 − q2 + p3 + q3 = 0.
Elementary linear algebra veriﬁes that these relations are equivalent to the
equations p2 = p1 − p0 , p3 = p1 − p0 + q1 − q0 , q3 = q2 − q1 , p4 = q1 − q0 , and
q4 = q2 − q1 − p0 , as in the lifted ﬁve term relation (2). The lemma thus follow s
for ( x0, . . . , x4) ∈ FT+ . It is then true in general by analytic continuation.
We mention here a lemma that will be useful later.
Lemma 3.5 If the ﬂattenings (xi, pi, qi) are speciﬁed for a subset of the above
ﬁve ideal simplices and the sum of adjusted angles is zero aro und each edge E
that lies on three simplices of this subset, then one can spec ify ﬂattenings on
the remaining simplices so that the ﬂattening condition hol ds (sum of adjusted
angles is zero for all edges E ). Moreover, once the ﬂattenings are speciﬁed on
three of the simplices, the ﬂattenings on the ﬁnal two are uni quely determined.
Proof The lemma does not depend on the ordering of z0, . . . , z4 since the
ﬂattening condition at an edge is purely geometric. We assum e therefore that
the speciﬁed ﬂattenings are ( xi; pi, qi) for i = 0 , . . . , k with 0 ≤ k < 4. The
above proof shows that if k = 0 or 1 there is no restriction on the ﬂattenings,
while if k = 2 the the condition at the edge z3z4 implies p2 = p1 − p0 if
(x0, . . . , x4) ∈ FT+ , or the appropriate analytic continuation of this in genera l.
In each of these cases the previous lemma says how the ﬂatteni ngs on the
remaining simplices may be chosen, and moreover, that this c hoice is unique if
k = 2. If k = 3 then the conditions from the edges z0z4 and z2z4 determine
p3 = p1 − p0 + q1 − q0 and q3 = q2 − q1 if ( x0, . . . , x4) ∈ FT+ , or the approriate
analytic continuation in general, and the previous lemma th en determines the
ﬂattening ( x4; p4, q4).
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class 425
4 Deﬁnition of λ
Let G = PSL(2 , C) (with the discrete topology). In this section we describe
the map λ : H3(G; Z) → ˆP(C).
We ﬁrst describe the combinatorial representation of eleme nts of H3(G; Z) that
we will use. As we will describe, a special case is to give a clo sed oriented
triangulated 3–manifold with a ﬂat G–bundle on it. Any element of H3(G; Z)
can be represented this way, but we do not want to restrict to t his type of
representation.
We need to clarify our terminology for simplicial complexes .
Deﬁnition 4.1 We use the usual concept of simplicial complex K except that
we do not require that distinct simplices have diﬀerent verte x sets (but we do
require that closed simplices embed in |K|, ie, vertices of a simplex are distinct
in K ). The (open) star of a 0–simplex v of K is the union of τ − ∂τ over
simplices that have v as a vertex. It is an open neighborhood of v and is
the open cone on a simplicial complex Lv called the link of v . Note that Lv
immerses, but does not necessarily embed in K as the boundary of the star
of v .
We really only need quasi-simplicial complexes — cell compl exes whose cells
are simplices with simplicial attaching maps, but no requir ement that closed
simplices embed. We discuss this later; our more restrictiv e hypothesis is ﬁrst
needed near the end of section 10, but is eliminated again by P roposition 11.2.
4.1 Representing elements of Hn(G; Z)
Deﬁnition 4.2 An ordered n–cycle will be a compact n–dimensional simpli-
cial complex K such that the complement |K| − |K (n−3)| of its ( n − 3)–skeleton
is an oriented n–manifold, together with an ordering of the vertices of each n–
simplex of K so that these orderings agree on common faces. The ordering
orients each n–simplex ∆ i of K , and this orientation may or may not agree
with the orientation of |K| − |K (n−3)|. Let ǫi = +1 or −1 accordingly. Then
the n–cycle ∑
i ǫi∆ i represents a homology class [ K] ∈ Hn(|K|; Z) called the
fundamental class .
We will also require that the link Lv of each 0–simplex is connected. This can
always be achieved by duplicating 0–simplices if necessary .
Geometry & Topology, Volume 8 (2004)
426 Walter D Neumann
One can represent any element of Hn(G; Z) by giving an ordered n–cycle K
and labeling the vertices of each simplex ∆ of K by elements of G so that:
• Two G–labelings ( g0, . . . , gk) and ( g′
0, . . . , g′
k) of an ordered k –simplex
are considered equivalent if there is a g ∈ G with ggi = g′
i for each i;
• The G–labeling of any face of any simplex ∆ is equivalent to the G–
labeling induced from ∆.
We will also require that the labels for the vertices of any n–simplex are distinct
(we can do this because G is inﬁnite).
We describe two ways of seeing how any element of Hn(G, Z) can be described
by such data. The ﬁrst is algebraic, and is taken from [17].
