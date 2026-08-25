---
doc_id: arxiv-math-0411505v2
doc_title: "A NON-COMMUT A TIVE FORMULA FOR THE COLORED JONES FUNCTION"
section_id: sec-009-6-cabling-of-the-arc-graph
section_title: "Cabling of the arc graph"
section_number: 6
pages: 9-11
source_pdf: 0411505v2.pdf
source_sha256: a38cec365e0a227e
doc_brief: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION — The colored Jones function of a knot is a sequence of Laurent p olynomials that encodes the Jones polynomial of a knot and its parallels."
---
Recall the operation of cablingK(n) the knot projection K n times. Recall that a1, . . . , ar+1 are the arcs
ofK. Each al is in the cabling replaced by n2 arcs al
i,j, i, j = 1 , . . . , n, with the agreement that the ’long
arcs’ obtained by cabling arc ak will be ak
1j, j = 1, . . . , n and the ’small arcs’ obtained by cabling of crossing
k will be denoted by ak
ij for i = 2, . . . , n and j = 1, . . . , n. Note that all crossings which replace the original
crossing k have the same sign, equal to the sign of the crossing k. We make the following agreement: assume
the parallel arcs al
i,1, . . . , al
i,n go horizontally from left to right. Then al
i,1 is the upmost one. See ﬁgure
below for part of Example 3.2 and of its 3-cabled version K(3):
1a 3a
a 13
3
a 12
3
a 11
3
a 13
4
a 23
4
a 33
4
a 13
1a 11
1 a 12
1
4a 4
a 12
4a 11
4
a 21
4
a 31
4 a 32
4
a 22
9
We further let K (n) denote the link obtained from K(n) by deletion of the n special long arcs ar+1
1j ,
j = 1, . . . , n.
Next we consider the arc-graph of the cabling of K. For example, part of the red-blue digraph GK of
Example 3.2 and of its 3-cabled version is depicted as follows:
a
a 23
4
a 33
4a 32
4
a 22
4
a 12
4
a 31
4
a 21
4
a 11
4 4
1
a 3
a 4
a 13
1a 12
1a 11
1
a 13
3
a 12
3
a 11
3
a 13
where vertical edges are blue and horizontal edges are red.
We now deﬁne an n-cabling G(n)
K of the arc-graph GK . Cabling of a planar projection is a local operation,
and so is cabling of a digraph. In the language of combinatorics, we blo w up the vertices of G using a suitable
gadget. For a similar discussion, see also [GL, Section 4].
Deﬁnition 6.1. Fix a red-blue arc-graph GK. Let G(n)
K denote the digraph with vertices av
j for v a vertex of
GK and j = 1, . . . , n. G(n)
K contains blue directed edges ( al
j, al+1
j ) with weight t−ǫn (where ǫ∈{− 1, +1} is the
sign of the crossing l) for each l = 1, . . . , r− 1 and j = 1, . . . , n. Moreover, if ( ak, al) is a red directed edge of
GK, then G(n)
K contains red edges ( ak
i , al
j) for all i, j = 1, . . . n with weight t(j−1)(1− t) resp. t−(n−j)(1− t−1),
if the sign of the i crossing is−1 resp. +1. Notice that the weights of the red edges are independe nt of the
index i.
Lemma 6.2. There is a 1-1 correspondence
{admissible subgraphs of GK (n)}←→{ admissible subgraphs of G(n)
K }.
We will denote the set of admissible even subgraphs of G(n)
K bySn(GK ).
Proof. Denote by pk
j path ( ak
1j , ak
2j, . . . , ak
nj) of n− 1 blue edges in GK (n) , k = 1 , . . . , r and j = 1 , . . . , n.
There is a natural map GK (n)−→ G(n)
K which contracts each directed path pk
j into its initial vertex, and
deletes all vertices ar+1
ij . Forgetting the weights, it is clear that the result of the contract ion coincides with
G(n)
K .
GK (n) has two types of vertices: ak
ij for k = 1 , . . . , r + 1 and i, j = 1 , . . . , n and i⁄= 1 (call these white)
and ak
1j, k < r + 1 (call these black). The indegree of a white vertex is 1, but the ind egree of a black vertex
may be higher. The black vertices are the initial vertices of the path s pk
j , hence the vertices of G(n)
K . Let
E{n} and E(n) denote the set of edges of GK (n) and G(n)
K respectively. Then each edge e of E(n) replaces the
unique directed path Pe of GK (n) between the corresponding black end-vertices of e, which contains no other
black vertices. If E⊂ E{n} is an admissible even subgraph of GK (n) then E is a vertex-disjoint union of
directed cycles of GK (n) and each directed cycle may be decomposed into directed paths bet ween the black
vertices. If each such directed path is replaced by a directed edge , we get an admissible even subgraph E′
of G(n)
K . This gives the 1-1 correspondence between the admissible even su bgraphs without the weights. To
realize that the weights are correct as well, we only need to compare the product of the weights in GK (n)
along Pe with the weights of e in G(n)
K . □
Theorem 6 and Lemmas B.2, 6.2 imply that:
Lemma 6.3. For every knot K and every n∈ N, we have
Jn(K, t) = tnδ(K) ∑
c∈Sn(GK )
tδ(c)β(c).
Our next task is to ﬁgure out δ(c) = exc( c)− rot(c) for c∈S n(GK ).
The following lemma is clear from the Deﬁnition 4.1:
10
Lemma 6.4. If f is a ﬂow on GK and ~f is a lift of f to ﬂow on G(n)
K , for some n, then rot(f ) = rot(~f ).
