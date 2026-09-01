---
doc_id: 0803219
doc_title: "ACTA MATHEMATICA VIETNAMICA 219 AN INTRODUCTION TO THE VOLUME CONJECTURE AND ITS GENERALIZATIONS"
section_id: sec-011-31-representations-of-the-fundamental-group-here
section_title: "Representations of the fundamental group. Here we follow R. Riley"
section_number: 3.1
pages: 13-15
source_pdf: 0803219.pdf
source_sha256: 8e37e11b8c8953c8
---
[53] to describe non-abelian representations of π 1(S3 \ E) at SL(2; C), where E
is the ﬁgure-eight knot. Let x and y be the generators of π 1(S3 \ E) indicated
in Figure 5, where the basepoint of the fundamental group is a bove the paper.
Then the other elements z and w indicated in Figure 6 can be expressed by x
Figure 5. The two generators of π 1(S3 \ E)
and y as follows.
Figure 6. The other elements of π 1(S3 \ E)
232 HITOSHI MURAKAMI
z = xyx−1(3.1)
(from the top-most crossing) ,
w = z−1xz
(from the second top crossing) .
Therefore we have
(3.2) w =
(
xy−1x−1)
x
(
xyx−1)
= xy−1xyx−1
Now from the bottom-left and the bottom-right crossings we h ave the following
relations.
yw−1y−1z = 1,
yw−1x−1w = 1.
Using (3.1) and (3.2), these relations become a single relat ion
(3.3) yxy −1x−1yx−1y−1xyx−1 = 1.
Therefore π 1(S3 \ E) has the two generators x and y with the single relation (3.3),
that is:
(3.4) π 1(S3 \ E) = ⟨x, y |ωx = yω ⟩
with ω := xy−1x−1y.
Let ρ be a non-abelian representation of π 1(S3 \ E) at SL(2; C). From [53] we
can assume up to conjugate that the images of ρ (x) and ρ (y) are given as follows.
ρ (x) :=
(
m1/ 2 1
0 m−1/ 2
)
,
ρ (y) :=
(
m1/ 2 0
− d m −1/ 2
)
.
(3.5)
Then from the presentation (3.4), we have ρ (ωx ) = ρ (yω ). Since ρ (ω ) is equal to
(
(d + 1)2 − dm − m−1/ 2(d − m + 1)
dm−1/ 2(d − m + 1) m−1(m − d)
)
,
we have
ρ (ωx ) =
(
m1/ 2((d + 1)2 − dm) − m−1(dm2 − (d2 + 2d + 2)m + d + 1)
− d(m − d − 1) m−3/ 2(− dm2 + (d2 + d + 1)m − d)
)
,
and
ρ (yω )
=
(
m1/ 2((d + 1)2 − dm) m − d − 1
dm−1(dm2 − (d2 + 2d + 2)m + d + 1) m−3/ 2(− dm2 + (d2 + d + 1)m − d)
)
.
So d and m satisfy the equation
(3.6) d2 + d(3 − m − m−1) + 3 − m − m−1 = 0,
THE VOLUME CONJECTURE AND ITS GENERALIZATIONS 233
and d becomes a function of m:
(3.7) d = 1
2
(
m + m−1 − 3 ±
√
(m + m−1 + 1)(m + m−1 − 3)
)
.
Therefore if we put ξ := tr
(
ρ (x)
)
and η := tr
(
ρ (xy)
)
as in Subsection 1.2, we
have
ξ = m1/ 2 + m−1/ 2
η = tr
(
m − d m −1/ 2
− dm−1/ 2 m−1
)
= m + m−1 − d.
Moreover since from (1.1) we calculate
tr
(
ω
)
= η 2 − ξ 2η + 2ξ 2 − 2
tr
(
ω (1))
= η
we have
F (ξ, η ) = η 2 − η + 2ξ 2 − ξ 2η − 1,
which also gives (3.6) (See Theorem 1.2.).
Now the longitude λ is (read oﬀ from the top right)
λ = wx−1yz −1 = xy−1xyx−1x−1yxy −1x−1 = xy−1xyx−2yxy −1x−1.
From a direct calculation, we have
ρ (λ ) =
(
𝓁(m)±1 (m1/ 2 + m−1/ 2)
√
(m + m−1 + 1)(m + m−1 − 3)
0 𝓁(m)∓1
)
,
where
𝓁(m)
:=
(
m2 − m − 2 − m−1 + m−2)
2 + (m − m−1)
2
√
(m + m−1 + 1)(m + m−1 − 3).
Note that 𝓁(m) is a solution to the following equation.
(3.8) 𝓁 + (m2 − m − 2 − m−1 + m−2) + 𝓁 −1 = 0,
which coincides with the A-polynomial of the ﬁgure-eight knot [6], replacing 𝓁
and m with l and m2, respectively.
Let ρ m± denote the representation (3.5) with d deﬁned by (3.7).
