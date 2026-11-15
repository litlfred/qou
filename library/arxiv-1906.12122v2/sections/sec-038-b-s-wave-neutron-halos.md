---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear eﬀective ﬁeld theory: status and perspectives"
section_id: sec-038-b-s-wave-neutron-halos
section_title: "B S-wave neutron halos"
section_number: null
pages: 26-27
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.98
doc_brief: "Nuclear eﬀective ﬁeld theory: status and perspectives — 82 sections: Nuclear effective field theory: st; Contents; I Introduction"
---
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
