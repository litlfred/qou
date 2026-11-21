---
doc_id: 1-s20-s0097316524000426-main
doc_title: "Proof of a conjecture of Ballantine and Merca on truncated sums of 6-regular partitions"
section_id: sec-002-2-proofs-of-theorem-13-and-corollary-14
section_title: "Proofs of Theorem 1.3 and Corollary 1.4"
section_number: 2
pages: 3-9
source_pdf: 1-s2.0-S0097316524000426-main.pdf
source_sha256: 76a8ab857163aa09
toc_source: outline
doc_brief: "Proof of a conjecture of Ballantine and Merca on truncated sums of 6-regular partitions — Article history: In 2012, Andrews and Merca proved a truncated theorem on Received 27 December 2023 Euler’s"
---
In order to prove Conjecture 1.1, we need a formula of p3(n) due to Cayley [5], where 
p3(n) denotes the number of partitions of n into parts not exceeding 3. The generating 
function of p3(n) is
4
O.X.M. Yao / Journal of Combinatorial Theory, Series A 206 (2024) 105903
∞

n=0
p3(n)qn =
1
(1 −q)(1 −q2)(1 −q3).
(2.1)
It is well-known that if n is a nonnegative integer, then
p3(n) =
(n + 3)2
12

,
(2.2)
where < N > denotes the nearest integer of N. It follows from (2.2) that if n ∈N, then
(n + 3)2
12
−1
3 ≤p3(n) ≤(n + 3)2
12
+ 1
4.
(2.3)
We ﬁrst prove two lemmas.
Lemma 2.1. Let m0 ≥1, k ≥1 and n ≥6(m0 −1)2 + 6k(m0 −1) + 11(m0 −1) + 5k + 5
be integers. We have
G(n, k, m0) ≥−m0n
3
−5
2m0 + m0k2 −1
6m0k + 3m2
0k + 2m3
0,
(2.4)
where G(n, k, m0) is deﬁned by
G(n, k, m0) :=
m0−1

j=0
(p3(n −6j2 −6kj −j) −p3(n −6j2 −6kj −5j −2k −1)
−p3(n −6j2 −6kj −7j −3k −2) + p3(n −6j2 −6kj −11j −5k −5)).
(2.5)
Proof. In view of (2.2) and (2.3),
G(n, k, m0) =
m0−1

j=0

(n −6j2 −6kj −j + 3)2
12

−
(n −6j2 −6kj −5j −2k + 2)2
12

−
(n −6j2 −6kj −7j −3k + 1)2
12

+
(n −6j2 −6kj −11j −5k −2)2
12


≥
m0−1

j=0

(n −6j2 −6kj −j + 3)2
12
−1
3
−(n −6j2 −6kj −5j −2k + 2)2
12
−1
4
−(n −6j2 −6kj −7j −3k + 1)2
12
−1
4
O.X.M. Yao / Journal of Combinatorial Theory, Series A 206 (2024) 105903
5
+(n −6j2 −6kj −11j −5k −2)2
12
−1
3

=
m0−1

j=0

k2 + 17
6 k −1
2 −n
3 + (6k + 6)j + 6j2

= −m0n
3
−5
2m0 + m0k2 −1
6m0k + 3m2
0k + 2m3
0,
as desired. This completes the proof of this lemma.
Thoughout this paper, we alway set G(n, k, 0) = 0 which satisﬁes (2.4).
Lemma 2.2. Let k ≥1 and n ≥0 be integers and deﬁne
F(n, k) :=
∞

j=0
(p3(n −6j2 −6kj −j) −p3(n −6j2 −6kj −5j −2k −1)
−p3(n −6j2 −6kj −7j −3k −2) + p3(n −6j2 −6kj −11j −5k −5)).
(2.6)
If (n, k) ̸= (11, 1), then
F(n, k) ≥1.
(2.7)
In addition, F(11, 1) = 0.
Proof. Note that
N =

j≥0
{n|6j2 + 6kj + j ≤n ≤6(j + 1)2 + 6k(j + 1) + j}.
Thus, for any nonnegative integer n, there exists a unique nonnegative integer m0 such 
that 6m2
0 + 6m0k + m0 ≤n ≤6(m0 + 1)2 + 6(m0 + 1)k + m0. We break our proof into 
four cases.
Case 1: 6m2
0 + 6m0k + m0 ≤n ≤6m2
0 + 6m0k + 5m0 + 2k.
If m0 = 0, then
F(n, k) = p3(n) ≥1.
If k = 1 and 1 ≤m0 ≤3, then 13 ≤n ≤89, we can check that F(n, 1) ≥1 with 
Maple.
If k = 1 with m0 ≥4 or k ≥2 with m0 ≥1, then
F(n, k) =G(n, k, m0) + p3(n −6m2
0 −6m0k −m0)
(by (2.5) and (2.6))
≥G(n, k, m0) + (n −6m2
0 −6m0k −m0 + 3)2
12
−1
3
(by (2.3))
6
O.X.M. Yao / Journal of Combinatorial Theory, Series A 206 (2024) 105903
≥1
12n2 −

