---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Steklov Mathematical Institute"
section_id: sec-025-2-level---rank-duality
section_title: "(Level - rank duality)"
section_number: 2
pages: 24-26
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
doc_brief: "DILOGARITHM IDENTITIES ANATOL N. KIRILLOV — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
s(j,n,r ) +s(j,r,n ) = nr− 1
Corollary 1. We have
s(j,n,r ) = c(n)
r − 24h(r,n)
j + 6Z+,
where
c(n)
r = (n2− 1)r
n +r , h (n,r)
j = n(n2− 1)
24 · j(j + 2)
r +n , 0≤j≤r +n− 2
are the central charge and conformal dimensions of the SU (n) level r WZNW primary
ﬁelds, respectively.
Sketch of a proof of Theorem 2.
We are going to show that the dilogarithm identity (1.28) fol lows from the functional
equation (1.4) and the well-known results (F. Newman, 1847)
ReL(eiθ) = π2
B2
( θ
2π
)
, ReL
( eiθ
2 cosθ
)
=−π2B2
(θ
π + 1
2
)
. (1.29)
(Hint: take x :=e2iθ in the Abel duplication formula (1.7) and use functional equ ation for
the modiﬁed Bernoulli polynomial: B2(nx) = n
n−1∑
k=0
B2
(
x + k
n
)
.)
We start with a proving of the following accessible dilogari thm identity
L
(1−a−1
1−b−1· 1−ac
1−bc
)
= L
(b−a
1−a
)
+ L
((b−a)c
1−ac
)
− L
((b− 1)ac
1−ac
)
(1.30)
− L
((bc− 1)a
1−a
)
+ L(abc) + L(ba−1)− L
( −b
1−b
)
− L
( −bc
1−bc
)
,
where a,b,c ∈ C are the complex numbers such that a⁄= 1,c −1, and b⁄= 1,c −1.
Dilogarithm identities 25
For this purpose let us apply three times the ﬁve-term relati on (1.4):
L
(1−a−1
1−b−1· 1−ac
1−bc
)
+ L
(1−bc
1−ac
)
− L
(1−a−1
1−b−1
)
− L
((a− 1)bc
1−bc
)
− L
(1−abc
1−ac
)
= 0,
L
((a− 1)bc
1−bc
)
+ L
((bc− 1)a
1−a
)
− L(abc)− L
( −a
1−a
)
− L
( −bc
1−bc
)
= 0,
L
(1−a−1
1−b−1
)
+ L
(1−b
1−a
)
− L(ba−1)− L
( −b
1−b
)
+ L
( −a
1−a
)
− L(1) = 0.
Taking the sum of these, one can obtain the relation (1.30). T he next step is to consider
a specialization
a−→ exp(2iθ), b−→ exp(2iϕ), c−→ exp(2iψ)
of the dilogarithm identity (1.30). One can easily check tha t under this specialization the
following rules are valid
1−a−1
1−b−1· 1−ac
1−bc−→ sinϕ
sinθ· sin(ϕ +ψ)
sin(θ +ψ),
b−a
1−a−→− sin(ϕ−θ)
sinθ exp(iϕ),
(b−a)c
1−ac −→− sin(ϕ−θ)
sin(θ +ψ) exp(i(ϕ +ψ)),
(b− 1)ac
1−ac −→− sinϕ
sin(θ +ψ) exp(i(ϕ +θ +ψ)),
(bc− 1)a
1−a −→− sin(ϕ +ψ)
sinθ exp(i(ϕ +θ +ψ)),
−b
1−b−→ ei(ϕ+ π
2 )
2 cos(ϕ + π
2 ).
Finally, let us introduce a single-valued function (see e.g . [Le1], [KR1])
L(x,θ ) := ReL(xeiθ).
Taking the real part of the both sides of specialized dilogar ithm identity (1.30) and using
the Newman formulae (1.29), one can obtain
L
( sinθ
sinϕ· sin(θ +ψ)
sin(ϕ +ψ)
)
= L
(
− sin(ϕ−θ)
sinθ ,ϕ
)
+ L
(
− sin(ϕ−θ)
sin(θ +ψ),ϕ +ψ
)
(1.31)
− L
(
− sinϕ
sin(θ +ψ),θ +ϕ +ψ
)
− L
(
− sin(ϕ +ψ)
sinθ ,θ +ϕ +ψ
)
+π2
{
B2
(ϕ +θ +ψ
π
)
−B2
(ϕ +ψ
π
)
+B2
(ϕ−θ
π
)
−B2
(ϕ
π
)}
.
As it was shown in [Kir7], the dilogarithm identity (1.28) fo llows from (1.31) and properties
of the modiﬁed Bernoulli polynomial B2(x).
