---
doc_id: arxiv-2505.02719v2
doc_title: "On the Palais-Smale condition in geometric knot theory"
section_id: sec-013-bending-energy-with-self-avoidance-term
section_title: "Bending energy with self-avoidance term"
section_number: null
pages: 29-31
source_pdf: 2505.02719v2.pdf
source_sha256: 1803d10aa55c18cf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.868
latex_coverage_ratio: 0.987
doc_brief: "On the Palais-Smale condition in geometric knot theory — We prove that various families of energies relevant in geometric knot theory satisfy the Palais–Smale condition (PS) on submanifolds of"
---
\label{sec:PS-elastic-knot}
Now we deal with linear combinations of bending energy $\BendingEnergy$ and some choice
of knot energy $\FL$ in any one of the three knot energy families introduced
in \cref{sec:intro}, i.e., 
$\FL\in\{\TP^{(p,q)},\intM^{(p,q)},E^{\alpha,p}\}$ 
in the respective range \cref{eq:individual-energy-spaces}
for the parameters $p,q,$ and $\alpha,p$. 
For each energy space
 one has $s>\frac1{\rho}$ so that the fractional Sobolev
space $W^{1+s,\rho}(\R/\Z,\R^n)$
embeds compactly into $C^1(\R/\Z,\R^n)$; see
\cite[Theorem A.2]{knappmann-etal_2023}. Since $W^{2,2}$ embeds 
continuously into $W^{1+\sigma,2}$ for any $\sigma\in (0,1)$ (see, e.g.,
\cite[Lemma 2.20]{steenebruegge_2023}), and the latter embeds
compactly into $W^{1+s,\rho}(\R/\Z,\R^n)$ as long as
$s\in (0,1)$, $\rho\in (1,\infty)$ and $\sigma-s >\max\{
\frac{1}{2}-\frac1{\rho},0\}$ by virtue of \cite[Proposition A.3(i)]{matt-etal_2023},
we can check for each energy separately 
under the additional restriction \cref{eq:shrink-range}
of the parameter range that we
have a compact embedding of $W^{2,2}(\R/\Z,\R^n)$ into
the respective energy space. Therefore, to set the stage for the application of \cref{cor:PS-total-energy}, we define $\HL \ceq H^2(\R/\Z,\R^n)$,
$\OL \ceq H^2_\injreg(\R/\Z,\R^n)$, $\BL \ceq C^1(\R/\Z,\R^n)$ as we did
for the pure bending energy $\BendingEnergy$, and add the Banach spaces
$\CL \ceq W^{1+s,\rho}(\R/\Z,\R^n)$ with its open subset $\UL\ceq
W^{1+s,\rho}_\injreg(\R/\Z,\R^n)$ of immersed knots, where we choose
the fractional differentiability $s$ and integrability $\rho$ adapted to
the respective knot energy as in \cref{eq:individual-energy-spaces}, only
with the slightly more restricted parameter ranges \cref{eq:shrink-range}
assumed in \cref{thm:bending-knot-energy}.

\begin{refproof}[Proof of \cref{thm:bending-knot-energy}]
The bending energy $\BendingEnergy$
as well as all knot energies considered are non-negative. Moreover, it follows from
\cite[Proposition 4.8]{okabe-schrader_2023} that $\BendingEnergy\in C^1(\OL)$. 
Continuous
differentiability of the knot energies on the open subset $\UL$ of their 
energy space in the respective full parameter range given in \cref{eq:individual-energy-spaces} was shown in \cite[Theorem 1.4 \& subsequent remark]{blatt-reiter_2015a}
(see also \cite{wings_2018}) for $\TP^{(p,q)}$, in 
\cite[Theorem 3]{blatt-reiter_2015b}
for $\intM^{(p,q)}$, and in \cite[Theorem 5.1]{matt-etal_2023}
for $E^{\alpha,p}$. The slightly
restricted parameter ranges 
lead to a compact injection $\iota:\HL\hookrightarrow \CL$ with $\iota(\OL)\subset
\UL$ for any of the three knot energy families.
The conditions \ref{condE} and \ref{condP} follow from \cref{cor:basic-assumptions} for $s=1$. 
In addition, we have checked conditions \ref{condB*}, \ref{condS}, and \ref{condD} for $\BendingEnergy|_{\AL^2_\bz}$
in \cref{thm:PS_elastic}. 

