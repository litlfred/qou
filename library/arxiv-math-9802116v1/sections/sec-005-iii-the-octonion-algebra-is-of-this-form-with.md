---
doc_id: arxiv-math-9802116v1
doc_title: "arXiv:math/9802116v1 [math.QA] 25 Feb 1998"
section_id: sec-005-iii-the-octonion-algebra-is-of-this-form-with
section_title: "The octonion algebra is of this form with"
section_number: iii
pages: 19-20
source_pdf: 9802116v1.pdf
source_sha256: be7999751ffb6db3
toc_source: inferred
doc_brief: "Quasialgebra structure of the octonions — We show that the octonions are a twisting of the group algebra of Z2 × Z2 × Z2 in the quasitensor category of representations of a quasi-Hopf algebra asso"
---
¯¯G = Z2 × Z2 × Z2,
¯¯f(⃗x,⃗y) =
X
i≤j
xiyj + y1x2x3 + x1y2x3 + x2x2y3.
iv) The 16-onion algebra is of the form ¯¯¯G = Z2 × Z2 × Z2 × Z2 and
¯¯¯f(⃗x,⃗y) =
X
i≤j
xiyj +
X
i̸=j̸=k̸=i
xixjyk +
X
distinct i,j,k,l
xixjykyl +
X
i̸=j̸=k̸=i
xiyjykx4
We are now able to apply our various criteria in the last section for the structure of the
algebras of the form kF G, to this construction and to all these algebras. Note in all these cases
(and for the who 2n-onion family generated in this way) f has a bilinear part deﬁned by the
bilinear form







1
1
· · ·
1
0
1
· · ·
1
...
...
0
· · ·
1
1
0
· · ·
0
1







.
For the complex number and quaternion algebras this is the only part, which implies that F
is a bicharacter and hence, in particular, its group coboundary φ = 1, i.e. these algebras are
associativity. The f for the octonions has this bilinear part, which does not change associativity,
plus a cubic term which contributes to φ. The 16-onion has additional cubic an quartic terms,
etc. This makes the origin of the breakdown of associativity for the higher members of the
family particularly clear.
In the remainder of this section we suppose that the quasialgebra kF G is admits a diagonal
involution σ(x) = s(x)x in the basis G and we shall denote by k ¯F ¯G the generalized Cayley-
Dickson extension with respect to this (with general α̸ = 0). It is easy to see that ¯s provides a
diagonal involution on it.
Proposition 4.5 The associativity cocycle φ of kF G and the associativity cocycle ¯φ of k ¯F ¯G are
related by
¯φ(x, y, z) = φ(x, y, z),
¯φ(vx, y, z) = R(y, z)φ(x, y, z)
¯φ(x, vy, z) = R(y, z)R(xy, z)φ(x, y, z),
¯φ(x, y, vz) = R(x, y)φ(x, y, z)
¯φ(vx, vy, z) = R(xy, z)φ(x, y, z),
¯φ(vx, y, vz) = R(y, z)R(x, y)φ(x, y, z)
¯φ(x, vy, vz) = R(x, yz)φ(x, y, z),
¯φ(vx, vy, vz) = R(xy, z)R(x, y)φ(x, y, z)
∀x, y, z ∈G.
Proof
We use the deﬁnition of ¯φ as coboundary of ¯F, the form of this in Proposition 4.1 and
F(x, y) = R(x, y)F(y, x) from Deﬁnition 3.2. We also use Lemma 3.4 which tells us that s2 = 1,
R(x, y) = s(x)s(y)/s(x, y) and φ(x, y, z)φ(z, y, x) = 1. ⊔⊓
Corollary 4.6 k ¯F ¯G is associative if and only if kF G is associative and commutative.
Proof
We already know that kF G is commutative iﬀF is symmetric, which means iﬀR = 1.
So in this case if φ = 1 then ¯φ = 1.
So if kF G is associative and commutative, k ¯F ¯G is
associative. Conversely, if ¯φ = 1 then by restriction, φ = 1 so kF G is associative. Moreover,
1 = ¯φ(x, y, v) = R(x, y)φ(x, y, e) = R(x, y) tells us that kF G is commutative.
⊔⊓
