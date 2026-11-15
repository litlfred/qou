---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear eﬀective ﬁeld theory: status and perspectives"
section_id: sec-005-c-nuclear-efts
section_title: "C Nuclear EFTs"
section_number: null
pages: 6-8
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.992
doc_brief: "Nuclear eﬀective ﬁeld theory: status and perspectives — 82 sections: Nuclear effective field theory: st; Contents; I Introduction"
---
\label{subsec:NuclearEFTS}

The implementation of these ideas in nuclear physics has posed some unexpected 
challenges.  They can be traced to the fact that at LO some interactions need 
to be fully iterated---or, equivalently, a dynamical equation should be solved 
exactly---in order to produce the bound states and resonances that we refer to 
as nuclei.  

Nuclear EFTs typically include fields for the nucleon or clusters of nucleons.
These particles have masses of $\OO(\MQCD)$, and the expansion~(\ref{Texp})
includes a $Q/m_N$ expansion around the nonrelativistic limit.  Creation of 
{virtual} heavy particle-antiparticle pairs takes place at small distances 
$r\simle 1/(2m_N)$ and its effects can be absorbed in the LECs.  As a 
consequence, a process involving $A$ heavy particles is not affected by 
interactions in Eq.~\eqref{Lexp} involving more than $2A$ fields associated with
these heavy particles.  The simplest way to incorporate the fact that the
(large) particle rest energy does not play any role is to employ a ``heavy
field'' from which the trivial evolution factor due to the rest energy is 
removed~\cite{Jenkins:1990jv}.  Lorentz invariance for these fields is encoded 
in ``reparametrization invariance''~\cite{Luke:1992cs}.  Kinetic terms reduce
to the standard nonrelativistic form {that respects Galilean invariance}, 
with relativistic corrections {suppressed by inverse powers of $m_N$}
appearing at higher orders.

There is a crucial difference between $A= 1$ and $A\ge 2$ 
processes.  The former processes involve also light particles (\eg, photons) in 
initial and final states with momenta $Q\sim \Mlo$.  They deposit on the 
nucleon an energy of $\OO(Q)$ which is larger than the recoil of 
$\OO(Q^2/(2m_N))$, so that the nucleon is essentially static---deviation from 
the static limit can be treated as a perturbation.  Intermediate states differ 
in energy from the initial state by an amount of $\OO(Q)$.  In contrast, there 
are Feynman diagrams for the $T$ matrix of an $A\ge 2$ process---whether it 
involves external probes or not---that include intermediate states which differ 
in energy from the initial state only by a small difference in nucleon kinetic 
energies of $\OO(Q^2/(2m_N))$.  In these ``reducible'' diagrams nucleons are 
not static, and there is an infrared (IR) enhancement relative to intermediate 
states for $A= 1$ processes~\cite{Weinberg:1991um}.  Nucleon recoil cannot be 
treated perturbatively, although relativistic corrections remain small.

The ``full'' nuclear potential $V$ is defined as the sum of irreducible diagrams
for a process involving $A$ nucleons in initial and final states.  The full $T$ 
matrix~\eqref{Texp} is obtained by sewing potential subdiagrams with nucleon 
lines representing the free $A$-body Green's function $G$.  This gives rise to
the Lippmann-Schwinger equation, schematically

\begin{equation}
 T = V + \int V G T = V + \int V G V + \cdots \,,
\label{LS}
\end{equation}

or alternatively to the Schr\"odinger equation and its many-body relatives.  The
full potential so defined involves all $A$ bodies but it includes components
with $1\le C\le A-1$ separately connected pieces.  Frequently the potential is
thought of as one of these connected pieces.  One thus defines the ``$A$-nucleon
($AN$) potential'' as the sum of diagrams with $C=1$ in the $A$-nucleon system.
For $A=2$ all diagrams in the nuclear potential are connected ($C=1$), but
starting at $A=3$ multiply connected diagrams appear, \ie, the full potential is
made up of a sum of fewer-body potentials.  Diagrams with $C=A-1$ are made out
of the $2N$ potential and $A-2$ disconnected nucleon lines.  Diagrams in the
full potential that have $1< C <A-1$ are made of combinations of lower-$A$
potentials and disconnected nucleon lines.

