---
doc_id: arxiv-1104.0755v2
doc_title: "A connection formula between the Ramanujan function and the q-Airy function"
section_id: sec-001-2-standard-notations
section_title: "Standard notations"
section_number: 2
pages: 4-6
source_pdf: 1104.0755v2.pdf
source_sha256: d2fbbea44598e8f4
doc_brief: "A connection formula between the Ramanujan function and the q-Airy function — We show a connection formula between two diﬀerent q-Airy func- tions."
---
In this section, we ﬁx our notations. We assume that q ∈ C∗ satisﬁes
0< |q|< 1. We deﬁne the q-Pochhammer symbol (a;q)n.
Deﬁnition 1 For any n ∈ Z≥0,
(a;q)n =
{
1, n = 0,
(1 −a)(1 −aq) · · ·(1 −aqn−1), n ≥ 1,
and
(a;q)∞ = lim
n→∞
(a;q)n.
Moreover,
(a1,a 2, · · ·,a m;q)∞ = (a1;q)∞(a2;q)∞ · · · (am;q)∞.
The q-diﬀerence operator σq is given by σqf (x) = f (qx). The basic
hypergeometric series rϕ s is deﬁned as follows.
Deﬁnition 2 The basic hypergeometric series is given by
rϕ s(a1, · · ·,a r;b1, · · ·,b s;q,x ) :=
∑
n≥0
(a1, · · ·,a r;q)n
(b1, · · ·,b s;q)n(q;q)n
[
(−1)nq
n(n− 1)
2
] 1+s−r
xn.
We deﬁne the theta function of Jacobi. We denote by θq(x) or more
shortly θ(x). The theta function of Jacobi is given by following series;
Deﬁnition 3 For any x ∈ C∗,
θq(x) = θ(x) =
∑
n∈Z
q
n(n− 1)
2 xn.
4
The theta function has some important properties. The following lem ma is
called Jacobi’s triple product identity.
Lemma 1 For any x ∈ C∗, we have
θ(x) =
(
q, −x, −q
x ;q
)
∞
.
The theta function satisﬁes the following q-diﬀerence relation.
Lemma 2 For any k ∈ Z,θ (x) satisﬁes
θ(qkx) = q− k(k− 1)
2 x−kθ(x), ∀x ∈ C∗.
From lemma2 , we remark that the function θ(−λx)/θ (λx), ∀λ ∈ C∗ satisﬁes
a q-diﬀerence equation
u(qx) = −u(x)
which is also satisﬁed by the function u(x) = eπi( log x
log q ). From the deﬁnition,
the theta function has the following inversion formula.
Lemma 3 For any x ∈ C∗ , one gets
xθ
(1
x
)
=θ(x).
3 Two types of the q-analogue of the Airy
function
There are two diﬀerent q-analogue of the Airy function. One is called the
Ramanujan function which appears in [9]. Ismail [6] pointed out that t he
Ramanujan function can be considered as a q-analogue of the Airy function.
The other one is called the q-Airy function which is obtained by K. Kajiwara,
T. Masuda, M. Noumi, Y. Ohta and Y. Yamada [7] . In this section, we s ee
the properties of these functions. We explain the reason why they are called
q-analogue of the Airy function and we show q-diﬀerence equations which
they satisfy.
5
