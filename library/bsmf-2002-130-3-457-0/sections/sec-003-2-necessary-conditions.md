---
doc_id: bsmf-2002-130-3-457-0
doc_title: "Hyperideal polyhedra in hyperbolic 3-space"
section_id: sec-003-2-necessary-conditions
section_title: "Necessary conditions"
section_number: 2
pages: 8-10
source_pdf: BSMF_2002__130_3_457_0.pdf
source_sha256: 63f79235d0c13ba8
toc_source: inferred
doc_brief: "Hyperideal polyhedra in hyperbolic 3-space — — A hyperideal polyhedron is a non-compact polyhedron in the hyperbolic 3-space 3 which, in the projective model for 3 ⊂ 3, is just the intersection of 3"
---
Proposition 5. — Let Γ be the dual graph of a hyperideal polyhedron P in H3
and, for every edge e of Γ, let θe ∈]0, π[ be the external dihedral angle of P
at the edge corresponding to e. For every closed curve γ embedded in Γ and
passing through the edges e1, e2, . . . , en of Γ, then !n
i=1 θei ≥2π with equality
if only if γ is the boundary of a component of S2 −Γ corresponding to an ideal
vertex of P Proj.
Proof. — Counting indices modulo n, let vi be the vertex of Γ that is between
ei−1 and ei in γ, and let fi be the face of P corresponding to vi. Let Πi ⊂H3 be
the hyperbolic plane containing fi, and let Hi ⊂H3 be the half-space delimited
by Πi and containing P. Let P ′ be the intersection of the Hi. The boundary
∂P ′ is an annulus, and is decomposed as a union of inﬁnite strips Πi∩P ′, in such
a way that Πi ∩P ′ and Πi+1 ∩P ′ meet along the geodesic of H3 containing the
edge of P corresponding to ei.
The closure of P ′ in H3 ∪∂∞H3 meets ∂∞H3 along two topological disks
D1 and D2, one of which will be reduced to a single point if (and only if) γ is
the boundary of a component of S2 −Γ which corresponds to an ideal vertex
tome 130 – 2002 – no 3
HYPERIDEAL POLYHEDRA IN HYPERBOLIC 3-SPACE
465
of P. The disk Dj is the union of circle arcs kj
1, kj
2, . . . , kj
n, where each kj
i is
contained in the circle Ci ⊂∂∞H3 bounding the hyperbolic plane Hi. Note
that, at the point where kj
i meets kj
i+1, the euclidean external angle between
these two arcs is equal to the angle between the circles Ci and Ci+1, namely to
the hyperbolic external dihedral angle θei of P along the edge ei. This holds
even when kj
i or kj
i+1 is reduced to a point, provided we use the convention
that the tangent line at a point of kj
i is equal to the tangent line of Ci at the
same point.
First consider the case where neither one of the two disks D1 and D2 is
reduced to a point. Let ϕ : ∂∞H3 →R2 be deﬁned by stereographic projection
from a point in the interior of D2. Because the stereographic projection sends
circle to circle and because this stereographic projection was performed from
a point in the interior of D2, the arcs ϕ(k1
i ) forming the boundary of ϕ(D1)
are circle arcs whose curvature vectors point away from ϕ(D1). In particular,
outside of the corners of ∂ϕ(D1), the geodesic curvature κ of ∂ϕ(D1) is negative.
Also, because the stereographic projection preserves angles, the angle between
ϕ(k1
i ) and ϕ(k1
i+1) is equal to the angle between k1
i and k1
i+1, namely to θei.
If we apply to ϕ(D1) the Gauss-Bonnet formula (also known in this case as
the Theorem of the Turning Tangents), 2π =
$
∂ϕ(D1) κ + !n
i=1 θei < !n
i=1 θei
where the inequality is strict because of our assumption that D1 is not reduced
to a single point. This proves the expected result in this case.
If one of D1 and D2, say D2, is reduced to a point, consider again the
stereographic projection ϕ : ∂∞H3 →R2 from this point of D2. The sides ϕ(k1
i )
of the polygon ϕ(D1) are now straight arcs, and the Gauss Bonnet formula gives
2π = !n
i=1 θei in this case.
Proposition 6. — Let Γ be the dual graph of a hyperideal polyhedron P in H3
and, for every edge e of Γ, let θe ∈]0, π[ be the dihedral angle of P at the edge
corresponding to e. For every arc γ embedded in Γ, passing through the edges
e1, e2, . . . , en of Γ, and joining two distinct vertices v1 and vn+1 which are in
the closure of the same component A of S2 −Γ but such that γ is not contained
in the boundary of A, then !n
i=1 θei > π.
Proof. — It clearly suﬃces to restrict attention to those γ which meet the
closure of A only at their two end points. Let v be the vertex of P Proj corre-
sponding to A.
If the vertex v is on the sphere at inﬁnity ∂∞H3 then, by Proposition 5,
we can join the two end points of γ by an arc γ′ in ∂A crossing edges en+1,
. . . , en+p such that !n+p
i=n+1 θei ≤π. Applying Proposition 5 to the simple
closed curve γ ∪γ′, we obtain that !n
i=1 θei ≥!n+p
i=1 θei −π ≥2π −π = π.
In addition, equality can occur only when γ∪γ′ is the boundary of a component
A′ of S2 −Γ, which is diﬀerent from A since γ is not contained in the boundary
of A. In this case, γ′ is contained in ∂A ∩∂A′ and therefore consists of a single
BULLETIN DE LA SOCI´ET´E MATH´EMATIQUE DE FRANCE
466
BAO (X.) & BONAHON (F.)
edge en+1, so that !n+p
i=n+1 θei = θen+1 < π. As a consequence, the inequality
is always strict.
Now consider the other case, where the vertex v is strictly hyperideal. Let
ρ be the hyperbolic reﬂection across the plane v⊥, and let P ′ be the union
P ∪ρ(P).
Because v⊥separates v from the other vertices of P Proj and is
orthogonal to the edges and faces of P that it meets, P ′ is a hyperideal poly-
hedron. Each edge of P ′ is, either an edge of P that does not meet v⊥, or the
image under ρ of an edge of P that does not meet v⊥, or an edge of P that
meets v⊥. Similarly, a face of P ′ is, either a face of P that does not meet v⊥,
or the image under ρ of a face of P that does not meet v⊥, or the intersection
of a face of P that meets v⊥with its image under ρ. As a consequence, the
dual graph Γ′ of P ′ is obtained by gluing together two copies of Γ along the
two images of ∂A.
Because of our assumption that γ meets ∂A only at its end points, the
images of γ in each of the two copies of Γ form a closed curve γ′ embedded
in Γ′. Applying Proposition 5 to the closed curve γ′ in the graph Γ′ dual to P ′,
we conclude that 2 !n
i=1 θei > 2π, which concludes the proof.
Lemma 7. — Let P be a convex cone with non-empty interior in H3, inter-
section of ﬁnitely many half-spaces each containing the point x ∈H3 in its
boundary.
If e1, . . . , en are the edges of P and if θe ∈]0, π[ denotes the
external dihedral angle of P along the edge e, then !n
i=1 θei < 2π.
Proof. — In the unit tangent sphere T 1
xH3 of H3 at x, consider the set Q of
those vectors which point towards P. Then Q is a convex polygon with geodesic
sides in the sphere T 1
xH3. In addition, the external angle of Q at each of its
corners is equal to the external dihedral angle of P at the corresponding edge.
The inequality then follows by application of the Gauss-Bonnet formula to
