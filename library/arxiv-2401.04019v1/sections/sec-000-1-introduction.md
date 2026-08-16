---
doc_id: arxiv-2401.04019v1
doc_title: "TRUNCA TED THET A SERIES RELA TED TO THE JACOBI TRIPLE PRODUCT IDENTITY"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: 2401.04019v1.pdf
source_sha256: 1a29e52a81639640
doc_brief: "TRUNCATED THETA SERIES RELATED TO THE JACOBI TRIPLE PRODUCT IDENTITY — The work of Andrews and Merca on the truncated Euler’s pen- tagonal number theorem led to a resurgence in research on tru ncated"
---
A partition λ of n is a non-increasing sequence λ = (λ1,λ 2,...,λ ℓ) of positive
integers that add up to n. We refer to the integers λi as the parts of λ. As usual,
we denote by p(n) the number of partitions of n. Since the empty partition ∅ is the
only partition of 0, we have p(0) = 1. For a thorough introduction to the theory of
partitions we refer the reader to [1, 4].
We use the Pochhammer symbol: for n ∈ N0 ∪ {∞}
(a;q)n :=
n−1∏
j=0
(1 −aqj).
The generating function for the sequence p(n) is given by
∞∑
n=0
p(n)qn =
∞∏
i=1
1
1 −qi = 1
(q;q)∞
.
Throughout this article, we assume q is a complex number with |q|< 1 so that all
products and series converge absolutely.
The earliest theta series identity is likely Euler’s pentagonal number t heorem [1,
Eq. (1.3.1)]:
(1)
∞∑
j=−∞
(−1)jqj(3j−1)/2 = (q;q)∞.
2020 Mathematics Subject Classiﬁcation. 05A17, 11P81, 05A19, 05A20.
Key words and phrases. partitions, theta series, truncated series, combinatoria l injection.
B.F. partially supported by Simons Foundation Collaborati on Grant 635835.
1
2 CRISTINA BALLANTINE AND BROOKE FEIGON
Multiplying both sides in (1) by 1 /(q;q)∞, leads to the recurrence relation
p(n) =
∞∑
j=1
(−1)j−1p(n −j(3j ± 1)/2)
for n ≥ 1.
In 1951, Shanks [18] considered a truncation of the theta series o ccurring in (1)
and proved that
(2)
k∑
j=−k
(−1)jqj(3j−1)/2 =
k∑
j=0
(−1)j(q;q)kq(
j+1
2 )+jk
(q;q)j
.
With few exceptions [19, 3] the subject was dormant for more than half a cen-
tury. Then, in 2012, Andrews and Merca [5] obtained a new trunca tion of Euler’s
pentagonal number theorem. They showed that
(3) 1
(q;q)∞
k−1∑
j=0
(−1)iqj(3j+1)/2(1 −q2j+1) = 1 + ( −1)k−1
∞∑
n=1
q(
k
2)+(k+1)n
(q;q)n
[n − 1
k − 1
]
,
where
[
n
k
]
=