In contrast to phenomenological models, all mesons with masses $\simge \MQCD$
and nucleon excitations heavier than the nucleon by the same amount can be
integrated out because their effects can be captured by the LECs.  As we are
going to see in Sec.~\ref{sec:pionless}, in Pionless EFT the potential consists
purely of contact interactions, while in Chiral EFT pion exchanges are present
as well (Sec.~\ref{sec:chiral}).  In either case, the potential involves small
transfers of energy $\OO(Q^2/(2m_N))$, and the total exchanged four-momentum is
close to the total transferred three-momentum.  Dependence on the latter
translates into a function of the position in coordinate space---the potential
is local.  Meanwhile, dependence on other nucleon momenta leads to derivatives
with respect to position, \ie, the momentum operator in quantum mechanics---the
potential becomes nonlocal.  We expect to be able to expand the potential
in momentum space analogously to Eq.~\eqref{Texp},

\begin{multline}
{
 V(Q,\Lambda) = \sum_{\mu= 0}^\infty V^{(\mu)}(Q,\Lambda)
 = \tilde {\mathcal{N}} 
 \sum_{\mu= 0}^\infty \, 
 \left(\frac{Q}{\Mhi}\right)^{\!\mu}} \\
 {\null\times
 \tilde{F}^{(\mu)}\!\left(\frac{Q}{\Mlo};\frac{Q}{\Lambda};
 \tilde{\gamma}^{(\mu)}\!\left(\frac\Mlo\Mhi,\frac\Lambda\Mhi\right)  
\right) \,,}
\label{Vexp}
\end{multline}

where $\tilde{\mathcal{N}}$ is a normalization factor,\footnote{Note that, in 
the units we use, the momentum-space potential, like the $T$ matrix, has mass 
dimension $-2$.  Its Fourier transform, which involves three powers of momentum,
has mass dimension $+1$, as it should.} the $\tilde{F}^{(\mu)}$ are functions 
obtained from irreducible diagrams, the $\tilde \gamma^{(\mu)}=\OO(1)$ are 
dimensionless combinations of the $c_i$, and $\mu$ is a counting index for the 
potential.

When the nucleus is disturbed by low-momentum external probes (photons, leptons,
perhaps pions), similar considerations apply.  One can define nuclear currents
(or reaction kernels) as the sum of irreducible diagrams to which the probes are
attached.  Again, currents involve all $A$ nucleons but include disconnected
diagrams.  A subtlety is that a probe can deposit an energy $\OO(Q)$ on a
nucleon line, and thus there can be purely nucleonic intermediate states in
irreducible diagrams.  Observables come from the sandwich of currents between
wavefunctions of the initial and final states.  Currents have an expansion
similar to Eq.~\eqref{Vexp}.

The nuclear potential and associated currents can always be defined as such 
intermediate quantities between $\LL$ and $T$.  We have reduced the EFT to a
quantum-mechanical problem, but one in which the form of the potential and
currents is determined.  This is a distinct improvement over a purely
phenomenological approach, particularly in what concerns the bewildering variety
of many-body potentials and currents one can construct.
{This feature is one of the major reasons for
the dominant role nuclear EFTs play nowadays in the nuclear theory community.}

However, one should keep in mind that the potential and currents are not
directly observable.  There are important differences between Eqs.~\eqref{Vexp}
and~\eqref{Texp}:

\begin{itemize}

\item
The potential does not need to obey an equation such as~\eqref{TRGtrunc}. 
EFT potentials involve terms that are singular and often attractive, in the 
sense of diverging faster than $-1/(4m_Nr^2)$ as the relative position 
$r\to 0$.  The potential would generate strong regulator dependence in 
Eq.~\eqref{LS} integrals if it did not itself depend strongly on 
$\Lambda${, see, \eg,} {a pedagogical discussion by
\textcite{Lepage:1997cs}.}

\item
Since after renormalization $\Lambda$ disappears from $T$ (apart from 
arbitrarily small terms),

