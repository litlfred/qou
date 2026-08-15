---
doc_id: 0310279v5
doc_title: "Stabilization in the braid groups I: MTWS JOAN S BIRMAN WILLIAM W MENASCO"
section_id: sec-019-43-construction-of-the-tabs
section_title: "Construction of the tabs"
section_number: 4.3
pages: 46-52
source_pdf: 0310279v5.pdf
source_sha256: a1d472d37291a333
doc_brief: "Stabilization in the braid groups I: MTWS JOAN S BIRMAN WILLIAM W MENASCO — 30 sections: Introduction; The problem; Block-strand diagrams and template"
---
In this section we modify the discs R1,..., Rk which we constructed in Section 2 to
special foliated discs T1
+,..., Tk
+ containing the clasp arcs.
We say that Ti
+⊂PA is a tab associated to the clasp arcγi
+ if the following hold:
• γi
+⊂ Ti
+.
• ∂Ti
+ =α∪β whereα⊂ X+ andβ is an arc that is transverse to the foliation
ofPA .
• There is a simple path l+ which is contained in a union of singular leaves in Ti
+.
The path l+ starts on X+, ends at a negative vertex, and contains all the negative
vertices in Ti
+.
• The arcγi
+ is the only clasp arc which intersects Ti
+. It is everywhere transverse
to the leaves in the foliation ofPA . The arc γi
+ intersects each of the singular
leaves in the induced foliation of Ti
+ exactly once.
Lemma 4.3.1 We may assume that each Ri is a tab Ti
+.
Proof We focus on a singleRi⊂PA , where Ri is one of the discs that we constructed
in Section 2. We construct the tab Ti
+ as a subset of the disc Ri in the basic construction.
Going back to Section 3, recall that the boundary of Ri is a union of 4 arcs:
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 459
----
e− X0
γi
+
δ4 δ2 δ1
e+
Figure 33: An example of a tab
• a subarc of the modiﬁed X0,
• a subarc of X+, and
• two modiﬁed s–arcs which join them.
It containsγi
+ in its interior. Using the methods described in Section 3, we may assume
that Ri supports a braid foliation. Initially, the foliated disc Ri will not look anything
like a tab. What we wish to do is to rechoose the discs R1,..., Rk so that they are as
simple as possible. The new discs that we choose will be subsets of the old ones, with
possibly modiﬁed foliations. In the course of the construction we will, in effect, be
making a new choice of the separating curve X0 which dividesPA into the embedded
annuliA− andA+. We note that right after the completion of this proof we will discard
X0, as we will have no further use for it.
The arcγi
+ has one of its endpoints at a pointei
+ on X+ and its other endpoint ei
−∈ X−
in the interior of Ri. In between, it winds around the vertices of the foliated disc Ri,
constrained to remain transverse to the leaves of the foliation. We may assume without
loss of generality that the point ei
− where X− pierces the interior of Ri is not on a
singular leaf. Therefore ei
− belongs to a non-singular leaf of type s, a+, a− or b.
Letα⊂ Ri\γi
+ be a simple path that starts at ei
− and ends at a point p∈ X+. Then
γi
+∪α⊂ Ri is a simple path that joins ei
+ to p in the interior of Ri. Without loss of
generality we may assume that this simple path is in braid position. For, if it is not,
apply Alexander’s braiding trick to wrongly oriented subarcs. This will change the
interior of Ri by an isotopy in 3–space. The changes will modify the foliation of Ri
by introducing new vertices and singularities which allow α to avoid the points of
non-transversality. After these modiﬁcations, let R′
i⊂ Ri be the foliated subdisc that
γi
+∪α splits off in Ri. Reapply the argument for eliminating leaves that are circles in
the foliation of R′
i , so that R′
i supports a braid foliation. Therefore we may assume that
R′
i supports a braid foliation.
Geometry &Topology 10 (2006)
460 Joan S Birman and William W Menasco
- - - -
+
+
+
-

