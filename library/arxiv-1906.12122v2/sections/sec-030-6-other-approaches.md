---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear eﬀective ﬁeld theory: status and perspectives"
section_id: sec-030-6-other-approaches
section_title: "Other approaches"
section_number: 6
pages: 52-56
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.989
---
\label{subsubsection:other}

{
The renormalization of Chiral EFT described in the previous section was
criticized by~\textcite{Epelbaum:2018zli}, who provided examples where the
nonperturbatively renormalized amplitude exhibits positive powers of the cutoff
$\Lambda$ when expanded in Planck's constant $\hbar$.
{Since no observable {considered} in that work is affected, however,
the significance of this claim for an EFT is unclear.}
Moreover, \textcite{Valderrama:2019yiv} argued that these powers of $\Lambda$
can be eliminated by changing the $\Lambda^{-1}$ running of the
LECs~\cite{Valderrama:2016koj}.  (See also the response
by~\textcite{Epelbaum:2019msl}.)
}

{
An alternative approach to the renormalization woes of Weinberg's
prescription was articulated by~\textcite{Epelbaum:2018zli}, building
on earlier work~{\cite{Gegelia:1998gn,Gegelia:1998iu,Gegelia:1998ee,
Gegelia:1999ja,Gegelia:2001ev,Gegelia:2004pz,Epelbaum:2009sd}}.
{It consists of renormalizing the perturbative series and subsequently
resumming the renormalized contributions, that is,
it includes} at each order the infinite number of LECs needed to
eliminate the cutoff dependence of all diagrams to be resummed.  These LECs
exist because an EFT contains all interactions allowed by symmetry, but even
without pions they are difficult or impossible to write down explicitly.
In a stark departure from naturalness, only the LECs prescribed by NDA are
assumed to contribute finite parameters, which amounts to an infinite number of
fine tunings.  The resummation of an infinite number of derivative interactions
introduces an intrinsic nonlocality in all channels at every order---not only
LO in, say, the $N\!N$ $^1S_0$~\cite{Beane:2000fi,SanchezSanchez:2017tws} or
the $N\alpha$ $^{2}P_{3/2}$~\cite{Bertulani:2002sz} channels, where there are
shallow poles.
}

{
In this approach, there are no constraints on the EFT from renormalization,
for example no Wigner bound on the effective range
(\textcite{Wigner:1955zz}; see
Sec.~\ref{subsubsec:regren}) when $C_2$ or higher-order interactions are
resummed~\cite{Gegelia:1998gn}} and no
explanation~\cite{Epelbaum:2016ffd,Epelbaum:2019msl} for the emergence of a
single, independent three-body scale in the three-body system at LO, which
determines the position of the Efimov tower of states
{(\textcite{Efimov:1970ab}; see Sec.~\ref{sec:Triton})}.  Thus, the
justification for power counting from the combination of renormalization and
naturalness, which in the perturbative context gives
NDA~\cite{Manohar:1983md,Georgi:1986kr}, is absent.  NDA becomes an \textit{ad
hoc} rule{. It does not, \eg, reproduce the established scaling of range
corrections in amplitudes resulting from short-range potentials, which is
represented in Pionless EFT through Eq.~\eqref{eq:scaling-re}.}


{
So far this approach has been implemented only in the $^1S_0$ channel, where
significant dependence on the choice of (low-energy) subtraction points
is seen~\cite{Gegelia:1998iu,Gegelia:1998ee,Gegelia:1999ja,Gegelia:2001ev}.
On the basis of a toy model, \textcite{Epelbaum:2017byx} conclude that
Weinberg's prescription is satisfactory as long as the renormalization scale
$\mu=\OO(\Mhi)$.  Chiral EFT's overlapping integrals in other channels
prevent the explicit resummation of ``renormalized diagrams'' and it is not
known whether this procedure, if it can be carried out at all, {reproduces
the nonperturbative} solution of the Lippmann-Schwinger equation.
Further discussion of renormalization from the perspective of subtraction
schemes can be found in~\cite{Timoteo:2010mm,Szpigel:2011bc,Batista:2017vao}.
}

{
\textcite{Gegelia:2001ev} offer the solution that the cutoff should not be
varied significantly around the breakdown scale in Chiral EFT.  In the absence
of renormalization, non-negative powers of the cutoff should appear in the
truncated amplitude {given by Eq.}~\eqref{Ttrunc} as corrections of
$\OO(Q^{\mathcal{V}+1-i} \Lambda^i/(\Mhi^{\mathcal{V}+1-j} \Mlo^{j}))$
{with nonnegative integers $i,j$.}  If $j=0$ the corrections should be small
for $\Lambda\ll \Mhi$~\cite{Gegelia:2004pz}, but $j> 0$ arises when the LO
potential, which does not involve $\Mhi$, is singular.
}

