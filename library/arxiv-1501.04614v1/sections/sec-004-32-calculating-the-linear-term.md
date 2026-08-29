---
doc_id: arxiv-1501.04614v1
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL II"
section_id: sec-004-32-calculating-the-linear-term
section_title: "Calculating the linear term"
section_number: 3.2
pages: 10-13
source_pdf: 1501.04614v1.pdf
source_sha256: ebebcae0c1823217
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL II — We continue our study of the degree of the colored Jones polyn omial under knot cabling started in [8]."
---
Theorem 3.3. For the 2-fusion knot K = K(m1, m 2), with m2 /∈ {−1, 0}, we have
bK (n) =



m2(1−m1)
2(−1+m1+m2) if (m1, m 2) ∈ I1 ∪ I2,
1 + m1 if (m1, m 2) ∈ I3,
m1(m2−1)
2(1+m1+m2) if (m1, m 2) ∈ I4,
5/ 2 + m1 + 3m2 if (m1, m 2) ∈ I5,
(−5+2m1)(1+m2)
2(−1+2m1+2m2) if (m1, m 2) ∈ I6 and −1+(1+m2)(n−1)
−1+2m1+2m2
/∈ Z,
(−3+2m1)(1+m2)
2(−1+2m1+2m2) if (m1, m 2) ∈ I6 and −1+(1+m2)(n−1)
−1+2m1+2m2
∈ Z.
In particular we have bK(n) ≤ 0. Moreover bK(n) = 0 if and only if m1 ∈ { 0, 1} and
m2 ≥ 1, or (m1, m 2) = ( −1, 1).
Proof. As in the previous subsection, there are 3 cases.
Case A. m1, m 2 ≥ 1. Recall that
c1 = 1 − m1 + m2 + m2n
2(−1 + m1 + m2)
and k1 is one of the integers closest to c1 satisfying k1 ≤ n
2 . We have
δK (n) = Q(n, k 1, −k1) = (1 − m1 − m2)k2
1 + (1 − m1 + m2 + m2n)k1
+ 2m1n + 4m2n + m1n2 + 2m2n2 + n
2 + n2
2 .
Write k1 = c1 + rn where rn is a periodic sequence with
{
|rn| ≤ 1/ 2 if m1 ≥ 2,
rn ∈ {−1/ 2, −1} if m1 = 1.
We have
δK (n) = Q(n, c 1 + rn, −c1 − rn) = Q(n, c 1, −c1) + (1 − m1 − m2)r2
n
and
Q(n, c 1, −c1) = 2 m1n + 4m2n + m1n2 + 2m2n2 + n
2 + n2
2 − (1 − m1 + m2 + m2n)2
4(1 − m1 − m2)
=
(
m1 + 2m2 + 1
2 + m2
2
4(−1 + m1 + m2)
)
n2
+
(
2m1 + 4m2 + 1
2 + m2(1 − m1 + m2)
2(−1 + m1 + m2)
)
n − (1 − m1 + m2)2
4(1 − m1 − m2) .
Since d+[JK (n)] = δK (n − 1) + (n − 1)/ 2 we obtain
d+[JK (n)] =
(
m1 + 2m2 + 1
2 + m2
2
4(−1 + m1 + m2)
)
n2 + m2(1 − m1)
2(−1 + m1 + m2) n
−
(
m1 + 2m2 + 1
2 − (1 − m1)2
4(−1 + m1 + m2)
)
+ (1 − m1 − m2)r2
n−1.
11
Case B. m1 ≤ 0, m 2 ≥ 1. There are 2 subcases.
(B-1) (1 + m1 + m2 ≤ 0) or (1 + m1 + m2 > 0 and 1 + 2 m1 + m2 < 0). Then
δK (n) = Q(n, n, 0) =
(1
2 + 2m2
)
n2 +
(3
2 + m1 + 4m2
)
n.
Hence
d+[JK (n)] =
(1
2 + 2m2
)
n2 + (1 + m1)n −
(3
2 + m1 + 2m2
)
.
(B-2) 1 + m1 + m2 > 0 and 1 + 2 m1 + m2 ≥ 0. Recall that
c2 = 1 − m1 − m2 + (1 + m2)n
2(1 + m1 + m2)
and k1 is one of the integers closest to c2. We have
δK (n) = Q(n, k 1, k 1 − n) = ( −1 − m1 − m2)k2
1 + (1 − m1 − m2 + (1 + m2)n)k1
+ 2m1n + 5m2n + m1n2 + 2m2n2 + n
2 + n2
2 .
Write k1 = c2 + rn where rn is a periodic sequence with |rn| ≤ 1/ 2. As in Case A we have
δK (n) = Q(n, c 2, c 2 − n) + (−1 − m1 − m2)r2
n
and
Q(n, c 2, c 2 − n) = 2 m1n + 5m2n + m1n2 + 2m2n2 + n
2 + n2
2 − (1 − m1 − m2 + (1 + m2)n)2
4(−1 − m1 − m2)
=
(3
4 + 3m1
4 + 9m2
4 + m2
1
4(1 + m1 + m2)
)
n2
+
(
1 + 2m1 + 9m2
2 − m1
1 + m1 + m2
)
n − (1 − m1 − m2)2
4(−1 − m1 − m2) .
Hence
d+[JK (n)] =
(3
4 + 3m1
4 + 9m2
4 + m2
1
4(1 + m1 + m2)
)
n2 + m1(m2 − 1)
2(1 + m1 + m2) n
−
(3
4 + 3m1
4 + 9m2
4 − (m2 − 1)2
4(1 + m1 + m2)
)
+ (−1 − m1 − m2)r2
n.
Case C. m2 ≤ −2. There are 2 subcases.
(C-1) m1 ≤ −3m2/ 2. Then
δK (n) = Q(n, n, n ) = (2 + m1 + 3m2)n.
Hence
d+[JK (n)] = (5 / 2 + m1 + 3m2)(n − 1).
(C-2) m1 > −3m2/ 2. Recall that
c3 = −3/ 2 + m1 + m2 + (1 + m2)n
1 − 2m1 − 2m2
12
and let k1 be one of the integers closest to c3. We have
δK (n) =
{
Q(n, k 1, k 1) if c3 /∈ 1
2 + Z
Q(n, k 1, k 1) − (c3 + 1/ 2) if c3 ∈ 1
2 + Z
and
Q(n, k 1, k 1) = (1 / 2 − m1 − m2) k2
1 − (−3/ 2 + m1 + m2 + (1 + m2)n) k1
+ 2m1n + 4m2n + m1n2 + 2m2n2 + n
2 + n2
2 .
Write k1 = c3 + rn where rn is a periodic sequence with |rn| ≤ 1/ 2. As in Case A we
have
Q(n, k 1, k 1) = Q(n, c 3, c 3) + (1/ 2 − m1 − m2) r2
n
and
Q(n, c 3, c 3) = 2 m1n + 4m2n + m1n2 + 2m2n2 + n
2 + n2
2 − (−3/ 2 + m1 + m2 + (1 + m2)n)2
4(1/ 2 − m1 − m2)
= (2m1 + 3m2)2
2(−1 + 2m1 + 2m2) n2 +
(1
2 + 2m1 + 9m2
2 + −3 + 2m1
2(−1 + 2m1 + 2m2)
)
n
− (−3/ 2 + m1 + m2)2
4(1/ 2 − m1 − m2) .
Hence
d+[JK (n)] = (2m1 + 3m2)2
2(−1 + 2m1 + 2m2) n2 +



(−5+2m1)(1+m2)
2(−1+2m1+2m2) n if −1+(1+m2)(n−1)
−1+2m1+2m2
/∈ Z
(−3+2m1)(1+m2)
2(−1+2m1+2m2) n if −1+(1+m2)(n−1)
−1+2m1+2m2
∈ Z
−
(
1
2 + m1 + 2m2 − (2m1 − 5)2
8(2m1 + 2m2 − 1)
)
+ (1/ 2 − m1 − m2) r2
n−1.
This completes the proof of Theorem 3.3. □
The proof of Theorem 3.3 implies the following.
Lemma 3.4. For the 2-fusion knot K = K(m1, m 2) we have
M1 =
{
0 if (m1, m 2) /∈ I6,
1+m2
−1+2m1+2m2
if (m1, m 2) ∈ I6,
and
max{0, M 2} =



(1−m1+m2)2
4(m1+m2−1) if (m1, m 2) ∈ I1,
3m2/ 4 if (m1, m 2) ∈ I2,
0 if (m1, m 2) ∈ I3,
max
{ m1+m2−1
4 + m1(m2−1)
m1+m2+1 , 0
}
if (m1, m 2) ∈ I4,
0 if (m1, m 2) ∈ I5,
max
{ 2m1+2m2−1
8 + (2m1−6)(m2+1)
2m1+2m2−1 , 0
}
if (m1, m 2) ∈ I6.
13
3.3. Proof of Theorem 3.1. Theorem 3.3 implies that Conjecture 1.2 holds true for
2-fusion knots: The fact that bK(n) ≤ 0 is clear by the statement of Theorem 3.3. This,
together with Theorem 3.2, proves Theorem 3.1 part (1). More over, bK (n) = 0 if and only
if m1 ∈ { 0, 1} and m2 ≥ 1, or ( m1, m 2) = ( −1, 1). As noted in [5] we have K(1, m 2) =
K ∗(0, −m2 − 1). On the other hand, by deﬁnition the knot K(0, m 2) is a torus knot.
Finally K(−1, 1) is the torus knot T (2, 5). Thus if bK (n) = 0, and K = K(m1, m 2),
then K is a torus knot. By combining Theorem 1.1, Theorem 3.2 and Lem ma 3.4 we get
Theorem 3.1 part (2). □
Example 3.5. Consider the 2-fusion knot K(m, 1), also known as the ( −2, 3, 2m + 3)-
pretzel knot. It is known that K(m, 1) is B–adequate if m ≤ − 2 and is A–adequate if
m ≥ − 1. Moreover K(m, 1) is a torus knot if |m| ≤ 1, and K(−2, 1) is the twist knot 5 2
which is an adequate knot. Hence we consider the two cases m ≥ 2 and m ≤ −3 only.
Note that K(m1, m 2) is the mirror image of K(1− m1, −1− m2). In particular, K(m, 1)
is the mirror image of K(1 − m, −2).
Case 1: m ≥ 2. From the proof of Theorem 3.3 we have
d+[JK(m, 1)(n)] =
(5
2 + m + 1
4m
)
n2 +
( 1
2m − 1
2
)
n −
(
3 + 3m
4 − 1
4m
)
− mr2
n−1
where rn is a periodic sequence with |rn| ≤ 1/ 2.
Hence, by Corollary 1.4, the ( p, q )-cable of K(m, 1) satisﬁes Conjectures 1.2 and 1.3 if
p −
(
10 + 4m + 1
m
)
q < 0 or p −
(
10 + 4m + 1
m
)
q > m
4 + 1
m − 1.
Case 2: m ≤ −3. From the proof of Theorem 3.3 we have
d+[JK(1−m, −2)(n)] = − 2(m + 2)2
2m + 3 n2 + b(n)n + (6m + 17)/ 8 + (m + 3/ 2)r2
n−1
where rn is a periodic sequence with |rn| ≤ 1/ 2, and b(n) =



− 1
2 if (2 m + 3) ∤ n,
− 2m+1
2(2m+3) if (2 m + 3) | n.
Hence, by Corollary 1.4, the ( p, q )-cable of K(1 − m, −2) = ( K(m, 1))∗ satisﬁes Con-
jectures 1.2 and 1.3 if
p+
(
10 + 4m + 1
2m + 3
)
q < 0 or p+
(
10 + 4m + 3
2m + 3
)
q > −
(m
4 + 1
2m + 3 + 11
8
)
.
