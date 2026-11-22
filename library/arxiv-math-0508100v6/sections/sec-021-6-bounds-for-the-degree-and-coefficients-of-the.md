---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-021-6-bounds-for-the-degree-and-coefficients-of-the
section_title: "Bounds for the degree and coefficients of the colored Jones function"
section_number: 6
pages: 14-14
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
toc_source: outline
text_source: latex
latex_prose_ratio: 0.936
latex_coverage_ratio: 0.973
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent polynomials, whose nth term is the nth colored Jones polynomial."
---
\lbl{sec.boundsJones}


\subsection{Bounds for the degree}
\lbl{sub.bdegree}

In this section we give a bound for the coefficients of the colored
Jones polynomial, and deduce Theorem \ref{thm.up}. This and the
next section are logically independent from the previous Sections
\ref{sec.estimates} and \ref{sec.allorders}.

For a Laurent polynomial $f(q)=\sum_{k=m}^M a_k q^k$, with $a_m a_M
\neq 0$, let us define $\maxdeg(f)=M$ and $\mindeg(f)=m$. In
\cite{Le} the second author showed that there are quadratic bounds for the
 degrees  of the colored Jones polynomial.

Suppose the knot $K$ has a planar projection
with $c+2$ crossings. Let $\w$ be the writhe number, i.e. the number
of positive crossing minus the number of negative ones.



Then by  \cite[Proposition 2.1]{Le}, taking
into account the change of variable, the framing, and the
normalization, one has the following bounds for the degrees of
$J_{K,n}(q)$.

\begin{proposition}
\lbl{21}
With the above notations, there are constants $s_\pm$ such that
$$
\begin{aligned} \maxdeg(J_{K,n})  & \le \frac{(c+2)(n-1)^2 +
2(n-1)(s_+-1) -\w(n^2-1)}{4}  \\
 \mindeg(J_{K,n}) &\ge -\frac{(c+2)(n-1)^2 + 2(n-1)(s_--1) +\w(n^2-1)}{4}.
\end{aligned}
$$
\end{proposition}
The constants $s_\pm$ have transparent geometric meaning, but we don't need
their exact values here.

Another proof of the quadratic bounds, though less as explicit,  for the
degrees of the colored Jones polynomial using the theory of $q$-holomorphic
functions is given in Section \ref{sub.qholo}.
