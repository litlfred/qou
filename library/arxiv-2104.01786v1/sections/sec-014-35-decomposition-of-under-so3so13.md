---
doc_id: arxiv-2104.01786v1
doc_title: "Spin(11, 3), particles and octonions"
section_id: sec-014-35-decomposition-of-under-so3so13
section_title: "Decomposition of under so(3)so(1,3)"
section_number: 3.5
pages: 13-14
source_pdf: 2104.01786v1.pdf
source_sha256: 34087d5063ef5507
toc_source: outline
doc_brief: "Spin(11, 3), particles and octonions — The fermionic ﬁelds of one generation of the Standard Model, including the Lorentz spinor degrees of freedom, can be identiﬁed with components of a single real"
---
The split octonions ˜O form the spinor representation of Spin(4, 3). When we restrict to Spin(3)×
Spin(1, 3), we expect the spinor to transform as spinor with respect to both of the factors. It
is nevertheless very interesting to see how this happens explicitly.
The (1, 0) coordinates on ˜O for the complex structure ˜J are given by
w0 := 1
2(y0 + i y4),
wi := 1
2(yi + i yi+4),
(35)
where the index i = 1, 2, 3 and we introduced the factors of 1/2 for future convenience.
The transformations from so(3) × so(1, 3) commute with ˜J and thus preserve the (1, 0) sub-
space. Therefore, they can be described as 4 × 4 complex matrices acting on the 4-columns
(w0, w1, w2, w3). Explicitly, we have
Xso(3) =




0
i x
i y
i z
i x
0
z
−y
i y
−z
0
x
i z
y
−x
0



,
(36)
where
x = ˜ω23,
y = −˜ω13,
z = ˜ω12
(37)
are 3 real parameters. We also have
Xso(1,3) =




0
a
b
c
a
0
i c
−i b
b
−i c
0
i a
c
i b
−i a
0



,
(38)
where
a = −˜ω45 + i ˜ω67,
b = −˜ω46 −i ˜ω57,
c = −˜ω47 + i ˜ω56
(39)
are complex parameters. It can be veriﬁed that the matrices Xso(3) and Xso(1,3) commute.
It is then easy to check that the 2-component columns
u =
 u1
u2

:=
 w0 + w3
w1 −i w2

,
d =
 d1
d2

:=
 w1 + i w2
w0 −w3

(40)
transform under Xso(1,3) transformations as 2-component spinors of the same Lorentz chirality,
that is
u →Au,
d →Ad,
A =

c
a + i b
a −i b
−c

.
(41)
On the other hand, the 2-component column with u, d as entries transforms under Xso(3) as
 u
d

→

i z
y + i x
−y + i x
−i z
  u
d

.
(42)
13
Summarising, by introducing the complex structure ˜J, the space of split octonions ˜O = R8
splits into its (1, 0) and (0, 1) eigenspaces. The (1, 0) eigenspace C4 transforms as the spinor
representation of Spin(3), as well as the 2-component spinor representation of the Lorentz group
Spin(1, 3)
C4
(1,0) = (2, 2, 1).
(43)
The complex conjugate (0, 1) eingespace transforms as the spinor of Spin(3), as well as the
complex conjugate 2-component spinor representation of Lorentz
C4
(0,1) = (2, 1, 2).
(44)
Thus, a single copy of ˜O gives us a 2-component Lorentz spinor that is at the same time a
spinor of what can be identiﬁed as ”weak” SU(2).4 Thus, the ”weak” SU(2) and the Lorentz
group are very naturally uniﬁed within Spin(4, 3).
