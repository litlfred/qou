---
doc_id: arxiv-nucl-th-0103005v2
doc_title: "Quantum Monte Carlo Calculations of Light Nuclei"
section_id: sec-007-3-v-ariational-monte-carlo
section_title: "V ARIATIONAL MONTE CARLO"
section_number: 3
pages: 8-10
source_pdf: 0103005v2.pdf
source_sha256: c2aaa21b51d7bc10
doc_brief: "Quantum Monte Carlo Calculations of Light Nuclei — Accurate quantum Monte Carlo calculations of ground and low-lying excited states of light p-shell nuclei are now possible for realistic nuclear"
---
The variational method can be used to obtain approximate sol utions to the many-
body Schr¨ odinger equation, HΨ = EΨ, for a wide range of nuclear systems,
including few-body nuclei, light closed-shell nuclei, nuc lear matter, and neutron
Exact Calculations of Light Nuclei 9
stars (36). A suitably parameterized wave function, Ψ V , is used to calculate an
upper bound to the exact ground-state energy,
EV = ⟨Ψ V |H|Ψ V ⟩
⟨Ψ V |Ψ V ⟩ ≥E0 . (21)
The parameters in Ψ V are varied to minimize EV , and the lowest value is taken as
the approximate solution. Upper bounds to excited states ar e also obtainable, if
they have diﬀerent quantum numbers from the ground state, or f rom small-basis
diagonalizations if they have the same quantum numbers. The corresponding Ψ V
can be used to calculate other properties, such as particle d ensity or electromagnetic
moments, or to start a Green’s function Monte Carlo calculat ion. In this section we
describe the ansatz for Ψ V for light nuclei and brieﬂy review how the expectation
value is evaluated and the parameters of Ψ V are ﬁxed.
The best variational wave function has the form (11)
|Ψ V ⟩ =

1 +
∑
i<j<k
(Uijk +U T N I
ijk ) +
∑
i<j
U LS
ij

 |Ψ P ⟩, (22)
where the pair wave function, Ψ P , is given by
|Ψ P ⟩ =

S
∏
i<j
(1 +Uij)

 |Ψ J ⟩. (23)
The Uij, U LS
ij , Uijk , and U T N I
ijk are noncommuting two- and three-nucleon correla-
tion operators, and S is a symmetrization operator. The form of the antisymmetric
Jastrow wave function, Ψ J , depends on the nuclear state under investigation. For
the s-shell nuclei the simple form
|Ψ J ⟩ =

 ∏
i<j<k
f c
ijk(rik, rjk )
∏
i<j
fc(rij)

 |Φ A(JMTT 3)⟩ (24)
is used. Here fc(rij) and f c
ijk are central (spin-isospin independent) two- and three-
body correlation functions and Φ A is an antisymmetrized spin-isospin state, e.g.,
|Φ 3( 1
2
1
2
1
2
1
2 )⟩ = A| ↑ p ↓p ↑n⟩, (25)
|Φ 4(0000)⟩ = A| ↑ p ↓p ↑n ↓n⟩, (26)
with A the antisymmetrization operator.
The two-body correlation operators Uij andU LS
ij are sums of spin, isospin, tensor,
and spin-orbit terms:
Uij =
∑
p=2,6

 ∏
k⁄=i,j
f p
ijk (rik, rjk )

up(rij)Op
ij , (27)
U LS
ij =
∑
p=7,8

 ∏
k⁄=i,j
f p
ijk (rik, rjk )

up(rij)Op
ij , (28)
