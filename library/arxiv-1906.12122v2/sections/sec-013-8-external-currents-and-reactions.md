---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear effective field theory: status and perspectives"
section_id: sec-013-8-external-currents-and-reactions
section_title: "External currents and reactions"
section_number: 8
pages: 24-32
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
doc_brief: "Nuclear effective field theory: status and perspectives — 34 sections: Contents; Two-body scattering amplitude; Power counting"
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.969
---
\label{sec:Currents-ThreeBody}

The coupling to external currents works exactly as in the two-body sector (see
Sec.~\ref{sec:Currents-TwoBody}).  Given the increased technical challenges,
there are fewer {calculations}, and they mostly tackle triton and helion
properties.  Within this limited scope, they confirm the convergence of Pionless
EFT at low energies.

The simplest observable is the triton charge form factor, in particular the
charge radius, which determines the leading momentum dependence.
\textcite{Platter:2005sj} used an effective quantum-mechanical framework to
obtain the form factor in the impulse approximation, \ie, considering the
electric charge operator between triton wavefunctions obtained by solving a
Faddeev equation for the effective potential derived from the pionless
Lagrangian at LO.  Similar to the Phillips line (see Sec.~\ref{sec:Triton}), the
existence of a single LO three-body parameter in Pionless EFT explains a
correlation between the triton binding energy and charge radius that had
previously been observed with different potential models~\cite{Friar:1985aa}.
An N$^2$LO calculation was reported by \textcite{Sadeghi:2009dm}, but few
details are given.  Recently, the fully perturbative treatment of higher-order
corrections was extended to the triton and helion charge radii at
\NNLO~\cite{Vanasse:2015fph,Vanasse:2017kgh}, and magnetic moments and radii at
\NLO~\cite{Vanasse:2017kgh}.  Even though Coulomb interactions were neglected
for \ThreeHe, good agreement with experiment was found.  Analogous results were
obtained with a resummation of higher-order effects by
\textcite{Lensky:2016djr}, who also showed the correlation between the \FourHe
charge radius and other three- and four-nucleon observables.

\textcite{Sadeghi:2004es}, \textcite{Sadeghi:2006fc}, and
\textcite{Sadeghi:2007qy} calculated the $nd \to \ThreeH\,\gamma$ capture cross
section, finding good agreement with available experimental data at \NNLO.
\textcite{Sadeghi:2009rf} calculated the inverse process of triton
photodisintegration, which features the same amplitudes due to time-reversal
symmetry.  Several significant flaws in the calculation of
\textcite{Sadeghi:2006fc} were identified by \textcite{Arani:2014qsa}, who
presented an updated calculation.  At \NNLO, they still find reasonable
agreement of the thermal $nd$ capture cross section with experiment.  The total
cross section for the related reaction $pd \to \ThreeHe\,\gamma$ was calculated
to \NLO in a range of energies amenable to perturbative Coulomb interactions by
\textcite{Nematollahi:2016zjg}.  The $3N$ force was fixed by the helion binding
energy and data were reasonably described considering the uncertainty of the
calculation.  The even more challenging process of deuteron-deuteron radiative
capture ($dd\to \FourHe\,\gamma$) was calculated at \LO by
\textcite{Sadeghi:2014yia}, with the $3N$ force fitted to the alpha-particle
energy.  While available data for the astrophysical $S$-factor are apparently
well described, a lack of technical details makes it difficult to assess
the validity of the calculation.

New ground was broken with the extension to electroweak processes made by
\textcite{De-Leon:2016wyu}, who studied triton $\beta$ decay to \NLO.  This
work establishes a new way of fixing the LEC $L_{1,A}$ of the axial-vector
counterpart of Eq.~\eqref{eq:L-mag-L1L2}, which is relevant for other
electroweak processes ($pp$ fusion, in particular) as well.  Calculations like
this reveal the potential of Pionless EFT to tackle interesting reactions
involving more than two nucleons{, based for example on the general framework
developed by \textcite{De-Leon:2019dqq}.}



\subsection{Outstanding issues and current trends}
\label{sec:pionlesssummary}

Pionless EFT has fulfilled the longstanding goal of a renormalizable quantum
field theory for nuclear physics.  Although it has a narrow regime of strict
validity, it seems to apply to, at least, $A\le 3$ bound states and possibly
to extend to $A=4$ and beyond.  RG invariance, combined with the fine tuning
that places two-body bound states near zero energy, has led to a power counting
that flies in the face of NDA, as summarized for the potential in
Fig.~\ref{fig:pionlesspot}.  Yet, unresolved questions remain, such as:

\begin{itemize}

\item
How far in $A$ can we describe nuclei within this framework?  So far all LO
calculations ($A\le 40$) give binding energies in agreement with experiment
within the expected theoretical uncertainty, but finer details such as relative
energies and thresholds are not reproduced.  Calculations for $A=4,16,40$ where
subleading interactions are resummed reinforce the surprising success of LO.
However, at the moment, no calculation exists {for more than four} nucleons
where \NLO and higher orders are treated perturbatively.  There also remain
issues about the power counting of Coulomb interactions and other
isospin-breaking interactions.  Higher-order calculations for {$A > 4$} are
sorely needed.

\item
{\textcite{Wigner:1936dx,Wigner:1937zz}} proposed an $SU(4)$
spin-isospin symmetry to explain the strong binding of nuclei containing integer
numbers of alpha particles.  Since the $3N$ force~\eqref{eq:L-NN-3} is $SU(4)$
symmetric~\cite{Bedaque:1999ve}, one cannot but wonder whether there are signs
of $SU(4)$ symmetry also in light nuclei.  It was shown by
\textcite{Chen:2004rq} that binding energies of $A\le 4$ nuclei satisfy
inequalities obtained from $SU(4)$ symmetry.  Accordingly,
\textcite{Vanasse:2016umz} developed an expansion around an $SU(4)$-symmetric LO
based on average \OneSNot and \ThreeSOne scattering lengths.  They showed that
this expansion is promising also for observables other than binding energies,
since it converges well for the triton charge radius up to \NLO in the
symmetry-breaking parameter (and including range corrections as well).

