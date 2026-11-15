---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear eﬀective ﬁeld theory: status and perspectives"
section_id: sec-002-i-introduction
section_title: "I Introduction"
section_number: null
pages: 2-3
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.984
doc_brief: "Nuclear eﬀective ﬁeld theory: status and perspectives — 82 sections: Nuclear effective field theory: st; Contents; I Introduction"
---
\label{sec:introduction}
The problem of obtaining the properties of atomic nuclei from the interactions
among the constituent nucleons has been central to nuclear physics since its 
inception.  Attempts to derive nuclear forces and currents from the exchange of 
mesons---in particular the lightest meson, the pion---were derailed in the 
1950s by a lack of renormalizability, that is, by an uncontrolled sensitivity 
to physics at short distances.\footnote{Not long after the successful 
renormalization of QED, it was understood that the only relativistic
pion-nucleon coupling that is renormalizable in the same sense is 
pseudoscalar~\cite{Matthews:1951sk}. However, pseudoscalar coupling differs 
from pseudovector coupling by a large nucleon-pair term, which was found
to be in conflict with pion phenomenology~\cite{Marshak:1952NN}.  The favored 
pseudovector coupling required the introduction of short-distance cutoffs, on 
which description of two-nucleon data depended sensitively (see, for example, 
\cite{Gartenhaus:1955zz}).  Subsequent work increasingly emphasized 
the phenomenology of short-range interactions.
{A brief history of nuclear potential models is given by 
\textcite{Machleidt:2011zz} and \textcite{Machleidt:2017vls}.}}  
The rise in the 1970s of a
renormalizable theory of the strong interactions, Quantum Chromodynamics (QCD),
did not immediately offer a path forward: because QCD---formulated in terms of
quarks and gluons---is nonperturbative for processes characterized by external
momenta $Q\simle \MQCD\sim 1~\GeV$, it is very difficult to calculate the
properties of hadrons and nuclei, a problem that becomes more severe as the
number $A$ of nucleons increases.  {Yet, a precise and accurate description 
of nuclei is crucial for the transition from the perturbative regime of the 
Standard Model to the atomic domain and beyond, governed by Quantum 
Electrodynamics (QED) and its small fine-structure constant.} 
{Examples} {relying on input from nuclear physics include
tests of fundamental symmetries (such as neutrinoless double-beta decay to probe
lepton number violation) and reactions in astrophysical environments.}

About a quarter of a century ago effective field theories (EFTs) entered 
nuclear physics~\cite{Weinberg:1990rz,Rho:1990cf,Weinberg:1991um,
Ordonez:1992xp,Weinberg:1992yk,VanKolck:1993ee}.  EFTs had been developed in 
particle and condensed-matter physics to deal with systems containing multiple 
momentum scales.  An EFT captures the most general dynamics among low-energy 
degrees of freedom that is consistent with some assumed symmetries.  In nuclear 
physics, where the symmetries of QCD are known, an EFT provides a realization 
of QCD in terms of hadrons instead of quarks and gluons.  All the details of 
the QCD dynamics at short distances are encoded in the EFT interaction strengths
(``Wilson coefficients'' or ``low-energy constants'').  Scattering amplitudes
(and their poles representing bound states and resonances) are calculated as
expansions in $Q/\Mhi$ and $\Mlo/\Mhi$, {with $\Mhi$ the momentum 
scale where the EFT breaks down and $\Mlo$ standing for low-energy scales 
of} physics we want to capture.  An EFT is renormalizable in the sense that at 
each order in the expansion the sensitivity to unaccounted short-distance
physics is small, that is, of relative $\OO(Q/\Mhi,\Mlo/\Mhi)$.  EFTs opened
the door to a description of nuclear phenomena with systematic error estimates.

