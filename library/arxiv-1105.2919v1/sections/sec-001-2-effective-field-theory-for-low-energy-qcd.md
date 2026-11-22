---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral eﬀective ﬁeld theory and nuclear forces"
section_id: sec-001-2-effective-field-theory-for-low-energy-qcd
section_title: "Effective field theory for low-energy QCD"
section_number: 2
pages: 6-7
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.918
latex_coverage_ratio: 1.0
doc_brief: "Chiral eﬀective ﬁeld theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
---
Quantum chromodynamics (QCD) is the theory of strong interactions.
It deals with quarks, gluons and their interactions and is
part of the Standard Model of Particle Physics.
QCD is a non-Abelian gauge field theory
with color $SU(3)$ the underlying gauge group.
The non-Abelian nature of the theory has dramatic
consequences. While 
the interaction between colored objects is weak 
at short distances or high momentum transfer
(``asymptotic freedom'');
it is strong at long distances ($\gea 1$ fm) or low energies,
leading to the confinement of quarks into colorless
objects, the hadrons. Consequently, QCD allows for a 
perturbative analysis at large energies, whereas it is
highly non-perturbative in the low-energy regime.
Nuclear physics resides at low energies and
the force between nucleons is
a residual color interaction
similar to the van der Waals force between neutral molecules.
Therefore, in terms of quarks and gluons, the nuclear force
is a very complicated problem that, nevertheless, can be attacked
with brute computing power on a discretized, Euclidean space-time lattice
(known as lattice QCD). In a recent study~\cite{Bea06}, the neutron-proton scattering lengths
in the singlet and triplet $S$-waves have been determined in fully dynamical
lattice QCD, with a smallest pion mass of 354 MeV. This result is then extrapolated
to the physical pion mass with the help of chiral perturbation theory. The pion mass
of 354 MeV is still too large to allow for reliable extrapolations, but the feasibility has been
demonstrated and more progress can be expected for the near future.
In a lattice calculation of a very different kind, the nucleon-nucleon ($NN$) potential
was studied~\cite{IAH07,Ino10}.
The $NN$ potential is extracted from the equal-time Bethe-Salpeter
amplitude with local interpolating operators for the nucleons. The central part of the
potential shows a repulsive core plus attraction of intermediate range. This is a very promising
result, but it must be noted that also in this investigation still rather large pion masses are being used.
In any case, advanced lattice QCD calculations are under way and continuously improved. 
However, since these calculations are very time-consuming
and expensive, they can only be used to check a few representative key-issues. For everyday
nuclear structure physics, a more efficient approach is needed. 

The efficient approach is an effective field theory.
For the development of an EFT, it is crucial to identify a separation of
scales. In the hadron spectrum, a large gap between the masses of
the pions and the masses of the vector mesons, like $\rho(770)$ and $\omega(782)$,
can clearly be identified. Thus, it is natural to assume that the pion mass sets the soft scale, 
$Q \sim m_\pi$,
and the rho mass the hard scale, $\Lambda_\chi \sim m_\rho$, also known
as the chiral-symmetry breaking scale.
This is suggestive of considering an expansion in terms of the soft scale over the hard scale,
$Q/\Lambda_\chi$.
Concerning the relevant degrees of freedom, we noticed already that,
for the ground state and the
low-energy excitation spectrum of
an atomic nucleus as well as for conventional nuclear
reactions,
quarks and gluons are ineffective degrees of freedom,
while nucleons and pions are the appropriate ones.
To make sure that this EFT is not just another phenomenology,
it must have a firm link with QCD.
The link is established by having the EFT observe
all relevant symmetries of the underlying theory.
This requirement is based upon a `folk theorem' by
Weinberg~\cite{Wei79}:
\begin{quote}
If one writes down the most general possible Lagrangian, including {\it all}
terms consistent with assumed symmetry principles,
and then calculates matrix elements with this Lagrangian to any given order of
perturbation theory, the result will simply be the most general possible 
S-matrix consistent with analyticity, perturbative unitarity,
cluster decomposition, and the assumed symmetry principles.
\end{quote}
In summary, the EFT program consists of the following steps:
\begin{enumerate}
\item
Identify the soft and hard scales, and the degrees of freedom appropriate
for (low-energy) nuclear physics.
\item
Identify the relevant symmetries of low-energy QCD and
investigate if and how they are broken.
\item
Construct the most general Lagrangian consistent with those
symmetries and symmetry breakings.
\item
Design an organizational scheme that can distinguish
between more and less important contributions: 
a low-momentum expansion.
\item
Guided by the expansion, calculate Feynman diagrams
for the problem under consideration
to the desired accuracy.
\end{enumerate}
In the following (sub)sections,
we will elaborate on these steps, one by one.
Since we discussed the first step already, we will address now step two.
