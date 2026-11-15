---
doc_id: s0002-9947-96-01660-1
doc_title: "AMERICAN MATHEMATICAL SOCIETY INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS"
section_id: page-004
section_title: "Page 4"
section_number: null
pages: 4-4
source_pdf: S0002-9947-96-01660-1.pdf
source_sha256: aa63e62b78aa5045
toc_source: undetermined
doc_brief: "Invariants of piecewise-linear 3-manifolds — This paper presents an algebraic framework for constructing in- variants of closed oriented 3-manifolds by taking a state sum model on a tri- angulation."
---
4000
JOHN W. BARRETT AND BRUCE W. WESTBURY
orientation.
There is a unique standard linear map V π(M) →V (M) given by
iterating the standard twist P : x ⊗y 7→y ⊗x. This deﬁnes a linear map V (M) →
V (M), and the element Z(M) is deﬁned to be the trace of this linear map.
Note that if A: X →Y and B : Y →X are linear maps, then
trX⊗Y (P(A ⊗B)) = trX(AB) = trY (BA).
This also introduces the notation, used throughout the paper, that the map X
composed with map Y is written XY (not Y ◦X).
A state sum invariant of a closed manifold is obtained by a weighted sum of
these elements Z(M) over a class of labellings. This state sum invariant is deﬁned
in section 5.
2. Spherical categories
The data which deﬁnes the state sum model is a spherical category, whose deﬁ-
nition is obtained by axiomatising the properties of the category of representations
of the spherical Hopf algebra. The reason this abstraction is necessary is that the
category of representations of a Hopf algebra may be degenerate, and it is necessary
to take a non-degenerate quotient category to construct the invariants.
This quotient is not the category of representations of any ﬁnite dimensional Hopf
algebra. The reason for this is that it is not possible to assign a positive integer,
the dimension, to each object which is additive under direct sum and multiplicative
under the tensor product.
First we recall the deﬁnition of a strict pivotal category given in [6]. The def-
inition of a (relaxed) pivotal category is given in [3] and a similar deﬁnition is
given in [7]. A spherical category is a pivotal category which satisﬁes an additional
condition.
In this paper we will only consider strict pivotal categories. There is no loss of
generality, as it is shown in [3] that every pivotal category is canonically equivalent
to a strict pivotal category. However the main examples of pivotal categories are
categories of representations of Hopf algebras and are not strict. The diﬀerence
between a pivotal category and a strict pivotal category is that some objects that are
equal in a strict pivotal category are canonically isomorphic in a pivotal category. In
this section we denote any such canonical isomorphism by =. These constructions
can be extended to pivotal categories by putting in the canonical isomorphism for
each =.
Deﬁnition 2.1. A category with strict duals consists of a category C, a functor
⊗: C × C →C, an object e and a functor b : C →Cop. The conditions are that
(C, ⊗, e) is a strict monoidal category and
1. The functors b b and 1 are equal.
2. The objects ˆe and e are equal.
3. The functors C × C →C which on objects are given by (a, b) 7→(a ⊗b)b
and
(a, b) 7→ˆb ⊗ˆa are equal.
Deﬁnition 2.2. A strict pivotal category is a category with strict duals together
with a morphism ϵ(c): e →c ⊗ˆc for each object c ∈C.
The conditions on the morphisms ϵ(c) are the following:
