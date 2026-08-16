---
doc_id: cor-ma1
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-018-7-new-partition-theorems
section_title: "New partition theorems"
section_number: 7
pages: 23-25
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
We ﬁrst prove Corollary 1.6 and then extract its combinatori al information.
7.1. Proof of Corollary 1.6. We recall here the Jacobi Triple Product identity (JTP) give n in equation
(1.2):
(−1/z,−zq, q; q)∞ =
∞∑
n=−∞
znq(n+1
2 ).
and the result of Theorem 1.5
E k,i(a, q) = (−aq)∞
(q)∞
∞∑
n=−∞
(−1)nanq2k(n+1
2 )−n(i−1) (−1/a)n
(−aq)n
.
We ﬁrst prove (1.3). Using Theorem 1.5, we get
E k,i(0, q) = 1
(q)∞
∞∑
n=−∞
(−1)nq(2k+1)(n+1
2 )−ni.
We substitute q→ q2k+1, z→− q−i in (1.2) and get
E k,i(0, q) = (qi, q2k+1−i, q2k+1; q2k+1)∞
(q)∞
.
Second we prove (1.4). Using Theorem 1.5, we get
E k,i(1/q, q2) = (−q; q2)∞
(q2; q2)∞
∞∑
n=−∞
(−1)nq4k(n+1
2 )−n(2i−1).
We substitute q→ q4k, z→− q−2i+1 in (1.2) and get
E k,i(1/q, q2) = (q2; q4)∞(q2i−1, q4k+1−2i, q4k; q4k)∞
(q)∞
.
Third we prove (1.5). Using Theorem 1.5, we get
E k,i(1, q) = (−q)∞
(q)∞
∞∑
n=−∞
(−1)nq2k(
n+1
2 )−n(i−1) 2
1 + qn
OVERPARTITIONS, LATTICE PATHS, AND ROGERS-RAMANUJAN IDEN TITIES 23
Writing half of this series twice, once with n and once with −n, we have
E k,i(1, q) = (−q)∞
(q)∞
( ∞∑
n=−∞
(−1)nq2k(n+1
2 )−ni qn
1 + qn +
∞∑
n=−∞
(−1)nq2k(n+1
2 )+n(i−2k) 1
1 + qn
)
Therefore
E k,k(1, q) = (−q)∞
(q)∞
∞∑
n=−∞
(−1)nq2k(n+1
2 )−nk;
and for i < k
E k,i(1, q) = (−q)∞
(q)∞
( ∞∑
n=−∞
(−1)nq2k(n+1
2 )−ni−
∞∑
n=−∞
(−1)nq2k(n+1
2 )−n(i+1) qn
1 + qn
+
∞∑
n=−∞
(−1)nq2k(n+1
2 )+n(i−2k)−
∞∑
n=−∞
(−1)nq2k(n+1
2 )+n(i+1−2k) 1
1 + qn
)
= (−q)∞
(q)∞
( ∞∑
n=−∞
(−1)nq2k(
n+1
2 )(q−ni + qn(i−2k))
)
−E k,i+1(1, q)
= (−q)∞
(q)∞
2(k−i)∑
j=0
(−1)j
∞∑
n=−∞
(−1)nq2k(n+1
2 )−n(i+j).
We substitute q→ q2k, z→− q−i−j in (1.2) and get
E k,i(1, q) = (−q)∞
(q)∞
2(k−i)∑
j=0
(−1)j(qi+j , q2k−i−j , q2k)∞.
Finally we prove (1.6).
E k,i(1/q, q) = (−1)∞
(q)∞
∞∑
n=−∞
(−1)nq2k(
n+1
2 )−ni 1 + qn
2 .
We substitute q→ q2k, z→− q−i and q→ q2k, z→− q−i+1 in (1.2) and get
E k,i(1/q, q) = (−q)∞
(q)∞
(qi, q2k−i, q2k; q2k)∞ + (qi−1, q2k−i+1, q2k; q2k)∞.
Now we give some combinatorial interpretation of Equations (1.4), (1.5) and (1.6).
7.2. 2-modular diagrams. We state in details the result for the Andrews’ generalizati on of the Gordon-
G¨ ollnitz identities which correspond to equation (1.4) of Corollary 1.6. The coeﬃcient of qn in this equation
is the number of partitions of n with parts not congruent to 2 mod 4 and 0 ,±(2i− 1) mod 4 k. We make
the change of variable q→ q2 and a→ 1/q in Theorem 1.4 and interpret it combinatorially in terms of
2-modular diagrams deﬁned in Section 2. There exists an easy bijection φ between 2-modular diagrams of
weight n with j ones and overpartitions of ( n + j)/2 with j overlined parts. This bijection consists of erasing
any 2 of the modular diagram and changing any 1 to a marked corn er. With this bijection in hand, the
successive ranks (resp. Durfee dissection) of a 2-modular d iagram µ are the successive ranks (resp. Durfee
dissection) of the corresponding overpartition φ(µ ).
Proposition 7.1. All the following are equal:
• The number of partitions of n with parts not congruent to 2 mod 4 and 0,±(2i− 1) mod 4 k;
• The number of partitions of n of the form (λ1, λ2, . . . , λs) with unrepeated odd parts, where λℓ−
λℓ+k−1≥ 3 if λℓ+k−1 is even and 2 otherwise; and f1 + f2 < i;
• The number of 2-modular diagrams of n whose successive ranks lie in [−i + 2, 2k− i− 1];
• The number of 2-modular diagrams of n with i− 1 successive Durfee squares followed by k− i
successive Durfee rectangles, the ﬁrst one being a generali zed Durfee square/rectangle.
