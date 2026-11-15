---
doc_id: arxiv-2312.00624v1
doc_title: "On the structure of wave functions in complex Chern–Simons theory"
section_id: sec-018-computing-the--expansions
section_title: "Computing the -expansions"
section_number: null
pages: 37-38
source_pdf: 2312.00624v1.pdf
source_sha256: bda867f7b84f69c3
toc_source: outline
doc_brief: "On the structure of wave functions in complex Chern–Simons theory — We study the structure of wave functions in complex Chern–Simons theory on the complement of a hyperbolic knot, emphasizing the"
---
For completeness, we include here the details of the computations performed in Section 3.2. We
observe that, as a consequence of Eqs. (3.3), (3.7), the coefficient functions ˆa±n(q) satisfy the relation
ˆa±n(q)q−σ±n =
X
k|n
kD±k

q
n
k

q−n
k σ±k
k−1
X
j=0
q
n
k j ,
n ∈Z>0 ,
(A.1)
and we write the Z-polynomials D±k(q) explicitly as
D±k(q) =
deg D±k
X
ℓ=0
D±k,ℓqℓ,
k ∈Z>0 ,
(A.2)
where D±k,ℓis an integer and deg D±k denotes the degree of the polynomial. Let us now take
q = e2πi P
Q ,
P, Q ∈Z>0 coprime ,
(A.3)
while we introduce
qϵ = eiℏϵ ,
ℏϵ = 2π P
Q + ϵ ,
0 < ϵ ≪1 ,
(A.4)
and consider the limit ϵ →0. In the case n = sQ, s ∈Z>0, we have the ϵ-expansions
D±k

q
sQ
k
ϵ

=

1 + iϵ q ∂
∂q

D±k

q
sQ
k

+ O(ϵ2) ,
(A.5a)
k−1
X
j=0
q
sQ
k (j−σ±k)
ϵ
=

1 + iϵ q ∂
∂q
 k−1
X
j=0
q
sQ
k (j−σ±k) + O(ϵ2) ,
(A.5b)
and therefore also
ˆa±sQ(qϵ)q−σ±sQ
ϵ
=

1 + iϵ q ∂
∂q

ˆa±sQ(q)q−σ±sQ + O(ϵ2) .
(A.6)
We now observe that
1
qsQ
ϵ
−1
= −
i
sQϵ −1
2 + O(ϵ) ,
(A.7)
and, combining Eqs. (A.6), (A.7), we finally obtain the NLO ϵ-expansion in Eq. (3.22a). On the
dual side, we consider
qD = q
Q2
P 2 = e2πi Q
P ,
qϵ,D = e
4π2i
ℏϵ ,
(A.8)
– 36 –
and take again the limit ϵ →0. It follows that
qϵ,D = qD e−ϵ Q2
P 2 +O(ϵ2) .
(A.9)
Similarly to the case above, when n = sP, s ∈Z>0, we have the ϵ-expansions
D±k

q
sP
k
ϵ,D

=

1 −iϵQ2
P 2 qD
∂
∂qD

D±k

q
sP
k
D

+ O(ϵ2) ,
(A.10a)
k−1
X
j=0
q
sP
k (j−σ±k)
ϵ,D
=

1 −iϵQ2
P 2 qD
∂
∂qD
 k−1
X
j=0
q
sP
k (j−σ±k)
D
+ O(ϵ2) ,
(A.10b)
and therefore also
ˆa±sP (qϵ,D)q−σ±sP
ϵ,D
=

1 −iϵQ2
P 2 qD
∂
∂qD

ˆa±sP (qD)q−σ±sP
D
+ O(ϵ2) .
(A.11)
Finally, we note that
1
qsP
ϵ,D −1 =
iP
sQ2ϵ −1
2 +
i
2πsQ + O(ϵ) ,
(A.12)
and, combining Eqs. (A.11), (A.12), we obtain the NLO ϵ-expansion in Eq. (3.22b).
