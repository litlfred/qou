---
doc_id: 0310279v5
doc_title: "Stabilization in the braid groups I: MTWS Introduction"
section_id: sec-033-57-pushing-across-a-standard-annulus
section_title: "Pushing across a standard annulus"
section_number: 5.7
pages: 100-102
source_pdf: 0310279v5.pdf
source_sha256: a1d472d37291a333
toc_source: outline
doc_brief: "Stabilization in the braid groups I: MTWS Introduction — 40 sections: Front matter; Introduction; The problem"
---
♦
A region R has a tree foliation if, after a sequence of bb–exchanges the foliation is
reduced to a root foliation.
The next proposition shows how a tree foliation imposes a block decomposition on our
two braids:
Proposition 5.6.2 Let R ⊂PA \ S be a component whose image is embedded.
Assume that S̸ = ∅. Assume that all b–arcs are essential, and that R has a tree foliation.
Then the isotopy which corresponds to pushing Y+ across R is a sequence of exchange
moves over a block-strand tree.
Proof The isotopy of the braid through the sequence of bb–exchanges corresponds to
collapsing a tree to its root. The collapsing is realized by bb–exchange moves followed
by braid isotopy to remove inessential b–arcs. After that, an isotopy of Y+ across the
new R corresponds to a sequence of aa and ab–exchange moves over this root.
Remark 5.6.3 Two remarks are in order. They relate to Propositions 5.6.1 and 5.6.2.
(1) In both propositions the basic assumption is that the region R is embedded. Of
course this will be the case if no clasp arcs intersect R. But it will also be the
case if (a) clasp arcs intersect R but no clasp arc pair intersects R, or (b) there
are no long clasp arcs which intersect R.
(2) After a G–exchange move across R, valence 1 vertices may be revealed. See
Figure 22. Later, when we get to the ﬁnal steps in the proof, we will remove
them by destabilization.
♦
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
513
We are ﬁnally ready to introduce clasp arcs into the picture. In the most general case
there will be several related regions R1, . . . , Rk which are intersected by paired clasp
arcs. Thus the exchange moves across one Ri will have to be interrupted midway to
do part of an exchange move along an associated Rj. Let {R1, . . . , Rk} ⊂PA be a
collections of regions such that each int(Ri), 1 ≤i ≤k, is embedded in S3 \ (X+ ∪X−)
and each Ri has a tree foliation. Assume each Ri has at least one clasp arc with an
endpoint on X+ and at least one clasp arc with an endpoint on X−, and with the puncture
endpoints on b–arcs in Ri, so that in particular no clasp arc is long. Moreover, assume
that the image of {R1, . . . , Rk} in CA is connected. Then the collection of regions is
said to have a G–exchange foliation. The motion across a region with a G–exchange
foliation is a G–exchange move. As we have shown, in the absence of clasp arcs it
would be a sequence of exchange moves which carries a subarc of X+ over a rooted
block and strand tree.
Proposition 5.6.3 Let {R1, . . . , Rk} ⊂PA be a collection of regions which, taken
together, have a G–exchange foliation. Then an isotopy of X+ to X−across the regions
{R1, . . . , Rk} is realized by a G–exchange move.
Proof Since each region Ri is embedded, the isotopy of any one arc Ri ∩X+ across
Ri to Ri ∩X−corresponds to a G–exchange move. Moreover, since each region
contains clasp arcs having endpoints on both X+ and X−and since their image in CA
is connected, we have an interdependence of the isotopies across all the regions. Thus,
an isotopy across the collection {R1, . . . , Rk} is a G–exchange move.
5.7
Pushing across a standard annulus
In constructing the thin annuli, we omitted the case of a standard annulus (with or
without clasp arcs). Motions across a standard annulus will in general occur at the very
end of the isotopy from X+ →X−, after all singularities that are on clasp arcs have
been eliminated, and all short clasp arcs have been removed. To give an example of
such a motion, let us suppose that X is a link of µ ≥2 components and that the ﬁrst
component, X1
+ cobounds with X1
−a standard annulus with 2k vertices, with or without
clasp arcs. Figure 61 shows an example without clasp arcs, when k = 4.
Figure 61 shows that a stabilization along one of the singular leaves in G−,ϵ, followed
by a sequence of k −1 exchange moves, followed by a destabilization, sufﬁces to move
X1
+ to X1
−. The total change in braid index is zero. We have a Markov tower similar to
the one in Figure 5. If there are clasp arcs, we may assume that they have been pushed
into singular leaves. Keeping in mind the stabilization move in Figure 61, where X+ is
Geometry & Topology 10 (2006)
514
Joan S Birman and William W Menasco
pushed across a singular leaf, we note that when there is a pair of clasp arcs a microﬂype
pushes both the black boundary arc and the dotted grey boundary arc, simultaneously,
across a pair of singular leaves. After all of the clasp arc pairs have been removed
with the help of microﬂypes, the rest of the standard annulus can be crossed with the
help of complexity-reducing destabilizations and exchange moves. In Section 1 of this
-
-
-
-
+
+
+
+
-
-
-
+
+
+
+
+
stabilize
3 exchange
moves
destabilize
δ
−δ
−δ
δ
δ
−δ
−δ
δ
δ
−δ
−δ
δ
δ
−δ
−δ
−δ
Figure 61: Pushing across a standard annulus
paper, in Figure 8, we constructed the Markov tower and the associated template for
the crossing of a standard annulus without clasp arcs. If there are clasp arcs, then as
was just shown the annulus can be crossed using microﬂypes, exchange moves and
destabilizations, and no other template is needed. The blocks shown in Figure 8 allow
for the possibility that other components of X braid with X1. If there were no other
components, then the entire move in Figure 8 can be realized by braid isotopy. If there
are other components, or if k > 4, this may not be the case. The cyclic move exists for
every k. The associated templates are the cyclic templates of the MTWS.
