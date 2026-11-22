---
doc_id: arxiv-math-0403224v1
doc_title: "Difference equation of the colored Jones polynomial for torus knot"
section_id: page-003
section_title: "Page 3"
section_number: null
pages: 3-3
source_pdf: 0403224v1.pdf
source_sha256: c25ccba77da375ad
toc_source: undetermined
doc_brief: "Difference equation of the colored Jones polynomial for torus knot — 7 sections: Page 1; Page 2; Page 3"
---
DIFFERENCE EQUATION OF THE COLORED JONES POLYNOMIAL FOR TORUS KNOT3
Proof of Theorem 1. We ﬁrst prove for a case of N being even. We have
stN
X
k=0
χ2st(s t N −k) q
k2−(st−s−t)2
4st
=
stN
X
k=0
χ2st(k) q
k2−(st−s−t)2
4st
=
N
2 −1
X
k=0

qk(stk+st−s−t) −q(sk+s−1)(tk+1) −q(sk+1)(tk+t−1) + q(k+1)(stk+s−1)
=
N
2 −1
X
k=−N
2

qk(stk+st−s−t) −q(sk+s−1)(tk+1)
In the second equality, we have substituted a non-zero value of the periodic
function χ2st(k). In the last equality, we have replaced k with −k −1 in both
the third and the fourth terms in a parenthesis. By further replacing k with
k −1
2 in the last expression and comparing with an explicit form given in
eq. (5), we get an assertion of the theorem.
For a case of N being odd, we can prove it in a same manner.
□
Proposition 3. Let the function Ks,t(N) be deﬁned by eq. (3). Then it satis-
ﬁes the following diﬀerence equation;
Ks,t(N) = 1 −qs(1−N)−1 −qt(1−N)−1 + q(s+t)(1−N) + qst(2−N)−s−t Ks,t(N −2) (6)
Proof. We decompose a sum in eq. (3) into Pst(N−2)
k=0
+ PstN
k=st(N−2). From the
ﬁrst sum we obtain Ks,t(N −2). The second sum can be written explicitly as
what appeared in eq. (6) using a property of χ2st(k).
□
As we have obtained a relationship between the colored Jones polynomial
JTs,t(N) and Ks,t(N), it is straightforward to obtain a following theorem.
Theorem 4. The N-colored Jones polynomial for the torus knot Ts,t fulﬁlls
a recursion relation of the second order;
JTs,t(N) = q
1
2 (s−1)(t−1)(1−N)
1 −q−N

1 −qs(1−N)−1 −qt(1−N)−1 + q(s+t)(1−N)
+ 1 −q2−N
1 −q−N qst(1−N)−1 JTs,t(N −2)
(7)
We should note that this diﬀerence equation can be directly derived by
use of Morton’s expression (5). A beneﬁt of our expression (4) is in reduc-
ing the diﬀerence equation (7) into the ﬁrst order diﬀerence equation in a
case of T2,2m+1.
Proposition 5 (see e.g. Ref. 9). The function K2,2m+1(N) satisﬁes the diﬀer-
ence equation of the ﬁrst order,
K2,2m+1(N) = 1 −q1−2N −q2m(1−N)−N K2,2m+1(N −1)
(8)
Proof. We note that the function χ8m+4(n) has an anti-periodicity, χ8m+4(n +
4m + 2) = −χ8m+4(n). Then a proof follows in a same method with that of
eq. (6).
□
