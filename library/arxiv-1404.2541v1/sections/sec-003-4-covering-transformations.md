---
doc_id: arxiv-1404.2541v1
doc_title: "The Stokes phenomenon for the Ramanujan’s q-diﬀerence equation and its higher order extension Takeshi MORITA∗"
section_id: sec-003-4-covering-transformations
section_title: "Covering transformations"
section_number: 4
pages: 11-13
source_pdf: 1404.2541v1.pdf
source_sha256: edb7c9b2b1561ac3
doc_brief: "The Stokes phenomenon for the Ramanujan’s q-difference equation and its higher order extension Takeshi MORITA∗ — We show connection formulae of local solutions of the Ramanu - jan equation between"
---
We deﬁne a covering transformation for a second order linear q-diﬀerence
equation.
Deﬁnition 4.1. For a q-diﬀerence equation
a(x)u(q2x) +b(x)u(qx) +c(x)u(x) = 0, (9)
we deﬁne the covering transformation as follows
t2 :=x, v (t) := u(t2), p := √
q.
The covering transform of the equation (9) is given by
a(t2)v(p2t) +b(t2)v(pt) +c(t2)v(t) = 0.
By the covering transformation, the equation
(
K ·xσ 2
q −σq + 1
)
u(x) = 0
is transformed to (
K ·t2σ 2
p −σp + 1
)
v(t) = 0, (10)
where K is a ﬁxed constant in C∗.
5 The Ramanujan function and the q-Airy
function
There are two diﬀerent q-analogue of the Airy function. One is called the
Ramanujan function which appears in [12]. Ismail [6] pointed out that the
Ramanujan function can be considered as a q-analogue of the Airy function.
The other one is called the q-Airy function which is obtained by K. Kajiwara,
T. Masuda, M. Noumi, Y. Ohta and Y. Yamada [8]. In this section, we
see the properties of these functions. We explain the reason why t hey are
called q-analogues of the Airy function and we show q-diﬀerence equations
which they satisfy.The Ramanujan function appears in Ramanujan’s “Lost
notebook” [12]. Ismail has pointed out that the Ramanujan functio n can be
11
considered as a q-analogue of the Airy function. The Ramanujan function is
deﬁned by following convergent series;
Aq(x) :=
∑
n≥0
qn2
(q;q)n
(−x)n = 0ϕ 1(−; 0;q, −qx).
In the theory of ordinary diﬀerencial equations, the term Planche rel-
Rotach asymptotics refers to asymptotics around the largest an d smallest
zeros. With x = √2n + 1 − 2
1
2 3
1
3n
1
6t and for t ∈ C, the Plancherel-Rotach
asymptotic formula for Hermite polynomials Hn(x) is
lim
n→+∞
e− x2
2
3
1
3π − 3
4 2
n
2 + 1
4
√
n!
Hn(x) = Ai(t). (11)
In [6], Ismail shows the q-analogue of (11);
Proposition 5.1. We have
lim
n→∞
qn2
tn hn(sinhξn|q) = A q
( 1
t2
)
whereeξn =tq− n
2 .
Here,hn(·|q) is the q-Hermite polynomial. In this sense, we can deal with
the Ramanujan function A q(x) as a q-analogue of the Airy function. The
Ramanujan function satisﬁes the following q-diference equation;
(
qxσ 2
q −σq + 1
)
u(x) = 0. (12)
Remark. We remark that another solution of the equation (12) is given by
u(x) = θ(x)2ϕ 0(0, 0; −;q, −x/q ).
Here,
2ϕ 0
(
0, 0; −;q, −x
q
)
=
∑
n≥0
1
(q;q)n
{
(−1)nq
n(n− 1)
2
} −1(
−x
q
) n
is a divergent series.
12
The q-Airy function is found by K. Kajiwara, T. Masuda, M. Noumi,
Y. Ohta and Y. Yamada [8], in their study of the q-Painlev´ e equations. This
function is the special solution of the second q-Painlev´ e equations and given
by the following series
Aiq(x) :=
∑
n≥0
1
(−q,q ;q)n
{
(−1)nq
n(n− 1)
2
}
(−x)n = 1ϕ 1(0; −q;q, −x).
T. Hamamoto, K. Kajiwara, N. S. Witte [4] proved following asymptot ic
expansions;
Proposition 5.2. With q =e− δ 3
2 , x = −2ie− s
2 δ2
as δ → 0,
1ϕ 1(0; −q;q, −qx) = 2π
1
2δ− 1
2e−( πi
δ 3 ) ln 2+( πi
2δ )s+ πi
12
[
Ai
(
se
πi
3
)
+O(δ2)
]
,
1ϕ 1(0; −q;q,qx ) = 2π
1
2δ− 1
2e−( πi
δ 3 ) ln 2−( πi
2δ )s− πi
12
[
Ai
(
se− πi
3
)
+O(δ2)
]
for s in any compact domain of C.
Here, Ai(x) is the Airy function. From this proposition, we can regard
the q-Airy function as a q-analogue of the Airy function.
We can easily check out that the q-Airy function satisﬁes the second order
linear q-diﬀerence equation
(
σ 2
q +xσq − 1
)
u(x) = 0. (13)
Another solution of the equation (13) is given by
u(x) = eπi( log x
log q )1ϕ 1(0; −q;q,x ) = eπi( log x
log q ) Aiq(−x).
