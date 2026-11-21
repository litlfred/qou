---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-052-a-taxonomy-of-multiple-points
section_title: "A taxonomy of multiple points"
section_number: null
pages: 311-317
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
293
no critical values at inﬁnity) we can write
ar =
X
w∈critical( ˆr)
κw
(2πi)d
Z
Cw
F(z)z−r−1dz
(10.1)
where critical( ˆr) is the set of critical points of the generating function F in
the direction ˆr, each κw is an integer, and each Cw is a chain of integration
deﬁned by tangential and normal Morse data at critical points of F. Roughly
speaking, the normal Morse data describes an integral that can be simpliﬁed
using residues, while the tangential data results in a saddle point integral that
can be asymptotically approximated.
Throughout this chapter we make various assumptions that simplify both
the determination of contributing critical points and the computation of in-
tegrals over tangential and normal Morse data. This was not necessary for
smooth points because all smooth points look the same topologically, but mul-
tiple points can vary substantially in their local topology and geometry. We
thus begin in Section 10.1 by introducing the types of multiple points we con-
sider, before Section 10.2 derives asymptotics for the integrals that arise and
Section 10.3 gives our main results on coeﬃcient asymptotics. Section 10.4
discusses the algebraic techniques used to identify multiple points in more de-
tail, and we conclude in Section 10.5 by examining asymptotics in non-generic
directions and the diﬃcult issue of tangential intersections.
10.1 A taxonomy of multiple points
Figure 10.2 displays the taxonomy we describe in this section. Eﬀective clas-
siﬁcation within this taxonomy is discussed in Section 10.4.
The simplest multiple point case occurs when V is a hyperplane arrange-
ment, meaning a ﬁnite union of hyperplanes (a simple example is shown in
Figure 10.3). If V is the union of transversely intersecting hyperplanes then
the normal data of a critical point on a stratum of codimension k is a k-torus,
both the normal and tangential Morse data can be described explicitly, and the
critical points describing asymptotics can be determined algorithmically (see
Theorem 10.23 below).
Example 10.3. Figure 10.4 shows the pole set of the generating function
F(x, y, z) =
16
(4 −2x −y −z)(4 −x −2y −z),
whose divisors are two planes meeting at the complex line S = {(1, 1, 1) +
λ(−1, −1, 3): λ ∈C}.
294
Multiple point asymptotics
Figure 10.2 A taxonomy of multiple points.
(1,1)
L
L2
1
Figure 10.3 A transverse multiple point on a hyperplane arrangement, shown in
two depictions.
For each direction ˆr in the positive orthant, there are critical points z1( ˆr)
and z2( ˆr) on the respective planes, and a critical point p( ˆr) on the line S . The
normal data at p is a 2-torus and the asymptotic behavior of the Cauchy integral
10.1 A taxonomy of multiple points
295
Figure 10.4 A singular variety deﬁned by two hyperplanes in three dimensions.
in (10.1) with domain Cp is determined by analyzing a one-dimensional saddle
point integral over a curve maximized at p, while the normal data at z1 (or z2)
is a 1-torus and the asymptotic behavior of the Cauchy integral with domain
Cz1 (respectively Cz2) is a two-dimensional saddle point integral over an open
disk maximized at z1 (respectively z2).
◁
As we will see below, partial fraction decomposition can always be used to
reduce analysis of an arbitrary set of linear divisors to an analysis of trans-
versely intersecting linear divisors. Figure 10.5 illustrates an example of three
linear divisors in two dimensions that are pairwise transverse but not jointly
transverse, resulting in a stratum of codimension k = 2.
Figure 10.5 Three linear divisors intersecting in two dimensions.
Moving on from linear divisors, if V consists of transverse multiple points
296
Multiple point asymptotics
then it is locally diﬀeomorphic to the transverse linear case, and once again the
topological normal data at a critical point is a k-torus.
Example 10.4 (lemniscate). Let F = 1/Q(x, y), where Q(x, y) = 19 −20x −
20y+5x2+14xy+5y2−2x2y−2xy2+x2y2 is the polynomial whose real zeros are
shown in Figure 10.6. The curve V intersects itself at the point (x, y) = (1, 1),
near which it is a union of two distinct segments of smooth curves intersecting
only at (1, 1).
◁
Figure 10.6 A local self-intersection.
Exercise 10.3. Make the change of coordinates Q(x, y) = Q(1 + u, 1 + v)
in Example 10.4 and write formulae v = f(u) for the two curves of V that
intersect at the origin in uv-coordinates.
Remark 10.5. If the transverse multiple point p lies in a complete intersec-
tion then there is no tangential integral and, provided F(z) = P(z)/Q(z) with
P(p) , 0, we will be able to compute the integral over the normal data explic-
itly as a polynomial times an exponential term (see Theorem 10.12 below).
Moving beyond transverse multiple points with non-linear divisors, the most
general class of multiple points for which we have a general method of deter-
mining asymptotics is that of arrangement points, where the lattice of intersec-
tions of the divisors deﬁning a stratum is the same as the lattice of intersections
of the tangent planes to the divisors (this being a hyperplane arrangement). A
central hyperplane arrangement is a hyperplane arrangement in which each
hyperplane passes through the origin. Each central hyperplane arrangement
A = W1 ∪· · · ∪Wn possesses a natural structure as a matroid M(A), an
10.1 A taxonomy of multiple points
297
axiomatic system discussed further below, whose elements index sets of hy-
perplanes Wk1, . . . , Wks with linearly independent normal vectors. The set of
all intersections LT = T
j∈T Wj for T ⊂[n] is called the lattice of ﬂats of A
as it possesses a natural lattice structure [OT92, Lemma 2.3], and we let
T = {j ∈[n] : LT ⊂Wj}
(10.2)
encode the maximal set of hyperplanes having intersection LT. If T = T when-
ever LT is nonempty then we call the arrangement transverse.
Deﬁnition 10.6 (arrangement points). The point p ∈V is an arrangement
point of order n if there exist complex manifolds V1, . . . , Vn such that
U ∩V = (U ∩V1) ∪· · · ∪(U ∩Vn)
and the intersection lattice of the surfaces {Vj} within U coincides with the
intersection lattice of their tangent planes, for every suﬃciently small neigh-
borhood U of p in Cd.
Example 10.7. If Q is a product of linear factors then every point p ∈V is
an arrangement point because the collection of surfaces {Vj} is a translation of
the collection of tangent planes.
◁
Example 10.8. Let F(x, y) = 1/(1−x)(1−y)(1−xy) be the generating function
with coeﬃcients ars = 1+min{r, s}. The three divisors are pairwise transverse,
intersecting at the single point p = (1, 1) which is not transverse (as we are in
two dimensions). The point p is an arrangement point because the intersection
lattice (each pair of divisors intersects at p, hence all three do) is the same as
one would get by replacing the curve V(1−xy) by its tangent line V(2−x−y)
at p. This is illustrated in Figure 10.7.
◁
Figure 10.7 An arrangement point in dimension two where three curves intersect.
298
Multiple point asymptotics
Example 10.9. The zero set of Q(x, y, z) = (1−z)(1−z+(1−y)2−(1+x)3) is the
union of the plane V1 deﬁned by 1 −z and a smooth surface V2 deﬁned by the
vanishing of the other factor p(x, y, z). These two surfaces intersect in the curve
S deﬁned by translating the cusp of V(z, x3−y2) to the point (−1, 1, 1). Because
the expansion of p at (−1, 1, 1) begins p(x, y, z) = 1−z+(y−1)2+· · · the tangent
planes of V1 and V2 coincide at (−1, 1, 1), which is not an arrangement point.
Note that the intersection S is not smooth, so the sets V1 \ V2, V2 \ V1, and
S do not form a Whitney stratiﬁcation. To reﬁne these sets into a Whitney
stratiﬁcation requires decomposing S further into the singleton {(−1, 1, 1)} and
the remainder S \ {(−1, 1, 1)}.
◁
Every transverse multiple point is an arrangement point. Although there are
arrangement points that are not transverse points, arrangement points have a
transversality in successive intersections.
Proposition 10.10. Suppose p is an arrangement point of order n, with divi-
sors V1, . . . , Vn as above, and let i < T ⊂[n]. Then either VT ⊂Vi in a
neighborhood of p or VT intersects Vi transversely at p. Consequently, if Pi
denotes the tangent space of Vi at p then any intersection VT is a manifold in
a neighborhood of p with tangent space LT = ∩j∈TP j at p.
Proof
We induct on the codimension of VT. If VT has codimension 1 then
VT = Vi for all i ∈T, with tangent space LT at p. If i < T then Pi is distinct
from the tangent plane to VT at p, hence the intersection of Vi and VT is
transverse.
Now suppose VT has codimension k ≥1 and i < T. By induction, VT is
smooth with tangent space LT at p. If i ∈T then there is nothing to prove, so
assume i < T and let T ′ = T ∪{i}. The normal vector to Vi at p is not in (LT)⊥,
and hence the surface Vi intersects VT transversely. The transverse intersec-
tion of smooth varieties is smooth with tangent space given by the intersection
of the tangent spaces, hence VT ′ is smooth with tangent space LT ′, completing
the induction.
□
We end this section with an example illustrating the most complicated be-
havior that can occur for multiple points: tangential intersections.
Example 10.11 (two curves intersecting tangentially). Consider the generat-
ing function
F(x, y) =
1
(2 −x −y)(1 −xy) =
X
i, j≥0
ai jxiy j,
with the divisors V(2 −x −y) and V(1 −xy) intersecting tangentially at the
point p = (1, 1) as shown in Figure 10.8.
