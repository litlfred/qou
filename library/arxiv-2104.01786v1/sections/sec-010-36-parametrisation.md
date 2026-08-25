---
doc_id: arxiv-2104.01786v1
doc_title: "Spin(11, 3), particles and octonions"
section_id: sec-010-36-parametrisation
section_title: "Parametrisation"
section_number: 3.6
pages: 14-15
source_pdf: 2104.01786v1.pdf
source_sha256: 34087d5063ef5507
doc_brief: "Spin(11, 3), particles and octonions — The fermionic ﬁelds of one generation of the Standard Model, including the Lorentz spinor degrees of freedom, can be identiﬁed with components of a sin gle real"
---
It will help if we develop the notation a bit further. We have seen that a Spin(4, 3) spinor
y ∈ ˜O splits into its (1 , 0), (0, 1) components
y = ˜P+y + ˜P−y :=y+ +y−, (45)
where
˜P± = 1
2 (I ± i ˜J) (46)
are the projectors. The split octonion y+ transforms as a 2-component Lorentz and SU(2)
spinors, and y− transforms as a 2-component Lorentz spinor of the opposite chir ality, and
again as a SU(2) spinor. Note that the two complex octonions y± are related by the complex
conjugation y− = (y+)∗.
It will be helpful to write down the explicit parametrisation of the oct onions y± by the
components of the Lorentz and SU(2) spinors. Using (40) we have
w0 = 1
2 (u1 +d2), w 3 = 1
2(u1 −d2), w 1 = 1
2(u2 +d1), w 2 = i
2 (u2 −d1). (47)
We also have for the real coordinates on ˜O
y0 = (w0 +w∗
0), y 4 = −i (w0 −w∗
0), y i = (wi +w∗
i ), y i+4 = −i (wi −w∗
i ), (48)
withi = 1, 2, 3, and where the star denotes the complex conjugation. This mean s that we have
y+ = 1
2


u1 +d2
u2 +d1
i (u2 −d1)
u1 −d2
−i (u1 +d2)
−i (u2 +d1)
(u2 −d1)
−i (u1 −d2)


. (49)
4Below we will see that this SU(2) corresponds to the diagonal subgr oup in SU(2) L × SU(2)R.
14
If we introduce an octonion y parametrised in this way, a computation gives the expected
Lorentz and SU(2) invariant pairing
⟨y,y ⟩ = ⟨y+,y +⟩ + ⟨y−,y −⟩ =
(
u d
) (
0 1
−1 0
) (
u
d
)
+ c.c., (50)
where c.c. stands for ”complex conjugate”, and we have used the index-free 2-component spinor
notation for the pairing of 2-component spinors
ud = −du :=uTǫd, u =
( u1
u2
)
,d =
( d1
d2
)
, ǫ :=
( 0 1
−1 0
)
. (51)
From now on, we will never spell out the Lorentz pairing of 2-compon ent spinors in terms
of matrices, always using the index-free (and matrix-free) notat ion. But in order to avoid
confusion, it will be useful to explicitly write the SU(2) invariant pairin g in matrix terms. Also,
from now on ”complex conjugate” will always refer to the operation that maps between the
(1, 0), (0, 1) eigenspaces of the complex structure ˜J. When we consider Spin(11 , 3), there will
be another complex structure ﬂoating around, but in order to avo id confusion we will always
spell out the complex conjugate with respect to this other complex structure explicitly.
We can also write a more general formula for the pairing of two diﬀere nt Spin(4, 3) spinors.
We have
⟨y1,y 2⟩ = ⟨y+
1,y +
2 ⟩ + ⟨y−
1,y −
2 ⟩ =
(
u d
)
1
( 0 1
−1 0
) ( u
d
)
2
+ c.c. (52)
The ﬁrst term is a Lorentz and SU(2) invariant pairing of two diﬀeren t 2-component Lorentz
and SU(2) spinors.
