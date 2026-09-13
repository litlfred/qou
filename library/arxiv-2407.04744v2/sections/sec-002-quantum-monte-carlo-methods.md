---
doc_id: arxiv-2407.04744v2
doc_title: "Magnetic structure of A≤ 10 nuclei using the Norfolk nuclear models with quantum Monte Carlo methods G. Chambers-Wall 1,∗ A. Gnech 2,3,† G. B. King 1,‡ S"
section_id: sec-002-quantum-monte-carlo-methods
section_title: "Quantum Monte Carlo methods"
section_number: null
pages: 2-3
source_pdf: 2407.04744v2.pdf
source_sha256: fc6fda3138296fb1
doc_brief: "Magnetic structure of A≤ 10 nuclei using the Norfolk nuclear models with quantum Monte Carlo methods G. Chambers-Wall 1,∗ A. Gnech 2,3,† G. B. King 1,‡ S — 21 sections: Front matter; Theory; Introduct"
---
Quantum Monte Carlo (QMC) approaches [50] are a
suite of computational methods used to stochastically
solve the Schr¨ odinger equation
HΨ(Jπ;T,Tz) =EΨ(Jπ;T,Tz) , (1)
where Ψ(Jπ;T,Tz) is a nuclear wave function with spe-
cific spin-parity Jπ, isospin T , and charge state Tz. The
Hamiltonian has the form
H =
X
i
Ki +
X
i<j
vij +
X
i<j<k
Vijk , (2)
whereKi is the non-relativistic kinetic energy andvij and
Vijk are respectively two- and three-nucleon potentials.
The QMC approach of this work is a two-step pro-
cess that begins with the variational Monte Carlo (VMC)
method. In nuclear VMC calculations, the variational
ansatz taken for the many-body wave function is [51]
|ΨT⟩ =S
Y
i<j

1 +Uij +
X
i<j̸=k
eUTNI
ijk

|ΨJ⟩ (3)
whereS is the symmetrization operator, Uij is a two-
body correlation operator, eUTNI
ijk is a three-body cor-
relation operator, and Ψ J is a Jastrow-like wave func-
tion. The antisymmetric state ΨJ encodes the long-range
structure of the system and is constructed by acting on a
Slater determinant that places nucleons in s- and p-shell
orbitals with correlation functions that encode the appro-
priate cluster structure (e.g., 6Li∼α +d) of the system.
The design of the two- and three-body correlation func-
tions in Eq. 3 reflects the influence of the short-distance
nuclear interaction in the medium. The correlation oper-
ators contain embedded variational parameters that one
then optimizes to find a best variational state, Ψ V , by
minimizing the expectation value
EV = ⟨ΨV|H|ΨV⟩
⟨ΨV|ΨV⟩ ≥E0 (4)
where E0 is the true ground state energy of the system.
The VMC result is then further improved upon by us-
ing the Green’s function Monte Carlo (GFMC) method.
The method leverages the fact that the real time ( t)
Schr¨ odinger Equation
i∂
∂t|Ψ(t)⟩ = (H−ET )|Ψ(t)⟩ , (5)
may be recast as a diffusion equation in imaginary time
τ =it
− ∂
∂τ|Ψ(τ)⟩ = (H−ET )|Ψ(τ)⟩ , (6)
whereET is an energy offset that controls the normaliza-
tion of the wave function. Noting that one may expand
any state in a complete orthonormal basis, we can write
ΨV as a sum of the true eigenstatesψi of the Hamiltonian
|ΨV⟩ =
∞X
i=1
ci|ψi⟩ . (7)
From Eq. (6), if the energy offset ET is taken to be the
exact energy of the ground state E0, it is clear that in
the limit τ→∞
lim
τ→∞
e−(H−E0)τ|ΨV⟩∝ c0ψ0, (8)
3
making it possible to project the true ground state out of
ΨV . In practice, the propagation is performed in n small
steps in imaginary time ∆τ,
|Ψ(τ)⟩ =
h
e−(H−E0)∆τ
in
|ΨV⟩ , (9)
until spurious contamination is removed from the wave
function and convergence is reached.
In this work, we will study matrix elements of oper-
atorsO acting on the VMC wave function. To obtain
expectation values in GFMC, we compute the so-called
“mixed-estimate,”
⟨O(τ)⟩≈ 2⟨ΨV|O|Ψ(τ)⟩
⟨ΨV|Ψ(τ)⟩ − ⟨ΨV|O|ΨV⟩
⟨ΨV|ΨV⟩ , (10)
derived assuming the GFMC wave function atτ is a small
improvement over the VMC state; i.e., Ψ(τ) = ΨV +δΨ.
Since the variational wave functions are typically good
descriptions of light nuclei, this a valid approximation.
In principle, it is possible to calculate a matrix element
between two propagated states in GFMC; however, this
requires performing separate imaginary time propaga-
tions for each matrix element that one would like to com-
pute [52], which makes an order-by-order analysis of the
magnetic moments and form factors quite costly. Thus,
the mixed estimate is a necessary approximation to sys-
tematically analyze the convergence ofχEFT predictions
for the magnetic structure of nuclei over a range of mo-
menta.
