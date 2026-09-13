---
doc_id: arxiv-math-0108215v1
doc_title: "Möbius Energy of Thick Knots Eric J. Rawdon 2"
section_id: sec-014-3-33-13-then-our-proof-stops-here-the-quadratic
section_title: "(33 − 13), then our proof stops here. The quadratic bound (4) is valid and"
section_number: 3
pages: 10-11
source_pdf: 0108215v1.pdf
source_sha256: 191784d2ccb3415a
---
certainly (4) < (3), so (3) is valid as well. We continue under the assumption
that EL(K) ≥ 104
3 + 2π.
10
The ﬁrst observation is that for any ρ > 0, if |x − y| ≥ ρ, then the integrand
1
|x−y|2 ≤ 1
ρ2 . In obtaining the quadratic bound, we stopped here, allowing the
idea that with respect to each point x ∈ K, the whole knot (except for the arc
around x of length π in each direction) lies just at distance 2 from x. But the
knot is thick : a piece w of K of length ℓ(w) carries along with it a solid tube
W of volume πℓ(w) (we still are assuming R(K) = 1). Furthermore, such a
tube W cannot intersect any other part of K nor any of the rest of the tube
around K. This restricts how much length of K can be packed within any
given distance from x.
Fix x on K. Let Ydist denote the set on which we integrate to compute I x
dist,
that is Ydist = {y ∈ K : arc( x, y) ≥ π}. The arclength of Ydist is just L − 2π.
Let S(ρ, σ] denote the half-open spherical shell centered at x with radius from
ρ to σ. Let Y (ρ, σ] = Ydist ∩ S(ρ, σ], a measurable set, and let ℓ(ρ, σ] denote
its 1-dimensional measure, i.e. the measure of the length of K lying in S(ρ, σ].
Let T (ρ, σ] be the solid tube with axis Y (ρ, σ], that is, the portion of the unit
radius tube about K consisting of disks centered at points y ∈ Y (ρ, σ]. The 3-
dimensional measure, i.e. volume, of T (ρ, σ] is πℓ(ρ, σ]. Deﬁne S[ρ, σ], Y [ρ, σ],
ℓ[ρ, σ], and T [ρ, σ] analogously. Note that Ydist ⊂ S[2, L/2]. The subset of Ydist
lying at distance exactly 2 from x plays a special role in the analysis, so we
also deﬁne S[2], Y [2], ℓ[2], and T [2].
Let P = ( 3
4L − 3π
2 + 1)1/ 3 − 1. The constant P is the radius required so that
a spherical shell from r = 1 to r = P + 1 has the same volume as a tube of
radius 1 about a set of length L − 2π.
We bound the total amount of length that can lie in each spherical sh ell by a
function ℓ∗ (see (9) below). Let ℓ∗[2] = 4
3(33 − 13) = 104
3 . For 2 ≤ a < b , let
ℓ∗(a, b] = 4
3
(
(min{b, P } + 1)3 − (min{a, P } + 1)3
)
.
In particular, when 2 ≤ a < b ≤ P , this simpliﬁes to
ℓ∗(a, b] = 4
3
(
(b + 1)3 − (a + 1)3
)
.
Let
ℓ∗[2, b] = ℓ∗[2] + ℓ∗(2, b].
For b ≤ P , ℓ∗[2, b] = 4
