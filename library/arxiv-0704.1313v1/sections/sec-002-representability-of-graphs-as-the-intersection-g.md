---
doc_id: arxiv-0704.1313v1
doc_title: "Mutant knots and intersection graphs"
section_id: sec-002-representability-of-graphs-as-the-intersection-g
section_title: "Representability of graphs as the intersection graphs of chord diagrams"
section_number: null
pages: 3-6
source_pdf: 0704.1313v1.pdf
source_sha256: a75bb39c60ec9b15
toc_source: outline
doc_brief: "Mutant knots and intersection graphs — We prove that if a ﬁnite order knot invariant does not disting uish mutant knots, then the corresponding weight system depends on the interse ction graph of a"
---
chord diagrams
Not every graph can be represented as the intersection graph of a chord diagram. For
example, the following graphs are not intersection graphs.
A characterization of those graphs that can be realized as interse ction graphs is given
by an elegant theorem of A. Bouchet [4].
On the other hand, distinct diagrams may have coinciding intersectio n graphs.
For example, next three diagrams have the same intersection grap h :
A combinatorial analog of the tangle in mutant knots is a share [5, 6]. Informally,
a share of a chord diagram is a subset of chords whose endpoints are separ ated into
at most two parts by the endpoints of the complementary chords. More formally,
Deﬁnition 1 A share is a part of a chord diagram consisting of two arcs of the outer
circle possessing the following property: each chord one of whose e nds belongs to
these arcs has both ends on these arcs.
Here are some examples:
A share Not a share Two shares
The complement of a share also is a share. The whole chord diagram is it s own share
whose complement contains no chords.
Deﬁnition 2 A mutation of a chord diagram is another chord diagram obtained by
a rotation/reﬂection of a share.
For example, three mutations of the share in the ﬁrst chord diagra m above produce
the following chord diagrams:
Obviously, mutations preserve the intersection graphs of chord d iagrams.
3
Theorem 2 Two chord diagrams have the same intersection graph if and on ly if they
are related by a sequence of mutations.
This theorem is contained implicitly in papers [3, 8, 11] where chord diag rams
are written as double occurrence words , the language better suitable for describing
algorithms than for topological explanation.
Proof of Theorem 2.
The proof of this theorem uses Cunningham’s theory of graph deco mpositions [9].
A split of a (simple) graph Γ is a disjoint bipartition {V1, V 2} of its set of vertices
V (Γ) such that each part contains at least 2 vertices, and there ar e subsets W1 ⊆ V1,
W2 ⊆ V2 such that all the edges of Γ connecting V1 with V2 form the complete
bipartite graph K(W1, W 2) with the parts W1 and W2. Thus for a split {V1, V 2} the
whole graph Γ can be represented as a union of the induced subgrap hs Γ( V1) and
Γ( V2) linked by a complete bipartite graph.
Another way to think about splits, which is sometimes more convenien t and which
we shall use in the pictures below, looks like follows. Consider two grap hs Γ 1 and Γ 2
each having a distinguished vertex v1 ∈ V (Γ 1) and v2 ∈ V (Γ 2), respectively, called
markers. Construct the new graph Γ = Γ 1 ⊠(v1,v2) Γ 2 whose set of vertices is
V (Γ) = {V (Γ 1) − v1} ⊔ {V (Γ 2) − v2}
and whose set of edges is
E(Γ) = {(v′
1, v ′′
1 ) ∈ E(Γ 1) : v′
1 ⁄= v1 ⁄= v′′
1 } ⊔ { (v′
2, v ′′
2 ) ∈ E(Γ 2) : v′
2 ⁄= v2 ⁄= v′′
2 } ⊔
{(v′
1, v ′
2) : ( v′
1, v 1) ∈ E(Γ 1) and ( v2, v ′
2) ∈ E(Γ 2)} .
Representation of Γ as Γ 1 ⊠(v1,v2) Γ 2 is called a decompositionof Γ, Γ 1 and Γ 2 are called
the components of the decomposition. The partition {V (Γ 1)−v1, V (Γ 2)−v2} is a split
of Γ. Graphs Γ 1 and Γ 2 might be decomposed further giving a ﬁner decomposition
of the initial graph Γ. Pictorially, we represent a decomposition by pic tures of its
components where the corresponding markers are connected by a dashed edge.
A prime graph is a graph with at least three vertices admitting no splits. A de-
composition of a graph is said to be canonical if the following conditions are satisﬁed:
(i) each component is either a prime graph, or a complete graph Kn, or a star Sn,
which is the tree with a vertex, the center, adjacent to n other vertices;
(ii) no two components that are complete graphs are neighbors, th at is, their mark-
ers are not connected by a dashed edge;
(iii) the markers of two components that are star graphs connect ed by a dashed edge
are either both centers or both not centers of their components .
W. H. Cunningham proved [9, Theorem 3] that each graph with at leas t six vertices
possesses a unique canonical decomposition.
Let us illustrate the notions introduced above by two examples of ca nonical de-
composition of the intersection graphs of chord diagrams. We numb er the chords and
4
the corresponding vertices in our graphs, so that the unnumbere d vertices are the
markers of the components. The ﬁrst example is our example from p age 3:
4
1
1 6
6
5
5
2 2
33
4
A chord diagram
4
/0
/0
/1
/1
/0
/0
/1
/1
/0
/0
/1
/1
/0
/0
/1
/1
/0
/0
/1
/1
3
2
6
5
1
/0
/0
/1
/1
The intersection graph
1/0/0
/0/0
/0/0
/1/1
/1/1
/1/1
/0/0
/0/0
/1/1
/1/1
/0/0
/0/0
/1/1
/1/1
/0
/0
/1
/1
/0/0
/0/0
/1/1
/1/1
/0
/0
/1
/1
/0/0
/0/0
/0/0
/1/1
/1/1
/1/1
/0/0
/0/0
/1/1
/1/1
/0
/0
/1
/1
6 5 4
2
3
/0/0
/0/0
/1/1
/1/1
The canonical decomposition
The second example represents the chord diagram of the double po ints in the plane
diagram of the Conway knot C from page 1. The double points of the shaded tangle
are represented by the chords 1,2,9,10,11.
6
3
2
11
1
9
10
11
7852 1
8 6 9 104
7
3
5
4
Chord diagram
9
/0
/0
/1
/1
/0
/0
/1
/1
/0
/0
/1
/1
/0
/0
/0
/1
/1
/1
/0
/0
/1
/1
/0
/0
/1
/1
/0
/0
/1
/1 /0
/0
/1
/1
/0
/0
/1
/1
/0
/0
/0
/1
/1
/1
4
3
68
5
1
211
10
7
/0
/0
/1
/1
Intersection graph
10
/0/0
/0/0
/1/1
/1/1
/0/0
/0/0
/1/1
/1/1
/0
/0
/1
/1
/0
/0
/1
/1
/0
/0
/0
/1
/1
/1
/0/0
/0/0
/0/0
/1/1
/1/1
/1/1
/0/0
/0/0
/0/0
/1/1
/1/1
/1/1
/0/0
/0/0
/0/0
/1/1
/1/1
/1/1
/0
/0
/0
/1
/1
/1
/0/0
/0/0
/1/1
/1/1
/0/0
/0/0
/0/0
/1/1
/1/1
/1/1
/0
/0
/1
/1
/0
/0
/1
/1 /0
/0
/1
/1
/0
/0
/1
/1
/0
/0
/0
/1
/1
/1
/0/0
/0/0
/1/1
/1/1
/0/0
/0/0
/1/1
/1/1
9
2111
4
368
5
7
/0/0
/0/0
/1/1
/1/1
Canonical decomposition
The key observation in the proof of Theorem 2 is that components o f the canoni-
cal decomposition of any intersection graph admit a unique represe ntation by chord
diagrams. For a complete graph and star components, this is obviou s. For a prime
component, this was proved by A. Bouchet [3, Statement 4.4] (see also [11, Section
6] for an algorithm ﬁnding such a representation for a prime graph) .
Now to describe all chord diagrams with a given intersection graph, w e start with
a component of its canonical decomposition. There is only one way to realize the
component by a chord diagram. We draw the chord corresponding t o the marker as a
dashed chord and call it the marked chord. This chord indicates the places where we
must cut the circle removing the marked chord together with small a rcs containing
its endpoints. As a result we obtain a chord diagram on two arcs. Rep eating the
same procedure with a neighbor component of the canonical decom position, we get
another chord diagram on two arcs. We have to sew these two diagr ams together by
their arcs in an alternating order. There are four possibilities to do t his, and they
diﬀer by mutations of the share corresponding to the second (or, alternatively, the
ﬁrst) component. This completes the proof of Theorem 2. □
To illustrate the last stage of the proof consider our standard exa mple and take
the star 2-3-4 component ﬁrst and then the triangle component. We get
/0
/0
/1
/1
/0
/0
/0
/1
/1
/1
/0/0
/0/0
/1/1
/1/1
/0
/0
/1
/1
4
2
3
CUT and
/0/0
/0/0
/1/1
/1/1
5
/0/0
/0/0
/0/0
/1/1
/1/1
/1/1
CUT/0
/0
/1
/1
Because of the symmetry, the four ways of sewing these diagrams produce only two
distinct chord diagrams with a marked chord:
CUT
and
CUT
;
5
repeating the same procedure with the marked chord for the last 1 -6 component of
the canonical decomposition, we get
/0/0
/0/0
/1/1
/1/1
6
1 /0
/0
/1
/1 CUT
/0/0
/0/0
/1/1
/1/1
Sewing this diagram into the previous two in all possible ways we get fou r mutant
chord diagrams from page 3.
As an enjoyable exercise we leave to the reader to work out our sec ond example
with the chord diagram of the diagram of the Conway knot and ﬁnd th e mutation
producing the chord diagram of the plane diagram of the Kinoshita–T erasaka knot
using the canonical decomposition.
