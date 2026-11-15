---
doc_id: cor-ma1
doc_title: "Overpartitions, lattice paths and Rogers-Ramanujan identities"
section_id: page-016
section_title: "Page 16"
section_number: null
pages: 16-16
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
toc_source: undetermined
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
OVERPARTITIONS, LATTICE PATHS, AND ROGERS-RAMANUJAN IDENTITIES
15
Proof. We can now prove equation (5.1). The lemma implies that
Bk,i(a, q) = Jk,i(−a, 1, q).
Hence
Bk,i(a, q)
=
(−aq)∞
(q)∞
∞
X
n=0
(−1)nan qkn2+n(k−i+1)(−1/a)n(1 −q(2n+1)i)
(−aq)n+1
+aq (−aq)∞
(q)∞
∞
X
n=0
(−1)nan qkn2+n(k−i+2)(−1/a)n(1 −q(2n+1)(i−1))
(−aq)n+1
=
(−aq)∞
(q)∞
 ∞
X
n=0
(−1)nan qkn2+n(k+1)(−1/a)n(q−in + aq1−(i−1)n)
(−aq)n+1
−
∞
X
n=0
(−1)nan qkn2+n(k+1)(−1/a)n(q(n+1)i + aq(n+1)(i−1)+1)
(−aq)n+1
!
=
(−aq)∞
(q)∞
 ∞
X
n=0
(−1)nan qkn2+n(k+1−i)(−1/a)n
(−aq)n
−
∞
X
n=0
(−1)nan+1 qkn2+n(k+i)+i(−1/a)n+1
(−aq)n+1
!
=
(−aq)∞
(q)∞
 ∞
X
n=0
(−1)nan qkn2+n(k+1−i)(−1/a)n
(−aq)n
+
−1
X
n=−∞
(−1)na−n qkn2+n(k−i)(−1/a)−n
(−aq)−n
!
=
(−aq)∞
(q)∞
∞
X
n=−∞
(−1)nan qkn2+n(k+1−i)(−1/a)n
(−aq)n
=
Ek,i(a, q)
□
5.2. A combinatorial proof. This part is a generalization of [16, Section 3]. We only give a sketch of
the proof and details can be found in [35]. In this section we represent overpartitions by their multiplicity
sequence (f0, f1, f2, . . .). We include the multiplicity f0 to simplify the deﬁnitions, although it is always
equal to 0.
We say that a sequence (fm, . . . , fm+ℓ) is a multuple (tuple of multiplicity) if
• fm+ℓ> 0,
• fm is not overlined, and
• fm+p is overlined for 1 ≤p ≤ℓ−1.
The length of a multuple (fm, . . . , fm+ℓ) is ℓand its weight is Pℓ
i=0(m + i)fm+i. We divide a multiplicity
sequence of an overpartition into multuples going from the right to the left. When we ﬁnd a positive multi-
plicity, we close a parenthesis to its right. We look for the next non-overlined multiplicity to its left and open
a parenthesis to the left of the multiplicity. The length of a multiplicity sequence is the sum of the length of
its multuples. For partitions, the length is called the number of pairs of multiplicities [16]. For example if
the overpartition has for multiplicity sequence (0, ¯2, 0, 2, ¯1, 1), then its multuples are ((0, ¯2), 0, (2, ¯1, 1)). The
ﬁrst multuple has length 1 and the second 2. Therefore the length is 3.
We deﬁne a map F from multuples of weight n and length ℓto multiplicity sequences of weight n −ℓand
length ℓ. Given a multuple (fm, . . . , fm+ℓ) then F(fm, . . . , fm+ℓ) is computed with the following algorithm :
• if fm+ℓ= 1, remove the overlining of fm+ℓand overline fm,
