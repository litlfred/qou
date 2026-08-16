---
doc_id: cor-ma1
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-002-2-definitions-on-overpartitions
section_title: "Definitions on overpartitions"
section_number: 2
pages: 4-7
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
We will deﬁne all the notions in terms of overpartitions. We r efer to [3] for deﬁnitions for partitions. In
all of the cases the deﬁnitions coincide when the overpartit ion has no overlined parts.
An overpartition of n is a non-increasing sequence of natural numbers whose sum is n in which the ﬁnal
occurrence (equivalently, the ﬁrst occurrence) of a number may be overlined. Alternatively n can be called
the weight of the overpartition. Since the overlined parts f orm a partition into distinct parts and the non-
overlined parts form an ordinary partition, the generating function for overpartitions is (−q)∞
(q)∞
. The Ferrers
diagram of an overpartition is a classical Ferrers diagram w here the corners can be marked (see Figure 1).
A 2-modular diagram is a Ferrers diagram of an overpartition where the marked corners are ﬁlled with ones
and the other cells are ﬁlled with twos (see Figure 2). The wei ght is the sum of the entries.
The multiplicity of the part j of an overpartition, denoted by fj, is the number of occurrences of this
part. We overline the multiplicity if the part appears overl ined. For example, the multiplicity of the part 4
in the overpartition (6 , 6, 5, 4, 4, 4, 3, 1) is f4 = 3. The multiplicity sequence is the sequence ( f1, f2, . . .). For
example the previous overpartition has multiplicity seque nce ( 1, 0, 1, 3, 1, 2).
4 SYL VIE CORTEEL AND OLIVIER MALLET
Figure 1. Ferrers diagram of the overpartition λ = (5, 4, 3, 3) of weight 15.
2 2 2 2 1
2 2 2 2
2 2 2
2 2 1
Figure 2. Example of a 2-modular diagram of weight 28.
The Frobenius representation of an overpartition [18, 30] o f n is a two-rowed array
(a1 a2 ···aN
b1 b2 ···bN
)
where ( a1, . . . , aN ) is a partition into distinct nonnegative parts and ( b1, . . . , bN ) is an overpartition into
nonnegative parts where the ﬁrst occurrence of a part can be overlined and N +∑ (ai + bi) = n. Following
[18], we call pQ,O(n) the number of such two-rowed arrays. We call this the Froben ius representation of an
overpartition because it is in bijection with overpartitio ns. This was proved in [18] and we now recall the
algorithm used for that proof.
We use the notion of a hook. Given a positive integer a and a non-negative integer b, h(a, b) is the
hook that corresponds to the partition ( a, 1, . . . ,1) where there are b ones. Combining a hook h(a, b) and a
partition α is possible if and only if a > α 1 and b≥ l(α), where l(α) denotes the number of parts of α. The
result of the union is β = h(a, b)∪ α with β1 = a, l(β) = b + 1 and βi = αi−1 + 1 for i > 1.
Now take a two-rowed array ν counted by pQ,O(n), increase the entries on the top row by 1 and initialize
α and β to the empty object, ǫ. Beginning with the rightmost column of ν, we proceed to the left, building
α into an ordinary partition and β into a partition into distinct parts. At the ith column, if bi is overlined,
then we combine the hook h(ai, bi) and α. Otherwise, we add the part bi to α′ (the conjugate of α) and the
part ai to β. Joining the parts of α together with the parts of β gives the overpartition λ. An example is
given below starting with ν =
(7 5 4 2 0
6
4 4 3 1
)
.
ν α β
(8 6 5 3 1
6
4 4 3 1
)
ǫ ǫ
(8 6 5 3
6
4 4 3
)
(1, 1) ǫ
(8 6 5
6
4 4
)
(2, 2, 1) (3)
(8 6
6
4
)
(3, 3, 2, 1) (5 , 3)
(8
6
)
(6, 4, 4, 3, 2) (5 , 3)
ǫ (7, 5, 5, 4, 3, 1) (8 , 5, 3)
We get λ = (
8, 7, 5, 5, 5, 4, 3, 3, 1). The reverse bijection can be easily described. See [18].
We now deﬁne the successive ranks.
OVERPARTITIONS, LATTICE PATHS, AND ROGERS-RAMANUJAN IDEN TITIES 5
Deﬁnition 2.1. The successive ranks of an overpartition can be deﬁned from its Frobenius represe ntation.
If an overpartition has Frobenius representation
(a1 a2 ···aN
b1 b2 ···bN
)
then its ith successive rank ri is ai− bi minus the number of non-overlined parts in {bi+1, . . . , bN}.
This deﬁnition is an extension of Lovejoy’s deﬁnition of the rank [30]. For example, the successive ranks
of
(7 4 2 0
3 3 1 0
)
are (2 , 0, 1, 0).
We say that the generalized Durfee square of an overpartition λ has size N if N is the largest integer such
that the number of overlined parts plus the number of non-ove rlined parts greater or equal to N is greater
than or equal to N (see Figure 3).
Figure 3. The generalized Durfee square of λ = (7, 4, 3, 3, 2, 1) has size 4.
Proposition 2.2. There exists a bijection between overpartitions whose Frob enius representation has N
columns and whose bottom line has j overlined parts and overpartitions with generalized Durfe e square of
size N and N− j overlined parts.
Proof. An overpartition with generalized Durfee square of size N can be decomposed into a partition α into
at most N parts (the conjugate of the partition under the generalized Durfee square) and an overpartition
γ into N parts whose non-overlined parts are ≥ N (the rest). For example, the overpartition on Figure 3
gives α = (2 , 2, 1) and γ = (7, 4, 3, 1). An overpartition whose Frobenius representation has N columns can
be decomposed into a partition β into N distinct parts ( β is obtained by adding 1 to each part of the top
line), a partition δ into distinct parts which lie between 0 and N− 1 and a partition α into at most N parts.
δ and α are obtained from the bottom line as follows: we ﬁrst initial ize α to the bottom line, then if the ith
part of the bottom line is overlined, we take oﬀ its overline, we decrease the ﬁrst ( i− 1) parts of α by 1 and
add a part i− 1 to δ.
Now there exists a bijection between ordered pairs ( β, δ) and overpartitions γ. This bijection is deﬁned
as follows: we overline all the parts of β, then for each part i in δ, we add i to βi+1 and we remove the
overlining. We then reorder the parts, which gives us γ. This is easily invertible and is very similar to the
Algorithm Z [9].
The decompositions of the ﬁrst paragraph and the bijection o f the second paragraph show that there is
indeed a bijection between overpartitions whose Frobenius representation has N columns and overpartition
with generalized Durfee square of size N . If there are j overlined parts in the bottom line of the Frobenius
symbol, there are j parts in δ and by the bijection, there are N− j overlined parts in γ. The proposition is
thus established. □
Example 2.3. Let ν =
(7 5 4 2 0
6
4 4 3 1
)
. We thus have N = 5 and j = 2 in this example. By adding
1 to each part of the top line, we get β = (8 , 6, 5, 3, 1). From the bottom line, we get δ = (4 , 1) and
α = (4 , 3, 3, 2, 1). By applying the bijection described in the second paragr aph of the above proof, we get
γ = ( 8, 7, 5, 5, 3). Since α = (4 , 3, 3, 2, 1), the resulting overpartition is λ = ( 8, 7, 5, 5, 5, 4, 3, 3, 1). It has
N− j = 3 overlined parts and its generalized Durfee square is of si ze 5.
