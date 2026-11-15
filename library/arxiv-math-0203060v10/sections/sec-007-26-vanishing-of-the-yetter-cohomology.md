---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-007-26-vanishing-of-the-yetter-cohomology
section_title: "Vanishing of the Yetter cohomology"
section_number: 2.6
pages: 9-9
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.984
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
The cohomology theory that controls deformations of tensor categories and tensor functors is the cohomology theory developed in [@CY; @Y1; @Y2; @Da], which we will call the Yetter cohomology theory. This theory associates to any tensor category ${\mathcal C}$ and a tensor functor $F$ for ${\mathcal C}$ to another tensor category ${\mathcal C}'$, a sequence of cohomology spaces $H^i_F({\mathcal C})$ (See Section 7). If $F$ is the identity functor, then these groups are simply denoted by $H^i({\mathcal C})$. Namely, first order deformations of ${\mathcal C}$ are elements of $H^3({\mathcal C})$, while first order deformations of a tensor structure on a given functor $F$ between fixed tensor categories ${\mathcal C},{\mathcal C}'$ are elements of $H^2_F({\mathcal C})$. Obstructions to such deformations lie, respectively, in $H^4({\mathcal C})$ and $H^3_F({\mathcal C})$.

For multi-fusion categories, the Yetter cohomology often vanishes. Namely, we have the following result.

::: theorem
[]{#van label="van"} Let ${\mathcal C}$, ${\mathcal C}'$ be multi-fusion categories, and $F: {\mathcal C}\to {\mathcal C}'$ be a (unital) tensor functor from ${\mathcal C}$ to ${\mathcal C}'$. Then $H^i_F({\mathcal C})=0$ for $i>0$.
:::

Theorem [\[van\]](#van){reference-type="ref" reference="van"} is proved in Section 7, using weak Hopf algebras. The idea of this proof is due to Ocneanu, Blanchard, and Wassermann.
