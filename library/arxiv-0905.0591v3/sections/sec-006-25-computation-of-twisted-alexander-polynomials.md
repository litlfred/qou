---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-006-25-computation-of-twisted-alexander-polynomials
section_title: "Computation of twisted Alexander polynomials"
section_number: 2.5
pages: 7-7
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.98
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
\label{section:compdelta}

Let $N$ be a 3--manifold with empty or toroidal boundary, and  ${\alpha}:\pi_1(N)\to \mbox{GL}(k,R[F])$  a  representation with $R$ a Noetherian UFD
and $F$ a free abelian group.
Given a finite presentation for $\pi_1(N)$ the polynomials $\Delta_{N,1}^{\alpha}\in R[F]$ and $\Delta_{N,0}^{\alpha}\in R[F]$ can be computed
efficiently using Fox calculus (cf. e.g. \cite[p.~98]{CF77} and \cite{KL99a}). We point out that
because we view $C_*(\tilde{N})$ as a \emph{right} module over $\mathbb{Z}[\pi_1(N)]$ we need a slightly
different definition of Fox derivatives than the one commonly used. We refer to \cite[Section~6]{Ha05} for details.
Finally, Proposition \ref{prop:dualitydelta}  allows us to compute $\Delta_{N,2}^{\alpha}\in R[F]$ using the algorithm for
computing the zeroth twisted Alexander polynomial.
In particular  all the  twisted Alexander polynomials $\Delta^{{\alpha}}_{N,i}$ can be computed from a finite presentation
of the fundamental group.
