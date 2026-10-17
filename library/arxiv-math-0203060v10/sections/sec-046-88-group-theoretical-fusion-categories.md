---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-046-88-group-theoretical-fusion-categories
section_title: "Group-theoretical fusion categories"
section_number: 8.8
pages: 39-40
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.943
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
An example of a fusion category with integer Frobenius-Perron dimensions is the category ${\mathcal C}(G,H,\omega,\psi)$ associated to quadruples $(G,H,\omega,\psi)$, where $G$ is a finite group, $H$ is a subgroup, $\omega\in Z^3(G,{\mathbb{C}}^*)$ is a 3-cocycle, $\psi\in C^2(H,{\mathbb{C}}^*)$ a 2-cochain such that $d\psi=\omega|_H$ (see [@O1]). Namely, let ${\rm Vec}_{G,\omega}$ be the category of finite dimensional $G$-graded vector spaces with associativity defined by $\omega$. Let ${\rm Vec}_{G,\omega}(H)$ be the subcategory of ${\rm Vec}_{G,\omega}$ of objects graded by $H$. Consider the twisted group algebra $A={\mathbb{C}}_\psi[H]$. Since $d\psi=\omega|_H$, it is an associative algebra in this category. Then ${\mathcal C}(G,H,\omega,\psi)$ is defined to be the category of $A$-bimodules in ${\rm Vec}_{G,\omega}$.

::: remark
If $(\omega',\psi')$ is another pair of elements such that $\omega'=\omega+d\eta,\psi'=\psi+\eta|_H+d\chi$, $\eta\in C^2(G,{\mathbb{C}}^*)$, $\chi\in C^1(H,{\mathbb{C}}^*)$, then ${\mathcal C}(G,H,\omega,\psi)$ is equivalent to ${\mathcal C}(G,H,\omega',\psi')$. Thus, the categories ${\mathcal C}(G,H,\omega,\psi)$ are parametrized by the set $S(G,H)$ of equivalence classes of pairs $(\omega,\psi)$ under the above equivalence, which is a fibration over ${\rm Ker}(H^3(G,{\mathbb{C}}^*)\to 
H^3(H,{\mathbb{C}}^*))$ with fiber being a torsor over ${\rm Coker}(H^2(G,{\mathbb{C}}^*)\to H^2(H,{\mathbb{C}}^*))$.
:::

::: definition
A fusion category is said to be group-theoretical if it is of the form ${\mathcal C}(G,H,\omega,\psi)$.
:::

::: remark
We note that there may be more than one way to represent a given fusion category in the form ${\mathcal C}(G,H,\omega,\psi)$. In particular, $G$ is not uniquely determined. However, $|G|$ is uniquely determined, since it equals the global dimension of ${\mathcal C}(G,H,\omega,\psi)$.
:::

Group-theoretical fusion categories have the following simple characterization. Let us say that a fusion category ${\mathcal D}$ is pointed if all its simple objects are invertible. Any pointed fusion category has the form ${\rm Vec}_{G,\omega}$.

::: proposition
[]{#1dim label="1dim"}[@O1]. A fusion category ${\mathcal C}$ is group-theoretical if and only if it is dual to a pointed category with respect to some indecomposable module category.
:::

::: corollary
[]{#intdim label="intdim"} Group-theoretical fusion categories have integer Frobenius-Perron dimensions of simple objects. In particular, they are pseudo-unitary.
:::

::: proof
*Proof.* This follows from Proposition [\[1dim\]](#1dim){reference-type="ref" reference="1dim"}, Theorem [\[dualfrob\]](#dualfrob){reference-type="ref" reference="dualfrob"}, and the fact that any invertible object has Frobenius-Perron dimension $1$. ◻
:::

It is clear from the results of [@O1] that the class of group-theoretical categories is closed under tensor product, taking the opposite category, and taking the dual category with respect to an indecomposable module category. Moreover, the following result shows that this class is also closed under taking a subcategory or a component of a quotient category.

::: proposition
[]{#subquot label="subquot"}

\(i\) A full fusion subcategory of a group-theoretical category is group-theoretical.

\(ii\) A component in a quotient category of a group-theoretical category is group-theoretical.
:::

::: proof
*Proof.* (i) Let ${\mathcal C}\subset {\mathcal D}$ be fusion categories (${\mathcal C}$ is a full subcategory), and let ${\mathcal D}$ be group-theoretical. Let ${\mathcal M}$ be an indecomposable module category over ${\mathcal D}$ such that ${\mathcal D}^*$ is ${\rm Vec}_{G,\omega}$. Then by Proposition [\[star\]](#star){reference-type="ref" reference="star"}, ${\mathcal C}^*$ is a quotient of ${\rm Vec}_{G,\omega}$. Let $I$ label the component categories of ${\mathcal C}^*$. It is clear that for each $g\in G$ and $i\in I$ there exists a unique $g(i)\in I$ such that the functor $g\otimes$ is an equivalence ${\mathcal C}_{ir}\to {\mathcal C}_{g(i)r}$ for each $r\in I$. So we have an action of $G$ on $I$. Let $j\in I$ and $H$ be the stabilizer of $j$ in $G$. For any $g\in H$, denote by $\bar g_{jj}$ the projection of $g$ to the fusion category ${\mathcal C}^*_{jj}$. Then the assignment $g\to \bar g_{jj}$ is a surjective tensor functor ${\rm Vec}_{H,\omega}\to {\mathcal C}^*_{jj}$. This functor must map invertible objects to invertible objects. Hence, all simple objects of ${\mathcal C}^*_{jj}$ are invertible, so ${\mathcal C}^*_{jj}$ is pointed, and hence ${\mathcal C}$ is group-theoretical (as it is dual to ${\mathcal C}^*_{jj}$ with respect to a module category).

\(ii\) Let ${\mathcal D}$ be group-theoretical, $F:{\mathcal D}\to {\mathcal C}$ be surjective (${\mathcal C}$ is indecomposable), and ${\mathcal C}_{ii}$ a component of ${\mathcal C}$. We need to show that ${\mathcal C}_{ii}$ is group-theoretical. Let ${\mathcal M}$ be an indecomposable module category over ${\mathcal C}$. It suffices to show that ${\mathcal C}^*$ is group-theoretical, as ${\mathcal C}^*$ is dual to ${\mathcal C}_{ii}$ with respect to the i-th part of ${\mathcal M}$. But by Proposition [\[star\]](#star){reference-type="ref" reference="star"}, ${\mathcal C}^*$ is embedded into ${\mathcal D}^*$, so it suffices to know that ${\mathcal D}^*$ is group-theoretical, which follows by duality from the fact that ${\mathcal D}$ is group-theoretical. ◻
:::
