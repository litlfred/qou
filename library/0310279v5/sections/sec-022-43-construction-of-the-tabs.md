---
doc_id: 0310279v5
doc_title: "Stabilization in the braid groups I: MTWS"
section_id: sec-022-43-construction-of-the-tabs
section_title: "Construction of the tabs"
section_number: 4.3
pages: 46-49
source_pdf: 0310279v5.pdf
source_sha256: a1d472d37291a333
toc_source: outline
doc_brief: "Stabilization in the braid groups I: MTWS — 41 sections: Front matter; Introduction; The problem"
---
Construction of the tabs
In this section we modify the discs R1, . . . , Rk which we constructed in Section 2 to
special foliated discs T1
+, . . . , Tk
+ containing the clasp arcs.
We say that Ti
+ ⊂PA is a tab associated to the clasp arc γi
+ if the following hold:
•
γi
+ ⊂Ti
+.
•
∂Ti
+ = α ∪β where α ⊂X+ and β is an arc that is transverse to the foliation
of PA.
• There is a simple path l+ which is contained in a union of singular leaves in Ti
+.
The path l+ starts on X+, ends at a negative vertex, and contains all the negative
vertices in Ti
+.
• The arc γi
+ is the only clasp arc which intersects Ti
+. It is everywhere transverse
to the leaves in the foliation of PA. The arc γi
+ intersects each of the singular
leaves in the induced foliation of Ti
+ exactly once.
Lemma 4.3.1 We may assume that each Ri is a tab Ti
+.
Proof We focus on a single Ri ⊂PA, where Ri is one of the discs that we constructed
in Section 2. We construct the tab Ti
+ as a subset of the disc Ri in the basic construction.
Going back to Section 3, recall that the boundary of Ri is a union of 4 arcs:
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
459
-
-
-
-
e−
X0
γi
+
δ4
δ2
δ1
e+
Figure 33: An example of a tab
• a subarc of the modiﬁed X0,
• a subarc of X+, and
• two modiﬁed s–arcs which join them.
It contains γi
+ in its interior. Using the methods described in Section 3, we may assume
that Ri supports a braid foliation. Initially, the foliated disc Ri will not look anything
like a tab. What we wish to do is to rechoose the discs R1, . . . , Rk so that they are as
simple as possible. The new discs that we choose will be subsets of the old ones, with
possibly modiﬁed foliations. In the course of the construction we will, in effect, be
making a new choice of the separating curve X0 which divides PA into the embedded
annuli A−and A+. We note that right after the completion of this proof we will discard
X0, as we will have no further use for it.
The arc γi
+ has one of its endpoints at a point ei
+ on X+ and its other endpoint ei
−∈X−
in the interior of Ri. In between, it winds around the vertices of the foliated disc Ri,
constrained to remain transverse to the leaves of the foliation. We may assume without
loss of generality that the point ei
−where X−pierces the interior of Ri is not on a
singular leaf. Therefore ei
−belongs to a non-singular leaf of type s, a+, a−or b.
Let α ⊂Ri \ γi
+ be a simple path that starts at ei
−and ends at a point p ∈X+. Then
γi
+ ∪α ⊂Ri is a simple path that joins ei
+ to p in the interior of Ri. Without loss of
generality we may assume that this simple path is in braid position. For, if it is not,
apply Alexander’s braiding trick to wrongly oriented subarcs. This will change the
interior of Ri by an isotopy in 3–space. The changes will modify the foliation of Ri
by introducing new vertices and singularities which allow α to avoid the points of
non-transversality. After these modiﬁcations, let R′
i ⊂Ri be the foliated subdisc that
γi
+ ∪α splits off in Ri. Reapply the argument for eliminating leaves that are circles in
the foliation of R′
i, so that R′
i supports a braid foliation. Therefore we may assume that
R′
i supports a braid foliation.
Geometry & Topology 10 (2006)
460
Joan S Birman and William W Menasco
-
-
-
-
+
+
+
-

-
-
-
-
(a)
(b)
(c)
v
γi
+
e+
Figure 34: Rechoosing the disc Ri. In sketches (a) and (b) the dark area is in R′
i . The passage
from left to right shows how we modify R′
i to eliminate positive vertices.
We are now in position to re-choose γi
+, α and X0 so that every vertex in R′
i is negative.
See Figure 34. If the induced foliation of R′
i contains a positive vertex v then this
sub-foliation must also contain a singular leaf that has its endpoint on γi
+ ∪α and is
adjacent to a (possibly different) positive vertex v′. We can then push γi
+ ∪α along
the singular leaf and across v, staying transverse to the foliation, as in Figure 34(a),
moving v out of R′
i. Inducting on the number of positive vertices in the foliation of R′
i,
we have arranged that the foliation of R′
i contains only negative vertices.
Now the graph of singular leaves in R′
i is either a linear tree, or it is a tree with branches.
In the latter case, since ei
−can be adjacent to only one negative vertex, either γi
+ or α
intersects a singular leaf in the foliation of Ri twice. We can then ﬁnd a valence one
vertex, as in Figure 34(b), with either γi
+ or α in its boundary. After a ‘destabilization’
we can eliminate this negative vertex from Ri. Iterating this procedure, we alter γi
+ ∪α,
until R′
i is changed to a tab.
There is only one more problem. It may happen that near the X+ boundary of R′
i, either
γi
+ or α or both run along a band which is foliated without singularities by a and/or
s–arcs, as depicted in Figure 34(c) in the case of γi
+. If so, we simply ‘rescale’ X+, as
we did in the proof of Lemma 4.2.1 to pull the long arcs back into the single a−s–tile
which forms the base of the tab.
Remark 4.3.1 We make an important remark about simpliﬁed notation and simpliﬁed
tile types. Having standardized the tabs, we will not have further use for X0. This
eliminates the dual meanings of the boundary arcs in Figure 31 and allows the following
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
461
simpliﬁcation. If ϵ = ±, an aϵ–arc has its interior endpoint on a vertex of sign ϵ and
has its boundary endpoint on Xϵ. At the same time, we will no longer need to depict X0
in our ﬁgures, and will be free to use dotted arcs in other settings as we proceed through
the proof of the MTWS.
♦
Remark 4.3.2 Notice that the work in this section uses the braid foliation of Ri. If
we had braid foliations on hand as a tool, during the basic construction, we could have
arranged at that time for each Ri to be a tab.
♦
Remark 4.3.3 In Figure 14 we gave an example of a tab with the clasp arc on one
side of the singular leaves. Soon we will develop the ability to move it so that it is
transverse to the foliation and to one side or the other of a sequence of singular leaves,
or alternatively to position it in a union of leaves (singular and/or non-singular), at the
expense of introducing many new b–arcs into the foliation. See Section 4.5 below. ♦
