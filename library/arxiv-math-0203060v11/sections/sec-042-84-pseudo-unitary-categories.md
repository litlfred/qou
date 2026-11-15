---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-042-84-pseudo-unitary-categories
section_title: "Pseudo-unitary categories"
section_number: 8.4
pages: 34-35
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.956
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
Let us say that a fusion category ${\mathcal C}$ is *pseudo-unitary* if $\dim({\mathcal C})={\rm FPdim}({\mathcal C})$. This property is automatically satisfied for unitary categories, which occur in the theory of operator algebras, but it fails, for example, for the Yang-Lee category.

::: proposition
[]{#uniqpivo label="uniqpivo"} Any pseudo-unitary fusion category ${\mathcal C}$ admits a unique pivotal (in fact, spherical) structure, with respect to which the categorical dimensions of all simple objects are positive, and coincide with their Frobenius-Perron dimensions.
:::

::: proof
*Proof.* Let $g: Id\to ****$ be an isomorphism of tensor functors, $a:Id\to **$ an isomorphism of additive functors, such that $a^2=g$, $d_i$ be the dimensions of simple objects $X_i$ associated to $a$ as in Section 3.1, and $\mathbf d$ the vector with components $d_i$. Then $T_i\mathbf d=d_i\mathbf d$, and $|d_i|=f_i$ is the Frobenius-Perron dimension of $X_i$. But $|(T_i)_{jk}|\le (N_i)_{jk}$. Thus, $$f_if_j=|d_id_j|=|\sum (T_i)_{jk}d_k|\le \sum (N_i)_{jk}f_k=f_if_j$$ This means that the inequality in this chain is an equality. In particular $(T_i)_{jk}=\pm (N_i)_{jk}$, and the argument of $d_id_j$ equals the argument of $(T_i)_{jk}d_k$ whenever $(N_i)_{jk}>0$. This implies that whenever $X_k$ occurs in the tensor product $X_i\otimes X_j$, the ratio $d_i^2d_j^2/d_k^2$ is positive. Thus, the automorphism of the identity functor $\sigma$ defined by $\sigma|_{X_i}=d_i^2/|d_i|^2$ is a tensor automorphism. Let us twist $g$ by this automorphism. After this twisting, the new dimensions $d_i$ will be real. Thus, we can assume without loss of generality that $d_i$ were real from the beginning.

It remains to twist the square root $a$ of $g$ by the automorphism of the identity functor $\tau$ given by $\tau|_{X_i}=d_i/|d_i|$. After this twisting, new $T_i$ is $N_i$ and new $d_k$ is $f_k$. This means that $\beta_i^{jk}=1$ and $a$ is a pivotal structure with positive dimensions. It is obvious that such a structure is unique. We are done. ◻
:::
