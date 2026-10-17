---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-014-51-the-real-stability-criterion-revisited
section_title: "The real stability criterion revisited."
section_number: 5.1
pages: 14-15
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.971
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
\begin{prop}
Let $\kappa\in\NN^{m}$ and $f\in\CC[x]^{\leq\kappa}$.  Then
$\Pol_\kappa f$ is stable if and only if $f$ is stable.
\end{prop}
\begin{proof}
Diagonalization implies that if $\Pol_\kappa f$ is stable then $f$
is stable, so only the converse implication needs proof.  Assume that
$f$ is stable, and let $z_{ij}\in\HH$ for $(i,j)\in I(\kappa)$.
By induction on $m$, repeated application of GWS 
shows that there are $\z=(z_{1},\ldots,z_{m})\in\HH^m$ such that
$$
\Pol_{\kappa} f(z_{ij}:\ (i,j)\in I(\kappa)) = f(\z).
$$
Since $f$ is stable it follows that $\Pol_{\kappa} f$ is stable.
\end{proof}

If $f\in\RR[\x]^{\leq\kappa}$ then Theorem 3.1 applies to $\Pol_\kappa f$.
Thus, Proposition 5.1 bootstraps the real stability criterion from
multiaffine to arbitrary polynomials.  This is a typical application of
the GWS Theorem.
