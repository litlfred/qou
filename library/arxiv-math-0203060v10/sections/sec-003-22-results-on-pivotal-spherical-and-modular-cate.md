---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-003-22-results-on-pivotal-spherical-and-modular-cate
section_title: "Results on pivotal, spherical, and modular categories"
section_number: 2.2
pages: 5-7
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in pa rtic- ular, the theory of weak Hopf algebras), we prove a number of g eneral results about fusion categories in"
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.962
---
Now let ${\mathcal C}$ be a pivotal fusion category. In such a category, one can define the dimension of an object $V$ by $\dim(V)=\text{Tr}_V(i)$, and we have the following result which justifies the notation $|V|^2$.

::: proposition
[]{#pivo label="pivo"} In a pivotal fusion category one has $|V|^2=\dim(V)\dim(V^*)$ for any simple object $V$. Moreover, if $k={\mathbb{C}}$ then $\dim(V^*)=\overline{\dim(V)}$, so $|V|^2=|\dim(V)|^2$.
:::

Proposition [\[pivo\]](#pivo){reference-type="ref" reference="pivo"} is proved in Section 3.

This result can be further specialized to spherical (in particular, ribbon) categories, (see [@Mu1]). Namely, recall from [@Mu1] that a pivotal fusion category is spherical if and only if $\dim(V)=\dim(V^*)$ for all simple objects $V$. Thus we have the following corollary.

::: corollary
[]{#spheri label="spheri"} In a spherical category, $|V|^2=\dim(V)^2$. In particular, if $k={\mathbb{C}}$, then $\dim(V)$ is (totally) real.
:::

Corollary [\[spheri\]](#spheri){reference-type="ref" reference="spheri"} readily follows from Proposition [\[pivo\]](#pivo){reference-type="ref" reference="pivo"}.

::: remark
We note that in [@Mu1], the number $|V|^2$ is called the squared dimension of $V$, and denoted $d^2(V)$. We do not use this terminology for the following reason. In a pivotal category over ${\mathbb{C}}$, the dimensions of simple objects do not have to be real numbers (it suffices to consider the category of representations of a finite group $G$, where $i$ is given by a nontrivial central element of $G$). Thus, in general $\dim(V^*)\ne \dim(V)$, and $|V|^2\ne \dim(V)^2$. Therefore, the term "squared dimension", while being adequate in the framework of spherical categories of [@Mu1], is no longer adequate in our more general setting.
:::

Now assume that ${\mathcal C}$ is a modular category (i.e., a ribbon fusion category with a nondegenerate $S$-matrix, see [@BaKi]). In this case one can define matrices $S$ and $T$ of algebraic numbers, which yield a projective representation of the modular group $SL_2(\mathbb Z)$ ([@BaKi]). We note that the matrix $S$ is defined only up to a sign, since in the process of defining $S$ it is necessary to extract a square root of the global dimension of ${\mathcal C}$. So to be more precise we should say that by a modular category we mean the underlying ribbon category together with a choice of this sign.

::: proposition
[]{#modu label="modu"} If $k={\mathbb{C}}$ then the projective representation of $SL_2(\mathbb Z)$ associated to ${\mathcal C}$ is unitary in the standard hermitian metric (i.e. the matrices $S$ and $T$ are unitary).
:::

Proposition [\[modu\]](#modu){reference-type="ref" reference="modu"} is proved in Section 3.

::: remark
As before, the proposition actually means that this representation is totally unitary, i.e. the algebraic conjugates of this representation are unitary as well.
:::

::: remark
It is interesting whether Proposition [\[modu\]](#modu){reference-type="ref" reference="modu"} generalizes to mapping class groups of higher genus Riemann surfaces.
:::

We note that the results of this subsection are known for hermitian categories [@BaKi]. Our results imply that these results are valid without this assumption.

## Module categories, the dual category, the Drinfeld center

Let ${\mathcal M}$ be an indecomposable left module category over a rigid tensor category ${\mathcal C}$ [@O] (all module categories we consider are assumed semisimple). This means, ${\mathcal M}$ is a module category which cannot be split in a direct sum of two nonzero module subcategories. In this case one can define the dual category ${\mathcal C}^*_{{\mathcal M}}$ to be the category of module functors from ${\mathcal M}$ to itself: ${\mathcal C}^*_{{\mathcal M}}={\rm Fun}_{\mathcal C}({\mathcal M},{\mathcal M})$ [@O]. This is a rigid tensor category (the tensor product is the composition of functors, the right and left duals are the right and left adjoint functors).

For example, let us consider ${\mathcal C}$ itself as a module category over ${\mathcal C}\otimes {\mathcal C}^{op}$, via $(X,Y)\otimes Z=X\otimes Z\otimes Y$. Then the dual category is the Drinfeld center $Z({\mathcal C})$ of ${\mathcal C}$ (see [@O1; @Mu2]; for the basic theory of the Drinfeld center see [@K]).

The following result was proved by Müger [@Mu1; @Mu2] under the assumption $\dim({\mathcal C})\ne 0$ (which, as we have seen, is superfluous in zero characteristic) and minor additional assumptions.

::: theorem
[]{#dualcat label="dualcat"} For any indecomposable module category ${\mathcal M}$ over a fusion category ${\mathcal C}$, the category ${\mathcal C}^*_{{\mathcal M}}$ is semisimple (so it is a fusion category), and $\dim({\mathcal C}^*_{{\mathcal M}})=\dim({\mathcal C})$. In particular, for any fusion category ${\mathcal C}$ the category $Z({\mathcal C})$ is a fusion category of global dimension $\dim({\mathcal C})^2$.
:::

In fact, we have the following more general results, which (as well as the results in the next subsection) are inspired by [@Mu1; @Mu2].

::: theorem
[]{#m1m2 label="m1m2"} For any module categories ${\mathcal M}_1,{\mathcal M}_2$ over a fusion category ${\mathcal C}$, the category of module functors ${\rm Fun}_{{\mathcal C}}({\mathcal M}_1,{\mathcal M}_2)$ is semisimple.
:::

Theorems [\[dualcat\]](#dualcat){reference-type="ref" reference="dualcat"} and [\[m1m2\]](#m1m2){reference-type="ref" reference="m1m2"} are proved in Section 5.
