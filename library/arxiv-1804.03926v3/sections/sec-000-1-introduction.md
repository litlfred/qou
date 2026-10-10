---
doc_id: arxiv-1804.03926v3
doc_title: "Weighted Poincaré inequalities, concentration inequalities and tail bounds related to Stein kernels in dimension one"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1804.03926v3.pdf
source_sha256: 8ad8e2d5a8881a5b
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.994
doc_brief: "Weighted Poincaré inequalities, concentration inequalities and tail bounds related to Stein kernels in dimension one — We investigate links between the so-called Stein’s density approach indimension"
---
Since its introduction by Charles Stein (



\cite{MR0402873, MR882007}

), the so-called Stein's method is a corpus of techniques that revealed
itself very successful in studying probability approximation and convergence
in law (see for instance 



\cite{MR2732624, MR3727600, MR3595350}

and references therein). Much less is known regarding the interplay between
Stein's method and functional inequalities. Recently, a series of papers (



\cite{LedoucNourdinPeccati:15,  MR3665794,  MR3682667, courtade2017existence}

) started to fill this gap.

More precisely, Ledoux et al. \cite{LedoucNourdinPeccati:15} provide some
improvement of the log-Sobolev inequality and Talagrand's quadratic
transportation cost inequality through the use of a Stein kernel and in
particular, the Stein discrepancy that measures the closeness of the Stein
kernels to identity. In a second paper \cite{MR3665794}, these authors also
provide a lower bound of the deficit in the Gaussian log-Sobolev inequality
in terms Stein's characterization of the Gaussian distribution. Recently,
Fathi and Nelson \cite{MR3682667} also consider free Stein kernel and use it
to improve the free log-Sobolev inequality. Finally, Courtade et al. \cite
{courtade2017existence} proved that the existence a reversed weighted Poincar
\'{e} inequality is sufficient to ensure existence of a Stein kernel. To do
so, they use an elegant argument based on the Lax-Milgram theorem. They also
provide bounds on the Stein discrepancy and application to a quantitative
central limit theorem.

Particularizing to dimension one, the present paper aims at pursuing
investigations about the relations between Stein's method - especially Stein
kernels - and some functional inequalities, together with some concentration
inequalities. The limitation to dimension one comes, for most of the
results, from the one-dimensional nature of the covariance identities given
in Section $2$, that are instrumental for the rest of the paper and which
crucially rely on the use of the properties of the cumulative distribution
function.

We prove that a measure $\nu $ having a finite first moment and a density
with connected support satisfies a weighted Poincar\'{e} inequality in the
sense of \cite{MR2510011}, with the weight being the Stein kernel $\tau
_{\nu }$ (see the definition in Section \ref{section_cov_identity}\ below),
that is unique in this case. More precisely, for any $f\in L_{2}\left( \nu
\right) $, absolutely continuous, we have
\begin{equation}


\var

\left( f\left( X\right) \right) \leq \mathbb{E}\left[ \tau _{\nu }\left(
X\right) \left( f^{\prime }\left( X\right) \right) ^{2}\right] \text{ .}
\label{intro_ineq_weight_Poin}
\end{equation}

The latter inequality allows us to recover by different techniques some
weighted Poincar\'{e} inequalities previously established in \cite
{BobkovLedoux:14}\ for the Beta distribution or in \cite{MR3519678}\ for the
generalized Cauchy distribution and to highlight new ones, considering for
instance Pearson's class of distributions.

It is also well-known that Muckenhoupt-type criteria characterize (weighted)
Poincar\'{e} and log-Sobolev inequalities on the real line (



\cite{MR1845806, MR1682772}

). We indeed recover, up to a multiplicative constant, inequality (\ref
{intro_ineq_weight_Poin}) from the classical Muckenhoupt criterion.
Furthermore, using the criterion first established by Bobkov and G\"{o}tze 
\cite{MR1682772} to characterize log-Sobolev inequalities on the real line,
we prove that, under the conditions ensuring the weighted Poincar\'{e}
inequality (\ref{intro_ineq_weight_Poin}), together with some asymptotic
assumptions on the behavior of the Stein kernel around the edges of the
support of the measure $\nu $, the following inequality holds,
\begin{equation}


\ent

_{\nu }\left( g^{2}\right) \leq C_{\nu }\int \tau _{\nu }^{2}\left(
g^{\prime }\right) ^{2}d\nu \text{ ,}  \label{intro_ineq_weight_log_Sob}
\end{equation}
for some constant $C_{\nu }>0$ and with $


\ent

_{\nu }\left( g^{2}\right) =\int g^{2}\log g^{2}d\nu -\int g^{2}d\nu \log
\int g^{2}d\nu $. More precisely, if the support of $\nu $ is compact, then
inequality (\ref{intro_ineq_weight_log_Sob}) is valid if $\tau _{\nu }^{-1}$
is integrable at the edges of the support. If on contrary, an edge of the
support is infinite, then a necessary condition for inequality (\ref
{intro_ineq_weight_log_Sob}) to hold is that the Stein kernel does not tend
to zero around this edge.

