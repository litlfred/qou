---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear effective field theory: status and perspectives"
section_id: sec-021-2-nuclear-potential
section_title: "Nuclear potential"
section_number: 2
pages: 42-48
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
doc_brief: "Nuclear effective field theory: status and perspectives — 34 sections: Contents; Two-body scattering amplitude; Power counting"
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.96
---
\label{subsubsec:nukepot}

In Chiral EFT, Fig.~\ref{fig:PionsOut} is undone: pion exchange appears
explicitly in the potential, with the remaining contact interactions accounting
for higher-momentum physics.  In contrast to Pionless EFT, the potential itself
involves (irreducible) loops, where energies are comparable to momenta and
nucleons are approximately static.  The long-range pion-exchange contributions
appear in all partial waves and yield many-body forces consistent with
$2N$ forces and  the hadronic physics described by ChPT.  They are not known to
violate the estimate~\eqref{chiralnupot}.

Pion loops also generate short-range contributions that cannot be separated
from contact interactions in the potential.  The piece of a LEC that removes
the cutoff dependence in irreducible loops, or more generally the piece that
obeys NDA, is sometimes referred to as a {``primordial
counterterm''}~\cite{Long:2011xw,Long:2012ve}.  This is to distinguish it from
another piece that renormalizes the reducible loops of the full amplitude.
This
{additional piece}
may violate NDA and be present at a lower order than the primordial
piece, as discussed in Sec.~\ref{subsec:chiralamps}.
As in Pionless EFT, the potential is \emph{not} cutoff independent.

\paragraph{Leading order}

The full LO potential has maximum $C$ ($C_{\rm max}=A-1$, from $A-2$
disconnected lines): it consists of the sum over pairs of the $2N$ potential at
tree level ($L=0$) constructed entirely from $\Delta=0$ interactions.  The
long-range $2N$ potential consists of static one-pion exchange (OPE) and the
primordial counterterms are the two LECs of the non-derivative chiral-symmetric
contact interactions in Eq.~\eqref{chiLag2bar}:

\begin{multline}
 V^{(0)} = -\frac{4\pi}{m_N\MNN}
 \frac{\vec{\tau}_1\cdot\vec{\tau}_2}{\boldq^2+m_\pi^2}
 \left(S_{12}(\boldq)-\frac{m_\pi^2}{3}\boldsigma_1\cdot\boldsigma_2\right) \\
 + {C_{0\mathrm{s}}P_{\mathrm{s}}  + C_{0\mathrm{t}}P_{\mathrm{t}}} \,,
\label{OPE}
\end{multline}

where the indices 1 and 2 label the two nucleons, $\boldq$ is the transferred
momentum{, and
$S_{12}(\boldq)=(\boldsigma_1\cdot\boldq)(\boldsigma_2\cdot\boldq)
-\boldq^2(\boldsigma_1\cdot\boldsigma_2)/3$ is the tensor operator.}
OPE is static because the transferred energy, related to nucleon recoil, is
small (relative $\OO(Q/\MQCD)$) compared to $\abs{\boldq}$.  The scale
that controls the OPE strength, in a form we can compare with short-range
interactions in Pionless EFT, is given by~\cite{Kaplan:1998tg,Kaplan:1998we}:

\begin{equation}
 \MNN = \frac{16\pi f_\pi^2}{g_A^2 m_N} = \OO(f_\pi) {\,,}
\label{OPEscale}
\end{equation}

{using NDA.}  OPE gives rise in coordinate space to

\textit{i)} a tensor potential that is as singular $\sim1/r^3$ as $r\to0$, and

\textit{ii)} the regular Yukawa potential.

The tensor potential is non-vanishing only for total spin $s=1$ and can mix
waves with $l=j\pm 1$.  It is attractive in some uncoupled waves like $^3P_0$
and $^3D_2$, and in one of the eigenchannels of each coupled wave.  The Yukawa
potential is attractive in isovector (isoscalar) channels for $s=0$ ($s=1$).
The other two terms in Eq.~\eqref{OPE} are contact interactions, which for
large cutoffs contribute only to the $^3S_1$ and $^1S_0$ channels.  A contact
interaction from OPE has been eliminated through the redefinition

