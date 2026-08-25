---
doc_id: arxiv-1203.6551v1
doc_title: "On the number of hyperbolic 3-manifolds of a given volume"
section_id: sec-003-7-associated-circle-packings-and-cusp-moduli
section_title: "Associated circle packings and cusp moduli"
section_number: 7
pages: 18-23
source_pdf: 1203.6551v1.pdf
source_sha256: a8e84f8ed63dbcca
doc_brief: "On the number of hyperbolic 3-manifolds of a given volume — The work of Jørgensen and Thurston shows that there is a ﬁnite number N (v) of orientable hyperbolic 3-manifolds with any given volum e v."
---
In this section we study the circle packing corresponding to the hyp erbolic
graph Wn shown in Figure 8.
n
Figure 8. Graph Wn with 2 n + 2 vertices
The two isometric polyhedra in the decomposition of the complement o f Wn
described in section 6 are obtained by gluing together n regular ideal octahedra
(see Figure 9 (right)). Therefore the volume of its complement is 2 nV8 where
V8 = 3 .663862 . . . is the volume of the regular ideal octahedron. A circle packing
corresponding to the graph is depicted in Figure 9 (left). Each tang ency point of
the circle packing corresponds to an annulus cusp of the complemen t of Wn.
. . . 
. . . 
Figure 9. A circle packing obtained from the graph Wn (left) and
a (topological) polyhedral decomposition (right)
Recall from Remark 2.1 that each torus cusp of a hyperbolic 3-manif old has a
Euclidean structure C/Γ where Γ ∼
= Z2 ⊂ C is a lattice, and its shape parameter
is determined by giving two independent translations corresponding to a choice of
basis for Γ. Since there are inﬁnitely many ways to choose such a bas is, this shape
parameter is not unique. The modulus of a torus cusp is deﬁned as the complex
ratio
z = (second shortest translation) /(shortest translation) . (7.1)
It is a complex number lying in the region |Re(z)| ≤ 1/2 and |z| ≥ 1. If z lies on
the boundary of this region, we choose it so that Re( z) ≥ 0.
For the complement of Wn, there are three diﬀerent types of annulus cusps,
see Figures 10, 11 and 12. The circle packing diagrams giving the cusp shapes
ON THE NUMBER OF HYPERBOLIC 3-MANIFOLDS OF A GIVEN VOLUME 19
are obtained by M¨ obius transformations which map one of the mark ed cusps to
inﬁnity. Since the graph complement is reconstructed by gluing the t wo isometric
polyhedra along their corresponding white faces, we get the bound ary of a horoball
neighbourhood of the annulus cusp by gluing two copies of rectangle s together
along corresponding edges depicted by solid lines. Later, we glue the se annuli cusps
together along their boundaries (depicted as dotted lines) to get a torus cusp, and
compute its modulus.
By using Lemma 6.1, we obtain hyperbolic links from Wn. The modulus of
each cusp can be computed by knowing how to glue the rectangles ac cording to the
gluing pattern of thrice punctured spheres.
. . . 
Figure 10. Cusp modulus for ideal vertices of type 1
. . . 
Figure 11. Cusp modulus for ideal vertices of type 2
n
. . . 
. . . 
Figure 12. Cusp modulus for ideal vertices of type 3
20 HODGSON AND MASAI
Example 7.1. The graph Gn,k in Figure 13 (top) is obtained from the graph
in Figure 8 by k + 2 applications of Lemma 6.1, where k + 2 ≤ n. The torus cusp
corresponding to the knot component (with k crossings) comes from the 2( k + 1)
marked vertices in Figure 13 (bottom). Note that in Figure 13 (also in Figure 15),
the choice of crossings below the crossing circles is not important, b ecause changing
an over crossing to an under crossing does not change the graph c omplement.
k
. . .
. . . 
k
. . . 
Figure 13. A graph Gn,k obtained from Wn (top) and vertices
corresponding to the knot component cusp (bottom)
In Figure 14, we depict the shapes of the torus cusps. The left diag ram shows
the shape of a crossing circle cusp without a half twist below, the midd le shows the
shape of a crossing circle cusp with a half twist, and the right shows t he shape of
the cusp which comes from the knot component.
2( k+1) 
. . . 
Figure 14. Shapes of the torus cusps for the graph Gn,k in Figure 13
The shape of the torus cusp of the knot component in Figure 13 is ob tained
by arranging 2 × 2(k + 1) copies of the 1 × 2 rectangle in Figure 11 to form a
2 × 4(k + 1) rectangle with opposite edges identiﬁed by translations. There fore, its
ON THE NUMBER OF HYPERBOLIC 3-MANIFOLDS OF A GIVEN VOLUME 21
cusp modulus is 2( k + 1)√−1. The modulus of each crossing circle cusp depends
on the existence of a half twist; if it has a half twist below, the modulus is √−1
and if not, it is 2 √−1. (Note that these moduli do not depend on the total number
of vertices in the graph Gn,k .)
8. Construction of diﬀerent manifolds sharing the same volu me
We start with the graph with 2 n vertices shown in Figure 15. This graph is
obtained by applying the gluing move in Lemma 6.1 n + 1 times to W2n.
. . . 
Figure 15. Starting point: graph with 2 n vertices (represented by circles)
First, we label every remaining pair of thrice punctured spheres by an element
of {0, 1}. For each such pair we apply Lemma 6.1 as follows. We glue the pair of
thrice punctured spheres labelled by 0 (resp. 1) without (resp. wit h) a half twist,
as in Figure 5 (left) (resp.(right)). By this construction, we get a h yperbolic link
complement Mb for each cyclic binary word b of length n and its volume is 4 nV8.
Now we consider the decomposition of Mb into isometric convex hyperbolic
polyhedra with shaded faces described in section 6.1. Note that eve ry edge lies in
exactly one shaded triangular face, since the faces have a checke rboard colouring.
Deﬁnition 8.1 ([20], [ 39]). Given an edge e in such a polyhedral decomposi-
tion, let t be the shaded ideal triangle containing e. Then the midpoint m of e is
the foot of the perpendicular in t from the vertex of t opposite e to e.
Since isometries preserve angles, when we glue two thrice puncture d sphere
boundaries together by an isometry, it maps midpoints to midpoints. Moreover,
for fully augmented links, we may expand horoball neighbourhoods o f the cusps
to ﬁnd a horoball packing such that the horoballs bump together pr ecisely at the
midpoints of edges. More precisely,
Theorem 8.2 ([20], [ 39]). Let L be a fully augmented link. Then there exist
horoball neighbourhoods of the cusps of S3 \ L such that the midpoint of every edge
is a point of tangency of the corresponding horospherical to ri.
Remark 8.3. For each Mb, we ﬁx the horoball packing Hb given by Theorem
8.2. In fact, this horoball packing depends only on the geometry of Mb and not on
any choice of polyhedral decomposition for Mb. This follows since the horospherical
tori for Hb can be deﬁned as follows: For each cusp with modulus √−1 or 2 √−1
we choose the horospherical torus of area 2, and for each cusp w ith modulus m√−1
with m > 2 we choose the horospherical torus of area 4 m. These areas are easily
22 HODGSON AND MASAI
calculated from the diagrams in Figures 10–12 and Figure 14, using th e fact that
each dotted edge in Figures 10-12 has length 1 in the horospherical tori for Hb,
(since it is a horocycle joining midpoints of edges in an ideal hyperbolic t riangle).
Theorem 8.4. Let bi be a binary cyclic word of length n ≥ 3 and let Mbi be
the hyperbolic link complement obtained from bi by the above procedure for i = 1, 2.
Then Mb1 is isometric to Mb2 if and only if b1 and b2 are related by the natural
action of Dn, the dihedral group of order 2n.
Proof. Let b be a binary cyclic word of length n. If b contains k ≥ 1 zeros,
then we can split b into k subwords of the form pi = 011 · · ·10 with i 1’s (i ≥ 0) by
using each zero in b exactly twice.
After the gluing move in Lemma 6.1, each pi produces a torus cusp with 2 i + 1
crossings, whose modulus is mi = 2(2i + 2)√−1 = 4( i + 1)√−1 (see Example 7.1).
Let {pi1, pi2 , ..., pik } be the decomposition of b, and let Cj be the cusp corresponding
to the knot component produced by pij . We get a cyclic sequence {mi1, mi2 , ..., mik }
of cusp moduli from b. Note that the total number of cusps of Mb is 2n + 1 +k; the
crossing circle cusp C at the top of Figure 15 has modulus n√−1 (from the cusp
diagram in Figure 12), and the other 2 n crossing circle cusps have modulus √−1
or 2 √−1 by Example 7.1.
We now only consider cusps whose modulus has norm greater than 2. For
n ≥ 3, these are the cusps C1, . . . Ck and C. From Mb, we will construct a labelled
cusp graph Cb with vertices {v1, v2, ..., vk+1} as follows. We label vj by mij for
1 ≤ j ≤ k and vk+1 by n√−1, the modulus of C. Then join vi and vi′ by an edge if
in Hb, horoball neighbourhoods of the cusps corresponding to vi and vi′ are tangent
to each other. In Hb, the horoball neighbourhood of each cusp Cj bumps only into
Cj−1, Cj+1 (with index modulo k), and C. Therefore, the graph Cb consists of a
cycle of length k whose vertices are labelled cyclically by the mij ’s and one vertex
labelled by n joined to every vertex of the cycle.
The special case when b = 111 · · ·1 and k = 0 is slightly diﬀerent. Then Mb has
one cusp C of modulus n√−1 as above, two knot components giving cusps C1, C2
of modulus 2 n√−1, and 2 n cusps of modulus √−1. In this case, the cusp graph Cb
is a 3-cycle.
Conversely given such a labelled cusp graph, we can reconstruct a b inary cyclic
word. Therefore given two binary cyclic words b1 and b2 of length n, the graph Cb1
is isomorphic to Cb2 as a graph with labelled vertices if and only if b1 is related to
b2 by the natural action of Dn. Moreover, by Remark 8.3, any isometry between
manifolds Mb1 and Mb2 takes the horoball packing Hb1 to Hb2 . Hence, the manifold
Mb1 is isometric to Mb2 if and only if the graph Cb1 is isomorphic to Cb2 as a graph
with labelled vertices. This completes the proof. □
Theorem 8.5. For each n ≥ 3, there are at least 2n/(2n) diﬀerent hyperbolic
link complements of volume 4nV8.
Proof. By theorem 8.4, there are at least as many hyperbolic link complement s
of volume 4 nV8 as cyclic binary words of length n, up to the action of Dn. But
there are 2 n based cyclic binary words of length n, and each orbit under the Dn
action has at most 2 n elements. So the result follows. □
ON THE NUMBER OF HYPERBOLIC 3-MANIFOLDS OF A GIVEN VOLUME 23
Remark 8.6. For the sequence vn = 4 nV8, this gives a logarithmic growth
rate
lim sup
n→∞
log NL(vn)
vn
≥ log 2
4V8
≈ 0.0472962.
Chesebro-BeBlois [ 11] construct examples of 2 n/2 hyperbolic link complements of
volume wn ≈ 24.092184n + 2V8, giving a logarithmic growth rate
lim sup
n→∞
log NL(wn)
wn
≥ 0.0287706.
