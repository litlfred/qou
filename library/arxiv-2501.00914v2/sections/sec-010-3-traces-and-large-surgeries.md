---
doc_id: arxiv-2501.00914v2
doc_title: "L-spaces and knot traces"
section_id: sec-010-3-traces-and-large-surgeries
section_title: "Traces and large surgeries"
section_number: 3
pages: 13-14
source_pdf: 2501.00914v2.pdf
source_sha256: d94bd6edf8544d4a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 0.926
doc_brief: "L-spaces and knot traces — There has been a great deal of interest in understanding which knots are characterized by which of their Dehn surgeries."
---
\label{sec:large-surgeries}

Our goal in this section is to show that for any $n \geq 0$, the oriented diffeomorphism type of the $n$-trace $X_n(K)$ determines the $\Z/2\Z$-graded Heegaard Floer homology $\hfhat(S^3_m(K))$ of large integer surgeries on $K$, where $m \gg 0$ (in fact, $m \geq 2g(K)-1$ will suffice).  Specifically, the fact that $\chi(\hfhat(Y)) = |H_1(Y)|$ tells us that for integers $m > 0$ we have
\begin{align*}
\dim \hfhat(S^3_m(K)) &= \dim \hfhat_\geven(S^3_m(K)) + \dim \hfhat_\godd(S^3_m(K)) \\
m = |H_1(S^3_m(K))| &= \dim \hfhat_\geven(S^3_m(K)) - \dim \hfhat_\godd(S^3_m(K)),
\end{align*}
and so
\begin{equation} \label{eq:hfhat-odd-from-hfhat}
\dim \hfhat_\godd(S^3_m(K)) = \frac{ \dim \hfhat(S^3_m(K)) - m }{2}.
\end{equation}
When $m$ is sufficiently large, we have a surgery exact triangle
\[ \dots \to \hfhat(S^3) \xrightarrow{F_{X^\circ_m(K)}} \hfhat(S^3_m(K)) \to \hfhat(S^3_{m+1}(K)) \to \dots \]
in which $F_{X^\circ_m(K)} = 0$ because $X^\circ_m$ violates an adjunction inequality, so then
\[ \dim \hfhat(S^3_{m+1}(K)) = \dim \hfhat(S^3_m(K)) + 1 \]
and the right side of \eqref{eq:hfhat-odd-from-hfhat} is independent of $m \gg 0$.  We will show in Theorem~\ref{thm:trace-large-surgery} that the left side of \eqref{eq:hfhat-odd-from-hfhat} is completely determined by \[\hfhat(\partial X_n(K)) \cong \hfhat(S^3_n(K)),\] together with the various $\spc$ components of the cobordism map
\[ F_{X^\circ_n(K)}: \hfhat(S^3) \to \hfhat(S^3_n(K)). \]
It  will follow as a special case that the $0$-trace detects whether a given knot is an L-space knot.   Combined with Theorem \ref{thm:main-lspace-zero}, this will prove our main result, Theorem \ref{thm:main}, which states that the $0$-trace detects every L-space knot.
