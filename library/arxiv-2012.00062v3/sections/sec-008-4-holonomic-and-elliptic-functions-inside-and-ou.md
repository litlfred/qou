---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-008-4-holonomic-and-elliptic-functions-inside-and-ou
section_title: "Holonomic and elliptic functions inside and outside the unit disk"
section_number: 4
pages: 24-25
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
---
An important property for the functions of a complex variableq in our paper (such as the
holomorphic blocks considered below) is that they can be deﬁned both inside (|q|< 1) and
outside(|q|> 1)theunitdisk, insuchawaythattheyhavethesameannihilatorideal. Recall
that ifL and M denote the operators that act on functionsf(x;q) by (Lf)(x;q) =f(qx;q)
and (Mf )(x;q) = xf(x;q), then LM = qML, hence L−1M = q−1ML−1. It follows that
if P (L,M,q )f(x;q) = 0 , then P (L−1,M,q −1)f(x;q−1) = 0 where P (L,M,q ) denotes a
polynomial inL with coeﬃcients polynomials inM and q.
A ﬁrst example of a function to consider is(x;q)∞ =∏∞
j=0(1−qjx), which is well-deﬁned
for|q|< 1 and x∈ C and satisﬁes the linearq-diﬀerence equation
(1−x)(qx;q)∞ = (x;q)∞ (|q|< 1). (106)
We can extend it to a meromorphic function ofx when|q|> 1 (by a slight abuse of notation)
by deﬁning
(x;q−1)∞ := (qx;q)−1
∞ (|q|< 1), (107)
so that Equation (106) holds for|q|⁄ = 1. Our second example is the theta function
θ(x;q) = (−q
1
2x;q)∞(−q
1
2x−1;q)∞ (|q|< 1) (108)
which satisﬁes the linearq-diﬀerence equation
θ(qx;q) =q− 1
2x−1θ(x;q) ( |q|< 1) (109)
and can be extended toθ(x;q−1) = θ(x;q)−1 when|q|> 1 so that Equation (109) holds for
|q|⁄ = 1. θ(x;q) is a meromorphic function ofx∈ C ∗ with the following (simple) zeros and
(simple) poles
|q|< 1 zeros(θ) =−q
1
2 +Z poles(θ) =∅ (110)
|q|> 1 zeros(θ) =∅ poles(θ) =−q
1
2 +Z .
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 25
An important property of the theta functions is that they factorize the exponentials of a
quadratic and linear form ofu. This fact is a consequence of the modular invariance of the
theta function and was used extensively in the study of holomorphic blocks [BDP14].
Lemma 13.For integersr and s we have:
eπi(u+rcb)2
= e−πi
12 (τ+τ−1)θ((−q
1
2 )rx;q)θ((−˜q− 1
2 )r˜x; ˜q−1) (111a)
eπiru2+2πiscbu = ise
πi
12 (3s−r)(τ+τ−1)θ(x;q)r−sθ(−q
1
2x;q)s×θ(˜x; ˜q−1)r−sθ(−˜q− 1
2 ˜x; ˜q−1)s (111b)
for integersr and s.
Note that we the above factorization formulas are by no means unique, and this is a
reﬂection of the dependence of the above formulas on a theta divisor.
Proof. When x = e2πbu, q =e(τ), ˜q =e(−1/τ) and|q|< 1, then we claim
e− 1
4πiτ (logx)2
= eπiu2
= Φb(0)−2Φb(u)Φb(−u) = e−πi
12 (τ+τ−1)θ(x;q)θ(˜x; ˜q−1). (112)
Theﬁrstequalityiseasy, thesecondonefollowsfromtheinversionformulaofFaddeev’squan-
tum dilogarithm, and the third one follows from the product expansion of Faddeev’s quantum
dilogarithm or from the modular invariance of the theta function. Note also thatΦb(0)2 =
(q/˜q)
1
24 = e
πi
12 (τ+τ−1). Equation (111a) follows easily from the above and Equation (111b)
follows from the above using for example,eπiru2+2πiscbu = e(r−s)πiu2
esπi(u+cb)2
e−sπic2
b. □
