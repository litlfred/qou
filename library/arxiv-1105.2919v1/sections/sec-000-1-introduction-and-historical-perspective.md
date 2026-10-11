---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral effective field theory and nuclear forces"
section_id: sec-000-1-introduction-and-historical-perspective
section_title: "Introduction and historical perspective"
section_number: 1
pages: 4-7
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
doc_brief: "Chiral effective field theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
text_source: latex
latex_prose_ratio: 0.794
latex_coverage_ratio: 1.0
---
The theory of nuclear forces has a long history (cf.\ Table~\ref{tab_hist}).
Based upon the seminal idea by Yukawa~\cite{Yuk35}, 
first field-theoretic attempts
to derive the nucleon-nucleon ($NN$) interaction
focused on pion exchange.
While the one-pion exchange turned out to be very useful
in explaining $NN$ scattering data and, in particular, the properties
of the deuteron~\cite{Sup56}, 
multi-pion exchange was beset with
serious ambiguities~\cite{TMO52,BW53}
that could not be resolved in a satisfactory way.
Thus, the ``pion theories'' of the 1950s
are generally judged as failures---for reasons
we understand today: pion dynamics is constrained by chiral
symmetry, a crucial point that was unknown in the 1950s.

Historically, the experimental discovery of heavy 
mesons~\cite{Erw61} in the early 1960s
saved the situation. The one-boson-exchange (OBE)
model~\cite{Sup67,BS64,Erk74,HM75,NRS78,Mac89} emerged, which still today is the most economical
and quantitative
phenomenology for describing the 
$NN$ interaction~\cite{Sto94,Mac01,GS08}.
The weak point of this model, however, is the scalar-isoscalar
``sigma'' or ``epsilon'' boson, for which empirical
evidence remains controversial. Since this boson is associated
with the  correlated (or resonant) exchange of two pions,
a vast theoretical effort 
was launched to derive the 2$\pi$-exchange contribution
of the nuclear force, which creates the intermediate-range attraction.
During this effort, which occupied more than a decade,
dispersion theory 
(Stony Brook~\cite{JRV75,BJ76} and Paris~\cite{Vin79,Lac80} potentials) 
as well as field theory 
(Partovi-Lomon model~\cite{PL70}, Bonn potential~\cite{Mac89,MHE87})
were invoked.

The nuclear force problem appeared to be solved; however,
with the discovery of quantum chromo-dynamics (QCD), 
all ``meson theories'' were
relegated to the status of models and the attempts to derive
the nuclear force had to start all over again.

The problem with a derivation of nuclear forces from QCD is that
this theory is non-perturbative in the low-energy regime
characteristic of nuclear physics, which makes direct solutions
very difficult.
Therefore, during the first round of new attempts, QCD-inspired quark 
models~\cite{Tar80,Har81,OY81,Fae83,Tho83,MW88,TSY89,Bar93,EFV00,Wu00,Dow10} 
became popular. 
The positive aspect of these models is that they try to explain hadron structure
and hadron-hadron interactions on an equal footing and, indeed, 
some of the gross features of the $NN$ interaction are explained successfully.
However, on a critical note, it must be pointed out
that these quark-based
approaches are nothing but
another set of models and, thus, do not represent
fundamental progress. 
For the purpose of describing hadron-hadron interactions, 
one may equally well stay
with the simpler and much more quantitative meson models.

A major breakthrough occurred when 
the concept of an effective field theory (EFT) was introduced
and applied to low-energy QCD.
As outlined by Weinberg in a seminal paper~\cite{Wei79},
one has to write down the most general Lagrangian consistent
with the assumed symmetry principles, particularly
the (broken) chiral symmetry of QCD. At low energy, the effective degrees of freedom are pions 
(the Goldstone bosons of the broken symmetry) and
nucleons rather than quarks and gluons; heavy mesons and
nucleon resonances are ``integrated out''.
So, the circle of history is closing and we are {\it back to Yukawa's meson (pion) theory},
except that we have finally learned how to deal with it:
broken chiral symmetry is a crucial constraint that generates
and controls the dynamics and establishes a clear connection
with the underlying theory, QCD.


\begin{table}[t]
\caption{The Theory of Nuclear Forces:
Seven Decades of Struggle
\label{tab_hist}} 
\smallskip
\begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}ll}
\hline 
\hline 
\noalign{\smallskip}
\bf 1935   &
\bf Yukawa: Meson Theory
\\
\noalign{\smallskip}
\hline
\noalign{\smallskip}
\bf 1950's &            
{\it The ``Pion Theories''.}
\\
          &
One-pion exchange: good;
multi-pion exchange: disaster.
\\
\noalign{\smallskip}
\hline
\noalign{\smallskip}
\bf 1960's & 
Many pions $\equiv$ multi-pion resonances:
{\boldmath $\sigma$, $\rho$, $\omega$, ...}
\\
           & 
