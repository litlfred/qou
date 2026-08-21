---
doc_id: arxiv-math-0411647v2
doc_title: "Asymptotics of characters of symmetric groups, genus expansion and free probability"
section_id: sec-007-22-partitions
section_title: "Partitions"
section_number: 2.2
pages: 13-22
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
doc_brief: "Asymptotics of characters of symmetric groups, genus expansion and free probability — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear"
---
14 PIOTR ´SNIADY
FIGURE 2.3. Graphical representation of a partition{
{1, 3 }, {2, 5, 7 }, {4}, {6}
}
.
2.2.1. Partitions. We recall that π = {π 1, . . . , π r} is a partition of a ﬁnite
ordered set X if sets π 1, . . . , π r are nonempty and disjoint and if π 1 ∪ · · · ∪
π r = X. We denote the set of all partitions of a set X by P(X). We call
sets π 1, . . . , π r blocks of the partition π. We say that elements a, b ∈ X
are connected by the partition π if they are the elements of the same block.
We will call elements of the set X the labels of the vertices of the partition
π. As usually, the numbers |π 1|, . . . , |π r|denote the numbers of elements in
consecutive blocks of π.
We say that a blockπ s is trivial if it contains only one element and a trivial
partitions has all blocks trivial. We say that a partition is a pair partition if
all its blocks contain exactly two elements.
We say that a partitionπ is ﬁner than a partition ρ of the same set if every
block of π is a subset of some block of ρ and we denote it by π ≤ ρ. The
restriction of a partition π to a set Y ⊆ X is a partition of Y which connects
elements a, b ∈ Y if and only if a, b are connected by π.
In the following we present some constructions on partition s of the set
X = {1, 2, . . . , n }. However, it should be understood that by a change of
labels these constructions can be performed for any ﬁnite ordered set X.
It is very useful to represent partitions graphically by arr anging the ele-
ments of the set X counterclockwise on a circle and joining elements of the
same block by a line, as it can be seen on Figure 2.3. Note that w e do not
need to write labels on the vertices in order to recover the partition from its
graphical representation if we mark the ﬁrst element as the ‘starting point’.
2.2.2. Fat partitions. Let π = {π 1, . . . , π r} be a partition of the set
{1, . . . , n }. For every 1 ≤ s ≤ r let π s = {π s,1 , . . . , π s,l s} with π s,1 <
· · · < π s,l s. We deﬁne π fat, called fat partition of π, to be a pair partition of
the 2n–element ordered set {1, 1 ′, 2, 2 ′, . . . , n, n ′}given by
π fat =
{
{π ′
s,t , π s,t +1}: 1 ≤ s ≤ r and 1 ≤ t ≤ ls
}
,
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 15
FIGURE 2.4. Fat partition π fat corresponding to the partition
π from Figure 2.3.
where it should be understood that π s,l s+1 = π s,1 .
This operation can be easily described graphically as follo ws: we draw
blocks of a partition with a fat pen and take the boundary of each block, as it
can be seen on Figure 2.4. This boundary is a collection of lines hence it is a
pair partition. However, every vertexk ∈ {1, . . . , n }of the original partition
π has to be replaced by its ‘right’ and ‘left’ copy (denoted respectively by k
and k ′). Please note that in the graphical representation of π fat we mark the
space between 1 and 1 ′ as the ‘starting point’.
2.2.3. Non–crossing partitions. We say that a partition π is non–crossing
[Kre72, SU91, Spe94, Spe97, Spe98] if for every i ⁄= j and a, c ∈ π i
and b, d ∈ π j it cannot happen that a < b < c < d . For example,
the partition from Figure 2.3 is crossing (as it can be easily seen from its
graphical representation) while a partition from Figure 2.5 is non–crossing.
The set of all non–crossing partitions of a set X will be denoted by NC(X)
and the set of all non–crossing pair partitions of a set X will be denoted by
NC2(X).
2.2.4. Kreweras complementation map. The function π ↦→ π fat which
maps partitions of a n–element set to pair partitions of a 2n–element set
is one to one but in general is not a bijection. However, it is a bijection
between NC(1, 2, . . . , n ) and NC2(1, 1 ′, . . . , n, n ′) [Kre72].
If ρ is a pair partition of the set{1, 1 ′, 2, 2 ′, . . . , n, n ′}, we denote by r(ρ)
a pair partition of the same set {1, 1 ′, . . . , n, n ′}which is obtained by cyclic
change of labels · · · → 2 ′ → 2 → 1 ′ → 1 → n ′ → n → · · · carried by
the vertices. In the graphical representation of a partitio n this corresponds
16 PIOTR ´SNIADY
FIGURE 2.5. Graphical representation of a non–crossing
partition
{
{1}, {2, 5, 6 }, {3, 4 }
}
.
FIGURE 2.6. Fat partition π fat for a non–crossing partition
π from Figure 2.5.
FIGURE 2.7. Graphical representation of r(ρ) where ρ is
given by Figure 2.6.
to a shift of the starting point by one counterclockwise (cf F igure 2.7). Of
course r is a bijection of the set NC2(1, 1 ′, . . . , n, n ′).
It follows that the map π ↦→ π comp, called Kreweras complementation
map, given by (π comp)fat = r(π fat) is well–deﬁned and is a permutation of
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 17
FIGURE 2.8. Partition π from Figure 2.5 in a solid line and
its Kreweras complement in a dashed line.
NC(1, 2, . . . , n ). Due to the canonical bijection between {1, 2, . . . , n }and
{1 ′, 2 ′, . . . , n ′} we can identify NC (1, 2, . . . , n ) with NC (1 ′, 2 ′, . . . , n ′)
and in the future we shall sometimes regard π comp as an element of
NC(1, 2, . . . , n ) and sometimes as an element of NC(1 ′, 2 ′, . . . , n ′). It will
be clear from the context which of the options we choose.
One can also state the above deﬁnition as follows: π comp is the biggest
non–crossing partition of the set {1 ′, 2 ′, . . . , n ′} with a property that π ∪
π comp is a non–crossing partition of the set{1, 1 ′, 2, 2 ′, . . . , n, n ′}(cf Figure
2.8).
We shall also consider the inverse of the Kreweras complementation map:
for π, ρ ∈ NC(1, 2, . . . , n ) we have π comp− 1 = ρ if and only if π = ρcomp.
One can observe that ρcomp− 1 and ρcomp are always cyclic rotations of each
other.
3. T HE FIRST MAIN RESULT : C ALCULUS OF PARTITIONS
3.1. Partition–indexed conjugacy class indicator Σ π .
3.1.1. Deﬁnition of Σ π . Let π be a partition of the set {1, . . . , n }. Since
the fat partition π fat connects every element of the set {1 ′, 2 ′, . . . , n ′}with
exactly one element of the set {1, 2, . . . , n }, we can view π fat as a bijec-
tion π fat : {1 ′, 2 ′, . . . , n ′} → {1, 2, . . . , n }. We also consider a bijection
c : {1, 2, . . . , n } → {1 ′, 2 ′, . . . , n ′} given by . . . , 3 ↦→ 2 ′, 2 ↦→ 1 ′, 1 ↦→
n ′, n ↦→ (n − 1) ′, . . . . Finally, we consider a permutation π fat ◦ c of the set
{1, 2, . . . , n }.
For example, for the partition π given by Figure 2.3 the composition
π fat ◦ c has a cycle decomposition (1, 2, 3, 5, 4 )(6, 7 ), as it can be seen from
Figure 3.1.
Alternatively, one can identify the set {1 ′, 2 ′, . . . , n ′} with the set
{1, 2, . . . , n }; then π fat becomes a permutation which coincides with the
18 PIOTR ´SNIADY
FIGURE 3.1. Bijection corresponding to the partition π fat
from Figure 2.4 plotted with a solid line and the bijection
c plotted with a dashed line. Lines corresponding to two
different cycles were plotted in different colors (gray and
black). The meaning of the additional decoration of some of
the vertices will be explained in Section 5.2.1.
construction from [Kre72, Bia97, Bia98] and c is equal to the full cycle
(n, n − 1, . . . , 2, 1 ).
We decompose the permutation
π fat ◦ c = (b1,1 , b 1,2 , . . . , b 1,j 1) · · ·(bt,1 , . . . , b t,j t)
as a product of disjoint cycles. Every cycle bs = ( bs,1 , . . . , b s,j s) can be
viewed as a closed clockwise path on a circle and therefore one can compute
how many times it winds around the circle. It might be useful t o draw
a line between the central disc and the starting point (cf Fig ure 3.2); the
number of winds is equal to the number of times a given cycle cr osses this
line and therefore is equal to the number of indices 1 ≤ i ≤ js such that
bs,i ≤ bs,i +1, where we use the convention that bs,j s+1 = bs,1.
To a cycle bs we assign the number
(3.1) ks = (number of elements in a cycle bs)−
(number of clockwise winds of bs).
In the above example we have b1 = ( 1, 2, 3, 5, 4 ), b2 = ( 6, 7 ) and k1 =
2, k2 = 1, as it can be seen from Figure 3.2, where all lines clockwise wind
around the central disc.
Alternatively, we can treat every cycle bs of π fat ◦ c as a closed counter–
clockwise path on a circle (cf Figure 3.3). Equation (3.1) implies that
(3.2) ks = (number of counterclockwise winds of the cycle bs).
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 19
FIGURE 3.2. A version of Figure 3.1 in which all lines wind
clockwise around the central disc.
FIGURE 3.3. A version of Figure 3.1 in which all lines of
π fat wind counterclockwise around the central disc.
Let a positive integer q be given. In Section 5 we shall deﬁne the most
important tool of this article: a certain mapΦ P
C(~S∞ ) from the set of partitions
to C(~S∞). The following Claim states thatΦ P
C(~S∞ )(π ) is closely related with
the normalized conjugacy class indicators from Section 2.1.10 of Section 2
and hence Σ π := Φ P
C(~S∞ )(π ) can be viewed as a normalized conjugacy class
indicator which is indexed by a partition π instead of a tuple of integers
(k1, . . . , k t).
Claim 3.1. Let π be a partition of the set {1, 2, . . . , n } and let numbers
k1, . . . , k t be given by the above construction. Then
Σ π := Φ P
C(~S∞ )(π ) = Σ k1 ,...,k t ,
20 PIOTR ´SNIADY
where Σ k1,...,k t ∈ C(~S∞) on the right–hand side should be understood as in
Section 2.1.10.
This Claim will follow from Theorem 5.7. Reader not interest ed in too
technical details may even take this Claim as a very simple alternative deﬁ-
nition of Σ π = Φ P
C(~S∞ )(π ).
3.1.2. Basic properties of Σ π . We say that partitions π and π ′ are cyclic
rotations of each other if one can obtainπ ′ from π by a cyclic shift of labels
of vertices. Graphically, this corresponds to a change of a m arked starting
point on a circle.
Proposition 3.2. Let π and π ′ be two partitions of the same set which are
cyclic rotations of each other. Then
Σ π = Σ π ′.
Proof. It is enough to observe that the winding numbers considered i n the
algorithm from Section 3.1.1 do not depend on the choice of th e starting
point. □
Proposition 3.3. If partition π connects some neighbor elements thenΣ π =
0.
Proof. If partition π connects some r with r + 1 then π fat connects r ′ with
r + 1, hence π fat(r ′) = r + 1 and (π fat ◦ c)(r + 1) = r + 1. One of the cycles
of π fat ◦ c is a 1–cycle bs = ( r + 1) and one can easily check that ks = 0.
Claim 3.1 implies that Σ π = Σ k1 ,...,k t = 0. □
3.1.3. Degree of Σ π and its geometric interpretation. We keep the notation
from the previous Section; in particular t denotes the number of cycles of
π fat ◦ c and r the number of blocks of π. Observe that
∑
1≤s≤t
(number of elements in a cycle bs) = n.
Furthermore ∑
1≤s≤t(number of clockwise winds of bs) is equal to the
total number of clockwise winds of π fat ◦ c. When we identify sets
{1, 2, . . . , n }and {1 ′, 2 ′, . . . , n ′}then c is a full clockwise cycle and it con-
tributes with a one wind. It is easy to observe that every block π s of partition
π is a counterclockwise cycle of the permutation π fat, hence when we treat
it as a collection of clockwise steps it contributes with |π s|− 1 clockwise
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 21
FIGURE 3.4. The ﬁrst collection of discs for partition π
from Figure 2.3.
winds. It follows that
∑
1≤s≤t
(number of clockwise winds of bs) =
1 +
∑
1≤s≤r
(|π s|− 1) = n − r + 1
since ∑
1≤s≤r |π s|= n. Therefore (3.1) gives us
(3.3) deg Σ π = k1 + · · · + kt + t = r + t − 1,
where the degree is taken with respect to the ﬁltration (2.8).
We can ﬁnd a natural geometric interpretation of (3.3): cons ider a large
sphere with a small circular hole. The boundary of this hole i s the cir-
cle that we consider in the graphical representations of par titions. Some
pairs of points on this circle are connected by lines: the blo cks of the
partition π fat. To the arcs on the boundary of the circle between points
1, 1 ′, 2, 2 ′, . . . , n, n ′ and to the lines of π fat we shall glue two collections of
discs. Every disc from the ﬁrst collection corresponds to on e of the blocks
of π (cf Figure 3.4).
After gluing the ﬁrst collection of discs, our sphere become s a surface
with a number of holes. The boundary of each hole corresponds to one of
the cycles of π fat ◦ c and we shall glue this hole with a disc from the second
collection.
Thus we obtained an orientable surface without a boundary. W e deﬁne
the genus of the partition π to be the genus of this surface. The numbers
of vertices, edges and faces of the polyhedron constructed a bove are the
following: V = 2n, E = 3n, F = 1 + r + t therefore the genus of this
22 PIOTR ´SNIADY
surface is equal to
(3.4) genus π = 2 − V + E − F
2 = n + 1 − r − t
2 .
We proved therefore the following result.
Proposition 3.4. For any partition π of an n–element set
(3.5) deg Σ π = n − 2 genusπ ,
where the degree is taken with respect to the ﬁltration(2.8).
We leave the proof of the following simple result to the reader.
Proposition 3.5. A partition is non–crossing if and only if its genus is equal
to zero.
