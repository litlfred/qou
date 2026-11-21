---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Dilogarithm identities"
section_id: sec-004-13-dilogarithm-identities-and-conformal-weights
section_title: "Dilogarithm identities and conformal weights."
section_number: 1.3
pages: 23-26
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
toc_source: inferred
doc_brief: "Dilogarithm identities — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
Let us consider the following dilogarithm sum
n−1
X
k=1
r
X
m=1
L

sin kϕ · sin(n −k)ϕ
sin(m + k)ϕ · sin(m + n −k)ϕ

:= π2
6 s(j, n, r),
where ϕ = (j + 1)π
n + r , 0 ≤2j ≤n + r −2 and g.c.d. (j + 1, n + r) = 1.
24
Anatol N. Kirillov
Theorem 2 (A.N. Kirillov [Kir7]). 1. We have
s(j, n, r) = 6(r + n)
[ n−1
2
]
X
k=0
{1
6 −B2 ((n −1 −2k)θ)} −1
4{2n2 + 1 + 3(−1)n},
(1.28)
where
θ = j + 1
n + r,
and
B2(x) = −1
π2
∞
X
k=1
cos 2kπx
k2
is the second modiﬁed Bernoulli
polynomial.
2. (Level - rank duality)
s(j, n, r) + s(j, r, n) = nr −1
Corollary 1. We have
s(j, n, r) = c(n)
r
−24h(r,n)
j
+ 6Z+,
where
c(n)
r
= (n2 −1)r
n + r
,
h(n,r)
j
= n(n2 −1)
24
· j(j + 2)
r + n ,
0 ≤j ≤r + n −2
are the central charge and conformal dimensions of the SU(n) level r WZNW primary
ﬁelds, respectively.
Sketch of a proof of Theorem 2.
We are going to show that the dilogarithm identity (1.28) follows from the functional
equation (1.4) and the well-known results (F. Newman, 1847)
ReL(eiθ) = π2B2
 θ
2π

,
ReL

eiθ
2 cos θ

= −π2B2
 θ
π + 1
2

.
(1.29)
(Hint: take x := e2iθ in the Abel duplication formula (1.7) and use functional equation for
the modiﬁed Bernoulli polynomial: B2(nx) = n
n−1
X
k=0
B2

x + k
n

.)
We start with a proving of the following accessible dilogarithm identity
L
1 −a−1
1 −b−1 · 1 −ac
1 −bc

= L
b −a
1 −a

+ L
(b −a)c
1 −ac

−L
(b −1)ac
1 −ac

(1.30)
−L
(bc −1)a
1 −a

+ L(abc) + L(ba−1) −L
 −b
1 −b

−L
 −bc
1 −bc

,
where a, b, c ∈C are the complex numbers such that a̸ = 1, c−1, and b̸ = 1, c−1.
Dilogarithm identities
25
For this purpose let us apply three times the ﬁve-term relation (1.4):
L
1 −a−1
1 −b−1 · 1 −ac
1 −bc

+ L
 1 −bc
1 −ac

−L
1 −a−1
1 −b−1

−L
(a −1)bc
1 −bc

−L
1 −abc
1 −ac

= 0,
L
(a −1)bc
1 −bc

+ L
(bc −1)a
1 −a

−L(abc) −L
 −a
1 −a

−L
 −bc
1 −bc

= 0,
L
1 −a−1
1 −b−1

+ L
 1 −b
1 −a

−L(ba−1) −L
 −b
1 −b

+ L
 −a
1 −a

−L(1) = 0.
Taking the sum of these, one can obtain the relation (1.30). The next step is to consider
a specialization
a −→exp(2iθ),
b −→exp(2iϕ),
c −→exp(2iψ)
of the dilogarithm identity (1.30). One can easily check that under this specialization the
following rules are valid
1 −a−1
1 −b−1 · 1 −ac
1 −bc −→sin ϕ
sin θ · sin(ϕ + ψ)
sin(θ + ψ) ,
b −a
1 −a −→−sin(ϕ −θ)
sin θ
exp(iϕ),
(b −a)c
1 −ac −→−sin(ϕ −θ)
sin(θ + ψ) exp(i(ϕ + ψ)),
(b −1)ac
1 −ac
−→−
sin ϕ
sin(θ + ψ) exp(i(ϕ + θ + ψ)),
(bc −1)a
1 −a
−→−sin(ϕ + ψ)
sin θ
exp(i(ϕ + θ + ψ)),
−b
1 −b −→
ei(ϕ+ π
2 )
2 cos(ϕ + π
2 ).
Finally, let us introduce a single-valued function (see e.g. [Le1], [KR1])
L(x, θ) := ReL(xeiθ).
Taking the real part of the both sides of specialized dilogarithm identity (1.30) and using
the Newman formulae (1.29), one can obtain
L
 sin θ
sin ϕ · sin(θ + ψ)
sin(ϕ + ψ)

= L

−sin(ϕ −θ)
sin θ
, ϕ

+ L

−sin(ϕ −θ)
sin(θ + ψ), ϕ + ψ

(1.31)
−L

−
sin ϕ
sin(θ + ψ), θ + ϕ + ψ

−L

−sin(ϕ + ψ)
sin θ
, θ + ϕ + ψ

+ π2

B2
ϕ + θ + ψ
π

−B2
ϕ + ψ
π

+ B2
ϕ −θ
π

−B2
ϕ
π

.
As it was shown in [Kir7], the dilogarithm identity (1.28) follows from (1.31) and properties
of the modiﬁed Bernoulli polynomial B2(x).
26
Anatol N. Kirillov
Remark. One can show that the ﬁve-term relation (1.4) follows from the nine-term
relation (1.30). Namely, let us take x := a = b and y := bc in (1.30) (a, b, c ∈R). Then
(1.30) is reduced to the relation
L(xy) = L(x) + L(y) + L

−x1 −y
1 −x

+ L

−y 1 −x
1 −y

,
which is a form of the ﬁve-term relation due to C. Hill (see e.g. [Le1]).
Hint: using the Landen result Re

L(x) + L
 −x
1 −x

= 0, replace the terms L(a)
and L(b) in RHS of (1.6) on −L
 −a
1 −a

and −L
 −b
1 −b

correspondently. It is easy to
check that
−a
1 −a = −x1 −y
1 −x and
−b
1 −b = −y 1 −x
1 −y .
