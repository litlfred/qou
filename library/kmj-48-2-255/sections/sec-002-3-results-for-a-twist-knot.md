---
doc_id: kmj-48-2-255
doc_title: "A Formula for the Colored Jones Polynomial of 2-Bridge Knots"
section_id: sec-002-3-results-for-a-twist-knot
section_title: "Results for a twist knot"
section_number: 3
pages: 19-26
source_pdf: KMJ-48-2-255.pdf
source_sha256: 720279042c6d762b
toc_source: inferred
doc_brief: "A Formula for the Colored Jones Polynomial of 2-Bridge Knots — We derive a formula for the colored Jones polynomial of 2-bridge knots."
---
In this section, we will consider the twist knots S(4p1 + 1, 2p1 + 1) and S(4p1 −
1, 2p1 −1).
From Theorem 1, we get explicit formulas for the colored Jones polynomials of
these twist knots.
Corollary 5.
JS(4p1+1,2p1+1)(n)
(14)
=
X
0≤mj−1≤mj≤n−1
q−n P2p1−1
i=1
(−1)imi+Pp1−1
i=1
m2i(1+m2i+1)
×
(¯q)n−1(¯q)mp′
(¯q)n−mp′−1
(−1)mp′


p1−1
Y
j=0
(¯q)m2j+1−m2j
p1
Y
j=1
(q)m2j−m2j−1


−1
,
and
JS(4p1−1,2p1−1)(n)
(15)
=
X
0≤mj−1≤mj≤n−1
qn(−1+P2p1−2
i=1
(−1)imi−2m2p1−1)+1−Pp1−1
i=1
m2i−1(1+m2i)
×
(q)n−1(q)mp′
(q)n−mp′−1
(−1)mp′


p1−1
Y
j=0
(¯q)m2j+1−m2j
p1−1
Y
j=1
(q)m2j−m2j−1