{
An attempt to mitigate cutoff artifacts was made
by~\textcite{Djukanovic:2007zz}, \textcite{Epelbaum:2012ua},
and \textcite{Epelbaum:2013naa,Epelbaum:2015sha}} with the most recent
formulations developed
{by~\textcite{Behrendt:2016nql} and \textcite{Baru:2019ndr}}.
A nucleon propagator with faster large-momentum
fall-off is constructed by demanding that states satisfy a relativistic
(Lorentz-invariant) normalization condition, while overall the treatment is
still nonrelativistic.  This softer UV behavior helps to obtain LO amplitudes
with well-defined {large-cutoff} limits.  While \textcite{Behrendt:2016nql}
state
that higher orders should be treated in perturbation theory if this feature is
to be maintained beyond LO, from a practical point of view they still advocate a
nonperturbative treatment (where the cutoff is then limited again to a finite
range, argued to be larger than what is typically used with standard Weinberg
counting). Moreover, \textcite{Behrendt:2016nql} find that with their
approach a $^3P_0$ LEC has to be promoted compared to NDA, {as in the purely
nonrelativistic context~\cite{Nogga:2005hy}.}
{There is, nevertheless, growing interest in the development of
a covariant version of Chiral EFT, which could perhaps be used as input
to relativistic formulations of nuclear physics
\cite{Petschauer:2013uua,Ren:2016jna,Ren:2017yvw}.}



\subsection{{Pion and electroweak reactions}}
\label{subsec:chiralreact}

One of the great advantages of a quantum-field-theoretical foundation of
nuclear physics is that not only many-body forces can be constructed
consistently with two-body forces, but also many-body currents can be derived
consistently with inter-nucleon interactions.  This virtue was realized early
on~\cite{Rho:1990cf,Weinberg:1991um}, and some of the pioneering papers on
reactions have been dedicated to electroweak
currents~\cite{Park:1993jf,Park:1995pn,Phillips:1999am}, neutron radiative
capture on the proton~\cite{Park:1994sr,Park:1997kp}, proton-proton
fusion~\cite{Park:1998wq}, Compton scattering on the
deuteron~\cite{Beane:1999uq}, pion photo-~\cite{Beane:1995cb,Beane:1997iv} and
electro-~\cite{Bernard:1999ff} production off the deuteron,
pion photoproduction off the
trinucleon~\cite{Lenkewitz:2011jd,Lenkewitz:2013hka},
pion scattering on the deuteron~\cite{Beane:1997yg}
and
{helion}~\cite{Liebig:2010ki}, as well as pion production in
$2N$ collisions~\cite{Park:1995ku,Cohen:1995cc,vanKolck:1996dp,Sato:1997ps}.
The goal is not only to supply information to other areas of physics where
these reactions play a role, but also to extract nucleon properties (in
particular for the neutron, for which good targets do not exist) to infer
properties of the QCD dynamics.

The early work, {reviewed by \textcite{vanKolck:1999mw} and
\textcite{Bedaque:2002mn},} was based on
Weinberg's prescription, where, in addition to the potential, also the kernel
of the reaction process is expanded according to NDA.  For probes with energies
$E\sim Q \sim m_\pi$, the kernel is defined as the subdiagrams to which the
external probes are attached, energies are comparable to momenta, and nucleons
are approximately static.  Like the potential, kernels can be multiply
connected, and power counting is similar to Eqs.~\eqref{chiralnu}
and~\eqref{chiralnupot}.  For any kernel, a figure like
Fig.~\ref{fig:chiralpot} can be drawn.  However, some subtleties need to
be taken into account when probes have other typical {energy or momentum}:

\begin{itemize}

\item
$E\sim \MNN^2/\MQCD$ (\eg~Compton scattering): a resummation is needed
between kernels because infrared enhancements appear in intermediate states,
where nucleons are not static~\cite{Beane:1999uq}.

\item
$Q\sim \sqrt{m_\pi m_N}$ (\eg~pion production):\footnote{{Although
parametrically $\sqrt{m_\pi m_N}= {\mathcal O}(\sqrt{m_\pi \MQCD})<\MQCD$,
one should keep in mind that the breakdown scale $\MQCD$ of Chiral EFT is
not known precisely.}} intermediate states containing
only nucleons can be part of the kernel, but these nucleons are not
static~\cite{Cohen:1995cc}.