\item
In the same spirit, how far can we push the expansion around the nontrivial
fixed point of the $N\!N$ amplitude, \ie, the unitary limit where both the
deuteron and the \OneSNot virtual state have zero energy?  In this limit the LO
EFT has not only exact $SU(4)$ symmetry but also discrete scale invariance:
while the two-body amplitude is invariant under continuous scale
transformations~\cite{Mehen:1999nd}, the three-body force \eqref{eq:H0-0} is
symmetric only under discrete scale
changes~\cite{Bedaque:1998kg,Bedaque:1998km}.  This remaining symmetry leads to
Efimov states in the three-body system and its descendants in the
four-~\cite{Hammer:2006ct} and higher-body systems.  \textcite{Konig:2016utl}
and \textcite{Konig:2016iny}, generalizing an earlier approach to the \OneSNot
channel~\cite{Konig:2015aka}, have proposed an expansion around the
unitary (or unitarity) limit also in the \ThreeSOne channel: expansions in both
$1/(Q a_{\rm t})$ and $1/(Q a_{\mathrm{s}})$ are added to the standard Pionless
EFT expansion.  A \emph{single} LO parameter $\Lambda_*$ provides the
nonperturbative scaffolding on top of which more quantitative results are built
in by perturbation theory.  This quite radical expansion appears to converge
remarkably well for three- and four-nucleon binding
energies~\cite{Konig:2016utl,Konig:2016iny}.  At LO all binding energies are
functions of $\Lambda_*$, and for bosons~\cite{Carlson:2017txq} they saturate
according to the liquid-drop formula.  The correlation between nuclear-matter
saturation energy and density expressed in the Coester
line~\cite{Coester:1970ai} would emerge from variation of
$\Lambda_*$~\cite{Kolck:2017zzf} just as the Tjon line---\emph{if}, that
is, Pionless EFT holds all the way to heavy nuclei.  {Related work that
aims to simplify nuclear physics based on the closeness of the real world to
the unitarity limit and/or Wigner $SU(4)$ limit has been carried out by
\textcite{Kievsky:2015dtk,Kievsky:2018xsl,Gattobigio:2019omi,Lu:2018bat}.}

\end{itemize}




\section{Halo/Cluster EFT} \label{sec:halo}

\subsection{Motivation}

In this section we discuss efforts to go one step further in the application
of low-energy universality by including tightly bound clusters of nucleons as
explicit fields in the effective Lagrangian.  This Halo/Cluster EFT
framework is appropriate for halo nuclei and nuclei with a cluster structure.
In both cases, the energy required to remove clusters or halo nucleons,
characterized by a momentum scale $\Mlo$, is much smaller than the energy
required to break clusters apart, associated with a momentum scale $\Mhi$.
The classic example is $^6$He, where the energy to separate two neutrons
from an alpha-particle core is $S_{2n}\simeq 0.975~\MeV \ll B(\FourHe)$.  This
class of systems can be thought of as nucleons orbiting one or more clusters,
all separated by distances much larger than the cluster sizes.  They typically
lie at the limits of nuclear stability represented in the nuclear chart by the
so-called driplines, and are target of a vigorous experimental program at
rare-isotope facilities worldwide.  As we discuss below, they can display more
than one low-momentum scale, \eg{,} when Coulomb interactions are present or
when a cluster has an isolated low-energy excited state.

As in Eq.~\eqref{Texp}, observables are expanded in powers of $\Mlo/\Mhi$ and
$Q/\Mhi$, where $Q$ is a typical momentum.  While Halo/Cluster EFT is
mathematically similar to the Pionless EFT for nucleons discussed in the
previous section---and in fact is a theory without explicit pions by itself,
becoming Pionless EFT for light nuclei when the cores are nucleons---there
are a number of new aspects. First, higher partial waves between clusters,
or between clusters and nucleons, are often enhanced, as for the $n\alpha$
scattering relevant for $^6$He.  This causes a richer structure already in the
two-body sector and requires modified power counting schemes.  Second,
the antisymmetrization between nucleons in a cluster (which are not active
degrees of freedom) and halo nucleons is not explicit.

{One} might ask what kind of error is introduced by using explicit fields
for tightly bound clusters.  The effect on observables of exchanging nucleons
in the core with halo nucleons is governed by the overlap of the wavefunctions
of the halo nucleons with the wavefunctions of the core nucleons.  Since the
range of the former is $\Mlo^{-1}$ while the range of the latter is
$\Mhi^{-1}$, this overlap is suppressed by $\Mlo/\Mhi$ compared to the overlap
of two halo nucleons.  Therefore, these effects are controlled by the EFT
expansion in $\Mlo/\Mhi$ and are encoded in the LECs of Halo/Cluster EFT.  The
same argument applies for nucleons in different, widely separated clusters.
For momenta $Q$ of the order of the breakdown scale $\Mhi$ or above, when
distances compared to the core size are probed, full antisymmetrization and
other short-range physics have to be included explicitly.

Halo/Cluster EFT exploits the scale separation between $\Mlo$ and $\Mhi$
independently of the mechanism creating it.  Thus it complements \abinitio
approaches to halo nuclei by zooming out to large distances and providing
universal relations between different few-body observables.  These relations can
be combined with input from an underlying EFT or experiment to predict halo
properties.  Moreover, they allow us to test the consistency of different
approaches and/or experiments.  A particular strength lies in the possibility to
describe the electroweak structure and reactions of halo nuclei in a
model-independent way with controlled error estimates.

Halo/Cluster EFT can be viewed as a generalization of nuclear cluster models
and is usually referred to simply as Halo
EFT~\cite{Bertulani:2002sz,Bedaque:2003wa}.  We give a brief overview here,
starting with $S$-wave neutron halos and Efimov states in Secs.~\ref{sec:Shalo}
and \ref{sec:efimovhalos}, respectively.  The complementarity with \abinitio
methods, useful to explore heavy halos, is discussed in
Sec.~\ref{sec:halo+abinitio}, before higher partial waves are tackled in
Sec.~\ref{sec:highpar}.  We show how Halo EFT connects with electromagnetic
processes in Sec.~\ref{sec:haloelectric}, before sketching the changes needed
for proton halos (Sec.~\ref{sec:phalos}) and multi-cluster systems
(Sec.~\ref{sec:clusters}), and ending with an outlook (Sec.~\ref{sec:haloook}).
Our emphasis is complementary to Sec.~\ref{sec:pionless}.  A more in-depth
discussion can be found in the recent review of Halo EFT by
\textcite{Hammer:2017tjm}.


\subsection{$S$-wave neutron halos}
\label{sec:Shalo}

We start with the case of $S$-wave halo nuclei or cluster states without
Coulomb interactions.  For definiteness, we consider one- and
two-neutron halo nuclei using the formalism of \textcite{Hagen:2013xga}.  The
extension to other cases is straightforward.  We also restrict our analysis to
LO in $\Mlo/\Mhi$.  Higher-order effects can be included as discussed in the
previous section for Pionless EFT.

