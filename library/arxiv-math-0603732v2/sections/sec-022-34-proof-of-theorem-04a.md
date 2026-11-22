---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-022-34-proof-of-theorem-04a
section_title: "Proof of Theorem 0.4(a)"
section_number: 3.4
pages: 12-13
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.838
latex_coverage_ratio: 0.917
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — We show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼ = νA1[d]."
---
[]{#xxsec3.4 label="xxsec3.4"}

In this subsection we assume that $S$ is bijective. Recall from (2.5.1) that ${\xi}=\Xi[\pi_0],$ the left winding automorphism obtained from $\pi_0: A\to A/(\text{r.ann}(\int^l))$.

::: theorem
Let $A$ be a noetherian AS-regular Hopf algebra of global dimension $d$.

1.  Let $\sigma$ be an algebra automorphism of $A$. Then $H_d(A,{^\sigma A})\cong Z({^{S^2{\xi}\; \sigma} A})$. Consequently, $H_d(A,{^\sigma A})\neq 0$ if and only if $S^2{\xi}\; \sigma \in N(A)$.

2.  $H_d(A,{^{{\xi}^{-1}S^{-2}}A})\cong Z(A)\neq 0$. Consequently, $\mathop{\mathrm{tHdim}}A=d$.

3.  $\mathop{\mathrm{Hdim}}A=d$ if and only if $S^2{\xi}\in N(A)$.
:::

::: proof
*Proof.* (a) By Corollary [\[xxsec3.3\]](#xxsec3.3){reference-type="ref" reference="xxsec3.3"} $$H_d(A,{^{\sigma}A}) \; \cong \;
\mathop{\mathrm{Hom}}_{A^{\sf op}}(\textstyle \int^l,({^\sigma A})')\; =\;
\mathop{\mathrm{Hom}}_{A^{\sf op}}(\textstyle \int^l,(A^{\sigma^{-1}})').$$ By Lemmas [\[xxsec2.6\]](#xxsec2.6){reference-type="ref" reference="xxsec2.6"}(d) and [\[xxsec2.3\]](#xxsec2.3){reference-type="ref" reference="xxsec2.3"}(b), $$\mathop{\mathrm{Hom}}_{A^{\sf op}}(\textstyle \int^l,(A^{\sigma^{-1}})')\;\cong \;
Z(A^{S^{-2}\sigma^{-1}{\xi}^{-1}})\;\cong \;
Z(A^{\sigma^{-1}\;{\xi}^{-1}S^{-2}})\;\cong \;
Z({^{S^2{\xi}\; \sigma}A}).$$ The second assertion follows from the definition $N(A)$

(b,c) Let $M$ be an $A$-bimodule. By Proposition [\[xxsec3.3\]](#xxsec3.3){reference-type="ref" reference="xxsec3.3"}, $H_i(A,M)= \mathop{\mathrm{Tor}}^A_i(M',k)=0$ for all integers $i>d$. Hence $\mathop{\mathrm{Hdim}}
A\leq d$ and $\mathop{\mathrm{tHdim}}A\leq d$. Therefore the assertions follow from (a). ◻
:::
