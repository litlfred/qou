---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-069-e1-angle-averaged-euclidean-response-functions
section_title: "E.1 Angle Averaged Euclidean Response Functions"
section_number: null
pages: 154-163
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
Angle Averaged Euclidean Response Functions
For any operator ˆO which is independent of the momentum k, e.g., ˆO can be e−Hτ
or e−V τ deﬁned in Eq.(4.48), we show how to take the angle average of momentum k
in calculating
R
ρ†(k) ˆOρ(k)dΩ/4π in the response functions.
In order to proceed, we ﬁrst set up the coordinates as shown in Fig. E.1. The polar
angle is θ, the azimuthal angle is ϕ, and dΩ= sin θdθdϕ. The length of k is k, its unit
vector is ˆk, the x, y and z components of ˆk are
ˆkx = sin θ cos ϕ,
(E.1)
ˆky = sin θ sin ϕ,
(E.2)
ˆkz = cos θ.
(E.3)
The vector between particle j and i is deﬁned as rji ≡rj −ri. Its length is rji, and
its unit vector is ˆrji and its components are ˆrx, ˆry and ˆrz.
Figure E.1: The coordinates for the angle averaged Euclidean response functions.
Note that the plane wave eik·rji can be expanded by spherical harmonics (Jackson
(1999)),
eik·rji = 4π
∞
X
ℓ=0
ℓ
X
m=−ℓ
iℓjℓ(krji)Y m
ℓ(ˆk)Y m
ℓ
∗(ˆrji)
= 4π
∞
X
ℓ=0
ℓ
X
m=−ℓ
iℓjℓ(krji)Y m
ℓ
∗(ˆrji)Y m
ℓ(θ, ϕ),
(E.4)
144
where jℓare spherical Bessel functions (Abramowitz and Stegun (1964)), and the
spherical harmonics Y m
ℓ(ˆk) = Y m
ℓ(θ, ϕ). In this calculation we only need those functions
with ℓ= 0, 2.
For the spherical Bessel functions we need j0(krji) and j2(krji),
j0(krji) = sin(krji)
krji
,
(E.5)
j2(krji) =

3
k2r2
ji
−1
 sin(krji)
krji
−3 cos(krji)
k2r2
ji
.
(E.6)
For ℓ= 0, the spherical harmonics of ˆk and ˆrji are the same and they can be
written as,
Y 0
0 (θ, ϕ) = Y 0
0 (ˆk) = Y 0
0 (rji) =
r
1
4π.
(E.7)
For ℓ= 2, the spherical harmonics of ˆk can be written in terms of θ and ϕ as,
Y −2
2
(θ, ϕ) = 1
4
r
15
2π · e−2iϕ · sin2 θ,
(E.8)
Y −1
2
(θ, ϕ) = 1
2
r
15
2π · e−iϕ · sin θ · cos θ,
(E.9)
Y 0
2 (θ, ϕ) = 1
4
r
5
π · (3 cos2 θ −1),
(E.10)
Y 1
2 (θ, ϕ) = −1
2
r
15
2π · eiϕ · sin θ · cos θ,
(E.11)
Y 2
2 (θ, ϕ) = 1
4
r
15
2π · e2iϕ · sin2 θ.
(E.12)
The spherical harmonics of ˆrji for ℓ= 2 can be written in terms of ˆrx, ˆry and ˆrz as,
Y −2
2
(ˆrji) = 1
4
r
15
2π · (ˆrx −iˆry)2,
(E.13)
Y −1
2
(ˆrji) = 1
2
r
15
2π · (ˆrx −iˆry)ˆrz,
(E.14)
Y 0
2 (ˆrji) = 1
4
r
5
π · (2ˆr2
z −ˆr2
x −ˆr2
y),
(E.15)
Y 1
2 (ˆrji) = −1
2
r
15
2π · (ˆrx + iˆry)ˆrz,
(E.16)
Y 2
2 (ˆrji) = 1
4
r
15
2π · (ˆrx + iˆry)2.
(E.17)
145
The Spherical harmonics are orthogonal such that
Z π
θ=0
Z 2π
ϕ=0
Y m
ℓ(θ, ϕ) Y m′
ℓ′
∗(θ, ϕ) dΩ= δℓℓ′ δmm′,
(E.18)
and they satisfy,
Y m
ℓ
∗= (−1)mY −m
ℓ
.
(E.19)
The following derived relations for spherical harmonics will be used,
cos2 θ = 4
3
rπ
5 Y 0
2
∗(θ, ϕ) + 1
3,
(E.20)
sin θ cos θ cos ϕ =
r
2π
15

