---
doc_id: arxiv-1908.07065v3
doc_title: "Prepared for submission to JHEP Non-perturbative approaches to the quantum Seiberg–Witten curve"
section_id: sec-011-51-a-closed-formula-and-its-derivation
section_title: "A closed formula and its derivation"
section_number: 5.1
pages: 30-31
source_pdf: 1908.07065v3.pdf
source_sha256: c43e413aed71aef1
doc_brief: "Non-perturbative approaches to the quantum Seiberg–Witten curve — We study various non-perturbative approaches to the quantization of the Seiberg– Witten curve ofN = 2, SU (2) super Yang–Mills"
---
By using the approach of [2, 18] we ﬁnd the following expression for the spectral determinant of
(2.14)6
Ξ(E) =A(ℏ)
(
sinh
(Πex
A (E, ℏ)
2ℏ
))−1
cosh
( 1
2ℏΠex
B (E, ℏ)
)
, (5.6)
where Πex
A,B(E, ℏ) are given by (4.18) and A(ℏ) is an u-independent constant which can be ﬁxed
from Ξ(0) = 1, namely,
A(ℏ) = sinh
(Πex
A (0, ℏ)
2ℏ
)(
cosh
( 1
2ℏΠex
B (0, ℏ)
))−1
. (5.7)
From this expression we can read oﬀ explicit formulae for the spectral traces. We ﬁnd for instance
Z1 =− 1
2ℏ
(
∂EΠex
B (0, ℏ) tanh
(Πex
B (0, ℏ)
2ℏ
)
− coth
(Πex
A (0, ℏ)
2ℏ
)
∂EΠex
A (0, ℏ)
)
, (5.8)
as well as
4ℏ2Z2 =2ℏ∂2
EΠex
A (0, ℏ) coth
(Πex
A (0, ℏ)
2ℏ
)
− (∂EΠex
A (0, ℏ))2csch2
(Πex
A (0, ℏ)
2ℏ
)
− sech2
(Πex
B (0, ℏ)
2ℏ
)(
ℏ∂2
EΠex
B (0, ℏ) sinh
(Πex
B (0, ℏ)
ℏ
)
+ (∂EΠex
B (0, ℏ))2
)
.
(5.9)
Note that in order to calculate Π ex
A (0, ℏ) we have to use (4.37) or (4.38), so the above formula
tests as well the analytic continuation of instanton calculus beyond the semiclassical region 7.
6While presenting these results at the conference Irregular singularities in Quantum Field Theory
(http://irregular.rd.ciencias.ulisboa.pt/conference), S. Lukyanov informed us that he had independently derived
this result [63] by using completely diﬀerent methods.
7In evaluating the derivative of the periods w.r.t.E, we used the quantum Matone relation (4.14) and instanton
calculus.
– 29 –
The explicit formula (5.6) can be extended to the family of operators considered in [18], see
Appendix A for more details.
Let us now explain how to derive (5.6) from the TS/ST correspondence of [2, 3]. The
relevant CY geometry is the canonical bundle over F0, also known as resolved Y 2,0 singularity.
The corresponding quantum mirror curve is
O−κ = (RΛ)2(ex + e−x)−κ + ep + e−p, [x, p] = iℏ. (5.10)
According to the TS/ST correspondence we have
det(1−κO−1) =
∑
m∈Z
exp [J(µ + iπ + 2πim,R Λ, ℏ)], κ = eµ, (5.11)
where J(µ,ξ, ℏ) is the grand potential of the resolvedY 2,0 singularity as deﬁned in [18], section 5.1.
The expression (5.6) is obtained by implementing the geometric engineering limit [37, 64] in
(5.11). More precisely, we consider the limit
p→Rp, ℏ→Rℏ, κ = 2 +ER2 +O(R3), R → 0. (5.12)
This has to be done carefully since both sides of (5.11) diverge, therefore they need to be properly
regularized. For that it is convenient to study the trace of the resolvent
GO(κ) = d
dκ log det(1−κO−1) = Tr
( 1
κ− O
)
, (5.13)
rather than the spectral determinant. It is easy to see that in the limit (5.12) one has
GO(κ)→ 1
R2G(E), G (E) = Tr
( 1
E− H
)
, (5.14)
where H is the modiﬁed Mathieu operator in (2.14). Likewise the limit (5.12) can be implemented
on the r.h.s of (5.11) in a quite straightforward way by following [18], section 5.2 and by using
the identity (3.9) in [65]. The overall divergent piece R−2 cancels and we ﬁnd
G(E) =−∂Ea
ℏ
(
∂2
aFNS tanh
(∂aFNS
ℏ
)
+π coth
(aπ
ℏ
))
. (5.15)
By integrating w.r.t. E we obtain (5.6), where A(ℏ) is an integration constant.
