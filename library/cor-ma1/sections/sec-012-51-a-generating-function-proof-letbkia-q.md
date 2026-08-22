---
doc_id: cor-ma1
doc_title: "Overpartitions, lattice paths and Rogers-Ramanujan identities"
section_id: sec-012-51-a-generating-function-proof-letbkia-q
section_title: "A generating function proof. LetBk,i(a, q) =∑"
section_number: 5.1
pages: 15-17
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
n,j≥0 Bk,i(n, j)ajqn. We prove that
(5.1) Bk,i(a, q) =E k,i(a, q)
We will generalize Lovejoy’s proof of Theorem 1.1 of [28]. Le t
Jk,i(a, x, q) = Hk,i(a, xq, q)− axqHk,i−1(a, xq, q)(5.2)
Hk,i(a, x, q) =
∞∑
n=0
xknqkn2+n−inan(1− xiq2ni)(axqn+1)∞(1/a)n
(q)n(xqn)∞
.(5.3)
Andrews showed in [3, p. 106-107] that
Hk,i(a, x, q)− Hk,i−1(a, x, q) = xi−1Jk,k−i+1(a, x, q)(5.4)
Jk,i(a, x, q)− Jk,i−1(a, x, q) = ( xq)i−1(Jk,k−i+1(a, xq, q)− aJk,k−i+2(a, xq, q)).(5.5)
We plug i = 0 in equation (5.3) and obtain Hk,0 = 0. We then plug i = 1 in equation (5.4) and obtain
Hk,1(a, x, q) = Jk,k(a, x, q). Then we plug i = 1 in equation (5.2) and obtain Jk,1(a, x, q) = Jk,k(a, xq, q).
Finally we set x = 0 in equations (5.2) and (5.3) and get Jk,i(a, 0, q) = 1. This implies for 1 ≤ i≤ k, the
following equations determine Jk,i(a, x, q):
Jk,i(a, 0, q) = 1
Jk,i(a, x, q)− Jk,i−1(a, x, q) = ( xq)i−1(Jk,k−i+1(a, xq, q)− aJk,k−i+2(a, xq, q));
Jk,1(a, x, q) = Jk,k(a, xq, q).
Let
Bk,i(a, x, q) =∑
n,j,p≥0 Bk,i(n, j, p)ajxpqn where Bk,i(n, j, p) is the number of overpartitions counted
by Bk,i(n, j) with p parts. We show that
Lemma 5.2. For 1≤ i≤ k,
Bk,i(a, x, q) = Jk,i(−a, x, q).
Proof. The only overpartition with zero parts is the empty one. Ther eforeBk,i(a, 0, q) = 1. It is obvious
that for 2 ≤ i≤ k,Bk,i(a, x, q)−Bk,i−1(a, x, q) is the generating function for overpartitions such that
∀ℓ, fℓ + fℓ+1 < k +1 and f1 = i− 1. MoreoverBk,i(a, xq, q) is the generating function for overpartitions such
that∀ℓ, fℓ+fℓ+1 < k +1, f2 < i and f1 = 0. Therefore ( xq)i−1Bk,k−i+1(a, xq, q) is the generating function for
overpartitions such that∀ℓ, fℓ + fℓ+1 < k +1, f1 = i− 1 and 1 is not overlined and a(xq)i−1Bk,k−i+2(a, xq, q)
is the generating function for overpartitions such that ∀ℓ, fℓ + fℓ+1 < k +1, f1 = i− 1 and 1 is overlined. We
get, for 2 ≤ i≤ k,Bk,i(a, x, q)−Bk,i−1(a, x, q) = ( xq)i−1(Bk,k−i+1(a, xq, q) + aBk,k−i+2(a, xq, q)). Finally
Bk,k(a, xq, q) is the generating function for overpartitions such that ∀ℓ, fℓ + fℓ+1 < k +1, f2 < k and f1 = 0
and therefore is equal to Bk,1(a, x, q). □
OVERPARTITIONS, LATTICE PATHS, AND ROGERS-RAMANUJAN IDEN TITIES 15
Proof. We can now prove equation (5.1). The lemma implies that
Bk,i(a, q) = Jk,i(−a, 1, q).
Hence
Bk,i(a, q) = (−aq)∞
(q)∞
∞∑
n=0
(−1)nan qkn2+n(k−i+1)(−1/a)n(1− q(2n+1)i)
(−aq)n+1
+aq (−aq)∞
(q)∞
∞∑
n=0
(−1)nan qkn2+n(k−i+2)(−1/a)n(1− q(2n+1)(i−1))
(−aq)n+1
= (−aq)∞
(q)∞
( ∞∑
n=0
(−1)nan qkn2+n(k+1)(−1/a)n(q−in + aq1−(i−1)n)
(−aq)n+1
−
∞∑
n=0
(−1)nan qkn2+n(k+1)(−1/a)n(q(n+1)i + aq(n+1)(i−1)+1)
(−aq)n+1
)
= (−aq)∞
(q)∞
( ∞∑
n=0
(−1)nan qkn2+n(k+1−i)(−1/a)n
(−aq)n
−
∞∑
n=0
(−1)nan+1 qkn2+n(k+i)+i(−1/a)n+1
(−aq)n+1
)
= (−aq)∞
(q)∞
( ∞∑
n=0
(−1)nan qkn2+n(k+1−i)(−1/a)n
(−aq)n
+
−1∑
n=−∞
(−1)na−n qkn2+n(k−i)(−1/a)−n
(−aq)−n
)
= (−aq)∞
(q)∞
∞∑
n=−∞
(−1)nan qkn2+n(k+1−i)(−1/a)n
(−aq)n
= E k,i(a, q)
□
5.2. A combinatorial proof. This part is a generalization of [16, Section 3]. We only give a sketch of
the proof and details can be found in [35]. In this section we r epresent overpartitions by their multiplicity
sequence ( f0, f1, f2, . . .). We include the multiplicity f0 to simplify the deﬁnitions, although it is always
equal to 0.
We say that a sequence ( fm, . . . , fm+ℓ) is a multuple (tuple of multiplicity) if
• fm+ℓ > 0,
• fm is not overlined, and
• fm+p is overlined for 1 ≤ p≤ ℓ− 1.
The length of a multuple ( fm, . . . , fm+ℓ) is ℓ and its weight is∑ ℓ
i=0(m + i)fm+i. We divide a multiplicity
sequence of an overpartition into multuples going from the r ight to the left. When we ﬁnd a positive multi-
plicity, we close a parenthesis to its right. We look for the n ext non-overlined multiplicity to its left and open
a parenthesis to the left of the multiplicity. The length of a multiplicity sequence is the sum of the length of
its multuples. For partitions, the length is called the numb er of pairs of multiplicities [16]. For example if
the overpartition has for multiplicity sequence (0 , ¯
2, 0, 2, ¯
1, 1), then its multuples are ((0 , ¯
2), 0, (2, ¯
1, 1)). The
ﬁrst multuple has length 1 and the second 2. Therefore the len gth is 3.
We deﬁne a map F from multuples of weight n and length ℓ to multiplicity sequences of weight n− ℓ and
length ℓ. Given a multuple ( fm, . . . , fm+ℓ) then F (fm, . . . , fm+ℓ) is computed with the following algorithm :
• if fm+ℓ =
1, remove the overlining of fm+ℓ and overline fm,
