---
doc_id: arxiv-1411.6062v2
doc_title: "EVALUATION OF STATE INTEGRALS AT RATIONAL POINTS"
section_id: sec-011-appendix-a-some-useful-properties-of-the-quantum
section_title: "Appendix A. Some useful properties of the quantum dilogarithm"
section_number: null
pages: 16-16
source_pdf: 1411.6062v2.pdf
source_sha256: 5abd328d027de43c
toc_source: outline
doc_brief: "EVALUATION OF STATE INTEGRALS AT RATIONAL POINTS — Multi-dimensional state-integrals of products of Faddeev’s quantum diloga- rithms arise frequently in Quantum Topology, quantum Teichm¨uller theory"
---
The quantum dilogarithm Φb(x) is deﬁned by [Fad95]
(75)
Φb(x) = (e2πb(x+cb); q)∞
(e2πb−1(x−cb); ˜q)∞
,
where
q = e2πib2,
˜q = e−2πib−2,
cb = i
2(b + b−1),
Im(b2) > 0.
An integral representation is given by
Φb(x) = exp
Z
R+iǫ
e−2ixz
4 sinh(zb) sinh(zb−1)
dz
z

in the strip |Imz| < |Imcb|. Remarkably, this function admits an extension to all values of b
with b2̸ ∈R≤0. Φb(x) is a meromorphic function of x with
poles: cb + iNb + iNb−1,
zeros: −cb −iNb −iNb−1 .
The functional equation
Φb(x) Φb(−x) = eπix2 Φb(0)2,
Φb(0) =
q
˜q
 1
48
= eπi(b2+b−2)/24
allows us to move Φb(x) from the denominator to the numerator of the integrand of a state-
integral.
The asymptotics of the quantum dilogarithm are given by [AK14, App.A]
(76)
Φb(x) ∼
(
Φb(0)2eπix2
when
ℜ(x) ≫0
1
when
ℜ(x) ≪0
The quantum dilogarithm is a quasi-periodic function. Explicitly, it satisﬁes the equations
Φb(x + cb + ib)
Φb(x + cb)
=
1
1 −qe2πbx
(77a)
Φb(x + cb + ib−1)
Φb(x + cb)
=
1
1 −˜q−1e2πb−1x .
(77b)
