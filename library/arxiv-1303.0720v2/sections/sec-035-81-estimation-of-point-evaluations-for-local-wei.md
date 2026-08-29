---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-035-81-estimation-of-point-evaluations-for-local-wei
section_title: "Estimation of point evaluations for local weighted Bergman spaces. The spaces PA2"
section_number: 8.1
pages: 31-33
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
q,m
considered in this paper involve the weight e−2mQ, where (locally at least) Q is subharmonic
and smooth.
The estimates we derived in Section 4 for q = 2 do not apply immediately,
as the weights considered there had rather the converse property of being exponentials of
32
ANTTI HAIMI AND HAAKAN HEDENMALM
subharmonic functions. Nevertheless, this diﬃculty is easy to overcome. Compare with, e.g.,
[2] for the analytic case.
Proposition 8.1. Let u be bianalytic in the disk D(z0, δm−1/2), where δ is a positive real parameter and
m ≥1. Suppose Q is C1,1-smooth in ¯D(z0, δ) and subharmonic in D(z0, δ), with
A := essupz∈D(z0,δ)∆Q(z) < +∞.
We then have the estimate
|u(z0)|2 ≤8m
πδ2 (1 + 6A2) e2Aδ2e2mQ(z0)
Z
D(z0,δm−1/2)
|u|2e−2mQdA.
Proof. Without loss of generality, we may assume that z0 = 0. For ξ ∈D, we put
ψm(ξ) := Aδ2|ξ|2 −mQ(δm−1/2ξ)
and
um(ξ) := u(δm−1/2ξ).
It is immediate that
(8.1.1)
−mQ(δm−1/2ξ) ≤ψm(ξ) ≤Aδ2 −mQ(δm−1/2ξ),
and we may also check that
(8.1.2)
0 ≤∆ψm(ξ) = Aδ2 −δ2(∆Q)(δm−1/2ξ) ≤Aδ2,
ξ ∈D.
so that ψm is subharmonic, and we obtain that
(8.1.3)
0 ≥G[∆ψm](0) = 1
π
Z
D
log |ξ|2∆ψm(ξ)dA(ξ) ≥Aδ2
Z
D
log |ξ|2dA(ξ) ≥−Aδ2.
Next, since ψ is subharmonic with ﬁnite Riesz mass, we may apply Proposition 4.4:
(8.1.4)
|u(0)|2e−2mQ(0) = |um(0)|2e2ψm(0) ≤8
π
h
1 + 6|G[∆ψm](0)|2i Z
D
|um|2e2ψmdA
≤8
π(1 + 6A2δ4)
Z
D
|um|2e2ψmdA ≤8
π(1 + 6A2δ4) e2Aδ2 Z
D
|u(δm−1/2ξ)|2e−2mQ(δm−1/2ξ)dA(ξ)
= 8m
πδ2 (1 + 6A2δ4) e2Aδ2 Z
D(0,δm−1/2)
|u(z)|2e−2mQ(z)dA(z),
and the claim follows.
Note that we used the estimates (8.1.1) and (8.1.2).
The proof is
complete.
□
We can also estimate the ¯∂-derivative:
Proposition 8.2. Suppose we are in the setting of Proposition 8.1. We then have the estimate
| ¯∂u(z0)|2 ≤3m
πδ2 e2Aδ2e2mQ(z0)
Z
D(z0,δm−1/2)
|u|2e−2mQdA.
Proof. The argument is analogous to that of the proof of Proposition 8.1, except that it is based
on Proposition 4.2.
□
ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS
33
