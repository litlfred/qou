---
doc_id: arxiv-1908.07065v3
doc_title: "Prepared for submission to JHEP Non-perturbative approaches to the quantum Seiberg–Witten curve"
section_id: sec-003-31-review-of-the-tba-equations-of-gaiottomoorene
section_title: "Review of the TBA equations of Gaiotto–Moore–Neitzke"
section_number: 3.1
pages: 9-11
source_pdf: 1908.07065v3.pdf
source_sha256: c43e413aed71aef1
doc_brief: "Non-perturbative approaches to the quantum Seiberg–Witten curve — We study various non-perturbative approaches to the quantization of the Seiberg– Witten curve ofN = 2, SU (2) super Yang–Mills"
---
The TBA equations we will obtain are conformal limits [7] of the integral equations proposed
by Gaiotto–Moore–Neitzke (GMN) in [5] to describe the hyperK¨ ahler metric on the Coulomb
branch ofN = 2 theories compactiﬁed on R3× S1
R, where R is the compactiﬁcation radius. We
will now review some basic aspects of these equations which will be useful in the following. The
basic ingredients in these equations are the central charges of the N = 2 supersymmetric gauge
theory
Z(u) = (a,aD), (3.1)
where
aD = ∂F0
∂a . (3.2)
We deﬁne the period associated to a vector γ∈ Γ in the lattice of electromagnetic charges as
Zγ =Z(u)·γ. (3.3)
This is just a linear combination of A periods and B periods.
To such a central charge we associate a ray
𝓁γ =
{
ζ : Zγ(u)
ζ ∈ R−
}
. (3.4)
The semiﬂat coordinate on the Coulomb branch is given by
χsf
γ (ζ) = exp
[
πRζ−1Zγ + iθγ +πRζZγ
]
, (3.5)
where R is the compactiﬁcation radius, and
θγ =θ·γ (3.6)
is the angular coordinate on the ﬁber. The semiﬂat coordinate is the “uncorrected” or “classical”
coordinate, and it is corrected by exponentially small eﬀects in the large R limit. These eﬀects
are encoded in a non-linear, TBA-like integral equation, which reads as
χγ(ζ) =χsf
γ (ζ) exp

− 1
2πi
∑
γ′∈Γ
Ω(γ′;u)⟨γ,γ′⟩Iγ′(ζ)

