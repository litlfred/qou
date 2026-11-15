---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-018-26-the-right-adjoint-action
section_title: "The right adjoint action"
section_number: 2.6
pages: 9-10
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.852
latex_coverage_ratio: 0.949
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — We show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼ = νA1[d]."
---
[]{#xxsec2.6 label="xxsec2.6"}

Let $M$ be an $A$-bimodule. The *right adjoint* $A$-module $R(M)$ [@Mo Definition 3.4.1(2)], which we shall often denote by $M'$ (see also [@FT; @HK1]), is $M$ as a $k$-vector space, with right $A$-action given by $$m \cdot a\; =\; \sum S(a_2)ma_1$$ for all $a\in A$ and $m\in M$. Below we shall want to combine twisting with the right adjoint action, producing right modules of the form $(^\sigma A^\tau)'$ which will be crucial in our calculation of Hochschild homology. Parallel results to those stated in ([\[xxsec2.2\]](#xxsec2.2){reference-type="ref" reference="xxsec2.2"}), ([\[xxsec2.3\]](#xxsec2.3){reference-type="ref" reference="xxsec2.3"}) and ([\[xxsec2.4\]](#xxsec2.4){reference-type="ref" reference="xxsec2.4"}) can be derived for $R(-).$ We shall omit most of the statements. The following lemma will be used later. For $\pi \in G(A^\circ)$, we write $k_{\pi}$ for the corresponding right $A$-module $A/\ker \pi$.

::: lemma
Let $A$ be a Hopf algebra, let $\pi, \phi \in G(A^\circ)$ and let $\sigma \in \mathop{\mathrm{Aut}}_{k\text{-}\mathrm{alg}}(A)$. Let $M$ be an $A$-bimodule. From (b) to (e) we assume $S$ is bijective. In (d) and (e) we assume that the left integral of $A$ exists. In (b) to (e) we identify the spaces of homomorphisms with vector subspaces of $M$ or $A$ as appropriate.

1.  $k_{\pi}^\sigma \cong k_{\pi\sigma}$.

2.  $\mathop{\mathrm{Hom}}_{A^{\sf
    op}}(k,(^{S^{-2}}M^\sigma)')\; =\; Z^{\sigma}_A(M)$.

3.  $\mathop{\mathrm{Hom}}_{A^{\sf op}}(k_{\phi \ast \pi}, (M^{\Xi[\phi]})') \; = \;
    \mathop{\mathrm{Hom}}_{A^{\sf op}}(k_{\pi},(M)')$. As a consequence, $$\mathop{\mathrm{Hom}}_{A^{\sf op}}(k_{\phi \ast \pi}, (^{S^{-2}}A^{\sigma\Xi[\phi]})')
    \; = \; \mathop{\mathrm{Hom}}_{A^{\sf op}}(k_{\pi},(^{S^{-2}}A^{\sigma})').$$

4.  $\mathop{\mathrm{Hom}}_{A^{\sf op}}(\textstyle \int^l,(^{S^{-2}}A^\sigma)') \; = \;
    Z(A^{\sigma {\xi}^{-1}})$. That is, $$\mathop{\mathrm{Hom}}_{A^{\sf op}}(\textstyle \int^l,(A^\sigma)') \;= \;
    Z(A^{S^{-2}\sigma \; {\xi}^{-1}})
    \; \cong \; Z(A^{S^{-2}{\xi}^{-1}\sigma}).$$

5.  $\mathop{\mathrm{Hom}}_{A^{\sf op}}(\textstyle \int^l, (^{S^{-2}}A^{{\xi}} )') \; = \;
    Z(A) \; = \; \mathop{\mathrm{Hom}}_{A^{\sf op}} (\textstyle \int^l,(^{{\xi}^{-1} S^{-2}}A )')$.
:::

::: proof
*Proof.* (a) follows from the definitions.

\(b\) By Lemma [\[xxsec2.3\]](#xxsec2.3){reference-type="ref" reference="xxsec2.3"}(a) we may assume $\sigma=\operatorname{id}_A$. The right $A$-action on $(^{S^{-2}}M)'$ is then given by $$m \cdot a = \sum S^{-1}(a_2)ma_1$$ for all $m \in M$ and $a \in A$, and so we need to prove that $$\mathop{\mathrm{Hom}}_{A^{\sf op}}(k,(^{S^{-2}}M)')=Z(M).$$ The proof of Lemma [\[xxsec2.4\]](#xxsec2.4){reference-type="ref" reference="xxsec2.4"}(a) can be modified and we leave the details to the reader.

\(c\) We may, in a similar way to the proof of (b), identify both the spaces of maps in question with subspaces of the $k$-vector space $M$. The rest of the proof is straightforward.

The second assertion follows by taking $M={^{S^{-2}}A^\sigma}$.

\(d\) As a right module, $\textstyle \int^l$ is by definition isomorphic to $k_{\pi_0}.$ So from (c) with $\pi=\pi_0$ and $\phi=\pi_0^{-1}$, together with (b) with $A$ for $M$, we see that $$\mathop{\mathrm{Hom}}_{A^{\sf op}}(\textstyle \int^l,(^{S^{-2}}A^\sigma)') \quad = \quad
Z^{\sigma}_A(A).$$ The first isomorphism in (d) now follows from Lemma [\[xxsec2.3\]](#xxsec2.3){reference-type="ref" reference="xxsec2.3"}(a). The second isomorphism in (d) follows from the first after we observe that $(A^{\sigma})' \cong
(^{S^{-2}}A^{S^{-2}\sigma})'$, which is clear from ([\[xxsec2.3\]](#xxsec2.3){reference-type="ref" reference="xxsec2.3"}.1).

\(e\) In view of ([\[xxsec2.3\]](#xxsec2.3){reference-type="ref" reference="xxsec2.3"}.2), this is a special case of (d). ◻
:::
