---
doc_id: arxiv-q-alg-9504015v2
doc_title: "Witten's invariants of rational homology spheres at prime values of K and trivial connection contribution"
section_id: sec-013-front-matter-page-14
section_title: "Front matter (page 14)"
section_number: null
pages: 14-14
source_pdf: 9504015v2.pdf
source_sha256: ea5588225a393477
toc_source: inferred
doc_brief: "Witten's invariants of rational homology spheres at prime values of K and trivial connection contribution — We establish a relation between the coeﬃcients of asymptotic expansion of the trivial"
---
Since ¯m(n) ≤3
4n ≤n, this estimate is enough to prove eq. (2.22) and also the Theorem 1.1.
Note that the proof required only a weaker bound m ≤n for ˜Dm,n rather than a stronger
bound m ≤3
4n of [18]. However the bound m ≤3
4n is necessary to prove that only a ﬁnite
number of polynomials ˜Dm,n contribute to the coeﬃcients of xn′, n′ ≤K−1
2
in the expansion
of [Z′(M; k)]⋄. Indeed, since ¯m(n) ≤3
4n, then n −¯m(n) ≥1
4n and eq. (2.30) suggests that
we may limit our attention to only those polynomials (2.15) for which
n ≤2(K −1).
(2.31)
3
Gaussian Sums and Integrals
We are going to derive a surgery formula for [Z′(M; k)]⋄which would express it in terms
of the derivatives ˜Dm,n of the colored Jones polynomial.
As we will see, this requires a
calculation of the gaussian sum
G(p, q; m) = ei π
4 (κ−1)
√
K
X′
−K≤α≤K
α∈2ZZ+1
ˇqq∗pα2α2mxm,
m ≤K −1
2
.
(3.1)
More precisely, we need to ﬁnd only [G(p, q; m)]⋄. We already know that G(p, q; m) ∈ZZ[ˇq].
Proposition 3.1 The sum of eq. (3.1) is related to the gaussian integral. For p, q ∈ZZ,
p, q̸ = 0 (mod K), 0 ≤m ≤K−1
2 ,
[G(p, q; m)]⋄=
pq∗
K
 
e−i π
4 sign(
p
q)
 2
K
 1
2

p
q

1
2 Z +∞
−∞dα e
2πi
K
p
q α2α2m xm


∨
(3.2)
+x
K+1
2
−mw, w ∈ZZ[ˇq].
To prove the proposition we calculate the following sum:
ei π
4 (κ−1)
√
K
X′
−K≤α≤K
α∈2ZZ+1
ˇqpq∗α2 ˇq2nα = ei π
4 (κ−1)
√
K
ˇq−p∗qn2
X′
−K≤α≤K
α∈2ZZ+1
ˇqpq∗(α+np∗q)2.
(3.3)
