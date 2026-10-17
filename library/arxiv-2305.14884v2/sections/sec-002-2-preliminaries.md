---
doc_id: arxiv-2305.14884v2
doc_title: "PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS"
section_id: sec-002-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 5-6
source_pdf: 2305.14884v2.pdf
source_sha256: ebc8e64d901c9e4f
toc_source: outline
doc_brief: "PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS — We prove that a formal power series associated to an ideally triangulated cusped hyperbolic 3-manifold (together with some further choices)"
---
2.1. The Faddeev quantum dilogarithm. In this subsection, we recall some basic prop-
erties of the Faddeev quantum dilogarithm, which are motivations for Theorems 3.4 and 3.6
below. At the same time, we will ignore additional properties of the Faddeev quantum dilog-
arithm that play no role in our paper, such as the fact that it is a meromorphic function
with precise zeros, poles and residues.
The Faddeev quantum dilogarithm [15] ϕ := Φb satisﬁes a key integral pentagon iden-
tity [16]
e2πixy eϕ(x)eϕ(y) =
Z
R
eπiz2 eϕ(x −z)eϕ(z)eϕ(y −z) dz
(8)
where both sides are tempered distributions on
R and eϕ denotes the distributional (inverse)
Fourier transformation
eϕ(x) :=
Z
R
e−2πixyϕ(y) dy .
(9)
It turns out that the inverse Fourier transform of ϕ±1 is expressed in terms of ϕ as given
in [2, Sec.13.2]
Z
R
e−2πixyϕ(y) dy = ζ8(q/eq)
1
24e−πix2ϕ(−x + cb)
Z
R
e−2πixyϕ(y)−1 dy = ζ−1
8 (eq/q)
1
24eπix2ϕ(x −cb)
(10)
where q = e2πib2, eq = e−2πi/b2, cb =
i
2(b + b−1) and ζ8 = e2πi/8. The Faddeev quantum
dilogarithm satisﬁes the inversion formula
ϕ(x)ϕ(−x) = (eq/q)
1
24eπix2
(11)
see for example [2, App.A]. In a certain domain, the Faddeev quantum dilogarithm is given
as a ratio of two Pochhammer symbols
Φb(x) =
(−q
1
2e2πibx; q)∞
(−eq
1
2e2πib−1x; eq)∞
,
(12)
from which it follows that its asymptotic expansion as b →0 is given by replacing the
denominator by 1 and the numerator by the asymptotic expansion of the Pochhammer
symbol.
6
STAVROS GAROUFALIDIS, MATTHIAS STORZER, AND CAMPBELL WHEELER
