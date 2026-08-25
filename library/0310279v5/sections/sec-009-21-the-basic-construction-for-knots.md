---
doc_id: 0310279v5
doc_title: "Stabilization in the braid groups I: MTWS"
section_id: sec-009-21-the-basic-construction-for-knots
section_title: "The basic construction for knots"
section_number: 2.1
pages: 19-23
source_pdf: 0310279v5.pdf
source_sha256: a1d472d37291a333
doc_brief: "Stabilization in the braid groups I: MTWS — 30 sections: Introduction; The problem; Block-strand diagrams and template"
---
Lemma 2.1.1 Let X+, X− be arbitrary disjoint closed braid representatives of the
same knot typeX . Then there is an intermediate representative X0 ofX such that the
following hold:
(1) X0 is the braid connected sum of X+ and k closed braid representatives of the
unknot, for some k≥ 0. These k representatives of the unknot bound pairwise
disjoint discs.
(2) X0− X− (resp. X+− X0) is the boundary of an embedded annulusA− (resp.
A+). It will be seen from the construction that X0 is the boundary of a Seifert
surface F0, andA− is a collar neighborhood of X0 on F0.
(3) The intersectionsA+∩A− are precisely k clasp arcs. See Figure 11.
positive clasp negative clasp
clasp
intersection
Figure 11: Clasp intersections
Remark 2.1.1 A word is in order on the basic construction. There are very simple
constructions which yield everything in Lemma 2.1.1 except the fact thatA−⊂ F0.
Astute readers will notice that F0 plays an almost invisible role in the pages that lie
ahead, and ask why we needed it? Our reasoning was that in our earlier papers we had
developed extensive machinery regarding braid foliations of Seifert surfaces for knots
and links, including the case of discs bounded by unknots. In this paper we need related
braid foliations of the immersed annulus of Lemma 2.1.1. The easiest way to develop
the tools that we need seemed to be to make one of our annuli (ie A−) a subset of a
Geometry &Topology 10 (2006)
432 Joan S Birman and William W Menasco
Seifert surface, and arrange that the other (ieA+) is a ﬁnite family of foliated discs
banded together with narrow strips to form a second annulus that intersects the ﬁrst in a
controlled fashion. That will allow us to make full use of the existing braid foliation
machinery for Seifert surfaces and discs, rather than to develop everything anew. This
issue will become clear in Section 3 and Section 4 below. ♦
Proof Without loss of generality we may assume that X+⊂ R3
+ and X−⊂ R3
−, with
X+ far above R2 = R3
−∩ R3
+, and X− a little bit below R2. We may further assume
that X+, X− are closed braids with respect to the same braid structure ( A, H). Our
ﬁrst task is to construct a series of knots X′
−, X′′
−, X0, all representing X , with X0
the braid-connected sum of X+ and k pairwise disjoint and pairwise unlinked copies
U1,..., Uk of the unknot.
Choose a Seifert surface F− for X−. Let X′
−⊂ F− be a preferred longitude for X−,
chosen close enough to X−, so that the annulus that they cobound in F− does not
intersect A, and so that X′
− is also a closed braid. The knots X− and X′
− will have
algebraic linking number 0, but X−∪ X′
− will not be a split link unlessX is the unknot.
Therefore, if we try to push X′
− out of R3
− and into R3
+ it will get stuck, ie there will
be a ﬁnite number of ‘undercrossing hooks’ whereX′
− is forced to dip back into R3
− to
pass under X−, as in Figure 12(a).
Our ﬁrst change is to modify X′
− (holding X− ﬁxed) to a new closed braid X′′
− which
has the same knot type as X′
− and is entirely in R3
+. This can be accomplished by
pushing X′
− across pairwise disjoint discs D1∪···∪ Dk , as in Figure 12(b) to X′′
−. By
placing X− very close to R2 and choosing the discs to be very ‘thin’ we may assume
that each subarcβi is in braid position and in R3
+. By construction X′′
− is a closed braid
(because X′
− is a closed braid and the isotopy X′
−→ X′′
− is arbitrarily small), also it
representsX , and it is entirely in R3
+.
We are now ready to bring X+ into the picture. The fact that X′′
− and X+ both represent
X and are both in the interior of R3
+ shows that we may ﬁnd a homeomorphism
g : R3
+→ R3
+ which is the identity on R2 with g(X′′
−) = X+. Extend g by the identity
on R3
− to a homeomorphism G : R3→ R3. Let Ri = G(Di,+∪Di,−) = g(Di,+)∪Di,−.
The facts that (i) G is a homeomorphism which is the identity in R3
− and (ii) if i⁄= j
then Di∩ Dj =∅ tell us that the R′
is are pairwise disjoint embedded discs, and also that
X− pierces each Ri exactly once. The fact that X+ was well above R2 shows that we
may assume that each Ri intersects X+ in a single arcβ′
i = g(βi).
Let X′
0 be the knot which is obtained from X+ by replacing each β′
i⊂ X+ by ∂Ri\β′
i .
Then X′
0 is the connected sum of X+ and k copies of the unknot, the ith copy being
∂Ri. By construction the k discs R1,..., Rk are pairwise disjoint, so that our k unknots
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 433
(a) (b) (c)
(d) (e) (f)
R2
R2
R2
R2
Ri
X′
−
X−
αi
βi
Di,+
Di,−
X′′
−
βi
Di,+
Di,−
β′
i X+
g(Di,+
)
β′
i X+
Di,−
X+
X0
X−
X0
X−
Figure 12: Constructing X0
represent the k–component unlink. It may happen that X′
0 is not a closed braid. The
only subarcs which might not be in braid position are the 2 k ‘vertical’ arcs in each
∂g(Di,+). To overcome this problem, recall that J W Alexander [1] introduced a very
simple way to change an arc δ which is not in braid position to one that is. See
Figure 13(a). Alexander showed that whenever a knot X is not transverse to the ﬁbers
of H it can be divided into small segments which can then be pushed across the braid
axis, one at a time, avoiding unwanted intersections with the rest of X, to change X to a
closed braid. Using this construction, we change all the wrongly oriented subarcs of
the 2k vertical arcs in the boundaries of the ‘ribbons’R1∪···∪ Rk to subarcs that are
everywhere transverse to the ﬁbers of H. We have proved (1).
There is an important aspect of our construction, which will give us the part of (2) that
relates toA−:
• X−∪ X0 has the same link type as X−∪ X′
−. For, by construction, the home-
omorphism G−1 : R3 → R3, being the identity on R3
−, sends X−∪ X0 to
X−∪ X′
−.
This simple fact gives us the annulusA−, in the following way: Since X′
− is a preferred
longitude for X−, and since X−∪ X0 has the same link type as X−∪ X′
−, it follows that
X0 is also a preferred longitude for X−. From this it follows that X− is also a preferred
longitude for X0. Choose a Seifert surface F0 for X0. Holding X0 and X− ﬁxed,
isotope the interior of F0 until X− lies on F0 as a preferred longitude. LetA−⊂ F0
Geometry &Topology 10 (2006)
434 Joan S Birman and William W Menasco
δ δ′
X0
(a)
clasps
X0
X−
X+
(b)
A
Figure 13: (a) Alexander’s trick (b) A fragment of the preimage PA ofA+∪A−
be the annulus in F0 which X0 and X− bound. This annulus is embedded because F0
is embedded. Thus we have proved the part of (2) that relates toA−.
In fact, a small modiﬁcation in X0 also gives usA+. The discs R1∪···∪ Rk have a
natural order which is determined by the order of the subarcs β′
1∪···∪ β′
k along X+.
Using this order, and the framing provided by F0, join the discs R1∪···∪ Rk by k
very narrow bands in F0, each having one edge on X+. Modify X0 by pushing it a
little bit into F0 along the bands and along the Ri’s. (By an abuse of notation, we use
the same names for the modiﬁed R′
i s and the modiﬁed X0). The union of the new R′
i s
and the bands is our annulusA+. The annulusA+ is embedded because the R′
i s are
disjoint and embedded, and the bands are too. We have proved (2). Since X−⊂∂A−
and since X− pierces each Ri⊂A + once, it follows thatA−∩A + always contains k
clasp arc intersections. Thus we have also proved (3), and the proof of Lemma 2.1.1 is
complete.
We establish conventions that will be used throughout this paper. The symbol CA
denotes the immersed annulusA+∪A−. We shall refer to it as a clasp annulus. We
will also be interested in its preimage PA under the immersion. Figure 13(b) is a
schematic that illustrates our basic construction, as described in Lemma 2.1.1. The
knot X0 will only be needed in the beginning of our argument, therefore we show it as a
dotted curve. The closed braid X+ will be the primary focus of our attention, and so we
show it as a thick black line. We will eventually modify it to X−, which we illustrate as
a thick grey line (to suggest that it is a distant goal). To avoid clutter in our ﬁgures we
will, whenever the meaning is unambiguous, suppress the labels X+ and X−. Most of
the time the black-grey convention will enable us to recognize them without labels.
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 435
Remark 2.1.2 The reader may wonder why the isotopy which we constructed fromX+
to X− in Lemma 2.1.1 required us to increase the braid index ofX+ by connect-summing
it with some number of closed braid representatives of the unknot, because one expects
these to have braid index greater than 1. This does indeed sound wrong, in view of the
fact that our goal is to have the braid index go down and not up, but in fact it is to be
expected because we are attempting to prove the MTWS, and for that we ﬁrst need
to have in hand a proof of the MT. Indeed, in [12] we showed that a variation on the
construction given here in Lemma 2.1.1 and Proposition 2.2.1 (but without taking any
note of the clasp arcs) can be used to give a new proof of Markov’s classical result.
When we began the work in this paper we started with that new proof of the Markov
theorem and proceeded to modify the Markov tower that it gave to us. Later, we realized
that it was not necessary to literally prove the Markov theorem, all we needed was the
isotopy encoded byCA . We hope that explains the logic. ♦
