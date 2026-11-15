---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-047-89-a-question
section_title: "A question"
section_number: 8.9
pages: 40-41
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.628
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
We think that the following question is interesting.

::: question
[]{#quest label="quest"} Does there exist a finite dimensional semisimple Hopf algebra $H$ whose representation category is not group-theoretical?
:::

::: remark
Hopf algebras with group theoretical category of representations can be completely classified in group theoretical terms (see [@O1]). Therefore, a negative answer to Question [\[quest\]](#quest){reference-type="ref" reference="quest"} would provide a full classification of semisimple Hopf algebras.
:::

::: remark
The answer to Question [\[quest\]](#quest){reference-type="ref" reference="quest"} is "no" for triangular Hopf algebras, as follows from [@EG3]. However, if the answer is "yes" in general, then it is "yes" already for quasitriangular Hopf algebras. Indeed, if $\text{Rep}(D(H))$ is group-theoretical then so is $\text{Rep}(H)\otimes \text{Rep}(H^{*cop})$ (as a dual category to $\text{Rep}D(H)$), from which it follows by Proposition [\[subquot\]](#subquot){reference-type="ref" reference="subquot"} that so is $\text{Rep}(H)$.
:::

::: remark
It is interesting that there exists a quasi-Hopf algebra $H$ whose category of representations is not group-theoretical. Namely, recall that in [@TY], there is a classification of fusion categories whose simple objects are elements of a group $G$ and an additional object $X=X^*$, with fusion rules $g\otimes X=X\otimes g=X, X\otimes X=\sum_{g\in G}g$ (and the usual multiplication rule in $G$). The result is that $G$ must be abelian, and for each $G$ the categories are parametrized by pairs $(q,r)$ where $q$ is a nondegenerate symmetric bilinear form on $G$ with coefficients in ${\mathbb{C}}^*$, and $r$ is a choice of $\sqrt{|G|}$. Let us denote such category by $TY(G,q,r)$. It is clear that $TY(G,q,r)$ is a representation category of a quasi-Hopf algebra (i.e. has integer Frobenius-Perron dimensions) iff $|G|$ is a square. So let us take $G=(\mathbb Z/p)^2$, where $p>2$ is a prime, and let $q$ be given by $q((x,y),(x,y))=ax^2-by^2$, where $a,b\in \mathbb F_p$ and $a/b$ is a quadratic non-residue (i.e. the quadratic form $ax^2-by^2$ is elliptic). Then one can check by direct inspection that $TY(G,q,r)$ is not group-theoretical. (We note that $TY(G,q,r)$ is not a representation category of a Hopf algebra; on the other hand, if $q$ is a hyperbolic form, then $TY(G,q,+\sqrt{|G|})$ is a representation category of a Hopf algebra, but is group-theoretical).
:::
