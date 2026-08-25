---
doc_id: arxiv-0805.1447v2
doc_title: "Braid ordering and the geometry of closed braid"
section_id: sec-001-2-braid-ordering-and-dehornoy-floor
section_title: "Braid ordering and Dehornoy floor"
section_number: 2
pages: 4-6
source_pdf: 0805.1447v2.pdf
source_sha256: b7ee20b0a7f5f3da
doc_brief: "Braid ordering and the geometry of closed braid — The relationships between braid ordering and the ge- ometry of its closure is studied."
---
In this section we review some of fundamental facts of Dehornoy
ordering and Dehornoy ﬂoor. Braid group Bn is, by deﬁnition, a group
which is presented by
⟨σ1, · · · , σ n−1|σiσjσi = σjσiσj if |i − j| = 1, σ iσj = σjσi if |i − j| ≥ 2⟩.
Geometrically, elements of braid group β ∈ Bn are represented by
braided n-strands which move from above to below, oriented downward.
By connecting their endpoints of strands canonically, we obtain an
oriented link. We denote this link by ˆβ and call closed braid or closure
of β .
We call the braid ( σ1σ2 · · · σn−1)(σ1σ2 · · ·σn−2) · · ·(σ1σ2)(σ1) Gar-
side’s fundamental braid and denote it by ∆. The Garside fundamental
braid∆ plays an important role in braid groups. It is known that ∆ 2
generates the center of Bn, which is an inﬁnite cyclic group. For these
basic facts about braid group, see [B].
2.1. Dehornoy ordering, Dehornoy ﬂoor. In this section we give
a brief exposition of left-invariant total ordering of braid groups c alled
Dehornoy ordering, and deﬁne Dehornoy ﬂoor. Dehornoy ﬂoor is ﬁ rst
introduced in [MN], though they do not use term Dehornoy ﬂoor. This
is a measure of how far braid is from the identity elements with respec t
to Dehornoy ordering and can be seen as some kinds of complexity of
BRAID ORDERING AND THE GEOMETRY OF CLOSED BRAID 5
braids. We describe fundamental results about Dehornoy ﬂoor, p roved
in [MN],[Ma].
A braid β ∈ Bn is called σ-positive if β can be represented by a word
which contains at least one σi, and contains no σ ±1
1 , σ ±1
2 · · · , σ ±1
i−1, σ −1
i
for some 1 ≤ i ≤ n − 1. we say α < β is true if and only if the
braid α −1β is σ-positive. It is known that the relation < deﬁnes left-
invariant total ordering of Bn; That is, < is total ordering and if braids
α, β ∈ Bn satisfy α < β , then for all braid γ ∈ Bn, γα < γβ holds. We
call this ordering Dehornoy ordering. Dehornoy ordering has following
nice property, called property S or Subword property.
Propotition 1 (Property S ([DDR W])). For any braids β1, β 2 ∈ Bn
and 1 ≤ i ≤ n − 1,
β1σiβ2 > β 1β2 > β 1σ −1
i σ2
holds.
As we mentioned at introduction, there are many other interpreta -
tion and deﬁnition of Dehornoy ordering. See [DDR W] for those oth er
deﬁnitions and meanings. We will describe one of the geometrical def -
inition later. Using Dehornoy ordering, we deﬁne Dehornoy ﬂoor of
braids [ β ]D as follows.
Deﬁnition 1. Dehornoy ﬂoor [β ]D of braid β ∈ Bn is a minimal
non-negative integer m which satisﬁes β ∈ (∆ −2m−2, ∆ 2m+2), where
(∆ −2m−2, ∆ 2m+2) = {α ∈ Bn | ∆ −2m−2 < α < ∆ 2m+2}.
Now we remark one important facts. We must be careful that when
we think about Dehornoy ﬂoor, which Bn a braid β belongs to is very
important. For example, for a braid β = ( σ1σ2)4, [ β ]D = 1 if we
consider β ∈ B3, and [ β ]D = 0 if we consider β ∈ B4. Fortunately,
if we use braid groups to describe links, the number of strands are
always implicit, so there might be no confusion about the number of
braid strands. So in most cases, we omit to write which Bn a braid
β belongs to. we also remark that Dehornoy ﬂoor is not a conjugacy
invariant of braids. For example, 3-braid ∆ 2σ1σ −1
2 has Dehornoy ﬂoor
1 but its conjugation ∆ −1(∆ 2σ1σ −1
2 )∆ = ∆ 2σ2σ −1
1 has zero Dehornoy
ﬂoor. This is mainly because Dehornoy ordering is not right-invariant ;
That is, it does not hold that for every γ ∈ Bn, αγ < βγ whenever
α < β . Thus, Dehornoy ﬂoor is far from knot invariant.
The most important property of Dehornor ﬂoor is that it can be see n
as some kinds of restriction for admissibility of braid moves. We sum-
marize the basic properties of Dehornoy ﬂoor, all of which are prov ed
in [MN], or [Ma].
6 TETSUYA ITO
Propotition 2 ([MN],[Ma]). Let α, β ∈ Bn. Then following holds.
(1) If braid β ∈ Bn is represented by braid word which contains s oc-
currence of σ1 and k occurrence of σ −1
1 , then [β ]D < max{s, k }.
(2) |[β ]D − [β ′]D| ≤ 1 if β and β ′ are conjugate.
(3) [ αβ ]D ≤ 1 + [α ]D + [β ]D.
(4) If closure of braid β ∈ Bn admit destabilization or exchange
move, [β ]D ≤ 1.
(5) For every n, there exist positive integer r(n) such that for every
β ∈ Bn, if [β ]D > r (n) then ˆβ is the unique closed n-braid
representative of link types represented by its closure. Th at is,
if ˆβ = ˆβ ′ holds for some β ′ ∈ Bn, β and β ′ are conjugate.
We remark that Dehornoy ﬂoor is not a conjugacy invariant but
proposition 2 (2) shows taking conjugate changes Dehornoy ﬂoor at
most by one.
Remark 1. Our deﬁnition of Dehornoy ﬂoor is slightly diﬀerent from
one in [Ma]. Our deﬁnition is rather after [MN]. We adopt this deﬁni-
tion because for application of knot theory, this formulation seems to
be more natural and makes statement of results simple.
Remark 2. There exist an inﬁnite family of left-invariant total order-
ing of braid groups, containing Dehornoy ordering, called Thurston-
type ordering (See [DDR W] or [SW]). Most of results in this paper can
be stated by using Thurston-type ordering instead of using Dehor noy
ordering, especially using ”Thurston ﬂoor” deﬁned by the similar way .