The effective Lagrangian for neutrons ($n$) and {a spinless core} ($c$)
can be  written as the sum of one-, two- and three-body contributions, $\LL =
\LL_{1b} + \LL_{2b} + \LL_{3b} + \cdots$, where the ellipses denote higher-order
terms and

\begin{align}
 \LL_{1b} &= \psi_0^\dagger
  \left(\ii\partial_0 + \frac{\Laplace}{2m_0}\right)\psi_0
  +
  \psi_1^{\dagger}
  \left(i\partial_0 + \frac{\Laplace}{2m_1}\right) \psi_1 \,,
  \nonumber\\
 \LL_{2b} &= \Delta_1 \,
  d_1^{\dagger}
  d_1
  - g_1\left[
  d_1^{\dagger} \,
  (\psi_1 \, \psi_0) + \hc\right]
  \nonumber\\
  &\hspace{1em}\null+ \Delta_0 \, d_0^\dagger d_0
  - \frac{g_0}{2}\left[d_0^\dagger \,
  (
  \psi_1^\text{\;T} P \,
  \psi_1) +  \hc \right] \, ,
  \nonumber\\
 \LL_{3b} &= \Omega \, t^\dagger \, t
  - h\left[t^\dagger (\psi_0\,d_0) + (\psi_0\,d_0)^\dagger t\right] \, .
\label{eq:lag_05}
\end{align}

The notation is slightly changed compared to the previous section
(\cf~Eq.~(\ref{eq:L-NN-simple-d})) in order to efficiently account for neutron
and core fields, the Pauli spinor $\psi_1$ and the scalar $\psi_0$,
respectively.  The two-body part $\LL_{2b}$ includes two dimerons, the scalar
$d_0$ corresponding to an $\OneSNot$ $nn$ pair and the Pauli spinor $d_1$ for a
$cn$ pair.  $P=\ii\sigma_2/\sqrt{2}$ projects the two neutrons on the spin
singlet.  Finally, $\LL_{3b}$ represents the three-body interaction written in
terms of a  trimeron auxiliary field~\cite{Bedaque:2002yg}, which is
particularly
useful for form{-}factor calculations~\cite{Hagen:2013xga,Vanasse:2015fph}.
It includes the bare trimeron residual mass $\Omega$ and the bare coupling $h$
of the trimeron $t$ to the $d_0$ dimeron ($nn$) and the $c$ field $\psi_0$.
Only the parameter combination $h^2/\Omega$ contributes to observables at LO.
As in Pionless EFT, there exists a whole class of equivalent theories with
three-body forces acting in different channels.  Integrating out the auxiliary
fields, different choices of $\LL_{2b}$ and $\LL_{3b}$ can be transformed into
the same theory without dimeron and trimeron fields up to four- and higher-body
interactions.

In the following, we focus on the properties of the $cn$, $nn$, and $cnn$
systems.  For compact notation, we define the mass parameters:

\begin{eqnarray}
 &&M_\text{tot} = m_0+2m_1\, , \;
  M_i = M_\text{tot}-m_i \, ,\;
  m_{ij}= M_i-m_j\,,
  \nonumber\\
 &&\mu_i = \frac{m_0m_1^2}{m_iM_i}\, ,  \;
  \tilde \mu_i = \frac{m_i M_i}{M_\text{tot}} \,.
\label{eq:lag_40}
\end{eqnarray}

The diagrams for the dressed dimeron propagator, Fig.~\ref{fig:DibaryonProp},
are completely analogous to that for the dibaryon field discussed in
Sec.~\ref{sec:Dibaryons}.  At LO, the full dimeron propagator for the dimeron
$d_i$
is

\begin{equation}
 \ii D_i(p_0, \textbf{p} ) = \frac{2\pi\ii}{s_i \,g_i^2\mu_i} \left[
 1/a_i - \sqrt{ -2\mu_i \tilde{p}_0 - \ii\varepsilon} \,\right]^{-1} \, ,
\label{eq:2ps_40}
\end{equation}

where $\tilde{p}_0=p_0-\textbf{p}^2/(2M_i)$ and $s_i=\delta_{i0}/2 +
\delta_{i1}$ is a symmetry factor.  As before, $a_i$ stands for the respective
scattering length.  For positive $a_i$, the propagator has a bound-state pole on
the first Riemann sheet with residue $Z_i = 2\pi/(s_i \, g_i^2\mu_i^2 a_i)$.
For negative $a_i$, there is a pole on the second sheet corresponding to a
virtual state.

The leading correction to the propagator~\eqref{eq:2ps_40} is due to the
effective range.  It can be included by making the dimeron fields dynamical as
discussed in Sec.~\ref{sec:Dibaryons}.  Here, we stay at LO in the EFT expansion
and neglect effective-range corrections.  The pole momentum $\gamma_i$ is then
given by $\gamma_i=1/a_i$.

Observables in the $cnn$ system can be obtained from the $T$-matrix for the
scattering process of a dimeron and a particle.   The  universal properties and
structure of two-neutron halos were also explored in an effective
quantum-mechanical framework~\cite{Canham:2008jd,Canham:2009xg,Acharya:2013aea}
by solving the Faddeev equations for an effective potential reflecting the
expansion in $\Mlo/\Mhi$ and for the renormalized zero-range
model~\cite{Amorim:1997mq,Delfino:2007zu}.  For a review of the latter work
see~\cite{Frederico:2012xh}.

We consider the center-of-mass frame, in which the on-shell $T$-matrix only
depends on the total energy $E$ and the relative momenta in the ingoing and
outgoing channels $\textbf{p}$ and $\textbf{k}$, respectively. External dimeron
legs are renormalized with the wavefunction renormalization factors
$\sqrt{|Z_i|}$.  The absolute value is only required for $i=0$ because $Z_0<0$,
corresponding to the unbound $nn$ pair.  Here, the factor provides a convenient
redefinition of the amplitude but has no physical significance.

There are two possibilities for the initial or final state, depending on the
identity of the particle and dimeron.  Here we label the $T$-matrix element
$T_{ij}$ by the index $i$ ($j$) of the dimeron and particle in the incoming
(outgoing) channel.  Keeping the matrix structure of $T_{ij}$ implicit, the
integral equation for the $T$ {} matrix is given by
Fig.~\ref{fig:nd-IntEq-Q}
with the substitution in Fig.~\ref{fig:ThreeBodyForce}, where the contact
three-body coupling is $h^2/\Omega$.
The $T$ {} matrix can be decomposed into
partial-wave contributions $T_{l m,l'm'}=\delta_{ll'}\delta_{mm'}T_{l}$.
The resulting $2\times2$-matrix integral equation for angular momentum $l$ is
a generalization of the Skorniakov-Ter-Martyrosian
equation~\cite{Skorniakov:1957aa} and reads

