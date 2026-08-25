---
doc_id: arxiv-2104.01786v1
doc_title: "Spin(11, 3), particles and octonions"
section_id: sec-009-34-complex-structures
section_title: "Complex structures"
section_number: 3.4
pages: 12-14
source_pdf: 2104.01786v1.pdf
source_sha256: 34087d5063ef5507
doc_brief: "Spin(11, 3), particles and octonions — The fermionic ﬁelds of one generation of the Standard Model, including the Lorentz spinor degrees of freedom, can be identiﬁed with components of a sin gle real"
---
We now enter into a less familiar part of the discussion. It is clear that any of the 3 Cliﬀord
generators ˜E5, 6, 7 (or any unit vector constructed as their linear combination) can se rve as a
complex structure on ˜O. This complex structure identiﬁes ˜O = C4. What commutes with it in
so(4, 3) is the subalgebra so(4, 2). But this is not the complex structure that is of interest to
us in relation to physics.
Any of the generators ˜E1, 2, 3, 4 squares to plus the identity, and so is not a complex structure.
But we also have the object
τ = ˜E5 ˜E6 ˜E7. (32)
This is an operator that reverses the signs of the positive-deﬁnite directions ˜I, ˜e5, 6, 7 of the split
quadratic form (24), and leaves the negative-deﬁnite directions ˜ e1, 2, 3, 4 intact. As a matrix, this
is the already encountered matrix of the quadratic form (25). This operator squares to plus the
identityτ 2 = I, but anti-commutes with any of the Cliﬀord generators ˜E1, 2, 3, 4 (and commutes
with all the ˜E5, 6, 7 generators). Thus, the product of τ with any one of ˜E1, 2, 3, 4 (or with a unit
linear combination constructed from them) is a complex structure. We choose ˜u = ˜e4 and
deﬁne
˜J := ˜E4τ. (33)
Note the strong analogy with (15). This is the complex structure th at is of our main interest.
Indeed, being given by the product of 4 Cliﬀord generators, its com mutant in so(4, 3) is the
algebra so(3) × so(1, 3). Both groups are very interesting, because the ﬁrst factor r eminds us
of the SU(2) acting on isospin of particles, while the second factor is the Lorentz group. The
ﬁrst factor is the one describing rotations in the ˜ e1, 2, 3 plane, while the second one mixes the
directions ˜e4, 5, 6, 7. The direction ˜ e4 is a timelike direction with respect to the split octonion
quadratic form (24), and we will refer to it as such in what follows. Fo r later purposes we note
that we can rewrite the complex structure ˜J as
˜J := − ˜E1 ˜E2 ˜E3, (34)
i.e., as the product of the timelike Cliﬀord generators that are distinc t from the chosen ˜E4.
12
3.5 Decomposition of ˜O under so(3) × so(1, 3)
The split octonions ˜O form the spinor representation of Spin(4, 3). When we restrict to Spin(3) ×
Spin(1, 3), we expect the spinor to transform as spinor with respect to bo th of the factors. It
is nevertheless very interesting to see how this happens explicitly.
The (1, 0) coordinates on ˜O for the complex structure ˜J are given by
w0 := 1
2 (y0 + iy4), w i := 1
2 (yi + iyi+4), (35)
where the index i = 1 , 2, 3 and we introduced the factors of 1 /2 for future convenience.
The transformations from so(3) × so(1, 3) commute with ˜J and thus preserve the (1 , 0) sub-
space. Therefore, they can be described as 4 × 4 complex matrices acting on the 4-columns
(w0,w 1,w 2,w 3). Explicitly, we have
Xso(3) =


0 i x iy iz
ix 0 z −y
iy −z 0 x
iz y −x 0

, (36)
where
x = ˜ω23, y = −˜ω13, z = ˜ω12 (37)
are 3 real parameters. We also have
Xso(1, 3) =


0 a b c
a 0 i c −ib
b −ic 0 i a
c ib −ia 0

, (38)
where
a = −˜ω45 + i ˜ω67, b = −˜ω46 − i ˜ω57, c = −˜ω47 + i ˜ω56 (39)
are complex parameters. It can be veriﬁed that the matrices Xso(3) and Xso(1, 3) commute.
It is then easy to check that the 2-component columns
u =
( u1
u2
)
:=
( w0 +w3
w1 − iw2
)
, d =
( d1
d2
)
:=
( w1 + iw2
w0 −w3
)
(40)
transform under Xso(1, 3) transformations as 2-component spinors of the same Lorentz ch irality,
that is
u →Au, d →Ad, A =
(
c a + ib
a − ib −c
)
. (41)
On the other hand, the 2-component column with u,d as entries transforms under Xso(3) as
( u
d
)
→
( iz y + ix
−y + ix −iz
) ( u
d
)
. (42)
13
Summarising, by introducing the complex structure ˜J, the space of split octonions ˜O = R8
splits into its (1 , 0) and (0 , 1) eigenspaces. The (1 , 0) eigenspace C4 transforms as the spinor
representation of Spin(3), as well as the 2-component spinor rep resentation of the Lorentz group
Spin(1, 3)
C4
(1, 0) = (2, 2, 1). (43)
The complex conjugate (0 , 1) eingespace transforms as the spinor of Spin(3), as well as the
complex conjugate 2-component spinor representation of Loren tz
C4
(0, 1) = (2, 1, 2). (44)
Thus, a single copy of ˜O gives us a 2-component Lorentz spinor that is at the same time a
spinor of what can be identiﬁed as ”weak” SU(2). 4 Thus, the ”weak” SU(2) and the Lorentz
group are very naturally uniﬁed within Spin(4 , 3).
