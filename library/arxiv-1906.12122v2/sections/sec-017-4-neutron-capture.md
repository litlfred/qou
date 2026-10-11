---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear effective field theory: status and perspectives"
section_id: sec-017-4-neutron-capture
section_title: "Neutron capture"
section_number: 4
pages: 36-39
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
doc_brief: "Nuclear effective field theory: status and perspectives — 34 sections: Contents; Two-body scattering amplitude; Power counting"
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.983
---
The inverse reaction of the photodissociation of one-neutron halo nuclei is
radiative neutron capture on the core nucleus, which can be relevant for a
variety of astrophysical processes.  The corresponding efforts in
Halo EFT have been reviewed by \textcite{Higa:2015yvf} and
\textcite{Rupak:2016mmz}.

One example is the radiative neutron capture on $^7$Li.  This reaction was
investigated in Halo EFT by \textcite{Rupak:2011nk}. They expressed the cross
section in terms of $n$-$^7$Li scattering parameters and showed that the LO
uncertainty comes from the poorly known $P$-wave effective range $r_1$.  The
low-energy data for this reaction can be described well by a one-parameter fit
yielding $r_1 =-1.47~\fm^{-1}$.  In subsequent work, \textcite{Fernando:2011ts}
extended this calculation to higher energies, {where} the $3^+$ resonance
becomes important.  Their results suggest a resonance width about three times
larger than the experimental value.  They also presented  power-counting
arguments that establish a hierarchy for electromagnetic one- and two-body
currents.

The radiative neutron capture on $^7$Li was refined by \textcite{Zhang:2013kja}
in an approach combining Halo EFT and \abinitio calculations.  They presented a
Halo EFT calculation that describes neutron capture to both the ground and
first excited states of $^8$Li.  Each of the possible final states were treated
as halo bound-state configurations of $^7$Li plus a neutron,
including low-lying excited states of the $^7$Li core.  The asymptotic
normalization coefficients of these bound states were taken from an \abinitio
calculation using a phenomenological potential.  In contrast to
\textcite{Rupak:2011nk}, they found good agreement with the ratio of partial
cross sections for different initial spin states.  Moreover, they obtained
excellent agreement with the measured branching rations between the two final
states.

\textcite{Rupak:2012cr} applied Halo EFT to the dominant E1 contribution to
radiative neutron capture on $^{14}$C including contributions from both
resonant and non-resonant interactions.  They found that significant
interference between these two mechanisms leads to a capture contribution that
deviates from simple Breit-Wigner resonance form.



\subsection{Proton halos}
\label{sec:phalos}

Proton halos are less common due to the delicate interplay between attraction
from the strong interaction and the Coulomb repulsion.  The presence of the
Coulomb barrier introduces the Coulomb momentum,

\begin{equation}
    \label{eq:Cb-mom}
 {k_C=Z_1 Z_2 \alpha\mu_{12}\,,}
\end{equation}

with {$Z_{1,2}$} {the particle charges and $\mu_{12}$ their reduced
mass,  as a new scale corresponding to the inverse of the Bohr radius of the
system.}  This scale is
independent of the hadronic scales and complicates the power counting
{(cf. the discussion for protons in Sec.~\ref{sec:pionless}).}
In general, the correct scaling of the Coulomb momentum with respect to
strong-interaction scales strongly depends on the system considered.
One focus of recent studies in Halo EFT has been, therefore, on the underlying
scaling relations in systems and reactions with Coulomb forces.

An EFT for $S$-wave proton halo nuclei was developed
by \textcite{Ryberg:2013iga}.  They analyzed the universal features of proton
{halos} bound due to a large $S$-wave scattering length and derived
LO expressions for the charge form factor and the radiative proton-capture
cross section.  In subsequent work~\textcite{Ryberg:2015lea} extended
the calculation to higher orders and analyzed the effect of finite-range
corrections.  They calculated the charge radius to NLO and the
astrophysical $S$-factor for low-energy proton capture to fifth order in the
low-energy expansion. Higher-order ERE parameters cannot contribute
to the E1 capture reaction, and thus the accuracy is only limited by
gauge-invariant counterterms.  As an application, \textcite{Ryberg:2015lea}
considered the $S$-factor for proton capture on $^{16}$O into the excited
$1/2^+$ state of $^{17}$F and quantified an energy-dependent model error to be
utilized in data fitting.  They also provided a general discussion of the
suppression of proton halos compared to neutron halos by the need for two fine
tunings in the underlying theory.
{\textcite{Schmickler:2019dcy,Schmickler:2019ewl} investigated
universal binding in few-body systems of up to four charged particles.
They showed that range corrections are generically enhanced in the
strong Coulomb case relevant for most nuclei.
}

