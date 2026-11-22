---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-050-appendix
section_title: "APPENDIX"
section_number: null
pages: 130-132
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
VARIATIONAL MONTE CARLO BRIEF
120
The time-independent Schr¨odinger equation can be written as Hψ0 = E0ψ0 if the
system is at its lowest energy E0 with wave function ψ0. We are interested in the
ground state energy E0 because a system will naturally go to its lowest energy state
ψ0. The question is how to ﬁnd ψ0 and E0.
Variational Monte Carlo(VMC), based on a trial wave function ψT (usually not
normalized) with parameters, provides a way to ﬁnd the upper limit of E0. Its foundation
is
Evar ≡⟨ψT|H|ψT⟩
⟨ψT|ψT⟩
≡
Z HψT(R)
ψT(R) |ψT(R)|2dR
Z
|ψT(R)|2dR
≡
Z
EL(R)p(R)dR ≥E0,
(A.1)
where the local energy is deﬁned as
EL(R) = HψT(R)
ψT(R) ,
(A.2)
the probability density is given by
p(R) =
|ψT(R)|2
Z
|ψT(R)|2dR
.
(A.3)
The closer ψT is to ψ0, the closer Evar is to E0 from above. For bosons ψT has to
be symmetric while for fermions ψT has to be anti-symmetric. For example, a possible
trial wave function for the system of bosons might be written in the form of
ψT(R) =
Y
i<j
f2(rij)
Y
i<j<k
f3(i, j, k)
Y
i<j<k<l
f4(i, j, k, l)...
Y
k
g(rk −rc),
(A.4)
where fn denotes the correlation function between n particles, and g(rk −rc) denotes
the correlation between the position of one particle (rk) and the system’s center of
mass(rc). For fermions, the following form (Kalos and Whitlock (2008)) may be used
as a simple example,
ψT(R) = exp

−
X
i<j
f(rij)

×

eik1·r1
eik2·r1
...
eik1·r2
eik2·r2
...
eik1·r3
eik2·r3
...
...
...
...

,
(A.5)
where ki is momentum of the particle i in three dimensional space.
The VMC trial wave function ψT usually contains some parameters which can be
adjusted to minimize Evar, so that ψT can be optimized as close to the ground state as
its structure allows. Then DMC and PIMC can be performed based on this optimized
trial wave function.
121
