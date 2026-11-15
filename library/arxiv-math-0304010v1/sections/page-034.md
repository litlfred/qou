---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-034
section_title: "Page 34"
section_number: null
pages: 34-34
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
Theorem 7.1 (Central limit theorem for Young diagrams).
According to (7.2), let
u(n)
k
=
Z
R
uk(x)∆(n)(dx),
k = 1, 2, . . .,
and let, as before, ξ2, ξ3, . . . stand for a system of independent standard Gaussians.
We have
n
u(n)
k
o
k≥1
d
−→
 ξk+1
√
k + 1

k≥1
,
n →∞.
Recall that “
d
−→” means convergence in distribution.
Note that u(n)
0
≡0, which explains why we start with k = 1, not k = 0. The
theorem is proved at the end of the section. The scheme of the proof is as follows.
We remark that the moments of ∆(n) (i.e., the random variables v(n), where the v’s
are monomials) are expressed in terms of the elements epk, appropriately centered
and scaled. To evaluate the asymptotics of the corresponding random variables
we employ Theorem 6.1. The main work reduces to expressing the (centered and
scaled) elements epk through the elements ηk and vice versa, up to lower degree
terms.
As in §6, it is convenient to deal with the extended algebra Aext ⊃A. We extend
the deﬁnition of deg1( · ) to Aext as explained in §6.
We introduce the elements q1, q2, . . . ∈Aext, which are centered and scaled ver-
sions of the elements ep2, ep3, . . .:
qk =









epk+1 −(2m)!
m!m! (p#
1 )m
(k + 1)(p#
1 )k/2
,
if k is odd, k = 2m −1, where m = 1, 2, . . .,
epk+1
(k + 1)(p#
1 )k/2 ,
if k is even, k = 2m, where m = 1, 2, . . . .
(7.6)
Since 1
2 ep2 = p1 and p1 = p#
1 , we have q1 = 0.
Proposition 7.2. For any λ ∈Y,
Z
R
xk∆λ(x)dx = qk+1(λ)
k + 1
,
k = 0, 1, . . . .
(7.7)
Proof. Set n = |λ|. By the deﬁnition of ∆λ(x), see (7.1),
Z
R
xk∆λ(x)dx = √n
Z
R
xk ¯λ(x) −|x|
2
dx −√n
Z
R
xk Ω(x) −|x|
2
dx.
By Proposition 2.2, for any k = 0, 1, . . .,
√n
Z
R
xk ¯λ(x) −|x|
2
dx = n−(k+1)/2
Z
R
xk λ(x) −|x|
2
dx
=
1
(k+1)(k+2)
epk+2(λ)
n(k+1)/2 =
1
(k+1)(k+2)
epk+2
(p#
1 )(k+1)/2 (λ).
34
