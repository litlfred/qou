---
doc_id: arxiv-math-0411505v2
doc_title: "A NON-COMMUT A TIVE FORMULA FOR THE COLORED JONES FUNCTION"
section_id: sec-005-3-the-arc-graph-of-a-knot-projection
section_title: "The arc-graph of a knot projection"
section_number: 3
pages: 5-7
source_pdf: 0411505v2.pdf
source_sha256: a38cec365e0a227e
doc_brief: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION — The colored Jones function of a knot is a sequence of Laurent p olynomials that encodes the Jones polynomial of a knot and its parallels."
---
Given a knot projection K, we deﬁne the arc-graph GK as follows:
• The vertices of GK are in 1-1 correspondence with the arcs of K.
• The edges of GK are in 1-1 correspondence with transitions ofK, when we walk along K and we
either go under a crossing (blue edges), or jump up at a crossing (r ed edges) according to Figure 1.
ia
ja
i+1aia
ja
i+1a
Figure 1. From a planar projection to the arc-graph. Transitions in th e planar projection are indicated by
dashed paths, and the corresponding edges in the arc-graph a re blue (depicted with a small circle on them) or
red
More formally, GK is a weighted digraph deﬁned as follows.
5
Deﬁnition 3.1. The arc-graph GK has r + 1 vertices 1 , . . . , r+ 1, r + 1 blue directed edges (v, v + 1) (v taken
modulo r + 1) and r + 1 red directed edges (u, v), where at the crossing u the arc that crosses over is labeled
by av.
The vertices of GK are equipped with a sign, where sign( v) is the sign of the corresponding crossing v of
K, and the edges of GK are equipped with a weight. The edge-weights are speciﬁed by matrix WK = ( βij)
where
βe =
{
t−sign(v) if e = (v, v + 1)
1− t−sign(v) if e = (v, u)
Here t is a variable. Let WK denote the matrix obtained from WK by deleting the last row and column.
Notice that WK is formally stochastic (i.e., the sum of the rows of I− WK is zero), but WK is not.
Let (GK , WK) denote the weighted digraph obtained by deleting the r + 1 vertex from GK, together with
all edges to and from it. We let VK and EK denote the set of vertices and edges of GK.
It is clear from the deﬁnition that from every vertex of GK, the blue outdegree is 1, the red outdegree is
1, and the blue indegree is 1. It is also clear that GK has a Hamiltonian cycle that consists of all the blue
edges. We denote by eb
i (er
i ) the blue (red) edge leaving vertex i.
Example 3.2. For the ﬁgure 8 knot we have:
a 2
+2
−1 −3
+4
a 4 a 1 a 3
*
Its arc-graph GK with the ordering and signs of its vertices and GK = GK−{ 4} are given by
GK =
+2
−1+4
−3
GK = +2
−3
−1
where the blue edges are the ones with circles on them. Moreover,
WK =




0 t 0 1 − t
1− ¯t 0 ¯t 0
0 1 − t 0 t
¯t 0 1 − ¯t 0



 .
Deﬁnition 3.3. LetK be a knot projection. The writhe ofK, ω(K), is the sum of the signs of the crossings
ofK, and rot( K) is the rotation number of K, deﬁned as follows: smoothen all crossings of K, and consider
the oriented circles that appear; one of them is special, marked by ⋆. The number of circles diﬀerent from
the special one whose orientation agrees with the special one, minu s the number of circles whose orientation
is opposite to the special one is deﬁned to be rot( K). We further let δ(K, n) = 1 /2(n2ω(K) + nrot(K)), and
δ(K) = δ(K, 1).
We remark that we deﬁne rot( e) for each edge e of GK in Deﬁnition B.6.
6
