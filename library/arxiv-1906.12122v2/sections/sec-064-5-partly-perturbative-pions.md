---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear eﬀective ﬁeld theory: status and perspectives"
section_id: sec-064-5-partly-perturbative-pions
section_title: "Partly perturbative pions"
section_number: 5
pages: 50-52
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.995
doc_brief: "Nuclear eﬀective ﬁeld theory: status and perspectives — 82 sections: Nuclear effective field theory: st; Contents; I Introduction"
---
\label{subsubsection:partpertpions}

For a couple of years the choice facing the field was between a power counting
that lacks counterterms in the sense discussed in
Sec.~\ref{subsubsection:singrenorm} (\ie, ensuring that all divergences at a
given order can be absorbed) but worked well phenomenologically
(Sec.~\ref{sebsubsec:weinbergprescription}), and another one that has all
counterterms but failed to converge even at relatively small energies
(Sec.~\ref{subsubsection:pertpions}).  A way out was suggested by
\textcite{Nogga:2005hy} and carried out by
\textcite{Valderrama:2009ei,Valderrama:2011mv,Long:2011qx,Long:2011xw,
Long:2012ve}.  Perhaps not surprising in hindsight, this solution is a middle
ground between Weinberg's prescription and fully perturbative pions.  It is
based on two observations:

\begin{enumerate}

\item
Pions are perturbative in sufficiently high two-nucleon partial waves.  For an
orbital angular momentum $l> l_{\text{cr}}$, where
$l_{\text{cr}}(l_{\text{cr}}+1)\sim \Mhi/\MNN$, the centrifugal barrier
dominates over OPE at all distances $r \simge 1/\Mhi$ relevant when $Q\lesssim
\Mhi$.  In these waves OPE should be perturbative for the external momenta where
Chiral EFT holds~\cite{Nogga:2005hy}.  In other words, OPE in the radial
Schr\"odinger equation is an expansion in $Q/\MNN^{(l)}$, where $\MNN^{(0)} =
\MNN$ but $\MNN^{(l)}$ increases with $l$.  For $l \le l_{\text{cr}}$, OPE is
{nonperturbative}.  In these waves, and in these waves only, OPE needs to be
iterated at LO, as observed by \textcite{Fleming:1999ee}.  The LECs needed for
renormalization (Sec.~\ref{subsubsection:singrenorm}) should, of course, be
iterated as well.  All subleading interactions are to be treated in
distorted-wave perturbation theory for $l \le l_{\text{cr}}${, and in
ordinary perturbation theory for $l > l_{\text{cr}}$.}

\item
Multiple pion exchange, being suppressed by powers of $Q/(4\pi f_\pi)$, should
be small after renormalization, and thus amenable to perturbation theory in all
waves.  It is more singular than OPE, but can be renormalized perturbatively
with a finite number of LECs~\cite{Long:2007vp}.

\end{enumerate}

Since the OPE tensor force survives in the chiral limit, for $m_\pi \simle
\MNN$ one can perform an additional expansion around the chiral
limit~\cite{Beane:2001bc}, but, as discussed in
Sec.~\ref{subsubsection:pertpions}, this expansion is not likely to be useful
much beyond the physical pion mass.

For $\Mhi >\MNN$, \ie, $\MNN$ counted as a low-energy scale, one expects
$l_{\text{cr}}\ge 1$.  Of course, other dimensionless factors stemming from
spin and isospin make the transition from {nonperturbative} to perturbative
OPE somewhat fuzzy, which however does not mean that such a transition does not
exist.  Early studies of perturbative pions with and without
Deltas~\cite{Kaiser:1997mw,Ballot:1997ht,Kaiser:1998wa}, which did not
discriminate between iterated pion exchange and multiple pion exchange in the
potential, indicated that pion exchange might be perturbative for $l\simge 3$.
This interpretation is also consistent with subsequent investigations of
peripheral waves with chiral potentials up to
$\OO(Q^6/\MQCD^6)$~{\cite{Entem:2002sf,Epelbaum:2003gr,Krebs:2007rh,
Entem:2014msa,Entem:2015xwa}}.  Qualitatively, this result has been confirmed
for OPE~\cite{Nogga:2005hy}.  A semi-analytical estimate~\cite{Birse:2005um} of
the momenta where the tensor part of OPE needs to be treated
{nonperturbatively}
in the lower triplet waves is given in Table~\ref{tab:OPEtensorcrit}.
{Some evidence thus points to $l_{\text{cr}}\approx 3$.
More detailed, recent analyses suggest, however, that pions are perturbative
up to a relatively high scale in all waves other than $^3S_1$-$^3D_1$ and
$^3P_0$ \cite{Wu:2018lai,Kaplan:2019znu}.}


\begin{table}[tb]
\begin{center}
\begin{tabular}{|c|c||c|c||c|c|}
\hline
Channel & $p_{\text{cr}}$/MeV
& Channel & $p_{\text{cr}}$/MeV
& Channel & $p_{\text{cr}}$/MeV \\
\hline
\hline
$^3S_1$-$^3D_1$ & 66 & $^3P_0$ & 182 & $^3P_1$ & 365 \\
$^3P_2$-$^3F_2$ & 470 & $^3D_2$ & 403 & $^3D_3$-$^3G_3$ & 382 \\
$^3F_3$ & 2860 & $^3F_4$-$^3H_4$ & 2330 & $^3G_4$ & 1870 \\
\hline
\end{tabular}
\end{center}
\caption{{Estimate of the critical values} $p_{\text{cr}}$ of the
relative momentum in the lowest
two-nucleon triplet channels above which the OPE tensor force cannot be treated
perturbatively~\cite{Birse:2005um}.
\label{tab:OPEtensorcrit}}
\end{table}


