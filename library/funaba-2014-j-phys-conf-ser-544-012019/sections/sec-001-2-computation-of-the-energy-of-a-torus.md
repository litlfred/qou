---
doc_id: funaba-2014-j-phys-conf-ser-544-012019
doc_title: "Conference Series"
section_id: sec-001-2-computation-of-the-energy-of-a-torus
section_title: "Computation of the energy of a torus"
section_number: 2
pages: 4-5
source_pdf: Funaba_2014_J._Phys.__Conf._Ser._544_012019.pdf
source_sha256: c95b283a122d67e4
---
Proof of Theorem: Let T be a torus of revolution parametrized by
p(u,v ) = ((R + cosu) cosv, (R + cosu) sinv, sinu).
Let x = p(α, 0) = (R + cosα, 0, sinα) be a point on T . First we ﬁx α and compute
the renormalized r−4-potential of T at x. This is the main part of the paper. Some of the
complicated computation to obtain expansion in seiries in ε has been done with the help of
Maple.
Let Dist = Dist(u,v ) be the distance between x and a point y =p(u,v ):
Dist2 =|x−y|2 =|p(u,v )−p(α, 0)|2
= ((R + cosα)− (R + cosu) cosv)2 + (R + cosu)2 sin2v + (sinα− sinu)2
= 2R2 + 2 + 2R (cosα + cosu)− 2 sinα sinu− 2 (R+ cosα) (R + cosu) cosv.
To compute the integral
∫
T\Bε(x)|x−y|−4d2y, we will divide the domain of the integration
into four parts and use several kinds of changes of variables. We may assume without loss of
generality that u∈ [α−π,α +π] and v∈ [−π,π ]. Put
θ = π
2− u−α
2 , t= 2 cosθ = 2 sinu−α
2 .
Then, as (u−α)/2∈ [−π/2,π/ 2] we have θ∈ [0,π ] and cos(u−α)/2≥ 0. Therefore,
cosu = 2−t2
2 cosα− t
√
4−t2
2 sinα, sinu = t
√
4−t2
2 cosα + 2−t2
2 sinα,
which implies that the distance can be expressed as
Dist2 =t2 +
[
4(R + cosα)2− 2(R + cosα) cosα·t2− 2(R + cosα) sinα·t
√
4−t2
]
sin2v
2
= 4
[
cos2θ + (R + cosα)
(
R + cosα− 2 cosα cos2θ− 2 sinα sinθ cosθ
)
sin2v
2
]
= 4
[
cos2θ + (R + cosα) (R− cos(α− 2θ)) sin2v
2
]
.
Flux in QCS IOP Publishing
Journal of Physics: Conference Series 544 (2014) 012019 doi:10.1088/1742-6596/544/1/012019
3
Deﬁne b =b(θ) and c =c(t) by
c(t) = 2(R+ cosα)
[
2(R + cosα)− cosα·t2− sinα·t
√
4−t2
]
b = c
4 = (R + cosα) (R− cos(α− 2θ)).
(3)
Then
Dist2 =t2 +c(t) sin2v
2 = 4
(
cos2θ +b sin2v
2
)
.
Put
V (ε,x ) =
∫∫
Dist≥ε
d2y
|x−y|2.
Since the area element of T is given by d2y = (R + cosu)dudv, V (ε,x ) is given by
∫∫
Dist≥ε
(R + cosu)
(2R2 + 2 + 2R (cosα + cosu)− 2 sinα sinu− 2 (R+ cosα) (R + cosu) cosv)2dudv
=
∫∫
Dist≥ε
R +
(
2−t2
2 cosα− t
√
4−t2
2 sinα
)
(
t2 +c(t) sin2 v
2
)2
2dt√
4−t2dv (4)
= 1
8
∫∫
Dist≥ε
(R− cos(α− 2θ))(
cos2θ +b sin2 v
2
)2dθdv. (5)
The integration by dv an be executed as
∫ dv
(A2 +B sin2 v
2)2
= 2A2 +B
A3(A2 +B)
3
2
tan−1
(√
A2 +B
A tanv
2
)
+ B tan v
2
A2(A2 +B)
(
(A2 +B) tan2 v
2 +A2).
(6)
We devide the domain of the integration T\Bε(x) into eight parts as is illustrated in Figure