Y −1
2
∗(θ, ϕ) −Y 1
2
∗(θ, ϕ)

,
(E.21)
sin θ cos θ sin ϕ = 1
i
r
2π
15

Y −1
2
∗(θ, ϕ) + Y 1
2
∗(θ, ϕ)

,
(E.22)
sin2 θ cos 2ϕ = 2
r
2π
15

Y 2
2
∗(θ, ϕ) + Y −2
2
∗(θ, ϕ)

,
(E.23)
sin2 θ cos ϕ sin ϕ = 1
i
r
2π
15

Y −2
2
∗(θ, ϕ) −Y 2
2
∗(θ, ϕ)

,
(E.24)
sin2 θ sin2 ϕ = 1
3 −2
3
rπ
5 Y 0
2
∗(θ, ϕ) −
r
2π
15

Y 2
2
∗(θ, ϕ) + Y −2
2
∗(θ, ϕ)

.
(E.25)
Before calculating the angle averaged response functions, we need to calculate
several relevant angle averaged functions.
1. Angle averaged function
R
eik·rjidΩ/4π can be calculated as,
1
4π
Z
eik·rjidΩ
=
∞
X
ℓ=0
ℓ
X
m=−ℓ
iℓjℓ(krji)Y m
ℓ
∗(ˆrji)
Z
Y m
ℓ(θ, ϕ)dΩ
=
∞
X
ℓ=0
ℓ
X
m=−ℓ
iℓjℓ(krji)Y m
ℓ
∗(ˆrji)
Z
Y m
ℓ(θ, ϕ)
√
4πY 0
0
∗(θ, ϕ)dΩ
=
∞
X
ℓ=0
ℓ
X
m=−ℓ
iℓjℓ(krji)Y m
ℓ
∗(ˆrji)
√
4πδℓ0 δm0
= j0(krji).
(E.26)
146
2. Angle averaged function
R
eik·rjiˆkxˆkxdΩ/4π can be calculated as,
1
4π
Z
eik·rjiˆkxˆkxdΩ
=
∞
X
ℓ=0
ℓ
X
m=−ℓ
iℓjℓ(krji)Y m
ℓ
∗(ˆrji)
Z
Y m
ℓ(θ, ϕ) sin2 θ cos2 ϕdΩ
=
∞
X
ℓ=0
ℓ
X
m=−ℓ
iℓjℓ(krji)Y m
ℓ
∗(ˆrji)
×
Z
Y m
ℓ(θ, ϕ)
(
1
3 −2
3
rπ
5 Y 0
2
∗(θ, ϕ) +
r
2π
15

Y 2
2
∗(θ, ϕ) + Y −2
2
∗(θ, ϕ)

)
dΩ
=
∞
X
ℓ=0
ℓ
X
m=−ℓ
iℓjℓ(krji)Y m
ℓ
∗(ˆrji)
×
 √
4π
3
δℓ0 δm0 −2
3
rπ
5 δℓ2 δm0 +
r
2π
15 δℓ2 δm−2 +
r
2π
15δℓ2 δm2
!
=
√
4π
3
j0(krji)Y 0
0
∗(ˆrji) + 2
3
rπ
5 j2(krji)Y 0
2
∗(ˆrji)
−
r
2π
15

j0(krji)Y −2
2
∗(ˆrji) −j2(krji)Y 2
2
∗(ˆrji)

= 1
3

j0(krji) + j2(krji)(ˆr2
z + ˆr2
y −2ˆr2
x)

.
(E.27)
3. Angle averaged function
R
eik·rjiˆkxˆkydΩ/4π can be calculated as,
1
4π
Z
eik·rjiˆkxˆkydΩ
=
∞
X
ℓ=0
ℓ
X
m=−ℓ
iℓjℓ(krji)Y m
ℓ
∗(ˆrji)
Z
Y m
ℓ(θ, ϕ) sin2 θ cos ϕ sin ϕdΩ
=
∞
X
ℓ=0
ℓ
X
m=−ℓ
iℓjℓ(krji)Y m
ℓ
∗(ˆrji)
Z
Y m
ℓ(θ, ϕ)1
i
r
2π
15

