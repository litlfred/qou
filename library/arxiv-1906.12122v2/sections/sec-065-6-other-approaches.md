---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear eﬀective ﬁeld theory: status and perspectives"
section_id: sec-065-6-other-approaches
section_title: "Other approaches"
section_number: 6
pages: 52-53
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.98
doc_brief: "Nuclear eﬀective ﬁeld theory: status and perspectives — 82 sections: Nuclear effective field theory: st; Contents; I Introduction"
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
