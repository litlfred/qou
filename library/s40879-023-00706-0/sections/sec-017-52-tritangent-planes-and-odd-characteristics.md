---
doc_id: s40879-023-00706-0
doc_title: "RESEARCH ARTICLE"
section_id: sec-017-52-tritangent-planes-and-odd-characteristics
section_title: "Tritangent planes and odd characteristics"
section_number: 5.2
pages: 39-40
source_pdf: s40879-023-00706-0.pdf
source_sha256: 4c5af312d2e5d6a7
doc_brief: "European Journal of Mathematics (2024) 10:3 RESEARCH ARTICLE — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
---
Recall that when we consider the canonical embedding of a curve in Pg−1, the inter-
section with a hyperplane gives an effective element of the canonical divisor class of
the curve, as it corresponds to the zero-locus of a differential on the curve. A tritangent
plane is a plane that intersects the curve tangentially in three points. If a hyperplane
is tangent at each intersection (i.e. the intersection is of order 2) then this naturally
constructs an effective theta divisor on the curve, and moreover every such theta char-
acteristic θ gives a hyperplane [13]. For any sextic that is the intersection of a smooth
quadric and smooth quartic in P
3, for example Bring’s curve, the 120 tritangent planes
a r ei n1− 1 correspondence with the 120 odd theta characteristics [ 32, Theorem 2.2].
On Bring’s curve we have the following result about these planes.
Proposition 5.6 ([25]) The 120 tritangent planes on Bring’s curve split into two
classes, 60 in each class;
(i) those where all three contact points are Weierstrass points, and
(ii) those where only one contact points is a Weierstrass point.
Planes in the ﬁrst and second class respectively have equations (recalling notation
from Sect. 3.1)
/Pi1(1)
α jk
..=
{ x j
β − xk
γ = 0
}
,
123
3 Page 40 of 46 H.W. Braden, L. Disney-Hogg
/Pi1(2)
ijk
..=
{
(α − 1)(α + 4) xi + (β − 1)(β + 4) x j + (γ − 1)(γ + 4) xk = 0
}
,
where [xi]∈ P4 and i, j, k distinct.
To clarify the notation we have used for the planes, recall that the position of the
indices on Weierstrass points Wijk indicates which root was equal to xi .T h es a m e
principle holds for /Pi1(1)
α jk ,/Pi1(1)
iβk, and /Pi1(1)
ij γ .
Corollary 5.7 The orbit decomposition of odd theta characteristics on Bring’s curve
is
120 = 20 + 20 + 20 + 60. (20)
Proof The characteristics coming from the tritangent planes are
T(1)
α jk =
5∑
i=1
i⁄= j,k
Wijk ,
T(2)
ijk = Wijk + O+
ijk + O−
ijk .
Here we deﬁne the points O±
ijk by, for example,
O±
345 =
[ 1 ± i
√
15
2 : 1 ∓ i
√
15
2 : α2 + α + 1,β 2 + β + 1,γ 2 + γ + 1
]
.
A simple orbit-stabiliser argument then gives the orbit decomposition as, for example,
T(1)
α45 is stabilised by the symmetric group S{1,2,3} and T(2)
345 is stabilised by S{1,2}.
Remark 5.8 While we were able to proceed analytically here characterising the orbits
of the odd characteristics using the work of earlier authors who had identiﬁed the
tritangent planes of the curve we also may obtain the orbit structure numerically using
Sage. Given a homology representation of the automorphism group, the algorithm to
compute the orbits is exact, but the current implementation in Sage requires ﬂoating
point arithmetic to calculate this representation.
