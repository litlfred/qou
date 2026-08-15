---
doc_id: 0310279v5
doc_title: "Stabilization in the braid groups I: MTWS JOAN S BIRMAN WILLIAM W MENASCO"
section_id: sec-020-45-creating-symmetric-normal-neighborhoods-of-th
section_title: "Creating symmetric normal neighborhoods of the clasp arcs"
section_number: 4.5
pages: 52-58
source_pdf: 0310279v5.pdf
source_sha256: a1d472d37291a333
doc_brief: "Stabilization in the braid groups I: MTWS JOAN S BIRMAN WILLIAM W MENASCO — 30 sections: Introduction; The problem; Block-strand diagrams and template"
---
In Section 4.3 we modiﬁed the discs R1,..., Rk which had been constructed as part
of the basic construction to very special foliated discs which we called tabs. Thus we
now know that each clasp arcγi
+ is contained in a tab. In this section we study γi
+ and
γi
− and arrange that they are contained in much larger neighborhoods which support a
canonical foliation. We will call them normal neighborhoods. The modiﬁcations will
be made with the help of the ﬁnger moves of Section 4.4, at the expense of adding
new b–arcs (see Section 3.3). Intuitively, the new b–arcs add pouches to the surface,
and so give additional ‘room to move around’. The normal neighborhoods which we
will construct will give us choices, which can be made one way or another as it is
convenient. For example we will be able to regard a clasp arcs as being on either side
of its associated chain of singular leaves and in braid position, or as being contained
in a union of leaves and so lying in a union of ﬁbers of H. Let γϵ⊂PA be a clasp
+
+
+
+
+
+
-
- -
-
+
+
+
+
-
-
-
-
- -
+ +
+ +
- -
--
ϕ1
ϕ2
ϕ3
ϕ4
γ+
γ−
γ−
δk
−δk
δk
−δk
δ1
−δ1
δ1
−δ1
−δk
δk
δk−1
−δk
δk
δk−1
−δ1
δ1
−δ1
δ1
−δ1
δ1
−δ1
δ1
−δ2 −δ2
Figure 37: Normal neighborhoods of γ− and γ+ inPA . The left (resp. middle and right)
sketch shows N+ (resp. N−, N− ). The arc γ− ends near X+ in the middle sketch and in the
interior ofPA in the right sketch. In all 3 sketches the foliation is deﬁned up to reﬂection about
a vertical axis which joins X− and X+ .
arc with the property thatγ+ crosses k singular leaves. A neighborhood Nϵ ofγϵ is a
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 465
normal neighborhood (Figure 37, which gives an example, should be helpful) if the
following conditions hold:
(1) Nϵ⊃γϵ. Also Nϵ intersects no other clasp arcs.
(2) Nϵ contains 2 k disjoint ‘horizontal’ pathsϱϵ
1,...,ϱ ϵ
2k , each contained in the
singular leaves of Nϵ and each containing two vertices and two singularities.
Traversingγϵ, starting at the Xϵ endpoint, each ϱϵ
i is crossed once. The vertices
on ϱϵ
2i−1 (resp. ϱϵ
2i) have sign ϵ (resp.−ϵ). For 1 ≤ i≤ k, the singularities
on ϱϵ
2i−1 have parity ϵδi and the singularities on ϱϵ
2i have parity−ϵδi, where
δi =±.
(3) ∂Nϵ =ϕ1∪ϕ2∪ϕ3∪ϕ4 where:
(a) ϕ1⊂ Xϵ.
(b) ϕ2 is a path contained in one arc of type aϵ and k singular leaves. It
contains k vertices of signϵ.
(c) ϕ3 is transverse to the foliation ofPA .
(d) ϕ4 is a path contained in k singular leaves and one arc of typeb (or type aϵ,
in the special case when the puncture point on γϵ is near X−ϵ). It contains
k vertices of sign−ϵ.
(e) Traversingϕ1⊂ Xϵ∩∂Nϵ, beginning at the pointϕ1∩ϕ4, we pass through
the endpoint of a type aϵb singular leaf, and end at the Xϵ endpoint of an
aϵ leaf.
We say that (N+, N−) is anormal neighborhood pairif each Nϵ is a normal neighborhood
of γϵ. Our main result in this section will be very important in the detailed work we
will need to do to push X+ acrossCA to X−, and to prove the MTWS. We stress this
by calling in a ‘proposition’.
Proposition 4.5.1 For each clasp arc pair (γ+,γ−) = (γi
+,γ i
−) we may assume
that there is a normal neighborhood pair (N+, N−). Moreover, within the normal
neighborhoods, we may assume that instead of being transverse to the foliation each
clasp arc is positioned in a ﬁnite union of leaves in its normal neighborhood pair.
Proof The proof of Proposition 4.5.1 will occupy the rest of this section. Our work
begins with the tab neighborhoods ofγ1
+,...,γ k
+ which we constructed earlier, when
we simpliﬁed the discs R1,..., Rk of the basic construction. The tab neighborhood
construction told us nothing about the other sheet ofCA , and our ﬁrst goal is to modify
it so that we have related tab neighborhoods of γ1
−,...,γ k
−. See Figure 38 for an
example. After that we will iterate the construction to produce normal neighborhoods.
Letγ be a clasp arc and let γ+,γ−, be its preimages inPA . We say that (T+, T−) is
a tab neighborhood ofγ inPA if the following hold:
Geometry &Topology 10 (2006)
466 Joan S Birman and William W Menasco
-
-
-
-
+
+
-
-
+
δ3
δ2
δ1
e−
e+
δ1
δ2
δ3
−δ1
−δ2
−δ3
e−
e+
γ−
γ+
Figure 38: Tab neighborhood pair inPA
(i) ∂Tϵ =α∪β where α⊂ Xϵ and β is an arc that is transverse to the foliation of
PA .
(ii) There is a simple path lϵ⊂ Tϵ, contained in singular leaves. It starts on Xϵ,
contains all k vertices and all k singularities. If the singularities on l+ have sign
δ1,δ 2,...,δ k on T+, then the singularities on l− have sign−δ1,−δ2,..., −δk .
(iii) The arcγϵ⊂ Tϵ is the only clasp arc which intersects Tϵ. It intersects each of
the k singular leaves in the induced foliation of Tϵ exactly once.
(iv) Let e+e′, e′e′′,..., e′...′e−⊂ γ+⊂ T+ be a subdivision of γ+ into k subarcs
such that each subarc crosses one singular leaf. Then the corresponding induced
subdivision ofγ− in T− given by the immersionCA also has the property that
each subarc crosses one singular leaf.
Lemma 4.5.1 We may assume that each pair of clasp arcsγ has a tab neighborhood
(T+, T−) for its associated pair (γ+,γ−)⊂PA .
Proof To prove the lemma we will make repeated use of the ﬁrst and second ﬁnger
moves. Consult Figure 39, which shows the changes we will make as they appear on
T+, and Figure 40, which depicts the corresponding changes onPA in a neighborhood
ofγ−. After the sequence of changes γ+ will have moved to the other side of the chain
of singular leaves in T+, but the key features will not have changed.
By Lemma 4.3.1 we may assume thatγ+ is already contained in a tab neighborhood
T+. Since we have not changed the fact that γ is transverse to ﬁbers of H, it follows
that in a sufﬁciently small foliated neighborhood of γ− inPA the arc γ− will also be
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 467
(a) (b) (c) (d) (e) (f) (g)
e−
p
γ+
p′
e′
p
p′
p′
∆
e′
p′
p′′
e′
p′
p′′
e′
p′
p′′
∆′
e′
p′
e′′
p′′
Figure 39: Local changes, as they appear on T+
transverse to the leaves of the foliation ofPA . Some of the leaves intersecting γ− may
be singular. Label them l1,..., lt , as in Figure 40. The ﬁrst change we introduce is to
perform the ﬁrst ﬁnger move on a small subarc of γ which is just below the singular
leaf in the end-tile of T+, pushing γ across the singular leaf, as in the passage from
sketch (a) to (b) in Figure 39(a)→ (b). This will induce a corresponding change in γ−,
as illustrated in Figure 40(a)→ (b).
We next perform the second ﬁnger move as shown in the passage Figure 39(b)→39(c)
and the corresponding alteration 40(b)→40(c). It will be helpful to label the two new
vertices and singularities introduced by this second ﬁnger move as v1 and v2 (the
vertices) and s1 and s2 (the singularities). This second ﬁnger move creates a disc ∆ in
the tab T+ whose interior is necessarily embedded because it is on a tab-neighborhood
of γ+ and there is only one clasp arc on each such tab-neighborhood. We use it to
do the second change in foliation (see Lemma 3.2.2 and Figure 21). The notation has
been chosen so that s1 in Figure 40(c) and ∆ in Figure 39(c) correspond to s1 and ∆
in Figure 21. The singularity s2 of Figure 21 is not shown in Figure 40(c), also the
singularity s2 of Figure 40(c) is similarly not part of the geometry of Figure 21. After a
series of such changes in foliation the singular leaf which is labeled m in Figure 40(c)
will have exchanged order with the singularities in the leaves l1,..., lt as illustrated
in Figure 40(d). (Note that this implies that each of the leaves l1,..., lt has one of its
endpoints at v2). After the change in foliation the clasp arc can be tightened, resulting
in the picture we see in Figure 40(e).
From the tab neighborhood deﬁnition, condition (ii) on the signs of the vertices follows
from the fact that the vertex endpoint of a singular leaf of the foliation ofPA which
begins at Xϵ necessarily has sign−ϵ. But then, the tiles which make up Tϵ are all type
Geometry &Topology 10 (2006)
468 Joan S Birman and William W Menasco
(a) (b) (c)
(d) (e)
l1
lt
γ−
e′
l1
lt
e′
l1
lt
m
v2
s2 v1
s1
e′
lt l1
e
m
s1
v1
v2
s2
v2
v1
e′
s1
s2
e
modiﬁedγ−
Figure 40: Local changes, depicted in a neighborhood of γ− onPA
a−ϵa−ϵ and never type aϵaϵ.
The point e′ in Figure 39(d) is deﬁned to be the point where the deformed clasp arc
is tangent to a ﬁber of H. Figures 39(d) →39(e)→ 39(f)→39(g) show how the
argument can be iterated. If there are k tiles on T+, then after k iterations—ﬁnger
move 1 followed by ﬁnger move 2 followed by the second change in foliation, or as we
shall call it, the FFF move, we will have created a tab neighborhood onPA forγ−.
The subdivision of the tabs described in condition (iv) is achieved automatically via the
iteration of the FFF sequence. Since we have not moved γ+ outside of T+ and since
after the ﬁnal iteration of our second change in foliation γ+ will again be transverse
to the foliation, we will have created a tab neighborhood pair ( T+, T−) for γ as its
associated pair (γ+,γ−).
We refer the reader back to the discussion in Section 4.4, where we introduced the two
ﬁnger moves, to verify that the parity information of condition (ii) is satisﬁed. The
proof of Lemma 4.5.1 is complete.
We are ready to complete the proof of Proposition 4.5.1 By repeating the procedure of
Lemma 4.5.1 we can replicate another T+ neighborhood inside the T+ neighborhoods
of Figure 38. This places γ+ inside a normal neighborhood N+. Since N+ contains a
tab neighborhood T+ which belongs to a tab neighborhood pair, we can interchange the
roles ofγ+ andγ− to produce a corresponding normal neighborhood forγ−. The main
point is that the application of our FFF procedure does not moveγ+ outside the tab
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 469
neighborhood that is nested inside T+. The key properties of the normal neighborhoods
follow.
+
+
+
+ +
+
+
+
− −
− −
−−
+
+
+
++
+
+
+
− −
− −
−−
+
+ +
+ +
+
1 2
3
45
6
1 2
3
45
6
1 2
3
45
6
e′
e′′
e′′′
γ− γ−
(a) (b) (c)
Figure 41: Positioning the clasp arc γ− into a ﬁnite number of leaves (singular and/or
non-singular)
We now claim that our procedure for creating ( N+, N−) also creates the conditions
necessary for pushing the associated clasp intersection arc into a union of leaves. To
see this let us review our construction of the normal neighborhood pair. See Figure 38.
Recall the notation: e+e′, e′e′′,..., e′...′e−⊂γ−⊂ T− is a subdivision of the clasp
arc into k subarcs such that each subarc crosses one singular leaf. Observe that each
of the subarcs e+e′, e′e′′,..., e′...′e−⊂γ−⊂ T− has a neighborhood which has the
foliation of one of the tiles in Figure 31. So except for a neighborhood around each
e′, e′′,..., e′...′ in γϵ, we can push γϵ into a ﬁnite number of leaves. The parity of each
of these singular leaves is the same as the parity of the pierce end-point of γϵ. (See
the end of Section 2 for the deﬁnition of the sign). Figure 41(b) illustrates an example
of a clasp arc having a positive pierce end-point that has been partially pushed into
singular leaves. In the example which is illustrated the pierce point is positive, and since
there is a negative singularity on the ‘vertical’ chain of singular leaves the clasp arc is
forced to bend in the manner that is illustrated in sketch (b). Figure 41(c) illustrates
that, after a change in ﬁbration which introduces singular leaves that have two singular
points (Figure 41(a)) it is possible to push our clasp arc into a ﬁnite union of leaves by
pushing the remaining arc neighborhoods of the points e′, e′,..., e′...′ into leaves of the
Geometry &Topology 10 (2006)
470 Joan S Birman and William W Menasco
foliation. These two-singularity tiles arise naturally during the change of ﬁbration of
Figure 20 in the following way: as we perform the change of ﬁbration in Figure 20 we
must pass through a tile having six sides and a two-singularity singular leaf. (This is
explained carefully in Birman–Finkelstein [4, Figure 2.2]). The two singular points
will always have common parity. In the example, after the change we can reposition
the clasp arc so that it only passes through positive singularities, as in sketch (c). Once
we allow the use of such tiles in the foliation ofPA , the ﬁnal assertion in the proof of
Proposition 4.5.1 follows.
Remark 4.5.1 When we push the clasp arcs into a union of leaves, we lose some of the
symmetry of normal neighborhoods. In this regard we note the following. The symmetry
will be needed in one place: for the construction of ‘thin annuli’ in Section 5.3.1. The
building blocks for those annuli are the regions which are illustrated in Figure 43. To
construct those regions, all we need is a normal neighborhood of that part of a positive
clasp arcγi
+ which begins on X+, follows an a+ arc and alongγ+ to a little bit after it
crosses the ﬁrst singular leaf, together with the corresponding segment on γi
−. In such
a subset of a normal neighborhood, the required symmetry will always be present, even
when it does not extend to a more global symmetry.