\end{itemize}

The full amplitude is given by the matrix element of the kernel with
wavefunctions obtained from the potential.  In Weinberg's prescription, these
wavefunctions are exact solutions of a truncated potential.  Much of the work
predating phenomenologically successful chiral potentials employed a ``hybrid''
approach where the kernel was calculated in Chiral EFT but wavefunctions from
``realistic'' phenomenological potentials were used.  Emphasis has since been
shifting towards increased consistency between wavefunctions and kernels.
Reactions are an area of renewed interest in Chiral EFT, in consonance with the
revival of development in the broader area of nuclear reactions, including
\abinitio approaches.  Of particular recent interest have been electroweak
currents, where earlier work was revisited and significantly improved
upon---see the excellent reviews by
{\textcite{Phillips:2016NN} and \textcite{Riska:2016cud}}.  There has
also been substantial work on reactions involving pions, particularly pion
production in two-nucleon collisions, which has now been calculated up to three
orders in the chiral expansion~\cite{Baru:2013zpa}.

The process that has been most thoroughly examined in Chiral EFT is Compton
scattering (CS).  It gives access to nucleon polarizabilities---response
functions that carry much information about hadron dynamics.  While proton
polarizabilities can be extracted directly, neutron polarizabilities can only
be probed in nuclear CS.  Chiral EFT allows for a consistent treatment of both
these cases, and at the same time enables a connection with lattice QCD through
variation in the pion mass.  Recent work has capitalized on all advances
in EFT and provides an analysis of CS that is a model for future work on
nuclear reactions.  At the one-nucleon level, CS was calculated in ChPT with
an explicit Delta isobar~\cite{McGovern:2012ew}, including the
resummation~\cite{Pascalutsa:2002pi} needed to go through the Delta peak.  At
the nuclear level, the kernel was calculated consistent with Weinberg's
prescription~\cite{Griesshammer:2012we}.  Proton~\cite{McGovern:2012ew} and
deuteron~\cite{Myers:2014ace,Myers:2015aba} data were fitted and
polarizabilities were extracted, see Fig.~\ref{fig:compton}.  The average quark
mass was then varied to produce predictions{, with uncertainties determined
\via Bayesian
techniques~\cite{Furnstahl:2014xsa,Furnstahl:2015rha,Wesolowski:2015fqa},} for
the polarizabilities at unphysical pion masses~\cite{Griesshammer:2015ahu}, to
which lattice QCD results can be compared.  Analyses of this type for other
processes should increasingly become standard in this field, allowing to bridge
from QCD to nuclear reactions just as to nuclear structure.


\begin{figure}[tb]
\begin{center}
\includegraphics[width=\columnwidth]{HgrieCompton}
\end{center}
\caption{
Nucleon electric ($\alpha_{{\rm E}1}$) and magnetic ($\beta_{{\rm M}1}$)
polarizabilities extracted with Chiral EFT.
Ellipses show the 1$\sigma$-error fits of \textcite{McGovern:2012ew}
for proton (blue, on lower band) and neutron (red, on upper band),
where statistic, systematic, and theory errors were added in quadrature.
For comparison, Particle Data Group averages
before (large, green ellipses) and after (small, black ellipses)
these fits are also given.
The bands are the constraints from the Baldin sum rule.
Reprinted from \cite{Griesshammer:2015wha}, with the permission of AIP
Publishing.
}
\label{fig:compton}
\end{figure}



The renormalization problems of Weinberg's prescription demand scrutiny in the
treatment of reactions as well.  The emergence of a perturbative-pion
formulation of Chiral EFT has led to a re-examination of many of the
reactions that had been studied earlier with Weinberg's prescription.
With perturbative pions, not only the kernel but also the wavefunction is
expanded in perturbation theory.  For the deuteron---target of most, if not
all, perturbative-pion studies---the {analytical} nature of the
calculations makes it easier to establish proper renormalization.
In most cases, the LO calculation is the same as in
Pionless EFT (Secs.~\ref{sec:Currents-TwoBody}
and~\ref{sec:Currents-ThreeBody}), and pion effects enter explicitly at
subleading orders.  For example, the charge, magnetic dipole and electric
quadrupole form factors of the deuteron have been calculated to NLO by
\textcite{Kaplan:1998sz}.  Other reactions include neutron radiative capture on
the proton~\cite{Savage:1998ae}, deuteron Compton scattering and
polarizability~\cite{Chen:1998vi,Chen:1998ie,Chen:1998rz}, and
neutrino-deuteron scattering~\cite{Butler:1999sv}.  Generally, this approach
has been successful for the low-energy properties of the deuteron, both in
comparison with data and with
{nonperturbative-pion} calculations.



