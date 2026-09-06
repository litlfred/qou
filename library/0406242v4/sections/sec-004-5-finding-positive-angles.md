---
doc_id: 0406242v4
doc_title: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements FRANC¸ OIS GUÉRITAUD APPENDIX BY DA VIDFUTER"
section_id: sec-004-5-finding-positive-angles
section_title: "Finding positive angles"
section_number: 5
pages: 10-12
source_pdf: 0406242v4.pdf
source_sha256: 27e48b483007b824
doc_brief: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements FRANC¸ OIS GUÉRITAUD APPENDIX BY DA VIDFUTER — 26 sections: Introduction; The canonical triangulation; Diago"
---
The tetrahedra ∆i and ∆i+1 have two common triangular faces whose union forms
a pleated punctured torus Σ properly isotopic to T×{∗} in T× R. Moreover, Σ
receives a transverse “upward” orientation from the R–factor. Suppose all tetrahedra
∆i are endowed with dihedral angles. Let e be an edge of Σ: if the sum of all dihedral
angles at e below Σ isπ +α, we callα the pleating angle of Σ at e.
In this section we ﬁnd positive dihedral angles for the ideal tetrahedra ∆i. More
precisely, we describe the convex space Π of positive angles xi, yi, zi for the ∆i such
that:
(1)



i — For each i in Z/mZ one has xi + yi + zi =π;
ii — The dihedral angles around any edge add up to 2 π;
iii — For each i in Z/mZ, the three pleating angles of the pleated
punctured torus between ∆i and ∆i+1 add up to 0.
Condition (1)-ii is necessary, though not sufﬁcient, for a hyperbolic structure at the
edges; Condition (1)-iii is necessary, though not sufﬁcient, to make the loop around the
puncture of T a parabolic isometry of H3 (see Sublemma 6.4). This “cusp condition”
(1)-iii restricts the space of angle structures, but will make it a little easier to describe.
Recall the line D that runs from the repulsive ﬁxed point q− to the attractive ﬁxed
point q+ of ϕ across the Farey triangulation. If the tetrahedron ∆i, corresponding
to the Farey edge ei, realizes a diagonal exchange that erases an edgeε′ and replaces
it with ε, we denote by zi the interior dihedral angle of ∆i at ε and ε′ by the fourth
remark following Figure 4. Observe that the slope of ε (resp. ε′) is the rational located
opposite ei in the Farey diagram, on the side of q+ (resp. q−). We deﬁne the half
pleating angle wi byπ− 2wi = zi.
Geometry &Topology 10 (2006)
Canonical triangulations 1249
Thus, if (1)-ii and (1)-iii are to be satisﬁed, the pleating angles of the pleated punctured
torus Σ living between ∆i and ∆i+1 must be
(2) − 2wi, 2wi+1 and 2 wi− 2wi+1.
(Observe the signs: by our deﬁnition, angles pointing upwards, like the “new” edge
of ∆i, are negative pleatings, while angles pointing downwards, like the “old” edge of
∆i+1, are positive ones.) We write the numbers (2) in the corners of the corresponding
Farey triangle (top of Figure 5), distinguishing the cases L and R, and we repeat this
for all indices i.
2c
/NUL2b
2b
/NUL2a2a /NUL 2b
R
2c
L
RL
R
2b
/NUL2b
2b
2wi /NUL 2wiC1
/NUL2wi
2b /NUL 2c2b /NUL 2c
2a /NUL 2b/NUL2a 2a /NUL 2b
2b
/NUL2wi
L
L
eiC1
L
ei
eiC1
R
ei
2c 2c
/NUL2a
2b /NUL 2c
2wiC1
2wi /NUL 2wiC1
2wiC1
/NUL2b
2a /NUL 2b
2b /NUL 2c
/NUL2a
/NUL2b
R
Figure 5: On the bottom row in each case, ei is the horizontal edge
In fact, the values of the wi will also determine the xi and yi. To see this, we must
write down the pleating angles of two pleated surfaces, living above and below the
tetrahedron ∆i. For notational convenience, write
(wi−1, wi, wi+1) =: (a, b, c).
By the fourth remark following Figure 4, the quantity 2xi (resp. 2yi) is the difference
between the numbers written just above and just below the right (resp. left) end of ei
in Figure 5 (the factor 2 comes from the fact that the two edges of ∆i with angle xi
(resp. yi) are identiﬁed). By computing differences between the pleating angles given
in Figure 5 (bottom), we ﬁnd the formulae in Figure 5 for xi, yi, zi (depending on the
letters Ω−
i and Ω+
i , each equal to R or L, living respectively just before and just after
the index i).
Geometry &Topology 10 (2006)
1250 Franc ¸ois Gu´eritaud and David Futer
Ω−
i , Ω+
i L L R R L R R L
xi a + c −a + 2b− c a + b− c −a + b + c
yi −a + 2b− c a + c −a + b + c a + b− c
zi π− 2b π− 2b π− 2b π− 2b
Table 1
Condition (1)-i can be checked immediately, while (1)-ii-iii are true by construction.
From Figure 5, the conditions for all angles xi, yi, zi to be positive are that:
(3)



i — For all i one has 0< wi<π/ 2.
ii — If i is not a hinge index (ﬁrst two cases), 2wi> wi+1 + wi−1.
iii — If i is a hinge index (last two cases),|wi+1− wi−1|< wi.
We call (3)-i the range condition, (3)-ii the concavity condition, and (3)-iii the hinge
condition. The space P of sequences (wi)i∈Z/mZ which satisfy (3), homeomorphic to
the solution space Π of (1), is clearly an open, convex polyhedron of compact closure
in Rm. Moreover, P is nonempty: to exhibit a sequence ( wi) in P, set wj =π/3 when
j is a hinge index, and complete the gaps between consecutive hinge indices j< k with
strictly concave subsequences taking their values in [π/3,π/ 2), eg wi =π/3+ (i−j)(k−i)
(k−j)2
for j≤ i≤ k (indices are of course seen in Z for the evaluation). Figure 6 shows the
typical graph of a sequence (wi) that satisﬁes all conditions of (3). Finally, note that the
formulae of Figure 5 are still valid when Ω is reduced to RL or LR (the letters a and c
are just two names for the same parameter then).
LLRRR
wi
L
=2
0 iLLLRRRRLLLL
Figure 6
