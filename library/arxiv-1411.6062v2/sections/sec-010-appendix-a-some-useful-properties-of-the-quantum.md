---
doc_id: arxiv-1411.6062v2
doc_title: "EV ALUATION OF STATE INTEGRALS AT RATIONAL POINTS"
section_id: sec-010-appendix-a-some-useful-properties-of-the-quantum
section_title: "Appendix A. Some useful properties of the quantum dilogarithm"
section_number: null
pages: 16-16
source_pdf: 1411.6062v2.pdf
source_sha256: 5abd328d027de43c
doc_brief: "EVALUATION OF STATE INTEGRALS AT RATIONAL POINTS — Multi-dimensional state-integrals of products of Faddeev’s quant um diloga- rithms arise frequently in Quantum Topology, quantum Teichm¨ uller t"
---
The quantum dilogarithm Φ b(x) is deﬁned by [ Fad95]
(75) Φ b(x) = (e2πb(x+cb); q)∞
(e2πb−1(x−cb); ˜q)∞
,
where
q = e2πib2
, ˜q = e−2πib−2
, c b = i
2 (b + b−1), Im(b2) > 0.
An integral representation is given by
Φ b(x) = exp
(∫
R+iǫ
e−2ixz
4 sinh(zb) sinh(zb−1)
dz
z
)
in the strip |Imz| <|Imcb|. Remarkably, this function admits an extension to all values of b
with b2⁄∈R≤0. Φ b(x) is a meromorphic function of x with
poles: cb + i/C6 b + i/C6 b−1, zeros: − cb− i/C6 b− i/C6 b−1 .
The functional equation
Φ b(x) Φ b(−x) = eπix2
Φ b(0)2, Φ b(0) =
(q
˜q
) 1
48
= eπi(b2+b−2)/24
allows us to move Φ b(x) from the denominator to the numerator of the integrand of a sta te-
integral.
The asymptotics of the quantum dilogarithm are given by [ AK14, App.A]
(76) Φ b(x)∼
{
Φ b(0)2eπix2
when ℜ(x)≫ 0
1 when ℜ(x)≪ 0
The quantum dilogarithm is a quasi-periodic function. Explicitly, it satis ﬁes the equations
Φ b(x + cb + ib)
Φ b(x + cb) = 1
1− qe2πbx(77a)
Φ b(x + cb + ib−1)
Φ b(x + cb) = 1
1− ˜q−1e2πb−1x .(77b)
