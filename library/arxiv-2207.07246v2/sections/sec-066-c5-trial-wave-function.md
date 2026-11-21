---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-066-c5-trial-wave-function
section_title: "C.5 Trial Wave Function"
section_number: null
pages: 149-150
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
Trial Wave Function
The trial wave function used in AFDMC for the N-particle system has the following
form,
ψT(R, S) = ΦS(R)ΦA(R, S),
(C.38)
where R ≡(r1, ..., rN) are the spatial coordinates and S ≡(s1, ..., sN) are the spin-
isospin part of the system. For example si can be written as
si =



ai
bi
ci
di


= ai|p ↑⟩+ bi|p ↓⟩+ ci|n ↑⟩+ di|n ↓⟩,
(C.39)
where ai, bi, ci and di are complex coeﬃcients for each basis.
The ΦS(R) is composed of the Jastrow two-particle correlation functions and is
given by
ΨS(R) =
Y
i<j
fJ(rij),
(C.40)
where fJ is taken from the scalar component of the correlation operator ˆFij in the
Fermi-Hyper-Netted-Chain in the Single Operator Chain approximation (FHNC/SOC).
The antisymmetric part of the trial wave function depends on the particular system to
be studied. The general form is given by the non-interacting fermion wave functions
in the Slater determinant,
ΦA(R, S) = A
N
Y
i=1
φα(ri, si) = det[φα(ri, si)],
(C.41)
where α is a set of quantum numbers of single-particle wave function. It can be label
as α = {n, j, mj} such that
φα(ri, si) = Rn,j(ri)[Yl,ml(Ω)χs,ms(si)]j,mj,
(C.42)
where Rn,j is a radial function, Yl,ml are spherical harmonics and χs,ms are spinor part.
For uniform inﬁnite nuclear matter, we can simulate the system by putting the N
particles in the periodic box of volume L3, and the single-particle function is given by
the plane wave,
φα(ri, si) = eikα·riχs,ms(si),
(C.43)
with integers nαx, nαy, nαz, and the quantized momentum vector is given by
kα = 2π
L (nαx, nαy, nαz).
(C.44)
139
APPENDIX D
