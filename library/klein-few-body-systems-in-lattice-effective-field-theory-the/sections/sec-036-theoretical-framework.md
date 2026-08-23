---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Few-body systems in lattice effective field theory"
section_id: sec-036-theoretical-framework
section_title: "Theoretical framework"
section_number: null
pages: 69-70
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
doc_brief: "Few-body systems in lattice effective field theory — 58 sections: Introduction and Motivation; The standard model of particle phy; Lattice QCD"
---
In the four-body system, we do not have any new operator as our system should be describable by the
2NFs and 3NFs only. As the four-body system scales with L9, an exact calculation at suﬃcient large
lattices is not practical anymore, and hence we have to use Monte Carlo methods. More precisely, we
use auxiliary ﬁeld Monte Carlo with the hybrid Monte Carlo algorithm [33]. In the following we will
deﬁne the LO auxiliary ﬁeld transfer matrix which we will minimize afterwards. All other contributions
are calculated perturbatively. For an increased convergence we prepare our trial states using a SU(4)
symmetric Hamiltonian
H0 = Hfree + 1
2C0
∑
⃗n1,⃗n2
fSU(4)
(⃗n1−⃗n2
)ρ(⃗n1
)ρ(⃗n2
), (5.59)
with fSU(4)(⃗n1−⃗n2) a Gaussian smearing function. This operator is used to eﬃciently create trial states
which are close to realistic nuclei,
⏐⏐⏐ψ4He
⟩
= exp(−t0H0
)⏐⏐⏐ψ0
⟩, (5.60)
where|ψ0⟩ is the antisymmetrized free-particle solution for 4He in a ﬁnite volume. The correlation
function at Euklidean time t is deﬁned as
Z4He (t) =
⟨
ψ4He| exp(−tHLO)|ψ4He
⟩
, (5.61)
where HLO = Hfree + HLO,contact + HOPE is the full LO Hamiltonian according to Eqs. (5.1,5.3,5.7), and
|ψ4He⟩ is the antisymmetrized wave function of the nucleons given by Eq. (5.61). The above-mentioned
expression can be calculated using auxiliary ﬁeld Monte Carlo methods for diﬀerent time steps and the
63
