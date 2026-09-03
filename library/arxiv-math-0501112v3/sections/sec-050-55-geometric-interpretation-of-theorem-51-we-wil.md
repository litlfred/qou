---
doc_id: arxiv-math-0501112v3
doc_title: "GAUSSIAN FLUCTUATIONS OF CHARACTERS OF"
section_id: sec-050-55-geometric-interpretation-of-theorem-51-we-wil
section_title: "Geometric interpretation of Theorem 5.1. We will use the notations"
section_number: 5.5
pages: 30-32
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
doc_brief: "GAUSSIAN FLUCTUATIONS OF CHARACTERS OF — We study asymptotics of reducible representations of the symmetric groups Sq for large q."
---
of Theorem 5.1. On the surface of a large sphere we draw a small circle on
which we mark counterclockwise points i1 + 1, i 1 + 2, . . . , i r+1. Inside the
circle we cut r holes; for any 1 ≤ s ≤ r the corresponding hole has a
shape of a disc, the boundary of which passes through the poin ts from the
block ρs. For every 1 ≤ s ≤ r the partition π s connects some points on the
boundary of the hole ρs and this situation corresponds exactly to the case
we considered in Section 5.4. We shall glue to the hole ρs only the ﬁrst
collection of discs that we considered in Section 5.4, i.e. t he discs which
correspond to the blocks of the partition π s. Thus we obtained a number of
holes with a collection of glued discs (cf Figure 5.3).
When we inﬂate the original small holes inside the circle we m ay think
about this picture alternatively: instead of r small holes we have a big
one (in the shape of the circle) but some arcs on its boundary a re glued
by an additional disc (on Figure 5.4 drawn in black) glued to v ertices
i2, i 3, . . . , i r+1. Furthermore we still have a collection of all discs (on Figure
5.4 drawn in gray) corresponding to partitions π s. We merge the additional
black disc to a gray disc from this collection if they touch th e same ver-
tex. After this merging the collection of discs corresponds to the partition
π 1 • · · · • π r =
{
{i2, i 3, . . . , i r+1}
}
∨ (π 1 ∪ · · · ∪ π r) which appears in the
formula (5.4) for the disjoint product.
The last step is to consider all ways of merging of the discs (o r equiva-
lently: all partitions σ ≥ π 1•· · ·• π r) with the property that any two vertices
GAUSSIAN FLUCTUATIONS OF CHARACTERS OF SYMMETRIC GROUPS 31
FIGURE 5.4. Figure 5.3 after inﬂating small holes.
that were lying on the boundary of the same small hole ρs if were not con-
nected by a disc from the collection π s then they also cannot be connected
after all mergings. In this way we obtain all partitions whic h contribute to
(5.5).
By splitting the holes (we recall that each hole corresponds to some set
ρi) into some new holes we can view the surface associated to the partition
ρ as a sphere with a number of new holes glued in pairs by handles and the
number of these handles is equal to the genus of the surface. I n this way
we obtain a graph Gσ the vertices of which correspond to the old holes (or,
equivalently, sets ρi) and the edges correspond to the handles between new
holes. Of course the above construction can be sometimes per formed in
many different ways but we do not mind it. Note that multiple c onnections
between vertices are allowed. Also, a vertex can be connecte d with itself
and the number of such loops is equal to the genus of the corres ponding
partitions π i. The genus of σ is equal to the total number of edges in Gσ .
In order to obtain all partitions σ which contribute to (5.6) we should
restrict our attention only to σ such that the graph Gσ is connected. A
connected graph with n vertices has at least n − 1 non-loop edges therefore
(5.10) genus σ ≥ genusπ 1 + · · · + genusπ n +(n − 1).
Proof of Theorem 4.3. In order to prove (4.5) for the special case whenxi =
Σ π i it is enough to apply Proposition 5.2 and (5.10).
It remains now to prove (4.6) and we shall do it in the followin g. We
use the notations of Theorem 5.1 if n = 2 and π 1, π 2 are trivial partitions
(every blocks consists of a single element). Let σ be a partition which
contributes to (5.6) with the minimal possible genus, namel y genusσ = 1.
It follows that one of the blocks of σ is equal to {i2, i 3}. Secondly, some
32 PIOTR ´SNIADY
of the elements of the set {i1 + 1, . . . , i 2 − 1} (but at least one of them)
are paired with some of the elements of the set {i2 + 1, . . . , i 1 + i3 − 1};
this pairing however is not arbitrary. Let us travel counter clockwise along
the boundary of the hole corresponding to the block π 1; in other words
we visit the vertices in the order i1 + 1 → i1 + 2 → · · · → i2 − 1 →
i1 + 1. Some of these vertices are paired by σ with some of the elements
of {i2 + 1, . . . , i 3 − 1} corresponding to the other hole; let us have a look
in which order these counterparts appear during our walk. Fr om the very
deﬁnition of the genus of a partition we know that it is possib le to draw
the blocks of σ \
{
{i2, i 3}
}
on the surface of the handle in such a way that
lines do not cross. It follows that these counterparts will b e visited in the
clockwise order i3 − 1 → i3 − 2 → · · · → i2 + 1 → i3 − 1, cf Figure 5.5.
Let a1, . . . , a r denote the distances (counted cyclically counterclock-
wise) between consecutive elements of the pairs in the ﬁrst h ole and let
b1, . . . , b r denote the distances (counted cyclically counterclockwis e) be-
tween consecutive elements of the pairs in the second hole. R eaders ac-
quainted with the results of Section 5.7 will see that
Σ σ = Σ a1 +b1 − 1,...,a r +br − 1.
It is easy to see that a1 + · · · + ar = i2 − i1 and b1 + · · · + br = i3 − i2.
Such sequences (ai) and (bi) uniquely determine σ once we specify the
ﬁrst element in each cycle (there are i2 − i1 − 1 choices for the ﬁrst one
and i3 − i2 − 1 choices for the second one). Partition σ can be represented
like this in r different ways which correspond to the cyclic rotations of t he
sequences (ai) and (bi). Since Σ π 1 = Σ i2 − i1− 1 and Σ π 2 = Σ i3 − i2 − 1 this
ﬁnishes the proof of (4.6). □
