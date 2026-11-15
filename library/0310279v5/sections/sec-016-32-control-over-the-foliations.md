---
doc_id: 0310279v5
doc_title: "Stabilization in the braid groups I: MTWS"
section_id: sec-016-32-control-over-the-foliations
section_title: "Control over the foliations"
section_number: 3.2
pages: 30-34
source_pdf: 0310279v5.pdf
source_sha256: a1d472d37291a333
toc_source: outline
doc_brief: "Stabilization in the braid groups I: MTWS — 41 sections: Front matter; Introduction; The problem"
---
Control over the foliations
Braid foliations are not unique, and in this section we describe some of the ways we have
discovered to modify them. This is an essential part of the argument in the proof of the
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
443
MTWS, because the vertices of valence 1 and 2 that we use to recognize destabilizations
and exchange moves may not be present initially, but after a change in foliation they
may be present. The existence of a vertex of valence 1 or 2 will be one of our ways to
learn when the complexity can be reduced.
The foliation of F depends upon the choice of half-planes Hθ in the ﬁbration of R3 \ A.
A change in ﬁbration is the choice of a new set of half-planes H = {Hθ : 0 ≤θ ≤2π}.
Equivalently, one could ﬁx the ﬁbers of H and the link, and move the surface. This
induces a change in foliation.
The changes which we shall make are always very controlled and very local in terms of
changing the tiling. In particular they do not change the braid, and are supported in a
neighborhood in R3 of subarcs of singular leaves. The question of when such changes
are possible has been studied. They were used in earlier papers by the authors, and we
use those results as needed here. We describe two changes in foliation. For details, see
Birman–Finkelstein [4].
Figure 20: The ﬁrst change in foliation, in the case when both tiles have type bb. There are two
other cases, obtained from the one which is illustrated by deleting part of the bb–tile and adding
one or both dotted arcs as boundary, to convert to an ab–tile. The 3 cases are: case (1), two
bb–tiles; case (2), one ab and one bb–tile; case (3), two ab–tiles.
Lemma 3.2.1 (First change in foliation) Let s1 and s2 be singularities of the same
sign δ = ± in tiles D1 and D2, where D1 and D2 intersect in a common leaf vw of type
b. For example, see the left sketch in Figure 20, which relates to the case when both tiles
Geometry & Topology 10 (2006)
444
Joan S Birman and William W Menasco
have type bb. Then after a change in foliation which is supported on a neighborhood
in 3–space of an arc γ which joins the two singular points, the foliation of D1 ∪D2
changes in one of the two ways which are illustrated in Figure 20. In particular, the
valence of the vertices v and w decreases as a result of the change.
Proof See [4, Theorem 2.1] for a very detailed proof of the Lemma. We note the
following feature of the proof. There are 6 vertices in D1 ∪D2, labeled v, a, y, w, z, b.
The proof in [4] shows that they remain ﬁxed during the change in foliation. There are
also singular leaves vy (resp. vz) with one endpoint at the vertex v in the region of
interest and the other at y (resp. z). In the passage from the left to the middle (resp right)
sketch in Figure 20 there is, at every point in the isotopy, a singular leaf vy (resp. vz)
which contains one of the two singularities. This justiﬁes our labeling that singularity
s′
1 (resp. s′
2) in the middle (resp. right) sketch, because it evolves directly from s1 (resp.
s2) during the isotopy which realizes the change. We call the other singularity s′
2 (resp.
s′
1). In fact (see [4]) if s1 and s2 occur in an angular interval [θ1, θ2] ⊂[0, 2π] in the
ﬁbration H, with s1 < s2 in this interval, then after the change in foliation the new
singularities will still be in the same angular interval, only now, in both cases, we will
have s′
1 > s′
2.
We will need one more change in foliation. It is similar to that of Lemma 3.2.1, except
that it holds without restriction as to the signs of the two singularities which are involved.
We call it the second change in foliation. The reader may ﬁnd Figure 21 helpful in
understanding what it says.
Lemma 3.2.2 (Second change in foliation) Let γ be an arc which is located in a
foliated disc N which is a subset of a foliated surface. Assume that the foliation of
N contains exactly two singular points s1 and s2. Let li be the singular leaf through
si, i = 1, 2. Let Hθi be the ﬁber of H which contains si, i = 1, 2. Suppose that there is
a disc ∆in 3–space, such that:
(i) The interior of ∆has empty intersection with F.
(ii)
∂∆= α ∪γ, with ∆∩N = γ and ∆∩Hθ2 = α.
(iii)
∆is trivially foliated, ie there are no vertices or singularities in ∆.
(iv)
γ ∩l1 = s1 and γ ∩l2 = {p}, where p is a point.
Then after a change in foliation which is induced by pushing N along ∆, changing the
order of s1 and s2, we may assume that γ ∩l1 = s′
2 and γ ∩l2 = ∅. Moreover, the
change in the foliation of F may be assumed to be supported on an arbitrarily small
neighborhood on N of the subarcs [s1, p] ⊂γ and [p, s2] ⊂l2. There could also be
Geometry & Topology 10 (2006)
Stabilization in the braid groups I: MTWS
445
1
2
3
4
5
6
1
2
3
4
5
6
1
2
3
4
5
6
s1
s2
γ
p
s′
1
s′
2
γ
p
α
γ
p
s1
s2
∆
(a)
(b)
Figure 21: Sketch (a) shows the second change in foliation. Sketch (b) shows N, embedded in
3–space, before the change, illustrating the position of ∆. The move is a push downward of s1
along ∆.
several singularities s1, s2, . . . sk, with associated neighborhoods, and if the conditions
are met for each of them in turn then the disc ∆may be used to push s1 past many
singularities, one at a time.
Proof Figures 21(a) shows the foliated disc N before and after the change which we
propose to make. The arrows which are attached to the leaves indicate the direction of
increasing θ. Using the foliation of N, and knowing the signs of the singularities, one
may construct an embedding of N in 3–space, and we have done so in Figure 21(b) in
the case when the signs of the singularities at s1 and s2 are different. (The other case
is similar). In Figure 21(b) ﬁbers of H are to be thought of as horizontal planes. The
auxiliary disc ∆, is also illustrated. The move which we make to realize the change
in foliation in Figure 21(a) is to push N down along the disc ∆. To understand how
this changes the foliation of N, we have labeled certain endpoints on ∂N with numbers
1,2,3,4,5,6. There are non-singular leaves which we call 12, 34, 56, each with arrows
directed inward (to illustrate the direction of increasing θ) and joining 1 to 2, 3 to 4
and 5 to 6 respectively. In the left picture the ﬁrst singularity occurs when leaf 12
approaches leaf 34, but in the right picture the ﬁrst singularity occurs when leaf 12
approaches leaf 56.
Geometry & Topology 10 (2006)
446
Joan S Birman and William W Menasco