−1
.
Proof. Firstly, let us consider the knot S(4p1 + 1, 2p1 + 1) for p1 ≥1. It is easy to
see that
Lemma 6.(1) σj = (−1)j−1
(2) ik =
(
2p1 + 2 −2k
if 1 ≤k ≤p1
2(k −p1) −1
if p1 + 1 ≤k ≤2p1,
σik =
(
−1
if 1 ≤k ≤p1
1
if p1 + 1 ≤k ≤2p1.
274
Toshie Takata
Lemma 7. (1) σik + σip′+1−k = 0.
(2) σj+1 + σp′+1−j = (−2)j.
From the above lemmas, we obtain
(16)
a(m) = −
2p1−1
X
j=1
(−1)jmj.
We compute b1(m) and b2(m). One calculate
(17)
X
1≤k≤p−t
2
1 −σik
2
mik−1 =
p1
X
j=1
m2j−1,
X
p−t
2 +1≤k≤p′
mik−1 =
p1−1
X
j=1
m2j,
X
p−t
2 +1≤k≤p′
1 + σik
2
mik
(18)
=
X
p1+1≤k≤2p1
mik =
X
p1+1≤k≤2p1
m2k−2p1−1 =
p1
X
j=1
m2j−1
(1 + σp′)mp′ = 0,
(19)
p′−1
X
j=1
(σj+1 −σj)mj = −2
p1
X
j=1
m2j−1 + 2
p1−1
X
j=1
m2j = 2
2p1−1
X
j=1
(−1)jmj.
(20)
Moreover, it follows that k < k′ and σik̸ = σik′ if and only if 1 ≤k ≤p1 and
p1 + 1 ≤k′ ≤2p1. We note that sign(ik −ik′) = 1 if and only if ik > ik′ and that
ik = 2p1 + 2 −2k for 1 ≤k ≤p1 and ik′ = 2k′ −2p1 −1 for p1 + 1 ≤k′ ≤2p1.
So, we obtain
X
1≤k≤p′
X
k+1≤k′≤p′
1 + sign(ik −ik′)
2
(σik −σik′)(mik −mik−1)(mik′ −mik′−1)
=
−2
X
1≤k≤p1
X
p1+1≤k′≤2p1+1−k
(m2p1+2−2k −m2p1+1−2k)(m2k′−2p1−1 −m2k′−2p1−2)
=
−2
X
1≤j≤p1
X
1≤j′≤j
(m2j −m2j−1)(m2j′−1 −m2j′−2),
A Formula for the Colored Jones Polynomial of 2-Bridge Knots
275
and
p′
X
j=1
σj(
r′(j)
X
k=1
(mik −mik−1))mj−1
=
p1
X
j=1
σ2j−1(
r′(2j−1)
X
k=1
(mik −mik−1))m2j−2 +
p1
X
j=1
σ2j(
r′(2j)
X
k=1
(mik −mik−1))m2j−1
=
p1
X
j=1
σ2j−1(
p1+j
X
k=1
(mik −mik−1))m2j−2 +
p1
X
j=1
σ2j(
p1−j+1
X
k=1
(mik −mik−1))m2j−1
=
p1
X
j=1
(
p1
X
k=1
(m2p1+2−2k −m2p1+1−2k) +
p1+j
X
k=p1+1
(m2k−2p1−1 −m2k−2p1−2))m2j−2
−
p1
X
j=1
(
p1−j+1
X
k=1
(m2p1+2−2k −m2p1+1−2k))m2j−1
=
p1
X
j=1
(
p1
X
j′=1
(m2j′ −m2j′−1) +
j
X
j′=1
(m2j′−1 −m2j′−2))m2j−2
−
p1
X
j=1
(
p1
X
j′=j
(m2j′ −m2j′−1))m2j−1
=
p1
X
j=1
(m2j +
p1
X
j′=j+1
(m2j′ −m2j′−1))m2j−2 −
p1
X
j=1
(
p1
X
j′=j
(m2j′ −m2j′−1))m2j−1
=
p1
X
j=1
(
p1
X
j′=j
(m2j′ −m2j′−1) + m2j−1)m2j−2 −
p1
X
j=1
(
p1
X
j′=j
(m2j′ −m2j′−1))m2j−1.
Summing up, we obtain
(21)
b1(m) + b2(m) =
p1−1
X
j=1
m2j(1 + m2j+1).
Next, we consider the knot S(4p1 −1, 2p1 −1) for p1 ≥1. It is not hard to show
the following two lemmas.
Lemma 8. It follows that (1) σj = (−1)j−1, and
(2) ik =
(
2p1 −2k + 1
if 1 ≤k ≤p1,
2(k −p1)
if p1 + 1 ≤k ≤2p1 −1,
σik =
(
1
if 1 ≤k ≤p1,
−1
if p1 + 1 ≤k ≤2p1 −1.
Lemma 9. (1) σik + σip′+1−k =
(
2
if k = p1,
0
if k̸ = p1.
(2) σj+1 + σp′+1−j = 0.
276
Toshie Takata
From these lemmas, it follows that
(22)
a(m) =
2p1−2
X
i=1
(−1)imi −2m2p1−1 −1,
We compute
X
1≤k≤p−t
2
1 −σik
2
mik−1 =
X
1≤k≤p1
1 −σik
2
mik−1 = 0,
(23)
X
p−t
2 +1≤k≤p′
mik−1 =
X
p1+1≤k≤2p1−1
mik−1 =
X
p1+1≤k≤2p1−1
m2k−2p1−1
(24)
=
p1−1
X
j=1
m2j−1,
X
p−t
2 +1≤k≤p′
1 + σik
2
mik =
X
p1+1≤k≤2p1−1
1 + σik
2
mik = 0,
(25)
(1 + σp′)mp′ = 2m2p1−1,
(26)
p′−1
X
j=1
(σj+1 −σj)mj =
2p1−2
X
j=1
(σj+1 −σj)mj = 2
2p1−2
X
i=1
(−1)imi.
(27)
Moreover, it follows that k < k′ and σik̸ = σik′ if and only if 1 ≤k ≤p1 and
p1 + 1 ≤k′ ≤2p1 −1. We note that sign(ik −ik′) = 1 if and only if ik > ik′ and
that ik = 2p1 −2k + 1 for 1 ≤k ≤p1 and ik′ = 2k′ −2p1 for p1 + 1 ≤k′ ≤2p1 −1.
So, we compute
X
1≤k≤p′
X
k+1≤k′≤p′
1 + sign(ik −ik′)
2
(σik −σik′)(mik −mik−1)(mik′ −mik′−1)
=
2
X
1≤k≤p1
X
p1+1≤k′≤2p1−k
(m2p1−2k+1 −m2p1−2k)(m2k′−2p1 −m2k′−2p1−1)
=
2
X
0≤j≤p1−1
X
1≤j′≤j
(m2j+1 −m2j)(m2j′ −m2j′−1),
A Formula for the Colored Jones Polynomial of 2-Bridge Knots
277
and
p′
X
j=1
σj(
r′(j)
X
k=1
(mik −mik−1))mj−1
=
p1
X
j=1
σ2j−1(
r′(2j−1)
X
k=1
(mik −mik−1))m2j−2 +
p1−1
X
j=1
σ2j(
r′(2j)
X
k=1
(mik −mik−1))m2j−1
=
p1
X
j=1
(
p1−j+1
X
k=1
(mik −mik−1))m2j−2 −
p1−1
X
j=1
(
p1−j
X
k=1
(mik −mik−1))m2j−1
=
p1
X
j=1
(
p1−j+1
X
k=1
(m2p1−2k+1 −m2p1−2k))m2j−2
−
p1−1
X
j=1
(
p1
X
k=1
(m2k−2p1+1 −m2k−2p1) +
p1+j
X
k=p1+1
(m2p1−2k −m2p1−2k−1))m2j−1
=
p1
X
j=1
(
p1
X
j′=j
(m2j′−1 −m2j′−2)m2j−2 −
p1−1
X
j=1
(
p1−1
X
j′=1
(m2j′+1 −m2j′) +
j
X
j′=1
(m2j′ −m2j′−1))m2j−1
=
p1
X
j=1
(
p1
X
j′=j
(m2j′−1 −m2j′−2))m2j−2 −
p1−1
X
j=1
(
p1
X
j′=j+1
(m2j′−1 −m2j′−2) + m2j)m2j−1
=
X
0≤j′≤p1−1
X
1≤j≤j′
(m2j′+1 −m2j′)(m2j −m2j−1) −
p1−1
X
j=1
m2jm2j−1.
Thus we obtain
(28)
b1(m) + b2(m) = 1 −
p1−1
X
j=1
m2j−1(1 + m2j).
□
Using Corollary 5, we give explicit formulas for the trefoil knot S(3, 1) and the
ﬁgure eight knot S(5, 3).
By the formula (15) with p1 = 1 and p′ = 1, we get
JS(3,1)(n)
=
X
0≤m1≤n−1
(q)n−1(q)m1(−1)m1
(q)n−m1−1(¯q)m1
qn(−1−2m1)+1
=
X
0≤m1≤n−1
(¯qn−1 −1) · · · (¯qn−m1 −1)(−1)m1qn(−1−m1)+1.
278
Toshie Takata
By the formula (14) with p1 = 1 and p′ = 1,
JS(5,3)(n) =
X
0≤m1≤m2≤n−1
(¯q)n−1(¯q)m2
(¯q)n−m2−1(¯q)m1(q)m2−m1
qnm1(−1)m2,
and using the formula
k
X
i=0
(q)k
(q)k−i(¯q)i
q−i
2 (k+b+1) =
k
Y
j=1
(1 −q−1
2 (k+b+1−2j)),
we obtain a formula of K. Habiro [2] or T. T. Q. Le as follows,
JS(5,3)(n) =
X
0≤m≤n−1
(q)n−1(q)n+m
(q)n(q)m(q)n−m−1
q−nm.
Finally, as an application of Corollary 5, we estimate the maximal and minimal
degree of JK(n) for a twist knot K. We denote by deg+(JK(n)) and deg−(JK(n))
the maximal degree and the minimal degree in q of JK(n) ∈Z[q±1] respectively,
and let br(JK(n)) = deg+(JK(n)) −deg−(JK(n)). From Corollary 5, we obtain
Corollary 10. For K = S(4p1 + 1, 2p1 + 1),
deg+(JK(n)) = 1
2n(n −1)(2p1),
deg−(JK(n)) = −n(n −1),
(29)
br(JK(n)) = 1
2n(n −1)(2p1 + 2),
and for K = S(4p1 −1, 2p1 −1),
deg+(JK(n)) = −n + 1,
deg−(JK(n)) = −n2 + 1 −1
2n(n −1)(2p1 −1),
(30)
br(JK(n)) = 1
2n(n −1)(2p1 + 1).
Thus, it follows that for K = S(4p1 + 1, 2p1 + 1) or K = S(4p1 −1, 2p1 −1),
(31)
br(JK(n)) = 1
2n(n −1)C(K),
where C(K) is the crossing number of K.
Proof. From Corollary 5, we obtain
JS(4p1+1,2p1+1)(n)
=
X
0≤mj−1≤mj≤n−1
q−n P2p1
i=1(−1)imi+ 1
2
P2p1−1
i=1
mi(1+mi)(−1)
P2p1
i=1 mi
×(qn−1 −1) · · · (qn−mp′ −1)
2p1
Y
j=2
(q)mj
(q)mj−1(q)mj−mj−1
.
A Formula for the Colored Jones Polynomial of 2-Bridge Knots
279
Notice that the maximal degree in q of
(q)a
(q)b(q)a−b
is b(a−b) and the minimal degree
is 1. Noting that
−n(n −1)
≤
n(m1 +
p1−1
X
i=1
(m2i+1 −m2i) −m2p1) + 1
2
2p1−1
X
i=1
mi(1 + mi) +
2p1
X
j=2
mj−1(mj −mj−1)
=
−n
p1−1
X
i=1
l2i −1
2
2p1−1
X
i=1
(mi −mi+1)2 + 1
2
2p1−1
X
i=1
m2
i+1 + 1
2
2p1−1
X
i=1
mi
≤
1
2n(n −1)(2p1 −1),
and
0 ≤1
2m2p1(2n −1 −m2p1) ≤1
2n(n −1),
it follows that the term with mi = n −1 contributes to deg+(JK(n)) and the term
with mi = 0 (i̸ = p′) and mp′ = n −1 to deg−(JK(n)). So, the formula (29) holds.
Similarly, from Corollary 5,
JS(4p1−1,2p1−1)(n)
=
X
0≤mj−1≤mj≤n−1
qn(−1+P2p1−1
i=1
(−1)imi)+1−1
2
P2p1−2
i=1
mi(1+mi)(−1)
P2p1−1
i=1
mi
×(¯qn−1 −1) · · · (¯qn−mp′ −1)
2p1−1
Y
j=2
(¯q)mj
(¯q)mj−1(¯q)mj−mj−1
.
Since
−n + 1
≥
n(−1 −m1 −
p1−1
X
i=1
(m2i+1 −m2i)) + 1 −1
2
2p1−2
X
i=1
mi(1 + mi+1) −
2p1−1
X
j=2
mj−1(mj −mj−1)
=
n(−1 −
p1
X
i=1
l2i−1 + 1) + 1
2
2p1−2
X
i=1
(mi −mi−1)2 −1
2
2p1−2
X
i=1
m2
i+1 −1
2
2p1−2
X
i=1
mi
≥
−n2 + 1 −1
2n(n −1)(2p1 −2),
and
0 ≥−1
2(2n −1 −m2p1+1)m2p1+1 ≥−1
2n(n −1),
the term with mi = 0 contributes to deg+(JK(n)) and the term with mi = n −1
(i̸ = p′) and mp′ = n −1 to deg−(JK(n)). Thus, we get the formula (30).
Moreover, since S(4p1 + 1, 2p1 + 1) (resp. S(4p1 −1, 2p1 −1)) is given in the
Conway notation by C(2p1, 2) (resp. C(2p1 −1, 2)), the equality (31) holds.
□
280
Toshie Takata
Remark 11. Recently, Le proved that the equality (31) holds for any non-trivial
alternating knot (see Proposition 2.1 of [6]).
Acknowledgment. We would like to thank the referee for many helpful comments.
