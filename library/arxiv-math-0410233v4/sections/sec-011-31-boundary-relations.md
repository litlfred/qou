---
doc_id: arxiv-math-0410233v4
doc_title: "CUSP SHAPES UNDER CONE DEFORMATION"
section_id: sec-011-31-boundary-relations
section_title: "Boundary relations"
section_number: 3.1
pages: 11-12
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.971
doc_brief: "CUSP SHAPES UNDER CONE DEFORMATION — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp shape."
---
Restrict to the case when we have a single cusp.

We will let $U$ be a horoball neighborhood of the one cusp, and $V_1$, ..., $V_n$ be tubular neighborhoods of the components of the singular locus $\Sigma$, each with radius $R$. Here, we are letting $n$ be the total number of components of $\Sigma$. We will assume throughout that these neighborhoods are chosen such that all intersections of distinct neighborhoods are trivial.

Let $\omega \in H^1(X;E)$ correspond to a harmonic infinitesimal deformation of hyperbolic structure at time $t$, and decompose $\omega$ in tubular neighborhoods and horoball neighborhoods as in the previous section, and consider boundary terms.

By equation ([\[eqn:sum\>0\]](#eqn:sum>0){reference-type="ref" reference="eqn:sum>0"}), we see immediately that $$-b_U(\eta_0, \eta_0) \leq \sum_{j=1}^n b_j.
\label{eqn:eta-bound}$$ Again, note that $\eta_0$ in the term $b_U(\eta_0,\eta_0)$ refers to the decomposition of $\eta$ valid only in the horoball neighborhood $U$.

Also, recall that the terms of equation ([\[eqn:eta-bound\]](#eqn:eta-bound){reference-type="ref" reference="eqn:eta-bound"}) all depend on time $t$, but we are suppressing $t$ for notational purposes.

Now, we will analyze the left hand side of ([\[eqn:eta-bound\]](#eqn:eta-bound){reference-type="ref" reference="eqn:eta-bound"}). Recall that in a horoball neighborhood of a cusp, $\omega_0$ can be written as a complex multiple of the form $\omega_\ell =
\omega_\ell(\infty)$ in equation ([\[eqn:omega_l-cusp\]](#eqn:omega_l-cusp){reference-type="ref" reference="eqn:omega_l-cusp"}). That is, there are real numbers $a$ and $b$

(for fixed $t$)

such that $$\omega_0 = (a+ib)\left[
  \begin{array}{ccc}
    0&0&0\\
    0&-1&-i\\
    0&-i&1
  \end{array}\right]
\label{eqn:eta_0-matrix}$$

::: lemma
Using the notation above, $$-b_U(\eta_0, \eta_0) = 2(a^2+b^2)\mbox{Area}(\partial U).$$ []{#lemma:b_U=area label="lemma:b_U=area"}
:::

::: proof
*Proof.* By equation ([\[eqn:eta_0-matrix\]](#eqn:eta_0-matrix){reference-type="ref" reference="eqn:eta_0-matrix"}), we may write $\eta_0 =
  \mbox{Re}(\omega_0)$ and $*D\eta_0 = \mbox{Im}(\omega_0)$ as: $$\eta_0 = \left[\begin{array}{ccc}
      0&0&0\\
      0&-a&b\\
      0&b&a\end{array}\right] =
  \left[\begin{array}{c}0\\-a\\b\end{array}\right] \omega_2 +
  \left[\begin{array}{c}0\\b\\a\end{array}\right] \omega_3
\label{eqn:eta0mat}$$ and: $$*D\eta_0 = \left[\begin{array}{ccc}
      0&0&0\\
      0&-b&-a\\
      0&-a&b\end{array}\right] =
  \left[\begin{array}{c}0\\-b\\a\end{array}\right] \omega_2 +
  \left[\begin{array}{c}0\\-a\\b\end{array}\right] \omega_3.$$ Here $\omega_1$, $\omega_2$, and $\omega_3$ are forms dual to the vectors $e_1$, $e_2$, and $e_3$ giving cylindrical coordinates on $U$. Recall in particular that $e_1$ is radial, and $e_2$ is tangent to a meridian.

We then may compute $-b_U(\eta_0, \eta_0)$ explicitly in terms of the constants $a$ and $b$. $$-b_U(\eta_0, \eta_0) = \int_{\partial U} \eta_0\wedge *D\eta_0 =
\int_{\partial U} 2(a^2+b^2)\omega_2\wedge\omega_3.$$

Since $\omega_2\wedge\omega_3$ is the area form for the torus $\partial U$, we have: $$-b_U(\eta_0, \eta_0) = 2 (a^2+b^2)\mbox{Area}(\partial U).$$ ◻
:::

Notice that equation ([\[eqn:eta-bound\]](#eqn:eta-bound){reference-type="ref" reference="eqn:eta-bound"}) and Lemma [\[lemma:b_U=area\]](#lemma:b_U=area){reference-type="ref" reference="lemma:b_U=area"} imply: $$0 \leq \sum_j b_j,
\label{eqn:b_j>0}$$ and that we have equality by equation ([\[eqn:sumbj=eta\]](#eqn:sumbj=eta){reference-type="ref" reference="eqn:sumbj=eta"}) if and only if $\eta$ is trivial on $X-V$, which happens only when the deformation is trivial.