In the low $2N$ waves where $l \le l_{\text{cr}}$ and $\MNN^{(l)}\approx
\MNN$, the situation at LO is similar to Weinberg's prescription, except that
more short-range interactions are needed for
renormalization~\cite{Nogga:2005hy} than implied by NDA.
{For example, in the $^1S_0$ channel OPE at LO solves the problem of the
slow convergence of perturbative pions~\cite{Beane:2001bc}
at the cost of the additional $D_{2\rm s}$ LEC in Eq.~\eqref{C0D0}.
The residual $1/\Lambda$ dependence then
means~\cite{Long:2012ve} that a correction appears at $\OO(Q/\MQCD)$
from the two-derivative contact interaction responsible for the
short-range contribution to the effective range,
similarly to Pionless EFT (Sec. \ref{subsubsec:regren}).}
At higher orders in the lower partial waves,
multiple-pion exchanges appear and require at $\OO(Q^\mu/\MQCD^\mu)$ LECs with
up to $\mu$ derivatives more than the LECs appearing at LO~\cite{Long:2007vp}.

{
This approach was confronted with empirical phase shifts for the lower $2N$
partial waves by~\textcite{Nogga:2005hy,Epelbaum:2006pt,Valderrama:2009ei,
Valderrama:2011mv,Long:2011qx,Long:2011xw,Long:2012ve,Yang:2016brl}.
}
The results of~\textcite{Long:2011xw} are included in
Fig.~\ref{fig:ThreeSOnePhase}, whereas Fig.~\ref{fig:Valderrama_2011mv}
shows the $\ThreePNot$ results of~\textcite{Valderrama:2011mv} as
a further example.
{While in both cases $\OO(Q^2/\MQCD^2)$ improves on
$\OO(1)$, $\OO(Q^3/\MQCD^3)$ goes in the wrong
direction---perhaps an indication that a better description of the
pion-nucleon subamplitude with an explicit Delta isobar is needed.}


\begin{figure}[tbp]
\centering
\includegraphics[width=0.95\columnwidth]{ps-3P0-pert_set-III_color}
\caption{{The $N\!N$ \ThreePNot phase shift $\delta$ as a function
 of the center-of-mass momentum $k_{c.m.}$
 at different chiral orders:
 ${\mathcal O}(1)$ (green),
 ${\mathcal O}(Q^2/\MQCD^2)$ (red), and
 ${\mathcal O}(Q^3/\MQCD^3)$ (blue),
 according to \textcite{Valderrama:2011mv}.
 Bands represent the variation of a
 coordinate-space cutoff in the range 0.6--0.9 fm, with the dashed
 line showing the ${\mathcal O}(Q^3/\MQCD^3)$ results with a 0.3 fm cutoff.
 The cyan band shows the ${\mathcal O}(Q^3/\MQCD^3)$
 potential in Weinberg's prescription with the regularization procedure
 of \textcite{Epelbaum:2003xx}, where the momentum-space cutoff in
 pion loops (Lippmann-Schwinger equation)
 is varied between 500 and 700 (450 and 650) MeV.
 The solid black line is the Nijmegen phase-shift analysis~\cite{Stoks:1993tb}.
 Figure from \textcite{Valderrama:2011mv}.}
 Courtesy of M.~Pav\'on Valderrama.
}
\label{fig:Valderrama_2011mv}
\end{figure}


Little is known quantitatively about partly perturbative pions beyond the
two-nucleon system. The three-nucleon system is renormalized properly without a
three-nucleon force at LO~\cite{Nogga:2005hy,Song:2016ale} and, without
explicit Deltas, also at NLO~\cite{Song:2016ale}.  The truncation in $l$ needed
at LO is reminiscent of the truncation in total {two-nucleon}
angular momentum typically
invoked in solutions of the Faddeev and Faddeev-Yakubovski equations for three-
and four-nucleon systems with phenomenological potentials. However, to go to
higher orders the $l$ dependence of $\MNN^{(l)}$ must be quantified.  So far,
this has been done only in singlet waves~\cite{PavonValderrama:2016lqn}.

{At LO, symmetric nuclear matter was found to saturate,
but with significant underbinding,
in a cutoff-converged Brueckner pair approximation
\cite{Machleidt:2009bh}. This is in contrast to Weinberg's prescription,
where Deltaless \cite{Sammarruca:2018bqh} or Deltaful \cite{Ekstrom:2017koy}
potentials of $\OO(1)$ and $\OO(Q^2/\MQCD^2)$
do not saturate within the EFT domain.
The fact that {higher-order} potentials with this
prescription do
saturate~\cite{Ekstrom:2017koy,Drischler:2017wtt,Sammarruca:2018bqh}
suggests that,
if nuclear matter is within the regime of Chiral EFT, the LO potential
requires more interactions than prescribed by NDA.}


Although they differ in detail from the
{field-theoretical} renormalization
outlined above, RG analyses of the Schr\"odinger
equation~\cite{Birse:2005um,Birse:2010fj,Valderrama:2016koj} support the
conclusion that counterterms in two-nucleon attractive singular waves appear at
lower order than expected on the basis of NDA.  The case is further
strengthened by removing the effect of OPE and (perturbative) TPE from
empirical two-nucleon phase shifts~\cite{Birse:2007sx,Ipson:2010ah}.
The Schr\"odinger RG analysis also
predicts the enhancement of some three-body forces~\cite{Birse:2010fj}.
