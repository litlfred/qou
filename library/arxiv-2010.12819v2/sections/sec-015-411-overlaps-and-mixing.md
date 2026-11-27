---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-015-411-overlaps-and-mixing
section_title: "Overlaps and mixing"
section_number: 4.1.1
pages: 18-19
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
Even when taking the possibility of repeating integers into account, the above picture of scaling states and their
conjectured limits is neater than reality. An important example of a more complicated situation, which will be
relevant for the numerical results below, is as follows.
7Note: numerically, our momentum only depends one, since we have smeared out the twist.eφ instead modiﬁes the Hamiltonian
itself.
18
Consider two scaling states on the lattice with the same Sz⁄= 0,φ = 0 but with opposite electric excitations
e,−e (with e⁄= 0). By conjecture (66) these should correspond in the double limit to two primary states with
the conformal weights switched with respect to one another, so that they both have the same energy. Following
(80)-(81) and taking into account that lattice momentum is deﬁned modulo the system size, the sectors of
lattice momentum are only separated by ∆ p = 2eSz. Making holes to create the descendant states will shift
p in integer steps, and it is clear that the momentum sectors of the left descendants of one state will start
overlapping with those of the right descendants of the other state at level eSz, no matter how large we take N.
By chiral/anti-chiral symmetry there is in such cases no way to distinguish from which primary a given state
descends, and the symmetry may even force us to consider linear combinations of the scaling states as candidates
for the descendant states in the limit. We then say that there is mixing of the scaling states. To make this issue
more clear, let us specialize this example. Let V1 be the primary state corresponding to Sz = 1,e =−1 and V2
the primary state corresponding to Sz = 1,e = 1. Let W1 be the level-1 chiral descendant of V1, and let W2
denote the level-1 anti-chiral descendant of V2. The momentum sectors of W1 and W2 are the same. Within
this sector, the lowest-energy state (whose energy comes with multiplicity one within this sector) can neither
be identiﬁed with W1 nor with W2. The reason is that the energies of W1,W 2 in the limit are the same, and
“favouring” one over the other by assigning it a scaling state with lower energy would be incompatible with
the symmetry of the system, which demands that chiral and anti-chiral quantities play equal roles. Instead, we
must create W1,W 2 out of linear combinations of more than one scaling state, such that each of them has the
same contribution from the lowest-energy state. This phenomenon will be further discussed in Appendix C.1.
Since we wish to explore the indecomposable structure of the modules, the issue of mixing will be particularly
important. The reason is that a primary state with a degenerate conformal weight given by the integers e and
Sz, related to r,s as in (66), will have its null state precisely at level |eSz|, in the sector of lattice momentum
where mixing can occur.
