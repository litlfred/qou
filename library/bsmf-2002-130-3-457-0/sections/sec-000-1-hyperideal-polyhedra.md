---
doc_id: bsmf-2002-130-3-457-0
doc_title: "Hyperideal polyhedra in hyperbolic 3-space"
section_id: sec-000-1-hyperideal-polyhedra
section_title: "Hyperideal polyhedra"
section_number: 1
pages: 4-8
source_pdf: BSMF_2002__130_3_457_0.pdf
source_sha256: 63f79235d0c13ba8
doc_brief: "Hyperideal polyhedra in hyperbolic 3-space — —A h y p e r i d e a l p o l y h e d r o n i s a n o n - c o m p a c t p o l y h e d r o n i n t h e h y p e r b o l i c 3-space 3 which, in the"
---
inﬁnity. Even in these cases, one could argue that our proof is a little simpler, as
it is based on relatively simple inﬁnitesimal lemmas followed by covering space
argument, as opposed to the more delicate global argument of Lemma 4.11
of [12]. However, the main point of Theorem 2 is that it is a key ingredient
for the proof of Theorem 1, justifying once again the heuristic principle that
“uniqueness implies existence” . Theorem 2 is the reason why we introduced
Condition 2 in the deﬁnition of hyperideal polyhedra, as it fails for general
polyhedra without vertices in H3.
Our proof of Theorems 1 and 2 is based on the continuity method pioneered
by Aleksandrov [1] and further exploited in [2] and [12]. We ﬁrst use an implicit
function theorem, proved through a variation of Cauchy’s celebrated rigidity
theorem for euclidean polyhedra [5], to show that a hyperideal polyhedron is
locally determined by its combinatorial type and its dihedral angles. We then
go from local to global by a covering argument.
Although the generalization of the results of [11] from ideal polyhedra to
hyperideal polyhedra is of interest by itself, the real motivation for this work
was to provide a proof of the classiﬁcation of ideal polyhedra which locally
controls the combinatorics of the polyhedra involved. Ideal polyhedra play
an important role in 3-dimensional geometry, as they can be used as building
blocks to construct hyperbolic 3-manifolds through the use of ideal triangula-
tions, possibly not locally ﬁnite. To study deformations of a hyperbolic metric
on a 3-manifold, it is therefore useful to have a good classiﬁcation of the defor-
mations of ideal polyhedra within a given combinatorial type. Unfortunately,
Rivin’s argument in [11] is indirect. He ﬁrst uses the classiﬁcation of compact
hyperbolic polyhedra by their dual polyhedra [12], where one completely looses
control of the combinatorics, and he extends it to ideal polyhedra by passing to
the limit as the vertices go to inﬁnity; he then observes that for ideal polyhedra
the dual polyhedron does determine the combinatorics of the ideal polyhedron.
tome 130 – 2002 – n o 3
HYPERIDEAL POLYHEDRA IN HYPERBOLIC 3-SPACE 461
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
the group PO(3 , 1) consisting of those projective transformations of RP3 that
respect the unit sphere S2 ⊂ R3 ⊂ RP3.T h i s i s p a r t i c u l a r l y r e m a r k a b l e w h e n
one notices that, for an edge e of P = H3 ∩ P Proj ,t h eh y p e r b o l i cd i h e d r a l
angle θe of P is equal to the euclidean angle between the two circles Π ∩ S2
and Π ′∩ S2 at their intersection points, where Π and Π ′are the two euclidean
planes respectively containing the two faces of P that meet along e.B y d u a l i t y ,
Theorems 1 and 2 also classify convex projective polyhedra whose faces all meet
the unit sphere S2 ⊂ R3 ⊂ RP3 but whose edges are all disjoint from the closed
ball H3 ∪ S2,m o d u l ot h ea c t i o no fP O ( 3, 1).
Theorems 1 and 2 for the somewhat simpler case of strictly ideal polyhedra,
where all vertices of P Proj are outside of the closure of H3,a p p e a r e di n[ 4 ] .
The ﬁnal draft of this paper was essentially completed while the second author
was visiting the Institut des Hautes ´Etudes Scientiﬁques, which he would like
to thank for its productive hospitality. The authors are also grateful to the
referee for several suggestions of improvement of the exposition, including a
simpliﬁcation of the proof of Proposition 6.
1. Hyperideal polyhedra
We ﬁrst recall a few basic facts ab out the pro jective mo del for H3 (see for
instance [16]).
Consider the symmetric bilinear form
B
(
(X0,X 1,X 2,X 3), (Y0,Y 1,Y 2,Y 3)
)
= −X0Y0 + X1Y1 + X2Y2 + X3Y3
on R4.I n t h e p r o j e c t i v e s p a c eRP3,w ec o n s i d e rt h ei m a g eH3 of the set of
those X ∈ R4 with B(X, X) < 0. For the standard embedding of R3 in RP3,
deﬁned by associating to ( x1,x 2,x 3) ∈ R3 the point of RP3 with homogeneous
coordinates (1 ,x 1,x 2,x 3), the subset H3 just corresponds to the open unit ball
in R3.
The projection R4 → RP3 induces a diﬀeomorphism between H3 and the
set H of those X =( X0,X 1,X 2,X 3) ∈ R4 with B(X, X)= −1a n d X0 > 0.
The tangent space TX H of H at X is equal to the B-orthogonal of X and,
BULLETIN DE LA SOCI ´ET´EM A T H´EMATIQUE DE FRANCE
462 BAO (X.) & BONAHON (F.)
since B(X, X) < 0a n d B has signature (3 , 1), the restriction of B to TX S is
therefore positive deﬁnite. The corresponding riemannian metric on H ∼= H3
is exactly the hyperbolic metric of the projective model for H3.
The group O(3 , 1) of linear B-isometries of R4 induces an action of
PO(3, 1) = O(3 , 1)/{±Id} on H3 which respects the metric of H3.T h e
group PO(3 , 1) is actually equal to the whole isometry group of H3.N o t e
that PO(3 , 1) is naturally isomorphic to the subgroup of O(3 , 1) consisting of
those elements that respect H.
In this model, the geodesics of H3 are exactly the non-empty intersections of
H3 with projective lines of RP3 or, equivalently, with straight lines of R3 ⊂ RP3.
Similarly, the (totally geodesic) hyperbolic planes in H3 correspond to the non-
empty intersections of H3 with projective planes of RP3 or, equivalently, with
aﬃne planes of R3.W e w i l l o c c a s i o n a l l y u s e t h e p r o p e r t y t h a t , g i v e n t w o
projective planes Π and Π ′whose intersection meets H3,t h eh y p e r b o l i cd i h e d r a l
angle between the hyperbolic planes Π ∩ H3 and Π ′∩ H3 along the geodesic
Π ∩Π′∩H3 is exactly equal to the euclidean angle between the circles Π ∩∂∞ H3
and Π ′∩ ∂∞ H3 at their two intersection points in the sphere at inﬁnity ∂∞ H3
bounding H3 in R3.
One of the most valuable features of the projective model for H3 is its du-
ality properties. Given a k-dimensional projective subspace 𝓁 ⊂ RP3,w i t h
0 ≤ k ≤ 2, the B-orthogonal L⊥ of the ( k +1 ) - d i m e n s i o n a l l i n e a r s u b s p a c eL
of R4 corresponding to 𝓁 is a (3 − k)-dimensional linear subspace of R4,a n d
therefore deﬁnes a (2 − k)-dimensional projective space 𝓁⊥ of RP3.
In particular, if x is a point which is not in the closure of H3 in RP3, x⊥ is
ap l a n ew h i c hm u s ti n t e r s e c tH3,s i n c eo t h e r w i s eB would be positive deﬁnite
or degenerate. By elementary linear algebra, if y ∈ x⊥ ∩ H3 and if l denotes
the projective line passing through x and y,t h eg e o d e s i cl ∩ H3 is orthogonal
to the hyperbolic plane x⊥ ∩H3 for the metric of H3.S i m i l a r l y , i fz belongs to
the intersection of x⊥ with the sphere ∂∞ H3 bounding H3,t h e nt h ep r o j e c t i v e
line joining x to z cannot meet H3,a n di st h e r e f o r et a n g e n tt o∂∞ H3.T h i s l a s t
point gives us a very geometric way to construct x⊥ :D r a w a l l t h e p r o j e c t i v e
lines passing through x and tangent to ∂∞ H3;t h e nx⊥ is the projective plane
which intersects ∂∞ H3 along the circle formed by all the points of tangency.
When x is a point of the sphere ∂∞ H3,t h ed u a lp l a n ex⊥ is just the plane
tangent to ∂∞ H3 at x.T h i s c a n , f o r i n s t a n c e , b e s e e n b y c o n t i n u i t y f r o m t h e
previous case.
Conversely, if Π is a hyperbolic plane in H3,t h ep o i n t x such that Π =
x⊥ ∩H3 is necessarily outside of the closure of H3 in RP3,f o rs i g n a t u r er e a s o n s .
In particular, the line L in R4 corresponding to x ∈ RP3 contains exactly two
vectors X ∈ R4 with B(X, X)=+ 1 . I f ,i na d d i t i o n ,Πi se n d o w e dw i t h
at r a n s v e r s eo r i e n t a t i o n ,t h i sd e ﬁ n e sat r a n s v e r s eo r i e n t a t i o nf o rt h el i n e a r
subspace L⊥ ⊂ R4.B y d e ﬁ n i t i o n , t h eunit normal vector of the transversely
tome 130 – 2002 – n o 3
HYPERIDEAL POLYHEDRA IN HYPERBOLIC 3-SPACE 463
oriented hyperbolic plane Π is the vector X ∈ L with B(X, X)=+ 1a n dw h i c h
crosses L⊥ in the direction of this transverse orientation.
Now, consider a hyperideal polyhedron P in H3,a sd e ﬁ n e di nt h ei n t r o d u c -
tion. Recall that this means that P = P Proj ∩ H3,w h e r eP Proj is a convex
projective polyhedron in RP3 whose vertices are all outside of H3 and whose
edges all meet H3 ∪∂∞ H3.A v e r t e x o fP Proj which is on the sphere at inﬁnity
∂∞ H3 is said to be ideal;o t h e r w i s e ,i ti sstrictly hyperideal.
At this point, it may be useful to remind the reader that a convex projective
polyhedron in RP3 is the closure of a component of the complement of ﬁnitely
many projective planes in RP3. To avoid degenerate cases, we require in addi-
tion that a convex projective polyhedron does not contain any projective line
or, equivalently, that it is disjoint from at least one projective plane in RP3,
so that is is homeomorphic to a closed 3-ball.
Since every edge of P Proj meets H3,s od o e se v e r yf a c ea n di tf o l l o w st h a t
the projective polyhedron P Proj is completely determined by P = P Proj ∩ H3.
For future reference, we note the following easy prop erty.
Lemma 3 .— For any two distinct vertices v and v′of the projective polyhedron
P Proj associated to the hyperideal polyhedron P ,t h el i n es e g m e n tj o i n i n gv to v′
in P Proj meets H3.
Proof.—M o d i f y i n gP with an element of PO(3 , 1) if necessary, we can assume
that P Proj ⊂ R3 ⊂ RP3 without loss of generality. Then, consider the radial
projection R3 −{ v}→ S2 to the unit sphere centered at v.T h e i m a g eϕ (H3)
is a spherical open disk contained in a hemisphere of S2,a n d ϕ (P )i sac o n v e x
spherical polygon whose vertices are contained in ϕ (H3). It follows that ϕ (P )
is contained in ϕ (H3), by convexity. In particular, ϕ (v′)i si n ϕ (H3), and it
follows that the line segment vv′must meet H3.
Consider a strictly hyperideal vertex v of P Proj .A m o n g t h e t w o c l o s e d
hyperbolic half-spaces delimited by the hyperbolic plane v⊥ ∩H3 in H3,l e t Hv
be the one with the following property: F or every other vertex v′⁄= v of P Proj ,
the (unique) oriented line segment k of RP3 which goes from v to v′ in P Proj
exits Hv at its intersection point with v⊥ ∩ H3.( T o m a k e s u r e t h a t t h i s r e a l l y
makes sense, it may be useful to modify P Proj by an element of PO(3 , 1) so that
it is contained in R3 ⊂ RP3 and to use the geometric description of v⊥ ∩ H3
by lines passing through v and tangent to ∂∞ H3.) In other words, the half-
space Hv is on the same side of x⊥ ∩H3 as v with respect to the other vertices
of P Proj .
Lemma 4 .— For any two distinct hyperideal vertices v, v′of P Proj ,t h ea s s o -
ciated hyperbolic half-spaces Hv and Hv′ in H3 are disjoint.
Proof.—B y d e ﬁ n i t i o n o fHv and Hv′,i tc l e a r l ys u ﬃ c e st os h o wt h a tt h et w o
hyperbolic planes v⊥ ∩ H3 and v′⊥∩ H3 are disjoint. In RP3,t h ei n t e r s e c t i o n
BULLETIN DE LA SOCI ´ET´EM A T H´EMATIQUE DE FRANCE
464 BAO (X.) & BONAHON (F.)
of v⊥ and v′⊥ is the line ( vv′)⊥ dual to the line vv′passing through v and v′.
By Lemma 3, the line vv′ meets H3 and its dual line ( vv′)⊥ is consequently
disjoint from the closure of H3.I t f o l l o w s t h a t t h e t w o h y p e r b o l i c p l a n e sv⊥ ∩H3
and v′⊥∩ H3 are disjoint, and therefore that Hv and Hv′ are also disjoint.
If v is an ideal vertex of P Proj ,w ec h o o s eas m a l lh o r o b a l lHv centered at v.
In the projective model H3 ⊂ R3 ⊂ RP3, Hv is just the intersection with H3 of
a closed euclidean ball which is contained in H3 ∪ ∂∞ H3 and tangent to ∂∞ H3
at v.T h e r e a r e o f c o u r s e m a n y p o s s i b l e c h o i c e s f o r s u c h a h o r o b a l l , b u t w e
choose it so that all Hv thus associated to strictly hyperideal and ideal vertices
are pairwise disjoint.
By deﬁnition, the truncated polyhedron P Tru n associated to the hyperideal
polyhedron P is obtained by removing from P its intersection with the interior
of each such Hv .N o t e t h a tP Tru n is completely determined if all the vertices
of P Proj are strictly hyperideal, and deﬁned modulo choice of the horoballs Hv
associated to the ideal vertices in the general case.
This truncated polyhedron P Tru n will play an important rˆ ole in our argu-
ments. By construction, P Tru n is compact. Its faces are of two types. The ﬁrst
type of face is the intersection of a face of P with P Tru n.T h e s e c o n d t y p e o f
face is the intersection of P Tru n with one of the ∂Hv .T h i s s e c o n d t y p e c a n
itself be subdivided in two subtypes, according to whether ∂Hv is a horosphere,
when the vertex v is ideal, or a hyperbolic plane, when the vertex v is strictly
hyperideal.
