---
doc_id: arxiv-1203.6551v1
doc_title: "On the number of hyperbolic 3-manifolds of a given volume"
section_id: sec-002-6-hyperbolic-graphs-with-parabolic-meridians
section_title: "Hyperbolic graphs with parabolic meridians"
section_number: 6
pages: 15-18
source_pdf: 1203.6551v1.pdf
source_sha256: a8e84f8ed63dbcca
doc_brief: "On the number of hyperbolic 3-manifolds of a given volume — The work of Jørgensen and Thurston shows that there is a ﬁnite number N (v) of orientable hyperbolic 3-manifolds with any given volum e v."
---
In this section, we recall some results on hyperbolic graphs in S3 with parabolic
meridians; for details see [ 26] and [ 34]. In this paper, spatial graphs may contain
link components, and we regard every link as a spatial graph without vertices. We
use the word link to emphasize that the graph does not have any vertices. Let G
be a spatial trivalent graph in S3 and let N be a manifold obtained from S3 \ G
by removing an open regular neighbourhood of each vertex. Then N is a manifold
with boundary consisting of thrice punctured spheres, one corre sponding to each
vertex of G. We say that G is hyperbolic if N admits a hyperbolic metric of ﬁnite
volume with geodesic boundary; then the meridians of the graph cor respond to
parabolic isometries. We can construct a hyperbolic link from a hyper bolic graph
by using the following.
Lemma 6.1 ([34]). For hyperbolic graphs, the moves shown in Figure 5 are
volume preserving, where regular neighbourhoods of the two trivalent vertices have
been removed in middle diagram.
16 HODGSON AND MASAI
gluing
cutting cutting 
gluing3 2
1
1
3 2
Figure 5. Volume preserving moves on hyperbolic graphs
Proof. Note that each vertex in a hyperbolic graph corresponds to a tota lly
geodesic thrice punctured sphere and each edge corresponds to an annulus cusp.
Moreover, the hyperbolic structure on a thrice punctured spher e is unique by [ 2];
hence any orientation preserving homeomorphism between hyperb olic thrice punc-
tured spheres is isotopic to an isometry. Since any homeomorphism b etween thrice
punctured spheres is uniquely determined by its action on the cusps , we may denote
homeomorphisms as elements of S3, the symmetry group of degree 3.
Fix labels for the cusps of the thrice punctured spheres as in Figure 5. If we glue
the boundaries via the homeomorphism corresponding to the identit y permutation,
then we get the tangle on the left of Figure 5. If we glue the boundar ies via the
homeomorphism corresponding to the permutation interchanging 2 and 3, we get
the tangle on the right of Figure 5.
Figure 6. Gluing by a homeomorphism
This is illustrated in Figure 6. Here we regard S3 as B3 ∪ B3 where one ball
B3 is a regular neighbourhood of a vertex of the graph shown in the midd le of
Figure 5. We then reverse the inside and the outside with respect to the boundary
sphere S2 = ∂B 3. After gluing, we get a link or graph in S2 × S1. The component
coming from the cusp labelled by 1 is a loop which corresponds to a gene rator of
ON THE NUMBER OF HYPERBOLIC 3-MANIFOLDS OF A GIVEN VOLUME 17
the fundamental group of S2 × S1, and its complement is homeomorphic to a solid
torus. Thus we get a tangle as shown on the left or right of Figure 5.
The inverse move (left or right to middle) is valid since any essential th rice
punctured sphere (or, 2-punctured disk) in a hyperbolic 3-manifo ld is totally geo-
desic ([ 2]). Since we are dealing with hyperbolic graphs, the 2-punctured disk on
the left or right of Figure 5 is essential (see [ 39] Lemma 2.1). □
Deﬁnition 6.2. A fully augmented link is a link obtained by applying the
gluing moves of Lemma 6.1 to a planar diagram of a hyperbolic graph (em bedded
in the plane) so that the resulting graph is actually a link. A crossing circle is a
component of a fully augmented link which appears as a circle in Figure 5 . A knot
component of a fully augmented link is a component which is not a crossing circle.
Remark 6.3. These deﬁnitions of a fully augmented link, a crossing circle,
and a knot component are equivalent to the original deﬁnitions in [ 20] or [ 39].
6.1. Polyhedral decomposition for the complement of a hyper bolic
graph with a planar diagram. Given a hyperbolic graph P with a planar dia-
gram D, let V be the set of vertices of P and NP = S3 \P \(∪v∈V N (v)) where N (v)
is a regular neighbourhood of v. Let Π be the plane containing D. Then NP admits
hyperbolic metric of ﬁnite volume with geodesic boundary. We can dec ompose NP
into two isometric convex ideal hyperbolic polyhedra by the following p rocedure,
depicted in Figure 7.
Step 1: Cut NP along Π.
Step 2: Collapse each edge of P to a point.
Let L be a fully augmented link which is obtained from D by the gluing moves
of Lemma 6.1. Then this decomposition is exactly equal to the decomp osition of
S3 \ L found by Agol-Thurston in [ 32] (see also [ 20], [ 39]).
Figure 7. Polyhedral decomposition of a graph complement
We shade the faces coming from the thrice punctured sphere boun daries of NP
and leave the faces on Π white as in [ 20], [ 39]. Note that every shaded face is an
ideal triangle, and since reﬂection φ about Π leaves each thrice punctured sphere
boundary invariant, the shaded faces are all orthogonal to the a djacent white faces.
Hence the dihedral angle of each edge is π/2. Since φ preserves white faces, each
face of these polyhedra is totally geodesic. Hence each white face e xtends to the
boundary at inﬁnity S2
∞ of hyperbolic space to give a Euclidean circle and such
circles corresponding to adjacent faces are tangent to each oth er. Therefore the
white faces of each polyhedron determine a circle packing of S2
∞ whose nerve is
isomorphic to the dual of the original graph diagram D.
18 HODGSON AND MASAI