The One-Boson-Exchange Model: success.
\\
\noalign{\smallskip}
\hline
\noalign{\smallskip}
\bf 1970's & 
Divers two-pion-exchange models: 
\\
   &
Partovi-Lomon, Stony Brook, Paris, Bonn.
\\
\noalign{\smallskip}
\hline
\noalign{\smallskip}
\bf 1980's &  
Nuclear physicists discover {\bf QCD}:
\\
           & Quark Models.
\\
\noalign{\smallskip}
\hline
\noalign{\smallskip}
\bf 1990's & 
Nuclear physicists discover {\bf EFT}; Weinberg, van Kolck, \ldots
\\
\bf and beyond &
{\bf Back to Meson (Pion) Theory!} {\it But, constrained by Chiral Symmetry.}
\\
\noalign{\smallskip}
\hline
\hline
\end{tabular*}
\vspace*{0.5cm}
\end{table}



The idea of chiral symmetry has an interesting history of its own.
The modern understanding is that this symmetry arises because the up and
down quarks happen to have relatively small masses.
However, chiral symmetry and its significance for low-energy hadron (pion)
physics was discovered long before QCD.
In 1960, based upon concepts proposed by Schwinger~\cite{Sch57},
Gell-Mann and Levy~\cite{GL60} developed the sigma model, which is
a linear realization of chiral symmetry.\footnote{For a pedagogical introduction into chiral symmetry
and the sigma model, see~\cite{EW88}.}
One major problem researchers had been struggling with in the 1950's was that the pion-nucleon
scattering length came out two orders of magnitude too
large when the (renormalizable) pseudo-scalar ($\gamma_5$) $\pi N$ interaction was used.
This unrealistic prediction was due to very large contributions from
virtual anti-nucleon states (the so-called ``pair terms'' or ``Z-graphs''). Similar problems
occurred in the $2\pi$-exchange contribution to the $NN$ interaction. 
In the sigma model, the large pair terms are canceled by processes
involving the (fictitious) $\sigma$ boson. In this way, the linear sigma model
demonstrates how imposing chiral invariance fixes the problem with low-energy
$\pi$-$N$ scattering. However, the fictitious character of the $\sigma$ particle as well as 
the reliance on the perfect
cancelation of huge terms are uncomfortable features.
In 1967, motivated by the current algebra approach to soft pion physics,
Weinberg~\cite{Wei67} worked out what has become known as the non-linear sigma model, which
does not include a $\sigma$ anymore and has pions and nucleons interact via pseudo-vector
(derivative, $\gamma_5 \gamma^\mu \partial_\mu$) 
coupling besides a new (non-linear) $\pi\pi NN$ term also involving a derivative
(``Weinberg-Tomozawa term''~\cite{Wei66,Tom66}).
The derivative (equivalent to momentum) guarantees that the interaction vanishes when the momentum goes to zero providing a natural explanation for the weakness of the interaction by
soft pions  which does not rely on the cancelation of large terms. 
Following suggestions by Schwinger, Weinberg~\cite{Wei68} developed, soon after, 
a general theory of non-linear realizations
of chiral symmetry, which was further generalized in an elegant way by
Callan, Coleman, Wess, and Zumino~\cite{CCWZ}.


Even though the original work on chiral symmetry was obviously all performed by particle physicists, 
it must be stated---to the honor of nuclear physics---that 
there have been some far-sighted nuclear physicists who early on
understood and appreciated the significance of chiral symmetry for low-energy hadron
interactions. One of them was Gerry Brown, who as early as 1968 published with two co-workers
a paper~\cite{BGG68} on three-nucleon forces, where the consequences of chiral symmetry are fully
exploited.  In 1970, Brown wrote a remarkable Comment~\cite{Bro70} and, in 1979, he published
a book chapter entitled ``Chiral symmetry and the nucleon-nucleon
interaction''\cite{Bro79}.
Moreover, in the more sophisticated relativistic meson models of the 
past~\cite{MHE87,FT80,BM84,GOH92}
the pseudo-vector coupling was applied in $\pi NN$ vertices (instead of the simpler pseudo-scalar
one that was commonly in use) in recognition of chiral symmetry.
However, this chiral patch work, even though it points into the right direction,
cannot be perceived as a serious chirally invariant theory.
Moreover, one has to face the problem that the derivative coupling is not renormalizable
in the conventional sense. 

