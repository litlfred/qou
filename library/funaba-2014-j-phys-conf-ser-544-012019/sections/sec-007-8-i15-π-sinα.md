---
doc_id: funaba-2014-j-phys-conf-ser-544-012019
doc_title: "Conference Series"
section_id: sec-007-8-i15-π-sinα
section_title: "I15− π sinα"
section_number: 8
pages: 8-12
source_pdf: Funaba_2014_J._Phys.__Conf._Ser._544_012019.pdf
source_sha256: c95b283a122d67e4
doc_brief: "Conference Series — 11 sections: Front matter; Introduction and main result; Computation of the energy of a tor"
---
8 I16,
where
I11 =
∫ cos−1 ε
2
0
dθ
a3√
a2 +b
, I 12 =
∫ cos−1 ε
2
0
cos2θdθ
a3√
a2 +b
, I 13 =
∫ cos−1 ε
2
0
sinθ cosθdθ
a3√
a2 +b
,
I14 =
∫ cos−1 ε
2
0
dθ
a(a2 +b)
3
2
, I 15 =
∫ cos−1 ε
2
0
cos2θdθ
a(a2 +b)
3
2
, I 16 =
∫ cos−1 ε
2
0
sinθ cosθdθ
a(a2 +b)
3
2
.
These integrals can be computed using
a2 +b = cos2θ
(
R2 + ((R + cosα) tanθ− sinα)2)
, tan
(
cos−1
(ε
2
))
=
√
4−ε2
ε .
Flux in QCS IOP Publishing
Journal of Physics: Conference Series 544 (2014) 012019 doi:10.1088/1742-6596/544/1/012019
7
We have used Maple to expand them in series in ε (the last step of each computation of I1j).
I15 =
∫ cos−1 ε
2
0
1
cos2θ
(
R2 + ((R + cosα) tanθ− sinα)2
) 3
2
dθ
=

 (R + cosα) tanθ− sinα
R2(R + cosα)
√
R2 + ((R + cosα) tanθ− sinα)2


cos−1 ε
2
0
= (R + cosα)
√
4−ε2− (sinα)ε
R2(R + cosα)
√
R2ε2 + ((R + cosα)
√
4−ε2− (sinα)ε)2
+ sinα
R2(R + cosα)
√
R2 + sin2α
= 1
R2(R + cosα) + sinα
R2(R + cosα)
√
R2 + sin2α
+O (ε),
I16 =
∫ cos−1 ε
2
0
sinθ
cos3θ
(
R2 + ((R + cosα) tanθ− sinα)2
) 3
2
dθ
=

 sinα ((R + cosα) tanθ− sinα)−R2
R2(R + cosα)2
√
R2 + ((R + cosα) tanθ− sinα)2


cos−1 ε
2
0
=
sinα
(
(R + cosα)
√
4−ε2− (sinα)ε
)
−R2ε
R2(R + cosα)2
√
R2ε2 +
(
(R + cosα)
√
4−ε2− (sinα)ε
)2
+
√
R2 + sin2α
R2(R + cosα)2
= sinα
R2(R + cosα)2 +
√
R2 + sin2α
R2(R + cosα)2 +O (ε),
I12 =
∫ cos−1 ε
2
0
1
cos2θ
√
R2 + ((R + cosα) tanθ− sinα)2
dθ
=
[ 1
R + cosα sinh−1
((R + cosα) tanθ− sinα
R
)]cos−1 ε
2
0
= 1
R + cosα
{
sinh−1
(
(R + cosα)
√
4−ε2− (sinα)ε
Rε
)
+ sinh−1
(sinα
R
)}
=− 1
2(R + cosα) log
( R2ε2
16(R + cosα)2
)
+ 1
R + cosα sinh−1
(sinα
R
)
+O(ε),
Flux in QCS IOP Publishing
Journal of Physics: Conference Series 544 (2014) 012019 doi:10.1088/1742-6596/544/1/012019
8
I13 =
∫ cos−1 ε
2
0
sinθ
cos3θ
√
R2 + ((R + cosα) tanθ− sinα)2
dθ
= sinα
R + cosαI12 + 1
(R + cosα)2
[√
R2 + ((R + cosα) tanθ− sinα)2
]cos−1 ε
2
0
= sinα
R + cosαI12 +
√
R2ε2 +
(
(R + cosα)
√
4−ε2− (sinα)ε
)2
(R + cosα)2ε −
√
R2 + sin2α
(R + cosα)2
= sinα
R + cosαI12 +
{ 2
(R + cosα)ε− sinα
(R + cosα)2 +O (ε)
}
−
√
R2 + sin2α
(R + cosα)2 ,
I14 =
∫ cos−1 ε
2
0
1
cos4θ
(
R2 + ((R + cosα) tanθ− sinα)2
) 3
2
dθ
= 1
(R + cosα)2I12− (1− 2R cosα− 2 cos2α)
(R + cosα)2 I15 + 2 sinα
R + cosαI16
= 1
(R + cosα)2I12 + 1 + 2Rcosα
R2(R + cosα)3 + (1 + 2R2) sinα + 2R2 sinα cosα
R2(R + cosα)3
√
R2 + sin2α
+O(ε),
and
I11 =
∫ cos−1 ε
2
0
1
cos4θ
√
R2 + ((R + cosα) tanθ− sinα)2
dθ
=R2− 1 + 4Rcosα + 3 cos2α
2(R + cosα)2 I12 + 3 sinα
2(R + cosα)I13
+

