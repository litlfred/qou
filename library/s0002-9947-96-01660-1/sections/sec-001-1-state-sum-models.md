---
doc_id: s0002-9947-96-01660-1
doc_title: "AMERICAN MATHEMATICAL SOCIETY INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS"
section_id: sec-001-1-state-sum-models
section_title: "State sum models"
section_number: 1
pages: 2-4
source_pdf: S0002-9947-96-01660-1.pdf
source_sha256: aa63e62b78aa5045
doc_brief: "AMERICAN MATHEMATICAL SOCIETY INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS — This paper presents an algebraic framework for constructing in- variants of closed oriented 3-manifolds by taking a state"
---
In this paper we have assumed thatF is a ﬁeld and that a vector space is a ﬁnite
dimensional vector space overF.
Deﬁnition 1.1. A complex is a ﬁnite set of elements called vertices, together with
a subset of the set of all subsets. These are called simplices. This is required to
have the property that any subset of a simplex is a simplex.
Deﬁnition 1.2. A simplicial complex is a complex together with a total ordering
on the vertices of each simplex such that the ordering on the vertices on any face of
a simplex is the ordering induced from the ordering on the vertices of the simplex.
Letσ be an n-simplex in a simplicial complex. Then for 0 ⩽i⩽n deﬁne∂iσ to
be the face obtained by omitting the i-th vertex. These satisfy
∂i∂jσ =∂j−1∂iσ if i<j.
A simplicial complex is an example of the more general notion of simplicial
set. This explains the use of the adjective ‘simplicial’ for the notion of a complex
with an ordering. In the following, the adjective ‘combinatorial’ will be used to
refer to complexes, reserving ‘simplicial’ for simplicial complexes. Combinatorial
maps are maps of complexes and simplicial maps are maps of simplicial complexes,
i.e., combinatorial maps which preserve orderings. For example, a single simplex
considered as a simplicial complex has no symmetries, whereas the corresponding
complex admits the permutations as its symmetries.
All manifolds are compact, oriented, piecewise-linear manifolds of dimension
three, unless stated otherwise. For background on piecewise-linear manifolds we
refer the reader to [21]. In line with the terminology explained above, a simplicial
manifold is a simplicial complex whose geometric realisation is a piecewise-linear
manifold, together with an orientation.
INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS 3999
Our notation for the orientation of a simplex is ﬁxed as follows. The standard
(n + 1)-simplex (012...n ) with vertices {0, 1, 2,...n } has a standard orientation
(+). The opposite orientation is indicated with a minus ( −). The standard (ori-
ented) tetrahedron +(0123) has boundary
(123)− (023) + (013)− (012).
The signs indicate the induced orientation of the boundary of +(0123). The tetra-
hedron−(0123) has the opposite orientation for the boundary,
−(123) + (023)− (013) + (012).
In an oriented closed manifold, each triangle is in the boundary of exactly two
tetrahedra, with each sign + or − occuring once.
The data for a state sum model consists of three parts, a set of labels I,as e to f
state spaces for a triangle, and a set of partition functions for a tetrahedron.
Deﬁnition 1.3. A labelled simplicial complex is a simplicial complex together with
a function which assigns an element of I to each edge.
Deﬁnition 1.4. LetT (a,b,c ) be the standard oriented triangle +(012) labelled by
∂0T↦→ a,∂ 1T↦→ b,∂ 2T↦→ c. The state space for this labelled triangle is a vector
space, H(a,b,c ). The state space for the oppositely oriented triangle −T (a,b,c )i s
deﬁned to be the dual vector space, H∗(a,b,c ).
Deﬁnition 1.5. LetA be the standard oriented tetrahedron +(0123) with the edge
∂i∂jσ labelled by eij. The partition function of this labelled tetrahedron is deﬁned
to be a linear map
{
e01 e02 e12
e23 e13 e03
}
+
:
H(e23,e 03,e 02)⊗H(e12,e 02,e 01)→H(e23,e 13,e 12)⊗H(e13,e 03,e 01).
The partition function of −A with the same labelling is deﬁned to be a linear
map
{e01 e02 e12
e23 e13 e03
}
−
:
H(e23,e 13,e 12)⊗H(e13,e 03,e 01)→H(e23,e 03,e 02)⊗H(e12,e 02,e 01).
In the deﬁnition, the four factors in the tensor products correspond to each of
the four faces. Also, the two factors in the domain of the linear map correspond to
the two faces with sign− in the boundary of the tetrahedron, and the two factors
in the range correspond to the two faces with sign +.
Deﬁnition 1.6. The data for a state sum model determines an elementZ(M)∈F
for each labelled simplicial closed manifoldM. This is called the simplicial invariant
of the labelled manifold. Let V (M) be the tensor product over the set of triangles
of M of the state space for each triangle. For each tetrahedron in M,t a k et h e
partition function of the labelled standard tetrahedron, A or−A, to which it is
isomorphic.
The tensor product over this set of partition functions is a linear map V (M)→
Vπ(M), where Vπ(M) is deﬁned in the same way as V (M) but with the factors
permuted by some permutation π. This uses the fact that in a closed oriented
manifold, each triangle is in the boundary of two tetrahedra, each with opposite
4000 JOHN W. BARRETT AND BRUCE W. WESTBURY
orientation. There is a unique standard linear map Vπ(M)→ V (M)g i v e nb y
iterating the standard twist P : x⊗y↦→y⊗x. This deﬁnes a linear map V (M)→
V (M), and the element Z(M) is deﬁned to be the trace of this linear map.
Note that if A: X→Y andB : Y →X are linear maps, then
trX⊗Y (P(A⊗B)) = trX (AB)=t rY (BA).
This also introduces the notation, used throughout the paper, that the map X
composed with map Y is written XY (not Y◦X).
A state sum invariant of a closed manifold is obtained by a weighted sum of
these elements Z(M) over a class of labellings. This state sum invariant is deﬁned
in section 5.
