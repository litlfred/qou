---
doc_id: arxiv-hep-th-0205308v2
doc_title: "WDVV Equations as Functional Relations"
section_id: sec-003-example-perturbative-seiberg-witten-prepotential
section_title: "Example: perturbative Seiberg-Witten prepotentials"
section_number: null
pages: 7-8
source_pdf: 0205308v2.pdf
source_sha256: 2de5a4f40d80174c
doc_brief: "WDVV Equations as Functional Relations — 5 sections: Introduction; WDVV and dispersionless Hirota equ; The associativity equations as coc"
---
tials
Here we shall consider one of the simplest examples of solutions to th e WDVV equations
coming from Seiberg-Witten theory. These are related to SU (N + 1) perturbative
prepotentials [2] and the corresponding Riemann surface is degene rate. With aij ≡
ai − aj the perturbative prepotential is given by
F = 1
2
N∑
i<j
a2
ij log aij
Λ + 1
2
N∑
i=1
a2
i log ai
Λ . (32)
The second derivatives (3) (for a special choice of Λ) are
Tij = − log aij, i < j ; Tij = Tji, i > j ;
Tii = ln ai +
∑
i<j
ln aij +
∑
j<i
ln aji = ln ai −
∑
j⁄=i
Tij. (33)
Using (33) one may reexpress all matrix elements Tij through a given row explicitly.
For example, in the ﬁrst nontrivial case corresponding to SU (4) one ﬁnds
T =


x y z
y log (ex+y+z − e−y) (e−z − e−y) − y − log (e−z − e−y)
z − log (e−z − e−y) log ( ex+y+z − e−z) (e−z − e−y) − z


=


log
(
e˜x+˜y+˜z + e−˜x) (
e−˜x + e−˜z)
− ˜x ˜x − log
(
e−˜x + e−˜z)
˜x ˜y ˜z
− log
(
e−˜x + e−˜z)
˜z log
(
e˜x+˜y+˜z + e−˜z) (
e−˜x + e−˜z)
− ˜z


=


log
(
eˆx+ˆy+ˆz + e−ˆx) (
e−ˆx − e−ˆy)
− ˆx − log
(
e−ˆx − e−ˆy)
ˆx
− log
(
e−ˆx − e−ˆy)
log
(
eˆx+ˆy+ˆz + e−ˆy) (
e−ˆx − e−ˆy)
− ˆy ˆy
ˆx ˆy ˆz

 .
(34)
Here we have exhibited the diﬀerent dependence on the rows which a re taken as inde-
pendent variables: ( x, y, z ) = ( T11, T 12, T 13), (˜x, ˜y, ˜z) = ( T21, T 22, T 23) and (ˆx, ˆy, ˆz) =
(T31, T 32, T 33).
In the SU (4) perturbative Seiberg-Witten case equation (31) has essentia lly only the
one nontrivial relation ∑
i,k
∂T 2i
∂T 1j
∂T 1k
∂T 3i
∂T 3l
∂T 2k
= δj
l . (35)
The corresponding matrices may be straightforwardly computed u sing (33). It is easy
to check, that (35) holds provided the Hirota relations (cf. with [14 ]) are satisﬁed:
sign(j − i)e−Tij + sign(k − j)e−Tjk + sign(i − k)e−Tki = 0, i ⁄= j ⁄= k, (36)
7
(originating from aij + cyclic = 0) together with
eT11+T12+T13−T23 + eT13+T23+T33−T12 − eT12+T22+T23−T13 = 0, (37)
(coming from aiajk + cyclic = 0) and
eT12+T22+T23 − eT13+T33+T23 = e−T23 (38)
(realizing aij = ai − aj). These may be seen to be satisﬁed upon utilising (33).
