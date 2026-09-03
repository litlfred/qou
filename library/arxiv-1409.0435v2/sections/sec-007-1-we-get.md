---
doc_id: arxiv-1409.0435v2
doc_title: "Asymptotics for Toeplitz determinants: perturbation of symbols with a gap"
section_id: sec-007-1-we-get
section_title: "We get"
section_number: 1
pages: 23-24
source_pdf: 1409.0435v2.pdf
source_sha256: 0c6abbb9c5a720d9
doc_brief: "Asymptotics for Toeplitz determinants: perturbation of symbols with a gap — We study the determinants of Toeplitz matrices as the size of the matrices tends to inﬁnity, in the particular case where"
---
|I1|
=
O
 
n3
Z
[θ0,θ0+r]∪[2π−θ0−r,2π−θ0]

e2ng(eiα)+nℓ

 dα
!
,
|I2|
=
O
Z 2π−θ0−r
θ0+r

e2ng(eiα)+nℓ

 dα

,
23
as n →∞with s ≤e−xcn. The function 2g(z) + ℓ−xc is always negative on γc except
that it has a zero of order two at z = −1. Therefore we obtain after a straightforward
analysis that
|I1| = O

en(xc−C)
,
C > 0,
(5.7)
|I2| = O(n−1/2enxc),
(5.8)
as n →∞, s ≤e−xcn.
If we integrate (5.6) from 0 up to s = e−xn ≤e−xcn, we ﬁnally obtain the desired
estimate
ln Dn(s, θ0, W) −ln Dn(0, θ0, W) =
Z s
0
(I1 + I2)ds′ = O(n−1/2e−n(x−xc)).
5.2
Alternative proof of Theorem 1.1 if W = 0, s = o(n1/2e−nxc)
In the case where W = 0, there is an alternative approach to prove Theorem 1.1: we
can use the diﬀerential identity (2.18) instead of (2.6). This does not make the proof
much shorter, but it has the advantage that no integrals have to be estimated, and
that we only need information about Y at the points 0 and z0, instead of on the entire
curve γc. The objects in the diﬀerential identity can be computed more explicitly in
this case by the following result.
Proposition 5.1 Let W = 0. As n →∞with x > xc, we have
Y12(0) = e−nℓ

sin θ0
2 + O(n−1/2)

,
(5.9)
∂s ln Y12(0) = O(n−1/2enxc),
(5.10)
Y11(z0) = e−nℓ
2 O(n1/2).
(5.11)
Proof.
Using (5.2) and the expressions g(0) = πi and P (∞)
