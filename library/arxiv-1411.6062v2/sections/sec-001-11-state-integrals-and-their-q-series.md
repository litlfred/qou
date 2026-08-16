---
doc_id: arxiv-1411.6062v2
doc_title: "EV ALUATION OF STATE INTEGRALS AT RATIONAL POINTS"
section_id: sec-001-11-state-integrals-and-their-q-series
section_title: "State-integrals and their q-series"
section_number: 1.1
pages: 1-3
source_pdf: 1411.6062v2.pdf
source_sha256: 5abd328d027de43c
doc_brief: "EVALUATION OF STATE INTEGRALS AT RATIONAL POINTS — Multi-dimensional state-integrals of products of Faddeev’s quant um diloga- rithms arise frequently in Quantum Topology, quantum Teichm¨ uller t"
---
1.2. The Rogers and the cyclic dilogarithms 3
1.3. Evaluation of state-integrals 4
1.4. The quantum dilogarithm at roots of unity 6
Acknowledgments 7
2. Integrals of quasi-periodic functions 7
2.1. Some lemmas from complex analysis 7
2.2. Applications to 1-dimensional state-integrals: proof of Theor em 1.1 10
2.3. The case of the ( −2, 3, 7) pretzel knot 11
3. Proof of Theorem 1.9 13
Appendix A. Some useful properties of the quantum dilogarithm 16
References 16
1. Introduction
1.1. State-integrals and their q-series. State-integrals are multi-dimensional integrals
of products of Faddeev’s quantum dilogarithms. They appear in abu ndance in Quantum
Topology, quantum Teichm¨ uller theory and in complex Chern–Simonstheory. State integrals
were studied among others by Hikami [ Hik01], Dimofte–Gukov–Lennels–Zagier [ DGLZ09],
Date: April 27, 2015.
S.G. was supported in part by grant DMS-0805078 of the US Nationa l Science Foundation. R.K. was
supported in part by the Swiss National Science Foundation.
Key words and phrases: state-integrals, q-series, quantum dilogarithm, cyclic dilogarithm, Rogers diloga-
rithm, quasi-periodic functions, Nahm equation, gluing equations, 4 1, 5 2, (−2,3,7) pretzel knot.
1
2 STA VROS GAROUF ALIDIS AND RINAT KASHAEV
Andersen–Kashaev [
AK14, AK], Kashaev–Luo–Vartanov [ KL V12], Dimofte [ Dim14a] and
Dimofte–Garoufalidis [ Dim14b].
In our previous paper [ GK], we showed how to express 1-dimensional state-integrals as a
ﬁnite sum of products of q-series and ˜q-series with integer coeﬃcients, where the variables q
and ˜q are related by the modular transformation: q = e2πiτ and ˜q = e−2πi/τ .
In this paper we evaluate 1-dimensional state-integrals at rationa l points in terms of the
Rogers dilogarithm, the cyclic (quantum) dilogarithm and truncated state-sums at roots of
unity. Our formulas are syntactically similar with
(a) the constant terms of the power series that appear in the Qua ntum Modularity Con-
jecture of Zagier [ Zag10, GZa],
(b) the 1-loop terms of the perturbation expansion of complex Che rn–Simons theory
[Dim14b],
(c) the state-sums of quantum Teichm¨ uller theory [Kas94, Kas95, Kas97] and also [ BB07,
Sec.6].
This is not a coincidence; it is one part of a story discussed in detail in [ GZb].
In order to keep our principle clear, we focus exclusively on 1-dimens ional state-integrals,
and we illustrate our results for the state-integrals of 4 1, 5 2 and (−2, 3, 7) pretzel knots. In
a separate publication we will discuss the evaluation of multi-dimension al state-integrals.
A 1-dimensional state-integral is an absolutely convergent integr al of the form
(1) IA,B(b) =
∫
/CA +iǫ
Φ b(x)Be−Aπix2
dx
for a complex number b with b2⁄∈/CA
≤0. Here A, B are natural numbers satisfying B > A > 0
and Φ b(x) is Faddeev’s quantum dilogarithm function [ Fad95, FK94]. Few properties of this
special function are reviewed in Appendix A.
A numerical computation by the ﬁrst author and Zagier [ GZb] suggested the following
formula forI1,2(1):
(2) I1,2(1) = eπi/6
√
3
(
e
V
2π − e− V
2π
)
(and more generally for the Taylor coeﬃcients of the analytic funct ionI1,2(b) at b = 1),
where V = 2 Im(Li2(eπi/3)) = 2 . 0298832 . . . is the volume of the 4 1 knot. Understanding and
proving the above identity led to the results of our paper.
Our aim is to evaluate IA,B(b) when b2 = M/N for a pair of coprime natural numbers
M, N . The content of our paper can be summarized in a diagram
{state-integrals} −−−→ { Nahm series}

↓


↓
{evaluations} ←−−− {truncated Nahm series}
The top arrow was the content of our previous article [
GK]. To recall the connection between
state-integrals and q-series, consider the integrand of the state-integral IA,B(b), shifted by
EV ALUATION OF STATE INTEGRALS AT RATIONAL POINTS 3
cb = i(b + b−1)/ 2:
(3) f( x− cb) = Φ b(x)Be−Aπix2
.
The quasi-periodicity of the quantum dilogarithm (see Equations ( 77a)–(77b)) implies that
f(x + imb + inb−1) = f( x) g+
m(e2πbx, q +) g−
n (e2πb−1x, q −)
where q± = e2πib±2
and
(4) g ±
k (x, q ) = (−x)Ak q
A
2 k(k+1)
(qx; q)B
k
.
This gives rise to the series G±(x, q )∈
/CI [ [x, q ] ] deﬁned by
G±(x, q ) =
∞∑
k=0
g±
k (x, q )(5)
The q-series G±(1, q )∈
/CI [ [q] ] are special q-hypergeometric series of Nahm type and appear
in the expression of the state-integral IA,B(b) as a sum of products of q-series and ˜q-series,
where ˜q = 1/q −, see [ GK, Thm.1.1].
Throughout the paper, ( M, N ) will denote an admissible pair, i.e., a pair of coprime
positive integers. Consider the state-sum deﬁned by
GM,N (x+, x −) =
M N−1∑
k=0
g+
kP (x+, ζ M
N ) g−
kQ(x−, ζ N
M )(6)
where P, Q are integers that satisfy the equation M P + N Q = 1 and ζN = e2πi/N . When
xN
+ = xM
− , it follows from Lemma
2.2 that GM,N (x+, x −) is independent of the choice of P
and Q. Observe that
G1,N (x+, x −) = G+
N (x+), G M,1(x+, x −) = G−
M (x−)
where
G±
N (x) =
N −1∑
k=0
g±
k (x, ζ N ) .(7)
