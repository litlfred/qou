---
doc_id: arxiv-q-alg-9504015v2
doc_title: "Witten’s Invariants of Rational Homology Spheres at Prime"
section_id: sec-013-3-gaussian-sums-and-integrals
section_title: "Gaussian Sums and Integrals"
section_number: 3
pages: 14-15
source_pdf: 9504015v2.pdf
source_sha256: ea5588225a393477
doc_brief: "Witten’s Invariants of Rational Homology Spheres at Prime — We establish a relation between the coeﬃcients of asymptotic expan sion of the trivial connection contribution to Witten’s invariant of"
---
We are going to derive a surgery formula for [ Z ′(M; k)]⋄ which would express it in terms
of the derivatives ˜Dm,n of the colored Jones polynomial. As we will see, this requires a
calculation of the gaussian sum
G(p, q; m) = ei π
4 (κ−1)
√
K
∑ ′
−K≤α ≤K
α ∈2Z Z+1
ˇqq∗pα2
α2mxm, m ≤ K − 1
2 . (3.1)
More precisely, we need to ﬁnd only [ G(p, q; m)]⋄. We already know that G(p, q; m) ∈ Z Z[ˇq].
Proposition 3.1 The sum of eq. (3.1) is related to the gaussian integral. For p, q ∈ Z Z,
p, q ⁄= 0 (mod K), 0 ≤ m ≤ K−1
2 ,
[G(p, q; m)]⋄ =
( pq∗
K
) 
e−i π
4 sign(
p
q )
( 2
K
) 1
2
⏐
⏐
⏐
⏐
⏐
p
q
⏐
⏐
⏐
⏐
⏐
1
2∫ +∞
−∞
dα e
2πi
K
p
q α2
α2m xm


∨
(3.2)
+x
K+1
2 −mw, w ∈ Z Z[ˇq].
To prove the proposition we calculate the following sum:
ei π
4 (κ−1)
√
K
∑ ′
−K≤α ≤K
α ∈2Z Z+1
ˇqpq∗α2
ˇq2nα = ei π
4 (κ−1)
√
K ˇq−p∗qn2 ∑ ′
−K≤α ≤K
α ∈2Z Z+1
ˇqpq∗(α+np∗q)2
. (3.3)
13
Since (for p∗ ∈ Z Z)
∑ ′
−K≤α ≤K
α ∈2Z Z+1
ˇqpq∗(α+np∗q)2
=
∑ ′
−K≤α ≤K
α ∈2Z Z+1
ˇqpq∗α2
=
∑
3−K
2 < ˜α≤ K−1
2
ˇqpq∗(2 ˜α+1)2
=
∑
3−K
2 < ˜α≤ K−1
2
ˇq4pq∗( ˜α+2∗)2
=
√
Ke i π