Y −2
2
∗(θ, ϕ) −Y 2
2
∗(θ, ϕ)

dΩ
=
∞
X
ℓ=0
ℓ
X
m=−ℓ
iℓjℓ(krji)Y m
ℓ
∗(ˆrji)1
i
r
2π
15 (δℓ2 δm−2 −δℓ2 δm2)
= −j2(krji)
"
Y −2
2
∗(ˆrji)1
i
r
2π
15 −Y 2
2
∗(ˆrji)1
i
r
2π
15
#
= −j2(krji)ˆrxˆry.
(E.28)
147
4. Angle averaged function
R
eik·rjiˆkxˆkzdΩ/4π can be calculated as,
1
4π
Z
eik·rjiˆkxˆkzdΩ
=
∞
X
ℓ=0
ℓ
X
m=−ℓ
iℓjℓ(krji)Y m
ℓ
∗(ˆrji)
Z
Y m
ℓ(θ, ϕ) sin θ cos θ cos ϕdΩ
=
∞
X
ℓ=0
ℓ
X
m=−ℓ
iℓjℓ(krji)Y m
ℓ
∗(ˆrji)
Z
Y m
ℓ(θ, ϕ)
r
2π
15

Y −1
2
∗(θ, ϕ) −Y 1
2
∗(θ, ϕ)

dΩ
=
∞
X
ℓ=0
ℓ
X
m=−ℓ
iℓjℓ(krji)Y m
ℓ
∗(ˆrji)
 r
2π
15 δℓ2 δm−1 −
r
2π
15 δℓ2 δm1
!
= −j2(krji)
"
Y −1
2
∗(ˆrji)
r
2π
15 −Y 1
2
∗(ˆrji)
r
2π
15
#
= −j2(krji)ˆrxˆrz.
(E.29)
5. Angle averaged function
R
eik·rjiˆkyˆkydΩ/4π can be calculated as,
1
4π
Z
eik·rjiˆkyˆkydΩ
=
∞
X
ℓ=0
ℓ
X
m=−ℓ
iℓjℓ(krji)Y m
ℓ
∗(ˆrji)
Z
Y m
ℓ(θ, ϕ) sin2 θ cos2 ϕdΩ
=
∞
X
ℓ=0
ℓ
X
m=−ℓ
iℓjℓ(krji)Y m
ℓ
∗(ˆrji)
×
Z
Y m
ℓ(θ, ϕ)
(
1
3 −2
3
rπ
5 Y 0
2
∗(θ, ϕ) +
r
2π
15

Y 2
2
∗(θ, ϕ) + Y −2
2
∗(θ, ϕ)

)
dΩ
=
∞
X
ℓ=0
ℓ
X
m=−ℓ
iℓjℓ(krji)Y m
ℓ
∗(ˆrji)
×
"√
4π
3
δℓ0 δm0 −2
3
rπ
5 δℓ2 δm0 +
r
2π
15 (δℓ2 δm−2 + δℓ2 δm2)
#
=
√
4π
3
j0(krji)Y 0
0
∗(ˆrji) + 2
3
rπ
5 j2(krji)Y 0
2
∗(ˆrji)
−
r
2π
15j0(krji)Y −2
2
∗(ˆrji) −
r
2π
15j2(krji)Y 2
2
∗(ˆrji)
= 1
3

j0(krji) + j2(krji)(ˆr2
z + ˆr2
x −2ˆr2
y)

.
(E.30)
148
6. Angle averaged function
R
eik·rjiˆkyˆkzdΩ/4π can be calculated as,
1
4π
Z
eik·rjiˆkyˆkzdΩ
=
∞
X
ℓ=0
ℓ
X
m=−ℓ
iℓjℓ(krji)Y m
ℓ
∗(ˆrji)
Z
Y m
ℓ(θ, ϕ) sin θ cos θ sin ϕdΩ
=
∞
X
ℓ=0
ℓ
X
m=−ℓ
iℓjℓ(krji)Y m
ℓ
∗(ˆrji)
Z
Y m
ℓ(θ, ϕ)1
i
r
2π
15

Y −1
2
∗(θ, ϕ) + Y 1
2
∗(θ, ϕ)

dΩ
=
∞
X
ℓ=0
ℓ
X
m=−ℓ
iℓjℓ(krji)Y m
ℓ
∗(ˆrji)
 
