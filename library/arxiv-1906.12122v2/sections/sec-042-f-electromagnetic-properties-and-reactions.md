---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear eﬀective ﬁeld theory: status and perspectives"
section_id: sec-042-f-electromagnetic-properties-and-reactions
section_title: "F Electromagnetic properties and reactions"
section_number: null
pages: 31-32
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.984
doc_brief: "Nuclear eﬀective ﬁeld theory: status and perspectives — 82 sections: Nuclear effective field theory: st; Contents; I Introduction"
---
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
