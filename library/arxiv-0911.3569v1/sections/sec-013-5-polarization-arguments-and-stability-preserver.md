---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-013-5-polarization-arguments-and-stability-preserver
section_title: "Polarization arguments and stability preservers."
section_number: 5
pages: 14-14
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.8
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
For $\kappa\in\NN^m$ and a set $\S\subseteq\CC[\x]$ of polynomials,
let $\S^{\leq\kappa}$ be the set of all $f\in\S$ such that $\deg_i(f)\leq
\kappa(i)$ for all $i\in[m]$.  Let
$$
I(\kappa) = \{(i,j):\ i\in[m]\ \mathrm{and}\ j\in[\kappa(i)]\}
$$
and let $\u=\{u_{ij}:\ (i,j)\in I(\kappa)\}$ be indeterminates.
For $f\in\CC[\x]^{\leq\kappa}$, Let $\Pol_{\kappa(i)}^{(i)} f$ denote
the \emph{$\kappa(i)$-th polarization of $x_i$ in $f$}:\ this is the image
of $f$ under the linear transformation $\Pol_{\kappa(i)}^{(i)}$ defined by
$x_i^j \mapsto \binom{\kappa(i)}{j}^{-1} e_j(u_{i1},...,u_{i\kappa(i)})$
for each $0\leq j \leq\kappa(i)$, and linear extension.  Finally, the 
\emph{$\kappa$-th polarization of $f$} is
$$
\Pol_\kappa f = \Pol_{\kappa(m)}^{(m)} \circ\cdots\circ\Pol_{\kappa(1)}^{(1)} f.
$$
This defines a linear transformation $\Pol_{\kappa}:\CC[\x]^{\leq\kappa}
\goesto\CC[\u]^{\ma}$.
