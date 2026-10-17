---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-006-25-results-on-weak-hopf-algebras
section_title: "Results on weak Hopf algebras"
section_number: 2.5
pages: 7-9
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.935
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
A convenient way to visualize (multi-) fusion categories is using weak Hopf algebras (see Section 4 for the definitions). Namely, let ${\mathcal C}$ be a multi-fusion category. Let $R$ be a finite dimensional semisimple $k$-algebra, and $F$ a fiber functor (i.e. an exact, faithful tensor functor) from ${\mathcal C}$ to $R$-bimod. Let $A=\text{End}_k(F)$ (i.e. the algebra of endomorphisms of the composition of $F$ with the forgetful functor to vector spaces).

::: theorem
[]{#Schlah label="Schlah"} ([@Sz]) $A$ has a natural structure of a semisimple weak Hopf algebra with base $R$, and ${\mathcal C}$ is equivalent, as a tensor category, to the category $\text{Rep}(A)$ of finite dimensional representations of $A$.
:::

::: remark
In order to lift the naturally existing map $A\to A\otimes_R A$ to a weak Hopf algebra coproduct $A\to A\otimes_k A$, one needs to use a separability idempotent in $R\otimes R$. We will always use the unique *symmetric* separability idempotent. In this case, the weak Hopf algebra $A$ satisfies an additional *regularity condition*, saying that the squared antipode is the identity on the base of $A$.
:::

One can show that for any multi-fusion category ${\mathcal C}$, a fiber functor $F$ exists for a suitable $R$. Indeed, let ${\mathcal M}$ be any semisimple faithful module category over ${\mathcal C}$, i.e. such that any nonzero object of ${\mathcal C}$ acts by nonzero (for example, ${\mathcal C}$ itself). Let $R$ be a semisimple algebra whose blocks are labeled by simple objects of ${\mathcal M}$: $R=\oplus_{M\in {\rm Irr}({\mathcal M})}R_M$, and $R_M$ are simple. Now define a functor $F:{\mathcal C}\to R-\text{bimod}$ as follows: for any object $X\in {\mathcal C}$ set $$F(X)=\oplus_{M,N\in {\rm Irr}({\mathcal M})}\text{Hom}_{{\mathcal M}}(M,X\otimes N)
\otimes B_{NM},$$ where $B_{NM}$ is the simple $(R_N,R_M)$-bimodule. This functor has an obvious tensor structure (coming from composition of morphisms), and it is clearly exact and faithful. So it is a fiber functor.

Therefore, we have

::: corollary
[]{#Schlah1 label="Schlah1"} ([@H],[@Sz]) Any multi-fusion category is equivalent to the category of finite dimensional representations of a (non-unique) regular semisimple weak Hopf algebra. This weak Hopf algebra is connected if and only if ${\mathcal C}$ is a fusion category.
:::

::: remark
In particular, we can choose $R$ to be a commutative algebra (i.e., all blocks have size $1$). Thus, any multi-fusion category is equivalent to the category of representations of a weak Hopf algebra with a commutative base. This result was proved by Hayashi in [@H], where weak Hopf algebras with commutative bases appear under the name "face algebras".
:::

.05in

The language of weak Hopf algebras is convenient to visualize various categorical constructions. One of them is that of a dual category. Indeed, let ${\mathcal C}$ be the category of representations of a weak Hopf algebra $A$. Let $R$ be the base of $A$. Then we have a natural fiber functor from ${\mathcal C}$ to the category of $R$-bimodules -- the forgetful functor. This functor defines a natural structure of a module category over ${\mathcal C}$ on the category ${\mathcal M}=R-\text{bimod}$. In this case, the dual category ${\mathcal C}^*_{{\mathcal M}}$ is simply the representation category of the dual weak Hopf algebra $A^{*cop}$ with the opposite coproduct (see [@O]). Furthermore, as we just showed, this example is general, in the sense that any faithful module category over a multi-fusion category can be obtained in this way.

The global dimension of the category of representations of a connected weak Hopf algebra is closely related to the trace of squared antipode in this weak Hopf algebra. This connection is expressed by the following theorem.

Let a fusion category ${\mathcal C}$ be the representation category of a regular semisimple weak Hopf algebra $A$. Let $S$ be the antipode of $A$. Let $q_i$ be the primitive idempotents of the center of the base $A_t$, and $n_i$ the block sizes of the matrix algebras $q_iA_t$.

::: theorem
[]{#traceofS2 label="traceofS2"} One has $\text{Tr}(S^2|_{q_jAS(q_i)})=\dim({\mathcal C})n_i^2n_j^2$. In particular, over ${\mathbb{C}}$ one always has $\text{Tr}(S^2|_{q_jAS(q_i)})>0$.
:::

::: remark
[]{#tra label="tra"} Theorem [\[traceofS2\]](#traceofS2){reference-type="ref" reference="traceofS2"} implies that $\text{Tr}(S^2|_{A}) = \dim(\text{Rep}(A)) \dim(A_t)^2$.
:::

We also have the following result, which generalizes the Larson-Radford theorem for Hopf algebras [@LR1].

::: theorem
[]{#sscoss label="sscoss"} A semisimple weak Hopf algebra over $k$ is also cosemisimple.
:::

Theorem [\[traceofS2\]](#traceofS2){reference-type="ref" reference="traceofS2"} is proved in Section 5. Theorem [\[sscoss\]](#sscoss){reference-type="ref" reference="sscoss"} follows from Theorem [\[multi-fus\]](#multi-fus){reference-type="ref" reference="multi-fus"}, since the representation category of the dual weak Hopf algebra is the dual category.
