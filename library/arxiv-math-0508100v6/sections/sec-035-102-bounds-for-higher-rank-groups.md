---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-035-102-bounds-for-higher-rank-groups
section_title: "Bounds for higher rank groups"
section_number: 10.2
pages: 24-24
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
toc_source: outline
text_source: latex
latex_prose_ratio: 0.931
latex_coverage_ratio: 1.0
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent polynomials, whose nth term is the nth colored Jones polynomial."
---
\lbl{sub.high}

In \cite{GL}, we considered the colored Jones function
$$
J_{\fg,K}: \La_w \longto \BZ[q^{\pm 1}]
$$
of a knot $K$, where $\fg$ is a {\em simple Lie algebra} with {\em
weight lattice}
$\La_w$. In the above reference, the authors proved that $J_{\fg,K}$
is a $q$-holonomic function, at least when $\fg$ is not $G_2$.
For $\fg=\mathfrak{sl}_2$, $J_{\mathfrak{sl}_2,K}$ is the colored Jones
function $J_K$ discussed earlier.

In \cite{GL} , the authors gave  state-sum formulas for $J_{\fg,K}$
similar to \eqref{eq.statesum} where the summand takes values in
$\BZ[q^{\pm 1/D}]$, where $D$ is the size of the center of $\fg$.


The methods of the present paper give an upper bound for
the growth-rate of the $\fg$-colored Jones function. More precisely,
we have:

\begin{theorem}
\lbl{thm.gJones}
For every simple Lie algebra $\fg$ (other than $G_2$)  and every
$\a \in \BC$, and every $\l \in \La_w$, there exists a
constant $C_{\fg,\a,\l}$ such that for every knot with $c+2$ crossings,
we have:
$$
\limsup_{n \to \infty} \frac{\log|J_{\fg,K,n\l}(e^{\a/n})|}{n} \leq
C_{\fg,\a,\l} c .
$$
\end{theorem}

The details of the above theorem will be explained in a subsequent
publication.