Therefore, ideas were still needed for how
to implement chiral symmetry consistently in the theory of pionic and nuclear interactions
and how to deal with the renormalization issue.
In his contribution to the `Festschrift' in honor of Schwinger of 1979~\cite{Wei79,Wei09}, Weinberg proposed
to consider the most general possible Lagrangian including all higher-derivative 
terms that are consistent
with chiral symmetry (besides the other commonly accepted symmetry principles).
For this theory to be manageable, one needs to assume some sort of perturbative
expansion such that only a finite number of terms contribute at a given order.
This expansion is provided by powers of small external momenta over the chiral symmetry
breaking scale, $\Lambda_\chi \sim 1$ GeV. The higher-derivative terms supply the counterterms
that make possible an order-by-order renormalization, which is the appropriate renormalization 
procedure for an effective field theory.
Weinberg's suggestions were soon picked up  
by Gasser, Leutwyler, and associates who worked out, to one loop, the cases of 
$\pi\pi$~\cite{GL84} and $\pi N$ scattering~\cite{GSS88} with great success.

But there was still the problem of the nuclear force which is more difficult, 
since nuclear interactions do not vanish in the chiral limit ($q\rightarrow 0$; $m_{u/d}, m_\pi \rightarrow 0$)
and require a non-perturbative
treatment because of the existence of nuclear bound states.
In a series of papers published around 1990~\cite{Wei90,Wei91,Wei92}, 
Weinberg picked up the nuclear force issue and suggested to calculate the $NN$ potential
perturbatively in the chiral expansion and then iterate it to all orders in a 
Schroedinger or Lippmann-Schwinger
equation to obtain the nuclear amplitude. 
Here, the introduction of four-nucleon contact terms is crucial for renormalization.

Following the Weinberg proposal, pioneering
work was performed by Ord\'o\~nez, Ray, and
van Kolck \cite{ORK94,ORK96} who applied time-ordered perturbation theory to
construct a $NN$ potential up to next-to-next-to-leading order (NNLO).
The results were encouraging and nuclear EFT quickly developed into one of the most popular
branches of modern nuclear physics.
The Munich group used covariant perturbation theory and dimensional regularization
to calculate the perturbative
$NN$ amplitude without~\cite{KBW97} and 
with $\Delta(1232)$-isobar degrees of freedom~\cite{KGW98} at NNLO.
Besides this, the Munich group worked out important loop contributions of
higher order~\cite{Kai00a,Kai00b,Kai01,Kai01a,Kai01b}.
A relativistic approach was also taken by the Brazil group~\cite{RR94,RR03}.
The Bochum-J\"ulich group devised
a method of unitarity transformations to eliminate the energy-dependence of 
time-ordered perturbation theory amplitudes and calculated 
the $NN$ potentials up to NNLO~\cite{EGM98,EGM00}.
The Idaho group managed to construct a chiral $NN$ potential
at next-to-next-to-next-to-leading order (N$^3$LO) and showed that only at
this order can one achieve the precision necessary for reliable few-nucleon
and nuclear structure calculations~\cite{EM02a,EM02,EM03,ME05}.
Progress extended beyond the $NN$ interaction, as nuclear many-body forces based 
upon chiral perturbation theory were also developed~\cite{Wei92,Kol94,Epe02b,IR07,Ber08}.

During the past decade or so,
chiral two-nucleon forces have been used in many microscopic calculations of
nuclear reactions and structure~\cite{DF07,Cor02,Cor05,Cor10,NC04,FNO05,Kow04,DH04,Wlo05,Dea05,Gou06,Hag08,Hag10,FOS04,FOS09} 
and the combination of chiral two- and three-nucleon forces has been applied in
few-nucleon reactions~\cite{Epe02b,Erm05,Kis05,Wit06,Ley06,Ste07,KE07,Mar09,Kie10,Viv10},
structure of light- and medium-mass nuclei~\cite{Nog06,Nav07,Hag07,Ots09},
and nuclear and neutron matter~\cite{Bog05,HS09}---with a great deal of success.
The majority of nuclear structure calculations is nowadays based upon chiral forces.

Consequently, it may be of interest to the community
to have a good understanding of these forces
and their background.
It is therefore the purpose of this report to provide an accessible review 
on how nuclear forces emerge from low-energy QCD via chiral effective field theory.
A pedagogical introduction into the phenomenology and the traditional
view of nuclear forces can be found in Refs.~\cite{Mac89,MS01}.
Alternative reviews on various aspects of the modern perspective are published in Refs.~\cite{Kol99,BK02,Epe06,EHM09}.

This article is organized as follows.
In Section~\ref{sec_EFT}, we sketch the foundations of an EFT for low-energy
QCD including the effective Lagrangians. Section~\ref{sec_overview} provides an overview
on nuclear forces derived from chiral EFT. The two-nucleon force is then discussed in detail in Section~\ref{sec_2NF}
and many-body forces in Section~\ref{sec_manyNF}. 
The extension of the theory through the introduction of $\Delta(1232)$-isobar degrees of freedom
and higher order contributions to nuclear forces are considered in Section~\ref{sec_delta}.
Finally, Section~\ref{sec_concl} contains our conclusions.
The appendices provide many mathematical details which may be useful to researchers
who wish to start working in the field.


\section{Effective field theory for low-energy QCD
\label{sec_EFT}}

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
