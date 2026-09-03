---
doc_id: arxiv-1501.01574v3
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL"
section_id: sec-009-32-cables-of-knots-of-period-at-most-2
section_title: "Cables of knots of period at most 2"
section_number: 3.2
pages: 10-14
source_pdf: 1501.01574v3.pdf
source_sha256: 8af5d6264a0ad5e0
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL — We study the behavior of the degree of the colored Jones polyn omial and the boundary slopes of knots under the operation of cabling."
---
period at most two. Examples of such knots include all the ade quate knots and the torus
knots. We show that, under a mild hypothesis satisﬁed by all t he known examples, the
property of having period at most two is preserved under cabl ing (Proposition 3.2). As a
result, if a knot K ⊂ S3 satisﬁes the Slope Conjecture and π(K) ≤ 2, then all but at most
two cables of K also satisfy the conjecture.
Proposition 3.2. Let K be a knot such that for n ≫ 0 we have
d+[JK (n)] = a(n)n2 + b(n)n + d(n)
is a quadratic quasi-polynomial of period ≤ 2, with b(n) ≤ 0.
Suppose p
q /∈ {4a(n)}. Then for n ≫ 0 we have
d+[JKp,q(n)] = A(n)n2 + B(n)n + D(n)
is a quadratic quasi-polynomial of period ≤ 2, with {A(n)} ⊂
(
{q2a(n)} ∪ { pq/4}
)
and
B(n) ≤ 0.
Proof. Since d+[JK (n)] is a quadratic quasi-polynomial of period ≤ 2, for n ≫ 0 we can
write
d+[JK (n)] =
{
a0n2 + b0n + d0 if n is even ,
a1n2 + b1n + d1 if n is odd .
11
Recall that Kp,q is the ( p, q)-cable of a knot K, where p, q are coprime integers and |q| >
1. It is known that K−p, −q = rKp,q , where rKp,q denotes Kp,q with the opposite orientation,
and that the colored Jones polynomial of a knot is independent of the orientation of the
knot. Hence, without loss of generality, we will assume that q > 1.
For n > 0, let Sn be the set of all k such that
|k| ≤ (n − 1)/2 and k ∈
{
Z if n is odd ,
Z + 1
2 if n is even .
By [33], for n > 0 we have
(3) JKp,q(n) = vpq(n2−1)/ 4 ∑
k∈Sn
v−pk(qk+1)JK (2qk + 1),
where it is understood that JK(−m) = −JK(m).
In the above formula, there is a sum. Under the assumption of t he proposition, we will
show that there is a unique term of the sum whose highest degre e is strictly greater than
those of the other terms. This implies that the highest degre e of the sum is exactly equal
to the highest degree of that unique term.
Let S +
n = {k ∈ Sn | k ≥ 0} and S −
n = {k ∈ Sn | k ≤ − 1
2}. For k ∈ S n let
f (k) = d+[v−pk(qk+1)JK (2qk + 1)].
Let g±
i (x), for i ∈ {0, 1}, be the quadratic real polynomials deﬁned by
g±
i (x) = ( −pq + 4q2ai)x2 + (−p + 4qai ± 2qbi)x + ai ± bi + di.
For k ∈ Sn we have f (k) = −pk(qk + 1) + d+[JK (|2qk + 1|)], which gives
f (k) =



g+
0 (k) if k ∈ S +
n and 2 qk + 1 is even ,
g−
0 (k) if k ∈ S −
n and 2 qk + 1 is even ,
g+
1 (k) if k ∈ S +
n and 2 qk + 1 is odd ,
g−
1 (k) if k ∈ S −
n and 2 qk + 1 is odd .
Case 1. Suppose that q is even. For k ∈ S n, since 2 qk + 1 is odd we have
f (k) =
{
g+
1 (k) if k ∈ S +
n ,
g−
1 (k) if k ∈ S −
n .
Subcase 1.1. Assume that p/q < 4a1.
Since −pq + 4 q2a1 > 0, the quadratic polynomial g+
1 (x) is concave up. Hence, for
n ≫ 0, g+
1 (k) is maximized on S +
n at k = (n − 1)/2. Similarly, g−
1 (k) is maximized on S −
n
at k = (1 − n)/2. Note that
g+
1
(
(n − 1)/2
)
− g−
1
(
(1 − n)/2
)
= (−p + 4qa1)(n − 1) + 2b1 > 0
12
for n ≫ 0. Hence f (k) is maximized on the set Sn at k = (n − 1)/2. Since f
(
(n − 1)/2
)
=
g+
1
(
(n − 1)/2
)
, equation (3) then implies that
d+[JKp,q(n)] = pq(n2 − 1)/4 + g+
1
(
(n − 1)/2
)
= q2a1n2 +
(
qb1 + (q − 1)(p − 4qa1)/2
)
n
+ a1(q − 1)2 − (b1 + p/2)(q − 1) + d1
for n ≫ 0. Since we assumed that q > 1, we have that B(n) = qb1 +(q −1)(p−4qa1)/2 < 0,
and the conclusion follows in this case.
Subcase 1.2. Assume that p/q > 4a1.
Since −pq + 4q2a1 < 0, the quadratic polynomial g+
1 (x) is concave down and attains its
maximum at
x = x0 := −
( 1
2q + b1
−p + 4qa1
)
.
Since b1 ≤ 0, we have x0 < 0. This implies that g+
1 (x) is a strictly decreasing function on
[0, ∞). Similarly, g−
1 (x) is a strictly increasing function on ( −∞, − 1
2 ].
First suppose n is even. Then k ∈ Z + 1
2 . In this subcase, g+
1 (k) is maximized on
S +
n at k = 1
2 and g−
1 (k) is maximized on S −
n at k = − 1
2 . Note that g+
1 ( 1
2 ) − g−
1 (− 1
2 ) =
(−p+4qa1)+2b1 < 0. Hence f (k) is maximized on Sn at k = −1/2. Since f (− 1
2 ) = g−
1 (− 1
2 ),
equation (3) then implies that
d+[JKp,q(n)] = pq(n2 − 1)/4 + g−
1 (−1/2)
for even n ≫ 0. Similarly, for odd n ≫ 0 we obtain
d+[JKp,q(n)] = pq(n2 − 1)/4 + g+
1 (0).
Note that B(n) = 0 in this case.
Case 2. Suppose that q is odd. As in Case 1 we have the following.
Subcase 2.1. Suppose that n is even.
For k ∈ S n, we have k ∈ Z + 1
2 and 2 qk + 1 is even. Hence f (k) =
{
g+
0 (k) if k ∈ S +
n ,
g−
0 (k) if k ∈ S −
n .
If p/q < 4a0 then f (k) is maximized on Sn at k = (n − 1)/2. Hence
d+[JKp,q(n)] = pq(n2 − 1)/4 + g+
0
(
(n − 1)/2
)
= q2a0n2 +
(
qb0 + (q − 1)(p − 4qa0)/2
)
n
+ a0(q − 1)2 − (b0 + p/2)(q − 1) + d0.
In this case we have B(n) = qb0 + (q − 1)(p − 4qa0)/2 < 0.
If p/q > 4a0 then f (k) is maximized on Sn at k = −1/2. Hence
d+[JKp,q(n)] = pq(n2 − 1)/4 + g−
0 (−1/2).
Note that B(n) = 0 in this case.
Subcase 2.1. Suppose that n is odd.
13
For k ∈ S n, we have k ∈ Z and 2 qk + 1 is odd. Hence f (k) =
{
g+
1 (k) if k ∈ S +
n ,
g−
1 (k) if k ∈ S −
n .
If p/q < 4a1 then f (k) is maximized on Sn at k = (n − 1)/2. Hence
d+[JKp,q(n)] = pq(n2 − 1)/4 + g+
1
(
(n − 1)/2
)
= q2a1n2 +
(
qb1 + (q − 1)(p − 4qa1)/2
)
n
+ a1(q − 1)2 − (b1 + p/2)(q − 1) + d1.
In this case we have B(n) = qb1 + (q − 1)(p − 4qa1)/2 < 0.
If p/q > 4a1 then f (k) is maximized on Sn at k = 0. Hence
d+[JKp,q(n)] = pq(n2 − 1)/4 + g+
1 (0).
Note that B(n) = 0 in this case.
This completes the proof of Proposition 3.2. □
Remark 3.3. (1) Proposition 3.2 generalizes [29, Lemma 2.2], [28, Lemma 2.2], [31,
Lemma 3.1] and [32, Lemma 3.2].
(2) When π(K) is greater than 2 then determining the highest degree of JKp,q(n) in
Equation (3) becomes harder as there might be more opportuni ties for cancellation between
terms. This case will be discussed in Section 4.
Proposition 3.2 and Theorem 2.2 imply the following.
Theorem 3.4. Let K be a knot such that for n ≫ 0 we have
d+[JK (n)] = a(n)n2 + b(n)n + d(n)
is a quadratic quasi-polynomial of period ≤ 2, with b(n) ≤ 0.
Suppose p
q /∈ jsK . Then for n ≫ 0 we have
d+[JKp,q(n)] = A(n)n2 + B(n)n + D(n)
is a quadratic quasi-polynomial of period ≤ 2, with B(n) ≤ 0. Moreover, if jsK ⊂ bsK we
have jsKp,q ⊂ bsKp,q.
Similarly, let K be a knot such that for n ≫ 0 we have
d−[JK (n)] = a∗(n)n2 + b∗(n)n + d∗(n)
is a quadratic quasi-polynomial of period ≤ 2, with b∗(n) ≥ 0. Suppose p
q /∈ js∗
K . Then for
n ≫ 0 we have
d−[JKp,q(n)] = A∗(n)n2 + B∗(n)n + D∗(n)
is a quadratic quasi-polynomial of period ≤ 2, with B∗(n) ≥ 0. Moreover, if js∗
K ⊂ bsK
we have js∗
Kp,q ⊂ bsKp,q.
Proof. The ﬁrst part of the theorem follows immediately by Proposit ion 3.2 and Theorem
2.2. To obtain the second part recall that if K ∗ denotes the mirror image of K then JK ∗(n)
is obtained from JK(n) by replacing the variable v with v−1. Now the result will follow
by applying Proposition 3.2 and Theorem 2.2 to K ∗. □
14
Figure 1. From left to right: A crossing, the A-resolution and the the B-resolution.
Figure 2. From left to right: An example link diagram, the graph Gσ
corresponding to state surface Sσ . Figure borrowed from [7].
