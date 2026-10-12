---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear effective field theory: status and perspectives"
section_id: sec-020-2-chiral-lagrangian
section_title: "Chiral Lagrangian"
section_number: 2
pages: 40-42
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
doc_brief: "Nuclear effective field theory: status and perspectives — 34 sections: Contents; Two-body scattering amplitude; Power counting"
text_source: latex
latex_prose_ratio: 0.886
latex_coverage_ratio: 0.961
---
\label{subsubsec:chiLag}

The construction of the most general chiral Lagrangian is based on the
theory of the non-linear realization of a
symmetry~\cite{Weinberg:1968de,Coleman:1969sm,Callan:1969sn}.  Different
parametrizations of the three-dimensional sphere $SU(2)_{\rm L}\times SU(2)_{\rm
R}/SU(2)_{\rm V} = SO(4)/SO(3)\sim S^3$ correspond to different choices of
pion fields.  Observables are of course independent of this choice.  Pions
appear in the chiral Lagrangian always as $\vec{\pi}/f_\pi$, where the
pion decay constant $f_\pi\simeq 92~\MeV$ is determined by the radius of $S^3$.
Because the three pions cannot provide a linear realization of $SO(4)$, they
transform non-linearly under chiral symmetry, so each term in the chiral
Lagrangian is associated with an infinite tower of interactions in powers of
$(\vec{\pi}/f_\pi)^2$.  Nucleon
{
$N=( p \; n)^T$ and Delta $\Delta =(\Delta^{++}
\; \Delta^{+} \; \Delta^{0} \; \Delta^{-})^T$ fields}
can be chosen to transform under
chiral symmetry just as under an isospin rotation, but with an angle linear in
the pion field.  Covariant derivatives of the pion and baryon fields can be
defined so that they transform in the same way.  They are
$D_\mu=(1-\vec{\pi}^2/4f_\pi^2 +\cdots)\partial_\mu$ and
{$\mathcal{D}_\mu=\partial_\mu  + \ii \vec{\tau} \cdot (\vec{\pi}\times
\partial_\mu\vec{\pi})/4f_\pi^2+\cdots$}
for the pion and nucleon, respectively, where $\vec{\tau}$ are the Pauli
matrices in isospin space.  For the Delta, the form is the same as for the
nucleon with $\vec{\tau}$ replaced by the $I=3/2$ representation of $SO(3)$.
Delta-nucleon transition operators involve a set of $2\times 4$ isospin
matrices $\vec{T}$.
{
Details
are given, \eg, by \textcite{Ordonez:1995rz}.}

The chiral Lagrangian is automatically chiral-invariant if it is built from
isospin-symmetric operators involving the baryon fields, their covariant
derivatives, and the pion covariant derivative.  Chiral-symmetric interactions
of the pions are thus proportional to the momentum.  Away from the chiral limit,
quark masses and electromagnetic interactions break chiral symmetry and even
the isospin subgroup.  The symmetry breaking pattern is known from
Eq.~\eqref{QCDL}, and interactions in the EFT are constructed to behave the
same way.  Thus, although chiral symmetry is not exact, information about QCD
is contained also in the {chiral-symmetry breaking} interactions.
These interactions {do not necessarily involve derivatives, but must be}
proportional to powers of the small parameters
$\bar m/\MQCD$, $\varepsilon$ and $e$, as well as the coefficients of
higher-dimensional operators (including violations of parity, time-reversal,
and possibly baryon-number and Lorentz invariance{)}.
The parameter $\bar m/\MQCD$ can be traded for
{$m_\pi^2/\MQCD^2$,}
while $\varepsilon$ and $e$ govern isospin-breaking quantities.
{
Electromagnetic
interactions are constrained by $U(1)_{\rm em}$ gauge invariance and appear in
two ways:

\textit{i)}
between low-energy photons and other fields \via chiral-covariant derivatives
enlarged to be gauge-covariant as well, and \via the electromagnetic field
strength;

\textit{ii)} among hadronic fields that originate in integrating
out energetic photons.
}


{Overall, chiral symmetry and its known breaking pattern}
{lead to a} {low-energy expansion because all interactions of pions
among} {themselves} {or with nucleons involve} {
derivatives (which bring powers of $Q\sim \Mlo$ to amplitudes),
powers of $m_\pi^2\sim \Mlo^2$, or powers of smaller parameters.}
Choices of fields with
different chiral-transformation properties do not change this feature, but will
in general require delicate cancelations among different interactions.