-
--
-
(a)
(b) (c)
v
γi
+
e+
Figure 34: Rechoosing the disc Ri . In sketches (a) and (b) the dark area is in R′
i . The passage
from left to right shows how we modify R′
i to eliminate positive vertices.
We are now in position to re-chooseγi
+,α and X0 so that every vertex in R′
i is negative.
See Figure 34. If the induced foliation of R′
i contains a positive vertex v then this
sub-foliation must also contain a singular leaf that has its endpoint onγi
+∪α and is
adjacent to a (possibly different) positive vertex v′. We can then push γi
+∪α along
the singular leaf and across v, staying transverse to the foliation, as in Figure 34(a),
moving v out of R′
i . Inducting on the number of positive vertices in the foliation of R′
i ,
we have arranged that the foliation of R′
i contains only negative vertices.
Now the graph of singular leaves in R′
i is either a linear tree, or it is a tree with branches.
In the latter case, since ei
− can be adjacent to only one negative vertex, eitherγi
+ or α
intersects a singular leaf in the foliation of Ri twice. We can then ﬁnd a valence one
vertex, as in Figure 34(b), with either γi
+ or α in its boundary. After a ‘destabilization’
we can eliminate this negative vertex fromRi. Iterating this procedure, we alter γi
+∪α,
until R′
i is changed to a tab.
There is only one more problem. It may happen that near the X+ boundary of R′
i , either
γi
+ orα or both run along a band which is foliated without singularities by a and/or
s–arcs, as depicted in Figure 34(c) in the case of γi
+. If so, we simply ‘rescale’ X+, as
we did in the proof of Lemma 4.2.1 to pull the long arcs back into the single a−s–tile
which forms the base of the tab.
Remark 4.3.1 We make an important remark about simpliﬁed notation and simpliﬁed
tile types. Having standardized the tabs, we will not have further use for X0. This
eliminates the dual meanings of the boundary arcs in Figure 31 and allows the following
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 461
simpliﬁcation. If ϵ =±, an aϵ–arc has its interior endpoint on a vertex of signϵ and
has its boundary endpoint on Xϵ. At the same time, we will no longer need to depict X0
in our ﬁgures, and will be free to use dotted arcs in other settings as we proceed through
the proof of the MTWS. ♦
Remark 4.3.2 Notice that the work in this section uses the braid foliation of Ri. If
we had braid foliations on hand as a tool, during the basic construction, we could have
arranged at that time for each Ri to be a tab. ♦
Remark 4.3.3 In Figure 14 we gave an example of a tab with the clasp arc on one
side of the singular leaves. Soon we will develop the ability to move it so that it is
transverse to the foliation and to one side or the other of a sequence of singular leaves,
or alternatively to position it in a union of leaves (singular and/or non-singular), at the
expense of introducing many new b–arcs into the foliation. See Section 4.5 below. ♦
4.4 The two ﬁnger moves
We need tools that will allow us to modify neighborhoods of the clasp arcs inCA in a
controlled manner, keeping track of the foliation on the two branches and making sure
that no new self-intersections are introduced. The ‘ﬁnger moves’ will help us to do that.
See Figures 35 (and eventually 36). To begin, we explain the pictures in Figure 35 The
ﬁrst column shows foliated neighborhoods N of a subarc of one of the clasp arcs. We
give separate pictures of the two foliated branches, N1 (the ﬁrst branch) and N2 (the
second branch). They intersect transversally. By hypothesis the clasp arc (and so also
its preimagesγ+ andγ−) is transverse to the leaves of H. We have oriented the clasp
arc (arbitrarily).
We are interested in modifying the position of one of the clasp arcs in a neighborhood
of a singular leaf on one of two branches N1 or N2. Since singular leaves correspond to
places where one of the two branches is tangent to a ﬁber ofH, and since the two branches
intersect transversally along a clasp arc, we may assume that there is a neighborhood
of the singular point in which the other branch is foliated without singularities. The
neighborhood has been chosen so that N2 is foliated without singularities, but N1
contains a singularity, together with the vertex endpoint of one of the branches of the
singular leaf. There are two sign choices: the sign of the vertex and the sign of the
singularity. We have chosen these to be (+, +), but in a moment we will consider the 4
possible sign choices. There are also little ‘+’ signs next to the two components of the
clasp arcs. They indicate which side of N2 (resp. N1) is the positive side, atγϵ (resp.
γ−ϵ).
Geometry &Topology 10 (2006)
462 Joan S Birman and William W Menasco
+
+
+
++
+
+
-
+
+ +
+
+
+
foliated neighborhood of
subarc of clasp arc
same neighborhood
after ﬁrst ﬁnger move
same neighborhood
after second ﬁnger move
ﬁrst branchsecond branch
1 23
1 2 3
1
2
3
γϵ
1 2 3
1
2
3
γϵ
p
α
1 2 3
1
2
3
γϵ
3 2 1
γ−ϵ
3 2 1
γ−ϵ
p
11.522.5 3
11.522.53
neg
pos
γ−ϵ
Figure 35: Controlled local changes in the clasp arc in a neighborhood of a singularity after the
ﬁrst and second ﬁnger moves
+
-
+
-
+
-
-
-
-
+
+
+
+
+
+
-
-
+
+
+
(+, +) (+,−)
(−,−) (−, +)
11.522.5 3
11.522.53
11.522.5 3
11.522.53
3 2.521.51
32.521.51
3 2.521.51
32.521.51
Figure 36: The 4 possible choices of the signs of the pair (vertex,singularity)
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 463
Selected ﬁbers Hθi have labels i = 1, 2, 3. The labels on the ﬁbers and the way that
γ intersects them and the little + signs next to γϵ and γ−ϵ completely determine the
position of N in 3–space, relative to the coordinate system provided by the ﬁbers of
H. We are ready to describe our two controlled changes in the clasp arc, and the
corresponding changes in the foliation of N1 and N2 and in the way thatγϵ andγ−ϵ
intersect the leaves in the foliation.
We now deﬁne the moves precisely:
(1) Our ﬁrst ﬁnger move, illustrated in the middle column of Figure 35, pushes γ
across the horizontal branch of the singular leaf in the ﬁrst branch, creating two
points where it is not transverse to the ﬁbers of H, one on ﬁber 1 and the other
on ﬁber 3. This move is always possible, because it occurs within an arbitrarily
small neighborhood of the singularity. The corresponding change in the second
branch can be understood by noticing that before the changeγϵ intersected ﬁbers
1,2,3 transversally in that order. After the change there are two points of tangency
with ﬁbers of H, the ﬁrst with ﬁber 3 and the second with ﬁber 1. This explains
the doubling back ofγ−ϵ after the ﬁrst ﬁnger move.
(2) Let α denote the subarc of the clasp arc which is between the two points of
non-transversality, and let p∈α∩ ﬁber 2 be the point which is closest to the
singularity on γϵ. The second ﬁnger move, illustrated in the right column of
Figure 35, pushes a neighborhood N(p) of p on α across the singularity and
across the vertex, staying within a neighborhood of the singular leaf. The foliation
on the ﬁrst branch is unchanged. The foliation of the second branch changes in
an arbitrarily small neighborhood of p on the second branch. Two new vertices
of opposite parity and two new singularities of opposite parity are created, as
illustrated in the bottom row sketch.
See Figure 36 for the local changes with the four possible sign choices for the pair
(vertex,singularity).
Remark 4.4.1 The two ﬁnger moves are always possible because of their local nature
and because of our control over the geometry. We have illustrated the case when the
singularity and vertex are both positive. The other three cases differ from this one by
local symmetries. Observe that we have given a great deal of detailed data in Figures 35
and 36, including the cyclic order of leaves in the ﬁbration, the signs of the singularities
and the signs of the vertices. Fibers of H are level sets for positioning the two branches
of the immersed surface in 3–space. The test for whether the ﬁnger moves are realizable
in 3–space is to examine them on a sequence of ﬁbers of H, and the data in Figures 35
and 36 sufﬁces for that purpose.
Geometry &Topology 10 (2006)
464 Joan S Birman and William W Menasco
If braid foliations had been available as a tool during the basic construction, we could
have used the two ﬁnger moves then. We stress this because later we will use an
inductive argument and we need to know that, after many changes, we are still in the
situation of the basic construction. ♦
