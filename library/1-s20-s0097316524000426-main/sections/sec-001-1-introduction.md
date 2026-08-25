---
doc_id: 1-s20-s0097316524000426-main
doc_title: "Proof of a conjecture of Ballantine and Merca on truncated sums of 6-regular partitions"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1-s2.0-S0097316524000426-main.pdf
source_sha256: 76a8ab857163aa09
doc_brief: "Proof of a conjecture of Ballantine and Merca on truncated sums of 6-regular partitions — 7 sections: Proof of a conjecture of Ballantin; Introduction; Proofs of Theorem 1.3 and Corollar"
---
Recall that a partition of a positive integer n is an integer sequence λ =( λ1, λ2, ...,  λk)
such that λ1 ≥ λ2 ≥···≥ λk > 0a n d λ1 + λ2 + ··· + λk = n. The numbers λi are called 
parts of λ [1]. Let p(n)d e n o t e the number of partitions of n. As usual, set p(0) =1a n d 
p(x) =0w h e n x is not a nonnegative integer. Euler found that the generating function 
for p(n)i s
E-mail address: yaoxiangmei@163.com.
https://doi.org/10.1016/j.jcta.2024.105903
0097-3165/© 2024 Elsevier Inc. All rights reserved.
2 O.X.M. Yao / Journal of Combinatorial Theory, Series A 206 (2024) 105903
∞∑
n=0
p(n)qn = 1
(q; q)∞
, (1.1)
where here and throughout the paper, we use the following notation
(a; q)∞ :=
∞∏
k=0
(1 − aqk).
The reciprocal of the right hand side of (1.1)h a s a nice series representation as follows:
(q; q)∞ =
∞∑
n=−∞
(−1)nqn(3n−1)/2, (1.2)
which is the Euler pentagonal number theorem.
In 2012, Andrews and Merca [2] proved the following identity which is a truncated 
version of the Euler pentagonal number theorem
1
(q; q)∞
k∑
n=1−k
(−1)nqn(3n−1)/2 =1+( −1)k−1qk(k−1)/2
∞∑
n=k
q(k+1)n
(q; q)n
[
n − 1
k − 1
]
, (1.3)
where k is a positive integer and the q-binomial coeﬃcient is deﬁned by
[
n
m
]
=
[
n
m
]
q
:=
⎧
⎪⎨
⎪⎩
(q; q)n
(q; q)m(q; q)n−m
, if 0 ≤ m ≤ n,
0, otherwise.
As a corollary of (1.3), Andrews and Merca [2] obtained the following inﬁnite family of 
linear inequalities involving the partition function p(n): for k ≥ 1a n d n ≥ 1,
(−1)k−1
k−1∑
j=0
(−1)j
(
p
(
n − j(3j +1 )
2
)
− p
(
n − (j + 1)(3j +2 )
2
))
≥ 0.
Motivated by Andrews and Merca’s work, the truncated versions of certain classical 
identities have been established. As corollaries of those truncated versions, a number of 
inﬁnite families of inequalities involving certain partition functions, such as overpartitions 
and partitions with odd parts distinct, have been proved; see for example [3,6–16].
Very recently, Ballantine and Merca [4] considered inﬁnite families of inequalities and 
congruences modulo 3 for b6(n). Recall that if t ≥ 2i s an integer, then a partition is 
called a t-regular partition if there is no part divisible by t. Let bt(n)d e n o t e the number 
of t-regular partitions of n. As usual, set bt(0) =1 . The generating function of bt(n)i s
∞∑
n=0
bt(n)qn = (qt; qt)∞
(q; q)∞
. (1.4)
O.X.M. Yao / Journal of Combinatorial Theory, Series A 206 (2024) 105903 3
At the end of their paper [4], Ballantine and Merca presented the following two con-
jectures on b6(n):
Conjecture 1.1. For n ≥ 0 and k ≥ 1,
(−1)k
⎛
⎝αn −
k∑
j=1−k
(−1)jb6(n − j(3j − 1)/2)
⎞
⎠ ≥ 0 (1.5)
with strict inequality if n ≥ k(3k +1 )/2, where αn is deﬁned by
αn :=
{
(−1)m, if n =3 m(3m − 1),m ∈ Z,
0, otherwise.
Conjecture 1.2. For n ≥ 0 and k ≥ 1,
(−1)k−1
⎛
⎝αn −
k∑
j=−k
(−1)jb6(n − j(3j − 1)/2)
⎞
⎠ ≥ 0 (1.6)
with strict inequality if n ≥ (k + 1)(3k +2 )/2.
The purpose of this paper is to prove a general result which implies Conjecture 1.1 by 
using a formula on the number of partitions into parts not exceeding 3g i v e n by Cayley. 
We omit the proof of Conjecture 1.2 since (1.6)i s a weaker version of (1.5). In fact, we 
will prove the following theorem.
Theorem 1.3. For k ≥ 1,deﬁne
∞∑
n=0
ν(n, k)qn := 1
(1 − q)(1 − q2)(1 − q3)
∞∑
j=0
(−1)jq(3j2 +6jk+j)/2(1 − q2j+2k+1).
Then ν(n, k) is positive for all nonnegative integers n and positive integers k with (n, k) ⁄=
(11, 1). In particular, ν(11, 1) =0 .
From Theorem 1.3, we obtain the following corollary.
Corollary 1.4. Conjecture 1.1 is true.
