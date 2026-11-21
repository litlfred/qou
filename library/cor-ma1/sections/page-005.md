---
doc_id: cor-ma1
doc_title: "Overpartitions, lattice paths and Rogers-Ramanujan identities"
section_id: page-005
section_title: "Page 5"
section_number: null
pages: 5-5
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
toc_source: undetermined
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
4
SYLVIE CORTEEL AND OLIVIER MALLET
Figure 1. Ferrers diagram of the overpartition λ = (5, 4, 3, 3) of weight 15.
2 2 2 2 1
2 2 2 2
2 2 2
2 2 1
Figure 2. Example of a 2-modular diagram of weight 28.
The Frobenius representation of an overpartition [18, 30] of n is a two-rowed array
a1
a2
· · ·
aN
b1
b2
· · ·
bN

where (a1, . . . , aN) is a partition into distinct nonnegative parts and (b1, . . . , bN) is an overpartition into
nonnegative parts where the ﬁrst occurrence of a part can be overlined and N + P(ai + bi) = n. Following
[18], we call pQ,O(n) the number of such two-rowed arrays. We call this the Frobenius representation of an
overpartition because it is in bijection with overpartitions. This was proved in [18] and we now recall the
algorithm used for that proof.
We use the notion of a hook.
Given a positive integer a and a non-negative integer b, h(a, b) is the
hook that corresponds to the partition (a, 1, . . . , 1) where there are b ones. Combining a hook h(a, b) and a
partition α is possible if and only if a > α1 and b ≥l(α), where l(α) denotes the number of parts of α. The
result of the union is β = h(a, b) ∪α with β1 = a, l(β) = b + 1 and βi = αi−1 + 1 for i > 1.
Now take a two-rowed array ν counted by pQ,O(n), increase the entries on the top row by 1 and initialize
α and β to the empty object, ǫ. Beginning with the rightmost column of ν, we proceed to the left, building
α into an ordinary partition and β into a partition into distinct parts. At the ith column, if bi is overlined,
then we combine the hook h(ai, bi) and α. Otherwise, we add the part bi to α′ (the conjugate of α) and the
part ai to β. Joining the parts of α together with the parts of β gives the overpartition λ. An example is
given below starting with ν =
7
5
4
2
0
6
4
4
3
1

.
ν
α
β
8
6
5
3
1
6
4
4
3
1

ǫ
ǫ
8
6
5
3
6
4
4
3

(1, 1)
ǫ
8
6
5
6
4
4

(2, 2, 1)
(3)
8
6
6
4

(3, 3, 2, 1)
(5, 3)
8
6

(6, 4, 4, 3, 2)
(5, 3)
ǫ
(7, 5, 5, 4, 3, 1)
(8, 5, 3)
We get λ = (8, 7, 5, 5, 5, 4, 3, 3, 1). The reverse bijection can be easily described. See [18].
We now deﬁne the successive ranks.
