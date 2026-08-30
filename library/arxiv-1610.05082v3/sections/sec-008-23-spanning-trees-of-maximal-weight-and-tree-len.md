---
doc_id: arxiv-1610.05082v3
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-008-23-spanning-trees-of-maximal-weight-and-tree-len
section_title: "Spanning trees of maximal weight and tree lengths"
section_number: 2.3
pages: 6-7
source_pdf: 1610.05082v3.pdf
source_sha256: 90c8089953ff2d97
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
Deﬁnition 2.1. A spanning tree of a graph L = (V,E ) is a subset E′ of E such that (V,E′) is a tree.
IfG is an edge-weighted graph, we deﬁne the weight w(T ) of a spanning tree of G as the product of
the weights of the edges in T . The maximum weight of a spanning tree of G is denotedM
(
G
)
.
We will be mainly interested in the case where V is a ﬁnite subset A of Zd,E consists of all pairs of
vertices and the weights are of the form w(i,j ) =ε‖i−j‖1 for some positive constant ε< 1. We denote
this weighted graph by GA. Then, for a spanning tree T of GA,
w(T ) =ε
∑
(i,j)∈T‖i−j‖1,
and the maximal such weight M
(
GA
)
is obtained by minimizing the quantity ∑
(i,j)∈T‖i− j‖1.
Therefore we deﬁne
𝓁′
T (A) = min
T
∑
(i,j)∈T
‖i−j‖1,
where the minimum is taken over all spanning trees T of GA, i.e. of the complete graph on A. Then
we haveM
(
GA
)
=ε𝓁′
T (A).
The quantity𝓁′
T (A) is sometimes referred to as the tree-length ofA. There is another closely related
notion of tree-length deﬁned as 𝓁T (A) = minB 𝓁′
T (A∪B), where the minimum is taken over all ﬁnite
subsets B of Zd. In other words, this is the minimum length of a tree connecting vertices of A and
possibly other vertices of Zd. Equivalently, this is the minimal size of a connected set of edges of the
lattice Zd such that each vertex of A is incident to at least one edge in the set. These two notions of
tree-length are illustrated on Fig. 1.
In [4, page 197], Duneau, Iagolnitzer and Souillard proved the following bound, which will be useful
later in our computations.