\begin{equation}
 C_{0\mathrm{s}} + \frac{4\pi}{m_N\MNN} \to C_{0\mathrm{s}}
 = \OO\left(\frac{4\pi}{m_N \MNN}\right) \,.
\label{C0redef}
\end{equation}

\paragraph{Subleading orders}

The order increases as the chiral index $\Delta$, the number of loops $L$, and
the number of nucleons in connected pieces increase.  In much of the literature
the potential at relative $\OO(Q^{\mu}/\MQCD^{\mu})$ is referred to as
N$^{\mu-1}$LO, but this notation is not flexible enough to accommodate changes
in the power counting described in Set.~\ref{subsec:chiralamps}, which suggest
$n=1$ in Eq.~\eqref{chiralnupot} and also
{departures} from NDA.  For clarity, we
denote the order of contributions using their explicit scaling throughout the
rest of this section.  The structure of the long-range nuclear potential
is shown schematically in Fig.~\ref{fig:chiralpot}.


\begin{figure}[tb]
\begin{center}
\includegraphics[width=\columnwidth]{chiralpot-new}
\end{center}
\caption{Sample of diagrams representing the pion-range components of
 the $AN$ nuclear potential in Chiral EFT, according to
 Eq.~\eqref{chiralnupot} with $n=2$.  The order of the contributions is
 indicated as $\OO(Q^\mu/\Mhi^\mu)$, $\mu\geq0$, where $Q\sim\mpi$ and
 $\Mhi\sim\MQCD$.  Arrows in the $3N$ and $4N$ columns indicate the
 changes for $n=1$.  A solid (double) line stands for a nucleon (nucleon
 excitation), while a dashed line, for a pion. A circle around the central
 solid circle denotes an inverse power of $\Mhi$.
}
\label{fig:chiralpot}
\end{figure}


The first few-body forces arise~\cite{VanKolck:1993ee,vanKolck:1994yi} at
$\OO(Q^n/\MQCD^{n})$ compared to LO, from $\Delta=0$ and $L=0$ with $C=A-2$:

\begin{itemize}

\item
a $3N$ TPE force via an intermediate Delta---the Fujita-Miyazawa
force~\cite{Fujita:1957zz}, shown in Fig.~\ref{fig:chiralpot};

\item
nucleon-only $3N$ and ``double-pair'' forces (for $A\ge 4$) when, in a
time-ordered diagram, a $2N$ interaction occurs while a pion is flying between
two nucleons.

\end{itemize}

Forces of the second type exactly cancel against nucleon recoil in the $2N$ OPE,
once the latter is inserted in the Lippmann-Schwinger
equation~\cite{Weinberg:1991um,Ordonez:1992xp,VanKolck:1993ee,vanKolck:1994yi}.
But recoil is an $\OO(Q/m_N)$ effect compared to LO: the cancellation
implies that $(4\pi)^{2-n}Q^2/\MQCD^2\sim Q/m_N$.  For $n=2$ one obtains $Q/m_N
\sim Q^2/\MQCD^2$ at variance with the NDA that underlies the power counting.
In contrast, if one takes NDA seriously, $m_N=\OO(\MQCD)=\OO(4\pi f_\pi)$, then
$n=1$ and $Q\sim f_{\pi}=\OO(M_{NN})$.  As we discuss in
Sec.~\ref{subsec:chiralamps}, this is consistent with the counting of factors
of $4\pi$ suggested by Pionless EFT.
{
Not all authors count $m_N$, and thus implicitly choose $n$, in the same
way. However, regardless of how $m_N$ is counted, Chiral EFT, just as
Pionless EFT, implements the constraints of Lorentz invariance in a $Q/m_N$
expansion.}

