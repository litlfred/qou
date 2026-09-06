---
doc_id: arxiv-1808.02836v2
doc_title: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds"
section_id: sec-010-26-faces-in-minimal-ideal-triangulations-of-cusp
section_title: "Faces in minimal ideal triangulations of cusped hyperbolic 3–manifolds"
section_number: 2.6
pages: 7-10
source_pdf: 1808.02836v2.pdf
source_sha256: 0224a296253122a2
doc_brief: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds — Previous work of the authors studies minimal triangulations of closed 3–manifolds using a characterisation of low degree edges"
---
(a) triangle
 (b) cone
 (c) M ¨obius
 (d) 3–fold
 (e) dunce
Figure 2: Types of faces. The M¨obius, 3–fold and dunce faces only have one vertex due to the edge identiﬁ-
cations. A cone face may have one or two vertices and a triangle face may have up to 3 vertices.
An ideal triangle in an ideal triangulation of a cusped hyperbolic 3–manifold M may have some of its edges
identiﬁed. There are eight possible types of triangular faces in the triangulation of the end-compactiﬁcation ˆM,
depending on how vertices or edges are identiﬁed (see Figure 1 in [17]). Ignoring possible identiﬁcations of
vertices as in [26], this reduces to ﬁve types in M based on edge identiﬁcations only (see Figure 2). We name
the faces in M according to their topology in ˆM. A face with no edge-identiﬁcations is termed a triangle face;
it is a 2–simplex, possibly with some or all of its vertices identiﬁed. If a pair of edges is identiﬁed, the face is
either a cone (possibly with the tip identiﬁed with the vertex on the boundary) and called a cone face or it is a
M¨obius band and called a M¨obius face. In a M ¨obius face, we distinguish the boundary edge and the core edge.
If all three edges are identiﬁed, the face is either a 3–fold or a dunce hat, and called a 3–fold face or dunce face
respectively.
For minimal ideal triangulations, we can prove the following statement.
Theorem 6 Let T be a minimal ideal triangulation of a cusped hyperbolic 3–manifold M. Then there is no
3–fold face and there is no dunce face.
Proof Choose a compact core Mc of M with the property that each boundary component of Mc is a vertex
linking surface. Let t be a triangle of T .
Case 1: t is a 3–fold face. Refer to Figure 3. Let e be the edge of t, N(e) a small regular neighbourhood of
e in M and Nc(e) = N(e)∩ Mc. The frontier of Nc(e) in Mc is an annulus; we call this the exchange annulus
around e . Let N(t) be a regular neighbourhood of t in M. Then the boundary of Nc(t) = N(t)∩ Mc has a
natural cell decomposition into two hexagons corresponding to the two sides of t and three quadrilaterals that
are subsurfaces of the exchange annulus around e. The edges of the hexagons through the interior of Mc are
termed the long edges. Seen with respect to (t∩ Mc)\ N(e) the long edges of the hexagons have a natural
labelling 1,2,3 in cyclic order. See Figure 3 on the right for a drawing of Nc(t), in particular the two hexagons
and their long edges.
7
Give t a transverse orientation. This allows us to refer to one of the hexagons as the top hexagon and to the
other as the bottom hexagon. The intersection t∩ Nc(e) is a tripod times [0,1]. Figure 3 on the left depicts a
cross-section of the tripod times [0,1] at some x∈ (0,1). The transverse orientation of t is in the same direction
at the legs of the tripod (either all clockwise or all anti-clockwise around the vertex of the tripod). It follows
that the quadrilaterals join each long edge of the top hexagon to a long edge of the bottom hexagon. Moreover,
on the labels this induces a 3–cycle. Thus, modulo orientation, the identiﬁcation must be as shown in Figure 3
(both on the left and on the right).
After collapsing the sections of the exchange annulus to the long edges of the hexagons, we obtain a connected,
orientable, bounded surface S decomposed into two hexagons, nine edges and six vertices – and thus of Euler
characteristic−1. As can be deduced from the vertex labels, the surface has three boundary components and
thus must be a 3–punctured sphere.
Figure 3: Left: Cross-section through the neighbourhood Nc(t) of an ideal 3–fold t near its boundary edge
e. The cross-section through the top and bottom hexagon of the right picture appear as green and purple
lines respectively. Their endpoints mark the cross-section through the long edges of the respective hexagons.
Labels coincide with the ones on the right. Right: Truncated boundary Nc(t) of regular neighbourhood of
the 3–fold face t (drawn in the centre in black). Its boundary surface is connected, of Euler characteristic
−1 with three boundary components (each containing two edges, as indicated by the edge labels) and thus a
3–punctured sphere. The dotted blue lines with labels represent the intersection of t with the boundary torus
T0 – a triple arc between nodes 1 and 2 , or the Θ–graph.
Because t is a 3–fold, the intersection of t with a boundary torus T0⊂ ∂Mc consists of two nodes and three
(normal) arcs, all running between the two nodes, also known as the Θ–graph, see the dotted arcs in Figure 3.
Since S has three boundary components meeting T0 along the boundary of a neighbourhood of t∩ T0, the
complement of the embedding of the Θ–graph into T0 must have three boundary components.
If no two arcs form a separating (i.e., inessential) curve on T0, then the Θ–graph forms a spine of T0. In
particular, its complement is a disc with a single boundary component, a contradiction. Hence, two arcs must
bound a disc inT0. The remaining arc now either runs parallel to the ﬁrst two, or completes each of the other two
to an essential curve on T0. In both cases the complement has three boundary components. Both embeddings
are shown in Figure 4.
Assume that we are in the latter situation and the Θ–graph contains an essential curve on T0. Since the embed-
ding features two parallel arcs, one of the boundary curves of S bounds a disc in T0. Pasting in this disc and
8
pushing it into the interior of the manifold yields a properly embedded annulus which, becauseM is hyperbolic,
must be compressible or boundary parallel. If it is compressible, then T0 is compressible. We conclude that S
must be boundary parallel.
Hence assume that the Θ–graph consists of three parallel arcs and is thus contained in a disc of T0. This time
two of the boundary curves of S bound discs in T0 and pasting them in and pushing them into the manifold
yields a properly embedded disc, and we conclude again that S must be boundary parallel.
In both cases, uniting S with the complement of N(t∩ T0) in T0 thus produces a torus
T0\ N(t∩ T0)∪ S
boundary parallel to T0 and disjoint from e (which is itself incident to T0). It follows that normalising this
boundary parallel torus cannot result in a surface normally isotopic to T0 and thus T cannot be boundary
efﬁcient. This is impossible since we assume that T is minimal and thus boundary efﬁcient by Theorem 4.
Figure 4: Two embeddings of the intersection of the 3–fold face t with torus boundary component T0. Left:
trivial embedding contained in a disc of T0; in this case the boundary parallel torus is made up of a once-
punctured torus and two discs that are subsurfaces of T0 and the 3–punctured sphere S . Right: two parallel
essential loops; in this case the boundary parallel torus is made of a disc and an annulus that are subsurfaces
of T0 and the 3–punctured sphere S .
Case 2: t is a dunce face. Refer to Figure 5. Let e be the edge of t. We use the notation and set-up as in
the previous case. The intersection of t with Nc(e) is again a tripod times an interval (see Figure 5 on the left
for a cross-section). However, now the transverse orientations do not all agree: two are in one direction and
the last is in the opposite direction. In particular, this implies that each of the hexagons has two of its long
edges connected by a quadrilateral on the exchange annulus, and exactly one long edge of the top hexagon is
joined to a long edge of the bottom hexagon (and these edges do not share the same label). It follows that, up
to symmetry, there is only a single way to identify the long edges of the hexagons, shown in Figure 5 (both on
the left and on the right).
The two hexagons again form a properly embedded 3–punctured sphere S⊂ Mc. The dunce hat t itself
meets ∂Mc in two nodes and three normal arcs: two loops, one at each node, and one arc connecting the
two nodes – also known as the barbell graph. Up to the action of the mapping class group, there are four
possibilities of embedding the barbell graph into a torus boundary component T0⊂ ∂Mc, producing three
boundary components in a regular neighbourhood of the graph: One where both loops are essential in T0 and
thus necessarily parallel; one where one loop is inessential and the other one is an arbitrary essential curve
in T0; and two where both loops are inessential. See Figure 6 for a picture of all four cases. Using the
same pasting argument as in Case 1 we can conclude that S is boundary parallel. Again, uniting S with
the complement of N(t∩ T0) produces a torus boundary parallel to T0 and disjoint from e. Thus, Theorem 4
produces a contradiction.
Remark 7 The preconditions of Theorem 6 are necessary: the minimal triangulation of the Gieseking man-
ifold has dunce faces, and there exists a minimal 2-tetrahedron triangulation of a 3–manifold with two Klein-
bottle cusps, in which one of the four faces is a 3–fold face.
9
Figure 5: Left: Cross-section through the neighbourhood Nc(t) of an ideal dunce hatt near its boundary edge
e. Labels coincide with the ones on the right. Right: Truncated boundary Nc(t) of regular neighbourhood of
the dunce hat t (drawn in the centre in black). The boundary surface is connected, of Euler characteristic−1
with three boundary components (one containing four edges and two containing a single edge, as indicated by
the edge labels) and thus a 3–punctured sphere. The dotted lines with vertex labels represent the intersection
of t with the boundary torus T0, two disjoint loops and a connecting arc.
Moreover, Frigerio, Martelli and Petronio describe classes of orientable hyperbolic manifolds Mg,k with k
torus cusps and one end of type an orientable surface of genus g [10]. They show, that these manifolds admit
minimal (g + k)–tetrahedra ideal triangulations if and only if g > k, or g = k and g even, see [10, Proposition
1.4]. Such triangulations must necessarily have 3 k cone faces, and (2g− k) dunce- or 3–fold faces, see [10,
Lemma 2.1]. Hence, for g large enough, there exist minimal ideal triangulations of orientable hyperbolic
3–manifolds with all but an arbitrarily small portion of faces being dunce- or 3–fold-faces.
