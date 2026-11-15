---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-014-33-comparing-the-cyclotomic-and-the-loop-expansi
section_title: "Comparing the cyclotomic and the loop expansion"
section_number: 3.3
pages: 10-10
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
toc_source: outline
text_source: latex
latex_prose_ratio: 0.85
latex_coverage_ratio: 1.0
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent polynomials, whose nth term is the nth colored Jones polynomial."
---
\lbl{sub.comparing}

In the loop expansion, as well as in the
cyclotomic expansion, one should treat $q^n$ and $q$ (where $n$ is
the color) as two independent variables. Consider two
independent variables $z$ (standing for $\a$) and $y$ (standing for
$\a/n$). Let us define the following biholomorphic functions


\begin{eqnarray*}
c_k(z,y) &=&
\prod_{j=1}^{k} (e^z+e^{-z} -e^{jy}-e^{-jy}), \\
h_{K,k}(z,y) &=& c_k(z,y) H_{K,k}(e^{y}).
\end{eqnarray*}

The cyclotomic expansion says that for every $n$ we have:

\begin{equation}
\lbl{11}
f_{K,n}(\a) = \sum_{k=0}^{\infty} h_{K,k}(\a,\a/n) \in \BQ[[\a]].

\end{equation}

The loop expansion is a Taylor expansion in $\a/n$, so we will
consider the Taylor expansion in $y$ (around 0) of $h_{K,k}(z,y)$:

$$
h_{K,k}(z,y) = \sum_{p=0}^\infty d_{k,p}(z) \, y^p,
$$
where $d_{k,p}(z)$ (which depends on $K$) is holomorphic for $z \in \BC$.

Comparing the loop and the cyclotomic expansion (Equations \eqref{eq.R}
and \eqref{11}), we obtain that:

\begin{lemma}
\lbl{lem.compare3}
For every knot $K$ and every $p \in \BN$ we have
\begin{equation} R_{K,p}(x) = \sum_{k=0}^\infty
d_{k,p}(x) \in \BQ[[x]].\label{12}
\end{equation}
as formal power series in $x$.
\end{lemma}



\section{A reduction of Theorem \ref{thm.boundC3}
to estimates of the cyclotomic function}
\lbl{sec.estimates}
