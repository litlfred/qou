---
doc_id: arxiv-hep-lat-0003021v3
doc_title: "arXiv:hep-lat/0003021v3 19 May 2000"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-4
source_pdf: 0003021v3.pdf
source_sha256: b35dfd9ab88b71d8
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 1.0
doc_brief: "arXiv:hep-lat/0003021v3 19 May 2000 — We compute the low-lying spectrum of the staggered Dirac operator above and below the ﬁnite temperature phase transition in both quenched QCD and in dynamical"
---
The correlations of Dirac operator eigenvalues in QCD and related 
theories have been shown to have a fascinating relation to Random Matrix
Theory. There are two very different domains of interest here. One is
the so-called ``bulk'' of the eigenvalue spectrum of the Dirac operator,
far from both the infrared and the ultraviolet ends. The other is the
so-called ``hard edge'' at $\lambda \sim 0, ~i.e.$ the infrared end of the 
spectrum in theories with spontaneous breaking of chiral symmetry. The
relevance of Random Matrix Theory in describing eigenvalue correlations
of the Dirac operator in the bulk of the spectrum was first demonstrated
by Halasz and Verbaarschot \cite{HV}, and it has since been confirmed
by numerous lattice gauge theory studies \cite{bulk}. {}From a theoretical
point of view, these results in the bulk of the spectrum remain to be
better understood. In the other case, near $\lambda \sim 0$, the connection
between universal Random Matrix Theory results and the QCD Dirac operator 
spectrum \cite{SV,V,ADMN} is by now firmly established, and has also been
extensively checked in lattice gauge theory simulations \cite{latedge}. 
Already in the original work
of Shuryak and Verbaarschot \cite{SV} it was shown that the pertinent
chiral Random Matrix
Theory partition function coincides exactly with the effective field theory
partition function in the relevant microscopic
limit. More recently an explicit relationship between the 
universal Random Matrix Theory eigenvalue distributions
and those of the QCD Dirac operator has been established \cite{AD,OTV},
the precise link being the partially quenched chiral condensate
\cite{OTV,DS}. In this domain Random Matrix Theory is an intriguing alternative
description of exactly the same phenomena that can be derived from the
effective QCD partition function in the large-volume limit where $V \ll 
1/m_{\pi}^4$ \cite{LS}.

\noi
There exists also an interesting physical situation that forces us to
reconsider the two different domains of the Dirac operator spectrum
simultaneously. This is near the finite-temperature chiral phase transition,
where the analytical connection between the effective QCD partition function
and Random Matrix Theory breaks down even for the part of the spectrum
that is close to $\lambda=0$. This situation is readily confronted in
lattice gauge theory. Indeed, it is for staggered fermions even rigorously
proven~\cite{Tomboulis}, that chiral symmetry is restored at high
temperature. The low-lying spectrum of the Dirac operator must therefore
be quite different in the high temperature phase as compared with zero
temperature. In particular, the absence of chiral symmetry breaking
implies, through the Banks-Casher relation,
\begin{equation}
 \langle \bar\psi \psi \rangle ~=~ \pi \rho(0) ~,
