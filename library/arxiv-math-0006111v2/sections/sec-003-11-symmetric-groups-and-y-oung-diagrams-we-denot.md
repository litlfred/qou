---
doc_id: arxiv-math-0006111v2
doc_title: "Approximate factorization and concentration for characters of symmetric groups"
section_id: sec-003-11-symmetric-groups-and-y-oung-diagrams-we-denot
section_title: "Symmetric groups and Y oung diagrams. We denote by Sq the symmet-"
section_number: 1.1
pages: 2-3
source_pdf: 0006111v2.pdf
source_sha256: cd99f45d686eb6e2
doc_brief: "Approximate factorization and concentration for characters of symmetric groups — We prove a factorization-concentration result for characters of s ymmet- ric groups."
---
ric group on {1,...,q }, by ( ij) the transposition exchanging i and j, and more
generally by ( i1i2...i n) cyclic permutations of order n. For σ ∈ Sq, let c(σ ) be
its number of cycles, and s(σ ) be the number of elements not ﬁxed by σ . Then
|σ | := q −c(σ ) is the smallest number n such that σ can be written as a product
of n transpositions. We denote by Yq the set of Young diagrams with q boxes,
and Y = ∪∞
q=1Yq. If λ ∈ Yq let [λ] be the associated irreducible representation
of Sq, and χλ be its normalized character, i.e. χλ (e) = 1. Recall from [B], [K]
that a Young diagram can be identiﬁed with a piecewise linear function with slopes
±1, and local minima and maxima occuring at two interlacing se quences of integer
points
x1<y 1<x 2 <...<y n−1 <x n
as in the following example
x1 y1 x2 y2 x3 y3 x4
and that we can embed the set of Young diagrams in the space CY of continuous
Young diagrams, i.e. functions ω : R → R satisfying
(1) |ω (u1) −ω (u2)| ≤ |u1 −u2| for all u1,u 2 ∈ R
(2) ω (u) = |u| for suﬃciently large |u|.
To each continuous diagram ω ∈ CY one can associate a probability measure mω
with compact support on R, determined by the equation
(1.1) 1
z exp
∫
R
1
x −zσ ′(x)dx =
∫
R
1
z −x mω (dx) z ∈ C \ R
where σ (u) = ( ω (u) − |u|)/ 2;u ∈ R. This measure is called the transition mea-
sure of the diagram and its moments are called the moments of t he corresponding
APPROXIMATE F ACTORIZATION AND CONCENTRATION 3
continuous diagram. We shall denote them by
mn(ω ) =
∫
R
xn mω (dx)
The measure corresponding to a diagram in CY has bounded support, it is centered
(i.e. m1 = 0), and its second moment is equal to half the area of the set
{(u,v ) ∈ R2| |u| ≤ v ≤ω (u)}
Besides moments of measures we shall also consider their fre e cumulants. Recall
([B], [VDN]), that the free cumulants are deﬁned as the coeﬃc ients Rn in the
expansion
K(z) = 1
z +
∞∑
n=1
Rnzn−1
where K(z) is the functional inverse of the Cauchy transform
G(z) =
∫
R
1
z −x mω (dx)
