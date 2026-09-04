---
doc_id: 0803219
doc_title: "ACTA MATHEMATICA VIETNAMICA 219 AN INTRODUCTION TO THE VOLUME CONJECTURE AND ITS GENERALIZATIONS"
section_id: sec-016-41-representations-of-the-fundamental-group-of-t
section_title: "Representations of the fundamental group of the trefoil kno t. We"
section_number: 4.1
pages: 24-27
source_pdf: 0803219.pdf
source_sha256: 8e37e11b8c8953c8
doc_brief: "ACTA MATHEMATICA VIETNAMICA 219 AN INTRODUCTION TO THE VOLUME CONJECTURE AND ITS GENERALIZATIONS — In this paper we give an introduction to the volume conjectur e and its generalizations."
---
choose the generators x and y for π 1(S3 \ T ) as in Figure 10. Note that we take
these generators so that their linking numbers with the knot are one. Then the
Figure 10. The two generators of π 1(S3 \ T )
element z (see Figure 11) can be expressed in terms of x and y as follows:
(4.1) z = xyx−1.
From the second crossing and from the third, we have the follo wing relations.
Figure 11. The other element of π 1(S3 \ T )
yzx −1z−1 = 1,
yzy −1z−1 = 1.
THE VOLUME CONJECTURE AND ITS GENERALIZATIONS 243
Using (4.1), these relation are equivalent to the relation
(4.2) yxy = xyx
Therefore π 1(S3 \ T ) has the following presentation.
π 1(S3 \ T ) = ⟨x, y |ωx = yω ⟩
with ω := xy.
Let ρ be a non-abelian representation of π 1(S3 \ T ) at SL(2; C). By [53], we
can assume that ρ sends x and y to
(
m1/ 2 1
0 m−1/ 2
)
and
(
m1/ 2 0
− d m −1/ 2
)
,
respectively. Since
ρ (ω ) =
(
m − d m −1/ 2
− dm−1/ 2 m−1
)
,
we have
ρ (yω ) =
(
m1/ 2(m − d) 1
− d(m + m−1 − d) m−3/ 2 − dm−1/ 2
)
and
ρ (ωx ) =
(
m1/ 2(m − d) m + m−1 − d
− d m −3/ 2 − dm−1/ 2
)
.
Therefore d should equal m + m−1 − 1 and m uniquely deﬁnes a representation.
Putting ξ := tr
(
ρ (x)
)
and η := tr
(
ρ (xy)
)
, we have
ξ = m1/ 2 + m−1/ 2
η = m + m−1 − d
and
F (ξ, η ) = Pω (ξ, η ) = η − 1.
This conﬁrms Theorem 1.2.
Now reading oﬀ from the top-right, the longitude of λ is
λ = yxzx −3 = yx2yx−4.
(Note that we add x−3 so that the longitude λ has linking number zero with the
knot.) So its image by ρ is
ρ (λ ) =

 − m−3 m3 − m−3
m1/ 2 − m−1/ 2
0 − m3

 .
We also put g := yzx = yxy and h := xy. Then we see that g2 = h3. So we
have another presentation of π 1(S3 \ T ):
⟨g, h |g2 = h3⟩.
244 HITOSHI MURAKAMI
We also compute
ρ (g) =
(
m1/ 2 − m−1/ 2 1
1 − m − m−1 − m1/ 2 + m−1/ 2
)
and
ρ (h) =
(
1 − m−1 m−1/ 2
− m1/ 2 + m−1/ 2 − m−3/ 2 m−1
)
.
Therefore we have tr
(
ρ (g)
)
= 0 and tr
(
ρ (h)
)
= 1, and so this representation
belongs to the same component as ρ 1, 1 in Theorem 1.4 in the SL(2; C)-character
variety.
4.2. Representations of the fundamental group of the cinquefoil knot.
Our next example is the cinquefoil knot (or the double overha nd knot) C =
T (2, 5). The elements z, w and v indicated in Figure 12 are presented in terms
Figure 12. Cinquefoil knot and elements of π 1(S3 \ C)
of x and y:
z = xyx−1,
w = zxz −1 = xyxy −1x−1,
v = wzw −1 = xyxyx −1y−1x−1.
The last two crossings give the same relation
yxyxyx −1y−1x−1y−1x−1 = 1.
THE VOLUME CONJECTURE AND ITS GENERALIZATIONS 245
Therefore we have a presentation of π 1(S3 \ C).
π 1(S3 \ C) = ⟨x, y |ωx = yω ⟩
with ω = xyxy. Then the longitude λ is
λ = yxyxy −1xyxyx −7.
Let ρ be a non-abelian representation of π 1(S3 \ C) at SL(2, C). Then we may
assume that
ρ (x) =
(
m1/ 2 1
0 m−1/ 2
)
and ρ (y) =
(
m1/ 2 0
− d m −1/ 2
)
.
Similar calculations show that d and m satisfy the following equation.
(4.3) d2 − (2m + 2m−1 − 1)d + m2 − m + 1 − m−1 + m−2.
If we put ξ := tr
(
ρ (x)
)
and η : tr
(
xy
)
, then we have
ξ = m1/ 2 + m−1/ 2,
η = m + m−1 − d
and
F (ξ, η ) = Pxyxy (ξ, η ) − Pxy + 1 = η 2 − η − 1,
which coincides (4.3) and this conﬁrms Theorem 1.2.
So we have
d = m + m−1 − 1 ±
√
5
2
and
ρ (λ ) =

 − m−5 m5 − m−5
m1/ 2 − m−1/ 2
0 − m5


for both choices of d, where ρ is given as before. We put d± := m + m−1 − 1 ±
√
5
2and denote the corresponding representation by ρ ±. Note that if we put g :=
yvwzx = yxyxy and h := xy then g2 = h5, and so we have another presentation
of π 1(S3 \ C):
⟨g, h |g2 = h5⟩.
We also calculate
ρ ±(g) =


1 ±
√
5