EFTs have,
{in fact, revolutionized} nuclear physics.  Most of the ``\abinitio'' 
studies of nuclear structure---based on the explicit solution of the 
Schr\"odinger equation or its equivalents---are now carried out with potentials
inspired by EFT.  A host of nuclear properties has been predicted or postdicted 
from two- and three-nucleon forces, and one- and two-nucleon currents {with}
low-energy constants were determined from $A\le 3$ experimental data.
In parallel, starting with~\textcite{Beane:2006mx}, fully dynamical simulations
of QCD on a discretized and boxed spacetime have been able to access some 
$A\le 4$ properties.  Matching an EFT {to results from} {lattice QCD 
(LQCD)}, {and not just to experiment,} allows for a determination of the
low-energy constants.  EFTs thus build a bridge between QCD and nuclear
structure and reactions.

Historically the first nuclear EFT was \textbf{Chiral (or Pionful) 
EFT}~\cite{Weinberg:1990rz,Rho:1990cf,
Weinberg:1991um,Ordonez:1992xp,Weinberg:1992yk,VanKolck:1993ee},
which is designed for momenta of the order of the pion mass.  In addition to
nucleons, it includes explicit pions, whose interactions are 
constrained by an approximate global symmetry of QCD, the chiral symmetry of 
independent flavor rotations of left- and right-handed quarks.  Chiral EFT 
generalizes a popular hadronic EFT, Chiral Perturbation 
Theory~\cite{Weinberg:1978kz,Gasser:1983yg,Gasser:1984gg}, to $A\ge 2$.  Despite
its phenomenological successes, Chiral EFT has proven to be extremely 
challenging to renormalize due to the singularity of the dominant interactions, 
which have to be treated nonperturbatively in order to produce bound states and 
resonances, \ie, nuclei.  Originally conceived as a renormalization playground,
a simpler EFT---\textbf{Pionless (or Contact) EFT}---focuses on momenta below
the pion mass~{\cite{Bedaque:1997qi,vanKolck:1997ut,Kaplan:1998tg,
Bedaque:1998mb,Kaplan:1998we,vanKolck:1998bw,Birse:1998dk}}.  This EFT, whose 
renormalization is relatively well understood, is constrained only by QCD
spacetime symmetries.  It exhibits a high degree of universality, and except for
the degrees of freedom it is formally identical to other EFTs where all
interactions are of short range.  Light nuclei are well described within the
same framework that has been successful for atomic systems with large scattering
lengths (for example, near a Feshbach resonance)~\cite{Braaten:2004rn}.  A
variant of this EFT, \textbf{Halo/Cluster EFT}, has been
applied~\cite{Bertulani:2002sz,Bedaque:2003wa} to bound states and reactions 
involving halo and cluster nuclei, characterized by such low energies
that one or more tight clusters of nucleons can be treated as elementary 
degrees of freedom.

{No doubt there are ``more effective'' EFTs to be discovered for larger 
nuclei.  In fact, a description of rotational and vibrational bands in heavy 
nuclei has been initiated by \textcite{Papenbrock:2010yg}, with 
successful applications to different nuclei and 
processes~\cite{Papenbrock:2013cra,Perez:2015ufa,
Perez:2016nwc,Perez:2017ksf,Perez:2018cly,Chen:2018jtd,Chen:2019ugo}.  These 
recent developments extend the EFT paradigm to generalized degrees of freedom 
that capture the low-energy physics of deformed nuclei.}

{Here we present a summary of the main ideas, achievements, and prospects
for the nuclear EFTs formulated in terms of nucleons and clusters thereof.}  
These theories can be thought of as a tower of EFTs at successively lower
$\Mhi$, starting at $\MQCD$.  Our emphasis is not on phenomenology, but on the
conceptual similarities and differences among  Chiral, Pionless, and
Halo/Cluster EFTs.  Our hope is that a focused approach will stimulate a
reformulation of our  understanding of heavy nuclei, just as these EFTs have
shed new light on the structure and reactions of light nuclei.

In the remainder of this section some common aspects of nuclear EFTs are 
presented.  Each of the three following sections deal with one nuclear EFT.
In Sec.~\ref{sec:other} we address the connection between these EFTs and QCD, 
as well as broader applications.  We conclude in Sec.~\ref{sec:conclusion}.
We use throughout units such that $\hbar=1$ and $c=1$.