1
i
r
2π
15 δℓ2 δm−1 −1
i
r
2π
15 δℓ2 δm1
!
= −j2(krji)
"
Y −1
2
∗(ˆrji)1
i
r
2π
15 + Y 1
2
∗(ˆrji)1
i
r
2π
15
#
= −j2(krji)ˆrxˆrz.
(E.31)
7. Angle averaged function
R
eik·rjiˆkzˆkzdΩ/4π can be calculated as,
1
4π
Z
eik·rjiˆkzˆkzdΩ
=
∞
X
ℓ=0
ℓ
X
m=−ℓ
iℓjℓ(krji)Y m
ℓ
∗(ˆrji)
Z
Y m
ℓ(θ, ϕ) cos2 θdΩ
=
∞
X
ℓ=0
ℓ
X
m=−ℓ
iℓjℓ(krji)Y m
ℓ
∗(ˆrji)
Z
Y m
ℓ(θ, ϕ)
1
3 + 4
3
rπ
5 Y 0
2
∗(θ, ϕ)

dΩ
=
∞
X
ℓ=0
ℓ
X
m=−ℓ
iℓjℓ(krji)Y m
ℓ
∗(ˆrji)
 √
4π
3
δℓ0 δm0 + 4
3
rπ
5 δℓ2 δm0
!
=
√
4π
3
j0(krji)Y 0
0
∗(ˆrji) −4
3
rπ
5 j2(krji)Y 0
2
∗(ˆrji)
= 1
3

j0(krji) + j2(krji)(ˆr2
x + ˆr2
y −2ˆr2
z)

.
(E.32)
With the help of Eqs.(E.26) to (E.32), the 5 angle averaged response functions
R
ρ†(k) ˆOρ(k)dΩ/4π can be conveniently calculated.
149
1. For the angle averaged nucleon coupling ρN(k) we have,
1
4π
Z
ρ†
N(k) ˆOρN(k)dΩ
=
1
4π
Z A
X
i=1
e−ik·ri
!
ˆO
 A
X
j=1
eik·rj
!
dΩ
=
1
4π
A
X
i=1
A
X
j=1
Z
eik·rjidΩ

ˆO
=
A
X
i=1
A
X
j=1
j0(krji) ˆO.
(E.33)
2. For the angle averaged proton coupling ρp(k) we have,
1
4π
Z
ρ†
p(k) ˆOρp(k)dΩ
=
1
4π
Z A
X
i=1
e−ik·ri 1 + τiz
2
!
ˆO
 A
X
j=1
eik·rj 1 + τjz
2
!
dΩ
=
1
4π
A
X
i=1
A
X
j=1
Z
eik·rjidΩ
 1 + τiz
2
ˆO1 + τjz
2
=
A
X
i=1
A
X
j=1
j0(krji)1 + τiz
2
ˆO1 + τjz
2
.
(E.34)
3. For the angle averaged isovector coupling ρτ(k) we have,
1
4π
Z
ρ†
τ(k) ˆOρτ(k)dΩ
=
1
4π
Z A
X
i=1
e−ik·riτiz
!
ˆO
 A
X
j=1
eik·rjτjz
!
dΩ
=
1
4π
A
X
i=1
A
X
j=1
Z
eik·rjidΩ

τiz ˆOτjz
=
A
X
i=1
A
X
j=1
j0(krji)τiz ˆOτjz.
(E.35)
150
4. For the angle averaged spin-longitudinal coupling ρστL(k) we have,
1
4π
Z
ρ†
στL(k) ˆOρστL(k)dΩ
=
1
4π
Z " A
X
i=1
e−ik·ri(σi · ˆk)τiz
#
ˆO
" A
X
j=1
eik·rj 1 + τjz
2
(σj · ˆk)τjz
#
dΩ
=
1
4π
A
X
i=1
A
X
j=1
Z
eik·rjiˆkxˆkxdΩ

σixτiz ˆOσjxτjz
+
1
4π
A
X
i=1
A
X
j=1
Z
eik·rjiˆkyˆkydΩ

σiyτiz ˆOσjyτjz
+
1
4π
A
X
i=1
A
X
j=1
Z
eik·rjiˆkzˆkzdΩ

σizτiz ˆOσjzτjz
+
1
4π
A
X
i=1
A
X
j=1
Z
eik·rjiˆkxˆkydΩ
 
