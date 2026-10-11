---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear effective field theory: status and perspectives"
section_id: sec-003-3-regularization-and-renormalization
section_title: "Regularization and renormalization"
section_number: 3
pages: 11-12
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
doc_brief: "Nuclear effective field theory: status and perspectives — 34 sections: Contents; Two-body scattering amplitude; Power counting"
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.994
---
\label{subsubsec:regren}

Loops in a quantum field theory are often not convergent, and the same in
true in Pionless EFT. Observables are rendered finite by renormalization.
For example, if we introduce a regulator function $f(x)$,
the nucleon bubble integral becomes

\begin{multline}
 I_0(k) = \MN\int\ddq
 \frac{f(\vecq^2/\Lambda^2)}{k^2- \vecq^2 + \ii\eps} \\
 = {-}\frac{\MN}{4\pi}
 \left[\theta_1\Lambda- \sqrt{-k^2-\ii\eps}+\OO(k^2/\Lambda) \right]
 \,,
\label{eq:I0-cutoff}
\end{multline}

where $\theta_1$ is a dimensionless number that depends
on the form of $f(x)$ (for example, $\theta_1=2/\pi$ for a step function).
With Eq.~\eqref{eq:T-kcot-b} truncated at the scattering length as a
renormalization condition, the choice

\begin{equation}
 C_0(\Lambda)= \frac{4\pi}{\MN}\frac{1}{1/a_0-\theta_1\Lambda}
\label{eq:C0-Lambda}
\end{equation}

ensures, to this order, that the physical amplitude is independent of
$\Lambda$, up to corrections that vanish as $\Lambda\to\infty$.
The latter can be removed by higher-order LECs, such as $C_2(\Lambda)$.
It is the non-analytic
dependence on energy, which is regulator independent, that characterizes a
loop. The corresponding term in Eq.~\eqref{eq:I0-cutoff} is an explicit example
of the estimates~\eqref{nucprop} and~\eqref{redloopint}.

\paragraph{Schemes and power counting}

In early stages, there was much confusion about whether or not the choice of
regularization should be understood to affect the power-counting scheme.
The difference between the \emph{artificial} regulator parameter $\Lambda$ and
the breakdown scale $\LamNoPi$ of the theory has not always been appreciated.
For example, \textcite{Kaplan:1998tg} have argued that $C_0\propto\Lambda^{-1}$
would again give a theory with a very limited range of applicability.  The need
to choose $\Lambda\simge \Mhi$ in order to suppress regulator artifacts
$\sim\OO(1/\Lambda)$ does seem to invalidate the scaling
$C_0\propto\aleph^{-1}$, but there are correlations among the diagrams which are
captured by determining $C_0(\Lambda)$ {\emph{after} resummation},
reflecting the original $\aleph$ counting.

If one uses dimensional regularization to render integrals finite, the $I_0$
bubble does not have a pole in four spacetime dimensions, so in the minimal
subtraction scheme there would be no divergence at all.  {Instead of this,
\textcite{Kaplan:1998tg} {advocate explicitly subtracting} the pole in
three dimensions (corresponding to the linear divergence in the cutoff scheme),
thereby introducing a renormalization scale $\mu$, which can be chosen freely,
and giving Eq.~\eqref{eq:C0-Lambda} with $\theta_1\Lambda\to \mu$.
This procedure, called ``power divergence subtraction'' (PDS),
makes the need for resummation of the bubble diagrams more transparent.
Picking $\mu\sim Q$, the \emph{running} coupling $C_0$ scales
like $Q^{-1}$, implying again that each diagram in Fig.~\ref{fig:BubbleChain} is
of the same order.}  With this scheme, power counting is ``manifest'' in the
sense that it is reflected by the scaling of coupling constants even after
renormalization has been carried out.  \textcite{Phillips:1998uy} have shown
that if \emph{all} poles of a divergent loop integral are subtracted---like the
original PDS, one particular choice of infinitely many possibly schemes---one
recovers exactly the same result as with a simple momentum cutoff.

{Under an appropriate power counting, changing the low-energy points used
as renormalization conditions affects the running of the LECs by $1/\Lambda$
terms, and leads to the same $T$ matrix up to higher-order terms.
Taking for example the pole position $\ii\gamma$ instead of zero energy
generates the LO amplitude with $1/a_0 \to \gamma$; the relative difference is
an NLO correction $\sim r_0/a_0 = \OO(\Mlo/\Mhi)$.
While the \apriori EFT error estimate is always determined by neglected higher
orders, the freedom to choose what input parameters are used at a given order
can improve agreement of the \emph{central values} with experimental data.}
{\textcite{Gegelia:1998iu} discusses the relation of subtractive
renormalization to the other approaches mentioned above.}

It was eventually realized~{\cite{Lepage:1997cs}} that cutoff variation can
be used (and is particularly useful in numerical calculations) as a diagnostic
for missing interactions at a given order, an example of which will be given in
Sec.~\ref{sec:Triton}.  \textcite{Long:2012ve} pointed out that also the leading
\emph{residual} cutoff dependence can be used to infer the existence of
next-order operators.  Equation~\eqref{eq:I0-cutoff}, for example, indicates
that $C_2\propto \Mhi^{-1}$ in order for the residual dependence on
$\Lambda\simge \Mhi$ to be no larger than NLO.  Thus renormalization provides
guidance for the power counting.


\paragraph{Subleading resummation}

Experience with nonsingular potentials makes it almost automatic to solve the
Schr\"odinger equation exactly with a truncation of the
potential~\eqref{eq:V-pp}.  At LO this is equivalent to the
resummation~\eqref{eq:T-C0}.  Renormalization of the truncation at the level of
$C_2$, however, leads to $r_0\simle
\Lambda^{-1}$~\cite{Cohen:1996my,Phillips:1996ae,Scaldeferri:1996nx}, a version
of the so-called ``Wigner bound''~\cite{Wigner:1955zz}.  This is problematic
for $N\!N$ scattering where $r_0>0$.  At first interpreted as a failure of EFT,
this observation reveals instead the danger of resumming subleading singular
potentials~\cite{vanKolck:1998bw}.  Such a resummation includes a subset of
arbitrarily high-order contributions without all the LECs needed for
perturbative renormalization, such as $C_4$ when $C_2$ is inserted twice at
N$^2$LO.  It is still possible to work with a fixed cutoff that reproduces
$r_0$, at the cost of losing the ability to use cutoff variation $\Lambda\simge
\Mhi$ as a diagnostic for missing interactions.  Moreover, there is no
guarantee that results for other observables will be any better than those
obtained from a perturbative treatment of subleading corrections.  An example
is given by \textcite{Stetcu:2010xq}.
