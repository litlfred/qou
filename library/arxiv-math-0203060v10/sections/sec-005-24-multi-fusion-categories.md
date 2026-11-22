---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-005-24-multi-fusion-categories
section_title: "Multi-fusion categories"
section_number: 2.4
pages: 7-7
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.977
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
We say that a multi-fusion category ${\mathcal C}$ is indecomposable if it is not a direct sum of two nonzero multi-fusion categories.

Let ${\mathcal C}$ be a multi-fusion category. Then for any simple object $X\in {\mathcal C}$ there exist unique $i,j\in J$ such that $\mathbf 1_i\otimes X\ne 0$ and $X\otimes \mathbf 1_j\ne 0$; moreover, we have $\mathbf 1_i\otimes X=X\otimes \mathbf 1_j=X$. Thus, as an additive category, ${\mathcal C}=\oplus_{m,n}{\mathcal C}_{mn}$, where ${\mathcal C}_{mn}$ is the full abelian subcategory of ${\mathcal C}$ with simple objects having $i=m,j=n$. It is easy to check that ${\mathcal C}_{ii}$ are fusion categories for all $i$, and ${\mathcal C}_{ij}$ are $({\mathcal C}_{ii},{\mathcal C}_{jj})$-bimodule categories, equipped with product functors ${\mathcal C}_{ij}\times {\mathcal C}_{jl}\to {\mathcal C}_{il}$ satisfying some compatibility conditions. We will refer to ${\mathcal C}_{ii}$ as *the component categories* of ${\mathcal C}$.

Since ${\mathcal C}_{ii}$ are fusion categories, they have well defined global dimensions. In fact, the off-diagonal subcategories ${\mathcal C}_{ij}$ can also be assigned global dimensions, even though they are not tensor categories. To do this, observe that for any simple object $V\in {\mathcal C}_{ij}$, and any morphism $g:V\to V^{**}$ one can define $\text{Tr}_V(g)\in 
\text{End}(\mathbf 1_i)=k$. Therefore, we can define $|V|^2$ by the usual formula $|V|^2=\text{Tr}_V(g)\text{Tr}_{V^*}((g^{-1})^*)$, and set $\dim({\mathcal C}_{ij}):=
\sum_{V\in {\rm Irr}{\mathcal C}_{ij}}|V|^2$.

::: proposition
[]{#samedim label="samedim"} If ${\mathcal C}$ is an indecomposable multi-fusion category, then all the categories ${\mathcal C}_{ij}$ have the same global dimensions.
:::

The setup of the previous section can be generalized to the multi-fusion case. Namely, we have the following generalization of Theorem [\[m1m2\]](#m1m2){reference-type="ref" reference="m1m2"} to the multi-fusion case:

::: theorem
[]{#multi-fus label="multi-fus"} If ${\mathcal C}$ is a multi-fusion category, and ${\mathcal M}_1,{\mathcal M}_2$ are module categories over ${\mathcal C}$, then the category ${\rm Fun}_{{\mathcal C}}({\mathcal M}_1,{\mathcal M}_2)$ is semisimple. In particular, the category ${\mathcal C}^*_{\mathcal M}$ is semisimple for any module category ${\mathcal M}$.
:::

Proposition [\[samedim\]](#samedim){reference-type="ref" reference="samedim"} and Theorem [\[multi-fus\]](#multi-fus){reference-type="ref" reference="multi-fus"} is proved in Section 5.

::: remark
We note that it follows from the arguments of [@O; @Mu1] that if ${\mathcal C}$ is a multifusion category and ${\mathcal M}$ is a faithful module category of ${\mathcal M}$, then ${\mathcal M}$ is a faithful module category over ${\mathcal C}^*_{\mathcal M}$, and $({\mathcal C}^*_{\mathcal M})^*_{\mathcal M}={\mathcal C}$.
:::