After this cancellation, the $2N$ potential vanishes at relative $\OO(Q/\MQCD)$
if we neglect parity
violation~\cite{Weinberg:1991um,Ordonez:1992xp,VanKolck:1993ee,vanKolck:1994yi}.
For $n=1$, the Fujita-Miyazawa $3N$ force survives at this order.
It is demoted
to relative $\OO(Q^2/\MQCD^2)$ if $n=2$, in which case the full potential
vanishes at $\OO(Q/\MQCD)$.  More generally, the first $aN$ force ($L=0$, all
interactions with $\Delta=0$) is expected to appear at relative
$\OO(Q^{n(a-2)}/\MQCD^{n(a-2)})$.  The relative suppression of few-body forces
\cite{Weinberg:1991um,Ordonez:1992xp,VanKolck:1993ee,vanKolck:1994yi} is in
agreement with the experience drawn from phenomenological potentials containing
explicit pion exchange, for which $3N$ forces are usually found necessary at
the 10\% level---for example, to provide $\sim 1$ MeV to the triton binding
energy $\simeq 8.5~\MeV$.  The explanation for the smallness, but
non-negligibility, of {phenomenological} few-body forces was an early
success of Chiral EFT.

\paragraph{$2N$ potential}

At relative $\OO(Q^2/\MQCD^2)$, corrections to OPE merely shift existing
couplings---for example, $g_A$ in Eq.~\eqref{OPEscale} receives a
contribution proportional to $m_\pi^2$, the so-called Goldberger-Treiman
discrepancy.  The long-range $2N$ potential consists of two-pion exchange (TPE),
the so-called box, crossed-box (shown in Fig.~\ref{fig:chiralpot}), triangle
and football diagrams built out of $\pi N^\dagger N$ and $2\pi N^\dagger N$
interactions with chiral index $\Delta=0$.  For the latter three types, all
combinations of nucleons and Deltas need to be considered in intermediate
states.  For the box diagram with nucleons only, once-iterated OPE needs to be
subtracted.  The primordial counterterms consist of all possible two-derivative
chiral-symmetric contact
interactions~\cite{Ordonez:1992xp,VanKolck:1993ee,Ordonez:1995rz}, such as the
$C_{2\mathrm{s}}$ and $C_{2\mathrm{t}}'$ terms in Eq.~\eqref{chiLag2bar}, and
no-derivative {chiral-symmetry breaking} terms linear in the quark masses,
such as $D_{2\mathrm{s}}$.  The constraints imposed by relativity on these
primordial counterterms have been discussed by \textcite{Girlanda:2010ya}.

At relative $\OO(Q^3/\MQCD^3)$, apart from further contributions to OPE
parameters, the $2N$ potential is made up of TPE with one $\Delta=1$ vertex,
such as the triangle diagram shown in Fig.~\ref{fig:chiralpot}.  For $n=1$,
Galilean corrections ($\propto m_N^{-1}$) should be kept, while for $n=2$ they
contribute only at next order.  There are no new contact interactions at this
order.

The isospin-symmetric $2N$ potential up to $\OO(Q^3/\MQCD^3)$ was derived early
on~{\cite{Ordonez:1992xp,VanKolck:1993ee,Ordonez:1995rz,Kaiser:1997mw,
Kaiser:1998wa}} and rederived many times since.
{\textcite{Epelbaum:1998ka} introduced the unitary transformation
method which allows for the separation of the iterated OPE with
a consistent set of $1/m_N$ corrections.}
{\textcite{Friar:1999sj} discusses the various
forms, including pre-EFT results, and the issues involved
in the separation of iterated OPE. The potential at this order resembles}
phenomenological potentials where pion exchange is supplemented by
a short-range structure.  {The TPE part, which carries information about
the chiral symmetry of QCD, involves LECs that can be determined
from pion-nucleon scattering.  (For recent work, see
\cite{Hoferichter:2015tha,Siemens:2016jwj}.)
It is a chiral analog of the van der Waals potential}
and behaves at short distances as $1/r^5$, $1/r^6$, or $1/r^7$ depending on
order and number of intermediate Deltas, and has the qualitative features of
heavier-meson exchange potentials~\cite{Kaiser:1997mw,Kaiser:1998wa}.  The TPE
from Chiral EFT without explicit Deltas successfully replaces heavier-meson
exchange in  the Nijmegen partial-wave analysis of $2N$
data~\cite{Rentmeester:1999vw,Rentmeester:2003mf};
for a modern version, see \cite{Perez:2013oba,Perez:2014bua}.