σiyτiz ˆOσjxτjz + σixτiz ˆOσjyτjz

+
1
4π
A
X
i=1
A
X
j=1
Z
eik·rjiˆkxˆkzdΩ
 
σizτiz ˆOσjxτjz + σixτiz ˆOσjzτjz

+
1
4π
A
X
i=1
A
X
j=1
Z
eik·rjiˆkyˆkzdΩ
 
σizτiz ˆOσjyτjz + σiyτiz ˆOσjzτjz

=
1
3
A
X
i=1
A
X
j=1

j0(krji) + j2(krji)(ˆr2
z + ˆr2
y −2ˆr2
x)

σixτiz ˆOσjxτjz
+
1
3
A
X
i=1
A
X
j=1

j0(krji) + j2(krji)(ˆr2
x + ˆr2
z −2ˆr2
y)

σiyτiz ˆOσjyτjz
+
1
3
A
X
i=1
A
X
j=1

j0(krji) + j2(krji)(ˆr2
x + ˆr2
y −2ˆr2
z)

σizτiz ˆOσjzτjz
−
A
X
i=1
A
X
j=1
j2(krji)ˆrxˆry

σiyτiz ˆOσjxτjz + σixτiz ˆOσjyτjz

−
A
X
i=1
A
X
j=1
j2(krji)ˆrxˆrz

σizτiz ˆOσjxτjz + σixτiz ˆOσjzτjz

−
A
X
i=1
A
X
j=1
j2(krji)ˆryˆrz

σizτiz ˆOσjyτjz + σiyτiz ˆOσjzτjz

.
(E.36)
151
5. For the angle averaged spin-transverse coupling ρστT(k) we have,
1
4π
Z
ρ†
στT(k) ˆO · ρστT(k)dΩ
=
1
4π
Z " A
X
i=1
e−ik·ri(σi × ˆk)τiz
#
ˆO ·
" A
X
j=1
eik·rj(σj × ˆk)τjz
#
dΩ
=
1
4π
A
X
i=1
A
X
j=1
Z
eik·rjiˆkxˆkxdΩ+
Z
eik·rjiˆkzˆkzdΩ

σiyτiz ˆOσjyτjz
+
1
4π
A
X
i=1
A
X
j=1
Z
eik·rjiˆkxˆkxdΩ+
Z
eik·rjiˆkyˆkydΩ

σizτiz ˆOσjzτjz
+
1
4π
A
X
i=1
A
X
j=1
Z
eik·rjiˆkyˆkydΩ+
Z
eik·rjiˆkzˆkzdΩ

σixτiz ˆOσjxτjz
−
1
4π
A
X
i=1
A
X
j=1
Z
eik·rjiˆkxˆkydΩ
 
σixτiz ˆOσjyτjz + σiyτiz ˆOσjxτjz

−
1
4π
A
X
i=1
A
X
j=1
Z
eik·rjiˆkxˆkzdΩ
 
σixτiz ˆOσjzτjz + σizτiz ˆOσjxτjz

−
1
4π
A
X
i=1
A
X
j=1
Z
eik·rjiˆkyˆkzdΩ
 
σiyτiz ˆOσjzτjz + σizτiz ˆOσjyτjz

=
1
3
A
X
i=1
A
X
j=1

2j0(krji) + j2(krji)(2ˆr2
y −ˆr2
x −ˆr2
z)

σiyτiz ˆOσjyτjz
+
1
3
A
X
i=1
A
X
j=1

2j0(krji) + j2(krji)(2ˆr2
z −ˆr2
x −ˆr2
y)

σizτiz ˆOσjzτjz
+
1
3
A
X
i=1
A
X
j=1

2j0(krji) + j2(krji)(2ˆr2
x −ˆr2
y −ˆr2
z)

σixτiz ˆOσjxτjz
+
A
X
i=1
A
X
j=1
j2(krji)ˆrxˆry

σixτiz ˆOσjyτjz + σiyτiz ˆOσjxτjz

+
A
X
i=1
A
X
j=1
j2(krji)ˆrxˆrz

σixτiz ˆOσjzτjz + σizτiz ˆOσjxτjz

+
A
X
i=1
A
X
j=1
j2(krji)ˆryˆrz

σiyτiz ˆOσjzτjz + σizτiz ˆOσjyτjz

.
(E.37)
152
