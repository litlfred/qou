---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear eﬀective ﬁeld theory: status and perspectives"
section_id: sec-017-6-spin-isospin-projection-and-parametrizations
section_title: "Spin-isospin projection and parametrizations"
section_number: 6
pages: 13-14
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.976
doc_brief: "Nuclear eﬀective ﬁeld theory: status and perspectives — 82 sections: Nuclear effective field theory: st; Contents; I Introduction"
---
{For a fixed $N\!N$ channel it is convenient to use the effective
Lagrangian~\eqref{eq:L-NN-simple}, with $\psi$ a
nucleon field for which the combination $\psi^\dagger\psi$ has definite spin and
isospin $(S,I)$.  The Pauli principle dictates that only isospin-triplet
{$\mathrm{t}\equiv(0,1)$} and isospin-singlet {$\textrm{s}\equiv(1,0)$}
are allowed combinations.}  We use subscripts ``$\mathrm{s}$'' and
``$\mathrm{t}$'' here in reference to isospin, with a warning {that
the same subscripts are sometimes used in reference to spin}.  To go beyond the
description of an isolated two-nucleon system, it is desirable to treat both
combinations on the same footing.  To this end, it is convenient to introduce a
nucleon field $N$ that is a doublet in both spin and isospin space, along with
projection operators

\begin{equation}
 (P_{\textrm{s}})^i = \sigma^2\sigma^i\tau^2 / \sqrt8
 \mathtext{,}
 (P_{\textrm{t}})^A = \sigma^2\tau^2\tau^A/\sqrt8 \,,
\label{eq:P-t-s}
\end{equation}

where $\sigma^i$ ($\tau^A$) denotes the three Pauli matrices in spin (isospin)
space, and we have used lower- (upper-) case indices to further distinguish the
two spaces.  The Lagrangian for the $N\!N$ system can then be written as

\begin{multline}
 \LL
 = N^\dagger \left(\ii\partial_0 + \frac{\Laplace}{2\MN}\right) N
 - \frac{C_{0\textrm{s}}}2  (N^T P_{\textrm{s}} N)^\dagger(N^T P_{\textrm{s}}N)
 \\
 - \frac{C_{0\textrm{t}}}2 (N^T P_{\textrm{t}} N)^\dagger(N^T P_{\textrm{t}} N)
 + \cdots \,,
\label{eq:L-NN}
\end{multline}

where the ellipses represent analogous terms with $C_{2\textrm{s/t}}$ as well
as higher-order operators.  Fierz rearrangements can be used to generate
equivalent interactions.  Analogously, Eq.~\eqref{eq:L-NN-simple-d} is
generalized to the nuclear case by introducing two dibaryon fields---one for
each $N\!N$ $S$-wave channel--- using the same projection operators
$P_{\textrm{s},\textrm{t}}$~\cite{Bedaque:1997qi}.

The two channels are somewhat different concerning both sign and magnitude of
the scattering lengths.  However, it has been customary to treat both
$a_{\mathrm{s}}^{-1}$ and $|a_{\mathrm{t}}|^{-1}$ as $\Mlo$, although we return
to this issue in Sec.~\ref{sec:pionlessCoulomb}.  The ERE,
Eq.~\eqref{eq:T-kcot-b}, has a certain radius of convergence, set by the
nearest singularity to the expansion point $k^2=0$.
{The pion-exchange cut
on the imaginary $k$ axis starting at $\mpi$/2}
{leaves the deuteron pole within the radius of convergence of the ERE,
and indeed it is well known that the properties of this pole can be
expressed in terms of the ERE parameters~\cite{Goldberger:1967},
\cf~Sec.~\ref{sec:pionlessscattamp}.}
For example, the deuteron binding momentum is

\begin{equation}
 \gamd = \frac{1}{a_{\rm s}}
 \left(1+\frac{r_{\rm s}}{2a_{\mathrm{s}}}+\cdots\right) \,.
\label{eq:gammad}
\end{equation}

Alternatively, and this is in fact what was done first
historically~\cite{Bethe:1949yr}, one can perform the ERE directly about
this pole (\ie, about the point $\ii\gamd$ in the complex momentum plane),

\begin{equation}
 k\cot\delta_{d}(k)
 = {-}\gamd + \dfrac{\rhod}2\big(k^2+\gamd^2\big) + \cdots \,,
\label{eq:ERE-d}
\end{equation}

where $\rho_d\simeq 1.765~\fm$~\cite{deSwart:1995ui} is the deuteron effective
range.  The motivation for using Eq.~\eqref{eq:ERE-d} instead of the ERE about
zero momentum is that it captures the exact location of the pole already at LO.
\textcite{Griesshammer:2004pe} extended the procedure to the \OneSNot channel,
where it is possible to define the ERE about the virtual-state pole.

The first detailed comparison of the \ThreeSOne phase shift obtained in Pionless
EFT with empirical values was carried out up to N$^2$LO by
\textcite{Chen:1999tn}, with LECs fitted to Eq.~\eqref{eq:ERE-d}.  In
Fig.~\ref{fig:ThreeSOnePhase} we show results {fitted to}
Eq.~\eqref{eq:T-kcot-b} instead, which are qualitatively similar: convergence is
seen at low energies and already at NLO a very good description is achieved.
The corresponding results for \OneSNot up to N$^2$LO were presented
by \textcite{Beane:2000fx}.


\begin{figure}[tb]
\centering
\includegraphics[clip,width=1\columnwidth]{Phase-3S1-new}
\caption{{The $N\!N$ scattering phase shift $\delta$ as a function
 of the nucleon laboratory energy $E_{\text{lab}}$ in the \ThreeSOne partial
 wave for Pionless EFT and Chiral EFT at various
 orders~\cite{Long:2011xw} (results kindly provided by C.-J.~Yang), and
 the chiral potential ``EM500''~\cite{Entem:2003ft}.
 For comparison we show the partial-wave analysis (PWA)
 of~\textcite{Perez:2013jpa}, with error bars smaller than the symbols.}}
\label{fig:ThreeSOnePhase}
\end{figure}
