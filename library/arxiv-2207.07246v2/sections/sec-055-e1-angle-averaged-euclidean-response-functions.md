---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-055-e1-angle-averaged-euclidean-response-functions
section_title: "E.1 Angle Averaged Euclidean Response Functions"
section_number: null
pages: 154-165
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
For any operator ˆO which is independent of the momentum k, e.g., ˆO can be e−Hτ
or e−Vτ deﬁned in Eq.(4.48), we show how to take the angle average of momentum k
in calculating
∫
ρ†(k) ˆOρ(k)dΩ/4π in the response functions.
In order to proceed, we ﬁrst set up the coordinates as shown in Fig. E.1. The polar
angle is θ, the azimuthal angle is ϕ, and dΩ = sinθdθdϕ. The length of k isk, its unit
vector is ˆk, the x, y and z components of ˆk are
ˆkx = sinθ cosϕ, (E.1)
ˆky = sinθ sinϕ, (E.2)
ˆkz = cosθ. (E.3)
The vector between particle j and i is deﬁned as rji≡rj−ri. Its length is rji, and
its unit vector is ˆrji and its components are ˆrx, ˆry and ˆrz.
Figure E.1: The coordinates for the angle averaged Euclidean response functions.
Note that the plane wave eik·rji can be expanded by spherical harmonics (Jackson
(1999)),
eik·rji = 4π
∞∑
𝓁=0
𝓁∑
m=−𝓁
i𝓁j𝓁(krji)Ym
𝓁 (ˆk)Ym
𝓁
∗(ˆrji)
= 4π
∞∑
𝓁=0
𝓁∑
m=−𝓁
i𝓁j𝓁(krji)Ym
𝓁
∗(ˆrji)Ym
𝓁 (θ,ϕ ), (E.4)
144
where j𝓁 are spherical Bessel functions (Abramowitz and Stegun (1964)), and the
spherical harmonicsYm
𝓁 (ˆk) =Ym
𝓁 (θ,ϕ ). In this calculation we only need those functions
with 𝓁 = 0, 2.
For the spherical Bessel functions we need j0(krji) and j2(krji),
j0(krji) = sin(krji)
krji
, (E.5)
j2(krji) =
( 3
k2r2
ji
− 1
) sin(krji)
krji
− 3 cos(krji)
k2r2
ji
. (E.6)
For𝓁 = 0, the spherical harmonics of ˆk and ˆrji are the same and they can be
written as,
Y 0
0 (θ,ϕ ) =Y 0
0 (ˆk) =Y 0
0 (rji) =
√
1
4π. (E.7)
For𝓁 = 2, the spherical harmonics of ˆk can be written in terms of θ and ϕ as,
Y−2
2 (θ,ϕ ) = 1
4
√
15
2π·e−2iϕ· sin2θ, (E.8)
Y−1
2 (θ,ϕ ) = 1
2
√
15
2π·e−iϕ· sinθ· cosθ, (E.9)
Y 0
2 (θ,ϕ ) = 1
4
√
5
π· (3 cos2θ− 1), (E.10)
Y 1
2 (θ,ϕ ) =−1
2
√
15
2π·eiϕ· sinθ· cosθ, (E.11)
Y 2
2 (θ,ϕ ) = 1
4
√
15
2π·e2iϕ· sin2θ. (E.12)
The spherical harmonics of ˆrji for𝓁 = 2 can be written in terms of ˆrx, ˆry and ˆrz as,
Y−2
2 (ˆrji) = 1
4
√
15
2π· (ˆrx−iˆry)2, (E.13)
Y−1
2 (ˆrji) = 1
2
√
15
2π· (ˆrx−iˆry)ˆrz, (E.14)
Y 0
2 (ˆrji) = 1
4
√
5
π· (2ˆr2
z− ˆr2
x− ˆr2
y), (E.15)
Y 1
2 (ˆrji) =−1
2
√
15
2π· (ˆrx +iˆry)ˆrz, (E.16)
Y 2
2 (ˆrji) = 1
4
√
15
2π· (ˆrx +iˆry)2. (E.17)
145
The Spherical harmonics are orthogonal such that
∫ π
θ=0
∫ 2π
ϕ=0
Ym
𝓁 (θ,ϕ )Ym′
𝓁′
∗(θ,ϕ )dΩ =δ𝓁𝓁′δmm′, (E.18)
and they satisfy,
Ym
𝓁
∗ = (−1)mY−m
𝓁 . (E.19)
The following derived relations for spherical harmonics will be used,
cos2θ = 4
3
√π
5Y 0
2
∗
(θ,ϕ ) + 1
3, (E.20)
sinθ cosθ cosϕ =
√
2π
15
[
Y−1
2
∗
(θ,ϕ )−Y 1
2
∗
(θ,ϕ )
]
, (E.21)
sinθ cosθ sinϕ = 1
i
√
2π
15
[
Y−1
2
∗
(θ,ϕ ) +Y 1
2
∗
(θ,ϕ )
]
, (E.22)
sin2θ cos 2ϕ = 2
√
2π
15
[
Y 2
2
∗
(θ,ϕ ) +Y−2
2
∗
(θ,ϕ )
]
, (E.23)
sin2θ cosϕ sinϕ = 1
i
√
2π
15
[
Y−2
2
∗
(θ,ϕ )−Y 2
2
∗
(θ,ϕ )
]
, (E.24)
sin2θ sin2ϕ = 1
3− 2
3
√π
5Y 0
2
∗
(θ,ϕ )−
√
2π
15
[
Y 2
2
∗
(θ,ϕ ) +Y−2
2
∗
(θ,ϕ )
]
. (E.25)
Before calculating the angle averaged response functions, we need to calculate
several relevant angle averaged functions.
1. Angle averaged function
∫
eik·rjidΩ/4π can be calculated as,
1
4π
∫
eik·rjidΩ
=
∞∑
𝓁=0
𝓁∑
m=−𝓁
i𝓁j𝓁(krji)Ym
𝓁
∗(ˆrji)
∫
Ym
𝓁 (θ,ϕ )dΩ
=
∞∑
𝓁=0
𝓁∑
m=−𝓁
i𝓁j𝓁(krji)Ym
𝓁
∗(ˆrji)
∫
Ym
𝓁 (θ,ϕ )
√
4πY 0
0
∗
(θ,ϕ )dΩ
=
∞∑
𝓁=0
𝓁∑
m=−𝓁
i𝓁j𝓁(krji)Ym
𝓁
∗(ˆrji)
√
4πδ𝓁0δm0
=j0(krji). (E.26)
146
2. Angle averaged function
∫
eik·rji ˆkxˆkxdΩ/4π can be calculated as,
1
4π
∫
eik·rji ˆkxˆkxdΩ
=
∞∑
𝓁=0
𝓁∑
m=−𝓁
i𝓁j𝓁(krji)Ym
𝓁
∗(ˆrji)
∫
Ym
𝓁 (θ,ϕ ) sin2θ cos2ϕdΩ
=
∞∑
𝓁=0
𝓁∑
m=−𝓁
i𝓁j𝓁(krji)Ym
𝓁
∗(ˆrji)
×
∫
Ym
𝓁 (θ,ϕ )
{
1
3− 2
3
√π
5Y 0
2
∗
(θ,ϕ ) +
√
2π
15
[
Y 2
2
∗
(θ,ϕ ) +Y−2
2
∗
(θ,ϕ )
]
}
dΩ
=
∞∑
𝓁=0
𝓁∑
m=−𝓁
i𝓁j𝓁(krji)Ym
𝓁
∗(ˆrji)
×
(√
4π
3 δ𝓁0δm0− 2
3
√π
5δ𝓁2δm0 +
√
2π
15δ𝓁2δm−2 +
√
2π
15δ𝓁2δm2
)
=
√
4π
3 j0(krji)Y 0
0
∗
(ˆrji) + 2
3
√π
5j2(krji)Y 0
2
∗
(ˆrji)
−
√
2π
15
[
j0(krji)Y−2
2
∗
(ˆrji)−j2(krji)Y 2
2
∗
(ˆrji)
]
= 1
3
[
j0(krji) +j2(krji)(ˆr2
z + ˆr2
y− 2ˆr2
x)
]
. (E.27)
3. Angle averaged function
∫
eik·rji ˆkxˆkydΩ/4π can be calculated as,
1
4π
∫
eik·rji ˆkxˆkydΩ
=
∞∑
𝓁=0
𝓁∑
m=−𝓁
i𝓁j𝓁(krji)Ym
𝓁
∗(ˆrji)
∫
Ym
𝓁 (θ,ϕ ) sin2θ cosϕ sinϕdΩ
=
∞∑
𝓁=0
𝓁∑
m=−𝓁
i𝓁j𝓁(krji)Ym
𝓁
∗(ˆrji)
∫
Ym
𝓁 (θ,ϕ )1
i
√
2π
15
[
Y−2
2
∗(θ,ϕ )−Y 2
2
∗(θ,ϕ )
]
dΩ
=
∞∑
𝓁=0
𝓁∑
m=−𝓁
i𝓁j𝓁(krji)Ym
𝓁
∗(ˆrji)1
i
√
2π
15 (δ𝓁2δm−2−δ𝓁2δm2)
=−j2(krji)
[
Y−2
2
∗
(ˆrji)1
i
√
2π
15−Y 2
2
∗
(ˆrji)1
i
√
2π
15
]
=−j2(krji)ˆrxˆry. (E.28)
147
4. Angle averaged function
∫
eik·rji ˆkxˆkzdΩ/4π can be calculated as,
1
4π
∫
eik·rji ˆkxˆkzdΩ
=
∞∑
𝓁=0
𝓁∑
m=−𝓁
i𝓁j𝓁(krji)Ym
𝓁
∗(ˆrji)
∫
Ym
𝓁 (θ,ϕ ) sinθ cosθ cosϕdΩ
=
∞∑
𝓁=0
𝓁∑
m=−𝓁
i𝓁j𝓁(krji)Ym
𝓁
∗(ˆrji)
∫
Ym
𝓁 (θ,ϕ )
√
2π
15
[
Y−1
2
∗
(θ,ϕ )−Y 1
2
∗
(θ,ϕ )
]
dΩ
=
∞∑
𝓁=0
𝓁∑
m=−𝓁
i𝓁j𝓁(krji)Ym
𝓁
∗(ˆrji)
(√
2π
15δ𝓁2δm−1−
√
2π
15δ𝓁2δm1
)
=−j2(krji)
[
Y−1
2
∗
(ˆrji)
√
2π
15−Y 1
2
∗
(ˆrji)
√
2π
15
]
=−j2(krji)ˆrxˆrz. (E.29)
5. Angle averaged function
∫
eik·rji ˆkyˆkydΩ/4π can be calculated as,
1
4π
∫
eik·rji ˆkyˆkydΩ
=
∞∑
𝓁=0
𝓁∑
m=−𝓁
i𝓁j𝓁(krji)Ym
𝓁
∗(ˆrji)
∫
Ym
𝓁 (θ,ϕ ) sin2θ cos2ϕdΩ
=
∞∑
𝓁=0
𝓁∑
m=−𝓁
i𝓁j𝓁(krji)Ym
𝓁
∗(ˆrji)
×
∫
Ym
𝓁 (θ,ϕ )
{
1
3− 2
3
√π
5Y 0
2
∗
(θ,ϕ ) +
√
2π
15
[
Y 2
2
∗
(θ,ϕ ) +Y−2
2
∗
(θ,ϕ )
]
}
dΩ
=
∞∑
𝓁=0
𝓁∑
m=−𝓁
i𝓁j𝓁(krji)Ym
𝓁
∗(ˆrji)
×
[√
4π
3 δ𝓁0δm0− 2
3
√π
5δ𝓁2δm0 +
√
2π
15 (δ𝓁2δm−2 +δ𝓁2δm2)
]
=
√
4π
3 j0(krji)Y 0
0
∗
(ˆrji) + 2
3
√π
5j2(krji)Y 0
2
∗
(ˆrji)
−
√
2π
15j0(krji)Y−2
2
∗
(ˆrji)−
√
2π
15j2(krji)Y 2
2
∗
(ˆrji)
= 1
3
[
j0(krji) +j2(krji)(ˆr2
z + ˆr2
x− 2ˆr2
y)
]
. (E.30)
148
6. Angle averaged function
∫
eik·rji ˆkyˆkzdΩ/4π can be calculated as,
1
4π
∫
eik·rji ˆkyˆkzdΩ
=
∞∑
𝓁=0
𝓁∑
m=−𝓁
i𝓁j𝓁(krji)Ym
𝓁
∗(ˆrji)
∫
Ym
𝓁 (θ,ϕ ) sinθ cosθ sinϕdΩ
=
∞∑
𝓁=0
𝓁∑
m=−𝓁
i𝓁j𝓁(krji)Ym
𝓁
∗(ˆrji)
∫
Ym
𝓁 (θ,ϕ )1
i
√
2π
15
[
Y−1
2
∗
(θ,ϕ ) +Y 1
2
∗
(θ,ϕ )
]
dΩ
=
∞∑
𝓁=0
𝓁∑
m=−𝓁
i𝓁j𝓁(krji)Ym
𝓁
∗(ˆrji)
(
1
i
√
2π
15δ𝓁2δm−1− 1
i
√
2π
15δ𝓁2δm1
)
=−j2(krji)
[
Y−1
2
∗
(ˆrji)1
i
√
2π
15 +Y 1
2
∗
(ˆrji)1
i
√
2π
15
]
=−j2(krji)ˆrxˆrz. (E.31)
7. Angle averaged function
∫
eik·rji ˆkzˆkzdΩ/4π can be calculated as,
1
4π
∫
eik·rji ˆkzˆkzdΩ
=
∞∑
𝓁=0
𝓁∑
m=−𝓁
i𝓁j𝓁(krji)Ym
𝓁
∗(ˆrji)
∫
Ym
𝓁 (θ,ϕ ) cos2θdΩ
=
∞∑
𝓁=0
𝓁∑
m=−𝓁
i𝓁j𝓁(krji)Ym
𝓁
∗(ˆrji)
∫
Ym
𝓁 (θ,ϕ )
[1
3 + 4
3
√π
5Y 0
2
∗
(θ,ϕ )
]
dΩ
=
∞∑
𝓁=0
𝓁∑
m=−𝓁
i𝓁j𝓁(krji)Ym
𝓁
∗(ˆrji)
(√
4π
3 δ𝓁0δm0 + 4
3
√π
5δ𝓁2δm0
)
=
√
4π
3 j0(krji)Y 0
0
∗
(ˆrji)− 4
3
√π
5j2(krji)Y 0
2
∗
(ˆrji)
= 1
3
[
j0(krji) +j2(krji)(ˆr2
x + ˆr2
y− 2ˆr2
z)
]
. (E.32)
With the help of Eqs.(E.26) to (E.32), the 5 angle averaged response functions∫
ρ†(k) ˆOρ(k)dΩ/4π can be conveniently calculated.
149
1. For the angle averaged nucleon coupling ρN(k) we have,
1
4π
∫
ρ†
N(k) ˆOρN(k)dΩ
= 1
4π
∫ ( A∑
i=1
e−ik·ri
)
ˆO
( A∑
j=1
eik·rj
)
dΩ
= 1
4π
A∑
i=1
A∑
j=1
(∫
eik·rjidΩ
)
ˆO
=
A∑
i=1
A∑
j=1
j0(krji) ˆO. (E.33)
2. For the angle averaged proton coupling ρp(k) we have,
1
4π
∫
ρ†
p(k) ˆOρp(k)dΩ
= 1
4π
∫ ( A∑
i=1
e−ik·ri 1 +τiz
2
)
ˆO
( A∑
j=1
eik·rj 1 +τjz
2
)
dΩ
= 1
4π
A∑
i=1
A∑
j=1
(∫
eik·rjidΩ
) 1 +τiz
2
ˆO1 +τjz
2
=
A∑
i=1
A∑
j=1
j0(krji)1 +τiz
2
ˆO1 +τjz
2 . (E.34)
3. For the angle averaged isovector coupling ρτ(k) we have,
1
4π
∫
ρ†
τ(k) ˆOρτ(k)dΩ
= 1
4π
∫ ( A∑
i=1
e−ik·riτiz
)
ˆO
( A∑
j=1
eik·rjτjz
)
dΩ
= 1
4π
A∑
i=1
A∑
j=1
(∫
eik·rjidΩ
)
τiz ˆOτjz
=
A∑
i=1
A∑
j=1
j0(krji)τiz ˆOτjz. (E.35)
150
4. For the angle averaged spin-longitudinal coupling ρστL (k) we have,
1
4π
∫
ρ†
στL (k) ˆOρστL (k)dΩ
= 1
4π
∫ [ A∑
i=1
e−ik·ri(σi· ˆk)τiz
]
ˆO
[ A∑
j=1
eik·rj 1 +τjz
2 (σj· ˆk)τjz
]
dΩ
= 1
4π
A∑
i=1
A∑
j=1
(∫
eik·rji ˆkxˆkxdΩ
)
σixτiz ˆOσjxτjz
+ 1
4π
A∑
i=1
A∑
j=1
(∫
eik·rji ˆkyˆkydΩ
)
σiyτiz ˆOσjyτjz
+ 1
4π
A∑
i=1
A∑
j=1
(∫
eik·rji ˆkzˆkzdΩ
)
σizτiz ˆOσjzτjz
+ 1
4π
A∑
i=1
A∑
j=1
(∫
eik·rji ˆkxˆkydΩ
)(
σiyτiz ˆOσjxτjz +σixτiz ˆOσjyτjz
)
+ 1
4π
A∑
i=1
A∑
j=1
(∫
eik·rji ˆkxˆkzdΩ
)(
σizτiz ˆOσjxτjz +σixτiz ˆOσjzτjz
)
+ 1
4π
A∑
i=1
A∑
j=1
(∫
eik·rji ˆkyˆkzdΩ
)(
σizτiz ˆOσjyτjz +σiyτiz ˆOσjzτjz
)
= 1
3
A∑
i=1
A∑
j=1
[
j0(krji) +j2(krji)(ˆr2
z + ˆr2
y− 2ˆr2
x)
]
σixτiz ˆOσjxτjz
+ 1
3
A∑
i=1
A∑
j=1
[
j0(krji) +j2(krji)(ˆr2
x + ˆr2
z− 2ˆr2
y)
]
σiyτiz ˆOσjyτjz
+ 1
3
A∑
i=1
A∑
j=1
[
j0(krji) +j2(krji)(ˆr2
x + ˆr2
y− 2ˆr2
z)
]
σizτiz ˆOσjzτjz
−
A∑
i=1
A∑
j=1
j2(krji)ˆrxˆry
(
σiyτiz ˆOσjxτjz +σixτiz ˆOσjyτjz
)
−
A∑
i=1
A∑
j=1
j2(krji)ˆrxˆrz
(
σizτiz ˆOσjxτjz +σixτiz ˆOσjzτjz
)
−
A∑
i=1
A∑
j=1
j2(krji)ˆryˆrz
(
σizτiz ˆOσjyτjz +σiyτiz ˆOσjzτjz
)
. (E.36)
151
5. For the angle averaged spin-transverse coupling ρστT (k) we have,
1
4π
∫
ρ†
στT (k) ˆO·ρστT (k)dΩ
= 1
4π
∫ [ A∑
i=1
e−ik·ri(σi× ˆk)τiz
]
ˆO·
[ A∑
j=1
eik·rj(σj× ˆk)τjz
]
dΩ
= 1
4π
A∑
i=1
A∑
j=1
(∫
eik·rji ˆkxˆkxdΩ +
∫
eik·rji ˆkzˆkzdΩ
)
σiyτiz ˆOσjyτjz
+ 1
4π
A∑
i=1
A∑
j=1
(∫
eik·rji ˆkxˆkxdΩ +
∫
eik·rji ˆkyˆkydΩ
)
σizτiz ˆOσjzτjz
+ 1
4π
A∑
i=1
A∑
j=1
(∫
eik·rji ˆkyˆkydΩ +
∫
eik·rji ˆkzˆkzdΩ
)
σixτiz ˆOσjxτjz
− 1
4π
A∑
i=1
A∑
j=1
(∫
eik·rji ˆkxˆkydΩ
)(
σixτiz ˆOσjyτjz +σiyτiz ˆOσjxτjz
)
− 1
4π
A∑
i=1
A∑
j=1
(∫
eik·rji ˆkxˆkzdΩ
)(
σixτiz ˆOσjzτjz +σizτiz ˆOσjxτjz
)
− 1
4π
A∑
i=1
A∑
j=1
(∫
eik·rji ˆkyˆkzdΩ
)(
σiyτiz ˆOσjzτjz +σizτiz ˆOσjyτjz
)
= 1
3
A∑
i=1
A∑
j=1
[
2j0(krji) +j2(krji)(2ˆr2
y− ˆr2
x− ˆr2
z)
]
σiyτiz ˆOσjyτjz
+ 1
3
A∑
i=1
A∑
j=1
[
2j0(krji) +j2(krji)(2ˆr2
z− ˆr2
x− ˆr2
y)
]
σizτiz ˆOσjzτjz
+ 1
3
A∑
i=1
A∑
j=1
[
2j0(krji) +j2(krji)(2ˆr2
x− ˆr2
y− ˆr2
z)
]
σixτiz ˆOσjxτjz
+
A∑
i=1
A∑
j=1
j2(krji)ˆrxˆry
(
σixτiz ˆOσjyτjz +σiyτiz ˆOσjxτjz
)
+
A∑
i=1
A∑
j=1
j2(krji)ˆrxˆrz
(
σixτiz ˆOσjzτjz +σizτiz ˆOσjxτjz
)
+
A∑
i=1
A∑
j=1
j2(krji)ˆryˆrz
(
σiyτiz ˆOσjzτjz +σizτiz ˆOσjyτjz
)
. (E.37)
152
E.2 Euclidean Response Functions in Diﬀerent Coordinates
In all the ρ(k), we can choose ri to be particle i’s absolute position, we can also
chooseri to be particle i’s relative position in the center of mass frame. The response
functions calculated using the center of mass ri multiply by a factor of e−k2τ/2M will
be those calculated using the absolute coordinate ri, where M =Am is the total mass
of system. This can be explained by decomposing the separable Hamiltonian into the
center of mass part HCM =P 2/2M, where P =∑A
i=1pi is the total momentum, and
a relative partHrel ﬁrst (Messiah (2014)), then make use of the momentum translation
operators.
The relevant part in Eq.(4.41) in absolute coordinate is
⟨Φ0|
∑
j
e−ik·ˆrje−Hτ
∑
n
eik·ˆrn|Φ0⟩ =⟨Φ0|
∑
j
e−ik·ˆrje− P 2
2Mτe−Hrelτ
∑
n
eik·ˆrn|Φ0⟩. (E.38)
The total momentum P of the ground state |Φ0⟩ is 0, and the momentum translation
operator eik·ˆrn will move particle n’s momentum by k, therefore∑
neik·ˆrn will change
the system’s total momentum from 0 to k and we have
∑
n
eik·ˆrn|Φ0⟩ =|k⟩. (E.39)
Also consider that the Hamiltonian is translational invariant, so [H,P ] = 0 and
therefore [Hrel,P ] = 0, so e−Hrelτ and e− P 2
2Mτ commute, then Eq.(E.38) becomes,
⟨Φ0|
∑
j
e−ik·ˆrje− P 2
2Mτe−Hrelτ
∑
n
eik·ˆrn|Φ0⟩
=⟨Φ0|
∑
j
e−ik·ˆrje−Hrelτe− P 2
2Mτ
∑
n
eik·ˆrn|Φ0⟩
=e− k2τ
2M⟨Φ0|
∑
j
e−ik·ˆrje−Hrelτ
∑
n
eik·ˆrn|Φ0⟩. (E.40)
The relevant part in Eq.(4.41) in the center of mass coordinate is
⟨Φ0|
∑
j
e−ik·(ˆrj− ˆRCM )e− P 2
2Mτe−Hrelτ
∑
n
eik·(ˆrn− ˆRCM )|Φ0⟩, (E.41)
where ˆRCM =
∑
i ˆri
A is the center of the mass operator. Note that e−ik· ˆRCM is also a
momentum translation operator which changes the system’s total momentum by −k,
e−ik· ˆRCM|Φ0⟩ =e−ik·
∑
i ˆri
A |Φ0⟩ =|− k⟩. (E.42)
So, the combined operator ∑
neik·(ˆrn− ˆRCM ) =e−ik· ˆRCM
∑
neik·ˆrn does not change the
system’s total momentum. Therefore, the ground state’s total momentum P remains
153
zero after being operated by ∑
ne±ik·(ˆrn− ˆRCM ). Also, ˆRCM commutes with Hrel so
e±ik· ˆRCM and e−Hrelτ commute with each other. Taking all these into consideration,
Eq.(E.41) becomes,
⟨Φ0|
∑
j
e−ik·(ˆrj− ˆRCM )e− P 2
2Mτe−Hrelτ
∑
n
eik·(ˆrn− ˆRCM )|Φ0⟩
=⟨Φ0|
∑
j
e−ik·ˆrjeik· ˆRCMe−Hrelτe−ik· ˆRCM
∑
n
eik·ˆrn|Φ0⟩
=⟨Φ0|
∑
j
e−ik·ˆrje−Hrelτ
∑
n
eik·ˆrn|Φ0⟩ (E.43)
Comparing Eq.(E.40) and Eq.(E.43), we see that the center of mass result Eq.(E.43)
need to multiply by the factor of e− k2τ
2M to match the result in absolute coordinate
Eq.(E.40). Take 4He as an example, in our plots, k = 350 MeV/c, m = 939 MeV/c2,
M = 4m = 8, so the factor e− k2τ
2M becomes e−16.3τ. We calculate our response functions
in the center of mass frame ﬁrst because it will give lower variance compared with
absolute coordinate (laboratory frame). We then multiply our results by e−16.3τ in
order to compare with the results in Carlson and Schiavilla’s 1994 paper which are
marked as the red dots in Figs. 4.12 and 4.13.
154
