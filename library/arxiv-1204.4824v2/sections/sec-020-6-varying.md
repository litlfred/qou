---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-020-6-varying
section_title: "Varying"
section_number: 6
pages: 34-34
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.636
latex_coverage_ratio: 1.0
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:varying-theta}

In \S\ref{sec:wnet} above, we held $\vartheta$ fixed and studied the generating functions $F(\wp,\vartheta)$.  In this section we consider what happens when
$\vartheta$ is allowed to vary.  In so doing we will uncover new phenomena,
associated with the 4d BPS states in the theory $S[\fg,C,D]$.

$F(\wp,\vartheta)$ is piecewise constant as a function of $\vartheta \in \R$:
if the pair $(\wp,\vartheta)$ is generic and $\delta \vartheta$ small enough,
$F(\wp,\vartheta) = F(\wp,\vartheta+\delta\vartheta)$.
However, $F(\wp,\vartheta)$ jumps at some special values
$\vartheta = \vartheta_c$.
These special values arise for two distinct reasons,
to be described in the next two sections.

At the special values, we define for convenience\footnote{The meaning of the limit \eqref{eq:f-lim} is easy to understand if there are no other special values
$\vartheta_c'$ in some neighborhood of $\vartheta_c$.  However, it does sometimes happen that the
special values accumulate.  In that case we have to explain what kind of limit we mean in \eqref{eq:f-lim}.
One possibility would be to fix some $R>0$ and work with a
``$Z$-adic'' norm where $\norm{\sum c_a X_{a}} = \sum \abs{c_a} e^{-R \abs{Z_{\bar a}}}$.  We expect that
in this norm the limit \eqref{eq:f-lim} indeed exists.  At any rate, in what follows we work formally,
assuming that the limits make sense.}
\begin{equation} \label{eq:f-lim}
F(\wp, \vartheta_c^\pm) = \lim_{\vartheta \to \vartheta_c^\pm} F(\wp, \vartheta)
\end{equation}
(think of $\vartheta_c^\pm$ as representing $\vartheta_c \pm \varepsilon$ for
$\varepsilon \to 0^+$.)
What we will explain in the rest of this section is how to determine the relation
between $F(\wp, \vartheta_c^+)$ and $F(\wp, \vartheta_c^-)$, and how to extract
from this relation the 4d BPS degeneracies.
