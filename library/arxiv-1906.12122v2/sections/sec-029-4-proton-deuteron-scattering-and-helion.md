---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear eﬀective ﬁeld theory: status and perspectives"
section_id: sec-029-4-proton-deuteron-scattering-and-helion
section_title: "Proton-deuteron scattering and helion"
section_number: 4
pages: 21-21
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
toc_source: outline
text_source: latex
latex_prose_ratio: 0.667
latex_coverage_ratio: 0.986
doc_brief: "Nuclear eﬀective ﬁeld theory: status and perspectives — 82 sections: Nuclear effective field theory: st; Contents; I Introduction"
---
\paragraph{Nonperturbative Coulomb effects}

As discussed in Sec.~\ref{sec:pionlessCoulomb}, at the low energies potentially
reached in scattering Coulomb-photon exchange needs to be treated
nonperturbatively, which poses additional technical challenges.  The first
attempt to study Coulomb effects was made in the simpler quartet $S$-wave $pd$
scattering by \textcite{Rupak:2001ci}.  They developed a power counting
that, with some approximations, amounts to iterating a Coulomb potential between
proton and deuteron to all orders, along with the one-nucleon exchange diagram
that also enters in $nd$ scattering.  \textcite{Rupak:2001ci} calculated the
Coulomb-subtracted $S$-wave phase shift in the quartet channel, but could not
reach convergence below $pd$ center-of-mass momenta of $20~\MeV$ (the regime
where Coulomb effects really are nonperturbative).  Convergence down to $3~\MeV$
was later achieved by \textcite{Konig:2011yq} owing to an improved numerical
procedure.  \textcite{Konig:2011yq} also extended the analysis to the doublet
$S$-wave channel, including helion, and applied the partial-resummation approach
of \textcite{Bedaque:2002yg} to calculate higher orders.

\textcite{Ando:2010wq} carried out a direct momentum-space calculation of helion
based on a generalization of the $nd$ integral equation discussed in
Sec.~\ref{sec:Triton}.  Recasting methods developed by
\textcite{Kok:1979aa,Kok:1981aa} into EFT, \textcite{Ando:2010wq} included
Coulomb effects via a fully off-shell Coulomb $T$ matrix and obtained, at a
single momentum cutoff $\Lambda_0=380.689~\MeV$ (the first cutoff value where
the experimental triton binding energy is reproduced without a $3N$ force,
$H(\Lambda_0) = 0$) a \ThreeHe binding energy $B(\ThreeHe) \simeq 7.66~\MeV$,
close to the experimental value of about $7.72~\MeV$.  \textcite{Ando:2010wq}
treated all Coulomb effects nonperturbatively, {but considered the strong
sector only at LO.}  \textcite{Kirscher:2009aj} obtained similar numerical
results in a calculation that included \NLO and selected higher-order
interactions as part of an effective potential which was treated exactly.

The pionless calculation of $pd$ scattering and helion was revisited and
extended by \textcite{Koenig:2013} and \textcite{Konig:2014ufa}, who argued that
the \NLO $pd$ system, within the partial-resummation approach, is not properly
renormalized by the isospin-symmetric $3N$ force alone.  The same conclusion was
reached in a parallel analysis by \textcite{Vanasse:2014kxa}, who calculated
$pd$ scattering and \ThreeHe at \NLO in strict perturbation theory.  Using an
asymptotic analysis, it was shown that Coulomb at LO requires a nonderivative
$3N$ interaction at \NLO (but not \LO) to properly renormalize the $pd$ system.
{At this level, one can no longer predict low-energy
$pd$ scattering from $nd$ scattering without further input.}
Fixing the corresponding LEC to the \ThreeHe binding energy gives good
agreement with an analytically-derived expression, and it also provides
cutoff-stable
results for the phase shift.  In contrast, \textcite{Kirscher:2015zoa} recently
argued that \ThreeHe is renormalized at NLO without an additional counterterm
($pd$ scattering was not investigated).  While both calculations use Pionless
EFT, they differ in the numerical implementation and regularization scheme.

