---
doc_id: arxiv-1203.6531v1
doc_title: "TRANSACTIONS OF THE AMERICAN MA THEMA TICAL SOCIETY"
section_id: sec-001-3-counting-reduced-words
section_title: "Counting Reduced Words"
section_number: 3
pages: 7-10
source_pdf: 1203.6531v1.pdf
source_sha256: 29541f28c1c62d8f
doc_brief: "AMERICAN MATHEMATICAL SOCIETY — Using Buchberger-Shirshov Algorithm and Composition-Diamond lemma we obtain the reduced Gr¨ obner-Shirshov bases of ~An and classify all reduced words of the aﬃne Weyl"
---
Theorem 14. Let ˆw = aisais−1...a i1v(bt) where aij = r0rnkjrnlj .Then aij ’s are
marked components of an arranged wordw =uv(bt) wherebt =r0rnpr1q if and only
if ks <k s−1 <...<k 1 <p and q <l1 <l 2 <...<l s <n
8 EROL YILMAZ, CENAP ¨OZEL AND U ˇGUR USTAOˇGLU
Proof. By construction of arranged words, the marked components satisfy the given
conditions. Conversely, if ˆw = aisais−1...a i1v(bt) is a word satisfying the condi-
tions, then an arranged word (w =uv(bt)) whose marked components are aij’s can
be obtained as follows:
The components up to r0rnksr1ls are
(r0rn2r1n)··· (r0rnksr1n)(r0rnksr1,n−1)··· (r0rnksr1ls),
the components between (r0rnkjr1lj) and (r0rnkj−1r1lj−1) are
(r0rnkjr1lj)··· (r0rnkj−1r1lj
)(r0rnkj−1r1,lj−1)··· (r0rnkj−1r1lj−1)
and the last part of the wordw =uv(bt) is
(r0rnk2r1l2)··· (r0rnk1r1l2
)(r0rnk1r1,l2−1)··· (r0rnk1r1l1)(v(bt)).
□
Therefore the number of the elements in an arranged word w =uv(bt) given by
the generating function
xα
(1−x2n)(1−x2n−1)··· (1−xn+1)
where α is the length of the word ˆw. In order to count all reduced words starting
with r0 we have to ﬁnd the number words ˆw whose length is α for any power α.
To do this, we will ﬁnd a correspondence between these words and some special
partitions of integers.
If m is a positive integer, then a partition of m is a nonincreasing sequence of
positive integers p1,p 2,...,p k whose sum is m. Each pi is called a part of the
partition. Let n be a positive integer. Any partition m =d1 +d2 +... +dk where
k≤n can be identify by the n−tuple (d1,d 2,...,d k, 0, 0,..., 0).
We can also represent each word r0rnkr1l with the n-tuple (k, 1,..., 1, 0,..., 0),
rnk with (k,..., 0) and r0l with (1, 1..., 1, 0,..., 0) where number one 1’s is equal
to l for 2≤k≤n− 1, 1≤l≤n.
Deﬁnition 15. Letn be a positive integer. Then-tuples (k, 1..., 1, 0,..., 0) where
number of 1’s is l for 1≤ k≤ n, 1 ≤ l≤ n− 1 are called basic partitions. The
basic partition (k1, 1..., 1, 0..., 0) is said to be connected to the basic partition
(k2, 1,..., 1, 0,..., 0) if k1 > k2 and the number of 1’s in the ﬁrst one is greater
than number of 1’s in the second one. Hence a sequence of connected partition
a1,a 2,...,a m corresponds to a word ˆw given in Theorem 14.
Theorem 16. There is one to one correspondence between words ˆw and the par-
titions in which there are at most n parts and in which no parts is larger than
n.
Proof. Since we identify each wordˆw with a sequence of connected basic partitions,
we must ﬁnd a correspondence between sequences of connected partitions and the
partitions ﬁt into a box of size n×n. Let a1,a 2,...,a m be a sequence of connected
partitions where ai = (ki,
li
1,..., 1| {z } 0,..., 0). Hence ki > kj and li > lj for 1≤i <
j≤m.
Deﬁne m⨁
i=1
ai =
m∑
i=1
σi−1
1 (ai)
GR¨OBNER-SHIRSHOV BASIS FOR AFFINE WEYL GROUP ~An 9
where σ(p1,p 2,...,p n−1,pn) = (pn,p 1,p 2,...,p n−1). Then
m⨁
i=1
ai = (k1,k 2+1,...,k m+m−1,
lm
m,...,m| {z },
lm−1 −(lm +1)
m− 1,...,m − 1| {z },...,
l1 −(l2 +1)
1,..., 1| {z }, 0..., 0)
We prove the last equation by induction on m.
Let m = 2, Since l1− 1≥l2,
a1⊕a2 = ( k1,
l1
1,..., 1| {z }, 0,..., 0) + (0,k 2,
l2
1,..., 1| {z }, 0,..., 0)
= ( k1,k 2 + 1,
l2
2,..., 2| {z },
l1 −(l2 +1)
1,..., 1| {z }, 0,..., 0)
Let us assume that
m−1⨁
i=1
ai = (k1,k 2 + 1,...,k m−1 +m− 2,
lm−1
m− 1,...,m − 1| {z },...,
l1 −(l2 +1)
1,..., 1| {z }, 0,..., 0).
m⨁
i=1
ai =
m∑
i=1
σi−1(ai)
=
m−1∑
i=1
σi−1(ai) +σm−1(am)
=
m−1⨁
i=1
ai +σm−1(am)
= ( k1,k 2 + 1,...,k m−1 +m− 2,
lm−1
m− 1,...,m − 1| {z },...,
l1
1,..., 1| {z }, 0,..., 0)
+ (
m−1
0, 0,..., 0| {z },km,
lm
1,..., 1| {z }, 0,..., 0)
= ( k1,k 2 + 1,...,k m +m− 1,
lm
m,...,m| {z },...,
l1 −(l2 +1)
1,..., 1| {z }, 0,..., 0)
The last equality easily follows from the fact lm−1− 1≥ lm. Since n≥ k1≥
k2 + 1≥··· >k m + (m− 1)≥m, the last line corresponds to a partition of 2 n ﬁts
into a n byn box.
Conversely letm = (m1,m 2,...,m n) be a partition wheren≥m1≥m2≥···≥
mn≥ 0. If i1 is the last index such thatmi1⁄= 0, then leta1 = (m1, 1,..., 1, 0,... 0)
where the last 1 in i1-th position. Then let
x =σ−1(m−a1) = (m2− 1,...,m i1− 1, 0,..., 0)
anda2 = (m2− 1,..., 1, 0,..., 0) where the position of the last nonzero element in
x and the position of last 1 in a2 are same. Clearly, a1 and a2 are basic partitions
anda1 is connected to a2. Continuing the process until reaching the (0,..., 0), one
can obtain a sequence of connected basic partitions. □
10 EROL YILMAZ, CENAP ¨OZEL AND U ˇGUR USTAOˇGLU
Deﬁnition 17. Let be positive integers. The q-binomial is deﬁned by
( m
r
)
q
= (1−qm)(1−qm−1)··· (1−qm−r+1)
(1−q)(1−q2)··· (1−qr)
Although the formula in the ﬁrst clause appears to involve a rational function, it
actually designates a polynomial, because the division is exact in Z[q]. A standard
combinatorial interpretation for q-binomial is that it counts the number of parti-
tions that will ﬁt into a box of sizek×(n−k), weighted by the size of the partition.
In particular the q-binomial
( 2n
n
)
x
= (1−x2n)(1−x2n−1)··· (1−xn+1)
(1−x)(1−x2)··· (1−xn)
counts the number of partitions in which there are at most n parts and in which
no parts is larger than n.
Now, we can proof the main result of this paper.
Theorem 18. Then the reduced Gr¨ obner-Shirshov basis of the aﬃne Weyl group
~An is the set G′. Moreover all the reduced words are the form rw where r is a
reduced word not including r0 and w is a arranged word.
The reduced words not including r0 is given in Lemma 5. It is easy to see that
the number of such words given by the generating function
(1 +x)(1 +x +x2)··· (1 +x +··· +xn).
Theorem 14 and Theorem 16 imply that the number of arranged words given by
the generating function
( 2n
n
)
x
(1−x2n)(1−x2n−1)··· (1−xn+1) =
(1−x2n)(1−x2n−1)···(1−xn+1)
(1−x)(1−x2)···(1−xn)
(1−x2n)(1−x2n−1)··· (1−xn+1)
= 1
(1−x)(1−x2)··· (1−xn).
By Lemma 7, the reduced words of ~An are in the form rw. Hence the number
of reduced words given by the generating function
(1 +x)(1 +x +x2)··· (1 +x +··· +xn)
(1−x)(1−x2)··· (1−xn)
which is well known Poincar´ e polynomial of the aﬃne Weyl group ~An. (see [11]).
Therefore these are all reduced words of ~An. Hence by Composition-Diamond
Lemma, G′ is a Gr¨ obner-Shirshov basis of~An. In fact, G′ is a reduced Gr¨ obner-
Shirshov basis.
