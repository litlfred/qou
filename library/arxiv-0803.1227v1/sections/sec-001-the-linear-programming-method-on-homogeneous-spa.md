---
doc_id: arxiv-0803.1227v1
doc_title: "Linear programming bounds for unitary space time codes"
section_id: sec-001-the-linear-programming-method-on-homogeneous-spa
section_title: "The linear programming method on homogeneous spaces"
section_number: null
pages: 2-3
source_pdf: 0803.1227v1.pdf
source_sha256: cf72e0fcdc7f3ddf
doc_brief: "Linear programming bounds for unitary space time codes — The linear programming method is applied to the space Un(C) of uni- tary matrices in order to obtain bounds for codes relative to the"
---
For more details we refer to [9], [14, Chapter 9] for a treatment of 2 -point
homogeneous spaces, and to [1] for the prominent case of Grassm ann codes.
Let G be a compact group acting transitively and continuously on a compac t
space X, and τ : X × X → Y such that τ characterizes the orbits of G acting
on X × X. We mean here that, for all x1, x 2, x ′
1, x ′
2 ∈ X,
τ(x1, x 2) = τ(x′
1, x ′
2) ⇔ ∃g ∈ G : g(x1, x 2) = ( x′
1, x ′
2).
Let S be any subset of Y , we call a ﬁnite subset V ⊂ X a S-code if for all
c1 ⁄= c2 ∈ V , τ (c1, c 2) ∈ S.
A continuous function P : Y → C is said to possess the positivity property
if for any ﬁnite subset V ⊂ X and any complex function α : X → C,
∑
x,y ∈V
α (x)α (y)P (τ(x, y )) is real non-negative.
A canonical example is the constant function P0 = 1; non-trivial examples are
given by the so called zonal functions that we introduce now.
Let L2(X) =
{
u : X → C :∫
X |u(x)|2dx < ∞
}
where dx is the unique G-
invariant Haar measure on X such that
∫
X dx = 1. This vector space is given
the standard G-action deﬁned by g.u (x) = u(g−1(x)) and is endowed with the
canonical G-invariant hermitian product : ( u1, u 2) =
∫
X u1(x)u2(x)dx. The
Peter-Weil theorem shows that L2(X) can be decomposed as a direct sum of
G-irreducible subspaces Vi. The next step is to associate to each irreducible
subspace Vi a so-called zonal function PVi . A standard construction is the
2
following: given an orthonormal basis ( u1(x), ..., u d(x)) of Vi, one can deﬁne
˜PVi (x, y ) = 1
d i
di∑
i=1
ui(x)ui(y). (1)
where di = dim( Vi). Since these functions are constant on G-orbits we can
rewrite ˜PVi (x, y ) = PVi (τ(x, y )). From this property comes the term zonal
functions used to qualify them. From equation (1) it is easy to prove that thes e
zonal functions verify the positivity property and do not depend o f the chosen
orthonormal basis. It turns out that, when the irreducible subsp aces Vi are
pairwise non isomorphic, the cone of continuous positive G-invariant functions
is exactly the set of linear combinations with non negative coeﬃcients of the
PVi (see [5]). In the remaining of this paper we assume that this condition is
satisﬁed. We moreover let V0 denote the one-dimensional subspace associated
to the trivial representation of G.
The so-called linear programming bounds are obtained with the followin g
theorem :
Theorem 2.1 Let P = ∑
i ciPVi a linear combination of the zonal functions
PVi with a ﬁnite number of non zero coeﬃcients. Assume furthermo re that :
ci ≥ 0, c0 > 0 and ℜ(P ) (the real part of P ) is non-positive on S. Then any
S-code veriﬁes
|V| ≤ P (τ0)
c0
(2)
where τ0 = τ(x, x ) for any x.
Proof : On one hand,
∑
x,y ∈V
P (τ(x, y )) =
∑
x=y∈V
P (τ(x, y )) +
∑
x⁄=y∈V
P (τ(x, y ))
≤ |V| P (τ0)
On the other hand,
∑
x,y ∈V
P (τ(x, y )) =
∑
x,y ∈V
c0P0(τ(x, y )) + non negative terms
≥ |V| 2c0.
