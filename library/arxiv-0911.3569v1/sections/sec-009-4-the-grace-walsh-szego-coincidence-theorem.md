---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-009-4-the-grace-walsh-szego-coincidence-theorem
section_title: "The Grace-Walsh-Szego Coincidence Theorem."
section_number: 4
pages: 11-11
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.972
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
Let $f\in\CC[x]$ be a univariate polynomial of degree at most $m$,
and let $\x=(x_1,...,x_m)$ as usual.  For $0\leq j\leq m$, the
\emph{$j$-th elementary symmetric function} of $\x$ is
$$
e_j(\x) = \sum_{1\leq i_1<\cdots< i_j\leq m} x_{i_1}\cdots x_{i_j}
= \sum_{S\subseteq[m]:\ |S|=j} \x^{S}.
$$
The \emph{$m$-th polarization} of $f$ is the polynomial obtained
as the image of $f$ under the linear transformation $\Pol_m$
defined by $x^j \mapsto \binom{m}{j}^{-1}e_j(\x)$ for all $0\leq j\leq m$,
and linear extension.  In other words, $\Pol_m f$ is the unique
multiaffine polynomial in $\CC[\x]^\ma$ that is invariant under all
permutations of $[m]$ and such that $\Pol_m f(x,...,x) = f(x)$.
A \emph{circular region} is a nonempty subset $\A$ of $\CC$ that is either
open or closed, and which is bounded by either a circle or a straight line.

\begin{theorem}[Grace-Walsh-Szeg\H{o}, Theorem 3.4.1b of \cite{RS}]
Let $f\in\CC[x]$ have degree at most $m$ and let $\A$ be a circular region.
If either $\deg(f)=m$ or $\A$ is convex, then for every $\z\in\A^m$ there
exists $z\in\A$ such that $\Pol_m f(\z)=f(z)$.
\end{theorem}

Figure 1 illustrates the Grace-Walsh-Szeg\H{o} (GWS) Theorem for the polynomial
$f(x)=x^5+10x^2+1$.  The black dots mark the solutions to $f(x)=0$.
Any permutation of the red (grey) dots is a solution to
$\Pol_5 f(x_1,...,x_5)=0$.  By GWS, any circular region containing all the
red dots must contain at least one of the black dots.  The figure indicates
the boundaries of several circular regions for which this condition is met.
\pix{0.8}{ceb_wagner.jpg}{Illustration of the Grace-Walsh-Szeg\H{o} 
Theorem.}

The proof of GWS in this section is adapted from Borcea and 
Br\"and\'en \cite{BB6}.
