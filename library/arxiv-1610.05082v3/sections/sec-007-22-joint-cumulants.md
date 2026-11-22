---
doc_id: arxiv-1610.05082v3
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-007-22-joint-cumulants
section_title: "Joint cumulants"
section_number: 2.2
pages: 6-6
source_pdf: 1610.05082v3.pdf
source_sha256: 90c8089953ff2d97
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.984
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
[]{#sec:cumulants label="sec:cumulants"} As usual in the physics literature (and as done in the introduction), we use the notation $\langle f \rangle$ for the expectation of $f(X)$ (adding parameters of the measure as indices if necessary). For random variables $X_1,\dots,X_r$ on the same probability space with finite moments, we define their *joint cumulant* (or *mixed cumulant*) as $$\kappa (X_1,\dots,X_r) = [t_1 \dots t_r] \log 
\big\langle \exp(t_1 X_1 + \dots + t_r X_r) \big\rangle.
    \label{EqDefCumulant}$$ The notation $[t_1 \dots t_r] F$ stands here for the coefficient of $t_1 \dots t_r$ in the series expansion of $F$ in positive powers of $t_1, \dots, t_r$. The finite moments assumption ensures that this series expansion exists. If all random variables $X_1,\cdots,X_r$ are equal to the same variable $X$, we denote $\kappa_r(X)=\kappa(X,\dots,X)$ and this is the usual *cumulant* of a single random variable.

Joint cumulants have a long history in statistics and theoretical physics, see *e.g.* [@UrsellCumulants]. In the case where the $X_i$'s are indicator functions of the presence of particles (or $+$ spins for examples), they are often referred to in the statistical physics literature as *truncated correlation functions* or *Ursell functions*.
