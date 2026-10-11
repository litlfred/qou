---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-012-5-asymptotic-expansion-of-polyanalytic-bergman-k
section_title: "Asymptotic expansion of polyanalytic Bergman kernels"
section_number: 5
pages: 9-10
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
---
9
Proposition 4.3. Suppose u is bianalytic and that ψ is subharmonic in D. If ψ ≤0 in D, then
|u(0)|2 ≤8
π[1 + 6|ψ(0)|2]e−2ψ(0)
Z
D
|u|2e2ψdA.
Proof. We will use the decomposition u(z) = u1(z) + c¯z + |z|2u2(z), where u1, u2 are both holo-
morphic. Proposition 4.2 allows us estimate c = ¯∂u(0), so that
(4.3.1)
Z 1
0

cr
π
Z
T
¯ζψ(rζ)ds(ζ)

2
rdr ≤
Z 1
0
|c|r
π
Z
T
|ψ(rζ)|ds(ζ)
2
rdr
≤
Z 1
0
4|c|2r2|ψ(0)|2rdr = |c|2|ψ(0)|2 ≤3
π|ψ(0)|2e−2ψ(0)
Z
D
|u|2e2ψdA.
Note that we used the subharmonicity of ψ, and that ψ ≤0. By the standard Hilbert space
inequality ∥x + y∥2 ≤2(∥x∥2 + ∥y∥2), it follows from Lemma 4.1 and the above estimate (4.3.1)
that
(4.3.2)
Z 1
0
|u1(0) + r2u2(0)|2rdr ≤2
Z 1
0

u1(0) + r2u2(0) + cr
π
Z
T
¯ζψ(rζ)ds(ζ)

2
rdr
+ 2
Z 1
0

cr
π
Z
T
¯ζψ(rζ)ds(ζ)

2
rdr ≤e−2ψ(0)
π
Z
D
|u|2e2ψdA + 6
π|ψ(0)|2e−2ψ(0)
Z
D
|u|2e2ψdA
= 1
π
n
1 + 6|ψ(0)|2o
e−2ψ(0)
Z
D
|u|2e2ψdA.
Next, we expand the left hand side of (4.3.2):
(4.3.3)
Z 1
0
|u1(0) + r2u2(0)|2rdr =
Z 1
0
n
|u1(0)|2 + r4|u2(0)|2 + 2r2Re[u1(0)u2(0)]
o
rdr
= 1
2|u1(0)|2 + 1
6|u2(0)|2 + 1
2Re[u1(0)u2(0)] = 1
8|u1(0)|2 + 1
6

3
2u1(0) + u2(0)

2
≥1
8|u1(0)|2.
So, (4.3.2) and (4.3.3) together give that
|u0(0)|2 ≤8
πe−2ψ(0) h
1 + 6|ψ(0)|2i
e−2ψ(0)
Z
D
|u|2e2ψdA,
as needed.
□
4.4. The eﬀective estimate of the point evaluation. The problem with Proposition 4.3 as it
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
