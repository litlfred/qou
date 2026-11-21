---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-019-the-2-structure-equation
section_title: "The 2-structure equation"
section_number: null
pages: 19-20
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
[]{#se label="se"} The following equation is an analogue of Cartan's structure equation. It will be of prime importance later.

::: Proposition
Let ${\Gc= ( \d\colon E \to  G,\tr)}$ be a Lie crossed module. Let $P$ be a principal $G$-bundle over the manifold $M$. Let also $(\w,m)$ be a categorical $\Gc$-connection on $P$. We have: $\M=dm {+}\w\wedge^\tr m,$ where $\M=D m$ is the 2-curvature $3$-form of $(\w,m)$. In particular the 2-curvature 3-form $\M$ is $G$-equivariant, in other words: $R_g^*(\M)=g^{-1} \tr \M,$ for each $g \in G$.
:::

The proof of the 2-structure equation follows directly from the following lemma.

::: Lemma
[]{#ext label="ext"} Let $a$ be a $G$-equivariant horizontal $(n-1)$-form in $P$. Then $Da=da+\w\wedge^\tr a$.
:::

::: Proof
Let $X^1,\ldots,X^n \in T_uP$, extended to a neighbourhood of $u\in P$. If all vectors are horizontal it follows that $Da(X^1,\ldots,X^n)=(da+\w\wedge^\tr a)(X^1,\ldots,X^n)$, since $\w$ is vertical. Suppose that one of the vectors, which we can suppose to be $X^1$, is vertical. We need to prove that $(da+\w\wedge^\tr a)(X^1,\ldots,X^n)=0$. Choose $A \in \lg$ such that $A^\#_u=X^1_u.$ By using Cartan's magic formula together with the fact that $a$ is horizontal it follows that $da (A^\#,X^2,\ldots,X^n)=(\L_{A^\#}a) (X^2,\ldots X^n)$, where $\L$ denotes Lie derivative. Since $a$ is $G$-equivariant it follows that $\L_{A^\#}a=-A \tr a$. However, $(\w\wedge^\tr a)(A^\#,X^2,\ldots,X^n)=\w(A^\#)\tr a(X^2,\ldots,X^n)$, since $a$ is horizontal. Note $\w(A^\#)=A$.
:::