As to condition \ref{condP*} required in \cref{cor:PS-total-energy},
observe that the explicit formula of the projection $\pr_\g^{\AL^2_\bz}(h)$
in \cref{eq:projection-ALsz} and \cref{eq:projection-ALs} based on the differential
$\D \varSigma $ of the logarithmic strain $\varSigma$ (see \cref{eq:log-strain-bounded-differential}) and its right
inverse $Y_\g$ given by \cref{eq:right-inverse-Y} does \emph{not} require the full regularity
$h\in H^2(\R/\Z,\R^n)$ to make sense. 
In fact, the starting point of the proof of \cref{prop:projection-ALs} uses \cite[Lemma 5.2]{knappmann-etal_2023} which is 
formulated for general fractional Sobolev spaces $W^{1+s,\rho}$, where $s\in (0,1),$
$\rho>1$ satisfy $s-\frac1{\rho} >0$. The energy spaces of all three knot energy families considered
here meet these requirements on the parameters $s$ and $\rho$; see \cref{eq:individual-energy-spaces}. So, we simply set 
$$
        \PR_\g \eta
        \ceq
        (\Id_\CL-Y_\g  \D \varSigma_\g) \, \eta - \pars[\big]{(\Id_\CL-Y_\g \, \D \varSigma_\g) \, \eta}(0)
        \quad\Fo\eta\in\CL,
$$
and copy the proof of \cref{prop:projection-ALs} line by line replacing
$h\in H^2(\R/\Z,\R^n)$ by $\eta\in\CL$ in each step, arriving at the estimate
corresponding to \cref{eq:projection-bound}, which confirms \ref{condP*}.


So, it remains to establish condition
\ref{condL*} for each of the knot energies, i.e., for $\FL\in\{\TP^{(p,q)},
\intM^{(p,q)},E^{\alpha,p}\}$. The key observation is the following: Any sequence
$(\g_k)_k\subset\AL^2_\bz$
with uniformly bounded knot energy, i.e., with $F\ceq\sup_{k\in\N}
\widetilde{\FL}(\g_k)
<\infty$, where $\widetilde{\FL}=\FL\circ\iota|_{\AL^2_\bz}$, satisfies a uniform bilipschitz
estimate depending only on the energy bound $F$ and the fixed  parameters
$s$ and $\rho$ determining the respective energy space as in 
\cref{eq:individual-energy-spaces}. In other words, there is a
constant $c=c(s,\rho,F)>0$ such that 
\begin{equation}\label{eq:uniform-bilip}
|\g_k(u)-\g_k(v)|\ge  c \,|u-v|_{\R/\Z}\quad\Foa u,v\in\R/\Z,\,k\in\N.
\end{equation}

For $\TP^{(p,q)}$ this was proven in \cite[Proposition 2.7]{blatt-reiter_2015a},
for $\intM^{(p,q)}$ in \cite[Proposition 2.1]{blatt-reiter_2015b}, and for
$E^{\alpha,p}$ in \cite[Proof of Theorem 1.1, pp. 21-22]{matt-etal_2023}.
The sequences $(\g_k)_k$
considered  in \ref{condL*} are also assumed to converge weakly in $\HL$
to some limit curve $\g_\infty\in\HL$.
By the compact embedding $\HL\hookrightarrow \BL=C^1(\R/\Z,\R^n)$ and the subsequence principle
one also has $\g_k\to\g_\infty$ in $C^1$ as $k\to\infty$ so that the bilipschitz
estimate \cref{eq:uniform-bilip} transfers to the limit curve $\g_\infty$; 
hence
$\g_\infty$ itself is a knot, satisfying $|\g_\infty'|=\lim_{k\to\infty}|\g_k'|=1$, and
$\g_\infty(0)=\lim_{k\to\infty}\g_k(0)=\bz$. To summarize,
$\g_\infty\in \AL^2_\bz$, so that \ref{condL*} is satisfied for
each $\FL\in\{\TP^{(p,q)},
\intM^{(p,q)},E^{\alpha,p}\}$. Therefore, \cref{cor:PS-total-energy} is applicable which implies the statement of the theorem.
\end{refproof}

