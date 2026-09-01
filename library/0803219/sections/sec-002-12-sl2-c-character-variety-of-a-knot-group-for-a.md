---
doc_id: 0803219
doc_title: "ACTA MATHEMATICA VIETNAMICA 219 AN INTRODUCTION TO THE VOLUME CONJECTURE AND ITS GENERALIZATIONS"
section_id: sec-002-12-sl2-c-character-variety-of-a-knot-group-for-a
section_title: "SL(2; C)-Character variety of a knot group. For a knot in S3, let us"
section_number: 1.2
pages: 4-6
source_pdf: 0803219.pdf
source_sha256: 8e37e11b8c8953c8
---
consider representations of π 1(S3 \ K) at SL(2; C), where SL(2; C) is the set of
all 2 × 2 complex matrices with determinant one. The set of all chara cters of
representations is denoted by X(S3 \ K) or X(K). We can regard X(K) as the
set of equivalence classes where we regard two representati ons equivalent if they
have the same trace. It is well known that X(K) is an algebraic variety (the
set of the zeroes of polynomials) and called the SL(2; C)-character variety of the
knot K. (See for example [6].)
Here are two families of knots whose SL(2; C)-character varieties are well
known.
THE VOLUME CONJECTURE AND ITS GENERALIZATIONS 223
Figure 4. Figure-eight knot
Example 1.1 (Two-bridge knots) . If K is a two-bridge knot (a knot that can
be put in R3 = S3 \ {∞} in such a way that it has only two maxima), we can
express its SL(2; C)-character variety as follows [37, 3.3.1 Theorem] (see als o [53,
Theorem 1]).
It is well known that π 1(S3 \ K) has the following presentation:
⟨x, y |ωx = yω ⟩,
where ω is a word in x and y of the form x±1y±1 . . . x ±1y±1. Let ρ be a rep-
resentation of π 1(S3 \ K) at SL(2; C). Then for any word z in x and y we can
express tr
(
ρ (z)
)
as a polynomial in ξ := tr
(
ρ (x)
)
and η := tr
(
ρ (xy)
)
by using the
following formulas [58]:
tr(AB) = tr( A) tr(B) − tr(A−1B),
tr(A−1) = tr( A).
(1.1)
We denote this polynomial by Pz(ξ, η ).
The SL(2; C)-character variety X(K) is given as follows.
Theorem 1.2 (Le [37]) . The SL(2; C)-character variety is determined by the
polynomial
(2 + η − ξ 2)F (ξ, η ),
where
F (ξ, η ) :=
k∑
i=0
(− 1)iPω (i)(ξ, η )
with ω (i) the word obtained from ω by deleting the ﬁrst i letters and the last i
letters (we put P∅(ξ, η ) := 1) . Moreover the ﬁrst factor 2 + η − ξ 2 determines the
abelian part and the second factor F (ξ, η ) determines the non-abelian part.
224 HITOSHI MURAKAMI
Example 1.3 (Torus knots). A knot that can be put on the standard torus is
called a torus knot. Such knots are parametrized by two copri me integers, and
up to mirror image we may assume that they are both positive. W e also assume
that they are bigger than 1.
For the torus knot T (a, b ) of type ( a, b ) with positive coprime integers a and b
with a > 1 and b > 1, the fundamental group π 1(T (a, b )) also has a presentation
with two generators and one relation:
⟨g, h |ga = hb⟩.
Note that the meridian (a loop that goes around the knot in the positive direction)
µ and the longitude (a loop that is parallel to the knot and is nu ll-homologous
in the knot complement) λ can be expressed as µ = g−chd and λ = gaµ ab, where
we choose c and d so that ad − bc = 1.
Then the SL(2; C)-character variety of π 1(T (a, b )) is given as follows.
Theorem 1.4 ([9, Theorem 2]) . The components of the non-abelian part of the
SL(2; C)-character variety are indexed by k and l with 1 ⩽ k ⩽ a− 1, 1 ⩽ l ⩽ b− 1
and k ≡ l (mod 2) . Moreover a representation ρ k,l in the component indexed by
(k, l ) satisﬁes
tr (ρ k,l (g)) = 2 cos
(kπ
a
)
and
tr (ρ k,l (h)) = 2 cos
(lπ
b
)
.
(See also [34, Theorem 1]).