, (3.7)
where Ω(γ;u) is the number of BPS states with electromagnetic charge γ at the point u of the
Coulomb branch, and
Iγ =
∫
𝓁γ
dζ′
ζ′
ζ′ +ζ
ζ′−ζ log
(
1−σ(γ)χγ(ζ′)
)
. (3.8)
Here, σ(γ) is the quadratic reﬁnement. It has been argued in [6] that, for BPS hypermulti-
plets/vectormultiplets, one has, respectively,
σ(γ) =∓1. (3.9)
We have used the normalization of [34], which is more appropriate for our normalization of
charges/periods. An important feature of (3.7) is that only those states whose charge γ′ has a
non-vanishing Dirac pairing with γ contributes to the equation of χγ(ζ). The quantities χγ(ζ)
– 8 –
characterize in a precise way the hyperK¨ ahler metric of the moduli space of the N = 2 theory
compactiﬁed on R3× S1
R, and they can be realized as cluster coordinates on this moduli space
[6]. They satisfy the property
χγ+γ′(ζ) =χγ(ζ)χγ′(ζ). (3.10)
Very often we have both charges ±γ appearing in the sum in the r.h.s. of (3.7). If θγ = 0,
we have an extra symmetry [7],
χγ(ζ) =χ−γ(−ζ), (3.11)
and we can combine
Cγ =Iγ−I−γ =
∫
𝓁γ
dζ′
ζ′
ζ′ +ζ
ζ′−ζ log
(
1−σ(γ)χγ(ζ′)
)
−
∫
𝓁−γ
dζ′
ζ′
ζ′ +ζ
ζ′−ζ log
(
1−σ(−γ)χ−γ(ζ′)
)
=
∫
𝓁γ
dζ′
ζ′
(ζ′ +ζ
ζ′−ζ− ζ′−ζ
ζ′ +ζ
)
log
(
1−σ(γ)χγ(ζ′)
)
= 4ζ
∫
𝓁γ
dζ′
(ζ′)2−ζ2 log
(
1−σ(γ)χγ(ζ′)
)
.
(3.12)
In going from the ﬁrst to the second line we have changed variables ζ′→−ζ′, and we used the
symmetry (3.11).
In order to put the equations in a form similar to the TBA equations, we will perform a
change of variables akin to the one made in [5]. If
Zγ = eiφ′
|Zγ| (3.13)
then we change variables in (3.12) as follows:
ζ =−eiφ−θ, ζ ′ =−eiφ′−θ′
, (3.14)
and we obtain
Cγ = 2
∫
R
log (1−σ(γ)χγ(θ′))
sinh(θ−θ′ + iφ′− iφ)dθ′. (3.15)
3.2 TBA equations for the modiﬁed Mathieu equation
Building on [7, 8], we expect to have a general correspondence between the mathematical descrip-
tion of BPS states in [5, 6], and the “resurgent” properties of the quantum periods associated to
the corresponding SW curve. As noted in [7], this correspondence involves the conformal limit
of the TBA equations of [5], which is given by
R→ 0 , ζ → 0 , ζ/R ﬁnite . (3.16)
In this correspondence, the classical limit of the WKB periods Π (0)
γ corresponds to the central
charge Zγ, while the full quantum period is obtained as the logarithm of the Coulomb branch
coordinatesχγ(ζ) (in the conformal limit). The Borel singularities of the Borel transformsˆΠγ are
closely related to the BPS spectrum of the theory, and the Stokes discontinuities of the quantum
periods are closely related to the so-called Kontsevich–Soibelman symplectomorphisms [5, 6, 35].
This correspondence is summarized in Table 1, and it can be used to obtain integral equations of
the TBA type governing the quantum periods. We will now apply this correspondence to obtain
such equations for the modiﬁed Mathieu operator.
– 9 –
Resurgence BPS states
WKB curve SW curve
classical limit Π (0)
γ central charge Z(γ)
quantum period Πγ cluster coordinate log χγ
Borel singularities BPS spectrum
Stokes discontinuities KS symplectomorphisms
Table 1: Correspondence between the mathematical structures in the resurgent approach to the
WKB method, and those in the theory of BPS states.
Let us then consider the SW theory [27], i.e. pure N = 2 SYM with gauge group SU (2). We
will denote the charge by
γ =γ = (ne,nm). (3.17)
We will use the conventions of [34] for the symplectic product,
⟨γ,γ′⟩ =⟨(ne,nm), (n′
e,n′
m)⟩ =−nen′
m +nmn′
e. (3.18)
We will denote
χe(ζ) =χ(1,0)(ζ), χ m(ζ) =χ(0,1)(ζ), χ d(ζ) =χ(1,1)(ζ), (3.19)
and because of (3.10) we have
χd(ζ) =χe(ζ)χm(ζ). (3.20)
We will write TBA equations for χe(ζ) and χm(ζ), as in [34]. We have
χe(ζ) =χsf
e (ζ) exp

− 1
2πi
∑
γ′
ce(γ′)Iγ′(ζ)

,
χm(ζ) =χsf
m(ζ) exp

− 1
2πi
∑
γ′
cm(γ′)Iγ′(ζ)

,
(3.21)
where
ce(γ) = Ω(γ;u)⟨(1, 0),γ⟩, c m(γ) = Ω(γ;u)⟨(0, 1),γ⟩. (3.22)
In order to write the integral equations, we need to know the structure of the BPS spectrum
in SW theory. It is known that there is a curve of marginal stability C in the Coulomb branch of
