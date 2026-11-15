---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-028-441-cohomolgy-at-the-character-of-the-holonomy
section_title: "Cohomolgy at the character of the holonomy"
section_number: 4.4.1
pages: 32-33
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 0.926
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
In order to evaluate the torsion functions at the lift of the holonomy, some results on the cohomology for this representation are required. Again the proofs are postponed to Appendix [\[sec:cohomology\]](#sec:cohomology){reference-type="ref" reference="sec:cohomology"}.

::: thm
[]{#prop:dimatvarrho label="prop:dimatvarrho"} Let $\varrho\colon\pi_1 M^3\to\mathrm{SL}_2(\mathbb{C})$ be a lift of the holonomy.

(a) If $k_1+k_2$ is odd, then $\varrho^{k_1,k_2}$ is acyclic.

(b) If $k_1+k_2$ is even, $k_1\neq k_2$, then $$\dim H_i(M^3;    \varrho^{k_1,k_2})= \begin{cases}
                                        1 & \textrm{if } i=1,2\, ,\\
                                        0 & \textrm{otherwise.}
                                       \end{cases}$$
:::

Notice that when both $k_1$ and $k_2$ are odd, the homology of $\varrho^{k_1,k_2}$ differs from the generic homology of $\operatorname{Sym}^{k_1,k_2}$ on $X_0(M^3)$, there is a discontinuity in the dimension of the cohomology, which is generically trivial.

We also need to discuss the basis. Let $i\colon T^2\to M^3$ denote the inclusion.

::: prop
[]{#prop:basis complete label="prop:basis complete"} Let $\varrho\colon\pi_1 M^3\to\mathrm{SL}_2(\mathbb{C})$ be a lift of the holonomy. Assume that $k_1+k_2$ is even.

(a) $\dim  H^0(T^2;\varrho)=1$.

(b) For $0\neq a\in H^0(T^2;\varrho)$, $\langle i_*(a\cap [T^2]) \rangle = H_2(M^3;    \varrho^{k_1,k_2})$.

(c) For $0\neq a\in H^0(T^2;\varrho)$ and $0\neq\gamma\in H_1(T_2;\mathbb{Z})$:

    (i) $\langle i_*(a\cap \gamma) \rangle = H_1(M^3;    \varrho^{k_1,k_2})$ if $k_1=0$ or $k_2=0$; in addition $$\label{eqn:cuspsh}
             i_*(a\cap \gamma_1)=\operatorname{cs}(\gamma_1,\gamma_2) \, i_*(a\cap \gamma_2)$$ where $\operatorname{cs}(\gamma_1,\gamma_2)$ is the cusp shape (Definition [\[def:cs\]](#def:cs){reference-type="ref" reference="def:cs"}).

    (ii) $i_*(a\cap \gamma ) = 0$ if $k_1\neq 0$ and $k_2\neq 0$.
:::
