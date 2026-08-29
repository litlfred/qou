---
doc_id: arxiv-math-9905032v2
doc_title: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS"
section_id: sec-032-41-results-and-strategy-of-proof-in-this-section
section_title: "Results and strategy of proof. In this section we prove Theo-"
section_number: 4.1
pages: 24-26
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
doc_brief: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
rem 4 which was stated in Section 1.4 of the Introduction. We r efer the
ASYMPTOTICS OF PLANCHEREL MEASURES 25
reader to Section 1.4 for a discussion of the relation betwee n Theorem
4 and the results obtained in [2, 3, 23].
Recall that the Airy kernel was deﬁned as follows
A(x, y) = A(x)A′(y) − A′(x)A(y)
x − y .
where A(x) is the Airy function (1.15). The Airy ensemble is, by def-
inition, a random point process on R, whose correlation functions are
given by
ρAiry
k (x1, . . . , xk) = det
[
A(xi, xj)
]
1≤i,j ≤k
.
This ensemble was studied in [32]. We denote by ζ1 > ζ 2 > . . . a
random conﬁguration of the Airy ensemble. Theorem 4 says tha t after
a proper scaling and normalization, the rows λ1, λ2, . . . of a Plancherel
random partition λ converge in joint distribution to the Airy ensemble.
Namely, the following random variables ~λ
~λ =
(
~λ1 ≥~λ2 ≥ . . .
)
, ~
λi = n1/ 3
( λi
n1/ 2 − 2
)
,
converge, in joint distribution, to the Airy ensemble as n → ∞.
In the proof of Theorem 4, we shall follow the strategy explai ned in
Section 1.5 of the Introduction. First, we shall prove that u nder the
poissonized measure M θ on the set of partitions λ, the random variables
~
λ converge, in joint distribution, to the Airy ensemble as θ ≈ n → ∞.
This result is stated below as Theorem 5. From this, using cer tain
monotonicity and Lemma 4.7 which is due to K. Johansson, we sh all
conclude that the same is true for the measures Mn as n → ∞.
The proof of Theorem 5 will be based on the analysis of the beha vior
of the correlation functions of M θ , θ ≈ n → ∞ , near the point 2 √
n.
From the expression for correlation functions of M θ given in Theo-
rem 1 it is clear that this amounts to the study of the asymptot ics of
J2√n(2
√
θ) when θ ≈ n → ∞ . This asymptotics is classically known
and from it we shall derive the following
Proposition 4.1. Set r =
√
θ. We have
r
1
3 J
(
2r + xr
1
3 , 2r + yr
1
3 , r2
)
→ A(x, y), r → +∞ ,
uniformly in x and y on compact sets of R.
The prefactor r
1
3 corresponds to the fact that we change the local
scale near 2 r to get non-vanishing limit correlations.
Using this and verifying certain tail estimates we obtain th e following
