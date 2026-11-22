---
doc_id: arxiv-hep-th-9304063v2
doc_title: "arXiv:hep-th/9304063v2 29 Jan 1999"
section_id: page-006
section_title: "Page 6"
section_number: null
pages: 6-6
source_pdf: 9304063v2.pdf
source_sha256: 14a82437462eae23
toc_source: undetermined
doc_brief: "arXiv:hep-th/9304063v2 29 Jan 1999 — 18 sections: Page 1; Page 2; Page 3"
---
From this and (1.26) we deduce
r(n; s) ∼
(n−1
Y
k=0
Γ(α + k + 1) k!
)
π−n 2−n(2n+2α+1) s−n2
2 −α
2 n e2n√s.
(1.28)
For the special case α = 0, the quantity r(1; s) can be expressed exactly in terms of Bessel functions (see (2.30)
below).
II. DIFFERENTIAL EQUATIONS
A. Derivation of the system of equations
We shall use two representations for our kernel. The ﬁrst is just our deﬁnition (1.2a) using the notation (1.6),
K(x, y) = φ(x)ψ(y) −ψ(x)φ(y)
x −y
.
(2.1)
The second is the integral representation
K(x, y) = 1
4
Z 1
0
φ(xt) φ(yt) dt.
(2.2)
This follows from the diﬀerentiation formula
z J′
α(z) = α Jα(z) −z Jα+1(z),
which gives the alternative representation
λ
√x Jα+1(√x) Jα(√y) −Jα(√x) √y Jα+1(√y)
2 (x −y)
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
