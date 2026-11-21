---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-031-46-example-41-continued
section_title: "Example: 41 continued"
section_number: 4.6
pages: 27-29
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
41 continued. We brieﬂy demonstrate the generalized torsion formula,
using representations on the geometric component of the character variety X41 for the ﬁgure-
eight knot complement.
z
z′
z′′ w
w′
w′′
µ
z
z′
z′′
w
w′
w′′
z
z′
z′′ w
w′
w′′
z
z′
z′′
w
w′
w′′
λ
Figure 8. Longitude path for the ﬁgure-eight knot complement.
We may consider the same triangulation as in Section 2.6. The edge and meridian equa-
tions (2.14) are deformed to
(4.16)
z2w2z′′w′′ = 1 ,
zwz′′ = −m2 ,
28
TUDOR DIMOFTE AND STAVROS GAROUFALIDIS
with z′′ = 1 −z−1, w′′ = 1 −w−1 as usual. In addition, there is a longitude equation that
may be read oﬀfrom the longitude path in Figure 8. In logarithmic (combinatorial) form,
we have −2Z + 2Z′ = 2v, or
(4.17)
−4Z −2Z′′ = 2v −2πi ,
from which we identify
(4.18)
C = (−2, 0) ,
D = (−1, 0) ,
νλ = −1.
Dividing (4.17) by two and exponentiating, we ﬁnd
(4.19)
z−2z′′−1 = ℓ,
with ℓ= −ev. This is the appropriate square root of (4.6) for lifting the geometric repre-
sentations to SL(2, C). We can easily check it: by eliminating shape parameters from (4.16)
and (4.19), we recover the geometric SL(2, C) A-polynomial for the ﬁgure-eight knot,
(4.20)
Ageom
41
(ℓ, m) = m4 −(1 −m2 −2m4 −m6 + m8)ℓ+ m4ℓ2 .
We may also use equations (4.16)–(4.19) to express the shape parameters as functions of
ℓand m. We ﬁnd
(4.21)
z = −m2 −m−2
1 + m2ℓ,
w =
m2 + ℓ
m2 −m−2 .
These are functions on the curve Y geom
41
= {Ageom
41
(ℓ, m) = 0}.
The ﬂattening (2.15) does not satisfy the new longitude constraint C · f + D · f ′′ = νλ, so
we must ﬁnd one that does. The choice
(4.22)
(fz, f ′
z, f ′′
z ; fw, f ′
w, f ′′
w) = (0, 0, 1; 0, 0, 1)
will work. Repeating the calculation of Section 3.1 with the same A and B but the new
generalized ﬂattening, we now obtain
τ41(ρm) = ±1
2 det

z′′ + 1
w′′ + 1
1
w′′

zw
= ±1
2(z′′w′′ −1)zw
= ±1 −m2 −2m4 −m6 + m8 −2m4ℓ
2m4(m2 −m−2)
.
(4.23)
This is in full agreement with the torsion found by [GM08, DGLZ09]. Note that for ﬁxed
m there are two choices of representation ρm on the geometric component of the character
variety; they correspond to the two solutions of Ageom
41
(ℓ, m) = 0 in ℓ.
Remark 4.5. It is interesting to observe that the numerator of (4.23) is exactly ∂Ageom
41
/∂ℓ.
That the numerator of the geometric torsion typically carries a factor of ∂Ageom
41
/∂ℓmight be
gleaned from the structure of “ ˆA-polynomials” in [DGLZ09, GS], and will also be explored
elsewhere.
THE QUANTUM CONTENT OF THE GLUING EQUATIONS