\begin{refproof}[Proof of \Cref{thm:bending-moebius-energy}]
All the properties concerning  $\BendingEnergy$ as well as properties
\ref{condE} and \ref{condP} have been shown in the proof of
\Cref{thm:bending-knot-energy} for the same choice of spaces
$\HL \ceq H^2(\R/\Z,\R^n)$, $\BL \ceq C^1(\R/\Z,\R^n)$ and $\OL\ceq
H^2_\injreg(\R/\Z,\R^n)$. Also, \ref{condP*} follows in the same way if
we choose the slightly smaller Hilbert space $\CL \ceq H^{3/2 +\nu}(\R/\Z,\R^n)$
for some $\nu\in (0,1/2)$,
instead of the natural energy space $H^{3/2}(\R/\Z,\R^n)$ for the
M\"obius energy $E^{2,1}$ (see \cite[Theorem 1.1]{blatt_2012a}).
In \cite[Theorem 3.1]{reiter-schumacher_2021} it was shown that 
$E^{2,1}$ is of class $C^{1,1}_\loc$ on the open subset
$\UL \ceq H^{3/2 +\nu}_\injreg(\R/\Z,\R^n)$ of regular knots in $\CL$.
Finally, for the proof of \ref{condL*} we use the uniform
bilipschitz estimate for $E^{2,1}$ proved, e.g., in 
\cite[Lemma 3.1]{gilsbach-vdm_2018} 
together with the compact embedding $\HL\hookrightarrow\CL$ as
in the proof of \Cref{thm:bending-knot-energy}.
\end{refproof}

\begin{refproof}[Proof of \Cref{cor:minimizing-knots-total-energy}]
According to \Cref{thm:bending-knot-energy,thm:bending-moebius-energy} and their  proofs
all total 
energies $\TL$ under consideration are of class $C^1$ and
satisfy the (PS)-condition, and condition \ref{condL*}; hence
\ref{condL**} on the Hilbert submanifold $\AL^2_\bz$. Moreover,
all energies
are non-negative which verifies \ref{lower-bound}. 
Therefore,  \Cref{cor:critical+minimizers} implies
the result.
\end{refproof}


\begin{refproof}[Proof of \Cref{thm:gradient-flow-total-energy}]
In order to apply our abstract result on gradient flows,  
\Cref{thm:gradflow_subconvergence}, we notice 
first that the smooth arclength submanifold $\AL^2_\bz$ of the Hilbert
space $\HL \ceq H^2(\R/\Z,\R^n)$ inherits the Riemannian metric from the inner
product on $\HL$.
Moreover, the required  $C^{1,1}_\loc$-regularity
of all energies considered in \cref{eq:subfamilies}  holds true
 on the larger open subsets of regular knots in $\HL$,
 which  follows
from \cite[Theorem 3.1]{reiter-schumacher_2021} for the M\"obius energy
$E^{2,1}$, from \cite[Theorem 3.5]{steenebruegge_2023} for the tangent-point
energies $\TP^{(p,q)}$ listed in \cref{eq:subfamilies}, from
\cite[Theorem 2.1]{knappmann-etal_2023} for $\intM^{(p,2)}$, and
from \cite[Theorem 1.55]{knappmann_2020} for the classic integral Menger
curvature 
$\ML_p
=2^p\intM^{(p,p)} $
for $p>3$. The additional upper bounds on $p$ encoded
in  \cref{eq:subfamilies} and \cref{eq:shrink-range} are necessary for
the validity of the (PS)-condition established in 
\Cref{thm:bending-knot-energy} and \Cref{thm:bending-moebius-energy}. 
All energies are non-negative and therefore
satisfy condition \ref{lower-bound}, and we verified already condition
\ref{condL*} in the proof of \Cref{thm:bending-knot-energy} which 
implies condition \ref{condL**} on submanifolds of Hilbert spaces. Now,
\Cref{thm:gradflow_subconvergence} implies all statements on the gradient flow, including
the fact that the critical point in the limit as $t\to\infty$ is ambiently
isotopic to the initial knot $\g_0$ by means of 
\Cref{thm:components-knot-classes}. 
\end{refproof}