The $2N$ potential has now been extended to higher orders.  One- and
two-loop TPE and two-loop three-pion exchange (see Fig.~\ref{fig:chiralpot})
diagrams at $\OO(Q^4/\MQCD^4)$ were calculated by \textcite{Kaiser:1999ff,
Kaiser:1999jg,Kaiser:2001pc,Kaiser:2001at,Kaiser:2015yca}.  More recently the
long-range Deltaless potential has been constructed at
$\OO(Q^5/\MQCD^5)$~\cite{Kaiser:2001dm,Epelbaum:2014sza,Entem:2015xwa}, and even
$\OO(Q^6/\MQCD^6)$~\cite{Entem:2015xwa}.  By parity conservation, primordial
counterterms only appear at even orders.

\paragraph{$3N$ potential}

Beyond the Fujita-Miyazawa term, $3N$ forces have a similar hierarchy.  At
$\OO(Q^{n+1}/\MQCD^{n+1})$, the $3N$ potential contains TPE diagrams where one
interaction has $\Delta=1$ (see Fig.~\ref{fig:chiralpot}).  Again, the form of
TPE is constrained by chiral symmetry, and provides a chiral-corrected
version of the earlier Tucson-Melbourne (TM) potential~\cite{Coon:1978gr},
sometimes called the TM$'$
potential~\cite{Friar:1998zt,Huber:1999bi,Coon:2001pv}, and close in form to
the Brazil potential~\cite{Coelho:1984hk}.  There are no additional
isospin-symmetric contributions from Deltas~\cite{Epelbaum:2007sq}, but there
are mixed one-pion/short-range and purely short-range components originating in
the interactions with LECs $G_A$ and $H_0$, respectively, in
Eq.~\eqref{chiLag2bar}~\cite{vanKolck:1994yi,Epelbaum:2002vt}.  Again, parity
conservation implies primordial counterterms only at every second order.

The primordial counterterms at $\OO(Q^{n+3}/\MQCD^{n+3})$ have been listed
by \textcite{Girlanda:2011fh}.  Relativistic corrections, which appear at this
order for $n=1$, have been calculated by \textcite{Bernard:2011zr}. At
$\OO(Q^{n+2}/\MQCD^{n+2})$ the first loops in the $3N$ force appear as indicated
in Fig.~\ref{fig:chiralpot}, and have been derived without Deltas by
\textcite{Ishikawa:2007zz} {and \textcite{Bernard:2007sp,Bernard:2011zr}.}
The long-range {Deltaless and Deltaful
potentials at one order higher ($\OO(Q^{n+3}/\MQCD^{n+3})$) are found
in~\cite{Krebs:2012yv,Krebs:2013kha,Krebs:2018jkc}.}

One must as well look into higher-order double-pair or other disconnected
diagrams where more than two clusters of nucleons interact at the same time.
\textcite{Epelbaum:2006eu,Epelbaum:2007us} finds that double-pair diagrams with
a recoil correction ($\OO(Q^{2n}/\MQCD^{2n})$), with one insertion of a
$\Delta=2$ interaction ($\OO(Q^{n+2}/\MQCD^{n+2})$), or with $L=1$
($\OO(Q^{n+2}/\MQCD^{n+2})$) all add to nothing without Deltas.

\paragraph{$4N$ potential}

