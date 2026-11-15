---
doc_id: 0307092v2
doc_title: "Extended Bloch group and the Cheeger–Chern–Simons class"
section_id: sec-008-6-the-cycle-relation
section_title: "The cycle relation"
section_number: 6
pages: 23-26
source_pdf: 0307092v2.pdf
source_sha256: de2f7ddec49b2ce6
toc_source: outline
doc_brief: "Extended Bloch group and the Cheeger–Chern–Simons class — We deﬁne an extended Bloch group and show it is naturally isomorphic to H3(PSL(2, C)δ; Z)."
---
The cycle relation
In this section we prove a general relation called the “cycle relation,” that holds
in bP(C). We will use it repeatedly later. It is, in fact, a consequence of the
ﬁve-term relation (2) alone and does not involve the transfer relation (3).
Let K be a simplicial complex obtained by gluing 3–simplices ∆1, . . . , ∆n to-
gether in sequence around a common 1–simplex E. Thus, for each index j
modulo n, ∆j is glued to each of ∆j−1 and ∆j+1 along one of the two faces of
∆j incident to E. Suppose, moreover, that the vertices of each ∆j are ordered
such that orderings agree on the common 2–faces of adjacent 3–simplices.
There is then a sequence ǫ1 = ±1, . . ., ǫn = ±1 such that the 2–faces used for
gluing all cancel in the boundary of the 3–chain Pn
j=1 ǫj∆j . (Proof: choose
ǫ1 = 1 and then for i = 2, . . . , n choose ǫi so the common face of ∆i−1 and ∆i
cancels. The common face of ∆n and ∆1 must then cancel since otherwise that
face occurs with coeﬃcient ±2 in ∂Pn
j=1 ǫj∆j , and E occurs with coeﬃcient
±2 in ∂∂Pn
j=1 ǫj∆j .)
Geometry & Topology, Volume 8 (2004)
436
Walter D Neumann
E
Figure 4: Conﬁguration for the cycle relation
Suppose now further that a combinatorial ﬂattening wi has been chosen for
each ∆j such that the “signed sum” of log parameters around the 1–simplex
E vanishes and the same for parity parameters:
n
X
j=1
ǫjlE(∆j, wj) = 0,
n
X
j=1
ǫjδE(∆j, wj) = 0.
(6)
We think of the 1–simplex E as being vertical, so that we can label the two
1–simplices other than E of the common triangle of ∆j and ∆j+1 as Tj and
Bj (for “top” and “bottom”).
Let w′
j be the ﬂattening obtained from wj
by adding ǫjπi to the log parameter at Tj and its opposite edge in ∆j and
subtracting ǫjπi from the log parameter at Bj and its opposite edge in ∆j . If
we do this for each j then the total log parameter (and, by Corollary 5.4, also
parity parameter) around any 1–simplex of the complex K is not changed (we
sum log-parameters with the appropriate sign ǫj ): — at E no log-parameter
has changed while at every other 1–simplex πi has been added at one of the
two adjacent 3–simplices and subtracted at the other.
Lemma 6.1 (Cycle relation about E) With the above notation,
n
X
j=1
ǫj[wj] =
n
X
j=1
ǫj[w′
j]
∈bP(C),
where we are using [w] as a shorthand for [ℓ−1w] (ie, [w] means [z; p, q] where
ℓ(z; p, q) = w; see Lemma 3.2).
Proof Each of the 3–simplices ∆i has an associated ideal hyperbolic struc-
ture compatible with the combinatorial ﬂattenings wj . This ideal hyperbolic
structure is also compatible with the ﬂattening w′
j. Choose a realization of ∆1
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class
437
as an ideal simplex in H
3. We think of this as a mapping of ∆1 to H
3. We can
extend this to a mapping of K to H
3 which maps each ∆j to an ideal simplex
with shape appropriate to its combinatorial ﬂattening. Adjacent simplices will
map to the same side of their common face in H
3 if either their orientations
or the signs ǫj do not match and will be on opposite sides otherwise. The fact
that the signed sums of log and parity parameters around the 1–simplex E are
zero guarantees that the identiﬁcations match up as we go once around E.
Note that K has n + 2 vertices. We ﬁrst consider the special case that n = 3
and there is an ordering v0, . . . , v4 of the ﬁve vertices of K that restricts to the
given vertex ordering for each simplex. We also assume the ﬁve vertices of K
map to distinct points z0, . . . , z4 of ∂H3.
Each 3–simplex ∆j for j = 1, 2, 3 has vertices obtained by omitting one of
the ﬁve vertices v0, . . . , v4. Denote by ∆4 and ∆5 the 3–simplices obtained
by omitting each of the other two vertices.
The fact that the common 2–
faces of the ∆j cancel when taking boundary of the chain ǫ1∆1 + ǫ2∆2 + ǫ3∆3
means that, up to sign this sum corresponds to three summands of the chain
∂⟨v0, . . . , v4⟩= P(−1)i⟨vo, . . . , ˆvi, . . . , v4⟩. Choose ǫ4 and ǫ5 so that P5
j=1 ǫj∆j
is ±∂⟨v0, . . . , v4⟩.
By Lemma 3.5, we can choose unique combinatorial ﬂattenings w4 and w5 of
∆4 and ∆5 so that the signed sum of log parameters and parity parameters
around any 1–simplex of K ∪∆4 ∪∆5 is zero. Note that w4 and w5 do not
change if we replace w1, . . . , w3 by w′
1, . . . , w′
3. By Lemma 3.4 we then have
ǫ1w1 + ǫ2w2 + ǫ3w3 = −(ǫ4w4 + ǫ5w5)
ǫ1w′
1 + ǫ2w′
2 + ǫ3w′
3 = −(ǫ4w4 + ǫ5w5),
proving this case.
We next consider the case that for some index j modulo n the images of ∆j and
∆j+1 in H
3 do not coincide, so their union has ﬁve distinct vertices. By cycling
our indices we may assume j = 1. Since the orderings of the vertices of ∆1 and
of ∆2 agree on the three vertices they have in common, there is an ordering
of all ﬁve vertices compatible with both ∆1 and ∆2. Let ∆0 be the simplex
determined by the common 1–simplex E and the two vertices that ∆1 and ∆2
do not have in common. Then there is an ǫ0 = ±1 such that the common faces of
∆0, ∆1, and ∆2 cancel in the boundary of the chain ǫ0∆0+ǫ1∆1+ǫ2∆2. Choose
a ﬂattening w0 of ∆0 such that ǫ0lE(∆0, w0)+ǫ1lE(∆1, w1)+ǫ2lE(∆2, w2) = 0.
Then the relation of the lemma has already been proved for w0, w1, w2, and
by subtracting this relation from the relation to be proved for w1, . . . , wn we
Geometry & Topology, Volume 8 (2004)
438
Walter D Neumann
obtain a case of the lemma with one fewer simplices. Thus, if we assume the
lemma proved for n −1 simplices then this case is also proved.
The above induction argument fails only for the case that there are 2m simplices
that alternately “fold back on each other” so that their images in H
3 all have
the same four vertices. The above induction eventually reduces us to this case
(usually with m = 1). We must therefore deal with this situation to complete
the proof. We ﬁrst consider the case that m = 1 so n = 2. We then have
four vertices z0, . . . , z3 in ∂H
3. We assume the 1–simplex E is z0z1. Then the
ordering of the vertices of the faces z0z1z2 and z0z1z3 is the same in each of ∆1
and ∆2. Choose a new point z4 in ∂H
3 distinct from z0, . . . , z3 and consider
the ordered simplex with vertices z0, z1, z2 ordered as above followed by z4.
Call this ∆3. Similarly make ∆4 using z0, z1, z3 ordered as above followed by
z4. Choose ﬂattenings of ∆3 and ∆4 so that the signed sum of log parameters
for ∆1, ∆3, ∆4 around E is zero. Then we obtain a three simplex relation of
the type already proved for ∆1, ∆3, ∆4 and another for ∆2, ∆3, ∆4, and the
diﬀerence of these two relations gives the desired two-simplex relation.
More generally, if we are in the above “folded” case with m > 1 we can use an
instance of the three-simplex relation to replace one of the 2m simplices by two.
We then use the induction step to replace one of these new simplices together
with an adjacent old simplex by one simplex and then repeat for the other
new simplex. In this way we reduce to a relation involving 2m −1 simplices,
completing the proof.
7
