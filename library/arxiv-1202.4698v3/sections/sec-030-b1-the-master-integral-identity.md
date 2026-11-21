---
doc_id: arxiv-1202.4698v3
doc_title: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories"
section_id: sec-030-b1-the-master-integral-identity
section_title: "B.1 The master integral identity"
section_number: null
pages: 24-25
source_pdf: 1202.4698.pdf
source_sha256: 54171c652161ca5b
toc_source: outline
doc_brief: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories — We revisit the deﬁnition of the 6j symbols from the modular double of Uq(sl(2, R)), referred to as"
---
Let us start from the V -function [S03] which is the example from Spiridonov’ theory of elliptic
hypergeometric integrals [S01, S03]4 deﬁned by
V (s) = κ
Z
T
Q8
i=1 Γ(siz±1; p, q)
Γ(z±2; p, q)
dz
2πiz,
(B.1)
where Q8
i=1 si = (pq)2 is the so-called balancing condition and
κ = (p; p)∞(q; q)∞
2
with (z; q)∞= Q∞
i=0(1 −zqi). The main building block is the elliptic gamma function deﬁned
in (A.18) above.
Theorem 1. [S03]
V (s) =
Y
1≤i<j≤4
Γ(sisj; p, q)Γ(si+4sj+4; p, q)V (t),
(B.2)
where
ti = εsi, i = 1, 2, 3, 4;
ti = ε−1si, i = 5, 6, 7, 8,
4From physical point of view this integral is the so-called superconformal index for four-dimensional SQCD
theory with SU(2) gauge group and Nf = 4 ﬂavors. The integral transformations for V -function describe the
multiple duality effect for the above theory [SV10].
25
and
ε =
r
pq
s1s2s3s4
=
rs5s6s7s8
pq
.
The integral identities used in this paper will be obtained from (B.2) by limiting procedures
[DS] which reduce the elliptic gamma functions to double Sine functions. First, we reduce V -
function to the level of hyperbolic q-hypergeometric integrals using the reparameterization of
variables
z = e2πiru,
si = e2πirµi,
i = 1, . . . , 8,
p = e2πibr,
q = e2πir/b,
(B.3)
and the subsequent limit r →0. In this limit the elliptic gamma function has the following
asymptotics
Γ(e2πirz; e2πirb, e2πir/b)
=
r→0 e−πi(2z−b−1/b)/12rSb(z).
Using it in the reduction, one obtains an integral lying on the top of a list of integrals emerg-
ing as degenerations of the V -function (we omit some simple diverging exponential multiplier
appearing in this limit together with −i),
Ih(µ1, . . . , µ8) = 1
2
Z i∞
−i∞
Q8
i=1 Sb(µi ± u)
Sb(±2u)
du,
(B.4)
with the balancing condition P8
i=1 µi = 2(b + b−1). It has the following symmetry transforma-
tion formula descending from the elliptic one
Ih(µ1, . . . , µ8) =
Y
1≤i<j≤4
Sb(µi + µj)
Y
5≤i<j≤8
Sb(µi + µj)Ih(ν1, . . . , ν8),
(B.5)
where νi = µi + ξ, νi+4 = µi+4 −ξ, i = 1, 2, 3, 4, and the parameter ξ is
2ξ =
8
X
i=5
µi −b −b−1 = b + b−1 −
4
X
i=1
µi.
Formula (B.5) will be our main tool in the following.
