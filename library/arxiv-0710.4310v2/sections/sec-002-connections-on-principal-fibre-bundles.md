---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-002-connections-on-principal-fibre-bundles
section_title: "Connections on principal fibre bundles"
section_number: null
pages: 4-5
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 1.0
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
[]{#CCC label="CCC"}

For full details on connections on principal fibre bundles see [@KN; @P].

Let $M$ be a paracompact smooth manifold. Let $G$ be a Lie group with Lie algebra $\lg$. Consider a principal $G$-bundle $P$ over $M$, with canonical projection $\pi\colon P \to M$. For each $x \in M$, let $P_x=\pi^{-1}(x)$ be the fibre at $x$. Let also $\X(P)$ denote the Lie algebra of smooth vector fields on $P$. Recall that there exists a Lie algebra morphism $A \in \lg \mapsto A^\# \in \X(P)$, such that $A^\#_u=\frac{d}{dt}u \exp(tA)_{t=0}, \forall u \in P, \forall A \in \lg$. Here if $X\in \X(P)$ is a vector field then $X_u \in T_u P$ (the tangent space of $P$ at $u\in P$) denotes the value of $X$ at the point $u$.

Denote the right action of $G$ on $P$ as $g \in G \mapsto R_g \in \mathrm{diff}(P)$, where ${\rm diff}(P)$ denotes the diffeomorphism group of $P$. Recall the following very useful formula: $${(R_g)}_*(A^\#)=\left (g^{-1}Ag\right )^\#,$$ where $g \in G$ and $A \in \lg$. Given an element $u \in P$, recall that a vector $X_u \in T_u P$ is said to be vertical if $\pi_*(X_u)  =0$. Let $T_u^VP$ denote the subspace of vertical vectors in $T_u P$. Notice that any $X_u \in T_u^VP$ is of the form $A^\#_u$ for some $A \in \lg$, and this correspondence is one-to-one.

Let $\w\in \A^1(P,\lg)$ be a connection on $P$. In other words $\w$ is a smooth 1-form on $P$ with values in $\lg$ such that:

1.  $R_g^*(\w)=g^{-1}\w g , \forall g \in G,$

2.  $\w(A^\#)=A,\forall A \in \lg$.

Given an element $u \in P$, let $T^H_u P=\{X_u \in T_u P\colon \w(X_u)=0\}$, the horizontal subspace at $u \in P$. Then $T^H_u$ is a complementary subspace of $T^V_uP$ in $T_u P$ for each $u \in P$. Moreover, the following identity holds for each $g \in G$ and $u \in P$: $$\left (T^H_u P\right ) g= T^H_{ug} P .$$

The natural projection maps $X \in TP \mapsto X^H$ and $X \in TP \mapsto X^V$ are smooth. Here $TP$ denotes the tangent bundle of $P$. There exists also a unique map $X \in \X(M) \mapsto \t{X}\in \X(P)$, called the horizontal lift of $X\in \X(M)$, such that $\t{X}_u \in T_u^HP, \forall u \in P$ and $\pi_*(\t{X})=X$, for any $X \in \X(M)$, the Lie algebra of smooth vector fields on $M$. Note that this horizontal lift gives rise to linear maps $T_x M  \to T_u P$, if $\pi(u)=x$, where $x \in M$ and $u \in P$. The horizontal lift of a vector field $X \in \X(M)$ is always $G$-invariant. In other words: $$\t{X} g=\t{X}, \forall g \in G.$$