sinθ
√
R2 + ((R + cosα) tanθ− sinα)2
2(R + cosα)2 cosθ


cos−1 ε
2
0
=R2− 1 + 4Rcosα + 3 cos2α
2(R + cosα)2 I12 + 3 sinα
2(R + cosα)I13
+
√
4−ε2
√
R2ε2 +
(
(R + cosα)
√
4−ε2− (sinα)ε
)2
2(R + cosα)2ε2
=R2− 1 + 4Rcosα + 3 cos2α
2(R + cosα)2 I12 + 3 sinα
2(R + cosα)I13
+
{ 2
(R + cosα)ε2− sinα
(R + cosα)2ε− R2 + 4Rcosα + 2 cos2α
4(R + cosα)3 +O (ε)
}
.
Flux in QCS IOP Publishing
Journal of Physics: Conference Series 544 (2014) 012019 doi:10.1088/1742-6596/544/1/012019
9
Therefore
I1 =π(R + cosα)
16 I11− π cosα
8 I12− π sinα
8 I13 + π(R + cosα)
16 I14− π cosα
8 I15− π sinα
8 I16
= πR2
32(R + cosα)I12 + π
8ε2− sinα
8(R + cosα)ε− π(R2 + 4Rcosα + 2 cos2α)
64(R + cosα)2 − π
16R2(R + cosα)2
+ π sin2α
32(R + cosα)2− π sinα
16R2(R + cosα)2
√
R2 + sin2α
+ π sinα
√
R2 + sin2α
32(R + cosα)2 +O(ε)
=− πR2
64(R + cosα)2 log
( R2ε2
16(R + cosα)2
)
+ πR2
32(R + cosα)2 sinh−1
(sinα
R
)
+ π
8ε2− sinα
8(R + cosα)ε− π(R2 + 4Rcosα + 2 cos2α)
64(R + cosα)2 − π
16R2(R + cosα)2 + π sin2α
32(R + cosα)2
− π sinα
16R2(R + cosα)2
√
R2 + sin2α
+ π sinα
√
R2 + sin2α
32(R + cosα)2 +O(ε).
The integral I3 can be obtained from I1 by changing α to−α:
I3 = 1
8
∫ cos−1 ε
2
0
∫ π
2
0
R− cos(−α− 2θ)
(cos2θ + (R + cosα)(R− cos(−α− 2θ)) sin2 v
2)2dvdθ
=− πR2
64(R + cosα)2 log
( R2ε2
16(R + cosα)2
)
− πR2
32(R + cosα)2 sinh−1
(sinα
R
)
+ π
8ε2 + sinα
8(R + cosα)ε− π(R2 + 4Rcosα + 2 cos2α)
64(R + cosα)2 − π
16R2(R + cosα)2 + π sin2α
32(R + cosα)2
+ π sinα
16R2(R + cosα)2
√
R2 + sin2α
−π sinα
√
R2 + sin2α
32(R + cosα)2 +O(ε).
By putting all the formulae together we obtain
V (ε,x ) = 2 (I1 +I2 +I3 +I4)
= π
ε2− πR2
16(R + cosα)2 log
( R2ε2
(R + cosα)2
)
+ πR2
8(R + cosα)2 3 log 2
−π
8− π
4R2(R + cosα)2 + π(1 + sin2α)
8(R + cosα)2.
As the Gauss curvature and ∆ = (κ1−κ2)2 at the point x =p(α, 0) is given by
K(x) = cosα
(R + cosα), ∆(x) = R2
(R + cosα)2,
the renormalized potential is given by
V (x;T ) = lim
ε→0
(
V (ε,x )− π
ε2 + π∆(x)
16 log
(
∆(x)ε2)
+ πK(x)
4
)
= πR2
8(R + cosα)2 3 log 2− π
8− π
4R2(R + cosα)2 + π(1 + sin2α)
8(R + cosα)2 + π cosα
4(R + cosα).
Flux in QCS IOP Publishing
Journal of Physics: Conference Series 544 (2014) 012019 doi:10.1088/1742-6596/544/1/012019
10
Finally, it implies that the renormalized r−4-potential energy of the torus T is given by
E(T ) =
∫
T
V (x;T )d2x
= 2π
∫ 2π
0
( πR2
8(R + cosα)2 3 log 2− π
8− π
4R2(R + cosα)2 + π(1 + sin2α)
8(R + cosα)2
+ π cosα
4(R + cosα)
)
(R + cosα)dα
=π2
2
∫ π
0
((
R2 (3 log 2− 1) + 2− 2
R2
) 1
R + cosα
)
dα
=π2
2
[(
R2 (3 log 2− 1) + 2− 2
R2
) 2√
R2− 1
tan−1
(√
R− 1
R + 1 tanα
2
)]π
0
= π3
2
√
R2− 1
(
R2 (3 log 2− 1) + 2− 2
R2
)
.
□
