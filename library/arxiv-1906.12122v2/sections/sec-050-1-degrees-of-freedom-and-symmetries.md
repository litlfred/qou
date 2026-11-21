---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear eﬀective ﬁeld theory: status and perspectives"
section_id: sec-050-1-degrees-of-freedom-and-symmetries
section_title: "Degrees of freedom and symmetries"
section_number: 1
pages: 39-40
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.983
doc_brief: "Nuclear eﬀective ﬁeld theory: status and perspectives — 82 sections: Nuclear effective field theory: st; Contents; I Introduction"
---
\label{subsubsec:Dofssymms}

By extending the Pionless EFT of Sec.~\ref{sec:pionless} to include an
isovector field $\vec\pi$ that collects the three charged pion states one
develops a
representation of QCD for $Q\sim m_\pi$, with $m_\pi$ now among the low-energy
scales collectively denoted by $\Mlo$.  In this EFT, pion exchange among
nucleons generates amplitudes that are no longer given by the ERE or a simple
generalization thereof.  Instead, there appear non-analytic functions of
$Q/m_\pi$ in all amplitudes.

The lightness of the pions relative to other hadrons can be explained naturally
if they are identified with the pseudo-Goldstone bosons of the spontaneous
breaking of (approximate) chiral symmetry, $SU(2)_{\rm L}\times
SU(2)_{\rm R}$ for two flavors.  In the chiral limit ($\bar m=0$,
$\varepsilon=0$, $e=0$), the QCD Lagrangian~\eqref{QCDL} has an exact chiral
symmetry.  In contrast, the spectrum shows only an approximate isospin
symmetry, $SU(2)_{\rm V}$.  {Close to} the chiral limit
$SU(2)_{\rm L}\times SU(2)_{\rm R}$ is an approximate symmetry of Eq.~\eqref{QCDL}.
Pions, which have vanishing mass in the chiral limit, acquire a relatively
small but
non-zero common squared mass $m_\pi^2=\OO(\MQCD \bar m)$ and a square-mass
splitting $\delta m_\pi^2=\OO(\alpha \MQCD^2/4\pi, \varepsilon^2 m_\pi^4/\MQCD^2)$
between charged and neutral states.

Pions should play a special role as long as $\bar m\ll \MQCD$.  In this section
we consider this regime, where we integrate out all other mesons because they
are expected to have masses $\OO(\MQCD)$.  The lightest of these is the
$\sigma$ with spin $S=0$ and isospin $I=0$, and a mass (half-width)
$m_\sigma=441~\MeV$ ($\Gamma_\sigma/2 =2 71~\MeV$)~\cite{Caprini:2005zr}.  This
suggests that the EFT radius of convergence is no larger than $\Mhi\sim
\sqrt{m_\sigma^2+ \Gamma_\sigma^2/4} \simeq 500~\MeV$.  The hadronic
EFT of QCD beyond this scale is not known.  The problem is power counting: by
NDA, interactions with derivatives will produce powers of $Q/\MQCD$ in
amplitudes; thus, as $Q$ approaches $\MQCD$ all interactions are equally
important.  To incorporate mesons in an EFT we need an argument that, at least
at a formal level, justifies treating their masses and interactions as small
with respect to $\MQCD$.  Typically this is accomplished by assuming QCD to
have further approximate symmetries.  For example, scale symmetry has been
invoked in the context of three flavors to justify the inclusion of a
scalar-isoscalar meson~\cite{Crewther:2013vea} and a dynamical ``vector''
symmetry~\cite{Georgi:1989gp} postulated for the $\rho$ meson.  Although very
interesting, such schemes have so far met with limited success, if any, away
from the mesonic sector.

One must, however, consider the effects of nucleon excitations. As mentioned in
Sec.~\ref{sec:introduction}, for $Q\ll m_N \sim \MQCD$, the nucleon mass is
inert.  For baryon-number conserving processes, the relevant mass scale
for other baryons is their mass splitting from the nucleon.  The Delta isobar
with $S=3/2$ and $I=3/2$ lies at $m_\Delta - m_N -i \Gamma_\Delta/2 \simeq (270
- 50\ii)~\MeV$~\cite{Arndt:2006bf}.  Although the mass difference $m_\Delta -
m_N$ does not vanish in the chiral limit, it is relatively small, in line with
arguments based on a large number of colors $N_{\rm c}$: when QCD is generalized
to an $SU(N_{\rm c})$ gauge theory, $m_\Delta - m_N=\OO(\MQCD/N_{\rm c})$.
A Deltaless version of Chiral EFT exists where the Delta isobar is integrated
out, but it fails before one reaches the Delta region in $A=1$ processes, which
leads to relatively large errors in $A\ge 2$
systems~\cite{Pandharipande:2005sx}.  To increase the radius of convergence
beyond $\sim \sqrt{(m_\Delta - m_N)^2 + \Gamma_\Delta^2/4} \simeq 275~\MeV$,
one {introduces~\cite{Jenkins:1991es,Hemmert:1997ye}}
a heavy field $\Delta$---a
four-component
object in spin and isospin space with the nucleon mass $m_N$ removed from its
rest energy.  As a consequence, the Delta kinetic energy and interactions are
also expanded around the non-relativistic limit.  Apart from the spin/isospin
structure, the main difference with respect to the nucleon is that a term
linear in the mass difference $m_\Delta - m_N$ (included in $\Mlo$) remains in
the Lagrangian.
{
Explicit Delta propagation improves the description of data beyond threshold
\cite{Fettes:2000bb} and} enlarges the realm
of Chiral EFT beyond the Delta region once the power counting is properly
reformulated~\cite{Pascalutsa:2002pi,Long:2009wq}.

Whether other nucleon excitations should be introduced in Chiral EFT is less
clear.  The Roper resonance~\cite{Roper:1964zza} is special for several
reasons~\cite{Long:2011rt}.  First, its pole appears at an energy not much
above the Delta, $m_R - m_N - \ii\Gamma_R/2 \simeq (420 -
80\ii)~\MeV$~\cite{Arndt:2006bf}.   Other resonances lie at least $\Mhi\simeq
500~\MeV$ above threshold---the next resonance ($S_{11}$) has a mass $m_{S_{11}}
- m_N\simeq 500~\MeV$~\cite{Arndt:2006bf}---and it is difficult to see why they
should be incorporated in the EFT without the concomitant inclusion of meson
resonances.  Second, the Roper width is, numerically, $\Gamma_R\sim
\Gamma_\Delta (m_R - m_N)^3/(2(m_\Delta - m_N)^3)$, as expected from ChPT widths
scaling as $Q^3/\MQCD^2$.  This is not true for higher resonances, which
typically have relatively smaller widths.  As a consequence, the Delta and the
Roper nearly saturate the Adler-Weisberger sum rule, a result which suggests
that, together with the nucleon{,} they fall into a simple reducible
representation of the chiral group~\cite{Weinberg:1969hw,Beane:2002ud}.
Inclusion of an explicit Roper
{field~\cite{Banerjee:1995wz,Gegelia:2016xcw}}
improves the convergence of Chiral EFT around the Delta
resonance~\cite{Long:2011rt}, but it has not been systematically investigated.
In the following we consider Chiral EFT with nucleon and Delta fields only.
