---
doc_id: arxiv-2401.04019v1
doc_title: "TRUNCA TED THET A SERIES RELA TED TO THE JACOBI TRIPLE PRODUCT IDENTITY"
section_id: sec-004-41-proof-of-theorem-12
section_title: "Proof of Theorem 1.2"
section_number: 4.1
pages: 12-13
source_pdf: 2401.04019v1.pdf
source_sha256: 1a29e52a81639640
doc_brief: "TRUNCATED THETA SERIES RELATED TO THE JACOBI TRIPLE PRODUCT IDENTITY — The work of Andrews and Merca on the truncated Euler’s pen- tagonal number theorem led to a resurgence in research on tru ncated"
---
(−1)k
k∑
j=−k
(−1)jb3(n −j(3j − 1)/2) + (−1)k−1ρ3(n) ≥ 0.
From [17, Corollary 17], we have
(−1)k
(q;q)∞
k∑
j=−k
(−1)jqj(3j−1)/2 − (−1)k(15)
= qk(3k+7)/2+2
(q;q3)∞(q3;q3)∞
∞∑
n=0
qn(3n+3k+5)
(q3;q3)n(q2;q3)n+k+1
+ qk(3k+5)/2+1
(q2;q3)∞(q3;q3)∞
∞∑
n=0
qn(3n+3k+4)
(q3;q3)n(q;q3)n+k+1
.
Multiplying both sides of (15) by ( q3;q3)∞ we obtain
(−1)k (q3;q3)∞
(q;q)∞
k∑
j=−k
(−1)jqj(3j−1)/2 + (−1)k−1(q3;q3)∞(16)
=qk(3k+5)/2+1
(q2;q3)∞
∞∑
n=0
qn(3n+3k+4)
(q3;q3)n(q;q3)n+k+1
+ qk(3k+7)/2+2
(q;q3)∞
∞∑
n=0
qn(3n+3k+5)
(q3;q3)n(q2;q3)n+k+1
=:H1(q) +H2(q).(17)
Since each ofH1(q) andH2(q) above has non-negative coeﬃcients, this completes
the proof Theorem 1.2. □
We now interpret (16) as a partition generating function. First we in troduce some
notation. Given a 3-regular partition µ, we deﬁne the ( k + 2, 3)−Durfee rectangle
ofµ to be the largest a× (a+k + 2) rectangle that ﬁts inside the 3-modular diagram
ofµ. Note that ∑ k
t=0(3t + 2) =k(3k + 7)/2 + 2 and ∑ k
t=0(3t + 1) =k(3k + 5)/2 + 1.
Let Bi
3(m) be the set of 3-regular partitions λ of m such that if we write λ =
λ1,3 ∪λ2,3, parts 3 t +i, 0 ≤ t ≤ k occur in λi,3 at least once and the ﬁrst row in
the 3-regular diagram of λi,3 below the (k + 2, 3)−Durfee rectangle is shorter than
the width of the ( k + 2, 3)−Durfee rectangle. (If the ( k + 2, 3)−Durfee rectangle
of λi,3 has height zero, this means that the parts of λi,3 are at most 3 k +i and all
parts 3t +i, 0 ≤t ≤k occur.) Then Hi(q), i = 1, 2, is the generating function for
the sequence |Bi
3(n)|. To see the interpretation of H1(q) as a partition generating
function, write
H1(q) = 1
(q2;q3)∞
∞∑
n=0
qk(3k+5)/2+1
(q;q3)n+k+1
·qn(3n+3k+4)
(q3;q3)n
=: 1
(q2;q3)∞
∞∑
n=0
h1(q;n)·h2(q;n).
Informally, for partitions λ ∈ B 1
3(n),
• the term 1/(q2;q3)∞ generates the parts of λ2,3;
• h2(q;n) generates the ﬁrst n parts of λ1,3, all of size at least 3 n + 3k + 4;
TRUNCATED THETA SERIES RELATED TO THE JTP IDENTITY 13
• h1(q;n) generates the remaining parts of λ1,3, all of size at most 3 n + 3k + 1
and parts 3t + 1, 0 ≤t ≤k, occur at least once.
Thus, term h1(q;n) ·h2(q;n) generates partitions λ1,3 with (k + 2, 3)−Durfee rec-
tangle of height n. The interpretation of H2(q) is explained similarly.
Then, the coeﬃcient of qn is |B1
3(n)| + |B2
3(n)|.
We note that B1
3(n) ∩ B2
3(n) ⁄= ∅.
