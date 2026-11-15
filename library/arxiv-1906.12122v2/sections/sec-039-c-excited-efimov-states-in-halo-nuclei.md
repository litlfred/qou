---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear eﬀective ﬁeld theory: status and perspectives"
section_id: sec-039-c-excited-efimov-states-in-halo-nuclei
section_title: "C Excited Efimov states in halo nuclei"
section_number: null
pages: 27-29
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.99
doc_brief: "Nuclear eﬀective ﬁeld theory: status and perspectives — 82 sections: Nuclear effective field theory: st; Contents; I Introduction"
---
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