\begin{multline}
 T_{l}(E,p,k) = \int_0^\Lambda \! \dd q \, R_{l}(E,p,q) \,
 \bar{D}(E, q) \, T_{l}(E,q,k) \\
 \null + R_{l}(E,p,k)
\label{eq:3ps_30}
\end{multline}

when a sharp momentum-space cutoff $\Lambda$ is imposed on the loop momentum in
the three-body sector.  For simplicity we focus on the $S$ wave, $l=0$, and
drop the subscript $l$ on $R$ and $T$.  The components of the interaction matrix
$R$ are given by

\begin{align}
 R_{ij}(E,p,k) &= \frac{ 2\pi \, \chi_{ij} \,m_{ij}}{
 \left|a_i a_j s_i s_j\right|^{\frac{1}{2}} \mu_i\mu_j}
 \, \frac{1}{pk} \ Q_0\big(c_{ij}\big)
 - \delta_{i0} \delta_{j0} H \,, \nonumber \\
 c_{ij} &= \frac{m_{ij}}{pk} \left(\frac{p^2}{2\mu_j} +
 \frac{k^2}{2\mu_{i}} -E - \ii\varepsilon\right) \,,
\label{eq:3ps_40}
\end{align}

where $\chi_{ij}=1-\delta_{i0}\delta_{j0}$ and $Q_0$ is a Legendre function of
the second kind.  Moreover, $H=|Z_0|h^2/\Omega$ is the dimensionless three-body
coupling defined in Eq.~(\ref{eq:H0-0}) which depends log-periodically on the
cutoff $\Lambda$.  It only contributes for angular momentum $l=0$.  The dimeron
matrix is diagonal in the channel indices: $\bar{D} =
\text{diag}(\bar{D}_0,\bar{D}_1)$ with

\begin{equation}
 \bar{D}_i(E,q) = \frac{\mu_i |a_i|q^ 2}{2\pi^2} \ \left[-1/a_i
 + \sqrt{-2\mu_i\tilde{E}- \ii\varepsilon}\right]^{-1} \, ,
\label{eq:3ps_50}
\end{equation}

and $\tilde{E}=E-q^2/(2\tilde\mu_i)$.

{The transition amplitude near the energy of an $S$-wave three-body bound
state can be decomposed into a regular and an irregular part.}
This yields the homogeneous bound-state equation

\begin{equation}
 \mathcal B (p)= \int_0^\Lambda \dd q \, R(E,p,q) \, \bar{D}(E, q) \,
 \mathcal B(q) \,,
\label{eq:3ps_70}
\end{equation}

which has nontrivial solutions only at the bound-state energy $E=-B_{cnn}$.

For a given cutoff $\Lambda$, we can fix the unknown three-body parameter $H$
such that Eq.~\eqref{eq:3ps_70} has a solution at the desired value
$E=-B_{cnn}$.  However, any other three-body observable can be used as well.  In
this way, the three-body coupling is renormalized and other three-body
observables (including other three-body bound states) can be predicted.  In
particular, Eq.~\eqref{eq:3ps_30} can be solved numerically in order to
determine the $T$ matrix for three-body scattering observables.
Since the two-neutron system is not bound, only the element $T_{11}$ describes a
particle-dimeron scattering process, namely the scattering of a neutron from a
$cn$ bound state at energy $E=p^2/(2\tilde\mu_1) - 1/(2\mu_1 a_1^2)$:

\begin{equation}
 T_{11}\!\left(E,\,p,\,p\right)
 = \frac{2\pi}{\tilde \mu_1} \, \frac{1}{p\cot\delta_{cn-n}(p)- \ii p} {\,.}
\label{eq:3ps_75}
\end{equation}

{The other elements contribute to three-body scattering and
breakup.}

A fully perturbative extension of this formalism to NLO was recently presented
by \textcite{Vanasse:2016hgn}. NLO equations with resummed range corrections
were previously given by~\textcite{Canham:2009xg}.



\subsection{Excited Efimov states in halo nuclei}
\label{sec:efimovhalos}

The bound-state solutions of Eq.~(\ref{eq:3ps_70}) are a specific variant of
Efimov states~\cite{Efimov:1970zz,Efimov:1973awb}.  Thus the Efimov effect
provides a natural binding mechanism for two-neutron halos with dominantly
$S$-wave interactions.  However, the contributions of higher partial waves and
partial-wave mixing complicate the situation.  While Halo EFT naturally
accommodates resonant interactions in higher partial waves as discussed in
subsection~\ref{sec:highpar}, there is no Efimov effect in this
case{,
see, \eg, \cite{PhysRevA.77.043611,Nishida:2011np,Braaten:2011vf}.}
A general overview of Efimov states
in nuclear and particle physics was given by \textcite{Hammer:2010kp}.
Here, we review the possibility of identifying Efimov states in halo nuclei.

Since the strength of the interaction between the neutrons and the core is
fixed, the identification of Efimov physics is more delicate than for
ultracold atoms, where the effective scattering length can be dialed through an
external magnetic field.  In particular, the log-periodic dependence of
observables on the scattering length cannot be used to identify Efimov physics.
Instead one may look for excited states which (approximately) satisfy the
universal scaling relation for Efimov
states~\cite{Efimov:1970zz,Efimov:1973awb}.  Note that there are two relevant
scattering lengths for a $cnn$ system, $a_0\equiv a_{nn}$ and $a_1\equiv
a_{cn}$.  Since $a_{nn}$ is the same for all halo nuclei and negative, we focus
only on the dependence on $a_{cn}$.  We define the three-body momentum as

\begin{equation}
  K = \mathrm{sgn}(E)\sqrt{2\tilde{\mu}_1 |E|}\,,
  \label{eq:3bbm}
\end{equation}
where the sign of the square root is taken as the sign of the energy $E$.
The schematic dependence of the Efimov spectrum on $K$ and the inverse
neutron-core scattering length $a_{cn}^{-1}$ is illustrated in
Fig.~\ref{fig:efiplot}.  The breakdown scale $\Mhi$ defines a region outside of
which details of short-range physics matter and the bound states cease to be
universal.  Two typical situations are shown, with two universal states (at
$a_{cn}>0$) and one universal state (at $a_{cn}<0$).


