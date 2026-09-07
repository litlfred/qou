---
doc_id: arxiv-2208.13448v2
doc_title: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS"
section_id: sec-009-4-galois-groups-of-equations-of-order-one-and-di
section_title: "Galois groups of equations of order one and diagonal systems"
section_number: 4
pages: 20-21
source_pdf: 2208.13448v2.pdf
source_sha256: 8bfa244cf7ca867d
doc_brief: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS — In this paper we consider the problem of computing the diﬀere nce Galois groups of order three equations for a large"
---
4.1. Galois groups of equations of order one. We consider the equation of order one
(4.1) φ(y) = αy α ∈ k∗.
Let us now see how to compute the Galois group G of this diﬀerence equation. Recall
that since G ⊂ GL1(C) is an algebraic group, either G is C ∗, or it is isomorphic to Z/ℓZ
for some ℓ ∈ N∗.
Proposition 4.1. We have G ∼ Z/ℓZ if and only if there exists ζ, a primitive ℓth root of
unity and a nonzero solution f ∈ k∗ of φ(y) = ( ζ/α)y. In that situation, ζ = α φ(f )
f , and
[ζ] is a reduced form of [α] with a gauge transformation (f ).
Proof. Since the Galois group G of ( 4.1) is an algebraic subgroup of C ⋆, it is a ﬁnite cyclic
group or the multiplicative group C ⋆. Any equivalent equation of ( 4.1) is of the form
φ(y) = α φ(f )
f y with f ∈ k⋆. Therefore, from Theorem 2.1, if G is a ﬁnite cyclic group
of order ℓ ∈ N∗ then there exist f ∈ k⋆ and ζ, a primitive ℓth root of unity, such that
ζ = α φ(f )
f .
ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER T HREE EQ. 21
Conversely, assume that there exist f ∈ k⋆ and ζ, a primitive ℓth root of unity, such
that ζ = α φ(f )
f . From Theorem 2.1, G is contained in Z/ℓZ. Then, G ∼ Z/ℓ1Z where
ℓ1 divides ℓ. Then, there exist g ∈ k⋆ and ζ1, a primitive ℓ1th root of unity, such that
ζ1 = α φ(g)
g . This implies αℓ1 = gℓ1/φ(gℓ1 ). Let h := ( f /g)ℓ. Thus, φ(h) = h so h ∈ C ∗.
Since C is algebraically closed, there exists c ∈ C ∗ such that f = cg (with cℓ = h). Using
this equality, we obtain ζ = ζ1 and since ζ is a primitive ℓth root of unity, ℓ = ℓ1. □
Remark 4.2. Since det(G) is the Galois group of φ(y) = det( A)y, an equation of order 1,
we may now compute det(G) if we are able to reduce the diﬀerence equations of order 1.
Example 4.3. Consider the diﬀerence equation (1.1) and let G be its diﬀerence Galois group
over C(z1/∗). Assume that t ⁄= 0 . We want to compute det(G). We have to compute
the diﬀerence Galois group of φ(y) = −q3z
t y = αy over C(z1/∗). By Proposition 4.1,
det(G) is ﬁnite if and only if there exists ζ, a primitive ℓth root of unity, and a nonzero
solution f ∈ k∗ of φ(y) = ( ζ/α)y. But the valuation of α at z = 0 is 1, proving that
ζ/α must have valuation −1. Since for f ∈ k∗, f and φ(f ) have the same valuation, the
equation φ(f ) = ( ζ/α)f with f ∈ k∗, and ζ a root of unity, has no solutions. Therefore,
det(G) = C∗.