\subsection{Outstanding issues and current trends}
\label{subsec:Outissues}

Within Weinberg's prescription, work continues in pushing potential and kernels
to higher orders, as well as developing {better} fitting strategies.
Meanwhile, an
RG-invariant formulation of Chiral EFT has not yet achieved the level of
phenomenological impact of Weinberg's prescription.  Some of the outstanding
questions are:

\begin{itemize}

\item
What is the role of fine-tuning in Chiral EFT?  The scattering length is
particularly large in the $^1S_0$ two-nucleon channel, where short-range
interactions show strong energy dependence~\cite{Birse:2010jr}.  In particular,
short-range contributions to the effective range are anomalously large, which
has led to the suggestion that the two-derivative contact interaction
($C_{2\mathrm{s}}$ in Eq.~\eqref{chiLag2bar}) should be treated as
LO~{\cite{Beane:2001bc,Long:2013cya}}, following a similar proposal in
Pionless EFT~\cite{Beane:2000fi} (Sec.~\ref{sec:Dibaryons}) and Chiral EFT with
perturbative pions~\cite{Ando:2011aa} (Sec.~\ref{subsubsection:pertpions}).
Although an improved description is achieved, convergence deteriorates quickly
with momentum, at least in a calculation without Deltas~\cite{Long:2013cya}.
The role of the relatively low-energy zero of the amplitude remains to be fully
investigated~\cite{Lutz:1999yr,SanchezSanchez:2017tws}.

\item
What is the pion mass variation of nuclear amplitudes?  To determine this
variation, we need lattice data within the region of validity of Chiral EFT.
While lattice QCD data exist at relatively large $m_\pi$, not all competing
collaborations are in agreement.  Moreover, differences exist within Chiral EFT
depending on the approach used.  Among the issues for extrapolations is the
role of ``radiation'' pions, which are present only at relatively high order.
Real pions can be produced in $2N$ collisions for momenta
$Q\simge \sqrt{m_\pi m_N}$;
at lower $Q$ the effects of the corresponding virtual pions are
indistinguishable from the LECs \cite{Ordonez:1995rz,Epelbaum:1998ka}.
These contributions have been investigated in the
perturbative-pion context~\cite{Mehen:1999hz,Mondejar:2006yu,Soto:2011tb}
where they give rise to powers of $m_\pi^{1/2}$.

\item
The NDA-based organization of pion-exchange contributions to the potential is
not affected by the renormalization issues that plague Weinberg's prescription,
except for the possible enhancement factors of $4\pi$ in few-nucleon forces
(Sec.~\ref{subsubsec:nukepot}).  Once the $2N$ system has been properly
renormalized, one must ask whether short-range many-body forces are immune to
the enhancements seen in Pionless EFT (Sec.~\ref{sec:Triton}).
Most work on many-body forces in Chiral EFT takes Weinberg's power counting for
granted.  \textcite{Nogga:2005hy} and \textcite{Song:2016ale} have found no
renormalization evidence for a $3N$ force in LO or $\OO(Q/\MQCD)$, but they
obtain a triton binding energy which is only about half of the experimental
value, perhaps because this is a very-low energy observables in the sense of
being within the regime of Pionless EFT.  \textcite{Kievsky:2016kzb} argue from
continuity with Pionless EFT that the $H_0$ three-body force in
Eq.~\eqref{chiLag2bar} should be included at LO.

\item
The most important problem facing reaction theory in Chiral EFT echoes the
renormalization woes of Weinberg's prescription for nuclear structure.
In order to maintain model independence, one must ensure that the average of
the reaction kernel has a well-defined limit as the cutoff is increased.  Only
for electroweak reactions on the deuteron has this been
investigated~\cite{Valderrama:2014vra,Phillips:2016NN}, with the conclusion
that enhancements over NDA appear there as well.  The impact of this
observation on previously studied reactions and future reaction theory remains
to be investigated.

\item
To which extent can an RG-invariant formulation of Chiral EFT be incorporated
in calculations of larger nuclei?  Distorted-wave perturbation theory usually
becomes very demanding in second order where the fully off-shell $A$-body
propagation is needed in intermediate states.  In Pionless EFT, this problem
has been side-stepped by a reformulation in terms of the solution of further
integral equations~\cite{Vanasse:2013sda,Vanasse:2015fph}.  It is an open issue
whether this or another method can be  applied to the $A$-nucleon problem
{in Chiral EFT}.

