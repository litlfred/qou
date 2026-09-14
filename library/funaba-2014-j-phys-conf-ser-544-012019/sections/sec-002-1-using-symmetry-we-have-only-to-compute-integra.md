---
doc_id: funaba-2014-j-phys-conf-ser-544-012019
doc_title: "Conference Series"
section_id: sec-002-1-using-symmetry-we-have-only-to-compute-integra
section_title: "Using symmetry, we have only to compute integrals over the following four regions"
section_number: 1
pages: 5-8
source_pdf: Funaba_2014_J._Phys.__Conf._Ser._544_012019.pdf
source_sha256: c95b283a122d67e4
doc_brief: "Conference Series — 11 sections: Front matter; Introduction and main result; Computation of the energy of a tor"
---
{
p(u,v )| 2 sin−1(ε/2)≤u−α≤π, 0≤v≤π
}
,
{
p(u,v )| 0≤u−α≤ sin−1(ε/2), 0≤v≤π,|p(u,v )−x|≥ ε
}
,
{
p(u,v )|−π≤u−α≤− 2 sin−1(ε/2), 0≤v≤π
}
,
{
p(u,v )|− 2 sin−1(ε/2)≤u−α≤ 0, 0≤v≤π,|p(u,v )−x|≥ ε
}
,
which we denote by I1,I 2,I 3, and I4 respectively. We remark that the regions given by the ﬁrst
and the third lines do not have intersection with Bε(x).
Let us ﬁrst compute I2 and I4 using variables (t,v ). Since 0 ≤ u−α≤ 2 sin−1(ε/2) we
have
0≤t = 2 sin((u−α)/2)≤ε,
and the condition|p(u,v )−x|≥ ε implies
sin2v
2 = Dist2−t2
c(t) ≥ ε2−t2
c(t) , i.e., v≥ 2 sin−1
(√
ε2−t2
c(t)
)
.
Flux in QCS IOP Publishing
Journal of Physics: Conference Series 544 (2014) 012019 doi:10.1088/1742-6596/544/1/012019
4
v
u
I1 3I
x
4I
2I
Figure 1. Parts of the domains of integration of I1 (blue or light grey) and I4 (red or dark
grey) near the point x
Therefore, I2 is given by
I2 =
∫ ε
0
∫ π
2 sin−1
(√
ε2−t2
c(t)
) 2R + cosα· (2−t2)− sinα·t
√
4−t2
(t2 +c(t) sin2 v
2)2 dv dt√
4−t2.
By the formula (6) we get
I2 =
∫ ε
0
{
2R + cosα· (2−t2)− sinα·t
√
4−t2
√
4−t2
×
[
2t2 +c(t)
t3(t2 +c(t))
3
2
tan−1
(√
t2 +c(t)
t tanv
2
)
+ c(t) tanv
2
t2(t2 +c(t))
(
(t2 +c(t)) tan2 v
2 +t2)
]π
v=2 sin−1
(√
ε2−t2
c(t)
)



dt
=
∫ ε
0
2R + cosα· (2−t2)− sinα·t
√
4−t2
√
4−t2
×
{
2t2 +c(t)
t3(t2 +c(t))
3
2
(
π
2− tan−1
(√
ε2−t2
t
√
c(t) +t2
c(t) +t2−ε2
))
−
√
ε2−t2√
c(t) +t2−ε2
ε2t2(t2 +c(t))
}
dt
Putting τ = sin−1(t/ε), i.e., t =ε sinτ, we have
I2 =
∫ π
2
0
2R + cosα· (2−ε2 sin2τ)−ε sinα sinτ
√
4−ε2 sin2τ√
4−ε2 sin2τ
×
{
cosτ
(
2ε2 sin2τ +c(ε sinτ)
)
ε2 sin3τ(ε2 sin2τ +c(ε sinτ))
3
2
(
π
2− tan−1
(
cotτ
√
c(ε sinτ) +ε2 sin2τ
c(ε sinτ) +ε2 sin2τ−ε2
))
−cot2τ
√
c(ε sinτ) +ε2 sin2τ−ε2
ε2(ε2 sin2τ +c(ε sinτ))
}
dτ.
Flux in QCS IOP Publishing
Journal of Physics: Conference Series 544 (2014) 012019 doi:10.1088/1742-6596/544/1/012019
5
Expanding the integrand in a series in ε with the help of Maple we obtain
I2 = 1
2ε2
∫ π
2
0
(
τ cosτ
sin3τ− cos2τ
sin2τ
)
dτ− sinα
4(R + cosα)ε
∫ π
2
0
(
τ cosτ
sin2τ− cos2τ
sinτ
)
dτ
+ R2
16(R + cosα)2
∫ π
2
0
(
τ cosτ
sinτ − cos2τ
)
dτ + 1
8(R + cosα)2
∫ π
2
0
cos2τdτ +O(ε).
(7)
Direct integration shows
∫ π
2
0
(
τ cosτ
sin3τ− cos2τ
sin2τ
)
dτ = 1
2
[τ + sinτ cosτ− 2τ cos2τ
sin2τ
]π
2
0
= π
4,
∫ π
2
0
(
τ cosτ
sin2τ− cos2τ
sinτ
)
dτ =
[
− cosτ− τ
sinτ
]π
2
0
= 4−π
2 .
(8)
On the other hand,
∫ π
2
0
(
τ cotτ− cos2τ
)
dτ can be computed as follows.
Put
I =
∫ π
2
0
log(sinτ)dτ.
Then
I =
∫ π
2
0
log
(
sin
(π
2−τ′
))
dτ′ =
∫ π
2
0
log(cosτ)dτ.
Adding the two above, we get
2I =
∫ π
2
0
log(sinτ cosτ)dτ
=
∫ π
2
0
log(sin 2τ)dτ− π
2 log 2
= 1
2
∫ π
0
log(sinτ′)dτ′− π
2 log 2
= 1
2
(∫ π
2
0
log(sinτ)dτ +
∫ π
π
2
log(sinτ)dτ
)
− π
2 log 2
=I− π
2 log 2,
which implies
I =
∫ π
2
0
log(sinτ)dτ =−π
2 log 2.
Now we have
∫ π
2
0
(
τ cosτ
sinτ − cos2τ
)
dτ =
[
τ log(sinτ)
]π
2
0
−
∫ π
2
0
log(sinτ)dτ− π
4
=π
4 (2 log 2− 1).
(9)
Substituting (8) and (9) to (7) we obtain
I2 = π
8ε2 + (π− 4) sinα
8(R + cosα)ε + πR2
64(R + cosα)2 (2 log 2− 1) + π
32(R + cosα)2 +O(ε).
Flux in QCS IOP Publishing
Journal of Physics: Conference Series 544 (2014) 012019 doi:10.1088/1742-6596/544/1/012019
6
The integral I4 can be obtained from I2 by changing α to−α:
I4 =
∫ 0
−ε
∫ π
2 sin−1
(√
ε2−t2
c(t)
) 2R + cosα· (2−t2)− sinα·t
√
4−t2
(t2 +c(t) sin2 v
2)2
dt√
4−t2dv
= π
8ε2− (π− 4) sinα
8(R + cosα)ε + πR2
64(R + cosα)2 (2 log 2− 1) + π
32(R + cosα)2 +O(ε).
Let us next compute I1 and I3. Since u−α∈ [2 sin−1(ε/2),π ] θ = π/2− (u−α)/2∈
[0, cos−1(ε/2)]. The integral I1 is given by
I1 = 1
8
∫ cos−1 ε
2
0
∫ π
0
R− cos(α− 2θ)
(cos2θ +b sin2 v
2)2dvdθ,
where b = (R + cosα) (R− cos(α− 2θ)) as was given by (3). Put a = cosθ. Then (6) shows
∫ π
0
dv
(a2 +b sin2 v
2)2 = 2a2 +b
a3(a2 +b)
3
2
· π
2 .
Since
R− cos(α− 2θ) =R + cosα− 2 cosα cos2θ− 2 sinα sinθ cosθ,
we have
I1 = π
16
∫ cos−1 ε
2
0
(R− cos(α− 2θ)) 2a2 +b
a3(a2 +b)
3
2
dθ
= π
16
∫ cos−1 ε
2
0
[
(R + cosα)− 2 cosα cos2θ− 2 sinα sinθ cosθ
] (a2 +b) +a2
a3(a2 +b)
3
2
dθ
=π(R + cosα)
