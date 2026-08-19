---
doc_id: arxiv-1105.1998v3
doc_title: ""
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 1105.1998v3.pdf
source_sha256: daf3bffad8eb2749
doc_brief: "A Connection Formula of the Hahn–Exton q-Bessel Function Takeshi MORITA — We show a connection formula of the Hahn–Exton q-Bessel function around the origin and the infinity."
---
In this paper, we show a connection formula of the Hahn–Exton q-Bessel function J (3)
ν (x; q). At
first, we review the Bessel function and q-analogues of the Bessel function. The Bessel equation
d2u
dz2 + 1
z
du
dz +
(
1 − ν2
z2
)
u = 0
has a solution u(z) = Jν (z), J− ν (z). Here, the Bessel function Jν (z) is
Jν (z) = 1
Γ( ν + 1)
(z
2
)ν
0F1
(
−, ν + 1, − z2
4
)
.
The degenerated confluent hypergeometric function 0F1(−, α, z ) is defined by
0F1(−, α, z ) =
∑
n≥ 0
1
(α )nn! zn, (α )n = α {α + 1} · · · {α + (n − 1)}.
Both Jν (z) and J− ν (z) are linearly independent if ν ⁄∈Z.
It is known that there exists three different q-analogues of the Bessel function.
J (1)
ν (x; q) := (qν+1; q)∞
(q; q)∞
(x
2
)ν
2ϕ 1
(
0, 0; qν+1; q, − x2
4
)
, |x| < 2,
J (2)
ν (x; q) := (qν+1; q)∞
(q; q)∞
(x
2
)ν
0ϕ 1
(
−; qν+1; q, − qν− 1x2
4
)
, x ∈ C,
J (3)
ν (x; q) := (qν+1; q)∞
(q; q)∞
xν 1ϕ 1
(
0; qν+1; q, qx 2)
, x ∈ C.
Here,
(a; q)n :=
{
1, n = 0,
(1 − a)(1 − aq) · · · (1 − aqn− 1), n ≥ 1,
2 T. Morita
(a; q)∞ = lim
n→∞
(a; q)n
and
(a1, a 2, . . . , a m; q)∞ = (a1; q)∞ (a2; q)∞ · · ·(am; q)∞ .
Moreover, the basic hypergeometric series rϕ s is
rϕ s(a1, . . . , a r; b1, . . . , b s; q, x ) :=
∑
n≥ 0
(a1, . . . , a r; q)n
(b1, . . . , b s; q)n(q; q)n
[
(−1)nq
n(n− 1)
2
] 1+s− r
xn.
The first and the second one are called Jackson’s first and se cond q-Bessel function and the
third one is called the Hahn–Exton q-Bessel function. They satisfy the following q-difference
equations:
J (1)
ν : u(xq) −
(
qν/ 2 + q− ν/ 2)
u(xq1/ 2) +
(
1 + x2
4
)
u(x) = 0 ,
J (2)
ν :
(
1 + qx2
4
)
u(xq) −
(
qν/ 2 + q− ν/ 2)
u
(
xq1/ 2)
+ u(x) = 0 ,
J (3)
ν : u(xq) −
{
(qν/ 2 + q− ν/ 2) − q− ν/ 2+1x2
}
u
(
xq1/ 2)
+ u(x) = 0 . (1)
The limits of these q-analogues of the Bessel function are the Bessel function wh en q → 1− :
lim
q→ 1−
J (k)
ν ((1 − q)x; q) = Jν (x), k = 1, 2
and
lim
q→ 1−
J (3)
ν ((1 − q)x; q) = Jν (2x).
The relation between J (1)
ν (x; q) and J (2)
ν (x; q) was found by Hahn [3] as follows:
J (2)
ν (x; q) =
(
− x2
4 ; q
)
∞
J (1)
ν (x; q). (2)
Connection problems of the q-difference equation between the origin and the infinity ar e
studied by G.D. Birkhoff [1]. We review connection formulae for several q-difference functions.
1. Watson’s formula. In 1910 [6], Watson showed the connecti on formula of the basic hyper-
geometric function 2ϕ 1 as follows:
2ϕ 1 (a, b ; c; q; x) = (b, c/a ; q)∞ (ax, q/ax ; q)∞
(c, b/a ; q)∞ (x, q/x ; q)∞
2ϕ 1 (a, aq/c ; aq/b ; q; cq/abx )
+ (a, c/b ; q)∞ (bx, q/bx ; q)∞
(c, a/b ; q)∞ (x, q/x ; q)∞
2ϕ 1 (b, bq/c ; bq/a ; q; cq/abx ) .
2. Connection formula of J (1)
ν (x; q). C. Zhang has given some connection formulae for the
solutions of the q-difference equations of confluent type [7, 8] and [9]. In [8 ], Zhang
has shown connection formulae for J (1)
ν (x; q) and J (2)
