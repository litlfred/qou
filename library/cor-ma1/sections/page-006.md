---
doc_id: cor-ma1
doc_title: "Overpartitions, lattice paths and Rogers-Ramanujan identities"
section_id: page-006
section_title: "Page 6"
section_number: null
pages: 6-6
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
toc_source: undetermined
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
OVERPARTITIONS, LATTICE PATHS, AND ROGERS-RAMANUJAN IDENTITIES
5
Deﬁnition 2.1. The successive ranks of an overpartition can be deﬁned from its Frobenius representation.
If an overpartition has Frobenius representation
a1
a2
· · ·
aN
b1
b2
· · ·
bN

then its ith successive rank ri is ai −bi minus the number of non-overlined parts in {bi+1, . . . , bN}.
This deﬁnition is an extension of Lovejoy’s deﬁnition of the rank [30]. For example, the successive ranks
of
7
4
2
0
3
3
1
0

are (2, 0, 1, 0).
We say that the generalized Durfee square of an overpartition λ has size N if N is the largest integer such
that the number of overlined parts plus the number of non-overlined parts greater or equal to N is greater
than or equal to N (see Figure 3).
Figure 3. The generalized Durfee square of λ = (7, 4, 3, 3, 2, 1) has size 4.
Proposition 2.2. There exists a bijection between overpartitions whose Frobenius representation has N
columns and whose bottom line has j overlined parts and overpartitions with generalized Durfee square of
size N and N −j overlined parts.
Proof. An overpartition with generalized Durfee square of size N can be decomposed into a partition α into
at most N parts (the conjugate of the partition under the generalized Durfee square) and an overpartition
γ into N parts whose non-overlined parts are ≥N (the rest). For example, the overpartition on Figure 3
gives α = (2, 2, 1) and γ = (7, 4, 3, 1). An overpartition whose Frobenius representation has N columns can
be decomposed into a partition β into N distinct parts (β is obtained by adding 1 to each part of the top
line), a partition δ into distinct parts which lie between 0 and N −1 and a partition α into at most N parts.
δ and α are obtained from the bottom line as follows: we ﬁrst initialize α to the bottom line, then if the ith
part of the bottom line is overlined, we take oﬀits overline, we decrease the ﬁrst (i −1) parts of α by 1 and
add a part i −1 to δ.
Now there exists a bijection between ordered pairs (β, δ) and overpartitions γ. This bijection is deﬁned
as follows: we overline all the parts of β, then for each part i in δ, we add i to βi+1 and we remove the
overlining. We then reorder the parts, which gives us γ. This is easily invertible and is very similar to the
Algorithm Z [9].
The decompositions of the ﬁrst paragraph and the bijection of the second paragraph show that there is
indeed a bijection between overpartitions whose Frobenius representation has N columns and overpartition
with generalized Durfee square of size N. If there are j overlined parts in the bottom line of the Frobenius
symbol, there are j parts in δ and by the bijection, there are N −j overlined parts in γ. The proposition is
thus established.
□
Example 2.3. Let ν =
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
. We thus have N = 5 and j = 2 in this example. By adding
1 to each part of the top line, we get β = (8, 6, 5, 3, 1).
From the bottom line, we get δ = (4, 1) and
α = (4, 3, 3, 2, 1). By applying the bijection described in the second paragraph of the above proof, we get
γ = (8, 7, 5, 5, 3). Since α = (4, 3, 3, 2, 1), the resulting overpartition is λ = (8, 7, 5, 5, 5, 4, 3, 3, 1). It has
N −j = 3 overlined parts and its generalized Durfee square is of size 5.
