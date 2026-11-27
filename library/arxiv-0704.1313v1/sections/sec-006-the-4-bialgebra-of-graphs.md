---
doc_id: arxiv-0704.1313v1
doc_title: "Mutant knots and intersection graphs"
section_id: sec-006-the-4-bialgebra-of-graphs
section_title: "The 4-bialgebra of graphs"
section_number: null
pages: 8-9
source_pdf: 0704.1313v1.pdf
source_sha256: a75bb39c60ec9b15
toc_source: outline
doc_brief: "Mutant knots and intersection graphs — We prove that if a ﬁnite order knot invariant does not disting uish mutant knots, then the corresponding weight system depends on the interse ction graph of a"
---
By a graph, we mean a ﬁnite undirected graph without loops and multip le edges.
Let Gn denote the vector space freely spanned over C by all graphs with n vertices,
G0 = C being spanned by the empty graph. The direct sum
G = G0 ⊕ G1 ⊕ G2 ⊕ . . .
carries a natural structure of a commutative cocommutative gra ded Hopf algebra.
The multiplication in this Hopf algebra is induced by the disjoint union of g raphs,
and the comultiplication is induced by the operation taking a graph G into the sum
8
∑ GU ⊗ G ¯U , where U is an arbitrary subset of vertices of G, ¯U its complement, and
GU denotes the subgraph of G induced by U.
The 4 -term relation for graphs is deﬁned in the following way. By deﬁnition, the
4-term element in Gn determined by a graph G with n vertices and an ordered pair
A, B of its vertices connected by an edge is the linear combination
G − G′
AB − ~GAB + ~G′
AB,
where
• G′
AB is the graph obtained by deleting the edge AB in G;
• ~GAB is the graph obtained by switching the adjacency to A of all the vertices
adjacent to B in G;
• ~G′
AB is the graph obtained by deleting the edge AB in G′
AB (or, equivalently,
by switching the adjacency to A of all the vertices adjacent to B in G′
AB).
All the four terms in a 4-term element have the same number n of vertices. The
quotient of Gn modulo the span of all 4-term elements in Gn (deﬁned by all graphs
and all ordered pairs of adjacent vertices in each graph) is denote d by Fn. The direct
sum
F = F0 ⊕ F1 ⊕ F2 ⊕ . . .
is the quotient Hopf algebra of graphs, called the 4 -bialgebra. The mapping taking a
chord diagram to its intersection graph extends to a graded Hopf a lgebra homomor-
phism γ from the Hopf algebra of chord diagrams to F .
Being commutative and cocommutative, the 4-bialgebra is isomorphic to the
polynomial ring in its basic primitive elements, that is, it is the tensor pr oduct
S(P1) ⊗ S(P2) ⊗ . . . of the symmetric algebras of its homogeneous primitive spaces.
