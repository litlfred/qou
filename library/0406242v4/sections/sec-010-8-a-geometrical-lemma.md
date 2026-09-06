---
doc_id: 0406242v4
doc_title: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements FRANC¸ OIS GUÉRITAUD APPENDIX BY DA VIDFUTER"
section_id: sec-010-8-a-geometrical-lemma
section_title: "A geometrical lemma"
section_number: 8
pages: 20-23
source_pdf: 0406242v4.pdf
source_sha256: 27e48b483007b824
---
Deﬁnition 8.1 In the universal cover of the tessellationA of the torus at inﬁnity of
Vϕ (Figure 4), a fan is a sequence of at least three consecutive layers, such that the ﬁrst
and last layers are grey and all layers in between are white. Fans are in bijection with
the subwords of Ω of the form RLkR or LRkL with k≥ 2 (see the remarks to Figure 4
in Section 4).
Geometry &Topology 10 (2006)
Canonical triangulations 1259
Lemma 8.2 Suppose w0 = 0, so that Ω contains a subword L|RkL with k≥ 2, or
L|Rk|L with k≥ 3 (in the latter case, the second bar indicates thatwk vanishes as well as
w0). The corresponding fan admits a complete Euclidean structure with boundary (with
angles prescribed by the wi’s). Moreover, let Q, P, T be the lengths of the segments of
the broken line corresponding to the ﬁrst R, in the order indicated in Figure 9 ( P, T
are the sides adjacent to the apex in a ﬂat upward-pointing grey [hinge] triangle, in the
sense of Figure 3). Then Q< P + T .
u0
1
u0
2u2
u0
k/NUL2
u0
/NUL1
P
ukC1
u/NUL1
uk
u1Q
u0
k/NUL1
u0
0
T
uk/NUL1
uk/NUL2
/NUL1
1
0
u0
k
u0
D0
Figure 9: The situation where Q≥ P + T cannot hold
Proof We ﬁrst restrict our attention to the case L|RkL, k≥ 2. The interior vertices of
the topological fan correspond to the indices i living between two R’s, ie 1≤ i≤ k− 1,
in the sense that holonomy around thei–th vertex ui (Figure 9) is controlled by∂V/∂wi
(Sublemma 6.4). When 2 ≤ i≤ k− 1, none of the triangles adjacent to ui are ﬂat,
so wi can vary in a small interval without making the m–tuple w exit the domain
¯P; consequently, the value of wi in that interval is critical, which by the ﬁrst case
(nonhinge) of Sublemma 6.4 implies that the holonomy around the associated vertex ui
is trivial. As for i = 1, the corresponding vertex u1 is adjacent to a ﬂat angle z0 =π
(Figure 9) so its holonomy is not imposed by the wi’s (when a triangle has an angleπ,
the other two angles are always 0 while the adjacent sides may have arbitrary lengths).
The case of L|Rk|L is similar: for indices 2≤ i≤ k− 2, Sublemma 6.4 applies, while
for i = 1 or k− 1 holonomy is not imposed by the wi’s.
Therefore we can embed the fan as an inﬁnite necklace of triangulated polygons into
Geometry &Topology 10 (2006)
1260 Franc ¸ois Gu´eritaud and David Futer
C. We shall no longer distinguish L|RkL from L|Rk|L here, and shall formulate all
properties in terms of complex numbers in order to keep track of oriented angles. We
make two consecutive nodes (ie lifts of the (2 k + 4)–valent vertex ofA associated
to the full subword LRkL) coincide with−1 and 1 in C, and also denote by ui the
complex coordinate of the copy of ui between these nodes (the index i actually ranges
from−1 to k + 1; see Figure 9). Incidentally, one can show that the ui form (part of)
an orbit of a certain deck transformation of the universal cover H3→ Vϕ. We will
discuss this more at the end of Section 10.
We arrange matters so that Im(u0)< 0 and u1 lies on the open segment (u0, 1). While
removing any node disconnects the fan, Condition (1)-iii implies that the image of the
embedding is invariant under a horizontal translation of length 2. In particular, the
geometric link of each node, such as 1 or−1, is completely determined. To prove the
assertion of the Lemma, it is sufﬁcient to show that Re(u0)< 0. Assume Re(u0)≥ 0
(so u0 lies in the lower-right quadrant) and aim for a contradiction.
The similarity property of the triangles with vertices 1 , ui, ui+1 and−1, ui, ui−1 is
expressed by the relation ui+1−1
ui−1 = ui−1+1
ui+1 , hence by induction
(ui+1− 1)(ui + 1) = (ui− 1)(ui−1 + 1) =··· = (u1− 1)(u0 + 1) =: K.
Then, as u1 sits between 1 and u0, the number u1− 1 is a positive (real) multiple of
u0− 1, so K is a positive multiple of u2
0− 1 which implies Im(K)≤ 0. Let D be the
line through 0 and the points±
√
K : either D is vertical, or D visits the upper-left and
lower-right (open) quadrants. Let D′ be the line through 1, parallel to D; and deﬁne
u′
i := 2+ui for all i. By deﬁnition of K , the rays [1, ui+1) and [1, u′
i) are symmetric with
respect to D′. Moreover, the rays through u0, u1,..., uk, uk+1, u′
k, u′
k−1,..., u′
0, u′
−1, u0
issuing from 1 (in that cyclic order) divide C into angular sectors of sum 2π realizing
the geometric link of a node of the fan, as speciﬁed by the angles xi, yi, zi≥ 0. Finally,
since all these angles are nonnegative, the symmetry of the link with respect to D′
implies that for all−1≤ i≤ k, the point u′
i (resp. ui+1) is on the right (resp. left) of
D′.
Recall Im(u0) < 0. Suppose by induction Im(ui) < 0 for some 0 ≤ i≤ k. Then
Im(u′
i)< 0. Considering the direction of D′ and the symmetry property with respect to
D′, this implies Im(ui+1)< 0. By an immediate induction, the angular sector ˆuk+11u′
k
(just above 1) is larger than π. But it is an angle of the link at the node 1 (namely,
zk+1), giving a contradiction.
Of course, a statement similar to Lemma 8.2 holds for subwords LRk|L, and also for
R|LkR, R|Lk|R and RLk|R.
Geometry &Topology 10 (2006)
Canonical triangulations 1261
