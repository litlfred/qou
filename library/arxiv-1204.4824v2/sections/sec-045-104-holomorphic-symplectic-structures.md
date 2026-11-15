---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-045-104-holomorphic-symplectic-structures
section_title: "Holomorphic symplectic structures"
section_number: 10.4
pages: 66-67
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.877
latex_coverage_ratio: 0.99
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:hol-symp}

In this section we explain one of the important properties of $\Psi_\wnet$:
both its domain and codomain are holomorphic symplectic, and $\Psi_\wnet$ is a
holomorphic symplectic map,
\begin{equation}\label{eq:preserve-sf}
\Psi_{\wnet}^*(\varpi_C) = \varpi_{\Sigma}.
\end{equation}

We begin with $\CM(\Sigma, GL(1); \mathfrak{m})$.  The easiest way to understand
its holomorphic symplectic form is to recall that on the space of \ti{untwisted} connections
there is a standard such form \cite{MR85k:14006,boalch-thesis}.  This form, formally speaking, is
obtained by symplectic quotient from
\begin{equation} \label{eq:alpha-int}
\varpi_{\Sigma} = \int_{\Sigma} \delta \alpha \wedge \delta \alpha
\end{equation}
where $\alpha$ denotes the abelian connection 1-form.\footnote{Here and below,
we use the freedom to fix a gauge
so that we consider only variations $\delta \alpha$ which vanish near the punctures.
This makes  the integral \eqref{eq:alpha-int}
  convergent, despite the fact that the connections we consider are singular.}
Using a choice of spin structure on $\Sigma$ to relate twisted and untwisted connections
we can transfer this holomorphic symplectic structure to
$\CM(\Sigma, GL(1); \mathfrak{m})$; by abuse of notation we denote that structure
also as $\varpi_\Sigma$.

Similarly, $\CM_F(C, GL(K); \mathfrak{m})$ has symplectic form obtained
by symplectic quotient from
\begin{equation}
\varpi_{C} = \int_{C}{\rm Tr}\,\delta \CA  \wedge \delta \CA
\end{equation}
with $\CA$ the nonabelian connection 1-form.  Again we use a spin structure on $C$
to pass between twisted and untwisted connections.

To see why \eqref{eq:preserve-sf} is true,
first consider variations $\delta \alpha$ which have support away
from the spectral network $\wnet$.  In this case the corresponding
variation of $\CA$ is simply
$\delta \CA = \pi_* \delta \alpha$.
It follows easily that for such variations we have $\varpi_\Sigma(\delta \alpha, \delta \alpha') = \varpi_C(\delta \CA, \delta \CA')$.
If $\delta \alpha$ has support intersecting $\wnet$ then the situation is slightly more involved:
there is a distribution-valued contribution to $\delta \CA$ supported on $\wnet$.
By a gauge transformation $\delta \alpha \to \delta \alpha + \de \chi$
we may assume however that $\delta \alpha$ vanishes in neighborhoods of joints.
So it is enough to consider what happens in a patch intersecting only a single wall $p_c$ of $\wnet$.
Taking local coordinates $(x,y)$ on $C$
where $p_c$ is the locus $y = 0$, one finds the form
\begin{equation} \label{eq:delta-a-sing}
 \delta \CA = \pi_* \delta \alpha + s(x) \delta(y) \de y,
\end{equation}
where in the decomposition
\eqref{eq:e-simp-decomp} $s(x)$ is off-diagonal and $\pi_* \delta \alpha$ diagonal.
One thus has ${\rm{Tr}} (s(x) \de y \wedge \pi_* \delta \alpha') = 0$,
so the last term in \eqref{eq:delta-a-sing}
does not contribute to $\varpi$; we get once again
$\varpi_\Sigma(\delta \alpha, \delta \alpha') = \varpi_C(\delta \CA, \delta \CA')$.
