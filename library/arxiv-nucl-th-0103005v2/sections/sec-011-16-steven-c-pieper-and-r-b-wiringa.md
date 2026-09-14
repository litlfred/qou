---
doc_id: arxiv-nucl-th-0103005v2
doc_title: "Quantum Monte Carlo Calculations of Light Nuclei"
section_id: sec-011-16-steven-c-pieper-and-r-b-wiringa
section_title: "Steven C. Pieper and R. B. Wiringa"
section_number: 16
pages: 16-18
source_pdf: 0103005v2.pdf
source_sha256: c2aaa21b51d7bc10
doc_brief: "Quantum Monte Carlo Calculations of Light Nuclei — Accurate quantum Monte Carlo calculations of ground and low-lying excited states of light p-shell nuclei are now possible for realistic nuclear"
---
in spin-isospin space, deﬁned as
Gαβ(R, R′) = ⟨R,α |e−(H−E0)△τ |R′,β ⟩. (40)
It is calculated with leading errors of order ( △τ )3. Omitting the spin-isospin indices
α, β for brevity, Ψ( Rn,τ ) is given by
Ψ( Rn,τ ) =
∫
G(Rn, Rn−1) · · ·G(R1, R0)Ψ T (R0)dRn−1 · · ·dR1dR0 , (41)
with the integral being evaluated stochastically.
The short-time propagator should allow as large a time step △τ as possible,
because the total computational time for propagation is pro portional to 1 /△τ .
Earlier calculations (17, 3, 42) used the propagator obtain ed from the Feynman
formulae in which the kinetic and potential energy terms of H are separately ex-
ponentiated. The main error in this approximation to Gα,β comes from terms in
e−H△τ having multiplevij, like vijKv ij(△τ )3, where K is the kinetic energy, which
can become large when particles i and j are very close due to the large repulsive
core in vij. This requires a rather small △τ ∼ 0.1 GeV −1.
It has been found in studies of bulk helium atoms (43) that inc luding the exact
two-body propagator allows much larger time steps. This sho rt-time propagator is
Gαβ(R, R′) = G0(R, R′)⟨α|

S
∏
i<j
gij(rij, r′
ij)
g0,ij(rij, r′
ij)

 |β⟩, (42)
where
G0(R, R′) = ⟨R|e−K△τ |R′⟩ =
[ √
m
2π¯h2△τ
] 3A
exp
[
−(R − R′)2
2¯h2△τ/m
]
, (43)
gij is the exact two-body propagator,
gij(rij, r′
ij) = ⟨rij|e−Hij △τ |r′
ij⟩, (44)
and g0,ij is the free two-body propagator. All terms containing any nu mber of the
same vij and K are treated exactly in this propagator, as we have included t he
imaginary-time equivalent of the full two-body scattering amplitude. It still has er-
rors of order ( △τ )3, however they are from commutators of terms like vijKv ik(△τ )3
which become large only when both pairs ij and ik are close. Because this is a
rare occurrence, a ﬁve times larger time step, △τ ∼ 0.5 GeV −1, can be used (18).
Including the three-body forces and the E0 in Eq.(40), the complete propagator
is given by
Gαβ(R, R′) = eEo△τG0(R, R′) exp[−
∑
(V R
ijk (R) +V R
ijk (R′)) △τ
2 ]
⟨α|I3(R)|γ⟩⟨γ|

S
∏
i<j
gij(rij, r′
ij)
g0,ij(rij, r′
ij)

 |δ⟩⟨δ|I3(R′)|β⟩, (45)
Exact Calculations of Light Nuclei 17
where
I3(R) =
[
1 − △τ
2
∑
V π
ijk (R)
]
. (46)
and V π
ijk =V 2π
ijk +V 3π
ijk represents, in general, all non-central Vijk terms. With the
exponential of V π
ijk expanded to ﬁrst order in △τ , there are additional error terms
of the form V π
ijkV π
i′j′k′(△τ )2. However, they have negligible eﬀect because V π
ijk has
a magnitude of only a few MeV.
Quantities of interest are evaluated in terms of a “mixed” ex pectation value
between Ψ T and Ψ( τ ):
⟨O⟩Mixed = ⟨Ψ T |O|Ψ(τ )⟩
⟨Ψ T |Ψ(τ )⟩
=
∫
dPnΨ †
T (Rn)OG(Rn, Rn−1) · · ·G(R1, R0)Ψ T (R0)
∫
dPnΨ †
T (Rn)G(Rn, Rn−1) · · ·G(R1, R0)Ψ T (R0)
, (47)
where Pn = R0, R1, · · ·, Rn denotes the ‘path’, and dPn =dR0dR1 · · ·dRn with
the integral over the paths being carried out stochasticall y. The desired expectation
values would, of course, have Ψ( τ ) on both sides; by writing Ψ( τ ) = Ψ T +δΨ(τ )
and neglecting terms of order [ δΨ(τ )]2, we obtain the approximate expression
⟨O(τ )⟩ = ⟨Ψ(τ )|O|Ψ(τ )⟩
⟨Ψ(τ )|Ψ(τ )⟩ ≈ ⟨O(τ )⟩Mixed + [⟨O(τ )⟩Mixed − ⟨O⟩T ] , (48)
where ⟨O⟩T is the variational expectation value. More accurate evalua tions of
⟨O(τ )⟩ are possible (44), essentially by measuring the observable at the mid-point
of the path. However, such estimates require a propagation t wice as long as the
mixed estimate and require separate propagations for every ⟨O⟩ to be evaluated.
The nuclear calculations published to date use the approxim ation of Eq.(48).
A special case is the expectation value of the Hamiltonian. T he ⟨H(τ )⟩Mixed can
be re-expressed as (45)
⟨H(τ )⟩Mixed = ⟨Ψ T |e−(H−E0)τ /2He −(H−E0)τ /2|Ψ T ⟩
⟨Ψ T |e−(H−E0)τ /2e−(H−E0)τ /2|Ψ T ⟩ ≥E0 , (49)
since the propagator exp[ −(H −E0)τ ] commutes with the Hamiltonian. Thus
⟨H(τ )⟩Mixed approaches E0 in the limit τ → ∞ , and the expectation value obeys
the variational principle for all τ .
The A V18 interaction contains terms that are quadratic in or bital angular mo-
mentum, L. These terms are, in essence, state- and position-dependen t modiﬁca-
tions of the mass of the nucleons. If they are included in the c alculation of gij,
then the ratio gij/g0,ij in Eq.(43) becomes unbounded for large |rij| or |r′
ij| and the
Monte Carlo statistical error will also be unbounded. Hence the GFMC propaga-
tor is constructed with a simpler isoscalar interaction, H ′, with a v′
ij that has only
