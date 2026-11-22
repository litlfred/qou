---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-003-13-the-generalized-volume-conjecture-near-2-i
section_title: "The Generalized Volume Conjecture near 2 i"
section_number: 1.3
pages: 5-5
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
toc_source: outline
text_source: latex
latex_prose_ratio: 0.902
latex_coverage_ratio: 1.0
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent polynomials, whose nth term is the nth colored Jones polynomial."
---
\lbl{sub.faithfulresults}



Our next result states that the volume conjecture can only be barely true.

\begin{theorem}
\lbl{thm.near1} {\rm (Proof in Section \ref{sec.cyclotomic})}
For every knot $K$ and every fixed integer $m \neq
0$
$$
\lim_{n\to\infty}  \frac{1}{n} \log|J_{K,n+m}(\exp(2 \pi i/n))| =0.
$$
\end{theorem}

It follows that the {\em double-scaling limit}
$$
\lim_{n,k} \frac{1}{n} \log|J_{K,n}(\exp(2 \pi i/k))|
$$
when $n,k \to \infty$ and $n/k \to 1$ does not exist, or equals to $0$;
with the latter case in contradiction with the Volume Conjecture.
Our next result confirms the strange behavior in the Generalized Volume
Conjecture when $\a/(2 \pi i)$ is rational, not equal to $1$.

\begin{theorem}
\lbl{thm.near2} {\rm (Proof in Section \ref{sec.cyclotomic})}
For every knot $K$ there exist a neighborhood $V_K$
of $1 \in \BC$ such that when  $\a/(2 \pi i) \in V_K$ is rational
and not equal to $1$, then
$$
\liminf_{n\to\infty} \frac{|f_{K,n}(\a)|}{n} =0.
$$
\end{theorem}
