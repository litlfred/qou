---
doc_id: arxiv-hep-th-9304063v2
doc_title: "Level Spacing Distributions and the Bessel Kernel Craig A. Tracy∗"
section_id: sec-005-2-x-y
section_title: "(x −y)"
section_number: 2
pages: 6-7
source_pdf: 9304063v2.pdf
source_sha256: 14a82437462eae23
doc_brief: "Level Spacing Distributions and the Bessel Kernel Craig A. Tracy∗ — 26 sections: INTRODUCTION AND STATEMENT OF RESU; KN(; (α2 −aj + 2v)q2"
---
for K(x, y), and the Christoﬀel-Darboux type formula (7.14.1(9)) of [9].
Our derivation will use, several times, the commutator identity
[L, (I −K)−1] = (I −K)−1[L, K](I −K)−1,
(2.3)
which holds for arbitrary operators K and L, and the diﬀerentiation formula
d
da (I −K)−1 = (I −K)−1 dK
da (I −K)−1,
(2.4)
which holds for an arbitrary operator depending smoothly on a parameter a. We shall also use the notations
M = multiplication by the independent variable,
D = diﬀerentiation,
and a subscript on an operator indicates the variable on which it acts.
It will be convenient to think of our operator K as acting, not on J, but on (0, ∞) and to have kernel
K(x, y) χJ(y)
where χJ is the characteristic function of J. We continue to denote the resolvent kernel of K by R(x, y) and note that
it is smooth in x but discontinuous at y = aj. The quantities R(aj, aj) appearing in (1.5) are interpreted to mean
lim
y→aj
y∈J
R(aj, y),
and similarly for pj and qj in formulas (1.7). The deﬁnitions (1.8) of u and v must be modiﬁed to read
u = (φ χJ, (I −K)−1φ),
v = (φ χJ, (I −K)−1ψ),
(2.5)
6
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
