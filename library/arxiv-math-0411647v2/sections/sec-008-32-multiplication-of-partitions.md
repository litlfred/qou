---
doc_id: arxiv-math-0411647v2
doc_title: "Asymptotics of characters of symmetric groups, genus expansion and free probability"
section_id: sec-008-32-multiplication-of-partitions
section_title: "Multiplication of partitions"
section_number: 3.2
pages: 22-26
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
doc_brief: "Asymptotics of characters of symmetric groups, genus expansion and free probability — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear"
---
3.2.1. Deﬁnition of multiplication. We will introduce an algebraic structure
on the partitions. For any ﬁnite ordered setX one can consider a linear space
spanned by all partitions of X. We will deﬁne a ‘multiplicative’ structure as
follows: let ρ = {ρ1, . . . , ρ r}be a non–crossing partition of a ﬁnite ordered
set X and for every 1 ≤ s ≤ r let π s be a partition of the set ρs. We deﬁne
the ‘ρ–ordered product’ of partitionsπ s by
(3.6)
∏
s
π s :=
∑
σ 
σ,
where the sum denotes a formal linear combination and it runs over all
partitions σ of the set X such that
(1) for any a, b ∈ ρs, 1 ≤ s ≤ r we have that a and b are connected by
σ if and only if they are connected by π s,
(2) σ ≥ ρcomp− 1,
where ≥ denotes the order on partitions we introduced in Section 2.2.1.
Above we deﬁned the product of the elements of the basis of the lin-
ear space; by requirement that multiplication is distribut ive the deﬁnition
extends uniquely to general vectors.
For example, for
(3.7) ρ1 = {1, 2, 7, 8 }, ρ 2 = {3, 4, 5, 6 },
π 1 =
{
{1, 7 }, {2}, {8}
}
, π 2 =
{
{3, 5 }, {4, 6 }
}
we have
π 1 · π 2 =
{
{1, 7 }, {2, 4, 6 }, {3, 5 }, {8}
}
+
{
{1, 7 }, {2, 4, 6 }, {3, 5, 8 }
}
+
{
{1, 3, 5, 7 }, {2, 4, 6 }, {8}
}
.
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 23
FIGURE 3.5. Graphical representation of example (3.7).
3.2.2. Geometric interpretation of partitions multiplication. Suppose for
simplicity that X = {1, 2, . . . , n }. On the surface of a large sphere we draw
a small circle on which we mark counterclockwise points 1, 2, . . . , n . In-
side the circle we cut r holes; for any 1 ≤ s ≤ r the corresponding hole has
a shape of a disc, the boundary of which passes through the points from the
block ρs (it is possible to perform this operation since ρ is non–crossing).
For every 1 ≤ s ≤ r the partition π s connects some points on the boundary
of the hole ρs and this situation corresponds exactly to the case we consid-
ered in Section 3.1.3. We shall glue to the hole ρs only the ﬁrst collection
of discs that we considered in Section 3.1.3, i.e. the discs which correspond
to the blocks of the partition π s. Thus we obtained a number of holes with
a collection of glued discs (cf Figure 3.5).
When we inﬂate the original small holes inside the circle we m ay think
about this picture alternatively: instead of r small holes we have a big one
(in the shape of the circle) but some arcs on its boundary are g lued by ex-
tra discs (on Figure 3.6 drawn in black) given by the partitio n ρcomp− 1 ∈
NC(1, 2, . . . , n ). Furthermore we still have all discs (on Figure 3.6 drawn
in gray) corresponding to partitions π s. We merge discs from these two col-
lections if they touch the same vertex. After this merging th e collection of
discs corresponds to the partition ρcomp− 1 ∨ (π 1 ∪ · · · ∪π t), i.e. the smallest
partition which is bigger than both ρcomp− 1 and π 1 ∪ · · · ∪ π t.
The last step is to consider all ways of merging of the discs (o r equiva-
lently: all partitions σ ≥
(
ρcomp− 1 ∨ (π 1 ∪ · · · ∪π t)
)
) with the property that
any two vertices that were lying on the boundary of the same small hole ρs
if were not connected by a disc from the collectionπ s then they also cannot
be connected after all mergings.
24 PIOTR ´SNIADY
FIGURE 3.6. Figure 3.5 after inﬂating small holes.
3.3. Map Σ is a homomorphism. Since the map Σ = Φ P
C(~S∞ ) was deﬁned
on the basis of the linear space of partitions, we can extend i t linearly in
a unique way. It turns out that Φ P
C(~S∞ ) preserves also the multiplication
hence it is a homomorphism. However, since we consider only ‘ρ–ordered’
products of partitions, we have to state it in a bit unusual way.
Claim 3.6. Let ρ = {ρ1, . . . , ρ r} be a non–crossing partition of the set
{1, 2, . . . , n } and for every 1 ≤ s ≤ r let π s be a partition of the set ρs.
Then
Σ
( ∏
s
π s
)
=
∏
1≤s≤r
Σ π s ,
where the multiplication on the left hand side should be unde rstood as the
ρ–ordered product of partitions and on the right hand side it s hould be
understood as the usual product of commuting elements in C(~S∞).
This Claim will follow from Theorem 5.11. Due to distributivity of mul-
tiplication the above Claim remains true if we allowπ s to be a linear combi-
nation of partitions. It would be very interesting to prove Claim 3.6 directly
if one treats Claim 3.1 as a deﬁnition of Σ π .
The following result was proved in [KO94, IK99, LT01, Bia03].
Corollary 3.7. For any choice of tuples of positive integers (k1, . . . , k m )
and (k ′
1, . . . , k ′
n) there exists a function f with a ﬁnite support deﬁned on
the set of the tuples of integers such that
(3.8) Σ k1 ,...,k m · Σ k′
1 ,...,k ′n =
∑
p1 ,...,p r
fp1 ,...,p r Σ p1 ,...,p r .
Proof. It is enough to ﬁnd partitions π, π ′ such that Σ π = Σ k1 ,...,k m, Σ π ′ =
Σ k′
1 ,...,k ′n and use the fact that Σ π Σ π ′ = Σ π ·π ′. □
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 25
More detailed information about the product Σ k1 ,...,k m · Σ k′
1 ,...,k ′n is pro-
vided by the following result which was proved by Ivanov and O lshanski
[IO02].
Corollary 3.8. For any choice of integersk1, . . . , k m , k ′
1, . . . , k ′
n ≥ 1 let us
express the product Σ k1 ,...,k m · Σ k′
1 ,...,k ′n ∈ C(~S∞) as a linear combination
of normalized conjugacy class indicators Σ . Then
Σ k1 ,...,k m · Σ k′
1 ,...,k ′n = Σ k1 ,...,k m,k ′
1 ,...,k ′n +
(terms of degree at most k1 + · · · + km + k ′
1 + · · · + k ′
n + m + n − 2)
and therefore (2.8) indeed deﬁnes a ﬁltration.
Proof. Deﬁne li = ki + 1 and l ′
i = k ′
i + 1. We set π 1 to be a partition of the
set of consecutive integers ρ1 = {1, . . . , l 1 + · · · + lm }which has only one
non–trivial block π 1
1 = {l1, l 1+l2, l 1+l2+l3, . . . , l 1+· · ·+lm }and let π 2 be
a partition of the set of consecutive integersρ2 = {l1+· · ·+lm +1, l 1+· · ·+
lm +2, . . . , l 1+· · ·+lm +l ′
1+· · ·+l ′
n}which has only one non–trivial block
π 2
1 = {l1+· · ·+lm +l ′
1, l 1+· · ·+lm +l ′
1+l ′
2, . . . , l 1+· · ·+lm +l ′
1+· · ·+l ′
n};
all the other blocks of these partitions consist of single el ements. One can
easily check that Σ π 1 = Σ k1 ,...,k m and Σ π 2 = Σ k′
1 ,...,k ′n. We set ρ = {ρ1, ρ 2};
let us compute the ρ–ordered product π 1 · π 2.
Equation (3.5) implies that the terms of the maximal degree l1 + · · · +
lm +l ′
1+· · ·+l ′
n will correspond to non–crossing partitions (genus equal to
zero) and the degree corresponding to any crossing partition cannot exceed
l1 + · · ·+ lm + l ′
1 + · · · + l ′
n − 2. It is enough to show that there is only one
non–crossing partition σ which contributes to π 1 · π 2, namely the partition
τ = (π 1 ∪ π 2) ∨ ρcomp− 1 which has only one non–trivial blockπ 1
1 ∪ π 2
1. This
statement is pretty obvious from the geometric interpretation; we provide a
more detailed proof below.
Let us consider a partition σ ⁄= τ which contributes to π 1 · π 2. Of course
we have σ ≥ τ. Let a, c be a pair of elements which are connected by σ
and are not connected by τ; by the deﬁnition of the product of partitions a
and c cannot be both elements of ρ1 or both elements of ρ2 so let us assume
that a ∈ ρ1 and c ∈ ρ2.
Suppose that a ∈ π 1
1; then c /∈ π 2
1 (otherwise a and c would be connected
by τ). It follows that there is an element of ρ2 \ π 2
1, namely c, which is
connected by σ with a ∈ π 1
1, and the latter element must be connected byσ
with the elements of π 2
1. This contradicts the deﬁnition of π 1· π 2. Therefore
a /∈ π 1
1 and similarly we show that c /∈ π 2
1.
It follows that a tuple a, b, c, d with b = l1 + · · · + lm , d = l1 + · · · +
lm + l ′
1 + · · · + l ′
n is the one required for σ to be crossing.
□
26 PIOTR ´SNIADY
4. F REE CUMULANTS OF PARTITIONS
