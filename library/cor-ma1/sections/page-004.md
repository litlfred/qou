---
doc_id: cor-ma1
doc_title: "Overpartitions, lattice paths and Rogers-Ramanujan identities"
section_id: page-004
section_title: "Page 4"
section_number: null
pages: 4-4
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
toc_source: undetermined
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
OVERPARTITIONS, LATTICE PATHS, AND ROGERS-RAMANUJAN IDENTITIES
3
Corollary 1.6.
Ek,i(0, q)
=
(qi, q2k+1−i, q2k+1; q2k+1)∞
(q)∞
(1.3)
Ek,i(1/q, q2)
=
(q2; q4)∞(q2i−1, q4k+1−2i, q4k; q4k)∞
(q)∞
(1.4)
Ek,i(1, q)
=
(−q)∞
(q)∞
2(k−i)
X
j=0
(−1)j(qi+j, q2k−i−j, q2k; q2k)∞
(1.5)
Ek,i(1/q, q)
=
(−q)∞
(q)∞
((qi, q2k−i, q2k; q2k)∞
+(qi−1, q2k+1−i, q2k; q2k)∞)
(1.6)
Hence our result gives a general view of diﬀerent problems on partitions and overpartitions and shows
how they are related.
• Equation (1.3) corresponds to the Andrews-Gordon identities [5].
• Equation (1.4) corresponds to Andrews’s generalization of the Gordon-G¨ollnitz identities [6, 8].
• Equation (1.5) with i = k and (1.6) with i = 1 correspond to the two Gordon’s theorems for
overpartitions of Lovejoy [28].
Therefore our extension of the work on the Andrews-Gordon identities [8, 14, 16, 17] to the case of overparti-
tions includes these identities, but it also includes Andrews’s generalization of the Gordon-G¨ollnitz identities
and Gordon’s theorems for overpartitions. We prove this Corollary and deduce some new partition theorems
in Section 7.
In Section 2 we present all the necessary notions. In Section 3 we present the paths counted by Ek,i(n, j)
and compute the generating function. In Section 4 we present a direct bijection between the paths counted by
Ek,i(n, j) and the overpartitions counted by Ck,i(n, j). In Section 5 we present a recursive bijection between
the paths counted by Ek,i(n, j) and the overpartitions counted by Bk,i(n, j). We also give a generating
function proof. In Section 6, we present a combinatorial argument that shows that the paths counted by
Ek,i(n, j) and the overpartitions counted by Dk,i(n, j) are in bijection. All these bijections are reﬁnements
of Theorem 1.4. The number of peaks of the paths will correspond respectively to the number of columns of
the Frobenius representations, the length of the multiplicity sequence and the size of the generalized Durfee
square. In Section 7 we prove Corollary 1.6 and interpret it combinatorially. We conclude in Section 8 with
further questions.
2. Definitions on overpartitions
We will deﬁne all the notions in terms of overpartitions. We refer to [3] for deﬁnitions for partitions. In
all of the cases the deﬁnitions coincide when the overpartition has no overlined parts.
An overpartition of n is a non-increasing sequence of natural numbers whose sum is n in which the ﬁnal
occurrence (equivalently, the ﬁrst occurrence) of a number may be overlined. Alternatively n can be called
the weight of the overpartition. Since the overlined parts form a partition into distinct parts and the non-
overlined parts form an ordinary partition, the generating function for overpartitions is (−q)∞
(q)∞. The Ferrers
diagram of an overpartition is a classical Ferrers diagram where the corners can be marked (see Figure 1).
A 2-modular diagram is a Ferrers diagram of an overpartition where the marked corners are ﬁlled with ones
and the other cells are ﬁlled with twos (see Figure 2). The weight is the sum of the entries.
The multiplicity of the part j of an overpartition, denoted by fj, is the number of occurrences of this
part. We overline the multiplicity if the part appears overlined. For example, the multiplicity of the part 4
in the overpartition (6, 6, 5, 4, 4, 4, 3, 1) is f4 = 3. The multiplicity sequence is the sequence (f1, f2, . . .). For
example the previous overpartition has multiplicity sequence (1, 0, 1, 3, 1, 2).