\begin{figure}[tb]
 \centering
 \includegraphics[width=6cm,clip=true]{efiplot10d}
 \caption{Illustration of the Efimov spectrum as a function of the three-body
 momentum $K$ (\cf~Eq.~\eqref{eq:3bbm}) and the inverse neutron-core
 scattering length $a_{cn}^{-1}$.  The diagonal line in the fourth quadrant
 represents the neutron-core threshold.  The solid lines indicate the Efimov
 states.  The window of universality for bound states is represented by the
 hashed half circle, while the dashed and dot-dashed lines indicate a typical
 system with $a_{cn}>0$ and $a_{cn}<0$, respectively.
}
\label{fig:efiplot}
\end{figure}



In the hypothetical unitary limit $a_{cn}^{-1}=a_{nn}^{-1}=0$, the Efimov
spectrum becomes geometric,

\begin{equation}
 K^{(n)} = -\lambda_0^{-n} \kappa_*\,,
\label{B3-Efimov-uni}
\end{equation}

where $\lambda_0 = e^{\pi/ s_0}$ is the discrete scaling factor and $\kappa_*$
is the binding momentum of the state with label $n=0$. In general, $s_0$ and
$\lambda_0$ depend on the number of interacting pairs and the masses and
symmetry properties of the particles, {and} $\lambda_0\approx 22.7$ for the
equal-mass nucleons discussed in Sec.~\ref{sec:pionless}.  The value of
$\kappa_*$ is related by a {(regulator-dependent)} constant factor
to the three-body parameter
$\Lambda_\star$ that determines the three-body force $H$ in Eq.~\eqref{eq:H0-0}.
{An explicit value for the case of identical bosons is given}
{by \textcite{Braaten:2004rn}.}
The spectrum shown in Fig.~\ref{fig:efiplot} is invariant under discrete
scaling transformations with $\lambda_0$:

\begin{equation}
 \kappa_* \longrightarrow \kappa_* \,,
 \quad
 a_{cn}  \longrightarrow  \lambda_0^{m} a_{cn} \,,
 \quad
 K  \longrightarrow  \lambda_0^{-m} K \,,
\label{dssym}
\end{equation}

where $m$ is any integer.  This discrete scale invariance holds for all
few-body observables and is a clear signature of an RG limit cycle in the
three-body system~\cite{Bedaque:1998kg}.

If more particles are added, no new parameters are needed for renormalization
at LO~\cite{Platter:2004he,Platter:2004zs}.  As a consequence, all four-body
observables in the universal regime are governed by the same limit cycle and
can be characterized by $a$ and $\kappa_*$.  This leads to the universal
correlations between three- and four-body observables already discussed
in Secs.~\ref{sec:Triton} and~\ref{sec:Helion}.  A similar behavior is expected
for higher-body observables.

Halo nuclei have been discussed as possible candidates for Efimov states for
more than 30 years~\cite{Fedorov:1994zz}. As the full Efimov plot for $cnn$
systems is three-dimensional and depends on the two scattering lengths $a_{nn}$
and $a_{cn}$, it is more instructive to plot candidate nuclei in a
two-dimensional plane characterized by the neutron-core energy $E_{nc}$ and
the neutron-neutron energy $E_{nn}$, in units of the three-body ground-state
energy $E_{gs}$, as introduced by \textcite{Amorim:1997mq}.  If a given nucleus
lies within a certain boundary curve that weakly depends on the mass number $A$
of the core, it should display an excited Efimov state.  The candidate nuclei
$^{11}$Li, $^{12}$Be, $^{14}$Be, $^{18}$C, and $^{20}$C were investigated in
LO Halo EFT assuming only resonant $S$-wave interactions by
\textcite{Canham:2008jd}.  An update of this analysis with current halo
candidates and established halo nuclei is shown in Fig.~\ref{fig:efihalo}.  The
triton has also been added, since it can be interpreted as an two-neutron halo
with a proton core.


\begin{figure}[tb]
\centering
\includegraphics*[width=7.cm, angle=0,clip=true]{figEfihalo2x}
\caption{Boundary curves for the existence of {excited Efimov
  states in two-neutron halo nuclei with different core masses $A$} as
  function of the {square roots of the} neutron-core energy $E_{nc}$ and
  neutron-neutron energy
  $E_{nn}$ in units of the three-body ground-state energy $E_{gs}$.
  The sign of the square root is taken positive (negative)
  if the corresponding two-body system, $nc$ or $nn$,
  has a bound state (virtual state).  Established halo nuclei are
  shown by the data points while the shaded area gives the parameter
  range for the predicted halo nucleus $^{62}$Ca.
  Reprinted by permission from Springer Nature:
  \cite{Hammer:2018fbe}, copyright (2018).
}
\label{fig:efihalo}
\end{figure}


In 2010, $^{22}$C was established as the {then}
heaviest halo nucleus.
In particular, $^{22}$C was found to display a large matter
radius~\cite{Tanaka:2010zza} and a large $S$-wave component {in its}
$n$-$^{20}$C
{subsystem}~\cite{Horiuchi:2006ds}.  Since the information on the
neutron-core energy
$E_{nc}$ was ambiguous, \textcite{Acharya:2013aea} used Halo EFT to explore the
correlation between the $n$-$^{20}$C energy and the two-neutron separation
energy of $^{22}$C.  Combining this correlation with the matter-radius
measurement, they demonstrated that an excited Efimov state in $^{22}$C
is unlikely.  A recent update of this analysis by \textcite{Hammer:2017tjm},
using the more precise matter radius from \textcite{Togano:2016wyx} as input,
reached the same conclusion.

Whether heavier neutron halos than $^{22}$C exist is still an open question,
although there is some experimental evidence that the ground states of $^{31}$Ne
and $^{37}$Mg have a low one-neutron separation energy and can be considered
deformed $P$-wave halos~\cite{Nakamura:2014hxa,Kobayashi:2014owa}.
This makes it
worthwhile to investigate the possibility for Efimov states in heavier nuclei.



\subsection{\Abinitio methods and Efimov states in heavier nuclei}
\label{sec:halo+abinitio}

Halo EFT can be used in conjunction with \abinitio calculations
to extend the reach of the latter or to test the consistency of different
approaches.  Here, we discuss an example of the former in the context of Efimov
physics.  Further examples regarding electromagnetic reactions will be given
below.

Coupled-cluster calculations by \textcite{Hagen:2012fb} of neutron-rich
calcium isotopes---which used a chiral potential with schematic $3N$ forces and
included coupling to the scattering continuum---suggested that a large $S$-wave
scattering length might occur in the $^{61}$Ca system, with interesting
implications for $^{62}$Ca.  Subsequently, \textcite{Hagen:2013jqa} computed the
elastic scattering of neutrons on $^{60}$Ca obtaining quantitative estimates for
the scattering length and the effective range, and confirming that a large
scattering length can be expected.  These results were then used as input for
Halo EFT in the study of the $^{60}$Ca-$n$-$n$ system.

