---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-012-31-the-loop-expansion
section_title: "The loop expansion"
section_number: 3.1
pages: 8-9
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.927
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent polynomials, whose nth term is the nth colored Jones polynomial."
---
\lbl{sub.loop}

With $q=e^h$, one has

$$
J_{K,n}(e^h) = \sum_{i=0}^\infty a_{K,i}(n)\,
h^i \in \BQ[[h]].
$$

It turns out that $a_{K,i}(n)$ is a polynomial in $n$ with degree less
than or equal to $i$, see \cite{B-NG}. Hence there are rational numbers
$a_{K,i,j}$, depending on the knot $K$, such that

\begin{eqnarray}
\lbl{eq.pert} J_{K,n}(e^h) &=& \sum_{0 \leq j \leq i} a_{K,i,j}\, n^j
h^i  = \sum_{0 \leq i, 0 \leq j \leq i} a_{K,i,j} (nh)^j h^{i-j}\notag \\
\notag &=& \sum_{0 \leq j, k} a_{K,j+k,j} (nh)^j h^k.
\end{eqnarray}
If we define
$$
R_{K,k}(x)=\sum_{0 \leq j} a_{K,j+k,j} x^j \in \BQ[[x]],
$$
then we have the following {\em loop expansion}
\begin{eqnarray}
\lbl{eq.R}
J_{K,n}(e^h) &=& \sum_{k=0}^\infty R_{K,k}(nh) h^k \in \BQ[[h]]
\end{eqnarray}

It turns out that $R_{K,k}(x) \in \BQ(e^x)$ are rational functions
for all $k$. In fact,
the MMR Conjecture states that
$$
R_{K,0}(x)=\frac{1}{\D_K(e^x)} \in \BQ[[x]].
$$
More generally, Rozansky \cite{Ro1} proves  there are Laurent
polynomials $P_{K,k}(t) \in \BQ[t^{\pm 1}]$ such that in $\BQ[[x]]$,
$$
R_{K,k}(x)=\frac{P_{K,k}(e^x)}{\D_K(e^x)^{2k+1}}.
$$

\begin{remark}
\lbl{rem.aij}
For every $i,j$, the function $K \to a_{K,i,j}$ is a finite type invariant
of degree $i$.
Although the polynomials $P_{K,k}(t)$ are not finite type invariants
(with respect to the usual crossing change of knots), they are
finite type invariants with respect to a loop move described in \cite{GR}.
We will not use these facts in our paper.
\end{remark}