The inclusion of Coulomb effects in $P$-wave halos was pioneered by
\textcite{Higa:2010zi}, who looked at low-energy $p\alpha$ scattering.
More extensive calculations were carried out later
by \textcite{Zhang:2014zsa}---extending their previous work for neutron
capture to proton halos---for $^7\mathrm{Be}(p,\gamma)^8\mathrm{B}$.
This reaction is important for analyzing solar neutrino
experiments~\cite{Adelberger:2010qa,Robertson:2012ib}.  However,
due to the Coulomb barrier it cannot be measured at the very low energies
required for this purpose and the data must be extrapolated.
\textcite{Zhang:2014zsa} demonstrated that Halo EFT together with
input from \abinitio calculations constitutes a powerful tool
to carry out this extrapolation.  They treated $^8\mathrm{B}$ as a shallow
$P$-wave bound state of a proton and a $^7\mathrm{Be}$ core and
included the first core excitation explicitly.  The couplings were fixed using
measured binding energies and $p$-$^7\mathrm{Be}$ $S$-wave scattering lengths,
together with $^8\mathrm{B}$ asymptotic normalization coefficients from
\abinitio calculations. They  emphasized the important role of
$p$-$^7\mathrm{Be}$ scattering parameters in determining the energy
dependence of $S(E)$ and demonstrated that their present uncertainties
significantly limit attempts to extrapolate the data to stellar energies.
\textcite{Zhang:2015ajn} extended this  calculation to NLO and used
Bayesian methods to determine the EFT parameters and the low-energy $S$-factor,
using measured cross sections and scattering lengths as inputs.
The results of their analysis, which reduced the uncertainty of $S(0)$ by a
factor of two, are shown in Fig.~\ref{fig:results3}.
Further details are given by \textcite{Zhang:2017yqc}.