Specifically, the focus was on signals of Efimov physics that are a consequence
of the large scattering lengths in the $^{60}$Ca-$n$ and $n$-$n$ systems.
This is illustrated in Fig.~\ref{fig:Ca62plot}, where the universal correlation
between the  $^{61}$Ca-$n$ scattering length and the two-neutron separation
energy of $^{62}$Ca is shown.  For $^{62}$Ca with $m_0 = 60 m_1$,
the discrete scaling factor governing the energy spectrum is approximately
$16^2=256$~\cite{Braaten:2004rn}, which is slightly more favorable than in the
case of equal mass particles.  The asymptotic scaling ratio applies only for
deep states or in the unitary limit of infinite scattering length.  Away from
the unitary limit, however, the ratio of energies near threshold can be
significantly smaller---see Fig.~\ref{fig:efiplot} and the corresponding
discussion {by \textcite{Braaten:2004rn}}.  In the case of $^{62}$Ca,
the whole energy region between $S_{2n}\approx 5-8~\keV$ and the breakdown
scale $S_{\mathrm{hi}}\approx 500~\keV$ is available for Efimov states.
At $S_{2n}\approx 230~\keV$, the $^{60}$Ca-$n$ scattering length jumps from
$+\infty$ to $-\infty$ and an excited Efimov state appears.  It is thus
conceivable that $^{62}$Ca would display an excited Efimov state and unlikely
that it would not display any Efimov states at all.  The matter radius of
$^{61}$Ca relative to the $^{60}$Ca core was found to be 4.9(4)~\fm, while the
matter radius of $^{62}$Ca could be even larger, depending on the precise value
of $S_{2n}$.


\begin{figure}[tb]
 \centering
 \includegraphics*[width=7cm, angle=0,clip=true]{61Ca-n-scatt}
 \caption{
  Correlation between the $^{61}$Ca-$n$ scattering length and the
  two-neutron separation energy $S_{2n}$ of $^{62}$Ca.  The emergence of an
  excited Efimov state around $S_{2n}=230$ keV is indicated by the vertical
  dashed line.  The shaded area indicates the region where Halo EFT
  breaks down.
  Figure taken from \cite{Hammer:2016exd}
  under the terms of the Creative Commons Attribution License,
  https://creativecommons.org/licenses/by/4.0/.
}
\label{fig:Ca62plot}
\end{figure}


One can summarize the situation on (excited) Efimov states in halo nuclei as
follows.  While the ground {states} of many $S$-wave halo nuclei {are}
close to the
Efimov limit, there is currently no observed halo nucleus that displays an
excited Efimov state or is likely to display such a state.  There is some
theoretical evidence that the situation could be different for $^{62}$Ca.
The corresponding parameter range is indicated by the shaded square in
Fig.~\ref{fig:efihalo}.   The results of \textcite{Hagen:2013jqa} imply that
$^{62}$Ca is possibly the largest and heaviest halo nucleus in the chart of
nuclei and demonstrated that a large number of observables would display
characteristic features of Efimov physics.  {Measurement} of these
observables
clearly poses a significant challenge for experiment.  For example, $^{58}$Ca is
the heaviest Calcium isotope that has been observed
experimentally~\cite{Tarasov:2009hb}.  However, future radioactive-beam
facilities might provide access to calcium isotopes as heavy as $^{68}$Ca.



\subsection{Higher partial waves and resonances}
\label{sec:highpar}

Next we discuss systems with resonant interactions in higher partial waves.
Such interactions are ubiquitous in halo and cluster nuclei and lead to a
richer power counting structure.

Consider two-body scattering with reduced mass $\mu$ and energy $E=k^2/2\mu$ in
the center-of-mass frame.  Resonance behavior arises when the $S$-matrix has a
pair of poles in the two lower quadrants of the complex $k$ plane.  The
projection of $S$ into the resonant partial wave $l$ can be written

\begin{equation}
 \frac{S_l}{s_l(k)} = \frac{k+k_+}{k-k_+}\, \frac{k+k_-}{k-k_-}
 = \frac{E-E_0-\ii\Gamma(E)/2}{E-E_0+\ii\Gamma(E)/2} \,.
\label{smat}
\end{equation}

{Here $k_\pm= \pm k_R - \ii k_I$ with $k_{R,I} >0$ are the pole positions,
$s_l(k)$ is a smooth function in the energy region under consideration, $E_0
=(k_R^2 + k_I^2)/2\mu$ is the position of the resonance (where the corresponding
phase shift crosses $\pi/2$), and $\Gamma(E)/2= k k_I/\mu$ is referred to as
the half-width of the resonance.  A \emph{narrow} resonance is one for which
$\Gamma(E_0)/{(2E_0)}\ll 1$, that is, for which the poles are near the real
axis,
{$k_I/k_R\ll 1$}.  We call the resonance \emph{shallow} if $|k_\pm| \equiv
\Mlo
\ll \Mhi$.  An example of a shallow, narrow resonance, is given by the
$^2P_{3/2}$ resonance in $n\alpha$ scattering (the ground state of $^5$He),
which has~\cite{Bertulani:2002sz} $\Gamma(E_0)/2\simeq 0.3~\MeV \ll E_0 \simeq
0.8~\MeV \ll E_\alpha \simeq 20\, \MeV$, or $k_I \simeq 6 \, \MeV \ll k_R
\simeq 34~\MeV \ll \sqrt{m_N E_\alpha} \simeq 140~\MeV$, where $E_\alpha$ is
the excitation energy of the $\alpha$ core and $m_N$ is the nucleon mass.}

Shallow resonances can be described in Halo EFT, just as bound states.  For
notational simplicity we take the two scattering particles to be identical, with
mass $m=2\mu$ and no spin.  Generalization to other situations is
straightforward.  Like for bound states, it is convenient to introduce a
dimeron field with the quantum numbers of the resonance.
{Note that the formulation with dimeron fields is equivalent to a
formulation with particle contact interactions.}
{(For details see the discussion by~\textcite{Bertulani:2002sz}
and, for $S$-wave states, Sec.~\ref{sec:pionless}.)}
In the following, we focus on the case where the resonance is in the $l=1$
state, {in which case the dimeron field $d$ has three components
corresponding to spin 1.}  In a notation
similar to Eq.~\eqref{eq:L-NN-simple-d},