\begin{equation}
 \int V G V\sim \frac{Q^3}{4\pi} \frac{m_N}{Q^2} V^2\sim \frac{m_NQ V}{4\pi}V
\label{VGV}
\end{equation}

and the expansion~\eqref{LS} is in the dimensionless ratio $m_N Q
V/(4\pi)$~\cite{Bedaque:2002mn}.  For $Q\simge 4\pi/(m_N V^{(0)})$, $F^{(0)}$ in
Eq.~\eqref{Texp} stems from an infinite iteration of the LO potential
$V^{(0)}$.  This is good, because nuclear bound states and resonances, as poles
of $T$ matrices, can only be obtained from a nonperturbative LO.

\item
Equations~\eqref{Vexp} and~\eqref{LS} do \emph{not} imply that all terms in 
$V$ should be treated on the same footing.  One cannot immediately identify
$\mu$ with $\nu$ because a term in $V$ contributes to various orders in the $T$ 
matrix.  Higher-order $F^{(\nu>0)}$ can be obtained from $V^{(\mu>0)}$ in a
distorted-wave Born expansion: $F^{(1)}$ from a single insertion of $V^{(1)}$,
$F^{(2)}$ from a single insertion of $V^{(2)}$ or two insertions of $V^{(1)}$, 
and so on.  Treating the potential truncated at a subleading order 
exactly---\ie, treating it as a phenomenological potential---is in general 
not correct from a renormalization point of view.  In an expansion in $Q$,
the potential gets more and more singular with increasing order.  Resumming a 
partial subset of higher-order terms will in general not include all the LECs
needed for proper renormalization.\footnote{{
An example of resummation of higher-order interactions is found in lattice
implementations of Nonrelativistic QCD (NRQCD)~\cite{Thacker:1990bm}.
In Heavy Quark Effective Theory (HQET) all $Q/m_Q$ corrections in the heavy 
quark mass $m_Q$ are treated perturbatively, and lattice simulations have
a continuum limit~\cite{Sommer:2010ic}.  For NRQCD, lattice practice is to treat
exactly not only heavy quark recoil but also the associated, subleading gluon
interactions.  Thus, only for relatively large values of the lattice spacing $a$
do observables look like they might converge, before $1/a$-type effects take 
over.  There are also situations where one can resum higher-order interactions
without introducing essential regulator dependence. An example is given by
\textcite{Lepage:1997cs}.}}

\end{itemize}

The age-long challenge in nuclear physics has been to achieve RG invariance 
when some interactions are nonperturbative and yet some others can be treated 
as small.  In an EFT, that translates into the nontrivial task of developing a 
power counting that guarantees  Eqs.~\eqref{Ttrunc} and~\eqref{TRGtrunc}.
In a purely perturbative context the cutoff dependence of loops can be obtained 
analytically.  Assuming naturalness and looking at individual loop diagrams, 
a simple rule has been devised for the size of the LECs needed for perturbative
renormalization~\cite{Manohar:1983md,Georgi:1986kr}.  This ``na\"ive dimensional
analysis'' (NDA) states that, for an operator $O_i$ in Eq.~\eqref{Lexp} with
canonical dimension $D_i$ involving $N_i$ fields $\psi$,

\begin{equation}
 c_i = \OO\left(\frac{(4\pi)^{N_i-2}}{\MQCD^{D_i-4}}\,
 c_{i {\text{red}}}\right) \,,
\label{NDA}
\end{equation}

where the dimensionless ``reduced'' LEC $c_{i \text{red}}$ is of the order 
of the combination of {reduced} QCD parameters that give rise to it.  
Examples for Chiral
Perturbation Theory are given in Sec.~\ref{sec:chiral}.  It is, however, not
immediately obvious that NDA applies to LECs of operators involving four or
more nucleon fields {subject to nonperturbative renormalization, \ie, 
which} {are renormalized once LO interactions are resummed.}
In
fact, as we are going to see below, cutoff variations in the Lippmann-Schwinger
equation~\eqref{LS} require significant departures from NDA for contact 
interactions among nucleons.  These departures were first understood within
Pionless EFT.  Its simplicity makes Pionless EFT the poster-child for nuclear 
EFT, and we {therefore} make it the start of this review.
