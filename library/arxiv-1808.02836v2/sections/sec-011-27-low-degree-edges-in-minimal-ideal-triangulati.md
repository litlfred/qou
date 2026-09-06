---
doc_id: arxiv-1808.02836v2
doc_title: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds"
section_id: sec-011-27-low-degree-edges-in-minimal-ideal-triangulati
section_title: "Low degree edges in minimal ideal triangulations"
section_number: 2.7
pages: 10-15
source_pdf: 1808.02836v2.pdf
source_sha256: 0224a296253122a2
doc_brief: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds — Previous work of the authors studies minimal triangulations of closed 3–manifolds using a characterisation of low degree edges"
---
We now show that there are no edges of degree one or two in a minimal triangulation of a cusped hyperbolic
3–manifold, and that edges of degree three must be contained in layered ∂ –punctured solid tori.
Lemma 8 If T is a minimal ideal triangulation of a cusped hyperbolic 3–manifold M, then T has no edge
of degree one.
Proof Suppose e1 is an edge of T of degree 1. Let ˜∆1 be the single tetrahedron containinge1. Then ˜∆1 = e1∗
e is the join of e1 and the edge e opposite e1. The edge e of T bounds a disc. This contradicts Corollary 5.
Lemma 9 If T is a minimal ideal triangulation of a cusped hyperbolic 3–manifold M, then T has no edge
of degree two.
Proof The ﬁgure-eight knot complement m0042 and its sister m003 are the only cusped hyperbolic 3–manifold
having an ideal triangulation with two ideal tetrahedra. Neither of these triangulations has an edge of degree
2We include the names of manifolds from the cusped hyperbolic manifold census of SnapPea.
10
Figure 6: Four embeddings of the intersection of the dunce hat t with torus boundary component T0. Top
left: two inessential loops, not nested. Bottom left: two inessential loops, nested. Top right: two parallel
essential loops. Bottom right: one essential loop and one inessential loop.
two. Hence, we may assume T has at least three tetrahedra and that the preimage of an edge e of degree two
consists of two edges e′ and e′′ in two distinct tetrahedra, ˜∆′ and ˜∆′′, respectively (note that an edge of degree
two cannot be contained in a single tetrahedron).
We ﬁx the following notation. The vertices of ˜∆′ are denoted by A′,B′,C′, and D′ with e′ = A′D′. The vertices
of ˜∆′′ are denoted by A′′,B′′,C′′, and D′′ with e′′ = A′′D′′. The face identiﬁcations are (A′B′D′)↔ (A′′B′′D′′)
and (A′C′D′)↔ (A′′C′′D′′), with (A′D′) = (A′′D′′) = e.
Figure 7: Edge of degree two.
Typically, in such a case of an edge of degree two, one can discard the two tetrahedra˜∆′ and ˜∆′′ and make new
identiﬁcations (A′B′C′)↔ (A′′B′′C′′) and (B′C′D′)↔ (B′′C′′D′′).
If this is possible, then there is a triangulation of M having fewer tetrahedra than T , contradicting that T is
minimal. It follows that under the assumption of T minimal and e an edge of degree two, there must be an
obstruction to such a re-identiﬁcation, that is, some of the faces to be identiﬁed must already be identical. This
can happen on the level of edges (Obstruction 1 below), or on the level of triangles (Obstruction 2 below). We
consider both obstructions and show that each leads to a contradiction, establishing that there are no edges of
degree two.
Obstruction 1. The edges B′C′ and B′′C′′ are identiﬁed, preventing the collapse, see Figure 8. In this situation
we have two subcases:
(1) Edges are identiﬁed with opposite orientation (i.e., B′C′ is identiﬁed with C′′B′′). If this is the case, then
in the truncated 3–manifold Mc of M with an open neighbourhood of the vertices removed, we have a
11
properly embedded M ¨obius band N ⊂ Mc. If ∂ N is an inessential curve on the vertex linking torus
T0⊂ ∂Mc, M admits an embedded projective plane and we have a connected summand of RP3 in M,
contradiction to M being hyperbolic. Hence, assume that ∂ N is an essential curve on T0. From this
situation we can construct a Seifert ﬁbred space properly embedded in M which is impossible since our
manifold is hyperbolic. To see this, note that the boundary of a small regular neighbourhood of T0∪ N
is a torus. Since our manifold is hyperbolic this torus must be inessential, and thus it must bound a solid
torus outside T0∪ N . Hence the Seifert structure on T0∪ N extends to a Seifert ﬁbering over this solid
torus with at most two exceptional ﬁbres, one at the centre line of the M¨obius band N .
(2) Edges are identiﬁed with coinciding orientation (i.e., B′C′ is identiﬁed with B′′C′′). In this case we have
a properly embedded annulus A⊂ Mc. Note that, since M is hyperbolic, A must be either compressible
or boundary-parallel. Hence, if one boundary component of A is an essential curve, the other one is,
too, and both are parallel curves on the same torus boundary component T0⊂ ∂Mc. In this case the
annulus A runs parallel to T0 with either AB and AC or BD and CD contained in the region between
A and T0. Now consider a torus running parallel to T0 and bounding a collar neighbourhood of T0 in
Mc containing A . Normalising this torus cannot result in a surface normally isotopic to T0 because A
acts as a barrier. Accordingly, the triangulation is not boundary efﬁcient. This gives a contradiction to
the triangulation being minimal due to Theorem 4.
If the boundary components are inessential, colour the bounding discs in the respective torus boundary
components. More precisely, colour the disc near vertex B purple , and the one near vertex C green .
W.l.o.g, edges AB and AC (truncated to run inside Mc) run inside the solid torus bounded by A . By
construction, the endpoint near B is purple and the endpoint near C is green. Moreover, the endpoints
near A must either both be purple or both be green (note that A must be compressible). It follows that
one of the edges AB and AC has endpoints with equal colours. It thus follows that this edge must be
in the neighbourhood of the respective torus boundary components of Mc, see Figure 9. Again, we use
Theorem 4 to produce a contradiction to the fact that the triangulation is minimal.
It follows that Obstruction 1. cannot occur.
Figure 8: Obstruction 1 (1). Edge B′C′ identiﬁed with edge C′′B′′ forming a punctured RP2, or M ¨obius
strip N (left). Obstruction 1 (2). Edge B′C′ identiﬁed with edge B′′C′′ forming an annulus A (right).
Obstruction 2. Faces from the front are identiﬁed with faces of the back (cf. Figure 7). As a result of such a
face identiﬁcation, the two edges B′C′ and B′′C′′ may become identiﬁed. If this the case we fall back onto the
cases dealt with in Obstruction 1. Again, we have two subcases:
(1) Face (A′B′C′) is identiﬁed with the face (B′′C′′D′′) or (A′′B′′C′′) is identiﬁed with the face (B′C′D′).
These situations are symmetric. As explained above we may assume that B′C′ and B′′C′′ are not identi-
ﬁed. Suppose we ﬂatten the two tetrahedra so that (A′B′C′) is identiﬁed with (A′′B′′C′′) and (B′C′D′) is
identiﬁed with (B′′C′′D′′). Since the interiors of B′C′ and B′′C′′ were initially disjoint, the preimage of a
point under this operation is either a point or an interval. In particular this ﬂattening operation is cell-like
12
Figure 9: Obstruction 1 (2). Both boundary components of A are inessential ∂Mc .
and hence preserves the homeomorphism type of the manifold M. This gives a new triangulation of M
with fewer tetrahedra which contradicts our assumption that the triangulation T is minimal.
(2) The face (A′B′C′) is identiﬁed with the face (A′′B′′C′′) or the face (B′C′D′) is identiﬁed with the face
(B′′C′′D′′). Again, these situations are symmetric. However, if face (A′B′C′) is glued to face (A′′B′′C′′)
without a twist, B′C′ is glued to B′′C′′ and we are done (alternatively, if (A′B′C′)↔ (A′′B′′C′′), then the
vertex at A′ = A′′ is a manifold point and T is not an ideal triangulation). If the two faces are identiﬁed
with a twist, all edges of the two triangles become identiﬁed. In particular B′C′ and B′′C′′ are identiﬁed
and, again, we are done.
Since we have that T contains at least three tetrahedra, and that all possibilities of having an edge of degree
two lead to a contradiction, there are no edges of degree two.
Lemma 10 Let T be a minimal ideal triangulation of a cusped hyperbolic 3–manifold M. Suppose LST⋆ is
a layered ∂ –punctured solid torus and there is a combinatorial map ϕ : LST ⋆→ M. Then ϕ is an embedding.
Proof We need to show that no identiﬁcations of the boundary faces of LST ⋆ are possible in T . If the two
triangles of ∂ LST⋆ are identiﬁed, then M is a punctured lens space, contrary to the assumption that M is
hyperbolic.
Hence, identiﬁcations can occur at most at the edges of ∂ LST⋆ . But it follows from Theorem 6 that not all
three edges of ∂ LST⋆ can be identiﬁed, and thus we only need to consider the case that two edges of ∂ LST⋆
are glued together.
A priori there are a total of six choices of how two boundary edges of ∂ LST⋆ can be identiﬁed (three pairs of
edges and two possible orientations each). Ignoring the third edge, all of them result in a quadrilateral with all
of its edges identiﬁed in the pattern shown in Figure 10 in the centre and the third boundary edge is one of he
two diagonals of the quadrilateral. Denote the unique boundary edge of the quadrilateral by e.
We now pass to a small regular neighbourhood N = Nhd(LST⋆∩Mc) of LST ⋆ in the compact core Mc of M.
By construction, its boundary ∂N must be a surface with boundary properly embedded in Mc. We can think
of ∂N as the surface consisting of the octagon lying in the interior of the quadrilateral of ∂ LST⋆, and two
quadrilaterals from the annulus that is the regular neighbourhood of the ideal edge e in Mc, see Figure 10
on the right. The surface is obtained by gluing the dotted edges of the octagon to the dotted edges of the
quadrilateral. The solid edges then denote the boundary of ∂N .
13
Figure 10: Left: Boundary of LST ⋆ . Centre: Boundary of LST ⋆ after disregarding the third boundary edge
with two boundary edges identiﬁed. Right: Octagon and two quadrilaterals making up the boundary ∂N of a
regular neighbourhood of LST⋆ in Mc . Dotted edges are identiﬁed, solid edges denote the boundary of ∂N .
Up to symmetry, there are three ways two perform these gluings (notice that the red edges of the octagon can
be paired with the red edges of the two quadrilaterals arbitrarily, but the orientation of the gluings is ﬁxed).
All of them are shown in Figure 11. The ﬁrst set of gluings results in a once-punctured torus. This type of
identiﬁcation implies that the only identiﬁcations of e are the ones from inside LST ⋆, a contradiction to the
assumption that a pair of boundary edges of LST ⋆ are identiﬁed in T . The second results in ∂N a once-
punctured Klein bottle, and the third results in ∂N a thrice-punctured sphere.
Figure 11: Three possible ways to obtain ∂N . Left: a once-punctured solid torus. Centre: a once-punctured
Klein bottle. Right: a thrice-punctured sphere.
Since ∂N is separating it cannot be a once-punctured Klein bottle. Hence, it is a separating thrice-punctured
sphere with all boundary components on the same boundary component T0 of Mc. A parity argument shows
that the number of essential boundary components of ∂N must be even. Moreover, note that, by construction,
T0∩ N is the neighbourhood of a pinched disc in T0 and thus connected.
It follows that T0∩ N must fall into one of two categories.
(1) Two boundary components of ∂N are essential and hence T0∩N must be equal to an annulus with a disc
removed. Since N is separating, this disc must be outside N and thus disjoint from e. Hence, pasting
this disc into T0∩ N yields a necessarily boundary-parallel annulus.
(2) No boundary component of ∂N is essential and hence T0∩ N must be equal to a subsurface of T0 with
two discs removed. Again, these discs must be outside N and thus disjoint from e. Pasting the discs into
T0∩ N results in a necessarily boundary-parallel disc.
Now, as in earlier arguments, consider a torus running parallel to T0 and bounding a collar neighbourhood of
T0 in Mc containing the annulus or disc. Normalising this torus cannot result in a surface normally isotopic
to T0 because it must be disjoint from e. Accordingly, the triangulation is not boundary efﬁcient. This gives
a contradiction to the triangulation being minimal due to Theorem 4 and thus ϕ : LST ⋆→ M must be an
embedding.
14
Lemma 11 Let T be a minimal ideal triangulation of a cusped hyperbolic 3–manifold M and e be an ideal
edge of degree three. Then e is contained in an embedded two tetrahedron subcomplex of T combinatorially
equivalent to the layered ∂ –punctured solid torus LST⋆(1,3,4). In particular, e is contained in a maximal
layered ∂ –punctured solid torus LST⋆, twice in its core tetrahedron and once in the tetrahedron adjacent to the
core, and no other edge in LST⋆ is of degree three.
Moreover, T contains at least three ideal tetrahedra and each ideal edge of degree three is contained in its own
subcomplex of this type.
Proof We may and will work with the pseudo-manifoldˆM. Let e∈ T be an edge of degree 3. If e is incident
with three distinct tetrahedra, then a 3-2–move produces a triangulation with fewer tetrahedra, contradicting
minimality of the triangulation. If e is incident with exactly one tetrahedron, it cannot be of degree 3. Hence, e
is incident with exactly two tetrahedra. A brute-force enumeration shows that there exists only one 2–tetrahedra
complex with an edge of degree 3 in its interior – the layered solid torus LST (1,3,4) (see case| ˜∆e| = 2 in
the proof of [21, Proposition 9] for details). Moreover, LST (1,3,4) has exactly one such degree 3 edge in its
interior. This edge occurs twice in its core tetrahedron and once in the other tetrahedron (i.e., the tetrahedron
adjacent to the core tetrahedron).
It follows from Lemma 10 that no identiﬁcations between the faces of this layered solid torus are possible,
hence the subcomplex is embedded, contained in a maximal layered ∂ –punctured solid torus and, in particular,
the triangulation contains at least three tetrahedra.
We remark that an analysis of edges of degree four and ﬁve can be carried out following [21], but this is not
needed for the main applications of this paper and hence omitted.
