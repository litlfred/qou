---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear effective field theory: status and perspectives"
section_id: sec-005-6-spin-isospin-projection-and-parametrizations
section_title: "Spin-isospin projection and parametrizations"
section_number: 6
pages: 13-15
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
doc_brief: "Nuclear effective field theory: status and perspectives — 34 sections: Contents; Two-body scattering amplitude; Power counting"
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.959
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




\subsubsection{Coulomb effects and other isospin breaking}
\label{sec:pionlessCoulomb}

Since almost all nuclear systems involve more than one proton, the inclusion of
electromagnetic effects is {generally} important.  In the low-energy
regime, the dominant effect is given by ``Coulomb photons'', \ie, the familiar,
static potential {($\sim\alpha/r$)} between charged particles.  It
originates from the
replacement of derivatives in the effective Lagrangian with covariant ones,

\begin{equation}
 D_\mu = \partial_\mu + \ii eA_\mu \hat{Q} \,,
\label{eq:minimal}
\end{equation}

where $\hat{Q}$ is an appropriate charge operator (\eg{,}
$\hat{Q}=(1+\tau_3)/2$ for nucleons).  The Coulomb photon-nucleon coupling $\ii
e$ comes from the
gauging of the nucleon {time derivative in Eq.~\eqref{eq:L-NN}}, while the
Coulomb-photon ``propagator'' is $\ii/(\vecq^2+\lambda^2)$, where $\lambda$ is
an IR-regulating photon mass that is eventually taken to zero.  Finer
electromagnetic effects enter through operators with more covariant derivatives
and also directly through the field strength, or alternatively the electric
{(}$E_i=\partial_0A_i-\partial_iA_0${)} and magnetic {(}$B_i =
\leviciv_{ijm} \partial^j A^m${)} fields.

\textcite{Kong:1998sx,Kong:1999sf} were the first to study proton-proton ($pp$)
scattering in Pionless EFT.  The challenge here lies in the fact that the
Coulomb interaction is important at very low energies: we see from
Eq.~\eqref{VGV} for the Coulomb potential $V\sim e^2/Q^2$ {that} Coulomb is
nonperturbative for ${Q\simle \alpha m_N / 2 \equiv k_C}$,
which is in the low-energy region of Pionless EFT.
Subtracting the pure-Coulomb amplitude $T_C$
from the full amplitude $T$, one can write

\begin{equation}
 T_{SC}
 = T - T_C
 = {-}\frac{4\pi}{\MN}\frac{\eex^{2\ii \sigma_C}}{k\cot\delta_{pp}(k) - \ii k}
\label{eq:T-SC}
\end{equation}

in terms of the ``subtracted'' $pp$ phase shift $\delta_{pp}(k)$ and the
pure-Coulomb phase shift $\sigma_C = \arg{\Gamma(1 + \ii\eta)}$.
Renormalization can be carried out by matching to the ``Coulomb-modified''
ERE~\cite{Bethe:1949yr},

\begin{multline}
 C_\eta^2 \left(k\cot\delta_{pp}(k) - \ii k\right) + \alpha\MN H(\eta) \\
 = {-}\frac{1}{a_{pp}} + \frac{r_{pp}}{2} k^2 + \cdots \,,
\label{eq:ERE-pp}
\end{multline}

where $a_{pp}\simeq -7.8$ fm
and $r_{pp}\simeq 2.8~\fm$~\cite{Bergervoet:1988zz} are the ERE parameters,
$C_\eta^2 = 2\pi\eta [\exp(2\pi\eta) - 1]^{-1}$ is the
Sommerfeld factor in terms of {$\eta = k_C/k$}, and
$H(\eta)=\Re [\psi(1+\ii\eta)]-\ln\eta+\ii C_\eta^2/(2\eta)$
in terms of the digamma function $\psi$.
{It should be emphasized that the $pp$
scattering amplitude, and thus also the effective range parameters, are
always defined in the presence of the Coulomb interaction and cannot be divided
into strong and electromagnetic parts in a model-independent
way~\cite{Kong:1998sx,Gegelia:2003ta}.}
{For particles with non-unit charges
the definition of the Coulomb momentum $k_C$ is generalized in
Sec.~\ref{sec:halo}, see Eq.~\eqref{eq:Cb-mom}.}

In Pionless EFT, $T_{SC}$ is obtained by replacing all empty bubbles in
Fig.~\ref{fig:BubbleChain} with the dressed one shown in
Fig.~\ref{fig:DressedBubble}.  {The} initial and final-state Coulomb
interactions are {accounted for} by the construction in Eq.~\eqref{eq:T-SC}.
``Dressing'' here refers to resumming the Coulomb interaction to all orders
between each pair of $C_0$ vertices, which \textcite{Kong:1998sx,Kong:1999sf}
were able to do using a known analytic expression for the pure Coulomb Green's
function.  With dimensional regularization,

\begin{equation}
 \frac{4\pi}{\MN C_{0}^{pp}(\mu)} =
 \frac{1}{a_{{pp}}} - \mu
  + \alpha\MN\left(\frac{1}{\eps} +\ln\frac{\mu}{\alpha m_N}
  + \text{const.} \right) .
\label{eq:app-renorm}
\end{equation}