As in Pionless EFT, it is most convenient to choose a heavy nucleon for which
the Dirac matrices reduce to the Pauli spin matrices $\boldsigma$.
Analogously, one can employ a heavy Delta field using the corresponding $S=3/2$
matrices.  Nucleon-Delta bilinears can be constructed with $2\times 4$ spin
transition matrices $\boldS$ analogous to the isospin
transition matrices $\vec{T}$.  Incorporating Lorentz invariance---in an
expansion in $Q/m_N$---is thus no more difficult in Chiral EFT than in Pionless
EFT.  In recent years it has become popular to use ``covariant'' baryon fields
from which the nucleon mass is not subtracted.  As any field redefinition, such
choices cannot affect observables in an essential way: amplitudes obtained from
different fields but the same power counting can only differ by higher-order
terms.  Although these differences are sometimes interpreted as an
indication of the ``best'' field choice, they merely reflect the error of
the truncation.

The baryon-number-conserving chiral Lagrangian can be split into pieces with
even numbers of fermion fields, $\LL= \LL_{f=0} + \LL_{f=2} + \LL_{f\ge 4}$,
where

\begin{subequations}
\label{chiLag}
\begin{multline}
 \LL_{f=0} =
 \frac{1}{2}
 \left[ \left(D_0 \vec\pi\right)^2 -(\boldD\vec\pi)^2
 - m_\pi^2\vec\pi^2 \left(1-\frac{\vec{\pi}^2}{4f_\pi^2}+\cdots\right)\right] \\
 \null + \cdots \,,
\label{chiLagpi}
\end{multline}

\begin{multline}
 \LL_{f=2} =
 N^\dagger \left(\ii \mathcal{D}_0 + \frac{\boldcalD^2}{2m_N} \right) N
 + \frac{g_A}{2f_\pi} N^\dagger\vec\tau \boldsigma N \cdot \boldD \vec{\pi} \\
 \null + \Delta^\dagger  \left(\ii \mathcal{D}_0 +m_N - m_\Delta \right)\Delta
 \\
 + \frac{h_A}{2f_\pi} \left(N^\dagger \vec{T} \boldS \Delta + \hc\right)
 \cdot \boldD \vec{\pi}
 + \cdots \,,
\label{chiLag1bar}
\end{multline}