\begin{multline}
 {\LL = \psi^\dagger
  \left(\ii\partial_0
  + \frac{\Laplace}{2m}\right)
  \psi
  + d^\dagger_{l}
   \bigg[\eta_1 \bigg(\ii\partial_0+\frac{\Laplace}{4m}\bigg)
   -\Delta_1 \bigg] d_{l}}
   \\
  {\null + \frac{g_1}{4} \left[d^\dagger_{l} (\psi \galnab_{l} \psi)
  +\hc\right]
  + \cdots \,,}
\label{lagdPwave}
\end{multline}

where the Galilean combination $\vNablaLR*=\vNablaL-\vNablaR$ places the two
particles in a $P$ wave.

The full dimeron propagator, depicted in Fig.~\ref{fig:DibaryonProp}, is the
bare propagator given by the inverse of the dimeron kinetic term and dressed by
the bubbles generated by the $d\psi\psi$ interactions in Eq.~\eqref{lagdPwave}.
The two-particle $T$ matrix is obtained by attaching external particle
legs.
The result reproduces the ERE for $P$ waves, Eq.~\eqref{eq:T-kcot}, with

\begin{equation}
 \frac{1}{a_1}
 = \theta_3\Lambda^3-\frac{12\pi\Delta_1}{mg_1^2}
 \mathtext{,}
 {-}\frac{r_1}{2} = \theta_1\Lambda+ \eta_1\frac{12\pi}{m^2g_1^2}\,,
\label{matchingPwave}
\end{equation}

where, as in Eq. \eqref{eq:I0-cutoff}, $\theta_{1,3}$ are numbers that depend on
the chosen regularization.  We see that both the scattering length and effective
range need to be included at LO to absorb all
divergences~\cite{Bertulani:2002sz}.  This requirement has to be reflected by
the power counting for $P$ waves.  We note that the need to include additional
interactions for renormalization at LO will become more severe in higher partial
waves.

For the scaling of the parameters $a_1, r_1, \ldots$, different scenarios can
be envisioned:

\begin{itemize}
\item[(i)]
Na\"ive dimensional analysis suggests that the typical size for the ERE parameters
$a_1, r_1, \ldots$ is given by the appropriate power of the momentum scale
$\Mhi$ where the EFT breaks down.
\end{itemize}

For instance, if the interaction between the particles is described by a
potential of depth $\sim \Mhi$ and range $\sim 1/\Mhi$, one would expect
$a_1\sim 1/\Mhi^3$ and $r_1\sim \Mhi$.  In particular, a resonance or bound
state, if present, generally occurs at the momentum scale $\Mhi$.

Scenario (i) is clearly not appropriate for halo nuclei with shallow resonances
or bound states.  In such systems, the interactions are finely tuned in such a
way as to produce a resonance or bound state close to threshold, at a scale
$\Mlo$ much smaller than $\Mhi$, violating the NDA estimate.  This situation
can occur when one or more of the ERE parameters have unnatural sizes
related to $\Mlo$.

\begin{itemize}
\item[(ii)]
  \textcite{Bertulani:2002sz} proposed a different power counting
  assuming $a_1\sim 1/\Mlo^3$ and $r_1\sim \Mlo$, while all  higher
  ERE parameters scale with $\Mhi$.
\end{itemize}

With this scaling, all three terms of the ERE shown explicitly in
Eqs.~\eqref{eq:T-kcot-a} and~\eqref{eq:T-kcot-b} are of the same order for
momenta $k\sim \Mlo$ and must be retained at LO.  Higher ERE parameters are
suppressed by powers of $\Mlo/\Mhi$ and thus are subleading.

Scenario (ii) requires that \emph{two} combinations of constants,
$\Delta_1/g_1^2$ and $1/g_1^2$, be fine tuned against the large values
$\Lambda \simge \Mhi$ in Eq.~(\ref{matchingPwave}) in order to produce a result
containing powers of the small scale $\Mlo$.  From a naturalness perspective,
this makes it less likely to occur in nature than a scenario with one fine
tuning like the one for an $S$-wave bound state.

\begin{itemize}
\item[(iii)]
  An alternative scaling was suggested by \textcite{Bedaque:2003wa}, where
  $a_1\sim 1/(\Mlo^2\Mhi)$, $r_1\sim \Mhi$, and all other
  ERE parameters again scale with appropriate powers of $\Mhi$.\footnote{A
  similar scheme was applied to the $\Delta(1232)$ resonance
  in Chiral EFT by ~\textcite{Pascalutsa:2002pi} and \textcite{Long:2009wq}.}
\end{itemize}

This scenario requires only \emph{one} combination of constants, namely
$\Delta_1/g_1^2$, to be fine tuned.

With option (iii), the terms proportional to $1/a_1$ and $r_1 k^2$
in the dimeron propagator are of the same order for momenta $k\sim\Mlo$.
The term stemming from the unitarity cut, $\ii k^3$, is suppressed by one power
of $\Mlo/\Mhi$ and is, therefore, subleading.  The remaining terms in the
ERE are even more suppressed.  Thus, LO corresponds to taking the bare dimeron
propagator while the effects of loops and higher-derivative interactions enter
as higher-order corrections.

At LO the difference between the scalings~(ii) and~(iii) is the presence of the
unitarity-cut term $\sim \ii k^3$.  This difference disappears if instead of
considering generic momenta $k$ of order $\Mlo$ we focus onto a narrow region
around the position of the resonance at $k=\sqrt{2/a_1r_1}$.  Due to the near
cancellation
{within a window of size  $\Delta k =
2/a_1r_1^2$ around the pole
between the two
terms that are leading in scenario (iii),}
the unitarity-cut term has to be resummed to all
orders, and provides a width to the resonance.  In this kinematic range there
are two fine tunings: one implicit in the short-distance physics leading to the
unnatural value of $a_1$, and another one explicitly caused by the choice of
kinematics close to the pole.
{
Power counting for resonances is further discussed by \textcite{Gelman:2009be},
\textcite{Alhakami:2017ntb},} {and \textcite{Schmidt:2018vvl}.}

If the underlying theory cannot be solved, the appropriate scaling for a
specific physical system can be
{inferred} from the data, \ie, from the
numerical values of the ERE parameters.  However, such a determination is not
always unique and/or different scalings might apply in different kinematic
regions.
In the first papers on Halo EFT, \textcite{Bertulani:2002sz} and
\textcite{Bedaque:2003wa} applied the scalings~(ii) and~(iii),
respectively, to the lowest resonance in $n\alpha$ scattering.  The experimental
ERE parameters can be accommodated in both scalings such that both appear
viable.  Although the unitarization implicitly carried out in~(iii) is not
necessary except near the resonance, it improves the description throughout the
low-energy region.  In either case, scattering data determine the $n\alpha$
interaction parameters.