We also derive asymmetric Brascamp-Lieb type inequalities related to the
Stein kernel and show that existence of a uniformly bounded Stein kernel is
sufficient to ensure a positive Cheeger isoperimetric constant.

There is also a growing literature, initiated by Chatterjee (\cite{MR2288072}
), about the links between Stein's method and concentration inequalities.
Several approaches are considered, from the method of exchangeable pairs (



\cite{MR2288072,MR2683635, MR3189061,  MR3551202}

), to the density approach coupled with Malliavin calculus (



\cite{MR2556018, MR2568291, MR3380095, MR3352331}

), size biased coupling (



\cite{MR2773032,MR2763529,MR2832913,MR3758727}

), zero bias coupling (\cite{MR3162712}) or more general Stein couplings (
\cite{barbour2018central}). As emphasized for instance in the survey by
Chatterjee \cite{MR3727600}, one major strength of Stein-type methodologies
applied to concentration of measure is that it often allows to deal with
dependent and complex system of random variables, finding for instance
applications in statistical mechanics or in random graph theory.

In the present work, we investigate relationships between Stein kernels and
concentration of measure by building upon ideas and exporting techniques
about the use of covariance identities for Gaussian concentration from
Bobkov, G\"{o}tze and Houdr\'{e} \cite{MR1836739}.

Considering first the case where a Stein kernel is uniformly bounded, we
recover the well-known fact that the associated random variable admits a
sub-Gaussian behavior. But we also prove in this setting some refined
concentration inequalities, that we call generalized Mills' type
inequalities, in reference to the classical Mills' inequality for the normal
distribution (see for instance \cite{duembgen2010bounding}). Assume also
that a Stein kernel $\tau _{v}$ exists for the measure $\nu $, is uniformly
bounded, and denote $c=\left\Vert \tau _{v}\right\Vert _{\infty }^{-1}$.
Then the Furthermore, the function $T_{g}\left( r\right) =e^{cr^{2}/2}
\mathbb{E}\left( g-\mathbb{E}g\right) \mathbf{1}_{\left\{ g-\mathbb{E}g\geq
r\right\} }$ is non-increasing in $r\geq 0$. In particular, for all $r>0$,
\begin{equation}
\mathbb{P}\left( g-\mathbb{E}g\geq r\right) \leq \mathbb{E}\left( g-\mathbb{E
}g\right) _{+}\frac{e^{-cr^{2}/2}}{r}\text{ .}  \label{intro_concen_droite}
\end{equation}

In particular, Beta distributions have a bounded Stein kernel and our
concentration inequalities improve on previously best known concentration
inequalities for Beta distributions, recently due to Bobkov and Ledoux \cite
{BobkovLedoux:14}.

Furthermore, we consider the situation where a Stein kernel has a sub-linear
behavior, recovering and extending in this case sub-Gamma concentration
previously established by Nourdin and Viens \cite{MR2556018}. We also prove
some generalized Mills' type inequalities in this case. More generally, we
prove that the Laplace transform of a Stein kernel controls the Laplace
transform of a Lipschitz function taken on the related distribution. Take $f$
a $1$-Lipschitz function with mean zero with respect to $\nu $ and assume
that $f$ has an exponential moment with respect to $\nu $, that is there
exists $a>0$ such that $\mathbb{E}\left[ e^{af\left( X\right) }\right]
<+\infty $. Then for any $\lambda \in \left( 0,a\right) $,
\begin{equation}
\mathbb{E}\left[ e^{\lambda f\left( X\right) }\right] \leq \mathbb{E}\left[
e^{\lambda ^{2}\tau _{\nu }\left( X\right) }\right] \text{ .}
\label{intro_Laplace_ineq}
\end{equation}
It is worth noting that to prove such a result, we state a generic lemma -
Lemma \ref{Lemma_upper_Laplace}\ Section \ref{section_concentration} -
allowing to bound the Laplace transform of a random variable. We believe
that this lemma has an interest by itself, as it may be very convenient when
dealing with Chernoff's method in general.

We also obtain lower tail bounds without the need of Malliavin calculus,
thus extending previous results due to Nourdin and Viens \cite{MR2556018}
and Viens \cite{MR2568291}.

The paper is organized as follows. In Section \ref{section_cov_identity} we
introduce\ some background material, by discussing some well-known and new
formulas for Stein kernels and Stein factors in connection with Menz and
Otto's covariance identity. We also provide formulas involving the Stein
operator, for densities and tails. Then we prove in Section \ref
{section_weighted_func_ineq} some (weighted) functional inequalities linked
to the behavior of the Stein kernel. In Section \ref{section_concentration}\
we make use of some covariance inequalities to derive various concentration
inequalities for Lipschitz functions of a random variable having a Stein
kernel. Finally, we prove some tail bounds related to the behavior of the
Stein kernel - assumed to be unique - in Section \ref
{section_density_formula_tail_bounds}.
