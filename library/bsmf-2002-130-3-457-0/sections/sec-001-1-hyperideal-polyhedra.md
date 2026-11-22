---
doc_id: bsmf-2002-130-3-457-0
doc_title: "Hyperideal polyhedra in hyperbolic 3-space"
section_id: sec-001-1-hyperideal-polyhedra
section_title: "Hyperideal polyhedra"
section_number: 1
pages: 5-7
source_pdf: BSMF_2002__130_3_457_0.pdf
source_sha256: 63f79235d0c13ba8
toc_source: inferred
doc_brief: "Hyperideal polyhedra in hyperbolic 3-space — — A hyperideal polyhedron is a non-compact polyhedron in the hyperbolic 3-space 3 which, in the projective model for 3 ⊂ 3, is just the intersection of 3"
---
461
In this regard, the local characterization of hyperideal polyhedra by their di-
hedral angles provided by our Theorem 11, which is already the key technical
step in this paper, may be its most useful result for applications.
The paper [10] provides a diﬀerent approach to a local control of ideal polyhe-
dra through their combinatorics and dihedral angles. The reader is also referred
to [13], [14] for the consideration of other rigidity properties of polyhedra in
hyperbolic 3-space.
It may also be of interest that Theorems 1 and 2 can be translated into
purely euclidean (or at least projective) statements. Indeed, they provide a
classiﬁcation of hyperideal projective polyhedra P Proj modulo the action of
the group PO(3, 1) consisting of those projective transformations of RP3 that
respect the unit sphere S2 ⊂R3 ⊂RP3. This is particularly remarkable when
one notices that, for an edge e of P = H3 ∩P Proj, the hyperbolic dihedral
angle θe of P is equal to the euclidean angle between the two circles Π ∩S2
and Π′ ∩S2 at their intersection points, where Π and Π′ are the two euclidean
planes respectively containing the two faces of P that meet along e. By duality,
Theorems 1 and 2 also classify convex projective polyhedra whose faces all meet
the unit sphere S2 ⊂R3 ⊂RP3 but whose edges are all disjoint from the closed
ball H3 ∪S2, modulo the action of PO(3, 1).
Theorems 1 and 2 for the somewhat simpler case of strictly ideal polyhedra,
where all vertices of P Proj are outside of the closure of H3, appeared in [4].
The ﬁnal draft of this paper was essentially completed while the second author
was visiting the Institut des Hautes ´Etudes Scientiﬁques, which he would like
to thank for its productive hospitality. The authors are also grateful to the
referee for several suggestions of improvement of the exposition, including a
simpliﬁcation of the proof of Proposition 6.
1. Hyperideal polyhedra
We ﬁrst recall a few basic facts about the projective model for H3 (see for
instance [16]).
Consider the symmetric bilinear form
B
"
(X0, X1, X2, X3), (Y0, Y1, Y2, Y3)
#
= −X0Y0 + X1Y1 + X2Y2 + X3Y3
on R4. In the projective space RP3, we consider the image H3 of the set of
those X ∈R4 with B(X, X) < 0. For the standard embedding of R3 in RP3,
deﬁned by associating to (x1, x2, x3) ∈R3 the point of RP3 with homogeneous
coordinates (1, x1, x2, x3), the subset H3 just corresponds to the open unit ball
in R3.
The projection R4 →RP3 induces a diﬀeomorphism between H3 and the
set H of those X = (X0, X1, X2, X3) ∈R4 with B(X, X) = −1 and X0 > 0.
The tangent space TXH of H at X is equal to the B-orthogonal of X and,
BULLETIN DE LA SOCI´ET´E MATH´EMATIQUE DE FRANCE
462
BAO (X.) & BONAHON (F.)
since B(X, X) < 0 and B has signature (3, 1), the restriction of B to TXS is
therefore positive deﬁnite. The corresponding riemannian metric on H ∼= H3
is exactly the hyperbolic metric of the projective model for H3.
The group O(3, 1) of linear B-isometries of R4 induces an action of
PO(3, 1) = O(3, 1)/{±Id} on H3 which respects the metric of H3.
The
group PO(3, 1) is actually equal to the whole isometry group of H3.
Note
that PO(3, 1) is naturally isomorphic to the subgroup of O(3, 1) consisting of
those elements that respect H.
In this model, the geodesics of H3 are exactly the non-empty intersections of
H3 with projective lines of RP3 or, equivalently, with straight lines of R3 ⊂RP3.
Similarly, the (totally geodesic) hyperbolic planes in H3 correspond to the non-
empty intersections of H3 with projective planes of RP3 or, equivalently, with
aﬃne planes of R3.
We will occasionally use the property that, given two
projective planes Π and Π′ whose intersection meets H3, the hyperbolic dihedral
angle between the hyperbolic planes Π ∩H3 and Π′ ∩H3 along the geodesic
Π∩Π′∩H3 is exactly equal to the euclidean angle between the circles Π∩∂∞H3
and Π′ ∩∂∞H3 at their two intersection points in the sphere at inﬁnity ∂∞H3
bounding H3 in R3.
One of the most valuable features of the projective model for H3 is its du-
ality properties.
Given a k-dimensional projective subspace ℓ⊂RP3, with
0 ≤k ≤2, the B-orthogonal L⊥of the (k + 1)-dimensional linear subspace L
of R4 corresponding to ℓis a (3 −k)-dimensional linear subspace of R4, and
therefore deﬁnes a (2 −k)-dimensional projective space ℓ⊥of RP3.
In particular, if x is a point which is not in the closure of H3 in RP3, x⊥is
a plane which must intersect H3, since otherwise B would be positive deﬁnite
or degenerate. By elementary linear algebra, if y ∈x⊥∩H3 and if l denotes
the projective line passing through x and y, the geodesic l ∩H3 is orthogonal
to the hyperbolic plane x⊥∩H3 for the metric of H3. Similarly, if z belongs to
the intersection of x⊥with the sphere ∂∞H3 bounding H3, then the projective
line joining x to z cannot meet H3, and is therefore tangent to ∂∞H3. This last
point gives us a very geometric way to construct x⊥: Draw all the projective
lines passing through x and tangent to ∂∞H3; then x⊥is the projective plane
which intersects ∂∞H3 along the circle formed by all the points of tangency.
When x is a point of the sphere ∂∞H3, the dual plane x⊥is just the plane
tangent to ∂∞H3 at x. This can, for instance, be seen by continuity from the
previous case.
Conversely, if Π is a hyperbolic plane in H3, the point x such that Π =
x⊥∩H3 is necessarily outside of the closure of H3 in RP3, for signature reasons.
In particular, the line L in R4 corresponding to x ∈RP3 contains exactly two
vectors X ∈R4 with B(X, X) = +1.
If, in addition, Π is endowed with
a transverse orientation, this deﬁnes a transverse orientation for the linear
subspace L⊥⊂R4. By deﬁnition, the unit normal vector of the transversely
tome 130 – 2002 – no 3
HYPERIDEAL POLYHEDRA IN HYPERBOLIC 3-SPACE
463
oriented hyperbolic plane Π is the vector X ∈L with B(X, X) = +1 and which
crosses L⊥in the direction of this transverse orientation.
Now, consider a hyperideal polyhedron P in H3, as deﬁned in the introduc-
tion. Recall that this means that P = P Proj ∩H3, where P Proj is a convex
projective polyhedron in RP3 whose vertices are all outside of H3 and whose
edges all meet H3 ∪∂∞H3. A vertex of P Proj which is on the sphere at inﬁnity
∂∞H3 is said to be ideal; otherwise, it is strictly hyperideal.
At this point, it may be useful to remind the reader that a convex projective
polyhedron in RP3 is the closure of a component of the complement of ﬁnitely
many projective planes in RP3. To avoid degenerate cases, we require in addi-
tion that a convex projective polyhedron does not contain any projective line
or, equivalently, that it is disjoint from at least one projective plane in RP3,
so that is is homeomorphic to a closed 3-ball.
Since every edge of P Proj meets H3, so does every face and it follows that
the projective polyhedron P Proj is completely determined by P = P Proj ∩H3.
For future reference, we note the following easy property.
Lemma 3. — For any two distinct vertices v and v′ of the projective polyhedron
