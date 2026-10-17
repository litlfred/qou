---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-026-57-surjective-and-injective-functors
section_title: "Surjective and injective functors"
section_number: 5.7
pages: 20-21
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.986
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
Let ${\mathcal C},{\mathcal D}$ be multi-fusion categories, and $F:{\mathcal C}\to {\mathcal D}$ be a unital tensor functor.

We will say that $F$ is injective if it is fully faithful (in this case $F$ identifies ${\mathcal C}$ with a full tensor subcategory of ${\mathcal D}$). We will say that $F$ is surjective if any simple object $X$ of ${\mathcal D}$ is contained in an object of the form $F(T)$, $T\in {\mathcal C}$. If $F$ is surjective and ${\mathcal C}$,${\mathcal D}$ are indecomposable, then ${\mathcal D}$ is said to be a quotient category of ${\mathcal C}$.

Now let ${\mathcal M}$ be a faithful module category over ${\mathcal D}$. Then it is also a faithful module category over ${\mathcal C}$. Let $R$ be a semisimple algebra with blocks labeled by simple objects of ${\mathcal M}$, and $G$ the corresponding fiber functor ${\mathcal D}\to R$-bimod. Let $A=\text{End}_k(G)$, $B=\text{End}_k(G\circ F)$ be the corresponding weak Hopf algebras. Then the functor $F$ induces a morphism of weak Hopf algebras $\phi_F:A\to B$, and vice versa. It is easy to check that $F$ is surjective, respectively injective if and only if $\phi_F$ is injective, respectively surjective.

Let us now consider the corresponding dual categories ${\mathcal C}^*,{\mathcal D}^*$ (we will drop the subscript ${\mathcal M}$, since the only module category we will consider in this subsection will be ${\mathcal M}$). We have a natural dual functor $F^*:{\mathcal D}^*\to {\mathcal C}^*$, since any ${\mathcal D}$-linear functor $\Phi:{\mathcal M}\to {\mathcal M}$ has a natural ${\mathcal C}$-linear structure, defined using $F$. It is clear that the morphism $\phi_{F^*}:B^*\to A^*$ is given by $\phi_{F^*}=\phi_F^*$.

::: proposition
[]{#star label="star"} Let $F:{\mathcal C}\to {\mathcal D}$ be a unital tensor functor between multi-fusion categories. If $F$ is surjective (injective) then $F^*$ is injective (surjective).
:::

::: proof
*Proof.* The claim is equivalent to the statement that surjectivity of $\phi_F$ is equivalent to injectivity of $\phi_F^*$, and vice versa, which is obvious. ◻
:::
