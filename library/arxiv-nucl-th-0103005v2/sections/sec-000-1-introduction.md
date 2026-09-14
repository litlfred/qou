---
doc_id: arxiv-nucl-th-0103005v2
doc_title: "Quantum Monte Carlo Calculations of Light Nuclei"
section_id: sec-000-1-introduction
section_title: "INTRODUCTION"
section_number: 1
pages: 1-4
source_pdf: 0103005v2.pdf
source_sha256: c2aaa21b51d7bc10
doc_brief: "Quantum Monte Carlo Calculations of Light Nuclei — Accurate quantum Monte Carlo calculations of ground and low-lying excited states of light p-shell nuclei are now possible for realistic nuclear"
---
HAMILTONIAN AND CURRENTS . . . . . . . . . . . . . . . . . . . . . . . . . . .4
V ARIATIONAL MONTE CARLO . . . . . . . . . . . . . . . . . . . . . . . . . . . .8
GREEN’S FUNCTION MONTE CARLO . . . . . . . . . . . . . . . . . . . . . . . .15
ENERGY RESULTS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .20
DENSITY AND MOMENTUM DISTRIBUTIONS . . . . . . . . . . . . . . . . . . .27
Annu. Rev. Nucl. and Part. Science 2001 1 1056-8700/97/0610 -00
LOW-ENERGY NUCLEON-NUCLEUS SCATTERING . . . . . . . . . . . . . . . .35
ASTROPHYSICAL ELECTROWEAK REACTIONS . . . . . . . . . . . . . . . . .36
NEUTRON DROPS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .39
CONCLUSIONS AND OUTLOOK . . . . . . . . . . . . . . . . . . . . . . . . . . . .39
1 INTRODUCTION
A major goal of nuclear physics is to understand the stabilit y, structure, and re-
actions of nuclei as a consequence of the interactions betwe en individual nucleons.
This is an extremely challenging many-body problem, exacer bated by the fact that
we do not know in detail what the interactions are. Quantum ch romodynamics,
the fundamental theory for strong interactions, is so diﬃcu lt to solve in the non-
perturbative regime of low-energy nuclear physics that no o ne is currently able
to quantitatively describe the interactions between two nu cleons from ﬁrst princi-
ples. However, we do have a tremendous amount of experimenta l data on nucleon-
nucleon (NN) scattering and we can construct accurate representations of NN
interactions by means of two-body potentials. These potent ials are complicated,
depending on the relative positions, spins, isospins, and m omenta of the nucle-
ons, which makes the problem of ﬁnding accurate quantum-mec hanical solutions
of many-nucleon bound and scattering states a demanding tas k. Nevertheless, a
variety of precise calculations have been carried out for th e three- and four-nucleon
systems which reveal an additional complication: two-nucl eon forces alone are in-
adequate to quantitatively explain either the bound-state properties or a variety
of Nd and Nt scattering data. This is not surprising, because meson-exc hange
theory and the composite nature of nucleons indicate that ma ny-nucleon forces,
at least three-nucleon forces, are important. However, the se are even more diﬃ-
cult to construct from ﬁrst principles. In like manner, meso n-exchange introduces
two-body charge and current operators, and calculations of electroweak transitions
show that these are also necessary to achieve agreement with data.
Despite these diﬃculties, tremendous progress has been mad e in the past decade,
both in the characterization of nuclear forces and currents , and in the development
of accurate many-body techniques for evaluating them. A mul tienergy partial-
wave analyses of elastic NN scattering data below Tlab = 350 MeV was produced
by the Nijmegen group in 1993 (1), which demonstrated that ov er 4300 data points
could be ﬁt with a χ2 per datum ≈ 1. This was achieved by careful attention to
the known long-range part of the NN interaction and a rigorous winnowing of
inconsistent data. Their work inspired the construction of a number of new NN
potential models which gave comparably good ﬁts to the datab ase.
Concurrently, several essentially exact methods have been developed for the
study of few-nucleon ( A = 3,4) systems with such realistic NN potentials. The
ﬁrst accurate, converged calculations of three-nucleon ( NNN) bound states were
2
Exact Calculations of Light Nuclei 3
obtained by conﬁguration-space Faddeev methods in 1985 (2) , while the ﬁrst accu-
rate 4He bound states were obtained by the Green’s function Monte C arlo method
in 1987 (3). Other methods of comparable accuracy have been d eveloped since then
for both A = 3,4 bound states and for NNN scattering. A comprehensive review
of many aspects of the few-nucleon problem can be found in the article by Carlson
and Schiavilla (4). The result of all the progress in the last decade is that we
have obtained an excellent understanding of few-nucleon sy stems, including both
structure and reactions, although a few unanswered problem s remain.
Until recently, nuclei larger than A = 4 have been described within the frame-
work of the nuclear shell model or mean-ﬁeld pictures such as Skyrme models.
The classic description of p-shell (5 ≤ A ≤ 16) nuclei was developed by Cohen
and Kurath in the 1960s (5). In that work, a large number of exp erimental levels
were ﬁt in terms of a relatively small number of two-body matr ix elements, but no
direct connection was made to the underlying NN force. Beginning with the work
of Kuo and Brown (6), approximate methods for relating the sh ell-model matrix
elements to the underlying forces were developed and applie d to even larger nuclei.
However, in most calculations, only the valence nucleons, i .e., the nucleons in the
last unﬁlled shell, are treated as active, while the core is i nert. Recently the ﬁrst
”no-core” shell model calculations, in which all the nucleo ns are active, have been
made in the p-shell with eﬀective interactions that have been derived by a G-matrix
procedure from a realistic underlying NN force (7). These calculations agree with
the other exact methods for the A = 3, 4 nuclei, but fully-converged calculations
for larger systems have not yet been obtained.
The present article focuses on recent developments in quant um Monte Carlo
methods that are making the light p-shell nuclei accessible at a level of accuracy
close to that obtained for the s-shell ( A ≤ 4) nuclei. The quantum Monte Carlo
methods include variational Monte Carlo (VMC) and Green’s function Monte Carlo
(GFMC) methods. The VMC is an approximate method (8,9,10,11 ) that is used as
a starting point for the more accurate GFMC calculations. Be cause of its relative
simplicity, the VMC has also been used to make ﬁrst studies of various reactions,
such as the nuclear response to electron (12, 13) or pion scat tering (14), and for
electroweak capture reactions of astrophysical interest ( 15,16). The GFMC is exact
in the sense that binding energies can be calculated with an a ccuracy of better
than 2%; it has been used to compute ground states and low-lyi ng excitations
of all the A ≤ 8 nuclei (3, 17, 18, 19). These studies of light p-shell nucle i have
shown that nuclear structure can be predicted from the eleme ntary nuclear forces.
As presently implemented, both the VMC and GFMC methods requ ire signiﬁcant
additional computer resources for every nucleon added, so t hey probably will be
limited to systems of A ≤ 12 nuclei. A new method, whose accuracy lies between
that of the VMC and GFMC methods, is auxiliary-ﬁeld diﬀusion M onte Carlo
(AFDMC); it has been implemented for large pure neutron syst ems (20) and with
further development should be capable of handling nuclei ab oveA = 12.
Most of the calculations discussed here have been made using Hamiltonians con-
