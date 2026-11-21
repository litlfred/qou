---
doc_id: arxiv-math-0005296v1
doc_title: "An example concerning Ohtsuki’s invariant and the full SO(3) quautum invariant"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-3
source_pdf: 0005296v1.pdf
source_sha256: 1714653ecfdf01bc
toc_source: inferred
doc_brief: "An example concerning Ohtsuki’s invariant and the full SO(3) quautum invariant — Two lens spaces are given to show that Ohtsuki’s τ for rational homology spheres does not determine Kirby-Melvin’s {τ"
---
arXiv:math/0005296v1  [math.QA]  31 May 2000
An example concerning Ohtsuki’s invariant and the full
SO(3) quautum invariant ∗
Bang-He Li & Tian-Jun Li
Abstract
Two lens spaces are given to show that Ohtsuki’s τ for rational homology spheres
does not determine Kirby-Melvin’s {τ
′
r, r odd ≥3}
By using partial Kirby-Melvin’s quautum SO(3) invariants {τ
′
r(M), r odd prime >
|H1(M, Z)|} [KM], Ohtsuki [O] deﬁned a topological invariant
τ(M) =
∞
X
n=0
λn(M)(t −1)n ∈Q[[t −1]]
for rational homology 3-sphere M. R.Lawrence [La] conjectured that
λn(M) ∈
(
Z,
if |H1(M, Z)| = 1
Z[1
2,
1
|H1(M,Z)|],
if |H1(M, Z)| > 1
and if r is an odd prime which does not divide |H1(M, Z)|, then {|H1(M, Z)|}rτ
′
r(M) is
the r−adic limit of the series
∞
X
n=0
λ
√
n (M)hn
where {·}r stands for the Jacobi symbol, and h = e
2πi
r −1.
Rozansky [R] has proved that this conjecture is true. So τ(M) and {τ
′
r, r odd prime
not dividing |H1(M, Z)|} determine each other.
A natural question arises: Does τ determine all {τ
′
r, r odd ≥3}?
It was proved in [Li] that τ
′
r(M) = τ
′
r(M′) iﬀξr(M, A) = ξr(M′, A) for r odd ≥3,
where A is any r−th primitive root of unit. So the question is equivalent to: Does τ(M)
determine all ξr(M, er)? Where, ea stands for e
2πi
a .
∗The ﬁrst author is supported partially by the National Science Foundation of P. R. China, the second
author is supported partially by NSF grant DMS 9304580
1
For lens space L(p, q), all ξr(L(p, q), er) has been obtained in [LL1] ( explicit formulas
for τ
′
r(L(p, q)) were given in [LL2]), that is: let r ≥3 be odd and c = (p, r) the common
factor, then
(1) ξr(L(p, q), er) =



























{p}re−12s(q,p)
r
er′(q+q∗)
p
e2p
′
r
−e−2p
′
r
e2r −e−2
r
,
if c = 1
(−1)
r−1
2
c−1
2 {p/c}r/c{q}ce−12s(q,p)
r
e(r/c)
′(q+q∗−ηp∗p)
pc
e−2η(p/c)
′
rc
ǫ(c)√cη
e−2
r
−e2r
,
if c > 1 , c | q∗+ η
0,
if c > 1 and c |/q∗± 1
where η = 1 or −1, p∗p + q∗q = 1 with 0 < q∗< p, (p/c)
′p/c + (r/c)′r/c = 1, s(p, q) is the
Dedekind sum, and
ǫ(c) =
 1,
if c ≡1
(mod 4)
i,
if c ≡−1
(mod 4)
Since
τ(L(p, q)) = t−3s(q,p)t
1
2p −t−1
2p
t
1
2 −t−1
2
([O] and [LL2]), τ(L(p1, q1)) = τ(L(p2, q2)) iﬀp1 = p2 and s(q1, p1) = s(q2, p2).
The
following Theorem answers the question above.
Theorem.
s(6, 25) = s(11, 25), while ξr(L(25, 11)) = ξr(L(25, 6)) if and only if
(r, 25)̸ = 5.
Proof. We calculate s(q, p) by the formula in [H]:
12s(q, p) =
n
X
i=1
mi + q + q∗
p
−3n
if p
q = mn −
1
mn−1 −· · · −
1
m2 −1
m1
with mi ≥2.
Now
25
6 = 5 −
1
2 −
1
2 −
1
2 −
1
2 −1
2
,
25
11 = 3 −
1
2 −
1
2 −
1
3 −1
2
11∗= 16, 6∗= 21, so
12s(6, 25) = 12s(11, 25) = −3 + 27
25
2
c = (r, 25) can be only 1, 5 or 25. If c = 25, then c |/6∗± 1 and c |/11∗± 1, thus by (1)
ξr(L(25, 11), er) = ξr(L(25, 6), er) = 0. If c = 1, it is easy to see from (1) that the two ξr
are equal.
Assume c = 5, then c|6∗−1 and 11∗−1. Now since q∗q + p∗p = 1, we have
q + q∗+ (25)∗× 25 =
 27 + 125,
if q = 6
27 + 175,
if q = 11
Therefore, by (1)
ξr(L(25, 11), er)
ξr(L(25, 6), er) = e(r/5)
′×50
125
Since (p/c)
′p/c + (r/c)′r/c = 1, we see that (r/5)
′ is prime to (p/5) = 5. This shows that
e(r/5)
′×50
125̸
= 1, and the theorem is proved.
