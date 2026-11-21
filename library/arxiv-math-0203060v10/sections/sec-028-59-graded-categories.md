---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-028-59-graded-categories
section_title: "Graded categories"
section_number: 5.9
pages: 22-22
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
Let $G$ be a finite group.

::: definition
A $G$-grading on a tensor category ${\mathcal C}$ is a decomposition ${\mathcal C}=\oplus_{g\in G}{\mathcal C}_g$, such that $\otimes: {\mathcal C}_g\times {\mathcal C}_h\to {\mathcal C}_{gh}$, $\mathbf 1\in {\mathcal C}_e$, and $*:{\mathcal C}_g\to
{\mathcal C}_{g^{-1}}$. We will say that the grading is faithful if ${\mathcal C}_g\ne 0$ for any $g\in G$.
:::

It is clear that if ${\mathcal C}$ is a $G$-graded category, then ${\mathcal C}_e$ is a tensor category, and ${\mathcal C}_g$ are left and right module categories over ${\mathcal C}_e$.

Let ${\mathcal C}$ be a fusion category, $G$ a finite abelian group.

::: proposition
[]{#gradi label="gradi"} Suppose that $Z({\mathcal C})$ contains, as a full tensor subcategory, the category of modules $\tilde G$ over $\mathcal O(G)$, and that all simple objects of this subcategory map to the neutral object of ${\mathcal C}$ under the functor $Z({\mathcal C})\to {\mathcal C}$. Then ${\mathcal C}$ admits a faithful $G^\vee$-grading (where $G^\vee$ is the dual group to $G$).
:::

::: proof
*Proof.* Let $g\in \tilde G$ be a simple object. Since $g$ is trivial as an object of ${\mathcal C}$, it defines a tensor automorphism of the identity functor of ${\mathcal C}$. Thus we have a homomorphism $G\to {\rm Aut}_{\otimes}(Id)$, and hence any simple object of ${\mathcal C}$ defines an element of the dual group $G^\vee$. This is obviously a faithful grading. ◻
:::
