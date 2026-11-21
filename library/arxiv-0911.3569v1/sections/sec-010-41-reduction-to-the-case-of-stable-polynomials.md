---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-010-41-reduction-to-the-case-of-stable-polynomials
section_title: "Reduction to the case of stable polynomials."
section_number: 4.1
pages: 11-13
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.859
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
First of all, it suffices to prove GWS for open circular regions, since a closed
circular region is the intersection of all the open circular regions which
contain it.  Second, it suffices to show that for any $g\in\CC[x]$ of degree
at most $m$, if $\deg(g)=m$ or $\A$ is convex, and $\z\in\A^m$ is such that
$\Pol_m g(\z)= 0$, then there exists $z\in\A$ such that $g(z)=0$.
This implies the stated form of GWS by applying this special case to
$g(x)=f(x)-c$, where $c=\Pol_m f(\z)$.  Stated otherwise, it suffices to show
that if $f(z)\neq 0$ for all $z\in\A$ then $\Pol_m f(\z)\neq 0$ for
all $\z\in\A^m$ (provided that either $\deg(f)=m$ or $\A$ is convex).

Let $\MM$ be the set of M\"obius transformations
$z\mapsto\phi(z)=(az+b)/(cz+d)$ with $a,b,c,d\in\CC$ and $ab-cd=\pm 1$.
Then $\MM$ with the operation of functional composition is a group of
conformal transformations of the Riemann sphere $\widehat{\CC}=
\CC\cup\{\infty\}$, and it acts simply transitively on the set of all ordered
triples of distinct points of $\widehat{\CC}$. 
Consequently, for any open circular region $\A$ there is a
$\phi\in\MM$ such that $\phi(\HH)=\{\phi(z):\ z\in\HH\}=\A$.
We henceforth regard circular regions as subsets of $\widehat{\CC}$.
Note that an open circular region $\A$ is convex if and only if
it does not contain $\infty$.  (The point $\infty$ is on the boundary
of any open half-plane.)  In this case,
if $\phi(z)=(az+b)/(cz+d)$ is such that $\phi(\HH)=\A$ then $cz+d\neq 0$
for all $z\in\HH$.

Given $0\not\equiv f\in\CC[x]$ of degree at most $m$, consider the
polynomial $\widetilde{f}(x)=(cx+d)^m f((ax+b)/(cx+d))$.
If either $\deg(f)=m$ or $\A$ is convex, then $f$ is nonvanishing on $\A$
if and only if $\widetilde{f}(z)$ is nonvanishing on $\HH$.
Also,
$$
\Pol_m \widetilde{f}(\x) = 
\Pol_m f (\phi(x_1),...,\phi(x_m)) \cdot \prod_{i=1}^m(cx_i+d).
$$
Thus, to prove GWS it suffices to prove the following lemma.
\begin{lemma}
Let $f\in\CC[x]$ be a univariate polynomial of degree at most
$m$.  Then $\Pol_m f$ is stable if and only if $f$ is stable.
\end{lemma}
\noindent
Clearly, diagonalization implies that if $\Pol_m f$ is stable then $f$
is stable, so only the converse implication needs proof.  This is
accomplished in the following two easy steps.
