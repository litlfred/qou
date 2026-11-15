---
doc_id: arxiv-2111.04763v2
doc_title: "Resurgence of Chern-Simons theory at the trivial flat connection"
section_id: sec-016-44-borel-resummation-and-stokes-constants
section_title: "Borel resummation and Stokes constants"
section_number: 4.4
pages: 42-47
source_pdf: 2111.04763v2.pdf
source_sha256: 760a7f9794e8baaa
toc_source: outline
doc_brief: "Resurgence of Chern-Simons theory at the trivial flat connection — Some years ago, it was conjectured by the first author that the Chern–Simons perturbation theory of a 3-manifold at the trivial flat"
---
Φ(σj)(τ) for j = 0, 1, 2, 3 corresponding to the trivial, the geometric, the conjugate, and
the real flat connections respectively, denoted respectively by σj for j = 0, 1, 2, 3. Similar
to the 41 knot, the asymptotic series Φ(σj)(τ) for j = 1, 2, 3 can be defined in terms of a
perturbation theory of a state-integral [KLV16, AK14] using the standard formal Gaussian
integration as explained in [DGLZ09, GGMn21], and they have been computed in [GGMn21]
with more than 200 terms. Let ξj (j = 1, 2, 3) be the roots to the algebraic equation
(1 −ξ)3 = ξ2
(184)
with numerical values
ξ1 = 0.78492 . . . + 1.30714 . . . i,
ξ2 = 0.78492 . . . −1.30714 . . . i,
ξ3 = 0.43016 . . . . (185)
The asymptotic series Φ(σj)(τ) for j = 1, 2, 3 have the universal form6
Φ(σj)(τ) = e
3πi
4
p
δj
e
Vj
2πiτ φ(σj)(τ),
j = 1, 2, 3,
(187)
where δj = 5 −3ξj + 3ξ2
j and
V1 =3Li2(ξ1) + 3/2 log(ξ1) log(1 −ξ1) −πi log(ξ1) −π2
3
V2 =3Li2(ξ2) + 3/2 log(ξ2) log(1 −ξ2) + πi log(ξ2) −π2
3 ,
V3 =3Li2(ξ3) + 3/2 log(ξ3) log(1 −ξ3) −π2
3 .
(188)
Their numerical values are given by
V1 = 3.0241 . . . + 2.8281 . . . i,
V2 = 3.0241 . . . −2.8281 . . . i,
V3 = −1.1134 . . . .
(189)
where the common absolute value of the imaginary parts of V1, V2 is the Vol(S3\52). Finally
the power series φ(σj)(τ/(2πi) have coefficients in the number field Q(ξj) and their first few
coefficients are given by
φ(σj)  τ
2πi

= 1 + 1452ξ2
j −1254ξj + 15949
23 · 3 · 232
τ + 2124948ξ2
j −2258148ξj + 11651375
27 · 32 · 233
τ 2 + . . .
(190)
The additional new series Φ(σ0)(τ) ∈Q[[τ]] corresponds to the zero volume (V (σ0) = 0)
trivial flat connection. As exlained in Section 2.3, it can be computed using the colored
6The series Φ(σj)(τ) (j = 1, 2, 3) are related to the series in [GGMn21, GGMn], which we will denote by
Φ(σj)
GGM(τ), by a common prefactor
Φ(σj)(τ) = ie−πi
12 (τ+τ −1)−2πiτΦ(σj)
GGM(τ),
j = 1, 2, 3.
(186)
The Stokes constants associated to the Borel resummation of Φ(σj)
GGM(τ) are not changed. The additional
prefactor is introduced so that the Stokes automorphism between Φ(σ0)(τ) and Φ(σj)(τ) (j = 1, 2, 3) can be
presented in an elegant form, and is also dictated by positions of singularities of Borel transform of Φ(σ0)(τ).
RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION
43
Jones polynomial or the Kashaev invariant. The first few terms are
Φ(σ0)( τ
2πi) = φ(σ0)( τ
2πi) = 1 + 2τ 2 + 6τ 3 + 157
6 τ 4 + . . .
(191)
ι0,2
ι0,1
ι0,3
ϕ(σ0)(τ)
(a)
Λ(σ0)
ι1,2
ι1,3
ϕ(σ1)(τ)
(b)
Λ(σ1)
ι2,1
ι2,3
ϕ(σ2)(τ)
(c)
Λ(σ2)
ι3,2
ι3,1
ϕ(σ3)(τ)
(d)
Λ(σ3)
Figure 6. Singularities of Borel transforms of φ(σj)(τ) for j = 0, 1, 2, 3 of the
knot 52.
We are interested in the Stokes automorphism of the Borel resummation of the 4-vector
Φ(τ) of asymptotic series
Φ(τ) =




Φ(σ0)(τ)
Φ(σ1)(τ)
Φ(σ2)(τ)
Φ(σ3)(τ)



.
(192)
First of all, the Borel transform of each asymptotic series Φ(σj)(τ) (j = 0, 1, 2, 3) has rich
patterns of singularities. Similar to the case of 41 knot discussed in Section 2.4, the Borel
transforms of Φ(σj)(τ), j = 1, 2, 3 have singularities located at
Λ(σj) = {ιj,i + 2πik | i = 1, 2, 3, i̸ = j, k ∈Z} ∪{2πik | k ∈Z̸=0},
j = 1, 2, 3
(193)
as shown in the right three panels of Fig. 6, while the Borel transform of Φ(σ0)(τ) have
singularities located at (some of these singular points are actually missing as we will comment
in the end of the section.)
Λ(σ0) = {ι0,i + 2πik | i = 1, 2, 3, k ∈Z},
(194)
as shown in the left most panel of Fig. 6, where
ιj,i = Vj −Vi
2πi
,
i, j = 0, 1, 2, 3.
(195)
44
STAVROS GAROUFALIDIS, JIE GU, MARCOS MARIÑO, AND CAMPBELL WHEELER
To any singularity located at ι(k)
i,j := ιi,j + 2πik in the union
Λ = ∪j=0,1,2,3Λ(σj),
(196)
we can associate a local Stokes matrix
Sι(k)
i,j (˜q) = I + S(k)
i,j ˜qkEi,j,
S(k)
i,j ∈Z,
(197)
where Ei,j is the 4 × 4 elementary matrix with (i, j)-entry 1 (i, j = 0, 1, 2, 3) and all other
entries zero, and S(k)
i,j is the Stokes constant. Then the Borel resummation along the rays
ρθ± raised slight above and below the angle θ are related by the Stokes automorphism
∆(τ)sθ+(Φ)(τ) = Sθ(˜q)∆(τ)sθ−(τ),
(198)
where
Sθ(˜q) =
Y
arg ι=θ
Sι(˜q),
∆(τ) = diag(τ 3/2, 1, 1, 1),
(199)
and the locality condition is assumed.
I
II
IV
III
ι1,2
ι2,1
ι3,2
ι3,1
ι1,3
ι2,3
ι0,2
ι0,1
ι0,3
Figure 7. Stokes rays and cones in the τ-plane for the 4-vector Φ(τ) of as-
ymptotic series of the knot 52.
More generally, for two rays ρθ+ and ρθ−whose arguments satisfy 0 < θ+ −θ−≤π, we
can define the global Stokes matrix Sθ−→θ+ as in (44), and it also satisfies the factorisation
property (45). Since the factorisation is unique [GGMn21, GGMn], we only need to compute
finitely many global Stokes matrices in order to extract all the local Stokes matrices associ-
ated to the infinitely many singularities in Λ and thus the corresponding Stokes constants.
In particular, we can choose four cones I, II, III, IV slightly above the positive and the
negative real axes as shown in Fig. 7, and compute the four global Stokes matrices
SI→II, SII→III, SIII→IV , SIV →I,
(200)
RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION
45
where a cone R in the subscript means any ray inside the cone.
On the other hand, each of the global Stokes matrices in (200) has the block upper trian-
gular form




1
∗
∗
∗
0
∗
∗
∗
0
∗
∗
∗
0
∗
∗
∗



.
(201)
The 3 × 3 sub-matrices Sred
R→R′ in the right bottom have been worked out in [GGMn21]. For
later convenience, we write down two of the four reduced global Stokes matrices,
Sred
I→II(˜q) = 1
2


0
1
0
0
1
1
−1
0
0

Jred
−1(˜q−1)T


0
0
1
0
−2
0
1
0
0

Jred
−1(˜q)


0
0
−1
1
−3
0
0
1
0

,
|˜q| < 1,
(202a)
Sred
III→IV (˜q) = 1
2


1
−3
0
0
1
0
0
0
−1

Jred
−1(˜q−1)T


0
0
1
0
−2
0
1
0
0

Jred
−1(˜q)


1
0
0
1
1
0
0
0
−1

,
|˜q| > 1.
(202b)
In addition, as seen from Fig. 6, there are no singularities along the positive and negative
real axes in Λ(σ0) relevant for Φ(σ0)(τ); all the singular points in Λ(σ0) are either in the upper
half plane beyond the cones I, II or in the lower half plane beneath the cones III, IV .
Consequently we only need to compute the first row of two Stokes matrices SI→II and
SIII→IV . For this purpose, we find the following.
Conjecture 20. For every cone R ⊂C \ Λ and every τ ∈R, we have
Q(2,0)
0
(q) = sR(Φ(σ0))(τ) + τ −3/2
3
X
j=1
MR,j(˜q)sR(Φ(σj))(τ),
(203)
where MR,j(˜q) (j = 1, 2, 3) are ˜q (resp., ˜q−1)-series if Imτ > 0 (resp., Imτ < 0) with integer
coefficients that depend on R.
A more elegant way to present MR,j(˜q) is by the row vector MR(˜q) := (MR,1, MR,2, MR,3)(˜q),
and it can be expressed in terms of a 3 × 3 matrix M(σ0)
R
(˜q)
MR(˜q) =

˜qQ(2,0)
0
(˜q), ˜q2Q(2,0)
1
(˜q), ˜q3Q(2,0)
2
(˜q)

M (σ0)
R
(˜q).
(204)
46
STAVROS GAROUFALIDIS, JIE GU, MARCOS MARIÑO, AND CAMPBELL WHEELER
Conjecture 21. Equation (203) holds in the cones R = I, II, III, IV where the ˜q,˜q−1-series
MR,j(˜q) are given in terms of M (0)
R (˜q) through (235) which are as follows
M (σ0)
I
(˜q) =


1
−1
−3˜q
0
−1
−1 + 3˜q
0
0
−˜q

,
(205a)
M (σ0)
II (˜q) =


−1
1
−3˜q
−1
0
−1 + 3˜q
0
0
−˜q

,
(205b)
M (σ0)
III (˜q) =


3
1
−3˜q
−1
0
−1 + 3˜q
0
0
−˜q

,
(205c)
M (σ0)
IV (˜q) =


1
3
−3˜q
0
−1
−1 + 3˜q
0
0
−˜q

.
(205d)
Eqs. (203), together with the reduced Stokes matrices Sred
R→R′(˜q) for Φ(σj)(τ) (j = 1, 2, 3),
allow us to calculate entries in the first row of SI→II(˜q) and SIII→IV (˜q) by
SR→R′(˜q)0,j = MR,j(˜q) −
3
X
k=1
MR′,k(˜q)Sred
R→R′(˜q)k,j,
j = 1, 2, 3.
(206)
In the following we list the first few terms of these ˜q and ˜q−1-series. In the upper half plane
SI→II(˜q)0,1 = −1 + 13˜q −12˜q2 −82˜q3 −29˜q4 + 85˜q5 + O(˜q6),
(207a)
SI→II(˜q)0,2 =1 −16˜q + 42˜q2 + 135˜q3 −54˜q4 −346˜q5 + O(˜q6),
(207b)
SI→II(˜q)0,3 = −˜q + 10˜q2 + 18˜q3 −31˜q4 −92˜q5 + O(˜q6).
(207c)
In the lower half plane
SIII→IV (˜q)0,1 =4˜q−1 −4˜q−2 −51˜q−3 −62˜q−4 −27˜q−5 + O(˜q−6),
(208a)
SIII→IV (˜q)0,2 =3˜q−1 + 2˜q−2 −26˜q−3 −47˜q−4 −64˜q−5 + O(˜q−6),
(208b)
SIII→IV (˜q)0,3 = −1 + ˜q−2 + 18˜q−3 + 39˜q−4 + 73˜q−5 + O(˜q−6).
(208c)
Finally, we can factorise the global Stokes matrices SI→II(˜q), SIII→IV (˜q) to obtain local
Stokes matrices associated to individual singular points in Λ and extract the associated Stokes
constants. The Stokes constants for Φ(σj)(τ) (j = 1, 2, 3) are already given in [GGMn21,
GGMn]. We collect the Stokes contants for Φ(σ0)(τ) in the generating series
S+
0,j(˜q) =
X
k≥0
S(k)
0,j ˜qk,
S−
0,j(˜q) =
X
k≤0
S(k)
0,j ˜qk,
j = 1, 2, 3.
(209)
RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION
47
And we find that in the upper half plane
S+
0,1(˜q) = −1 + ˜q + 3˜q2 + 25˜q3 + 278˜q4 + 3067˜q5 + O(˜q6),
(210a)
S+
0,2(˜q) =1 −˜q −3˜q2 −25˜q3 −278˜q4 −3067˜q5 + O(˜q6),
(210b)
S+
0,3(˜q) =0,
(210c)
while in the lower half plane
S−
0,1(˜q) =3˜q−1 −34˜q−2 + 391˜q−3 −4622˜q−4 + 54388˜q−5 + O(˜q−6),
(211a)
S−
0,2(˜q) =3˜q−1 −34˜q−2 + 391˜q−3 −4622˜q−4 + 54388˜q−5 + O(˜q−6),
(211b)
S−
0,3(˜q) = −1 + 9˜q−1 −56˜q−2 + 705˜q−3 −8378˜q−4 + 98379˜q−5 + O(˜q−6).
(211c)
We comment that the results of S+
0,3(˜q) and S−
0,3(˜q) indicate that there are actually no singular
points of the type ι(k)
0,3 in the upper half plane, but they exist in the lower half plane. Also
note that the constant terms in S+
0,1(˜q), S+
0,2(˜q) and S−
0,3(˜q) are Stokes constants associated to
the singular points ι0,j (j = 1, 2, 3). The Stokes constants associated to ιi,j (i, j = 1, 2, 3, i̸ =
j) have already been computed in [GGMn21, GGMn]. We can assemble all these Stokes
constants in a matrix




0
−1
1
−1
0
0
4
3
0
−4
0
−3
0
−3
3
0




(212)
which matches (after some changes of signs) the one appearing in [GZb, Eq.(40)].