(q;q)n
(q;q)k(q;q)n−k
if 0 ⩽ k ⩽ n,
0 otherwise.
As explained in [5], combinatorially, (3) means that
(−1)k−1
k∑
j=−(k−1)
(−1)jp(n −j(3j − 1)/2) = Mk(n),
whereMk(n) is the number of partitions of n in which k is the smallest integer that
is not a part of the partition and there are more parts greater tha n k than there
are less than k.
Work of Merca [17, Corollary 17] shows that Shank’s truncation (2) leads to the
following inequality which holds for all n,k ≥ 1:
(4) ( −1)k
k∑
j=−k
(−1)jp(n −j(3j − 1)/2) ≥ 0.
Xia and Zhao [22] showed that the left hand side of (4) equals the num ber of
partitions of n in which every integer less than or equal to k appears as a part at
least once and the ﬁrst part larger than k appears at least k + 1 times.
The work of Andrews and Merca opened up the study of truncated theta series
and linear partition inequalities and many articles followed. For example , Guo and
Zeng [10] obtained truncations of Gauss’ identities [1, (2.2.12), (2.2 .13)], and Yee
[23] and also Wang and Yee [21] found a truncation of the Jacobi trip le product
identity
(5) 1
(qS;qR)∞(qR−S;qR)∞(qR;qR)∞
∞∑
n=−∞
(−1)nqRn(n−1)/2+Sn = 1,
TRUNCATED THETA SERIES RELATED TO THE JTP IDENTITY 3
where R and S are positive integers with 1 ≤ S < R/2. Wang and Yee show
explicitly that the truncations
1
(qS;qR)∞(qR−S;qR)∞(qR;qR)∞
m∑
n=−(m−1)
(−1)nqRn(n−1)/2+Sn
and
1
(qS;qR)∞(qR−S;qR)∞(qR;qR)∞
m∑
n=−m
(−1)nqRn(n−1)/2+Sn,
when expanded as q-series, have non-negative coeﬃcients.
Motivated by these results, Merca [14] investigated truncations o f Jacobi’s triple
product written in the form
(6) 1
(qS;qR)∞(qR−S;qR)∞
∞∑
n=−∞
(−1)nqRn(n−1)/2+Sn − (qR;qR)∞ = 0
and made a stronger conjecture.
Conjecture 1. [14, Conjecture 4.3] For 1 ≤S <R, k ≥ 1, the theta series
(7) (−1)k
(qS;qR)∞(qR−S;qR)∞
∞∑
j=k
(−1)jqRj(j+1)/2−Sj (
1 −qS(2j+1))
has non-negative coeﬃcients.
We deﬁne
∞∑
n=0
aS,R,k(n)qn := (−1)k−1
(qS;qR)∞(qR−S;qR)∞
k−1∑
j=0
(−1)jqj(j+1)R/2−jS (1 −q(2j+1)S)
− (−1)k−1(qR;qR)∞,(8)
and we write ak(n) for aS,R,k(n) when S and R are clear from the context. As
mentioned in [14], Conjecture 1 is equivalent to showing aS,R,k(n) ≥ 0 for all n ≥ 0,
k ≥ 1, 1 ≤S <R.
In this article we prove Conjecture 1 for k ∈ {1, 2, 3}.
Theorem 1.1. If k ∈ { 1, 2, 3} and 1 ≤ S < R, then the theta series (7) has
non-negative coeﬃcients.
Let
(9) ρR(n) :=
{
(−1)i if n =Ri(3i − 1)/2 for some i ∈ Z
0 otherwise.
Then, (1) with q replaced by qR, implies that ( qR;qR)∞ is the generating function
for the sequence ρR(n).
When R = 3,S = 1, for all n ≥ 0,k ≥ 1, we have
(10) a1,3,k(n) = ( −1)k−1
k∑
j=−(k−1)
(−1)jb3(n −j(3j − 1)/2) − (−1)k−1ρ3(n),
wherebℓ(n) denotes the number of ℓ-regular partitions of n, i.e., partitions with no
parts divisible by ℓ.
4 CRISTINA BALLANTINE AND BROOKE FEIGON
Remark 1. From [5, Lemma 1.2] it follows that the q-series on the right hand side
of (8) for R = 3,S = 1 equals
(q3;q3)∞
∞∑
n≥0
Mk(n)qn.
Hence, if Conjecture 1 is true for R = 3 and S = 1, then for k ≥ 1,
∞∑
j=0
(−1)j(Mk(n −T3j) −Mk(n −T3j+2)) ≥ 0,
where Tj =j(j + 1)/2 is the jth triangular number.
We prove the following related theorem, which is weaker than Conjec ture 1 for
R = 3, S = 1.
Theorem 1.2. Letk ≥ 1. Then for all n ≥ 0,
(−1)k
k∑
j=−k
(−1)jb3(n −j(3j − 1)/2) + (−1)k−1ρ3(n) ≥ 0.
Note that Theorem 1.2 together with (10) shows that for all n ≥ 0, k ≥ 1,
a1,3,k(n) +b3(n −k(3k − 1)/2) ≥ 0.
Following the proof of Theorem 1.2 we also give a combinatorial interpr etation for
a1,3,k(n) +b3(n −k(3k − 1)/2).
Inequalities for b6(n) analogous to those in Theorem 1.2 were conjectured in [9].
We give a proof of the conjecture.
Theorem 1.3. [9, Conjecture 3] Forn ≥ 0,k >0
(11) ( −1)k−1

ρ6(n) −
k∑
j=−k
(−1)jb6(n −j(3j − 1)/2)

 ≥ 0,
with strict inequality if n ≥ (k + 1)(3(k + 1) − 1)/2.
We also give a combinatorial interpretation of the numbers on the lef t hand side
of (11).
Remark 2. In [9, Conjecture 3], the inequality (11) is conjectured to be strict for
n ≥k(3k + 1)/2. This is, in fact, not true as seen from the proof of Theorem 1.3.
WhenR = 4,S = 1, by considering the parity of triangular numbers, we see that
Conjecture 1 is equivalent to Conjecture 4 in [16], which states that for k ≥ 1 the
q-series
(−q;q)∞
∞∑
n=0
(−1)TnqTn+2k
has non-negative coeﬃcients. Here we used Euler’s identity
1
(q;q2)∞
= (−q;q)∞.
We prove that a weaker version of the conjecture is eventually tru e. As usual, we
denote by Q(n) the number of partitions of n with distinct parts, which by Euler’s
TRUNCATED THETA SERIES RELATED TO THE JTP IDENTITY 5
identity is also the number of partitions of n with odd parts. Let c1(n) = Q(n)
and, if k ≥ 2, let ck(n) be the sequence whose generating function is
(12)
∞∑
n=0
ck(n)qn = (−1)k−1(−q;q)∞

(−1)k−1qT2(k− 1) +
k−2∑
j=0
(−1)j(qT2j −qT2j+1 )

.
Theorem 1.4. If k ≥ 1 there exists Nk such that ck(n) ≥ 0 if n ≥Nk. Moreover,
Nk can be given explicitly.
This article is structured as follows. In section 2, we introduce relev ant back-
ground and notation used throughout. In section 3, we prove The orem 1.1 and
discuss applications in the case R = 4,S = 1. In particular, in Proposition 1 we
give a connection with the odd minimal excludant of partitions into odd parts. In
section 4, we prove Theorems 1.2, 1.3, and 1.4. In section 5 we prove combinato-
rially an identity related to the Jacobi Triple product identity. In par ticular cases,
this identity reduces to identities (6.7), (6.10), (6.12), and (6.13) c onjectured in [14].
Hence, we have combinatorial proofs of Merca’s identities. In sect ion 6, we use the
Weierstrass addition formula [13, Identity (8.1)] to prove an identit y involving the
number of 5-regular distinct partition of n. Finally, in section 7, we oﬀer some
concluding remarks.
