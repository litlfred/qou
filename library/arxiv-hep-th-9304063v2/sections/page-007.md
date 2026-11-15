---
doc_id: arxiv-hep-th-9304063v2
doc_title: "arXiv:hep-th/9304063v2 29 Jan 1999"
section_id: page-007
section_title: "Page 7"
section_number: null
pages: 7-7
source_pdf: 9304063v2.pdf
source_sha256: 14a82437462eae23
toc_source: undetermined
doc_brief: "arXiv:hep-th/9304063v2 29 Jan 1999 — 18 sections: Page 1; Page 2; Page 3"
---
where now the inner products are taken over (0, ∞). Notice that since
(I −K)−1ξ = (I −K)−1ξχJ
in J
for any function ξ, this agrees with the original deﬁnitions (1.8) of u and v.
We have, by (2.2),
((MD)x + (MD)y)K(x, y) = 1
4
Z 1
0
t ∂
∂t (φ(xt)φ(yt)) dt = 1
4φ(x)φ(y) −K(x, y).
But it is easy to see that
[MD, L] .= ((MD)x + (MD)y + I) L(x, y)
(2.6)
for any operator L with kernel L(x, y), where “ .=” means “has kernel”. Taking L(x, y) = K(x, y) χJ(y) gives
[MD, K] .= 1
4 φ(x) φ(y) χJ(y) −
X
(−1)kakK(x, ak) δ(y −ak).
(Recall the form (1.4) of J.) It follows from this and (2.3) that
[MD, (I −K)−1] .= 1
4 Q(x) (I −Kt)−1χJφ (y) −
X
(−1)kakR(x, ak) ρ(ak, y),
(2.7)
where Q(x), and an analogous function P(x), are deﬁned by
Q(x) := (I −K)−1φ,
P(x) := (I −K)−1ψ,
(2.8)
where ρ(x, y) = R(x, y) + δ(x −y) is the distributional kernel of (I −K)−1, and where Kt is the transpose of the
operator K. (Note that K takes smooth functions to smooth functions while its transpose takes distributions to
distributions.) Observe that
qj = Q(aj),
pj = P(aj).
Next we consider commutators with M and use the ﬁrst representation (2.1) of K(x, y). We have immediately
[M, K] = (φ(x) ψ(y) −ψ(x) φ(y)) χJ(y),
and so, by (2.3) again,

M, (I −K)−1 .= Q(x) (I −Kt)−1ψ χJ(y) −P(x) (I −Kt)−1φχJ(y).
(2.9)
Notice that since
(I −Kt)−1ψχJ = (I −K)−1ψ = P
on J,
and similarly for φ, Q, we deduce
R(x, y) = Q(x) P(y) −P(x) Q(y)
x −y
(x, y ∈J.)
In particular we have
R(aj, ak) = qj pk −pj qk
aj −ak
(j̸ = k)
(2.10)
R(x, x) = Q′(x) P(x) −P ′(x) Q(x)
(x ∈J).
(2.11)
In order to compute R(aj, aj), and also the derivatives in (1.11) and (1.12), we must ﬁnd Q′(x) and P ′(x). We
begin with the obvious
x Q′(x) = MD(I −K)−1φ (x) = (I −K)−1MD φ (x) +

MD, (I −K)−1
φ (x).
7