A comparison of the different schemes for the counting of Coulomb effects
in $pd$ scattering up to \NLO was provided by \textcite{Konig:2013cia}.
These authors argued that for the scattering of composite charged particles
there is a certain arbitrariness in the definition of Coulomb-subtracted
quantities (phase shifts and modified ERE parameters), namely whether or not
information about the deuteron substructure is included in the definition of
the pure Coulomb phase shift.

\paragraph{Perturbative Coulomb effects}

Renewed interest and developments in the strict application of perturbation
theory also motivated a new look into the counting of Coulomb effects.  The
characteristic trinucleon momentum scale $\gamma_T\sim 80~\MeV \gg \alpha m_N$
suggests that Coulomb effects should be a perturbative correction to the
\ThreeHe binding energy (compared to the triton as its isospin mirror state).
Already \textcite{Konig:2014ufa} showed that the calculation of
\textcite{Ando:2010wq} can be reproduced essentially unchanged when the fully
off-shell Coulomb $T$ matrix is replaced by one-photon exchange diagrams.
However, the calculation of \textcite{Konig:2014ufa} is still nonperturbative
because $B(\ThreeHe)$ is extracted from the pole in the off-shell $pd$ amplitude
obtained from an integral equation that resums both one-nucleon exchange as well
as $\OO(\alpha)$ Coulomb diagrams.  \textcite{Konig:2015aka} instead calculated
the binding-energy difference $B(\ThreeH)-B(\ThreeHe)$ as a perturbation
around an isospin-symmetric LO including a contribution missed in the earlier
calculation of \textcite{Konig:2014ufa}.  Once the logarithmic divergence
generated by $pp$ Coulomb effects is isolated and properly renormalized, the
\NLO \ThreeHe binding energy converges as the cutoff increases without an
isospin-breaking $3N$ force.  \textcite{Konig:2015aka} find $B(\ThreeHe) = (7.62
\pm 0.17)~\MeV$, supporting the perturbative nature of Coulomb in this bound
state.  The same conclusion was reached independently by
\textcite{Kirscher:2015zoa}.  These results suggest that for nuclear ground
states Coulomb is an \NLO effect and isospin-breaking $3N$ forces do not enter
up to this order.
{The same holds for $pd$ scattering for center-of-mass momenta
$k\gsim20~\MeV$, which \textcite{Konig:2016iny} showed to be
predicted from $nd$ scattering up to NLO.}

\paragraph{Dineutron constraints}

\textcite{Kirscher:2011zn} used Pionless EFT to constrain the neutron-neutron
($nn$) scattering length, for which there exist conflicting experimental
determinations of ${-}16.1\pm0.4~\fm$~\cite{Huhn:2000zz,Huhn:2001yk} and
${-}18.7\pm0.7~\fm$~\cite{GonzalezTrotter:1999zz,GonzalezTrotter:2006wz}.
Using a model-independent correlation between the difference of the $nn$ and
(Coulomb-modified) $pp$ scattering lengths on the one hand and the
\Triton-\ThreeHe binding-energy difference on the other,
\textcite{Kirscher:2011zn} extracted $\ann=(-22.9\pm 4.1)~\fm$ from an \LO
calculation where isospin-breaking, nonderivative $N\!N$ contact interactions
are included.

\textcite{Kirscher:2011zn} only considered negative values for $\ann$, thus
excluding the possibility of a bound shallow state, the existence of which would
correspond to $\ann$ large and positive.  Motivated by renewed experimental
interest in the existence of such a state, \textcite{Hammer:2014rba} revisited
the calculation and argued that the relevant parameter that enters the pionless
calculation is not $\ann$ directly, but rather its inverse, such that going from
large negative to large positive $\ann$ is only a small change.  Extending the
calculation of \textcite{Kirscher:2011zn} to \NLO, and taking into account the
new $pd$ counterterm identified by \textcite{Vanasse:2014kxa},
\textcite{Hammer:2014rba} concluded that Pionless EFT currently does not
exclude a bound dineutron state.
