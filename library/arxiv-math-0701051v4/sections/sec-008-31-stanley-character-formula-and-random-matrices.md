---
doc_id: arxiv-math-0701051v4
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS RELATED TO STANLEY CHARACTER FORMULA"
section_id: sec-008-31-stanley-character-formula-and-random-matrices
section_title: "Stanley character formula and random matrices"
section_number: 3.1
pages: 8-10
source_pdf: 0701051v4.pdf
source_sha256: 4592a048c3b84a8d
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS RELATED TO STANLEY CHARACTER FORMULA — We prove an upper bound for characters of the symmetric groups."
---
diagram and N ≥ r(λ), c(λ). We consider a random matrixTλ = (tij)1≤i,j≤N
such that
• its entries (tij) are independent random variables;
• if (i, j) ∈ λ then tij is a complex centered Gaussian variable, that is
to say that
E(tij) = 0 , E(tij
tij) = 1 , E(t2
ij) = 0;
• otherwise, if (i, j) /∈ λ then tij = 0.
The moments of TλT ⋆
λ are given by a formula which is very similar to the
Stanley formula for characters (Theorem 2):
ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS 9
Theorem 7. With the deﬁnitions above and π ∈ Sl with a cycle decompo-
sition k1, . . . , kr
(14) E
(
Tr(TλT ⋆
λ )k1 · · ·Tr(TλT ⋆
λ )kr
)
=
∑
σ1,σ2∈Sl
σ1σ2=π
N λ(σ1, σ2).
Proof. The ﬁrst step is to expand the product and the trace on the left -hand
side:
E
(
Tr(TλT ⋆
λ )k1 . . . Tr(TλT ⋆
λ )kr
)
= E
[( ∑
i1
1,j1
1,...,i1
k1 ,j1
k1
ti1
1j1
1
ti1
2j1
1
. . . ti1
k1 j1
k1
ti1
1j1
k1
)
. . .
( ∑
ir
1,jr
1,...,ir
kr ,jr
kr
tir
1jr
1
tir
2jr
1 . . . tir
kr jr
kr
tir
1jr
kr
) ]
=
∑
i1,j1,...,il,jl
E
[ l∏
m=1
timjm
tiπ (m)jm
]
.
Since random variables (tij) are Gaussian, we can apply Wick formula (see
[Zvo97]) to each summand; in order to do this we need to consider all ways
of pairing factors (tim,jm) with factors (tiπ (m)jm). Each such a pairing can
be identiﬁed with a permutation σ ∈ Sl: therefore
E
[ l∏
m=1
timjmtiπ (m)jm
]
=
∑
σ∈Sl
[ l∏
m=1
E
(
tiσ (m)jσ (m)tiπ (m)jm
) ]
Using the deﬁnition of T , this is equal to
∑
σ∈Sl
l∏
m=1
[iσ(m) = iπ(m)] [jσ(m) = jm] [(iσ(m), jσ(m)) ∈ λ].
If we plug this in our calculation, the left-hand side of (14) is equal to
∑
σ∈Sl
∑
i1,j1,...,il,jl
( l∏
m=1
[iσ(m) = iπ(m)] [jσ(m) = jm] [(iσ(m), jσ(m)) ∈ λ]
)
.
If we denote σ1 = πσ −1
2 , σ2 = σ then the sum over σ can be seen as
a sum over all σ1, σ2 ∈ Sl such that σ1σ2 = π. If a sequence i1, . . . , il
(respectively, sequence j1, . . . , jl) contributes to the above sum then it must
be constant on each cycle of σ1 (respecively, each cycle of σ2). It follows
that there is a bijective correspondence between sequences i1, j1, . . . , il, jl
which contribute to the above sum and colorings of the cycles of σ1 and σ2
which are compatible with λ. □
10 V ALENTIN FÉRAY AND PIOTR ´SNIADY
By comparing the above result with Theorem 2, we obtain the following
corollary.
Corollary 8. Let λ be a Young diagram. Then for any permutation π ∈ Sl
with a cycle decomposition k1, . . . , kr
|Σ λ(π)| ≤ E
(
Tr(TλT ⋆
λ )k1 · · · Tr(TλT ⋆
λ )kr
)
.
We shall not follow this idea in this article and we will proveall estimates
from scratch, but it is worth noticing that the above Corolla ry shows that
the asymptotics of characters of symmetric groups can be ded uced from
the corresponding asymptotics of random matrices. In parti cular it follows
that when the lengths k1, . . . , kr of the cycles of π are big enough then the
asymptotics of the corresponding character is related to the limit distribution
of the largest eigenvalue of TλT ∗
λ [SS98]. Notice, however, that due to
the minus sign in Theorem 2 and the resulting cancelations th e character
|Σ λ(π)| could, at least in priciple, be much smaller than the appropr iate
moment of the random matrix TλT ∗
λ .
