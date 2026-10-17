---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-014-5-asymptotic-expansion-of-polyanalytic-bergman-k
section_title: "Asymptotic expansion of polyanalytic Bergman kernels"
section_number: 5
pages: 9-9
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
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