Four-body forces first appear at relative $\OO(Q^{2n}/\MQCD^{2n})$, among them
the one from a
{four-pion} interaction displayed in Fig.~\ref{fig:chiralpot}.  They
are all of long range  and contain no free parameters.  The components without
Deltas can be found in~\cite{Epelbaum:2006eu,Epelbaum:2007us}.  A first
estimate~\cite{Rozpedzik:2006yi} of the effect of {these} components in
$^4$He gives an additional binding of a few hundred keV.  The first contact
$4N$ force is of $\OO(Q^{2(n+1)}/\MQCD^{2(n+1)})$; since it has no derivatives,
the exclusion principle allows only one such interaction, as has been verified
explicitly by \textcite{Girlanda:2011fh}.

\paragraph{Isospin violation}

As discussed in Sec.~\ref{sec:pionless}, Coulomb exchange is
{nonperturbative}
only at small energies; in the region Chiral EFT power counting is designed for,
the Coulomb potential can be treated in perturbation theory.  The way
$e_{\text{red}}$ is counted above ensures that the Coulomb potential  appears
at $\OO(\Mlo/\MQCD)$, not LO.  Other purely electromagnetic components are even
smaller and can be incorporated as in ChPT.  More interesting is the isospin
breaking coming from interactions in Eq.~\eqref{chiLag} where hard photons have
been integrated out and/or the quark mass difference $\bar{m}\varepsilon$ (see
Eq.~\eqref{QCDL}) appears.  These interactions lead to the charge-neutral pion
mass splitting $\delta m_\pi^2=\OO(\Mlo^3/\MQCD)>0$ and the neutron-proton mass
difference $\delta m_N=\OO(\Mlo^2/\MQCD)>0$.  Other isospin-violating effects
are, likewise, suppressed by at least one power of
$\MQCD^{-1}$~\cite{VanKolck:1993ee,vanKolck:1995cb}, which means isospin is an
accidental symmetry: although broken in QCD, it is a symmetry of the LO EFT.

In contrast to many models, Chiral EFT produces relatively simple
isospin-violating forces that are invariant under both gauge
{transformations and pion-field redefinitions.}  The isospin-violating $2N$
potential has been calculated up to relative $\OO(Q^3/\MQCD^3)$ by
\textcite{VanKolck:1993ee,vanKolck:1995cb,vanKolck:1996rm,vanKolck:1997fu,
Friar:1999zr,Niskanen:2001aj,Friar:2003yv,Friar:2004ca,Epelbaum:2005fd,
Epelbaum:2007sq,Epelbaum:2008td}, including the pion mass splitting in OPE and
TPE, the most important isospin-breaking pion-nucleon coupling in OPE,
simultaneous photon-pion exchange, the nucleon mass difference in TPE, and
primordial counterterms. In standard terminology~\cite{Miller:1990iz}, ``class
I'' forces refer to isospin symmetry, ``class II'' to forces that break charge
independence but not charge symmetry---defined as a rotation of $\pi$ around
the 2-axis in isospin space---, ``class III'' to forces that break charge
symmetry but vanish in the $np$ system, and ``class IV'' to those that break
charge symmetry but cause isospin mixing in the $np$ system.  Class M forces
are first found at $\OO(Q^{{\rm M}-1}/\MQCD^{{\rm M}-1})$, which provides a
justification for the pre-EFT phenomenology, where this hierarchy was
observed~\cite{Miller:1990iz}.

Isospin violation first appears in the $3N$ potential at relative
$\OO(Q^{n+1}/\MQCD^{n+1})$ where it breaks charge symmetry through the nucleon
mass difference in TPE~\cite{Friar:2004ca,Epelbaum:2004xf,Friar:2004rg}.
However, since $\delta\MN$ is the result of a partial cancellation between
quark-mass and electromagnetic effects, isospin breaking in the $3N$ potential
is relatively small.

\paragraph{Summary}

The nuclear potential---its long-range form and its primordial
counterterms---has been derived in Chiral EFT to a considerably high order.
Although some of its elements had been anticipated using phenomenological
methods, new forces have also been found, particularly those carrying the
hallmark of QCD via chiral symmetry.  Small differences of implementation
remain regarding the related
assignments of order to few-body forces and to the inverse nucleon mass.
A more detailed exposition of the chiral potential can be found in
{\cite{Epelbaum:2005pn,Machleidt:2011zz}}.
We turn now to some of the important issues that
arise in connecting these forces to data.



