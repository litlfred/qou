---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-014-44-the-eﬀective-estimate-of-the-point-evaluation
section_title: "The eﬀective estimate of the point evaluation. The problem with Proposition 4.3 as it"
section_number: 4.4
pages: 9-10
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
stands is the need to assume that ψ ≤0. We now show how to reduce the assumption to a
minimum.
Given a positive Borel measure µ on D with ﬁnite Riesz mass
Z
D
(1 −|z|2)dµ(z) < +∞,
we associate the Green potential G(µ), which is given by
G[µ](z) := 1
π
Z
D
log

z −w
1 −z ¯w

2
dµ(w),
z ∈D.
The Green potential of a positive measure is subharmonic. It is well-known that the Laplacian
∆ψ of a subharmonic function ψ is a positive distribution, which can be identiﬁed with a
positive Borel measure on D. Then, if ∆ψ has ﬁnite Riesz mass, we may form the potential
G[∆ψ], which diﬀers from ψ by a harmonic function.
10
ANTTI HAIMI AND HAAKAN HEDENMALM
Proposition 4.4. Let ψ be subharmonic and u bianalytic on D. If ∆ψ has ﬁnite Riesz mass, then
|u(0)|2 ≤8
π
h
1 + 6|G[∆ψ](0)|2i
e−2ψ(0)
Z
D
|u|2e2ψdA.
Proof. We decompose ψ = G[∆ψ]+h, where h is a harmonic function. To the harmonic function
h we associate a zero-free analytic function H such that h = log |H|. As the Green potential
has G[∆ψ] ≤0 (this is trivial by computation; it also expresses a version of the maximum
principle), we may invoke Proposition 4.3 with G[∆ψ] in place of ψ, and uH in place of u (The
function uH is bianalytic because H is holomorphic and u is bianalytic). The result is
(4.4.1)
|u(0)|2e2h(0) = |u(0)H(0)|2 ≤8
π
h
1 + 6|G
h
∆ψ](0)|2i
e−2G[∆ψ](0)
Z
D
|u(w)H(w)|2e2G[∆ψ](w)dA(w)
= 8
π
h
1 + 6|G
h
∆Ψ](0)|2i
e−2G[∆ψ](0)
Z
D
|u(w)|2e2h(w)+2G∆ψ](w)dA(w)
= 8
π
h
1 + 6|G[∆ψ](0)|2i
e−2G[∆ψ](0)
Z
D
|u(w)|2e2ψ(w)dA(w),
which is equivalent to the claimed inequality.
□
Remark 4.5. As stated, the proposition is void unless
G[∆ψ](0) = 1
π
Z
D
log |w|2dµ(w) > −∞.
5. Asymptotic expansion of polyanalytic Bergman kernels
