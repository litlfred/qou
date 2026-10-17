---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-029-510-deformations-of-weak-hopf-algebras
section_title: "Deformations of weak Hopf algebras"
section_number: 5.10
pages: 22-22
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 1.0
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
It is well known that a non-semisimple finite dimensional algebra can be perturbed into a semisimple one. However, for (connected) weak Hopf algebras the situation is different. Namely, we have the following result.

::: proposition
Let $H_t$ be a continuous family of finite dimensional regular connected weak Hopf algebras over $\Bbb C$ depending of a real parameter $t\in (a,b)$ (i.e., $H_t$ is independent of $t$ as a vectors space, and the structure maps continuously depend on $t$). Then either $H_t$ is semisimple for all $t$ or $H_t$ is non-semisimple for all $t$.
:::

::: proof
*Proof.* The set $U\subset (a,b)$ where $H_t$ is semisimple is open. Assume that this set is nonempty. The function $f(t)=\text{Tr}(S^2|_{H_t})$ is a continuous function of $t$. By Corollary [\[Tr S2 connected\]](#Tr S2 connected){reference-type="ref" reference="Tr S2 connected"}, $f$ is zero on the complement $U^c$ of $U$. Also, by Theorem [\[posi\]](#posi){reference-type="ref" reference="posi"} and Remark [\[tra\]](#tra){reference-type="ref" reference="tra"}, $f$ is a nonzero algebraic integer for any $t\in U$. Since $f$ is continuous, this implies that $f$ is constant (and nonzero) on each connected component of $U$. Thus, $U^c$ is empty. We are done. ◻
:::
