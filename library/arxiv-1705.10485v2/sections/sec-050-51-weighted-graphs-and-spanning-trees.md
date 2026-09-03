---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-050-51-weighted-graphs-and-spanning-trees
section_title: "Weighted graphs and spanning trees"
section_number: 5.1
pages: 40-41
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
An edge-weighted graphG, orweighted graphfor short, is a graphG in which each edgee is assigned a
weightwG(e). Here we restrict ourselves to weightswG(e) withwG(e)∈ R+. Edges not in the graph can
be thought of as edges of weight0, all our deﬁnitions being consistent with this convention.
If B is a multiset of vertices ofG, we can consider the graphG[B] induced byG on B and deﬁned as
follows: the vertices ofG[B] correspond to elements ofB (if B contains an element with multiplicitym,
thenmvertices correspond to this element), and there is an edge between two vertices if the corresponding
vertices of G are equal or connected by an edge inG. This new graph has a natural weighted graph
structure: put on each edge ofG[B] the weight of the corresponding edge inG (if the edge connects two
copies of the same vertex ofG, we put weight1).
Deﬁnition 42.A spanning tree of a graphG = (V,E ) is a subsetE′ of E such that(V,E′) is a tree. In
other words, it is a subgraph ofG that is a tree and covers all vertices.
The set of spanning trees ofT is denoted ST(G). IfG is a weighted graph, we say that the weightw(T )
of a spanning tree ofG is deﬁned as theproductof the weights of the edges inT.
1
w12
2
w23
w13 3 w34
4
w45
5
6
w67
7
G
G[B]
1
w12
2
w23
w13 3
4
4
w34
w34
1
T
1
2
3
4
4
Fig. 10 A weighted dependency graphG for 7 random variables; the induced graphG[B] with B ={1, 2, 3, 4, 4}; and a
spanning treeT of G[B], withw(T ) = w12w23w34.
Mod-φ convergence, II: Estimates on the speed of convergence 41