\subsection{Nuclear amplitudes and observables}
\label{subsec:chiralamps}

Observables are determined by the $T$ matrix, which in turn is obtained by
using the potential with the appropriate dynamical framework---the
Lippmann-Schwinger or Schr\"odinger equation, or one of its many-body variants.
This process involves reducible diagrams for which the power counting of the
previous section does not apply.  Weinberg's original
prescription~\cite{Weinberg:1990rz,Weinberg:1991um} was to truncate the
potential and solve the corresponding equation exactly.  The hope,
based on experience with regular potentials, was that, if corrections are small
in the potential, they would only generate small corrections at the amplitude
level even if treated {nonperturbatively}.  However, chiral potentials are
only
regular due to the regularization procedure, which means that reducible
diagrams generate further regulator dependence.  As in Pionless EFT
(Sec.~\ref{sec:pionless}),
{non-negative} powers of $\Lambda$ are generated this way
which, if not compensated by the LECs, lead not only to potentially large
corrections from subleading orders, but also to model dependence through the
regulator choice.  The relevant question is to which extent
Eq.~\eqref{TRGtrunc} affects the ordering of the short-range interactions in
the potential.



\subsubsection{Weinberg's prescription}
\label{sebsubsec:weinbergprescription}

The first numerical study of chiral potentials with Weinberg's
prescription by \textcite{Ordonez:1993tn,Ordonez:1995rz} yielded a reasonable
description of $2N$ data at $\OO(Q^3/\MQCD^3)$ with explicit Deltas for a
Gaussian regulator on the transferred momentum with cutoff values $\Lambda=500,
800, 1000~\MeV$, {but used an over-complete set of interactions}.
A drawback of such a local (but non-separable) regulator is
that it allows a contact interaction to contribute to all partial waves
consistent with the exclusion principle.  In the large-$\Lambda$ limit the
contribution of a contact interaction to all but one wave disappears, but at
any finite cutoff data fitting is highly coupled and complicated.
{\textcite{Epelbaum:1999dj} carried out the first fit with
the minimum number of} {seven LECs} {at $\OO(Q^2/\MQCD^2)$.}
{That work as well as subsequent} fits
have employed different regulators
for the potential and for the dynamical equation, with a separable, non-local
regulator for the latter.  Fits of higher quality were achieved, and it
eventually emerged that they do depend on the choice of regulator; only for a
limited range of cutoff values $\Lambda\simle \MQCD$ have good fits been
obtained~\cite{Epelbaum:2006pt,Marji:2013uia}.  A milestone was a fit
\cite{Entem:2003ft} to $2N$ data at $\OO(Q^4/\MQCD^4)$ without explicit
Deltas for a non-local, super-Gaussian exponential regulator with
$\Lambda=500~\MeV$.  This achieved accuracy comparable to that of
phenomenological potentials ({for the $^3S_1$ phase shifts,}
see curve labeled ``EM500'' in
Fig.~\ref{fig:ThreeSOnePhase}).  Since then other high-quality fits have been
achieved at this or even lower and/or incomplete
orders~\cite{Epelbaum:2003xx,Epelbaum:2004fk,Ekstrom:2013kea,Ekstrom:2014iya,
Epelbaum:2014efa,Piarulli:2014bda}.  The state-of-the-art
{are the $\OO(Q^5/\MQCD^5)$}
{fits of \textcite{Entem:2017gor} and \textcite{Reinert:2017usi}}.\footnote{
{The relatively large size of TPE for
the cutoff values employed by \textcite{Reinert:2017usi}
might call into question
the expansion of the potential shown in Fig. \ref{fig:chiralpot}.
However, the potential is not directly observable and its expansion
must be judged according to its effects on renormalized amplitudes.}}
We might expect increasingly accurate results as newly developed
fitting-optimization procedures are applied to higher-order potentials.


To the orders where good fits to $2N$ data have been achieved, the chiral
potential is expected, as discussed in the previous section, to include $3N$
forces whichever value one takes for $n$.  In most calculations, where $n=2$ is
assumed and the Delta is integrated out, the leading $3N$ forces appear at
$\OO(Q^3/\MQCD^3)$ and its two parameters $G_A$ and $H_0$
(Eq.~\eqref{chiLag2bar}) are fitted to few-nucleon data.  An obvious observable
to fit with $H_0$ is the triton binding energy, as frequently done in Pionless
EFT.  Possible ways to determine $G_A$ include a $2N$ process such as $N\! N\to
N\! N\pi$~\cite{Hanhart:2000gp,Baru:2009fm}, another $3N$ quantity, such as the
doublet neutron-deuteron ($nd$) scattering length~\cite{Epelbaum:2002vt} or the
triton{
half-life~\cite{Gardestig:2006hj,Nakamura:2007vi,Gazit:2008ma,Ekstrom:2014iya,
Baroni:2016xll}}, and a $4N$ quantity, such as the \FourHe binding
energy~\cite{Nogga:2005hp,Ekstrom:2013kea}.
{\textcite{KalantarNayestanaki:2011wz} review chiral $3N$ forces
in light nuclei.}  Recently a simultaneous
fit to $A\le 4$ properties~\cite{Carlsson:2015vda} has been performed up to
$\OO(Q^3/\MQCD^3)$ without explicit Deltas.  Overall, a good description of
$A\le 4$ systems, including scattering, can be achieved at this order and
higher, as long as a ``good'' regulator with a cutoff parameter $\Lambda \simle
\MQCD$ is employed.

Owing to their symmetry connection with QCD, chiral potentials have become
increasingly popular within the nuclear structure/reaction community,
particularly after the milestone fit of \textcite{Entem:2003ft}.  Remarkable
progress has been achieved in the development of ``\abinitio'' many-body
methods for the solution of the Schr\"odinger equation starting from a given
potential.
{Typically additional UV and IR regulators (see Sec.~\ref{infrareg}) are
introduced, and EFT suggests extrapolations to mitigate their effects
\cite{Coon:2012ab,Furnstahl:2012qg,Tolle:2012cx,Kruse:2013qaj,More:2013rma,
Furnstahl:2013vda,Furnstahl:2014hca,Coon:2014nja,Konig:2014hma,Wendt:2015nba}.}
Extensive benchmarking---for {examples}, see
\cite{Kamada:2001tv,Hagen:2007hi,Abe:2012wp}---has ensured that, while not
entirely controlled, results are found in very satisfactory agreement with each
other.  \Abinitio methods are now at a stage where they can contribute
substantially to the understanding of the input interactions, by relating
parameters of these interactions to $A>4$ data.  The majority of today's
\abinitio calculations uses chiral potentials as input, for many of the new
methods are flexible enough to accommodate the non-localities of both the
interactions themselves and the chosen regulators.

Weinberg's prescription
is simple to implement because it is the same as that used for a
phenomenological potential: the various components are treated equally
in the solution of the Schr\"odinger equation.  The availability of many-body
calculations has led to an increased use of $A>4$ data to constrain the
potential parameters---particularly those of the $3N$ force, which proves
important in describing some nuclear quantities such as the ground-state spin of
$^{10}$Be~\cite{Navratil:2007we}, the dripline in oxygen
isotopes~\cite{Otsuka:2009cs,Hagen:2012sh}, and the evolution of shell structure
in calcium isopes~\cite{Holt:2010yb,Hagen:2012fb}.  These achievements have been
reviewed by \textcite{Hammer:2012id}{, and more recently in a compilation
of articles~\cite{Dudek:2016phscr} celebrating the 40-year anniversary of the
1975 Nobel Prize.}
While a large number of nuclear data have been well
{described---for example an excellent reproduction of
$A\le 12$ spectra \cite{Piarulli:2017dwd}---there}
are also challenges in reproducing bulk properties
of both {nuclei~\cite{Soma:2013xha,Binder:2018pgl} and
nuclear matter~\cite{Hagen:2013yba,Drischler:2017wtt},
as well as some $A=3$ scattering observables, including
the recalcitrant $A_y$ puzzle \cite{Piarulli:2017dwd,Binder:2018pgl}.}

The issue of the optimal set of data to fit has come to the fore.  In a
controlled EFT, a change in input data at a given order is not, ordinarily, a
systematic improvement because it represents a change that can be compensated by
higher orders.  However this is not necessarily true when correlated data
are employed~\cite{Lupu:2015pba}.  If only data at $Q\sim \Mlo$ are used as
input, we expect no particular correlations.  Guaranteeing that this is
the case is made difficult by the relative closeness between $\Mlo$ and $\Mhi$
in Chiral EFT, aggravated by the use of cutoff parameters $\Lambda \simle \Mhi$.
If one employs data characterized by $Q< \Mlo$, which are better described by a
lower-energy EFT, correlations might appear.  Examples of correlations among
few-nucleon observables were
given in Secs.~\ref{sec:pionless}
and~\ref{sec:halo}.  If one attempts to use, say, the triton binding energy
and the doublet $nd$ scattering length to fix two parameters of the $3N$ force,
one might expect one parameter combination to be relatively poorly determined.
These are low-energy data within the realm of Pionless EFT, which reorganizes
interactions into the appropriate
low-energy combinations.  Since one expects
larger systems to be increasingly within the regime of Chiral EFT, it is
possible that using properties of heavier nuclei provides real improvement.
A concrete example is the so-called NNLO$_{\text{sat}}$
potential~\cite{Ekstrom:2015rta}, a Deltaless chiral potential at
$\OO(Q^3/\MQCD^3)$ where the LECs are simultaneously adjusted not only for
$A\le 4$, but also to binding energies and radii of carbon and oxygen isotopes.
Examples of the corresponding predictions for other nuclei are shown in
Fig.~\ref{fig:1502_04682v2_fig1}.  In a similar spirit,
\textcite{Elhatisari:2015iga,Elhatisari:2016owd}, implementing Chiral EFT in a
lattice framework, have shown that the alpha-alpha interaction can be used as a
sensitive handle to determine
{internucleon interactions}.


\begin{figure}[tbp]
\centering
\includegraphics[width=0.9\columnwidth]{1502_04682v2_fig1}
\caption{Ground-state energy (negative of binding energy) per nucleon (top),
 and residuals (differences between computed and experimental values) of charge
 radii (bottom) for selected nuclei computed with
 a variety of chiral potentials (labeled a---i and
 $\text{NNLO}_{\text{sat}}$).
 Figure and description taken from \cite{Ekstrom:2015rta}.
 Courtesy of A.~Ekstr\"om.
}
\label{fig:1502_04682v2_fig1}
\end{figure}


The role of the regulator has also been under increasing scrutiny in \abinitio
calculations.  A powerful tool for many-body calculations is quantum Monte Carlo
(QMC), which pioneered the modern solution of many-nucleon systems but is
best suited for local potentials.  In Chiral EFT, it favors local interactions
and regulators.  Antisymmetrization among nucleons can be used to eliminate
some non-local contact
interactions~\cite{Gezerlis:2013ipa,Gezerlis:2014zia,Lynn:2014zia,
Piarulli:2016vel,Logoteta:2016nzc}, enabling various new calculations.  For
example, the effects of the  $\OO(Q^2/\MQCD^2)$ potential in neutron matter
have been
studied~\cite{Gezerlis:2013ipa,Gezerlis:2014zia,Tews:2015ufa,Lynn:2015jua}.
Because of antisymmetrization, different spin-isospin forms of the $3N$ contact
interaction can be written, which are all equivalent and consistent with zero
within the EFT truncation error for $\Lambda\simge \MQCD$.  In contrast, the
limitation to $\Lambda\simle \MQCD$ leads to relatively large regulator
artifacts above saturation density~\cite{Lynn:2015jua}.  This indicated that a
lack of RG invariance, besides destroying model-independence, also has
undesirable phenomenological consequences.
