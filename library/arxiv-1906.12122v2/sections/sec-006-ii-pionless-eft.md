---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear eﬀective ﬁeld theory: status and perspectives"
section_id: sec-006-ii-pionless-eft
section_title: "II Pionless EFT"
section_number: null
pages: 8-9
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.989
doc_brief: "Nuclear eﬀective ﬁeld theory: status and perspectives — 82 sections: Nuclear effective field theory: st; Contents; I Introduction"
---
\label{sec:pionless}

\subsection{Motivation}
\label{sec:pionlessmotivation}

At very low energies---\ie, for momenta $Q\ll m_\pi$---few-nucleon systems
are not sensitive to the details associated with pion (or other meson) exchange.
This fact makes it possible to describe such systems with short-range
interactions alone (\ie interactions of finite range or falling off at least as
an exponential {in} the interparticle distance), an approach dating
back to Bethe and his effective range expansion (ERE) for nucleon-nucleon
($N\!N$) scattering~\cite{Bethe:1949yr}---see
also {related work
by~\textcite{Bethe:1935aa,Bethe:1935ab,Fermi:1936XX,Schwinger:1947zz,
Jackson:1950zz}}.
Casting this basic idea into a modern
systematic framework leads directly to what has become known as Pionless EFT.

Historically, Pionless EFT emerged out of the effort to understand the
renormalization of EFTs where a certain class of interactions need to be treated
nonperturbatively.  It had been shown by \textcite{Kaplan:1996xu},
\textcite{Phillips:1997xu}, and \textcite{Beane:1997pk} that the original
prescription~\cite{Weinberg:1990rz,Weinberg:1991um} to extend Chiral
Perturbation Theory to few-nucleon systems (discussed in Sec.~\ref{sec:chiral})
could not be implemented satisfying RG invariance.  It turned out that there is
a surprisingly rich structure of phenomena in the low-energy regime where
explicit pion exchange cannot be resolved.

Formally, the pion can be regarded as ``integrated out'' if all other dynamical
scales are much smaller than the pion mass.  Consider, for example, the Yukawa
potential corresponding to one-pion exchange:

\begin{equation}
 {\mbraket{\veck'}{V_{2N,\pi}}{\veck}
 \propto \frac{1}{\vecq^2 + \Mpi^2}
 \;,\;
 \vecq = \veck' - \veck \,,}
\label{eq:V-pi}
\end{equation}

where $\veck$ and $\veck'$ are incoming and outgoing momenta of two scattered
nucleons (in their center-of-mass frame).  If these are both small compared to
$\Mpi$, Eq.~\eqref{eq:V-pi} can be expanded in $\vecq^2$, with the leading term
being just a constant and the following terms coming with ever higher powers of
$\vecq^2$.  This shrinking of the original interaction to a point is illustrated
in Fig.~\ref{fig:PionsOut}.  Fourier-transforming into configuration space one
obtains a series of
{delta functions} with a growing number of derivatives.  In
Chiral EFT, which includes pions, analogous contact interactions
{represent the exchange} of heavier mesons.  Integrating out
pions to arrive at Pionless EFT means merging unresolved pion exchange with
these operators.  It should be noted, however, that Chiral EFT is based on an
expansion around a vanishing pion mass, whereas Pionless EFT treats $\Mpi$ as a
large scale.  As such, these two EFTs are very different{---in particular,
the respective LECs cannot in general be related by perturbative
matching---}but they are both well-defined low-energy limits of QCD.


\begin{figure}[tb]
\centering
\includegraphics[clip,width=0.75\columnwidth]{PionsOut}
\caption{Reduction of pion exchange (dashed line) to a series of contact
interactions between nucleons (solid lines) for $q^2\ll \Mpi^2$.}
\label{fig:PionsOut}
\end{figure}


In practice, one does not have to derive Pionless EFT from a more fundamental
EFT by integrating out explicit pions.  Instead, one can just follow the EFT
paradigm and write down an effective Lagrangian{, Eq.~\eqref{Lexp},} with
all contact interactions
between nucleons that are allowed by symmetry.  This restriction means that one
requires invariance under
{``small'' Lorentz boosts} (Galilean
boosts plus systematic relativistic corrections), {rotations, isospin, and
discrete symmetries like parity and time reversal}, the systematic breaking of
which can also be accounted for.  The same EFT with other particles substituted
for nucleons can describe different systems where the important dynamics takes
place at distances beyond the range of the force.  Some of these systems are
discussed in Secs.~\ref{sec:halo} and~\ref{sec:other}.  In particular{,}
Pionless EFT captures the universal aspects of Efimov physics
\cite{Braaten:2004rn}.

In this section we discuss the basic features and formalism of Pionless EFT,
first in the context of two-body systems (Sec.~\ref{sec:pionlessweaklyboundS})
and later for a larger number of particles
(Sec.~\ref{sec:pionlesslightnuclei}). Some of the outstanding issues are raised
in Sec.~\ref{sec:pionlesssummary}.