\label{eq:Banks}
\end{equation}
that the density of eigenvalues at zero vanishes. This could happen either
just at that point of $\lambda=0$ (as, for example, in the free theory
where $\rho(\lambda) \sim \lambda^3$), or the spectrum could develop a gap.
The chiral phase transition occurs at the temperature $T_c$ where the
density of Dirac operator eigenvalues just reaches zero at $\lambda=0$.
If the transition is continuous, this will happen smoothly as the temperature
$T$ is increased towards $T_c$. In such a case, an important question
to settle is the precise power-law behavior of the spectral density of the 
Dirac operator right at $T=T_c$, 
because this can be related to the critical exponents
of the phase transition \cite{Z}. 
The same chiral Random Matrix Theory
that yields universal microscopic spectral correlators which exactly
coincide with those of the Dirac operator at $T=0$ can be tuned
in such a way as to just reach (multi-critical) points where \cite{ADMN2} 
\beq
\rho(\lambda) ~\sim~ \lambda^{2k}
\eeq
near $\lambda = 0$. Here $k$ is an integer labeling the multi-criticality.
At such points universality of microscopic spectral correlators still 
holds in the Random Matrix Theory
context, but there is no justification for assuming that these results
are relevant for the Dirac operator spectrum at $T=T_c$.\footnote{In 
particular, this behavior is only compatible with a continuous phase
transition. But at a more fundamental level, there is simply no longer
any relation between the chiral Random Matrix Theory ensemble and the
effective QCD partition function for temperatures $T$ that do not satisfy
$T \ll \Lambda_{QCD}$.} There is also
a schematic Random Matrix model for the finite-temperature behavior of
the Dirac operator spectrum \cite{JV}. It gives a different behavior
at $T=T_c$: $\rho(\lambda) \sim \lambda^{1/3}$. Also here there is no
physical
justification for using it in connection with the Dirac operator
spectrum at finite temperature, but it is an interesting model
that depends on just one deterministic external parameter, and we shall
therefore return to it below.

\noi
Suppose, for a moment, that the Dirac spectrum actually develops a gap
around $\lambda=0$ above $T_c$.
In Random Matrix Theory the end of a spectrum around such a
gap is referred to as a ``soft edge''. 
Generally, the (macroscopic) density
of eigenvalues near a soft edge behaves as (for $\lambda > 
\lambda_0$) \cite{Brezin}:
\begin{equation}
\rho(\lambda) ~\propto~ (\lambda - \lambda_0)^{2m+1/2}
\label{eq:se_rho}
\end{equation}
with $\lambda_0$ being the location of the edge. Here $m$ is an 
integer that labels universality classes classified by their Random Matrix
Theory potentials ($m$ parameters in the potentials must be tuned in
order to reach each class). Thus the {\em generic} behavior, without any
fine tuning, corresponds to $m=0$, which gives a square root approach to
the soft edge:
\begin{equation}
\rho(\lambda) ~\propto~ (\lambda - \lambda_0)^{1/2}
\label{eq:sqrt_rho}
\end{equation}
Random Matrix Theory actually gives a more detailed, microscopic, 
description. This arises from a blowing-up of the eigenvalue density function
around the soft
edge $\lambda_0$ with a rescaling according to the macroscopic
behavior (\ref{eq:se_rho}). For example, for the generic $m=0$ universality
class, the corresponding microscopic eigenvalue density is 
~\cite{Forrester}
\begin{equation}
\rho(\lambda) ~\propto~ X [{\rm Ai}(-X)]^2 + [{\rm Ai}^\prime(-X)]^2 ~,
\label{eq:Airy_rho}
\end{equation}
where $X \propto (\lambda - \lambda_0) N^{2/3}$ and ${\rm Ai}(x)$ is
the standard Airy function. Here $N$ denotes the size of the matrix, and
the rescaling by $N^{2/3}$ is required in order to spread out the increasing
number of eigenvalues to obtain one well-defined limiting function.
{}From the known asymptotic behavior of the Airy
functions one finds:
\begin{equation}
\rho(\lambda) \sim \cases{
 \frac{\sqrt{X}}{\pi} + {\cal O}\left(\frac{1}{X}\right) &
 \mbox{\textrm{for $X \to \infty$}} \cr
 \frac{17}{96\pi} |X|^{-1/2} \exp( -4 |X|^{3/2} /3) &
 \mbox{\textrm{for $X \to -\infty$}} \cr }
\label{eq:Airy_asympt}
\end{equation}
Thus, at the microscopic level the spectrum is not cut off sharply at
$\lambda_0$, but has an exponentially suppressed tail beyond.
Further, the square root behavior of the eigenvalue density is
modulated by wiggles corresponding to the distribution of particular
eigenvalues (smallest, second, third, etc.).
(See, for example, Fig.~\ref{fig:Airy_compare}.)

