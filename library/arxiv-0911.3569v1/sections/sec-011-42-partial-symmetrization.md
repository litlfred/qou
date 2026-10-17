---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-011-42-partial-symmetrization
section_title: "Partial symmetrization."
section_number: 4.2
pages: 13-13
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.95
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
The group $\S(m)$ of all permutations $\sigma:[m]\goesto[m]$ acts on $\CC[\x]$
by the rule $\sigma(f)(x_1,...,x_m)=f(x_{\sigma(1)},...,x_{\sigma(m)})$.
Notice that
$$
\sigma(\x^\alpha) = \prod_{i=1}^m x_{\sigma(i)}^{\alpha(i)} =
\prod_{i=1}^m x_i^{\alpha\circ\sigma^{-1}(i)} = \x^{\alpha\circ\sigma^{-1}}.
$$
For $\{i,j\}\subseteq[m]$, let $\tau_{ij}$ be
the transposition that exchanges $i$ and $j$ and fixes all other elements of $[m]$.
\begin{lemma}
Let $0\leq \lambda\leq 1$ and $\{i,j\}\subseteq[m]$, and let
$T_{ij}^{(\lambda)}=(1-\lambda)+\lambda\tau_{ij}$.  If $f\in\Stab[\x]^\ma$ is stable
and multiaffine then $T_{ij}^{(\lambda)} f\in\Stab[\x]^\ma$ is stable and
multiaffine.
\end{lemma}
\begin{proof}
If $f$ is multiaffine then $(1-\lambda)f + \lambda\tau_{ij}(f)$
is also multiaffine.  We apply Theorem 3.4 to show that $T=T_{ij}^{(\lambda)}$
preserves stability of multiaffine polynomials.  By permutation we can assume
that $\{i,j\}=\{1,2\}$. The algebraic symbol of $T$ is
$$
T((\x+\y)^{[m]}) = T((x_1+y_1)(x_2+y_2))\cdot
\prod_{i=3}^m(x_i+y_i).
$$
Clearly, this is stable if and only if the same is true of
$T((x_1+y_1)(x_2+y_2))$.
Exercise 4.4 completes the proof.
\end{proof}
\begin{exercise}
Use the results of Sections 2.4 or 3.1 to show that for
$0\leq \lambda \leq 1$, the polynomial
$$
x_{1}x_{2} + ((1-\lambda)x_{1} + \lambda x_{2})y_{2} +
(\lambda x_{1} + (1-\lambda)x_{2})y_{1} + y_{1}y_{2}
$$
is real stable.
\end{exercise}
