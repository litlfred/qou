---
doc_id: arxiv-1908.07065v3
doc_title: "Prepared for submission to JHEP Non-perturbative approaches to the quantum Seiberg–Witten curve"
section_id: sec-004-321-strong-coupling-region
section_title: "Strong coupling region"
section_number: 3.2.1
pages: 11-15
source_pdf: 1908.07065v3.pdf
source_sha256: c43e413aed71aef1
doc_brief: "Non-perturbative approaches to the quantum Seiberg–Witten curve — We study various non-perturbative approaches to the quantization of the Seiberg– Witten curve ofN = 2, SU (2) super Yang–Mills"
---
region or chamberW outsideC [27, 36, 37]. As we move from the strong coupling region to the
weak coupling region, the spectrum of BPS states changes drastically by the famous wall-crossing
phenomenon. We consider the two chambers in turn.
3.2.1 Strong coupling region
We start with the regionW inside the curve of marginal stability. The spectrum consists of one
monopole with charge
γm = (0, 1) (3.23)
– 10 –
and one dyon with charge
γd = (1, 1), (3.24)
see [27, 36, 37] (we follow the conventions in [36]). We also have the corresponding antiparticles,
carrying opposite charges. Then, the only nonzero coeﬃcients in (3.21) are
ce(γm) =ce(γd) =−1, c m(γd) = 1. (3.25)
Therefore, the equations (3.21) read
χe(ζ) =χsf
e (ζ) exp
[ 1
2πi (Cγm +Cγd)
]
,
χm(ζ) =χsf
m(ζ) exp
[
− 1
2πiCγd
]
,
(3.26)
and it is better to write them in terms of χd, χm,
χd(ζ) =χsf
d (ζ) exp
[ 1
2πiCγm
]
,
χm(ζ) =χsf
m(ζ) exp
[
− 1
2πiCγd
]
.
(3.27)
We now write the central charges
Zd = eiφd|Zd|, Z m =−ieiφm|Zm|. (3.28)
These conventions are such that, when u∈ R inside the curve of marginal stability, we have
φd = φm = 0. Let us deﬁne the functions ϵd,m and ~ϵd,m(θ) as follows (this is similar to the
notation used in [8, 38]):
χd
(
−eiφd−θ
)
= exp (−ϵd(θ− iφd)) = exp (−~ϵd(θ)),
χm
(
ieiφm−θ
)
= exp (−ϵm(θ− iφm)) = exp (−~ϵm(θ)).
(3.29)
Then, the conformal limit of the TBA equations reads:
~ϵd(θ) =π|Zd|eθ− 2
∫
R
~Lm(θ′)
cosh(θ−θ′ + iφm− iφd)
dθ′
2π,
~ϵm(θ) =π|Zm|eθ− 2
∫
R
~Ld(θ′)
cosh(θ−θ′ + iφd− iφm)
dθ′
2π,
(3.30)
where we have shifted θ→θ− logR, and
~Lm,d(θ) = log
(
1 + e−~ϵm,d(θ)
)
. (3.31)
We have used here the fact that the BPS spectrum consists of hypermultiplets, therefore σ(γ) =
−1.
The equations simplify further when u is real, i.e. u∈ R∩W = [−1, 1]. Then one has
φd =φm = 0, i.e.
Zγd > 0, Z γm =−i|Zγm|, (3.32)
– 11 –
and we obtain,
ϵd(θ) =π|Zd|eθ− 2
∫
R
Lm(θ′)
cosh(θ−θ′)
dθ′
2π,
ϵm(θ) =π|Zm|eθ− 2
∫
R
Ld(θ′)
cosh(θ−θ′)
dθ′
2π.
(3.33)
We also note that, before taking the conformal limit, we ﬁnd the more conventional TBA equa-
tions
ϵd(θ) =πrZd cosh(θ)− 2
∫
R
Lm(θ′)
cosh(θ−θ′)
dθ′
2π,
ϵm(θ) =πr|Zm| cosh(θ)− 2
∫
R
Ld(θ′)
cosh(θ−θ′)
dθ′
2π,
(3.34)
where
r = 2R. (3.35)
The deﬁnition of r is such that we have the same conventions as in [39].
The TBA equations simplify greatly when u = 0. In this case, we have that
|Zd| =|Zm| =ξ, (3.36)
and that1
ϵd(θ) =ϵm(θ) =ϵ(θ). (3.37)
The two TBA equations collapse to one,
ϵ(θ) =πξeθ− 2
∫
R
L(θ′)
cosh(θ−θ′)
dθ′
2π, (3.38)
which coincides with the integral equation (B.19) associated to the modiﬁed Mathieu equation
and the Sinh-Gordon model and studied by Zamolodchikov (the factor ξ can be absorbed in
a redeﬁnition of the angle θ). The equation (3.38) was written down in [7] as governing the
quantum periods at u = 0.
We claim that the functions ~ϵd,m(θ) are identiﬁed with quantum periods as follows
~ϵd(x + iφd) = 1
ℏs(ΠD)(ℏ),
~ϵm
(
x + iφm− iπ
2
)
= 1
ℏs(ΠB)(ℏ),
(3.39)
with
ℏ =π−1e−x, ΠD = ΠA + ΠB , (3.40)
where ΠD denotes the dyonic quantum period. Then the TBA equations (3.30) are consistent
with the leading order contribution by the classical periods in the small ℏ expansion
s(ΠD,B)(ℏ) =Zd,m +O(ℏ2) . (3.41)
Furthermore, the TBA equations (3.30) clearly indicate that for some argument angles of ℏ the
quantum periods have discontinuities. These discontinuities are determined by the BPS spectrum
1Anticipating the identiﬁcation with quantum periods, this equation does not mean that the dyonic and mag-
netic quamtum periods ΠD(u, ℏ), ΠB(u, ℏ) are identical at u = 0, as ℏ is identiﬁed with θ diﬀerently, c.f. (3.39).
– 12 –
terms lateral Borel sum r.h.s. of (3.42)
181 0.17499253901611 0.1749925390148815032360
185 0.17499253901578 0.1749925390148815032482
189 0.17499253901545 0.1749925390148815032553
193 0.174992539015 19 0.17499253901488150325 95
Table 2: Discontinuity across the ray arg( ℏ) = 0 for Π B(u = 0, ℏ = 1) computed by lateral
Borel resummation and by using (3.42) with increasing number of terms in the asymptotic series.
Underlined are stabilised digits.
of SW theory and give the singularity structure of the Borel transform of the quantum periods.
These Stokes discontinuities can also be deduced from (3.30). The location of the singularities
in the Borel plane, as well as the precise discontinuities, can be checked against the asymptotic
series of the quantum periods, by inspecting the Borel plane and by performing lateral Borel
resummations, respectively.
For instance, from the TBA equations (3.30), we conclude that s(ΠB) are discontinuous
across the rays arg( ℏ) =φd,φd +π, with
discφd(+π)(ΠB)(ℏ) = + 2ℏ log
(
1 + e− 1
ℏs(ΠD)(ℏ)
)
=2ℏ
(
e− 1
ℏs(ΠD)(ℏ)− 1
2e−2 1
ℏs(ΠD)(ℏ) +...
)
. (3.42)
When u = 0, we have φd = 0, and the discontinuities are located at arg( ℏ) = 0 ,π . The
discontinuity across the ray arg( ℏ) = 0 can be computed by a lateral Borel resummation of the
quantumB period. We check it against the right hand side of (3.42), and ﬁnd good agreement.
See Table 2. Similarly, s(ΠD) is discontinuous across the rays arg( ℏ) =φm± π
2 , and one has
discφm±π
2
(ΠD)(ℏ) =−2ℏ log
(
1 + e− 1
ℏs(ΠB)(ℏ)
)
. (3.43)
Numerical checks for this discontinuity formula are completely analogous.
From the discontinuity formula (3.42) we can deduce in the standard way a formula for the
large order behavior of Π (n)
B , of the form (see e.g. [40])
iΠ(n)
B ∼ 2A−2n+b
π Γ(2n +b)
·
(
1− µ2A
2n +b− 1 + µ3A2
(2n +b− 1)(2n +b− 2)− µ4A3
(2n +b− 1)(2n +b− 2)(2n +b− 3)···
)
.
(3.44)
If we write the dyonic quantum period as
ΠD =
∑
n≥0
Π(n)
D ℏ2n, (3.45)
we can identify
A = Π(0)
D , b =−1, µ 2 = Π(1)
D , µ 3 = (Π(1)
D )2/2, µ 4 = (Π(1)
D )3/6 + Π(2)
D , ... (3.46)
– 13 –
These identities are numerically checked at u = 0 up to all stabilised digits (more than 40) with
the help of Richardson transforms.
The large order behavior of Π (n)
B also indicates that the Borel transform ˆΠB(ζ) has branch
points at ζ =±Π(0)
D , which is the central charge of the BPS state (dyon) whose electromagnetic
charge has non-vanishing Dirac pairing with the charge of the monopole. Similarly, the Borel
transform of ΠA(u, ℏ) should have branch points at the central charges of monopoles and dyons
with electromagnetic charges±(0, 1),±(1, 1), while the Borel transform of ΠB(u, ℏ) have branch
points only at the central charges of dyons. This explains the Borel plane plots in Figure 1,
where we also superimpose the central charges of the contributing BPS states as red spots.
