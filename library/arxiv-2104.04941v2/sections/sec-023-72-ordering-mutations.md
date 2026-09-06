---
doc_id: arxiv-2104.04941v2
doc_title: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES"
section_id: sec-023-72-ordering-mutations
section_title: "Ordering mutations"
section_number: 7.2
pages: 34-36
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
doc_brief: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES — Fock and Goncharov [FG06b] introduced cluster ensembles, p roviding a framework for coordi- nates on varieties of surface"
---
that these permute Dynkin sub-quivers of Q by switching certain vertices without changing the cluster seed,
as in Remark 2.7. These are used in Lemmas 7.4 to 7.6 to justify the~µOi parts.
Lemma 7.1. The permutation ~µCS of Deﬁnitions 5.7 and 5.14 acts on quivers (and cluster ensemb les) by
permuting the vertices of the appropriate column according to σG.
Lemma 7.2. The permutation ~µRS of Deﬁnitions 5.7 and 5.14 acts on quivers (and cluster ensemb les) by
permuting the vertices of the mutated sub-quiver according to σAℓ .
These proofs rely heavily on results of [YZ08] described in S ection 3.1. In short, we shall restrict the
quivers on which ~µCS and ~µRS act to those which Yang–Zelevinsky can strongly analyze. We then use
counting arguments to establish that the mutation acts by pe rmutation, and use classic results to apply
these results to larger quivers.
Proof of Lemma 7.1. In our construction, whenever ~µCS is applied, the vertices at which it mutates form
a subquiver of Dynkin type. Therefore, ﬁrst, we shall show th at the result holds when ~µCS is applied to a
quiver which is of Dynkin type. Then we shall show that the res ult holds for larger quivers which contain a
sub-quiver of Dynkin type.
First, suppose ~µCS acts on quiver of Dynkin type (non A2n). There exists an element g of Lc,c−1
such
that the initial cluster coordinate at vk is ∆ ωk,ωk (g).
Now we note that ~µCS is exactly ℓ + 2 = h
2 + 1 iterations of a mutation following the Coxeter element c,
with each mutation replacing ∆ cmωk,cmωk with ∆ cm+1ωk,cm+1ωk . Since the number h(i;c) is always h
2 by our
construction of c, from Proposition 3.3 we obtain that the ﬁnal cluster coordi nate at vk is
∆ ch(k;c)+1ωk,ch(k;c)+1ωk (g) = ∆ ωk∗ ,ωk∗ (g),
which was the initial coordinate at vk∗ .
Thus~µCS acts on the cluster by permuting the associations between ve rtices and cluster variables according
to σG. In this way we obtain the desired result without ever having to rely directly facts of g ∈Lc,c−1
.
Now it must be shown that this holds when ~µCS acts on a larger quiver. Since the action of ~µCS is
solely a permutation on the mutable portion of the quiver, it preserves the set of cluster variables. By [FZ03,
Theorem 1.12] and the ﬁniteness of Dynkin-type quivers, the cluster variables determine the exchange matrix
and therefore the quiver. Therefore the action of ~µCS on the graph must be trivial up to renaming, and
therefore must be exactly the renaming that we have created. □
Proof of Lemma 7.2. We would like to apply exactly the same argument as in the proo f of Lemma 7.1.
However, since rows are of type Aℓ and our construction algorithm for Q does not allow ~µRS to be repeated
iterations of a single Coxeter-style mutation, we must be a b it more careful.
For a type Aℓ, deﬁne QLin = QAℓ,Lin as the Dynkin quiver where the graph describes a linear order ing
from left to right. Also, let QAlt =QAℓ,Alt be the Dynkin quiver in source-sink position, see Figure 29.
1 2 3
· · ·
ℓ 1 2 3
· · ·
ℓ
Figure 29. QAlt on the left, QLin on the right, both quivers of Dynkin type Aℓ.
We also introduce one more piece of notation.
F act 7.3. LetY (x) be deﬁned as 1
2 when x is odd and 0 when x is even. Then
Y (a) −Y (b) = ( −1)parity aY (a −b).
As above, we will interpret the cluster coordinates of the mu table Dynkin-type quiver as minor coordinates
on some g ∈Lc,c−1
, but we cannot interpret them as the initial minors.
The mutation ~µRS acts on ℓ =b −a vertices, always arranged as in QLin of Figure 29. Recalling notation
of Proposition 3.2, by [YZ08] the quiver QAlt (together with cluster variables ∆ ωi,ωi atvi) is an initial seed,
governed by an element of Lt+t−,(t+t−)−1
.
34
It is straightforward that (up to Langlands dualizing, whic h has no eﬀect on coordinates) the mutation
~µLin =
{
µ {v1,v 3,...,v ℓ−0, v 2,v 4,...,v ℓ−1, ..., v 1,v 3, v 2, v 1 } ℓ odd
µ {v1,v 3,...,v ℓ−1, v 2,v 4,...,v ℓ−2, ..., v 1,v 3, v 2, v 1 } ℓ even
=
ℓ−1∏
j=2⌊ℓ/2⌋−(ℓ−1)
{∏ ⌈(ℓ−j)/2⌉
k=1 µ {v2k−1 } ℓ −j odd∏ (ℓ−j)/2
k=1 µ {v2k } ℓ −j even
transformsQAlt toQLin, using only source or sink mutations (thus governed by primi tive exchange relations).
By considering these relations, and counting mutations, it is also straightforward that the cluster coordinates
of QLin are given by the following.
coordinate at vk is ∆ c(ℓ−k)/2+Y (ℓ)+Y (k)ωk,c(ℓ−k)/2+Y (ℓ)+Y (k)ωk
For example, coordinates of QA4,Lin are
{
∆ c2ω1,c2ω1, ∆ c1ω2,c1ω2, ∆ c1ω3,c1ω3, ∆ c0ω4,c0ω4
}
, and the coordinates
forQA3,Lin are
{
∆ c2ω1,c2ω1, ∆ c1ω2,c1ω2, ∆ c1ω3,c1ω3
}
. To prove the lemma, we must show that ~µRS permutes
these by σG, which in the case of Aℓ replaces each ωk with ωℓ+1−k.
Since ~µRS also consists entirely of source-or-sink mutations, it is a lso governed by primitive exchange
mutations. Let
~µA =
ℓ∏
k=1
ℓ−k∏
j=0
~µT(i, 1 +j), ~µB =
ℓ∏
j=1
~µT(i,ℓ −j),
so that ~µRS =~µA~µB. We make the following observations, which are all easily ch ecked by induction:
• During ~µA, whenever a vertex vk is mutated at with k odd, vk has coordinate ∆ cmωk,cmωk while
its neighbors have coordinates ∆ cm−1ωk−1,cm−1ωk−1 and ∆ cm−1ωk+1,cm−1ωk+1. Since k ≺c k ± 1, the
coordinate at vk becomes ∆ cm−1ωk+1,cm−1ωk+1 .
• During ~µA, whenever a vertex vk is mutated at with k even, vk has coordinate ∆ cmωk,cmωk and its
neighbors have coordinates ∆ cmωk−1,cmωk−1 and ∆ cmωk+1,cmωk+1. Since k ± 1 ≺c k, the coordinate
at vk becomes ∆ cm−1ωk+1,cm−1ωk+1.
• By the same logic as the above statements every mutation in ~µB takes the coordinate at vk from
∆ cmωk,cmωk to ∆ cm+1ωk,cm+1ωk .
Therefore, since ~µA touches vertex k a total of ℓ −k + 1 times and ~µB touches each vertex once, we may
conclude via Proposition 3.3 that after ~µA~µB the coordinates are given by
coordinate at vk is ∆ c(ℓ−k)/2+Y (ℓ)+Y (k)−(ℓ−k)ωk,c(ℓ−k)/2+Y (ℓ)+Y (k)−(ℓ−k)ωk .
Now, let us consider the diﬀerence between the exponents of c in the ﬁnal coordinate of vk and in the
initial coordinate of vk∗ . If the diﬀerence is −h(k∗;c) − 1, then Proposition 3.3 will show that ~µRS acts by
permuting vertices according to σG.
ﬁnal at k − initial at k∗ =
[ ℓ −k
2 +Y (ℓ) +Y (k) − (ℓ −k)
]
−
[ ℓ −k∗
2 +Y (ℓ) +Y (k∗)
]
= k∗ −k
2 − (ℓ −k) +Y (k) −Y (k∗)
= (ℓ + 1 −k) −k
2 − (ℓ −k) +Y (k) −Y (ℓ + 1 −k)
= −
[ ℓ + 1
2 −Y (k) +Y (ℓ + 1 −k)
]
− 1
=
{
−
[ ℓ+1
2 +Y (ℓ + 1)
]
− 1 ℓ + 1 −k odd
−
[ ℓ+1
2 −Y (ℓ + 1)
]
− 1 ℓ + 1 −k even(Fact 7.3)
=
{
−⌈ ℓ+1
2 ⌉ − 1 k∗ odd
−⌊ ℓ+1
2 ⌋ − 1 k∗ even
35
Consulting Proposition 3.2, the exponent diﬀerence is inde ed −h(k∗;c)−1, so the action of ~µRS is to rearrange
the vertices of QLin according to σG. From here, the action of ~µRS generalizes to larger quivers as in the
proof for ~µCS. □