m0k −1
2 + 1
2m0 + m2
0

n + 5
12 −3m0 + 4m2
0k + 6m3
0k + 3m2
0k2
−35
12m2
0 + 3m3
0 + 3m4
0 −19
6 m0k + m0k2
(by (2.4))
≥−1
3 −3
2m0 + m0k2 + m2
0k −2
3m2
0 −1
6m0k
≥1.
(2.8)
Therefore, if 6m2
0 + 6m0k + m0 ≤n ≤6m2
0 + 6m0k + 5m0 + 2k, then
F(n, k) ≥1.
Case 2: 6m2
0 + 6m0k + 5m0 + 2k + 1 ≤n ≤6m2
0 + 6m0k + 7m0 + 3k + 1.
In view of (2.5) and (2.6),
F(n, k) = G(n, k, m0) + p3(n −6m2
0 −6m0k −m0)
−p3(n −6m2
0 −6m0k −5m0 −2k −1)
= G(n, k, m0) +
(n −6m2
0 −6m0k −m0 + 3)2
12

−
(n −6m2
0 −6m0k −5m0 −2k + 2)2
12

(by (2.2))
≥

−m0n
3
−5
2m0 + m0k2 −1
6m0k + 3m2
0k + 2m3
0

+

(n −6m2
0 −6m0k −m0 + 3)2
12
−1
3

−

(n −6m2
0 −6m0k −5m0 −2k + 2)2
12
+ 1
4

(by (2.3) and (2.4))
=

k
3 + 1
6 + m0
3

n −1
6 −k2
3 + 2k
3 −4m0
3
−m0k2 −3m2
0k −3m2
0 −2m3
0 −17m0k
6
≥m2
0k + m0k2 + m0k
2
+ k2
3 + 4k
3 −m2
0
3 −m0
6
≥1.
Case 3: 6m2
0 + 6m0k + 7m0 + 3k + 2 ≤n ≤6m2
0 + 6m0k + 11m0 + 5k + 4.
It follows from (2.5) and (2.6) that
F(n, k) = G(n, k, m0) + p3(n −6m2
0 −6m0k −m0)
O.X.M. Yao / Journal of Combinatorial Theory, Series A 206 (2024) 105903
7
−p3(n −6m2
0 −6m0k −5m0 −2k −1)
−p3(n −6m2
0 −6m0k −7m0 −3k −2)
= G(n, k, m0) +
(n −6m2
0 −6m0k −m0 + 3)2
12

−
(n −6m2
0 −6m0k −5m0 −2k + 2)2
12

−
(n −6m2
0 −6m0k −7m0 −3k + 1)2
12

(by (2.2))
≥

−m0n
3
−5
2m0 + m0k2 −1
6m0k + 3m2
0k + 2m3
0

+

(n −6m2
0 −6m0k −m0 + 3)2
12
−1
3

−

(n −6m2
0 −6m0k −5m0 −2k + 2)2
12
+ 1
4

−

(n −6m2
0 −6m0k −7m0 −3k + 1)2
12
+ 1
4

(by (2.3) and (2.4))
= −1
12n2 +

5k
6 + m0k + 3
2m0 + m2
0

n −13
12k2 −1
2 + 7
6k −m0
6 −4m0k2
−13m2
0k −6m3
0k −3m2
0k2 −73
12m2
0 −9m3
0 −3m4
0 −16
3 m0k
≥min

k2 + 7k
6 −11
6 −3
2m0 + m0k2 + m2
0k + m2
0
3 + 13
6 m0k,
2k2
3
−5
6 + 11k
6
+ m0
2 + m0k2 + m2
0k + m2
0
3 + 3
2m0k

