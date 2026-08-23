---
doc_id: cuspshapes
doc_title: "CUSP SHAPE AND TUNNEL NUMBER"
section_id: sec-004-4-pinched-handlebodies
section_title: "Pinched handlebodies"
section_number: 4
pages: 8-10
source_pdf: CuspShapes.pdf
source_sha256: 01db19e63193e6ae
doc_brief: "CUSP SHAPE AND TUNNEL NUMBER — We show that the set of cusp shapes of hyperbolic tunnel number one manifolds is dense in the Teichm¨ uller space of the torus."
---
We will glue the compression bodies of the previous section to carefully constructed
handlebodies, obtaining manifolds with a Heegaard splitting of genus n + 1. To
ensure there is not a Heegaard splitting of lower genus, we will use techniques
of [8] to bound the Hempel distance of the splitting. In this section we review the
CUSP SHAPE AND TUNNEL NUMBER 9
necessary background, particularly Hempel distance, and state the relevant results
on a handlebody.
Let S be a closed, oriented, connected surface, and let C(S) denote the curve
complex of S. ThusC(S) is the simplicial complex with vertices corresponding to
isotopy classes of simple closed curves, with a collection of k + 1 curves forming a
k simplex when the curves can be realized disjointly on S. Distance in C(S) is the
minimum number of edges in any path in the 1-skeleton.
Deﬁnition 4.1. Suppose a compression body or handlebody has outer boundary S.
The disk set inC(S) consists of vertices that correspond to boundaries of essential
disks in the compression body. Thus a Heegaard splitting of a 3-manifold along S
has two disk sets, one on either side. The Hempel distance of the Heegaard splitting
is the minimal distance in C(S) between the disk sets; see Hempel [ 17]. We denote
the disk set of a compression body or handlebody C byD(C).
The Hempel distance is relevant to us because it can be used to show a manifold
has tunnel number n: Scharlemann and Tomova showed that if the Hempel distance
of a genus g Heegaard splitting is strictly greater than 2 g, then the manifold will
have a unique Heegaard splitting of genus g and no Heegaard splitting of smaller
genus [33]. We wish to build manifolds with Heegaard splittings of high distance.
Suppose P is a disjoint collection of curves on S. Recall that a multitwist on P is
a collection of Dehn twists, one for each curve of P .
Lemma 4.2. Let C0 denote the maximally pinched structure on C(1;n + 1) of
Lemma 3.9. Let P denote the pinched curves on the outer boundary S; note these
form a maximal simplex of C(S).
(1) There exists a maximally pinched structure H0 on a handlebody H of genus
n + 1 such that the pinching is along curves of P⊂S∼=∂H .
(2) More generally, assuming results of [26], there exists a maximally pinched
structureH0 on a handlebody H of genus n + 1 with pinched curves P⊂S
such that if T is a multitwist on P , and D0 is the disk set of H0, then the
distance between disk sets of C0 and of T (D0) is at least 2n + 3.
Proof. The ﬁrst part of the lemma is straightforward. For example, take any
homeomorphism of C to the compression body in a Heegaard splitting of any one-
cusped 3-manifold of genus n + 1, and mark the curves P on S. Let H be the
handlebody of the splitting, also with curves P marked on S. Then the fact that
there is a maximally pinched structure on H with curves of P pinched to parabolics
follows from Thurston’s Uniformization theorem (see Morgan [28]).
The second part follows as in the proof of Theorem 4.12 of [ 8]. Let H(S) denote
the handlebody graph, consisting of a vertex for each handlebody with boundary S
and an edge between handlebodies whose disk sets intersect in the curve complex
C(S). The distance between handlebodies in H(S) is deﬁned to be the minimal
number of edges in a path between them in H(S). Abusing notation slightly, we
let D :H(S)→C (S) be the relation taking a handlebody V ∈H (S) to the disk set
D(V ) of V . Let h be the relation taking a disk set D(C) of a compression body C
with outer boundary S to the handlebody complex H(S), such that h maps D(C)
to the set h(D(C))⊂H (S) consisting of all V ∈H (S) for which D(C) is a subset of
D(V ). In particular, D(h(D(C0))) is a subset of C(S). Let X0 be the set
X0 ={h(T (D(C0)))∈H (S)|T is a multitwist on P},
10 VINH DANG AND JESSICA S. PURCELL
so X0 is the subset ofH(S) consisting of all handlebodies whose disk sets contain
T (D(C0)) for some multitwist T .
Now, a Dehn twist along a curve in P is an isometry ofC(S) ﬁxing P pointwise.
Thus if T is any multitwist on P , the distance from D(C0) to P is equal to the
distance from T (D(C0)) to P . Call this distance R0.
Then X0 has bounded diameter in H(S), for if V,W ∈ X0, then there are
multitwistsT1 and T2 such that T1(D(C0))⊂D(V ) and T2(D(C0))⊂D(W ). Then
d(D(V ),D (W ))≤d(D(V ),P ) +d(P,D (W ))
≤d(T1(D(C0)),P ) +d(P,T 2(D(C0))) = 2R0,
where d(·,·) denotes minimal distance in C(S). The distance in the handlebody
graph is bounded by one more than the distance in C(S); see [8, Lemma 4.11]. Hence
X0 has bounded diameter in H(S).
By work of Maher and Schleimer, H(S) has inﬁnite diameter [ 26]. Thus we may
choose a handlebody Y inH(S) such that for all V ∈ X0, the distance in the
handlebody graph between Y and V is at least 2n + 3.
Now, take a maximally pinched structure on Y with curves P on ∂Y pinched;
again such a structure exists by Thurston’s Uniformization Theorem [28]. □
Maximally pinched structures on handlebodies have been studied in depth. For
example, Keen and Series examined maximally pinched structures on genus 2 han-
dlebodies, and showed they are obtained by solutions to polynomials, one for each
curve on the 4-punctured sphere, each giving unique geometry [21].
More generally, the limit sets of maximally pinched structures are known to be
circle packings, given by limit sets of 3-punctured spheres that form the boundary at
inﬁnity of such a manifold [ 20]. When we take the convex core of such a structure,
we cut out the half-space bounded by each circle in the circle packing, obtaining in
the quotient a ﬁnite volume space whose boundary consists of embedded, totally
geodesic 3-punctured spheres.
The interiors of these convex cores can have a wide range of geometry. As
one example, the universal cover of a maximally pinched structure on a genus 2
handlebody is shown in [ 29, page 200]. There are four red circles shown the picture,
and a fundamental domain for the manifold is obtained by cutting out hyperplanes
bounded by these circles; the manifold is formed by gluing the boundaries of those
hyperplanes in pairs. See also Figure 7.7 in [ 29, page 205]. The convex core of the
manifold is then obtained by cutting out hyperplanes bounded by “dual circles,”
enclosing the black curvilinear triangles, and an additional circle enclosing all three
black triangles. Note that a fundamental domain for the convex core is therefore a
regular ideal octahedron.
