---
doc_id: arxiv-math-0403224v1
doc_title: "Difference equation of the colored Jones polynomial for torus knot"
section_id: page-004
section_title: "Page 4"
section_number: null
pages: 4-4
source_pdf: 0403224v1.pdf
source_sha256: c25ccba77da375ad
toc_source: undetermined
doc_brief: "Difference equation of the colored Jones polynomial for torus knot — 7 sections: Page 1; Page 2; Page 3"
---
4
KAZUHIRO HIKAMI
This proposition simpliﬁes the diﬀerence equation of the colored Jones
polynomial JK(N) for K = T2,2m+1 as follows;
Theorem 6. The N-colored Jones polynomial for the torus knot T2,2m+1
solves the diﬀerence equation of the ﬁrst order;
JT2,2m+1(N) = qm(1−N) 1 −q1−2N
1 −q−N −qm−(2m+1)N 1 −q1−N
1 −q−N JT2,2m+1(N −1)
(9)
This recursion relation coincides with a result in Ref. 5 for the trefoil
m = 1 (we need to replace q with q−1). We remark that in Ref. 7 by a dif-
ferent approach proposed was the diﬀerence equation of the colored Jones
polynomial for the torus knot T2,2m+1, which is much involved.
3. A-P
In Ref. 5 the “AJ conjecture” is proposed; the homogeneous diﬀerence
equation of the colored Jones polynomial JK(N) for knot K gives the A-
polynomial AK(L, M) for knot K. More precisely we rewrite the diﬀerence
equation of the colored Jones polynomial, P
k≥0 ak JK(N + k) = 0, into a
form, AK(E, Q; q) JK(N) ≡P
k≥0 ak(Q, q) Ek JK(N) = 0, where the opera-
tors Q and E act on JK(N) as
E JK(N) = JK(N + 1)
Q JK(N) = qN JK(N)
Then a claim of Ref. 5 is that the A-polynomial AK(L, M) coincides with
AK(L, M) = AK(L, M2; q = 1)
(10)
This AJ conjecture was checked with a help of Mathematica package for
trefoil, ﬁgure-eight knots [5], and for 52, 61 knots [21].
For our case of the torus knot Ts,t, we can easily check that applying
above procedure the diﬀerence equations (7) and (9) reproduce the A-polynomial
for the torus knots given in Ref. 23 (see also Refs. 3,20);
ATs,t(L, M) =

(L −1) (−1 + L2 M2st)
for s, t > 2
(L −1) (1 + L M2(2m+1))
for (s, t) = (2, 2m + 1)
We can thus conclude that
Theorem 7. AJ conjecture (10) proposed in Ref. 5 is true for the torus knots
K = Ts,t.
4.
q-HFCJP
At the end of this article, we comment on an explicit form of the colored
Jones polynomial for the torus knot. Recalling a result of Ref. 9, we see
that the colored Jones polynomial for the torus knot T2,2m+1 can be written
in a form of the q-hypergeometric function.
