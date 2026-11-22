---
doc_id: s0002-9947-96-01660-1
doc_title: "AMERICAN MATHEMATICAL SOCIETY INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS"
section_id: page-003
section_title: "Page 3"
section_number: null
pages: 3-3
source_pdf: S0002-9947-96-01660-1.pdf
source_sha256: aa63e62b78aa5045
toc_source: undetermined
doc_brief: "Invariants of piecewise-linear 3-manifolds — This paper presents an algebraic framework for constructing in- variants of closed oriented 3-manifolds by taking a state sum model on a tri- angulation."
---
INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS
3999
Our notation for the orientation of a simplex is ﬁxed as follows. The standard
(n + 1)-simplex (012 . . .n) with vertices {0, 1, 2, . . .n} has a standard orientation
(+). The opposite orientation is indicated with a minus (−). The standard (ori-
ented) tetrahedron +(0123) has boundary
(123) −(023) + (013) −(012).
The signs indicate the induced orientation of the boundary of +(0123). The tetra-
hedron −(0123) has the opposite orientation for the boundary,
−(123) + (023) −(013) + (012).
In an oriented closed manifold, each triangle is in the boundary of exactly two
tetrahedra, with each sign + or −occuring once.
The data for a state sum model consists of three parts, a set of labels I, a set of
state spaces for a triangle, and a set of partition functions for a tetrahedron.
Deﬁnition 1.3. A labelled simplicial complex is a simplicial complex together with
a function which assigns an element of I to each edge.
Deﬁnition 1.4. Let T(a, b, c) be the standard oriented triangle +(012) labelled by
∂0T 7→a, ∂1T 7→b, ∂2T 7→c. The state space for this labelled triangle is a vector
space, H(a, b, c). The state space for the oppositely oriented triangle −T(a, b, c) is
deﬁned to be the dual vector space, H∗(a, b, c).
Deﬁnition 1.5. Let A be the standard oriented tetrahedron +(0123) with the edge
∂i∂jσ labelled by eij. The partition function of this labelled tetrahedron is deﬁned
to be a linear map

e01
e02
e12
e23
e13
e03

+
:
H(e23, e03, e02) ⊗H(e12, e02, e01) →H(e23, e13, e12) ⊗H(e13, e03, e01).
The partition function of −A with the same labelling is deﬁned to be a linear
map
e01
e02
e12
e23
e13
e03

−
:
H(e23, e13, e12) ⊗H(e13, e03, e01) →H(e23, e03, e02) ⊗H(e12, e02, e01).
In the deﬁnition, the four factors in the tensor products correspond to each of
the four faces. Also, the two factors in the domain of the linear map correspond to
the two faces with sign −in the boundary of the tetrahedron, and the two factors
in the range correspond to the two faces with sign +.
Deﬁnition 1.6. The data for a state sum model determines an element Z(M) ∈F
for each labelled simplicial closed manifold M. This is called the simplicial invariant
of the labelled manifold. Let V (M) be the tensor product over the set of triangles
of M of the state space for each triangle. For each tetrahedron in M, take the
partition function of the labelled standard tetrahedron, A or −A, to which it is
isomorphic.
The tensor product over this set of partition functions is a linear map V (M) →
V π(M), where V π(M) is deﬁned in the same way as V (M) but with the factors
permuted by some permutation π.
This uses the fact that in a closed oriented
manifold, each triangle is in the boundary of two tetrahedra, each with opposite