The two-neutron halo nucleus $^6$He offers a further testing ground for
Halo EFT with resonant $P$ waves.  The $n\alpha$ interaction in that nucleus is
dominated by the $^2P_{3/2}$ resonance.  The structure and renormalization
of $^6$He were investigated by \textcite{Rotureau:2012yu} and
\textcite{Ji:2014wta}.  \textcite{Rotureau:2012yu} calculated $^6$He at LO in
the Gamow shell model using scenario~(ii) and found that a three-body
force---the analog of $\LL_{3b}$ in Eq. \eqref{eq:lag_05}---is required to
stabilize the system. \textcite{Ji:2014wta} solved the Faddeev equations in
scenario~(iii), but demoted the $^2S_{1/2}$ $n\alpha$ interaction to NLO.
They also found that a three-body force is required for renormalization at LO
and determined its running over a wide range of cutoffs.  The observed behavior
is not log-periodic, although some periodicity is observed.  Alternative
formulations at LO were investigated by \textcite{Ryberg:2017tpv} and shown to
be equivalent{,} {while momentum-space probability densities of ${}^6$He
were calculated by \textcite{Gobel:2019jba}.}

The power counting for resonant partial waves with $l\geq 2$ was also discussed
by \textcite{Bertulani:2002sz} and \textcite{Bedaque:2003wa}.  Their analysis of
the power divergences of the one-loop self-energy showed that
the first $l+1$ ERE parameters are required to absorb all divergences.  This
was confirmed by the Wilsonian RG analysis of \textcite{Harada:2007ua}, which
considered the cases $l=1,2$ explicitly.  An alternative power counting for
bound states with $l=2$ was proposed by \textcite{Braun:2018hug} and applied to
{the description of $D$-wave states in $^{15}$C
and $^{17}$C~\cite{Braun:2018vez}.}



\subsection{Electromagnetic properties and reactions}
\label{sec:haloelectric}

For one-neutron halos{,} Halo EFT essentially reproduces the ERE, but their
electromagnetic structure and reactions can be predicted.  The formalism is
similar to that of Pionless EFT (Sec.~\ref{sec:Currents-ThreeBody}) and serves
to illustrate it.  Moreover, the accuracy limits of cluster models can be
estimated from the order at which gauge-invariant couplings to currents appear.

In the following, we exemplify the power of Halo EFT in the electromagnetic
sector using the example of $^{11}$Be~\cite{Hammer:2011ye} and give a brief
overview of results in other systems.  The first excitation of
$^{10}$Be is $3.4~\MeV$ above the ground state, which has $J^P=0^+$.
Meanwhile, $^{11}$Be has a $1/2^+$ state with neutron separation energy
$B_0=500~\keV$, and a $1/2^-$ state with $2n$ separation energy
$B_1=180~\keV$~\cite{AjzenbergSelove:1990zh}, which we denote $^{11}$Be$^*$.
The shallowness of these two states of ${}^{11}$Be compared to the bound states
of ${}^{10}$Be suggests that they have significant components in which a loosely
bound neutron orbits a ${}^{10}$Be core.  In Halo EFT, the $1/2^+$
state is described as an $S$-wave bound state of the neutron and the core,
while $1/2^-$ is a $P$-wave bound state governed by scenario~(iii) from the
previous section.

The effective Lagrangian for the system can be obtained by combining
Eq.~\eqref{eq:lag_05} for the $1/2^+$ ground state and Eq.~\eqref{lagdPwave}
(generalized to unequal masses) for the $1/2^-$ excited state.  Photons are
included via the minimal substitution, Eq.~\eqref{eq:minimal}, and through the
field strength.  (See \cite{Hammer:2011ye} for explicit expressions.)

Here our focus is on electric properties, and the dominant pieces of the
electric response follow from the minimal substitution~\eqref{eq:minimal}.
But, at higher orders in the computation of these properties, gauge-invariant
operators (counterterms) appear involving the electric field $\mathbf{E}$ and
the fields $c$ for the $^{10}$Be core, $n$ for the halo neutron, {$d$ for
the $^{11}$Be} {ground-state}
{dimeron, and $d^*$ for the $^{11}$Be$^*$} {excited-state} {dimeron.}
Possible one- and
two-derivative operators with one power of the photon field are

\begin{spliteq}
 {\LL_\text{EM} = \;}& {L_{C0} \, d^\dagger
 (
 \vNabla\cdot\mathbf{E})\,d
  + L_{C0}^{(*)} \,d^{*\dagger} (
 \vNabla\cdot \mathbf{E}) \,d^*}
  \\
  & {\null + \ii L_{E1}^{(1/2)} \,\left( [d d^{*\dagger}]_l \,\mathbf{E}_l
  + \hc\right) + \cdots \,,}
\label{eq:nonminimalEM}
\end{spliteq}

where {$[\cdots]_l$} indicates the projection on $l=1$.  If magnetic
properties are to be considered, we have to include operators involving the
magnetic field
${\bf B}$ as well.

The electric interactions in Eq.~\eqref{eq:nonminimalEM} are gauge invariant
by themselves, and so we must determine the order at which they occur.
Rescaling the fields to absorb all powers of $\Mlo$ as
{
done by \textcite{Beane:2000fi},}
the scaling of the coupling constants with $\Mlo$ can be obtained from
NDA~\cite{Hammer:2011ye}.  As a consequence, the leading effects in the
charge-radius-squared of the $1/2^-$ state in ${}^{11}$Be are
$\sim (r_1 \Mlo)^{-1} \sim (\Mlo\Mhi)^{-1}$.  The operator proportional to
{$L_{C0}^{(*)}$} produces effects of order $(r_1 \Mhi)^{-1} \sim
(\Mhi)^{-2}$, and thus affects the prediction for the charge radius at NLO.
Similarly, the E1($1/2^+ \rightarrow 1/2^-$) matrix element has parametric
dependence $\Mlo^{-1} (\Mlo\Mhi)^{-1/2}$.  Including the proper wavefunction
renormalization factors, the operator with LEC $L_{E1}^{(1/2)}$
yields an effect $\sim \Mhi^{-1} (\Mlo\Mhi)^{-1/2}$, and so also  occurs already
at NLO.  {Thus for electric quantities involving the shallow $1/2^-$
excited state of $^{11}$Be there are two
parameters in the Halo EFT description
at NLO which cannot be fixed with ${}^{10}$Be-$n$
scattering information
alone. There are none at LO and presumably more at N$^2$LO.}