\noi
Until a few months ago, 
there existed only one low-statistics investigation of the
low-lying Dirac eigenvalue spectrum for staggered fermions in the high 
temperature phase~\cite{KLS}. It did not unequivocally 
establish the existence of a gap. For example, some low
eigenvalues were found. However, they could possibly
be attributed to ``would-be zero
modes'' from global gauge field topology, shifted away from zero by the
explicit chiral symmetry breaking of staggered fermions at finite
lattice spacing~\cite{Vink}. This is a general problem with staggered
fermions that also we must face here: 
at finite lattice spacing, the index theorem is not valid for 
staggered fermions, and
gauge field topology (whichever way one defines it on a discrete lattice)
does not give rise to exact zero modes of the staggered Dirac
operator. At $T=0$ no
trace of non-trivial gauge field topology on the lowest-lying
spectrum of staggered eigenvalues has been found \cite{DHNR}, except
in the 2-d Schwinger model at fairly small lattice
spacing~\cite{FHL}. Finite temperature,
which causes a depletion of genuine non-zero eigenvalues near 
$\lambda \sim 0$, further complicates this issue of a mix-up with 
would-be zero modes.

\noi
Very recently a study of just the
low-lying Dirac operator eigenvalues near $T_c$ has actually indicated
the presence of a gap at large lattice volumes \cite{Fetal}.
Again the statistics was rather limited, and only a small number of
the lowest-lying eigenvalues could be included (varying between 8 and 10).
The present
study will in many ways follow the same lines of thought as Ref.~\cite{Fetal},
but we shall have much larger statistics, and we shall also probe some
different aspects. In particular, we are also interested in seeing
whether quenching causes a different behavior of the smallest eigenvalues
near $T_c$ compared with dynamical fermions.
 
\noi
Last year a study of low-lying eigenvalues of the overlap Dirac operator
in quenched finite temperature gauge theories appeared~\cite{EHKN_fT}.
Overlap fermions are well suited for such an investigation since they
do not suffer from explicit chiral symmetry breaking even at finite lattice
spacing and since they have exact zero modes in topologically non-trivial
gauge fields. Ref.~\cite{EHKN_fT} found that effects
of topology persisted in the high temperature phase, although strongly
suppressed compared to the low temperature phase.
More interestingly, an accumulation of low eigenvalues 
with an apparently finite density in the infinite-volume limit was found
very near $\lambda\sim 0$ even above the (quenched) phase transition
temperature $T_c$.  The statistical properties of the 
smallest group of eigenvalues
were consistent with them being due to a dilute gas of instantons and
anti-instantons \cite{EHKN_fT}. These results have led to the speculation
that chiral symmetry might remain
broken even in the high temperature phase of quenched QCD with overlap
fermions. 

\noi
In this paper we describe high statistics investigations of the low-lying
eigenvalue spectrum of the staggered Dirac operator for SU(3) gauge group
at finite
temperature. We do this for both quenched (section~\ref{quenched}) and
dynamical QCD with four flavors of staggered fermions
(section~\ref{dynamical}). The interest in the quenched case lies primarily
in checking whether also staggered fermions, although insensitive to
topology at the gauge couplings we can investigate here, show signs of
unusual behavior of the smallest Dirac eigenvalues above $T_c$ (as was the
case for overlap fermions \cite{EHKN_fT}). Both
quenched and unquenched simulations give rise to Dirac operator spectra
that can be compared with Random Matrix Theory. In particular, if the
Dirac operator spectrum exhibits a gap, is it of the soft-edge kind of
Random Matrix Theory? Are there indications that Random Matrix Theory
provides a more accurate description of the Dirac operator spectrum
as the three-volume is increased? We shall try to answer these questions
in what follows.
