---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-029-9-general-spectral-networks-and-path-lifting
section_title: "General spectral networks and path lifting"
section_number: 9
pages: 54-56
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
As we have remarked in §5.7, in the theories S[A1,C,D ], each spectral network Wϑ cor-
responds naturally to an ideal triangulation of C. Ideal triangulations are rather ﬂexible
objects and one might study them without regard for whether they arise from any Wϑ. In
an analogous way, we now generalize theWϑ we have worked with thus far to some purely
topological objectsW, which we will refer to as spectral networks.
A spectral network W is associated to a branched cover Σ → C. In contrast to the
case ofW =Wϑ constructed in§5, now we do not require that Σ ⊂ T∗C. In particular,
we do not have the canonical 1-form λ on Σ anymore. In consequence the S-walls making
up a spectral network are not solutions to any diﬀerential equation; rather, locally they
are arbitrary paths. We thus gain some ﬂexibility in the S-walls, but at the same time
we lose some topological data which were previously induced by the 1-form λ (Seiberg-
Witten diﬀerential). We will build substitutes for those data explicitly into our deﬁnition
of “spectral network.”
– 52 –
9.1 General spectral networks
Let C be an oriented real surface with a (perhaps empty) boundary. Each connected
component of the boundary is a copy of S1; on each such component ﬁx a (nonempty) set
of marked points. Also ﬁx a (perhaps empty) set of marked points in the interior of C.
We refer to the interior marked points as punctures and we refer to all the marked points
as singular points (although they are not singularities of C) and denote them as sn. We
require that there is at least one singular point.
Let Σ→C be aK-fold branched covering which is unramiﬁed over the boundaries and
the singular points. Let C′ be C minus the branch points. For simplicity we assume the
branch points are all simple, so the monodromy around each branch point just exchanges
two sheets of Σ. (This condition can likely be relaxed at the price of a more cumbersome
deﬁnition.)
A spectral network subordinate to the covering Σ is a collection
W = (o(sn),{zµ},{pc}) (9.1)
where the symbols refer to the following data:
D1. For each singular point sn,o(sn) is a partially ordered subset of the set of sheets of Σ
over a neighborhood of sn. o(sn) must contain at least two elements, and if sn is a
puncture, o(sn) must contain all of the sheets over a neighborhood of sn.
D2. {zµ} is a locally ﬁnite collection of points on C′, called joints.
D3. {pc} is a ﬁnite or countable collection of closed segments (i.e. images of embeddings
of [0, 1] into C), called walls or streets (depending which metaphor is more useful in
a given context, cf. footnote 21). For each orientation o of the street pc,pc is labeled
with an ordered pair of distinct sheets of the covering Σ →C overpc. Reversing the
orientation reverses this ordered pair of sheets. So pc comes with two labels which
we could write as (o,ij ) and (−o,ji ).
The data must satisfy the following conditions:
C1. The segments pc cannot cross one another (but they are allowed to have common
tangents). Each pc must begin on a branch point or a joint, and must end on a joint
or a singular point. Any compact subset of C′ intersects only ﬁnitely many segments.
C2. Around each branch point b there is a neighborhood where W looks like Figure 13.
That is, each branch point of type ( ij) is an endpoint of three streets which carry
labels (o,ij ) or (o,ji ), and the streets encountered consecutively traveling around a
loop around b have oppositely ordered sheets.
C3. Around each jointzµ there is a neighborhood whereW looks like Figure 9, Figure 10,
or Figure 11.
C4. If a segment with label ij ends at a singular point sn, then i and j lie in the ordered
subset o(sn), and with respect to the ordering of o(sn) we have i<j .
– 53 –
Our deﬁnition of “spectral network” is somewhat provisional. With an eye toward the
future let us mention one natural generalization: we could have relaxed the requirement
that there is at least one singular point sn, and allowed the segments to be inﬁnite in one
direction. This generalization would be needed if we want our deﬁnition to encompass the
networksWϑ in theories S[g,C ] where the set of defects is actually empty. The resulting
spectral networks would be expected to look much more complicated — e.g. the streets
may well be dense on C. Nevertheless, as we described in the introduction, we think that
it should be possible to extend everything described in this paper to this case.