\item
Although not RG invariant, Weinberg's prescription has several practical
advantages because it is most closely related to previous phenomenological
approaches. For example, it provides fits to data of comparable quality to
``realistic'' phenomenological potentials
(Sec.~\ref{sebsubsec:weinbergprescription}){,} it explains some of the
qualitative features of these potentials (Sec.~\ref{subsubsec:nukepot}), and it
can be employed in already existing \abinitio codes.
Its successes beg the question, is it possible that a
{particular choice of regulator allows for a small-cutoff
formulation of Chiral EFT that is equivalent to its RG-invariant form?}
It is conceivable that one can iterate subleading
terms of the latter, as it is done in the former, within a limited range of
cutoffs, just as iterating momentum-dependent contact interactions in Pionless
EFT requires cutoff values $\Lambda \simle 1/r_0$ (Wigner bound,
Sec.~\ref{subsubsec:regren}).  If achieved, such an understanding of Weinberg's
prescription might justify current uses of Chiral EFT without requiring further
development of \abinitio methods.  {Furthermore, it will likely make it
desirable to choose a regulator which optimizes convergence for the problem at
hand,} {for example neutron matter \cite{Lynn:2015jua}.
First steps in this direction were just made by
\textcite{Tews:2018sbi} and \textcite{Valderrama:2019lhj}.
}

\item
Irrespective of other issues discussed above and throughout this section, it is
a highly nontrivial task to determine the LECs of Chiral EFT---quite
substantial in number at higher orders---from fitting calculated observables to
data. {One wants to do this in such a way that the EFT can fulfill its
promises of providing systematic model independence and fully quantified
uncertainties.  For that, one should account for the truncation error of the
EFT expansion directly as part of the fitting procedure, and propagate
forward all this information to the final result of a calculation.}  Following
the initial suggestion of \textcite{Schindler:2008fh}, Bayesian methods have
emerged in recent
{years~\cite{Furnstahl:2014xsa,Furnstahl:2015rha,Wesolowski:2015fqa,
Melendez:2017phj,Wesolowski:2018lzj}}
as an important tool to address the issue in a robust and comprehensive way.

\end{itemize}




\section{Broader applications} \label{sec:other}
Many of the ideas originating in nuclear EFTs have found applications to other
systems.  Pionless EFT, while being clearly connected to QCD as a low-energy
limit, is driven largely by the universal features that arise from the large
$N\!N$ scattering lengths and the associated large sizes of light nuclei.
As a consequence, the EFT for nuclear halo states discussed in
Sec.~\ref{sec:halo} can be constructed as a generalization of Pionless EFT.
But universality goes beyond nuclear physics: it is relevant to any system
dominated by short-range interactions, when one is interested in distance scales
much larger than the range of the interactions.

As one probes distances comparable to the interaction range, issues similar to
the ones discussed in Chiral EFT emerge.  For example, can the long-range part
of the interaction be treated in perturbation theory?  In other hadronic
systems, the long-range interaction might still be one-pion exchange, and then
Chiral EFT applies except that other heavy particles are substituted for
nucleons.

In this section we briefly describe some of the systems where versions of
Pionless and Chiral EFTs have found application.  We start by discussing how
these EFTs arise from QCD.



\subsection{Connection with QCD}
\label{subsec:qcdconn}

The inclusion of all possible interactions consistent with QCD symmetries
ensures that nuclear EFTs capture the low-energy limit of QCD.  This means
that in principle one can follow a top-down approach and determine low-energy
constants that appear in an EFT from a direct solution of the more
general theory.  While such solutions of QCD (in the highly nonperturbative
low-energy regime) are elusive analytically, lattice calculations have made
significant progress towards nuclear systems.  Matching EFT to
LQCD serves to extend the predictions of QCD in essentially two directions:

\begin{enumerate}

\item
Larger distances: solution by \abinitio methods of an EFT with parameters fixed
by LQCD allows for predictions of properties of larger nuclei and their
reactions, which are difficult to simulate directly from QCD.

\item
Smaller pion masses: with the relative importance of chiral-symmetry-breaking
interactions understood, Chiral EFT can be used as an extrapolation tool
from larger quark---and thus pion---masses to the physical point.

\end{enumerate}

{
Moreover, remnants of QCD's color gauge symmetry can be traced down to nuclear
EFTs.  In particular, it is possible to consider the inverse number of colors,}
{$1/N_{\rm c}$},
as an expansion parameter to constrain nuclear forces.  This has
been studied, for example, by
\textcite{Kaplan:1996rk,Phillips:2013rsa,Phillips:2014kna,Samart:2016ufg,
Schindler:2018irz}.
}