≥1/3.
Note that F(n, k) are integers. Thus, F(n, k) ≥1.
Case 4: 6m2
0 + 6m0k + 11m0 + 5k + 5 ≤n ≤6(m0 + 1)2 + 6(m0 + 1)k + m0.
If (m0, k) ∈{(0, 1), (1, 1)}, then 10 ≤n ≤37, we can check that F(n, 1) ≥1 when 
n ̸= 11 and F(11, 1) = 0 with Maple.
In view of (2.5) and (2.6), we deduce that if (m0, k) ̸∈{(0, 1), (1, 1)}, then
F(n, k) = G(n, k, m0) + p3(n −6m2
0 −6m0k −m0)
−p3(n −6m2
0 −6m0k −5m0 −2k −1)
−p3(n −6m2
0 −6m0k −7m0 −3k −2)
+ p3(n −6m2
0 −6m0k −11m0 −5k −5)
= G(n, k, m0) +
(n −6m2
0 −6m0k −m0 + 3)2
12

8
O.X.M. Yao / Journal of Combinatorial Theory, Series A 206 (2024) 105903
−
(n −6m2
0 −6m0k −5m0 −2k + 2)2
12

−
(n −6m2
0 −6m0k −7m0 −3k + 1)2
12

+
(n −6m2
0 −6m0k −11m0 −5k −2)2
12

(by (2.2))
≥

−m0n
3
−5
2m0 + m0k2 −1
6m0k + 3m2
0k + 2m3
0

+

(n −6m2
0 −6m0k −m0 + 3)2
12
−1
3

−

(n −6m2
0 −6m0k −5m0 −2k + 2)2
12
+ 1
4

−

(n −6m2
0 −6m0k −7m0 −3k + 1)2
12
+ 1
4

+

(n −6m2
0 −6m0k −11m0 −5k −2)2
12
−1
3

(by (2.3) and (2.4))
= −1
3 (m0 + 1) n + k2 −1
2 + 17
6 k + 7
2m0
+ m0k2 + 3m2
0k + 6m2
0 + 2m3
0 + 35
6 m0k
≥

k −1
3

m2
0 +

k2 + 11
6 k −17
6

m0 + k2 + 5
6k −5
2
≥1.
Thus, if 6m2
0 + 6m0k + 11m0 + 5k + 5 ≤n ≤6(m0 + 1)2 + 6(m0 + 1)k + m0, then 
F(n, k) ≥1. This completes the proof of this lemma.
Now, we are ready to prove Theorem 1.3.
By (2.1) and (2.6),
∞

n=0
F(n, k)qn =
1
(1 −q)(1 −q2)(1 −q3)
∞

j=0

q6j2+6kj+j −q6j2+6kj+5j+2k+1
−q6j2+6kj+7j+3k+2 + q6j2+6kj+11j+5k+5
=
1
(1 −q)(1 −q2)(1 −q3)
∞

j=0
(−1)jq(3j2+6jk+j)/2(1 −q2j+2k+1). (2.9)
Theorem 1.3 follows from (2.7) and (2.9). This completes the proof. 

To conclude this section, we present a proof of Corollary 1.4.
O.X.M. Yao / Journal of Combinatorial Theory, Series A 206 (2024) 105903
9
Note that
(q6; q6)∞−(q6; q6)∞
(q; q)∞
k

j=1−k
(−1)jqj(3j−1)/2
= (q6; q6)∞−(q6; q6)∞
(q; q)∞
⎛
⎝
∞

j=−∞
(−1)jqj(3j−1)/2 −
∞

j=k+1
(−1)jqj(3j−1)/2
−
−k

j=−∞
(−1)jqj(3j−1)/2
⎞
⎠
= (q6; q6)∞
(q; q)∞
∞

j=k+1
(−1)jqj(3j−1)/2 + (q6; q6)∞
(q; q)∞
∞

j=k
(−1)jqj(3j+1)/2
(by (1.2))
= (q6; q6)∞
(q; q)∞
∞

j=0
(−1)j+k+1q(j+k+1)(3j+3k+2)/2 + (q6; q6)∞
(q; q)∞
∞

j=0
(−1)j+kq(j+k)(3j+3k+1)/2
= (−1)kq(3k2+k)/2 (q6; q6)∞
(q; q)∞
∞

j=0
(−1)jq(3j2+6jk+j)/2(1 −q2j+2k+1)
= (−1)kq(3k2+k)/2 · (q6; q6)∞
(q4; q)∞
·
∞
j=0(−1)jq(3j2+6jk+j)/2(1 −q2j+2k+1)
(1 −q)(1 −q2)(1 −q3)
,
from which with Theorem 1.3, we deduce that for k ≥1, the coeﬃcient of qn in
(−1)k
⎛
⎝(q6; q6)∞−(q6; q6)∞
(q; q)∞
k

j=1−k
(−1)jqj(3j−1)/2
⎞
⎠
is nonnegative (resp. positive) for n ≥0 (resp. (3k2 + k)/2). This implies that Conjec-
ture 1.1 is true. This completes the proof.
