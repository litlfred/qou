---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear eﬀective ﬁeld theory: status and perspectives"
section_id: sec-051-2-chiral-lagrangian
section_title: "Chiral Lagrangian"
section_number: 2
pages: 40-41
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.987
doc_brief: "Nuclear eﬀective ﬁeld theory: status and perspectives — 82 sections: Nuclear effective field theory: st; Contents; I Introduction"
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
