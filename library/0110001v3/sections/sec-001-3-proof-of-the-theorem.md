---
doc_id: 0110001v3
doc_title: "A geometric interpretation of Milnor's triple linking numbers"
section_id: sec-001-3-proof-of-the-theorem
section_title: "Proof of the theorem"
section_number: 3
pages: 6-12
source_pdf: 0110001v3.pdf
source_sha256: f30f603ac1c555e0
toc_source: inferred
doc_brief: "A geometric interpretation of Milnor's triple linking numbers — Milnor’s triple linking numbers of a link in the 3-sphere are interpreted geometrically in terms of the pattern of intersections of the"
---
Proof of the theorem
A generic family F = Fi ∪Fj ∪Fk of Seifert surfaces for the link Li ∪Lj ∪Lk
will be called reduced if it is of one of the following types:
Type 1 : (disjoint clasps) The only double curves are disjoint clasps.
Type 2 : (boundary ordered) Around the boundary of any one of the
three surfaces, all intersections with either of the other two are adjacent,
except possibly for cancelling pairs (i.e. adjacent intersections of opposite
sign with the second surface that may occur between intersections with
the third).
If F is a family of type 1, then tijk(F) = 0 (since there are no triple points at
all) and mijk(F) is just the ¯µ-invariant (as is shown in the lemma below). If
F is of type 2, then by deﬁnition the word wk (see §2) is of the form mp
i mq
j
for an appropriate choice of basepoint on Lk, where p = µik and q = µjk (the
linking numbers of Li and Lj with Lk) and similarly for wi and wj . Thus
eijk(F) = εij(wk) = pq ≡0 (mod δ), and so mijk(F) ≡0. It will follow from
the theorem that in this case tijk(F) reduces (mod δ) to the negative of the
¯µ-invariant.
Lemma 1 If F is of type 1, then mijk(F) ≡¯µijk.
Proof By the classiﬁcation of surfaces, each component of F can be viewed
as a 2-dimensional handlebody, i.e. a disk (0-handle) with bands (1-handles)
attached, while the clasps between any two components can be viewed as pairs
of feelers, i.e. bands attached at one end to their respective disks and clasped
with each other at the other end.
Algebraic & Geometric Topology, Volume 3 (2003)
A geometric interpretation of Milnor’s triple linking numbers
563
Of course the bands and feelers may be highly linked and twisted, so consider
the eﬀect of a band pass (moving one such through another or through itself).
Clearly mijk(F) is unchanged, since the pattern of double curves is unaltered,
and ¯µijk is certainly unchanged under self-passes and passes between bands
from the same surface component, since it is a link homotopy invariant. In fact
¯µijk is also invariant under passes between bands from distinct components. To
see this, it suﬃces (using the antisymmetry of ¯µ) to consider a pass between
bands on Fj and Fk as shown below.
j
k
j
k
j1
j2
If the longitude of Lk on the left is the word u v (where u starts at the lower
left point) then on the right it is (j−1
1
j2)u v (where ab denotes the conjugate
aba−1) for suitable conjugates j1, j2 of the meridian j of Lj . But
εij((j−1
1
j2)uv) = εij((j−1j)uv) = εij(uv),
since in general εij(· · · (ab)c · · · ) = εij(· · · bc · · · ), and so ¯µijk remains unchanged.
Using band passes, the three surfaces can be “disentangled”, except for the
clasps. In particular, they can be placed so that their disks and bands lie near
the vertices of a triangle whose edges are formed by the feelers reaching out to
clasp each other (see Figure 3 for an example). Furthermore, it can be arranged
that the only link crossings aside from the clasps (under the projection to the
plane of the triangle) are between feelers from the same surface component, or
between bands from the same component. In fact the latter can be changed
at will, since self-crossings of a component do not contribute to mijk or ¯µijk.
Thus we may assume that each Seifert surface consists only of a disk with some
feelers, as shown in the ﬁgure.
Now ¯µijk = εij(uk), where uk is the word deﬁned in §1 which represents the
longitude lk. For the case at hand, uk is clearly a product of conjugates of
i and j and their inverses. In particular, each positive clasp of Fi with Fk
contributes a conjugate j−pijp, where p is the number of clasps of Fi with
Fj (counted with sign) which precede the given clasp along Li. (Actually the
conjugating element is a word in i and j with total exponent p in j, but
the i’s can be ignored when computing εij .)
Likewise each negative clasp
contributes j−pi−1jp, and so the total contribution from the clasps between Fi
and Fk is ejki (since εij(j−pi±1jp) = ±p). A similar argument shows that the
Algebraic & Geometric Topology, Volume 3 (2003)
564
Blake Mellor and Paul Melvin
contribution from the clasps between Fj and Fk is −eikj (the minus sign arising
since εij(i−pj±1ip) = ∓p). So the total internal contributions from these factors
is ejki −eikj = ejki +ekij (by Remark 2 in §2). The contribution from the order
of the factors is eijk, so we conclude that ¯µijk = eijk + ejki + ekij ≡mijk as
desired.
Fi
Fj
Fk
Figure 3: Disentangled surfaces
Remark There is a nice alternative proof that ¯µijk ≡mijk(F) for disentangled
surfaces: One observes that the braiding of the feelers can be accomplished
by “Borromean tangle” replacements – familiar from the theory of ﬁnite type
invariants of 3-manifolds – one for each braid generator. One then shows that
the invariants ¯µijk and mijk change by an equal amount (±1) under such a
tangle replacement, and it is easy to check that they agree if there is no braiding.
We now deﬁne three “ﬁnger moves” on a generic family F of Seifert surfaces.
Each move involves pushing the interior of a small disk on one of the surfaces
along a path in one of the other surfaces. It is understood that the path begins
at the center of the disk, and that the center should be pushed slightly beyond
the endpoint of the path.
First finger move : Push from a double point along a path to the
boundary which contains no other double points.
Second finger move : Push from a triple point along a path to the
boundary which lies in a double curve and contains no other triple points.
Algebraic & Geometric Topology, Volume 3 (2003)
A geometric interpretation of Milnor’s triple linking numbers
565
Third finger move : Push from a double point in the boundary to an
adjacent double point along a path in the boundary.
These moves are illustrated in Figures 4, 5 and 6.
Li
Fi
Fj
Li
Fi
Fj
Figure 4: First ﬁnger move
Li
Fi
Fj
Fk
Li
Fi
Fj
Fk
Figure 5: Second ﬁnger move
Lk
Fk
Fi
Fj
Lk
Fk
Fi
Fj
Figure 6: Third ﬁnger move
Algebraic & Geometric Topology, Volume 3 (2003)
566
Blake Mellor and Paul Melvin
Lemma 2 The diﬀerence mijk −tijk is invariant under all three ﬁnger moves.
Proof Each move is, to be exact, six possible moves, since the roles of the
three surfaces can be permuted. We will consider only one of the six cases, the
ones depicted in the ﬁgures, since the others can be proved similarly.
The ﬁrst ﬁnger move (Figure 4) clearly does not change the number of triple
points, so tijk remains the same. Also, since the words wj and wk (around the
boundaries of Fj and Fk) are unchanged, so are eijk and ekij . The word wi is
only changed by adding a cancelling pair, so ejki is unchanged. Therefore mijk
is ﬁxed as well, and so is the diﬀerence mijk −tijk.
The second ﬁnger move changes the number of triple points by 1. In the case
shown in Figure 5, a positive triple point is removed, so tijk decreases by 1 (the
boundaries of the surfaces are oriented counterclockwise). The words wj and
wk are unchanged; the word wi is modiﬁed by replacing one appearance of the
letter k by its conjugate j−1kj. So eijk and ekij are unchanged, while ejki
decreases by 1. The result is to decrease mijk by 1. Therefore the diﬀerence
mijk −tijk is unchanged.
The third ﬁnger move, as shown in Figure 6, decreases tijk by 1 by adding a
negative triple point. The words wi and wj are unchanged, but wk is modiﬁed
by replacing an adjacent pair of letters ij by ji. So ejki and ekij remain ﬁxed,
while eijk decreases by 1. This means mijk is reduced by 1, and once again the
diﬀerence mijk −tijk is preserved.
The ﬁnal step in the proof of the theorem is to show how to use ﬁnger moves
to transform a generic family of Seifert surfaces into either one of the two
reduced types. To achieve the ﬁrst type, in which the intersections between the
components are disjoint clasps, it is necessary to eliminate all circles, ribbons
and triple points. We describe a procedure to accomplish this.
First, remove circles by ﬁnger moves of type 1. Do this by following any path
from the circle to the boundary of one of the surfaces in which it lies, breaking
each double arc crossed by this path by a type 1 ﬁnger move. Note that this
move never creates circles, so its repeated application eventually eliminates all
the circles.
So now all triple points involve clasps and/or ribbons.
We can inductively
remove the triple points along each clasp or “long” ribbon (i.e. a double arc
with both endpoints on the boundary of one surface) by using ﬁnger moves of
type 2. Again, this move never creates circles, so we are left with a disjoint
collection of clasps and ribbons.
Algebraic & Geometric Topology, Volume 3 (2003)
A geometric interpretation of Milnor’s triple linking numbers
567
Finally, remove the ribbons by ﬁnger moves of type 1 on “short” ribbons (double
arcs with both endpoints in the interior of the surface) along any path from the
ribbon to the boundary which avoids other ribbons and clasps. Such a path
will exist because there are no triple points or circles, so no short ribbon can
be separated from the boundary. This leaves a collection of disjoint clasps, i.e.
a reduced family of type 1.
To obtain a reduced family of surfaces of the second type, begin with one of the
ﬁrst type, and then simply reorder the clasps as necessary via transpositions,
using the third ﬁnger move. This completes the proof of the theorem.
Final Remarks (1) The theorem suggests a natural construction of a three
component link with any prescribed pairwise linking numbers p, q, r and any
given triple linking number m: Start with the unlink, bounding disjoint disks.
Next add p feelers between one pair of disks (as in Lemma 1), and similarly for
q and r with the other pairs. Finally add m Borromean tangles (band sums
with the three components of the Borromean rings). Now apply the theorem,
using the calculation in the Example in §2.
(2) If one allows nonorientable Seifert surfaces, then the geometric invariants
tijk and mijk are still deﬁned modulo 2. (Note that the mod 2 reduction of
εij(w) depends only on the parity of the exponents of i and j in w.) Fur-
thermore, the proof of the theorem carries over, without change, to show that
¯µijk ≡mijk −tijk (mod 2). Of course this is a vacuous statement unless the
pairwise linking numbers are even.
(3) A geometric interpretation for the higher order Milnor invariants remains
open. A formula for the ﬁrst non-vanishing invariant is given by Cochran [1],
using surfaces associated to certain derived links. It is natural to ask whether
the ideas of this paper can be extended to the general case; the diﬃculty seems
to lie in ﬁnding the right ”higher-order surfaces.”
Algebraic & Geometric Topology, Volume 3 (2003)
568
Blake Mellor and Paul Melvin
