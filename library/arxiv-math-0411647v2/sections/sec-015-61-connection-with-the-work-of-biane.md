---
doc_id: arxiv-math-0411647v2
doc_title: "Asymptotics of characters of symmetric groups, genus expansion and free probability"
section_id: sec-015-61-connection-with-the-work-of-biane
section_title: "Connection with the work of Biane"
section_number: 6.1
pages: 53-57
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
doc_brief: "Asymptotics of characters of symmetric groups, genus expansion and free probability — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear"
---
article [Bia98] was pointed out to me by Philippe Biane.
Biane shows [Bia98] that the matrix Γ deﬁned in (2.1) fulﬁlls
MJM
n = 1
q + 1 Tr Γn =
1
q + 1
∑
p1 ,...,p n ∈{1,...,q +1}
Γp1p2 Γp2 p3 · · · Γpn− 1pn Γpn p1 ,
where the sum runs only over tuples (p1, . . . , p n) such that no neighbor
elements are equal. Under identiﬁcation ∗ = q + 1 summands in Biane’s
formula coincide with pushing sequences; the only modiﬁcation is that one
does not assume that p1 = ∗.
This connection goes much deeper: in Section 4.3 of [Bia98] one consid-
ers pairs (J, π ) where J = {r1, . . . , r k} ⊆ {1, 2, . . . , n }is the set of indices
such that pr1 = · · · = prk = ∗ and π is a partition of the set {1, 2, . . . , n } \ J
which tells us which of the elements in the tuple (p1, . . . , p n) are equal.
One can easily see that the union {J}∪ π is a pushing partition. We leave
it as an exercise to the reader to verify that the conjugacy cl ass assigned to
a pair (J, π ) by Biane coincides with the conjugacy class which appears in
Φ P
SA ({J} ∪ π ). Methods presented in this article can be used therefore to
simplify some of the arguments in the papers [Bia98, Bia01].
6.2. Ramiﬁed coverings and pushing partitions.
6.2.1. Ramiﬁed covering and an admissible sequence. Suppose that an ad-
missible sequence a1, . . . , a n ∈ {1, 2, . . . , q }is given. Following the idea
of Okounkov [Oko00] we consider a two–dimensional sphere S2 with dis-
tinguished points 0, 1, 2, . . . , n, ∞. Figure 6.1 depicts a small region on this
sphere (unfortunately, some conventions used in the pictur es in this article
do not coincide with the ones of Okounkov).
Let S be an oriented surface. We shall consider a covering S → S2 with
simple ramiﬁcations over points 1, 2, . . . , n and an unspeciﬁed ramiﬁcation
over 0. We consider n+1 cuts from points0, 1, 2, . . . , n to ∞. We chooseS
in such a way that in the ﬁber over any point not lying on a cut there are q+1
sheets marked 1, 2, . . . , q, ∗. Sheet ∗ will be called special sheet. We also
require that the monodromy around any point k ∈ {1, . . . , n }be a transpo-
sition of the sheet ak and the sheet ∗. Since a loop around 0 is homotopic to
54 PIOTR ´SNIADY
FIGURE 6.1. Two homotopic loops on a sphere.
a loop around points 1, 2, . . . , n hence the monodromy around 0 is a prod-
uct of monodromies around 1, . . . , n and hence is equal to (a1∗) · · ·(an∗)
(cf Figure 6.1). The difference with the situation from the p aper [Oko00]
is that we do not assume that (a1∗) · · ·(an∗) = e and for this reason we
might have a non–trivial ramiﬁcation in 0 and therefore we need the extra
cut between 0 and ∞, not present in [Oko00].
6.2.2. Shape of the special sheet. Since the sequence a1, . . . , a n is admis-
sible, hence the monodromy around0 preserves the special sheet. It follows
that when we consider only cuts from points 1, 2, . . . , n to ∞ then S splits
into the special sheet and the union of non–special sheets (w hich are, pos-
sibly, glued together along the cut between 0 and ∞). Let us have a look
on the shape of the special sheet. Along the cuts from 1, 2, . . . , n to ∞ it
is glued with non–special sheets and we are not interested ho w does this
gluing look like. Much more interesting is the vertex ∞ since some points
on the boundary of the special sheet might be glued there together.
To check if two vertices: the one betweenk− 1 and k and the one between
l − 1 and l are glued together or not, we consider a loop as on Figure 6.2.
To indicate better the shape of the special sheet we inﬂated s lightly the
cuts. Our question is equivalent to the following one: is it t rue that the
monodromy along this loop preserves the special sheet. This holds if and
only if (
(ak∗)(ak+1∗) · · ·(al− 1∗)
) − 1
(∗) = ∗
which is equivalent to
pk =
(
(ak∗)(ak+1∗) · · ·(an∗)
) − 1
(∗) =
(
(al∗) · · ·(an∗)
) − 1
(∗) = pl,
where p1, . . . , p n is the corresponding pushing sequence.
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 55
FIGURE 6.2. A loop on a sphere.
FIGURE 6.3. Shape of the special sheet (the white region).
It follows that the special sheet looks as it is depicted on Fi gure 6.3,
where points p1, p 2, . . . all cover ∞ and those of them which carry the same
labels should be glued together. The pushing partition π corresponding to
the pushing sequence p1, . . . , p n can be therefore identiﬁed as a receipt for
gluing vertices p1, . . . , p n of the special sheet covering ∞. The meaning of
the additional labeling of the edges will be explained below.
56 PIOTR ´SNIADY
6.2.3. Collapsing non–special sheets. Let us inﬂate the point ∞ a lit-
tle bit (or—speaking more precisely—while performing cuts from points
1, 2, . . . , n to ∞ let us leave some neighborhood of ∞ untouched). The
special sheet becomes now an oriented surface with a boundar y which co-
incides with a construction from Section 3.1.3 where we glue d a hole in a
sphere with the ﬁrst collection of discs (see also Figure 22 in [Oko00]).
Let us collapse the union of non–special sheets (for details of this con-
struction we refer to [Oko00]). After this operation the 2n edges of the
special sheet (denoted by 1, 1 ′, 2, 2 ′, . . . , n, n ′) become glued together in
pairs. We know that the vertices p1, . . . , p n are glued together according
to the pushing partition π; this implies that the edges of the special sheet
are glued according to the pair partition π fat. This provides an alternative
description of the Okounkov’s mapping Ψ from coverings to maps on sur-
faces.
A careful reader will notice that the above statement is not c ompletely
true: the reason is that Okounkov collapses non–special she ets with two
edges in a different way than the non–special sheets with thr ee or more
edges. This means that in fact in the process of computing π fat we should
treat two–element blocks ofπ differently. We leave the details as an exercise
to the reader.
6.2.4. Many Jucys–Murphy elements. In this article we deal with only one
Jucys–Murphy element J while in the work [Oko00] one considers products
of many such elements J1, J 2, . . . and therefore a careful reader might won-
der if our methods are general enough. However, one can easil y translate
Okounkov’s statements concerning products of many Jucys–M urphy ele-
ments into our favorite language of products of moments of a single Jucys–
Murphy element which translates easily into properties of c orresponding
pushing partitions.
6.2.5. The case (a1∗) · · ·(an∗) = e. Suppose now that (a1∗) · · ·(an∗) =
e. It follows that the construction from Section 3.1.1 assigns to every cycle
bs of the permutation π fat ◦ c the number ks = 1 (otherwise (a1∗) · · ·(an∗)
would have a non–trivial cycle). Now we see from (3.2) that itis equivalent
to the statement that every cyclebs of the product π fat ◦ c makes exactly one
counterclockwise wind around the circle.
As in Section 6.2.3 let us collapse the non–special sheets; t he 2n ver-
tices of the polygon representing the special sheet fall int o two classes:
those which were covering ∞ (and which correspond to glued vertices
p1, . . . , p n) and those corresponding to the ramiﬁcation points 1, 2, . . . , n .
Suppose we are going clockwise around the boundary of the pol ygon con-
stituting the special sheet and thus we visit vertices in the order n, p n, n −
1, p n− 1, . . . , 1, p 1; let us have a look in which order we visit corners which
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 57
meet in one of the vertices of the second class. One can see tha t the edges
which meet in such a vertex correspond to one of the polygons w hich con-
stitute the boundary of the special sheet after gluing in ∞ or—in other
words—to one of the cycles of π fat ◦ c. From our previous discussion it
follows that the corners will be visited in the counterclock wise order; in
Okounkov’s notation this means that the vertex is left.
Every group of the ﬁrst class of vertices (covering ∞) which is glued
together corresponds to one of the blocks of the partition π. It follows that
they will be visited in a clockwise order; in Okounkov’s notation this means
that the vertex is right.
The above classiﬁcation of vertices into the class of left an d the class of
right ones is one of the key points of the paper [Oko00] and it is interesting
that we were able to reconstruct this result by the technique s of pushing
partitions.
