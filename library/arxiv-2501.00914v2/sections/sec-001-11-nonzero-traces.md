---
doc_id: arxiv-2501.00914v2
doc_title: "L-spaces and knot traces"
section_id: sec-001-11-nonzero-traces
section_title: "Nonzero traces"
section_number: 1.1
pages: 3-3
source_pdf: 2501.00914v2.pdf
source_sha256: d94bd6edf8544d4a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 1.0
doc_brief: "L-spaces and knot traces — There has been a great deal of interest in understanding which knots are characterized by which of their Dehn surgeries."
---
We  consider detection by nonzero traces as well, and prove several results that are in stark contrast with what is known about characterizing slopes. For instance, all rational surgeries characterize the trefoils  \cite{osz-characterizing}, but if $K$ is a positive torus knot besides the right-handed trefoil, then it is  unknown whether \emph{any} integer $n\leq 0$ is a characterizing slope for $K$. On the other hand, we use Theorem \ref{thm:lspace-detection-main} to prove the following:

\begin{theorem}
\label{thm:negtracetorus}
If $K$ is a positive torus knot and $n\leq 0$, then $X_n(K)$ detects $K$.
\end{theorem}

This leaves open the question of whether every trace detects each torus knot, which by Theorem \ref{thm:negtracetorus} is equivalent to asking whether every \emph{positive} trace detects each \emph{positive} torus knot. We expect this to be true for torus knots of the form $T_{2,2g+1}$, and  prove the following  result in that direction. Together with Theorem \ref{thm:negtracetorus}, this result implies  that if knot Floer homology detects $T_{2,2g+1}$ then  so does every trace; this knot Floer result  is   known  to hold when $|g| \leq 2$ \cite{osz-genus,ghiggini,frw-cinquefoil}.

\begin{theorem} \label{thm:positive-trace-t2n-main}
Suppose for some knot $K$ and  positive integers $n$ and $g$ that $X_n(K) \cong X_n(T_{2,2g+1}).$  Then either $K = T_{2,2g+1},$ or $1 \leq n \leq 4g-1$ and $K$ is a hyperbolic knot such that \[\hfkhat(K) \cong \hfkhat(T_{2,2g+1})\] as bigraded vector spaces.
\end{theorem}


We remark that not every positive integer is a characterizing slope for each positive torus knot, not even for torus knots of the form $T_{2,2g+1}$. For example, \[S^3_{21}(T_{4,5}) \cong S^3_{21}(T_{2,11}).\] In Appendix~\ref{sec:torus-pairs}, we describe infinitely many new pairs of distinct positive torus knots $(K,J)$  such that $S^3_n(K) \cong S^3_n(J)$ for some integer $n>0$, generalizing a family discovered by Ni--Zhang \cite{ni-zhang-torus-1} which includes the example above. On the other hand, Proposition~\ref{prop:compare-torus-surgeries} guarantees in this case that $g(K) \neq g(J)$, and then Theorem~\ref{thm:lspace-detection-main} implies that these knots are distinguished by their $n$-traces.