The term linear in the renormalization scale $\mu$ comes from the PDS
prescription, but Coulomb exchange now introduces an additional logarithmic
divergence, reflected in the pole in $\eps = d-3$, where $d$ is the number of
spatial dimensions.  Range corrections have been considered at \NLO by
\textcite{Kong:1999sf} and at \NNLO by \textcite{Ando:2007fh}.  An equivalent
formulation in terms of a $pp$ dibaryon exists~\cite{Ando:2010wq}.  The RG
analysis of \textcite{Birse:1998dk} discussed in Sec.~\ref{sec:RG} has also
been
extended to the charged-particle sector~\cite{Barford:2002je,Ando:2008jb}.


\begin{figure}[tb]
\centering
\includegraphics[clip,width=0.9\columnwidth]{DressedBubble}
\caption{Bubble diagram dressed with Coulomb exchange (wavy line).}
\label{fig:DressedBubble}
\end{figure}


The LEC $C_{0}^{pp}=C_{0\textrm{t}}+\Delta C_{0(+)}$ in
Eq.~\eqref{eq:app-renorm} contains an isospin-dependent contribution $\Delta
C_{0(+)}$, which is a short-range (or ``indirect'') electromagnetic effect.
The EFT includes also isospin breaking from the quark
masses~\cite{VanKolck:1993ee,vanKolck:1995cb}.  While electromagnetic
interactions break isospin more generally (``charge dependence''), effects
linear in the quark masses break charge symmetry (a rotation of $\pi$ around
the second axis in isospin space) specifically.  Introducing the projectors
$P_{(\pm)}=(P_{\mathrm{t}}^{1}\mp\ii P_{\mathrm{t}}^{2})/\sqrt{2}$
onto the $pp$/$nn$ channel, the isospin-breaking Lagrangian takes the form

\begin{multline}
 \LL_{\textrm{ib}}
 = \delta m_N N^\dagger \tau_3 N
 - \frac{\Delta C_{0(+)}}{2}
   (N^T P_{(+)} N)^\dagger(N^T P_{(+)} N) \\
 - \frac{\Delta C_{0(-)}}{2}
   (N^T P_{(-)} N)^\dagger(N^T P_{(-)} N)
 + \cdots \,.
\label{eq:L-pp}
\end{multline}

NDA~\eqref{NDA} indicates that the neutron-proton mass splitting
$\delta m_N=\OO(\varepsilon {\bar m}, \alpha m_N/(4\pi))$.  It is well known
that the two types of contributions are comparable in magnitude, $\varepsilon
{\bar m}\sim \alpha m_N/4\pi$, {valid up to a (scale-dependent) factor of a
few,} but have opposite signs, the quark masses tilting the balance in favor of
the neutron.  The mass-splitting term can be
removed by a redefinition of the nucleon field~\cite{Friar:2004ca}, and
reappears as an $\OO(\delta m_N/m_N)$ effect in the nucleon kinetic term.
The most important quark-mass effects in the $N\!N$ system lie in the
short-range LECs $\Delta C_{0(\pm )}$.  The reduced quark mass is
$(\varepsilon {\bar m})_{\mathrm{red}}=\varepsilon {\bar m}/\Mhi$ and, together
with the $S$-to-$S$-wave enhancement discussed in Sec.~\ref{sec:PowerCounting},
leads to {$(a_{nn}-a_{\mathrm{t}})/a_{\mathrm{t}} \sim
\Delta C_{0(-)}/C_{0\mathrm{t}} = \OO(\varepsilon
{\bar m}\, a_{\mathrm{t}}) \simeq 0.2$, \cf~\cite{Konig:2015aka}.}
A similar contribution exists for $\Delta C_{0(+)}$ which is, however, dominated
by the electromagnetic contribution $\Delta C_{0(+)}/C_{0\textrm{t}}=\OO(\alpha
m_N a_{\mathrm{t}})$, consistent with Eq.~\eqref{eq:app-renorm}.

For most of the region of validity of Pionless EFT, $Q\simge \alpha m_N$
and \emph{all} electromagnetic interactions are expected to be perturbative.
In this region, $Q\simge 1/a_{\mathrm{t}}$ as well.  \textcite{Konig:2015aka}
developed an expansion in powers of $\alpha m_N/Q$ and $1/(Qa_{\mathrm{t}})$ in
addition to the standard $Q/\Mhi$ expansion.  For simplicity, they paired the
expansions by taking $\alpha m_N\sim a_{\mathrm{t}}^{-1} = \OO(\Mlo^2/\Mhi)$
and $\varepsilon {\bar m}=\OO(\Mlo^3/\Mhi^2)$.  In this case, LO in the
\OneSNot channel consists of the isospin-symmetric unitary amplitude, that is,
Eq.~\eqref{eq:T-kcot-a} with $k\cot \delta_{\textrm{t}}=0$.  The first
short-range and electromagnetic corrections break isospin symmetry at NLO,
reproducing $a_{pp}$ and leading to equal scattering lengths in the other two
\OneSNot isospin channels.  In addition, at NLO there is the standard,
isospin-symmetric $C_{2\mathrm{t}}$ interaction, while quark-mass effects (and
the $nn$ splitting from $np$) first enter at N$^2$LO.  This is consistent with
the observed relation $r_{pp}\simeq r_{\mathrm{t}}$.
