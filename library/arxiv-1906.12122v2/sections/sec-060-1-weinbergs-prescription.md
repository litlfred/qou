---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear eﬀective ﬁeld theory: status and perspectives"
section_id: sec-060-1-weinbergs-prescription
section_title: "Weinberg's prescription"
section_number: 1
pages: 46-48
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.986
doc_brief: "Nuclear eﬀective ﬁeld theory: status and perspectives — 82 sections: Nuclear effective field theory: st; Contents; I Introduction"
---
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
