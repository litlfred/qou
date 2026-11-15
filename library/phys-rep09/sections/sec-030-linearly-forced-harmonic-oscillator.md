---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-030-linearly-forced-harmonic-oscillator
section_title: "Linearly forced harmonic oscillator"
section_number: null
pages: 44-45
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
For the linearly driven harmonic oscillator, the procedure yields the exact solution, as in the preceding Section 4.1.2,
albeit the method is a bit more technically involved [120].
4.2.2. Rosen–Zener model
Following [122] we will deal with the Rosen–Zener model (see Section 4.1.2 and [15]) since it allows a clear illustration
of the adiabatic regime.
The preliminary linear transformation G(s) defined in (94) for the Hamiltonian (202) is given by G(s) = ˆb · σ, where the
unit vector ˆb points in the direction b = ˆa+ ˆk (ˆk = unit vector along the z-axis). Remember that s = t/T is the dimensionless
time-variable. The evolution operator then gets factorized as
UG(s) = GĎ(s)U(s)G(s0),
(205)
which, according to (90), satisfies the equation
dUG
ds = ˜HG(s)UG.
(206)
Here ˜HG ≡−iHG/¯h is given by
˜HG(s) =
T
i¯h
aσ3 −iθ′
2 σ2,
(207)
with a2 = E2
0 + V 2
0 / cosh2 s and cot θ = (E0/V0) cosh s.
Next, in analogy to (203), we introduce the Adiabatic Interaction Picture which allows us to integrate the diagonal piece
of ˜HG(s). The time-evolution operator gets eventually factorized as
UG(s) = exp

(−iT/¯h)
Z ∞
0
ds′ a(s′)σ3

U(I)
G (s) exp

(−iT/¯h)
Z 0
−∞
ds′ a(s′)σ3

,
(208)
where U(I)
G (s) obeys the equation
dU(I)
G
ds
= ˜H(I)
G (s)U(I)
G ,
(209)
with
˜H(I)
G (s) = −i(θ′/2)[σ1 sin A(s) + σ2 cos A(s)],
(210)
and
A(s) =
2T
¯h
Z s
0
ds′ a(s′) = ξ
2
ln
1 + ρ
1 −ρ +
2γ
π
arctan
2γ
πξ ρ.
(211)
We have introduced the definition
ρ = {1 −[1 + (πξ/2γ )] sin2 θ}1/2,
(212)
in terms of the dimensionless strength parameter γ = πV0T/¯h and θ. Using the ME to first order in the adiabatic basis
(which coincides with the fixed one at s = ±∞), one finds the spin-flip approximate (first order) transition probability
adP(1)
M = sin2
Z θ0
0
dθ sin A(s(θ))

.
(213)
In Fig. 8 we compare the numerical results given by the new approximation (213) with the exact formula Pex in (204). For
the sake of illustration, we also plot the results in the usual Interaction Picture to first order in ME (see P(1)
M
in (204)). The
gain achieved when using the adiabatic ME in the intermediate regime (i.e., moderate values of ξ) is of note, although only
the first order is considered. Here, the adiabatic regime corresponds to large values of ξ = 2ET/¯h (ε = 1/T ≪1).
It should also be noted that, for the Hamiltonian (210) one has
Z s
s0
∥˜H(I)
G (s1)∥2ds1 =
1
2|θ(s) −θ(s0)| <
1
2
2π = π
and thus the convergence condition given by Theorem 9 is always satisfied. In other words, for this example the Magnus
expansion is always convergent in the Adiabatic Interaction Picture.
More involved illustrative examples of ME in the Adiabatic Picture may be found in [120,123].
S. Blanes et al. / Physics Reports 470 (2009) 151–238
195
Fig. 8. Rosen–Zener model: Transition probability as a function of ξ, with γ = 1. The solid line stands for the exact result in (204). The remaining lines
stand for first order computations with ME (circles) and perturbation theory (triangles). Open symbols are for the Adiabatic Picture and solid symbols for
the Interaction Picture.