\begin{widetext}
\begin{multline}
 \LL_{f\ge 4} =
 {-}\frac{C_{0\textrm{t}}}{2}
 \left(N^T\pPt N \right)^\dagger \left(N^T \pPt N \right)
 - \frac{1}{2}\left[C_{0\textrm{s}}
 + D_{2\textrm{s}}m_\pi^2\left(1-\frac{\vec\pi^2}{2f_\pi^2}+\ldots\right)\right]
 \left(N^T\pPs N \right)^\dagger \left(N^T \pPs N \right) \\
 \null - \frac{C_{2\textrm{s}}}{8}\Big\{\left(N^T\pPs N \right)^\dagger
 \big[N^T \pPs \boldcalD^2 N  + (\boldcalD^2 N)^T \pPs N\big] + \hc\Big\}
 - \frac{C_{2\textrm{t}}'}{4}
 \Big[
 \left(N^T \pPt \boldcalD N \right)^\dagger \cdot
 \left(N^T \pPt \boldcalD N \right) \\
 \null + \left((\boldcalD N)^T \pPt N \right)^\dagger \cdot
 \left((\boldcalD N)^T \pPt N \right)
 \Big]
 + \frac{G_A}{2f_\pi}  N^\dagger\!N \, N^\dagger \boldsigma\vec\tau N
 \cdot \boldD\vec\pi
 -H_0 \, N^\dagger\!N \, N^\dagger\!N \, N^\dagger\!N
 + \cdots \,,
 \label{chiLag2bar}
\end{multline}
\end{widetext}
\end{subequations}

with LECs $g_A$, $h_A$, {$C_{0\textrm{s,t}}$, $D_{2\textrm{s}}$,
$C_{2\textrm{s}}$, $C_{2\textrm{t}}'$, $G_A$}, and $H_0$, and where we used a
notation similar to Eq.~\eqref{eq:L-NN}.  Only a few representative interactions
are shown explicitly here, others (including more fields, derivatives, powers of
$m_\pi^2$, isospin breaking, \etc) being relegated to the ``$\cdots$''.  Note
that many terms can be written in different forms with Fierz reordering and/or
field redefinitions.  One can also introduce dibaryon fields as described in
Sec.~\ref{sec:Dibaryons}
{and done,
for example, by~\textcite{Soto:2011tb} and \textcite{Long:2013cya}.}

Particularly convenient for nuclear processes, where nucleon energies and
momenta are of very different magnitudes, is to use field redefinitions to
eliminate time derivatives of the nucleon field in favor of spatial derivatives.
When interaction terms appear in the classical Lagrangian which depend on time
derivatives, the effective Lagrangian obtained \via the path integral of the
Hamiltonian contains additional
terms~\cite{Charap:1970xj,Salam:1971sp,Honerkamp:1996va,Charap:1971bn,
Gerstein:1971fm}.  These do not vanish in general if a momentum cutoff is
used.  Generally, the easiest way to respect symmetries is to implement
regulators as operators in the chiral Lagrangian constructed from
chiral-covariant objects
{\cite{Slavnov:1971aw,Djukanovic:2004px,Long:2016vnq}.}

If $m_\Delta-m_N$ is considered a large scale, the Delta is integrated out
and appears only through LECs starting at one order higher than in the Deltaful
EFT.  If $m_\pi$ is also considered a large scale, pions are integrated
out as well.  Although the chiral Lagrangian formally reduces to the pionless
form~\eqref{eq:L-NN} when terms with pions and Deltas are omitted from
{
Eq.~\eqref{chiLag}}, one should keep in mind that the remaining LECs depend on
what degrees of freedom appear in the EFT.



\subsection{Chiral Perturbation Theory and the nuclear potential}
\label{subsec:chiralpot}

A great advantage of EFT over earlier attempts to describe nuclear physics from
field theory is its explicit focus on the regime of momenta well below the
nucleon mass, where the theory splits into sectors of fixed nucleon number $A$.
As pointed out in Sec.~\ref{sec:introduction}, there are significant
differences between $A\le 1$ and $A\ge2$ processes.



\subsubsection{Power counting}
\label{subsubsec:PC}

To express amplitudes in an expansion in powers of $Q/\MQCD$, as in
Eq.~\eqref{Texp}, one needs to count powers of both $Q\sim \Mlo$ and $\MQCD$.
For $Q$ one first relates nucleon energies and momenta, and this relation in
general depends on the sector of the theory.  For $A\le 1$, typically (but not
always) $E=\OO(Q)$, while $A\ge 2$ processes with only nucleons in external
legs involve energies $E=\OO(Q^2/m_N)$.  For pions, since we count $m_\pi$ as
$\Mlo$, $E=\OO(Q)$.  The crucial assumption in counting powers of $\MQCD$ is
naturalness, namely that an LEC needed to eliminate cutoff dependence of a loop
at a certain order has finite pieces of the same order.

For an $A\le 1$ Feynman diagram, the various elements scale (after
renormalization) as:

\begin{subalign}[eq:ChPTPC]
 \text{derivative} &\sim  Q \,,
\label{derivative} \\
 \text{baryon, pion propagator} &\sim Q^{-1}, Q^{-2} \,,
\label{props} \\
 \text{(pion) loop integral} &\sim (4\pi)^{-2}Q^4 \,,
\label{loopintegral}
\end{subalign}

where the factor of {$(4\pi)^{{-}2}$} is typical of relativistic loops.  The
sizes of LECs
can be estimated \via NDA, Eq.~\eqref{NDA}.  Chiral-symmetric operators
depend on arbitrary powers of the reduced strong-coupling constant $g_{\rm
red}=g/(4\pi)$, which for consistency should be taken as 1.  NDA applied to
Eq.~\eqref{chiLagpi} gives $f_\pi = \OO(\MQCD/4\pi)$, and for a generic
LEC~\cite{Manohar:1983md,Georgi:1986kr}

\begin{equation}
 c_i=\OO\left(\frac{c_{i,\text{red}}}{f_\pi^{f_i+p_i-2} \MQCD^{\Delta_i}}\right)
 \,,\quad \Delta_i\equiv d_i+f_i/2 -2 \,,
\end{equation}

where $d_i$, $f_i$ and $p_i$ the number of, respectively, derivatives, baryon
fields, and pion fields of the corresponding operator.  The reduced LEC
$c_{i,\text{red}} = \OO(1)$ for a chiral-symmetric operator.  NDA is consistent
with the non-relativistic expansion since applied to Eq.~\eqref{chiLag1bar} it
gives $m_N=\OO(\MQCD)$.  Keeping explicit Deltas means, however, that we are
taking $(m_\Delta -m_N)_{\rm red}=\OO(\Mlo/\MQCD)\ll 1$, as suggested by
large-$N_{\rm c}$ arguments.  A {chiral-symmetry breaking} operator stemming from
the quark masses will have a reduced LEC proportional to powers of
${\bar m}_{\rm red}={\bar m}/\MQCD=m_\pi^2/\MQCD^2=\OO(\Mlo^2/\MQCD^2)$ and
$\varepsilon\simle \OO(1)$, using that $m_\pi^2=\OO(\MQCD \bar{m})$ when NDA
is again applied to Eq.~\eqref{chiLagpi}.
The effect of integrating out hard photons is given by powers of
$e_{\rm red}^2 = (e/(4\pi))^2\simle \OO(\Mlo^3/\MQCD^3)$~\cite{VanKolck:1993ee,
vanKolck:1995cb} in the corresponding
reduced LEC.\footnote{How one accounts for $e_{\rm red}$ relative to other
parameters is somewhat ambiguous, and to some extent a matter of convenience.
Sometimes the choice $e_{\rm red}^2=\OO(\Mlo^2/\MQCD^2)$ is made in the
literature.  This choice leads a pion mass splitting
$\delta m_\pi^2=\OO(\alpha \MQCD^2/4\pi)=\OO(m_\pi^2)$
and to a Coulomb potential comparable to OPE for momenta $Q\sim m_\pi$.
That means electromagnetic effects at LO, an overestimate.  A similar
ambiguity affects $\varepsilon\simeq 1/3$, which
can be counted as $\OO(1)$ or as $\OO(\Mlo/\MQCD)$.}
If we take  $\varepsilon=\OO(1)$, then
$c_{i,\text{red}} = \OO(\Mlo^{n_i}/\Mhi^{n_i})$ where $n_i$ counts the powers of the
low-energy scales $m_\pi$, $m_\Delta -m_N$ and $(e/(4\pi))^{2/3}m_N$.
It is convenient to enlarge the definition of $d_i$ to include $n_i$ as well.
The interactions displayed in Eqs.~\eqref{chiLagpi} and~\eqref{chiLag1bar}
then have $\Delta_i=0$, except for the nucleon recoil term $\boldcalD^2/2m_N$
with $\Delta_i =1$.  Chiral symmetry guarantees $\Delta_i\ge 0$ for all
interactions stemming from the terms shown explicitly in
Eq.~\eqref{QCDL}.\footnote{The choice of heavy baryon fields makes this evident
by removing positive powers of the large nucleon mass from the Lagrangian.}

Using standard identities for connected graphs, a diagram with $L$ loops and
$V_i$ vertices with chiral index $\Delta_i$ contributes to the
amplitude~\eqref{Texp} a term with~\cite{Weinberg:1978kz}\footnote{Note that
$\nu$ can be written in various ways that differ by an additive factor (and by
the overall normalization).  In writing Eq.~\eqref{chiralnu}---as well as
Eq.~\eqref{chiralnupot} below---we chose a form where LO corresponds to
$\nu=0$.}

\begin{equation}
 \nu = 2L + \sum_i V_i \Delta_i \,,\quad \mathcal{N} = f_\pi^{4-3A-E_b} \,,
\label{chiralnu}
\end{equation}

where $E_b$ is the number of external bosons.  The factor $2L$ implies that
ChPT amplitudes are in general perturbative, \ie, the non-analytic functions
$F^{(\nu)}$ in Eq.~\eqref{Texp} can be obtained from a finite number of Feynman
diagrams.  Because of the way NDA was inferred, these loop diagrams are
accompanied by higher-index interactions that provide the necessary
counterterms for RG invariance in the sense of
Eq.~\eqref{TRGtrunc}.  Because of chiral symmetry, $\nu \ge 0$.\footnote{If
interactions in the ``$\cdots$'' of Eq.~\eqref{QCDL} are considered, $\Delta$
and $\nu$ can be negative.  However, these interactions are small due to
strengths that are much smaller than our expansion parameter $Q/\MQCD$. Such
interactions can still be included perturbatively.}
LO ($\OO({\mathcal{N}})$) and NLO (relative $\OO(Q/\MQCD)$) consist of
tree-level ($L=0$) diagrams made out of interactions with chiral index
$\Delta=0$ and, respectively, no or one interaction with $\Delta=1$.  They are
equivalent to ancient current algebra.  Baryons are not only nonrelativistic,
but also approximately static.  Quantum-mechanical corrections ($L\ge 1$) start
at N$^2$LO (relative $\OO(Q^2/\MQCD^2)$).  As $\nu$ increases, progressively
more short-range physics is included, which account for details of hadron
structure.  Many good reviews of ChPT exist, see
for example~\cite{Bernard:1995dp,Bernard:2007zu}.

That is not to say that within certain regions of phase space perturbation
theory does not break down.  The power counting~\eqref{chiralnu} is only meant
as a general rule, which is bound to fail in specific situations.  For example,
within a momentum window of size $\OO(Q^3/\MQCD^2)$ around the Delta
pole---where $E\simeq m_\Delta -m_N$---the one-loop diagrams that make for most
of the Delta width become important and a resummation is necessary at
LO~\cite{Pascalutsa:2002pi,Long:2009wq}.  Similarly, around certain points
below threshold where energies are $\OO(Q^2/\MQCD)$, nucleon recoil needs to be
resummed and elevated to LO \cite{Lv:2016slh}.  The latter resummation is
naturally incorporated by the use of non-heavy baryon (``covariant'')
{fields~\cite{Becher:1999he,Fuchs:2003qc}}, but in the literature it is
often wrongly implied that such a choice is necessary. In general, the choice
of fields is unimportant, but one should always ensure that the power
counting~\eqref{chiralnu} applies to the kinematic region of interest.  Any
resummation needs to be done carefully so as not to break RG invariance.

Nucleon-only $A\ge 2$ processes have $E=\OO(Q^2/m_N)$ and require a
resummation as {well~\cite{Weinberg:1991um}}.  We will return to this in
Sec.~\ref{subsec:chiralamps}, focusing for now on the sum of ``irreducible''
diagrams involving $A\ge 2$ nucleons (and $E_b=0$), which is defined (see
Sec.~\ref{subsec:NuclearEFTS}) as the ``full'' nuclear
potential.\footnote{{For a recent attempt to treat pions dynamically
instead through quantum Monte Carlo methods, see \cite{Madeira:2018ykd}.}}
The analogous currents are briefly discussed in Sec.~\ref{subsec:chiralreact}.

By construction, the potential is free of IR enhancement, and we expect a power
counting similar to ChPT's to apply as long as interactions with $f\ge 4$ also
obey NDA.  A complication is that the full potential {introduced in
Sec. \ref{subsec:NuclearEFTS}} includes disconnected
diagrams.  Each disconnected piece scales as $(4\pi)^n Q^{-4}$, where $n$ is an
integer, coming from the fact that the extra four-dimensional delta function,
which enforces momentum conservation, also eliminates a loop integral. Weinberg
and others~\cite{Weinberg:1991um,Ordonez:1992xp,Weinberg:1992yk,VanKolck:1993ee}
assumed $n=2$ on the basis of Eq.~\eqref{loopintegral}, while
\textcite{Friar:1996zw} took $n=1$, which is consistent with the
nonrelativistic nature of reducible loops as discussed in
Sec.~\ref{subsubsection:conpiless}.  As a consequence, a diagram with
$1\le C\le A-1$ separately connected pieces contributes to the
potential~\eqref{Vexp} with~\cite{Weinberg:1991um,Friar:1996zw}

\begin{spliteq}
 \mu &= n (A-1-C) + 2L + \sum_i V_i \Delta_i \,, \\
 {\tilde{\mathcal{N}}} &= (4\pi)^{(2-n)A}f_\pi^{4-3A} \,.
\label{chiralnupot}
\end{spliteq}

This power counting (with $n=2$) has been used in most studies of
chiral potentials to date.