\begin{figure}[tb]
 \centerline{\includegraphics*[width=7cm,clip=true]{paper_S}}
 \caption{Right panel: NLO $S$-factor as function of energy (solid blue
  curve). Shading indicates 68\% interval.  The dashed line gives
  the LO result.
  Left panel: 1d probability distribution functions for $S(0)$
  (blue line and histogram) and $S(20~\mathrm{keV})$ (red-dashed
  line).
  Figure taken from~\cite{Zhang:2015ajn},
  under the terms of the Creative
  Commons Attribution License,
  \url{https://creativecommons.org/licenses/by/4.0/}.
 }
 \label{fig:results3}
\end{figure}


In related work, \textcite{Ryberg:2014exa} pointed out that the charge
radius of $^8$B and the $S$-factor for $^7\mathrm{Be}(p,\gamma)^8\mathrm{B}$
are correlated at LO in Halo EFT.  This correlation thus provides indirect
access to the $S$-factor at low energies and serves as a consistency check.



\subsection{Cluster systems}
\label{sec:clusters}

Many nuclear states are close to a threshold for break-up into smaller
clusters, and are therefore amenable to an EFT approach where
these smaller clusters are the relevant degrees of freedom. For example,
several states of nuclei with $A=4 (n+1)$, $n\ge 1$ an integer,
and equal numbers of proton and neutrons are thought to be made of
alpha-particle clusters~\cite{Ikeda:1968}.  The most famous example is the Hoyle
state, the first $0^+$ excited state of $^{12}$C, which {owing} to its
position
near the $3\alpha$ threshold plays an important role in the creation of
$^{12}$C and $^{16}$O---and thus our type of life---in the universe.
Traditionally, these states have been investigated with a variety
of phenomenological approaches~\cite{Freer:2017gip}.

The first step to study these systems in Halo EFT is $\alpha\alpha$
scattering.  \textcite{Higa:2008dn} developed a power counting for
this system, which is highly fine tuned.  Due to the subtle interplay of
strong and electromagnetic forces there is a narrow resonance at an energy of
about $0.1~\MeV$, the $^8$Be ground state.  The scenario
explored by \textcite{Higa:2008dn} can be viewed as an expansion around the
limit where, when electromagnetic interactions are turned off,
the $^8$Be ground state is at threshold and exhibits conformal invariance.
This implies treating the Coulomb momentum
{$k_C=2\alpha m_\alpha\simeq 60$ MeV},
where $m_\alpha$ is the alpha particle mass,
as a high-momentum scale and expanding observables in powers of
{$Q/(3k_C)$}, where $Q$ is a typical external momentum, in addition to the
standard expansion in the strong interactions.
{The Coulomb-modified scattering length is very large, and the
corresponding effective range almost saturates the Wigner bound for charged
systems~\cite{Koenig:2012bv}.}
The corresponding phase shifts are shown
in Fig.~\ref{fig:alal_pshift} together with the experimental data
from~\cite{Afzal:1969zz} and an \abinitio lattice EFT calculation
from~\cite{Elhatisari:2015iga}.
{Agreement with data seems to extend
somewhat beyond the laboratory energy $E_{\rm Lab} = 2$ MeV corresponding
to $k_C$.}
The sharp rise in the phase shift at low
energies is {a fine-tuned effect that is}
very difficult to describe in the \abinitio calculation,
{which displays a bound state instead.  In contrast,
the \abinitio calculation extends to much higher energies than Halo EFT.}


\begin{figure}[tb]
 \centerline{\includegraphics*[width=7.0cm,clip=true]{alphaalpha2}}
 \vspace*{-0pt}
 \caption{Halo EFT results for the $\alpha\alpha$ $S$-wave phase shift
  by \textcite{Higa:2008dn} as a function of the laboratory energy $E_{Lab}$.
  LO and NLO phase shifts are given by the (blue) dashed and (red) solid lines,
  respectively. The experimental data are from~\cite{Afzal:1969zz}, while the
  lattice EFT results are from \cite{Elhatisari:2015iga}.
 }
\label{fig:alal_pshift}
\end{figure}


An RG analysis of the coupled channels $p+^7$Li and $n+^7$Be
which couple to a $2^-$ state of $^8$Be very close to the
$n+^7$Be  threshold was carried out {by \textcite{Lensky:2011he}.}
A more recent study involving $^8$Be concerned a reported anomaly in the
$e^+e^-$ production from the decay of one of the $1^+$ resonances to the ground
state. A careful {analysis inspired by Halo EFT} was carried by
\textcite{Zhang:2017zap}, who concluded that nuclear physics is unlikely to
explain the experimental result.

C and O production in stars also depends on the radiative capture of alpha
particles by $^{12}$C, $^{12}$C$(\alpha,\gamma)^{16}$O, at low energies.
As in Sec. \ref{sec:haloelectric}, parameters from
elastic $\alpha$-$^{12}$C scattering enter in a Halo EFT approach
to the capture process.  {\textcite{Ando:2016ban,Ando:2017uqc}}
developed a description of the elastic reaction taking the $^{12}$C ground state
as pointlike, and obtained asymptotic normalization coefficients
for some of the $^{16}$O states from a fit to phase shifts.

Very little has been done using Halo EFT for other cluster systems.
{An early application of Halo EFT for $l=2$ to the reaction $d + t \to n +
\alpha$ was carried out by \textcite{Brown:2013zla}.  However, they used
dimensional regularization with minimal subtraction and thus missed relevant
parameters.}  \textcite{Higa:2016igc} recently investigated another
important  process in the Sun, namely the radiative capture of an $\alpha$
particle on $^3$He.  They extracted an $S$-factor slightly above the average in
the literature, but consistent within error bars. {\textcite{Zhang:2018qhm}
recently performed a Bayesian analysis of this reaction without relying on
existing phase shift analyses {as a} constraint.}



\subsection{Outlook}
\label{sec:haloook}

In this section, we have reviewed the progress in Halo/Cluster EFT, a
short-range EFT with explicit fields for nucleon and cluster
degrees of freedom, designed for the description of halos and cluster nuclei.
Such systems have a very rich structure due to the emergence of new scales from
the Coulomb interaction between the clusters.  The Efimov effect plays an
important role for neutron halos and its application in the presence of Coulomb
interactions presents an exciting opportunity for the discovery of new
phenomena.

Halo EFT is conceptually very similar to the Pionless EFT discussed
in Sec.~\ref{sec:pionless}.  As a description of nuclei not limited to the
few-nucleon sector, it complements \abinitio approaches by parametrizing
universal relations between low-energy observables in systems dominated by
shallow bound states and low-lying resonances, and it quantifies the corrections
to these relations.  While such \abinitio calculations can be based on
interactions from Chiral EFT (which is reviewed in the following section), for
systems within its reach of applicability Halo EFT sets up a more
effective/efficient expansion.  Halo EFT promises a quantitative description
on the same footing of both nuclear structure and reactions of clusterized
systems and exotic isotopes, which is is a major challenge of contemporary
nuclear theory. {Nuclear reactions have been investigated both
in strict Halo EFT \cite{Schmidt:2018doj} as well as in accurate
phenomenological models of reactions with a Halo EFT motivated description
of the projectile \cite{Yang:2018nzr,Capel:2018kss}.}
{Many} of these reactions have impact on
astrophysical processes and even on the quantification of nuclear uncertainties
in experimental anomalies.

Future challenges include a better integration of \abinitio methods and
Halo EFT in order to maximally benefit from the strengths of both approaches.
The use of Bayesian statistics for the estimation of higher-order corrections
provides a method to account for the different sources of theory errors beyond
simple scaling arguments.  Finally, hypernuclei are a new and almost unexplored
arena for Halo EFT and universality.  {As we discuss in
Sec.~\ref{subsection:hyperchiral},} experimental data are not abundant
and a combination of Halo EFT and \abinitio methods {therefore} appears to
be especially
promising.




\section{Chiral EFT} \label{sec:chiral}

\subsection{Motivation}
\label{subsec:chiralintro}

As the typical momentum in a nuclear process increases beyond the pion mass,
pion effects can no longer be approximated by an expansion around the
zero-range limit.  As a response to the failure of early attempts to achieve
RG invariance in pion theories, an approach gradually emerged in the 1950s
where the nuclear potential and currents took purely phenomenological forms or,
at best, came from
the single (and, very occasionally, double) exchange of an arbitrary selection
of mesons.  The potential was almost always constructed so as to be regular
(\ie, not a singular potential~\cite{Frank:1971xx}), which in the case of meson
exchange was ensured by including physical form factors.  The relative ease of
solving the two-nucleon Schr\"odinger equation numerically made it possible to
produce exquisite fits to a large amount of two-nucleon data, frequently of the
same quality even with very different physical input into the potential.  In
contrast, a comparable description of $A>2$ systems seems to require
three-nucleon forces and two-nucleon currents, but the large variety of
possible structures posed a significant obstacle to this purely
phenomenological approach.  Moreover, the connection to QCD and the assignment
of systematic errors are not addressed.

Chiral EFT attempts to overcome these shortcomings by solving the RG problems
of earlier pion theories.  In hindsight, the latter were both too restrictive,
in the sense of not including all interactions consistent with symmetries,
and not restrictive enough, in the sense of not incorporating the
constraints of chiral symmetry.  Early forms of mesonic Chiral Perturbation
Theory (ChPT) date back to the 1960s and were extremely important in the
development of the EFT paradigm.  The mature version of mesonic ChPT took shape
in the 1980s~\cite{Weinberg:1978kz,Gasser:1983yg,Gasser:1984gg}, and processes
for $A=1$~\cite{Gasser:1987rb,Jenkins:1990jv,Jenkins:1991es,
Bernard:1991rq,Bernard:1991rt} and $A\ge2$~\cite{Weinberg:1990rz,Rho:1990cf,
Weinberg:1991um,Ordonez:1992xp,Weinberg:1992yk,VanKolck:1993ee} started
receiving significant attention in the late 1980s and early 1990s.  As this
section reviews, substantial progress has been made in understanding the
structure of the nuclear potential and currents, but Chiral EFT has not yet
produced a complete solution to the RG problems that plagued earlier pion
theories.

Extensive reviews exist of Chiral EFT applications to nuclear phenomenology
{by, for example, \textcite{vanKolck:1999mw,Beane:2000fx,Bedaque:2002mn,
Epelbaum:2008ga,Machleidt:2011zz,Epelbaum:2012vx}.}
We focus here on some of the conceptual
issues, which parallel those of Pionless EFT (Sec.~\ref{sec:pionless}) and
Halo/Cluster EFT (Sec.~\ref{sec:halo}).  Chiral EFT extends Pionless EFT
to processes with characteristic momentum $Q\sim \Mlo$, where $\Mlo \sim
m_\pi\ll \MQCD$.  As discussed in Sec.~\ref{subsec:chiralbasis}, the
breakdown scale $\Mhi \simle \MQCD$ depends in part on the degrees of freedom
kept explicit.  Section~\ref{subsec:chiralbasis} also discusses the pertinent
symmetries and Lagrangian.  The nuclear potential and currents, defined in
Sec.~\ref{subsec:NuclearEFTS}, are free of the IR enhancement that leads to
nuclear bound states and resonances.  As a consequence, contributions to the
potential can be treated similarly to contributions to amplitudes in ChPT, as
discussed in Sec.~\ref{subsec:chiralpot}.  The relation to experiment
\textit{via} amplitudes
{
and the more complex issue of their renormalization are}
reviewed in Sec.~\ref{subsec:chiralamps}.  Analogous considerations afflict
reactions with external light probes such as photons and pions, which are
sketched in Sec.~\ref{subsec:chiralreact}.  Section~\ref{subsec:Outissues}
lists some of the outstanding issues facing Chiral EFT.



\subsection{Basic elements}
\label{subsec:chiralbasis}
