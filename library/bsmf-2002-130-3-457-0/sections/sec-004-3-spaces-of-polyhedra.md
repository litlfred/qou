---
doc_id: bsmf-2002-130-3-457-0
doc_title: "Hyperideal polyhedra in hyperbolic 3-space"
section_id: sec-004-3-spaces-of-polyhedra
section_title: "Spaces of polyhedra"
section_number: 3
pages: 10-15
source_pdf: BSMF_2002__130_3_457_0.pdf
source_sha256: 63f79235d0c13ba8
toc_source: inferred
doc_brief: "Hyperideal polyhedra in hyperbolic 3-space — — A hyperideal polyhedron is a non-compact polyhedron in the hyperbolic 3-space 3 which, in the projective model for 3 ⊂ 3, is just the intersection of 3"
---
3. Spaces of polyhedra
If Γ is a planar 3-connected graph, let %PΓ denote the space of hyperideal
polyhedra P whose dual graph ΓP is identiﬁed to Γ. More precisely, an element
of %PΓ is a pair consisting of a hyperideal polyhedron P and of an isomorphism
Γ →ΓP between Γ and the dual graph ΓP of P.
Because working with Γ often leads to confusing terminology (vertices of Γ
correspond to faces of the corresponding polyhedra, while vertices of the projec-
tive polyhedra correspond to components of S2−Γ, etc. . . ), it is convenient to ﬁx
a hyperideal polyhedron P0 ∈%PΓ, with associated projective polyhedron P Proj
0
.
We will see in §6 that %PΓ is always non-empty, but what is important here is
that the combinatorics of P0 can be abstractly described in terms of Γ. In
particular, the set F of faces of P0 and P Proj
0
is naturally identiﬁed to the set of
tome 130 – 2002 – no 3
HYPERIDEAL POLYHEDRA IN HYPERBOLIC 3-SPACE
467
vertices of Γ, and the set V of vertices of P Proj
0
is naturally identiﬁed to the set
of components of S2 −Γ. Recall that, because Γ is 3-connected, its embedding
in S2 is unique up to homeomorphism of S2 (see for instance [9, §32]), so that
these two sets F and V only depend on Γ. For every P ∈%PΓ with associated
projective polyhedron P Proj, the sets of faces and vertices of P Proj are now
naturally identiﬁed to F and V .
We endow %PΓ with the topology induced by the embedding Φ : %PΓ →(RP3)V
that associates to P
∈
%PΓ the vertices of its associated projective poly-
hedron P Proj.
The group PO(3, 1) has a natural action on %PΓ. Consider the quotient space
PΓ = %PΓ/PO(3, 1).
Lemma 8. — The space PΓ is Hausdorﬀ.
Proof. — We need to show that, whenever two sequences Pn ∈%PΓ and gn ∈
PO(3, 1) are such that Pn converges to some P ∈%PΓ and gnPn converges to
some Q ∈%PΓ, there is a g ∈PO(3, 1) such that gP = Q.
Pick four distinct faces f0, f1, f2, f3 ∈F of P Proj
0
in such a way that f0 is
adjacent to the faces f1, f2 and f3. For each i, consider the hyperbolic plane
that contains the face of P corresponding to fi, transversely oriented with the
outward boundary orientation from P, and let Xi ∈R4 be its unit normal
vector, as deﬁned in §1. A consequence of the choice of the faces f0, f1, f2, f3
is that the intersection of the four projective planes X⊥
0 , X⊥
1 , X⊥
2 , X⊥
3 in RP3
is empty. It follows that the vectors X0, X1, X2, X3 are linearly independent,
and form a basis {X0, X1, X2, X3} for R4.
Similarly, the polyhedron Q ∈%PΓ provides a basis {Y0, Y1, Y2, Y3} for R4,
where Yi ∈R4 is the unit normal vector to the hyperbolic plane which con-
tains the face of Q corresponding to fi, transversely oriented with the outward
boundary orientation from Q, and the polyhedron Pn ∈%PΓ gives a similar
basis {Xn
0 , Xn
1 , Xn
2 , Xn
2 }.
Since Pn converges to P for the topology of %PΓ, each vertex of P Proj
n
converges to the corresponding vertex of P Proj, and each of its faces conse-
quently converges to the corresponding face of P Proj. In particular, each Xn
i
converges to Xi in R4. Similarly, since gnPn converges to Q in %PΓ, each gnXn
i
converges to Yi.
If An denotes the matrix of gn from R4 with the basis
{X0, X1, X2, X3} to R4 with the basis {Y0, Y1, Y2, Y3}, it follows that An
converges to the identity matrix. As a consequence, gn converges to a linear
isomorphism g of R4, which must be in O(3, 1) since this subgroup is closed
in the linear group.
Therefore, g induces an element of PO(3, 1) which,
by continuity, sends P to Q as required.
To analyze the local topology of %PΓ and PΓ, subdivide the faces of the
model projective polyhedron P Proj
0
into triangles by adding a few edges (and
BULLETIN DE LA SOCI´ET´E MATH´EMATIQUE DE FRANCE
468
BAO (X.) & BONAHON (F.)
no vertex). Let &P Proj
0
denote P Proj
0
with this new cell decomposition of its
boundary. The set V of vertices of &P Proj
0
is the same as that of P Proj
0
, however
the set of edges of &P Proj
0
is now E ∪E′, where E is the set of ‘old’ edges of P Proj
0
and E′ is the set of ‘new’ edges introduced to subdivide its faces into triangles.
Let x ∈(RP3)V be a point which is close to the vertex set Φ(P) ∈(RP3)V
of a polyhedron P ∈%PΓ. For a (triangle) face f of &P Proj
0
, with vertices v1, v2
and v3, the corresponding coordinates xv1, xv2, xv3 ∈RP3 of x are the vertices
of a triangle tf in RP3, uniquely determined if we require that tf is close to
the triangle bounded by the corresponding vertices in a face of P (beware that
three non-collinear points are the vertices of 4 distinct triangles in RP3). As f
ranges over all faces of &P Proj
0
, the union of the tf forms the boundary of a
polyhedron Px in RP3.
This polyhedron Px is a perturbation of P Proj.
In
contrast to P Proj, Px is not necessarily convex and some of its vertices may
be inside H3. However, for x suﬃciently close to Φ(P), the polyhedron Px is
embedded and each of its edges meets H3.
If e ∈E ∪E′ is an edge of &P Proj
0
, consider the corresponding edge of Px,
and let %Θe(x) ∈] −π, π[⊂R be the external dihedral angle of the hyperbolic
polyhedron Px ∩H3 along this edge. Considering all such edges e ∈E ∪E′,
this deﬁnes a map %Θ : U →RE∪E′ on a neighborhood U of Φ(P) in (RP3)V .
We now use %Θ to characterize the intersection of U with the image of the
embedding Φ : %PΓ →(RP3)V .
Lemma 9. — For every P ∈%PΓ, there is a neighborhood U of Φ(P) in (RP3)V
such that, for the function %Θ : U →RE∪E′ deﬁned above, U ∩Φ
" %PΓ
#
consists
of those x ∈U with the following properties:
(i) %Θe(x) = 0 for every ‘new’ edge e ∈E′;
(ii) for every vertex v ∈V , !n
i=1 %Θei(x) ≥2π where e1, . . . , en ∈E are the
edges of P Proj
0
that contain the vertex v.
Proof. — Choose U small enough that %Θe(x) > 0 for every ‘old’ edge e ∈E
and every x ∈U. If x ∈U satisﬁes Conditions (i) and (ii), this property of
old edges and Condition (i) guarantee that Px is convex and, if we erase those
edges where ∂Px is ﬂat, has the same combinatorics as P Proj
0
. By Lemma 7,
Condition (ii) implies that all the vertices of Px lie outside of H3. Since all the
edges of Px already meet H3, this shows that Px∩H3 is a hyperideal polyhedron,
whose image in (RP3)V is equal to x.
Conversely, Conditions (i) and (ii) are clearly necessary for x ∈U to be
in Φ
" %PΓ
#
, by deﬁnition of %Θ and by Proposition 5.
The key technical step in the proof of the Rigidity Theorem 2 is the following
inﬁnitesimal rigidity result, whose proof will occupy the next section.
tome 130 – 2002 – no 3
HYPERIDEAL POLYHEDRA IN HYPERBOLIC 3-SPACE
469
Proposition 10 (Inﬁnitesimal Rigidity Lemma). — For P
∈
%PΓ, let %Θ :
U →RE∪E′ be the map deﬁned as above on a neighborhood U of Φ(P)
in (RP3)V . Then, the kernel of the tangent map of %Θ at Φ(P) is equal to the
image of the tangent map at Id ∈PO(3, 1) of the map PO(3, 1) →(RP3)V de-
ﬁned by g ,→gΦ(P). In other words, any inﬁnitesimal deformation of Φ(P) in
(RP3)V which inﬁnitesimally respects the dihedral angles %Θe for all e ∈E ∪E′
must come from composition by an inﬁnitesimal element of PO(3, 1).
Assuming Proposition 10, we are now ready to determine the local type of
PΓ = %PΓ/PO(3, 1).
The map %Θ is deﬁned on a neighborhood of Φ( %PΓ), and we can consider
the composition %Θ ◦Φ : %PΓ →RE∪E′. Propositions 5, 6 and Lemma 9 impose
constraints on the image of %Θ ◦Φ. Namely, its image is contained in KΓ × 0 ⊂
RE × RE′ where the subset KΓ ⊂RE consists of those θ ∈RE which satisfy
the following conditions:
0) For every e ∈E, the coordinate θe of θ corresponding to e is in the
interval ]0, π[;
1) For every closed curve γ embedded in Γ and passing through the edges
e1, e2, . . . , en of Γ, !n
i=1 θei ≥2π with equality allowed only when γ is the
boundary of a face of S2 −Γ.
2) For every arc γ embedded in Γ, passing through the edges e1, e2, . . . ,
en of Γ, and joining two distinct vertices which are in the closure of the same
component of S2 −Γ but such that γ is not contained in the boundary of that
component, !n
i=1 θei > π.
The map %Θ ◦Φ : %PΓ →KΓ × 0 ⊂RE × RE′ is invariant under the action
of PO(3, 1) on %PΓ, and therefore induces a map Θ : PΓ →KΓ on PΓ =
%PΓ/PO(3, 1).
Theorem 11 (Local characterization of hyperideal polyhedra by their dihedral
angles)
The map Θ : PΓ →KΓ is a local homeomorphism.
Proof (assuming Proposition 10). — Consider a hyperideal polyhedron P ∈
%PΓ, and its class in PΓ which, to avoid cumbersome notation, we will denote by
the same letter P ∈PΓ. We want to show that Θ restricts to a homeomorphism
from a neighborhood of P in PΓ to a neighborhood of Θ(P) in KΓ.
Consider the restriction %Θ : U →RE∪E′ of %Θ to an open neighborhood U of
Φ(P) in (RP3)V . Because all the faces of the cell decomposition of &P Proj
0
are
triangles, a counting argument shows that #E + #E′ = 3#V + 6, where #X
denotes the cardinal of X. In particular, the diﬀerence between the dimensions
of the domain and of the range of %Θ : U →RE∪E′ is equal to 6.
BULLETIN DE LA SOCI´ET´E MATH´EMATIQUE DE FRANCE
470
BAO (X.) & BONAHON (F.)
The map PO(3, 1) →(RP3)V deﬁned by g ,→gΦ(P) has an injective tangent
map at Id. This can easily be seen by picking, as in the proof of Lemma 8,
four faces f0, f1, f2, f3 ∈F such that the unit normal vectors X0, X1, X2,
X2 ∈R4 of the planes containing the corresponding faces of P Proj are linearly
independent; an element of the kernel of the tangent map inﬁnitesimally ﬁxes
the vertices of P Proj, therefore inﬁnitesimally ﬁxes the Xi, and consequently
must be trivial. It follows that the image of the tangent map of PO(3, 1) →
(RP3)V at Id has dimension 6.
Combining this computation of dimensions with Proposition 10, we conclude
that the diﬀerential of %Θ : U →RE∪E′ at Φ(P) is surjective. In particular,
%Θ(U) is open in RE∪E′ if we choose U small enough.
The Submersion Theorem shows that we can choose the neighborhood U of
Φ(P) so that it decomposes as U ∼= U ′ × U ′′ in such a way that %Θ corresponds
to the composition of the projection U ′ × U ′′ →U ′ and of a diﬀeomorphism
U ′ →%Θ(U). Let (u′
0, u′′
0) ∈U ′×U ′′ correspond to Φ(P) ∈U. For every u′ ∈U ′,
the map g ,→g(u′, u′′
0) immerses a neighborhood Wu′ of Id in PO(3, 1) in the
slice {u′} × U ′′ ⊂U since %Θ ◦g = %Θ. By the above dimension computations,
PO(3, 1) and U ′′ both have dimension 6, and we conclude that we can choose the
neighborhood U and the identiﬁcation U ∼= U ′×U ′′ so that each slice {u′}×U ′′
is of the form W(u′, u′′
0), where W is a ﬁxed neighborhood of Id in PO(3, 1).
We claim that, if U and W are chosen small enough, two elements of U
will be in the same PO(3, 1)-orbit if and only if they belong to the same slice
{u′} ×U ′′ ⊂U. It clearly suﬃces to show that, if x ∈(RP3)V and g ∈PO(3, 1)
are such that x and gx are both close to Φ(P), then g must be close to Id
in PO(3, 1). For this, pick again four faces f0, f1, f2, f3 ∈F such that the unit
normal vectors X0, X1, X2, X2 ∈R4 of the planes containing the corresponding
faces of P Proj are linearly independent. Then, as in the proof of Lemma 8,
each gXi is close to Xi, and it follows that g is close to Id in PO(3, 1).
Therefore, if we choose U small enough, two points (u′, u′′), (v′, v′′) ∈U ′ ×
U ′′ ∼= U are in the same PO(3, 1)-orbit if and only if they are in the same
slice {u′} × U ′′, namely if and only if v′ = u′, namely if and only if they have
the same image under %Θ. In other words, the restriction of %Θ to U induces a
homeomorphism between U/PO(3, 1) and %Θ(U).
By Lemma 9, the image of U ∩Φ
" %PΓ
#
is equal to %Θ(U) ∩(KΓ × {0}). It
follows that %Θ induces a homeomorphism between U ∩Φ
" %PΓ
#
/PO(3, 1) and
%Θ(U)∩(KΓ ×{0}). Since Φ is a PO(3, 1)-equivariant homeomorphism between
%PΓ and Φ
" %PΓ
#
, we conclude that %Θ ◦Φ induces a homeomorphism between
Φ−1(U)/PO(3, 1) and %Θ(U)∩(KΓ×{0}). Note that Φ−1(U)/PO(3, 1) is an open
neighborhood of P in PΓ, and that %Θ(U)∩(KΓ ×{0}) is an open neighborhood
of %Θ ◦Φ(P) in KΓ × {0} since %Θ(U) is open in RE × RE′.
tome 130 – 2002 – no 3
HYPERIDEAL POLYHEDRA IN HYPERBOLIC 3-SPACE
471
This proves that the map Θ : PΓ →KΓ restricts to a homeomorphism from
a neighborhood of P in PΓ to a neighborhood of Θ(P) in KΓ.
