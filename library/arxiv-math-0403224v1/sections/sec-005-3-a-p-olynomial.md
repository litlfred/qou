---
doc_id: arxiv-math-0403224v1
doc_title: "DIFFERENCE EQUATION OF THE COLORED JONES POLYNOMIAL FOR TORUS KNOT KAZUHIRO HIKAMI"
section_id: sec-005-3-a-p-olynomial
section_title: "A-P olynomial"
section_number: 3
pages: 4-6
source_pdf: 0403224v1.pdf
source_sha256: c25ccba77da375ad
doc_brief: "DIFFERENCE EQUATION OF THE COLORED JONES POLYNOMIAL FOR TORUS KNOT KAZUHIRO HIKAMI — We prove that the N-colored Jones polynomial for the torus knot Ts, t satisﬁes the second order diﬀerence"
---
In Ref. 5 the “AJ conjecture” is proposed; the homogeneous diﬀerence
equation of the colored Jones polynomial JK(N) for knot K gives the A-
polynomial AK(L, M) for knot K. More precisely we rewrite the diﬀerence
equation of the colored Jones polynomial, ∑
k≥0 ak JK(N + k) = 0, into a
form, AK(E, Q; q) JK(N) ≡ ∑
k≥0 ak(Q, q) Ek JK(N) = 0, where the opera-
tors Q and E act on JK(N) as
E JK(N) = JK(N + 1)
Q JK(N) = qN JK(N)
Then a claim of Ref. 5 is that the A-polynomial AK(L, M) coincides with
AK(L, M) = AK(L, M2; q = 1) (10)
This AJ conjecture was checked with a help of Mathematica package for
trefoil, ﬁgure-eight knots [5], and for 52, 61 knots [21].
For our case of the torus knot Ts, t, we can easily check that applying
above procedure the diﬀerence equations (7) and (9) reproduce the A-polynomial
for the torus knots given in Ref. 23 (see also Refs. 3, 20);
ATs, t(L, M) =









(L − 1) (−1 + L2 M2st) for s, t > 2
(L − 1) (1 + L M2(2m+1)) for ( s, t) = (2, 2m + 1)
We can thus conclude that
Theorem 7. AJ conjecture (10) proposed in Ref. 5 is true for the torus knots
K = Ts, t.
4. q-Hypergeometric Function and Colored Jones Polynomial
At the end of this article, we comment on an explicit form of the colored
Jones polynomial for the torus knot. Recalling a result of Re f. 9, we see
that the colored Jones polynomial for the torus knot T2, 2m+1 can be written
in a form of the q-hypergeometric function.
DIFFERENCE EQUATION OF THE COLORED JONES POLYNOMIAL FOR TOR US KNOT5
Hereafter we use a standard notation of the q-product and the q-binomial
coeﬃcient (see e.g. Ref. 1);
(x)n = (x; q)n =
n∏
k=1
(1 − x qk−1)
[
n
m
]
q
= (q)n
(q)n−m (q)m
Theorem 8 ( [9]). Let the function H2, 2m+1(x) be deﬁned by
H2, 2m+1(x) =
∞∑
km≥···≥k2≥k1≥0
(x)km+1 xkm







m−1∏
i=1
qki(ki+1) x2ki
[
ki+1
ki
]
q






 (11)
for |q| < 1 and |x| < 1. Then we have
H2, 2m+1(x) =
∞∑
n=0
χ8m+4(n) q
n2−(2m−1)2
8(2m+1) x
n−(2m−1)
2 (12)
and it satisﬁes
H2, 2m+1(x) = 1 − q x2 − q2m x2m+1 H2, 2m+1(q x) (13)
For m = 1 case, see also Ref. 1 [Chap. 2, p. 29] and Ref. 22.
With an expression (11), we can take a limit x → q−N; an inﬁnite sum
terminates into a ﬁnite sum due to (q−N)k = 0 for k > N. Comparing eq. (8)
with eq. (13) we obtain the colored Jones polynomial for the t orus knot
T2, 2m+1 as follows;
Proposition 9. The N-colored Jones polynomial for the torus knot T2, 2 m+1
is given by
JT2, 2m+1(N) = qm(1−N)
∞∑
km≥···≥k2≥k1≥0
(q1−N)km q−Nkm







m−1∏
i=1
qki(ki+1−2N)
[
ki+1
ki
]
q







(14)
We see that the colored Jones polynomial for the trefoil m = 1 coincides
with results in Refs. 8,13. It should be remarked that in Ref. 15 constructed
was the colored Jones polynomial for the twist knot, which gives a diﬀerent
expression of the colored Jones polynomial for the trefoil. By applying a
twisting formula given in Ref. 15, we have another expression of the colored
Jones polynomial in the form of cyclotomic expansion in a sense of Ref. 8
as follows;
