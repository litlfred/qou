---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-054-94-some-applications-of-lifting
section_title: "Some applications of lifting"
section_number: 9.4
pages: 47-47
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 1.0
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
::: corollary
[]{#fpnonzero label="fpnonzero"} Let ${\mathcal C}$ be a nondegenerate fusion category over $k$. Then its Frobenius-Perron dimension $\Delta$ is not divisible by $p$.
:::

::: remark
We do not know if the converse statement is true. For Hopf algebras the converse statement is the well known conjecture that if $H$ is a semisimple Hopf algebra whose dimension is not divisible by $p$ then $H$ is cosemisimple.
:::

::: proof
*Proof.* Assume that $\Delta$ is divisible by $p$. Let $\tilde{\mathcal C}$ be the lifting of ${\mathcal C}$, and $\hat
{\mathcal C}=\tilde{\mathcal C}\otimes_{W(k)}K$, where $K$ is the algebraic closure of the field of fractions of $W(k)$. Then by Theorem [\[divi\]](#divi){reference-type="ref" reference="divi"}, the global dimension $D$ of $\hat{\mathcal C}$ is divisible by $\Delta$, hence by $p$. So the global dimension of ${\mathcal C}$ is zero. Contradiction. ◻
:::

::: corollary
[]{#fpsubcat label="fpsubcat"} Let ${\mathcal D}$ be a nondegenerate fusion category over $k$, and ${\mathcal C}$ be a full subcategory of ${\mathcal D}$ of integer Frobenius-Perron dimension $N$. Then ${\mathcal C}$ is nondegenerate.
:::

::: remark
We do not know if this result is valid without assuming that $N$ is an integer.
:::

::: proof
*Proof.* Consider the lifting $\tilde {\mathcal D}$ of ${\mathcal D}$. This lifting necessarily contains a lifting $\tilde{\mathcal C}$ of ${\mathcal C}$. Consider the corresponding categories $\hat{\mathcal C}$, $\hat{\mathcal D}$ over the algebraically closed field $K$ of zero characteristic. Let $D$ be the global dimension of $\hat{\mathcal D}$, $\Delta$ its Frobenius-Perron dimension. Then $D$ is divisible by $\Delta$ by Proposition [\[divi\]](#divi){reference-type="ref" reference="divi"}. Also, the Frobenius-Perron dimension of $\hat{\mathcal C}$ is $N$ (an integer), hence it is equal to the global dimension of $\hat{\mathcal C}$ by Proposition [\[intFP\]](#intFP){reference-type="ref" reference="intFP"}. But by Theorem [\[subdivi\]](#subdivi){reference-type="ref" reference="subdivi"}, $N$ divides $\Delta$, and hence $D$. But $D$ is not divisible by $p$, hence $N$ is not divisible by $p$. Thus, ${\mathcal C}$ is nondegenerate, as desired. ◻
:::
