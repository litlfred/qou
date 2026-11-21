---
doc_id: arxiv-hep-th-9506138v1
doc_title: "Black Hole Complementarity vs. Locality"
section_id: sec-011-b1-a-four-point-amplitude-involving-commutators
section_title: "A Four Point Amplitude Involving Commutators"
section_number: B.1
pages: 22-25
source_pdf: 9506138v1.pdf
source_sha256: bb85afba0530402c
toc_source: inferred
doc_brief: "Black Hole Complementarity vs. Locality — 18 sections: Front matter; Introduction; The Nice-Slice Argument"
---
In this Appendix we present the calculation of the matrix element
C(4; 3; 2; 1) = ⟨0|[ΦH(4), ΦH(3)][ΦH(2), ΦH(1)]|0⟩.
(B.1)
As before, we will use perturbation theory to calculate C to leading nontrivial order in g.
Inserting a complete set of states {|γ⟩}, equation (B.1) can be written
C(4; 3; 2; 1) =
X
γ
M(4, 3; γ)M(1, 2; γ)∗,
(B.2)
where M is given by equation (A.6). The ﬁrst term which does not vanish identically when
the centers of mass of the string ﬁelds are spacelike related is the second order term
C(2)(4; 3; 2; 1) =
X
γ
M (1)(4, 3; γ)M (1)(1, 2; γ)∗.
(B.3)
>
σ
0
1
σ
>
1
2
3
4
Fig. 3: String diagram for four-point amplitude.
It was stated in Appendix A that M (1)(1, 2; γ) vanishes unless |γ⟩is a single string state.
Thus we can perform the sum, using the earlier results (A.9) and (A.11). This leads to a
sum of nine terms. Any one of these terms can be isolated by integrating the expression
against appropriate functions of the longitudinal momenta, so they cannot cancel one
another. We shall present the calculation for only one of those terms, the term in which
αr > 0 for all r:
C(2)(4; 3; 2; 1) =
g2
Z x+
3
x+
4
dx′+
Z x+
2
x+
1
dx′′+ ⟨0|Φa(4)Φa(3)V1acc(x′+)V1aac(x′′+)Φc(1)Φc(2)|0⟩.
(B.4)
Transforming to a momentum and occupation number representation (the measure being
as in the ﬁrst line of (A.12)), the matrix element is is
˜C(2)(4; 3; 2; 1)
= g2
Z x+
3
x+
4
dx′+
Z x+
2
x+
1
dx′′+ ⟨0|A(4)A(3)V1acc(x′+)V1aac(x′′+)A†(1)A†(2)|0⟩.
(B.5)
The time and operator orderings in the matrix element (B.5) diﬀer, but we may cal-
culate ﬁrst the Euclidean time ordered matrix element and obtain the needed Minkowski
result by analytic continuation. The ﬁelds will be at Euclidean times σ0
r and the interac-
tions at σ′0, σ′′0, with σ0
3,4 > σ′0 > σ′′0 > σ0
1,2. The matrix element in equation (B.5) is
then given by
 4
Y
s=1
2α+
s
!1/2
2πδ(α1 + α2 −α3 −α4)P(1, 2, 3, 4; σ′0, σ′′0),
(B.6)
where P is the functional integral on the string world sheet shown in ﬁg. 3, (the other
cyclic ordering, 1243, does not contribute to the Regge behavior of interest).
It is convenient to take the external times |σ0
r| to be large. The inverse of the mapping
ρ(z) = σ0 + iσ1 = α1 log(z) + α2 log(z −x) −α3 log(1 −z) + ¯ρ
(B.7)
then takes the string world-sheet Σ to the upper half z-plane minus four small semicircles
surrounding the points 0, x, 1, and ∞. The parameters x and ¯ρ in the mapping are deter-
mined implicitly in terms of the interaction times σ′0, σ′′0 by the condition that ∂zρ = 0
at the interaction points,
0 = α1
z +
α2
z −x +
α3
1 −z .
(B.8)
Solving this (quadratic) equation for z′, z′′, the equations ρ(z′) = σ′0 + iπα3, ρ(z′′) =
σ′′0 + iπα2 give two relations between σ′0, σ′′0 and x, ¯ρ. Note that the diﬀerence of these
relates x to δ = σ′0 −σ′′0. Strings 1, 2, 3, 4 are mapped to the semicircles, with respective
radii
r1 = x−α2/α1e(σ0
1−¯ρ)/α1
r2 = x−α1/α2(1 −x)α3/α2e(σ0
2−¯ρ)/α2
r3 = (1 −x)α2/α3e(¯ρ−σ0
3)/α3
r4 = e(¯ρ−σ0
4)/α4 ,
(B.9)
r4 being the radius in the inverse coordinate z−1.
Then
P(1, 2, 3, 4; σ′0, σ′′0) = J(αs, σ0
s, σ′0, σ′′0) P′(1, 2, 3, 4; σ′0, σ′′0)
= J(αs, σ0
s, σ′0, σ′′0)
* 4
Y
s=1
rhs
s Vs
+
.
(B.10)
Here P′ is the path integral on the upper half-plane minus semicircles and J is the deter-
minant from the conformal mapping. In the second line the small semicircles have been
replaced by the corresponding vertex operators. The semicircles correspond to vertex op-
erators renormalized at scale rs; the factor rhs
s
with hs the weight of Vs relates these to
normal ordered vertex operators. It can be thought of as arising from the radial evolution
from radius r to a standard radius 1. To simplify the analysis, we will consider the case of
four tachyon component ﬁelds, for which equation (B.10) is
P(1, 2, 3, 4; σ′0, σ′′0) = J(αs, σ0
s, σ′0, σ′′0) (2π)D−2δD−2(⃗p1 +⃗p2 −⃗p3 −⃗p4)
× x⃗p1·⃗p2(1 −x)−⃗p2·⃗p3
4
Y
s=1
r⃗p 2
s /2
s
.
(B.11)
The determinant J can now be determined by comparison with the on-shell four-point
function, using the fact that J is independent of the transverse momenta,
J(αs, σ0
s, σ′0,σ′′0) =
 4
Y
s=1
2α+
s
!−1/2
dx
dδ
×xα1/α2+α2/α1(1 −x)−α3/α2−α2/α3 exp
( 4
X
s=1
(−σ0
s + ¯ρ)θs/αs
)
,
(B.12)
with θs = +1 for s = 1, 2 and θs = −1 for s = 3, 4. The ﬁrst factor cancels the noncovariant
factor in the matrix element (B.6).
The result for the matrix element (B.5) is
˜C(2)(4; 3; 2; 1) = g2(2π)D−1δ(α1 + α2 −α3 −α4)δD−2(⃗p1 +⃗p2 −⃗p3 −⃗p4)
×
Z x+
3
x+
4
dx′+
Z x+
2
x+
1
dx′′+ dx
dδ xp1·p2 (1 −x)−p2·p3 exp
( 4
X
s=1
(ix+
s −¯ρ)p−
s θs
)
.
(B.13)
The straightforward continuation σ0
s →ix+
s
has been carried out.
The continuation
σ′0, σ′′0 →ix′+, ix′′+ is also implicit; this makes x and ¯ρ complex.
The matrix ele-
ment (B.13) cannot be evaluated in closed form. Solving the conformal mapping to express
all quantities in terms of x and σ′0, the integral over σ′0 can be carried out but the result
is a rather complicated integral over x, with endpoints that are determined only implicitly.
However, the important behavior will be determined simply from scaling.
