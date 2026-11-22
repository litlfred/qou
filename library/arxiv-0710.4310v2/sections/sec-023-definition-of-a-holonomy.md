---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-023-definition-of-a-holonomy
section_title: "Definition of a holonomy."
section_number: null
pages: 22-23
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
The following definition appears in [@CP].

::: Definition
Let $M$ and $N$ be smooth manifolds. Suppose that $M$ has a chosen base point $*$. A map $F \colon \pi_1^1(M,*) \to N$ is said to be smooth if, for any $2$-path $\G\colon [0,1]^2 \to M,$ with $\d_l(\G)=\d_r(\G)=*$, the map $$s \in [0,1] \mapsto F([\g_s])\in N$$ is smooth. Here $\G(t,s)=\g_s(t)$, where $s,t \in [0,1]$.

Let $G$ be a Lie group. A holonomy is, by definition, a smooth group morphism $\pi_1^1(M,*) \to G$.
:::

The following result appears in [@CP].

::: Theorem
[]{#E label="E"} Let $M$ be a smooth manifold with a base point $*$. Let also $G$ be a Lie group. Let $P \to M$ be a smooth principal $G$-bundle over $M$ with a connection $\w$. Let $u \in P_*$, the fibre of $P$ at $*$. Then the parallel transport of $\w$ determines a holonomy $F^1_{(\w,u)} \colon \pi_1^1(M,*) \to G$.
:::

::: Proof
Recall the notation of [\[Hol\]](#Hol){reference-type="ref" reference="Hol"}. Given a 1-path $\g \colon [0,1] \to M$, with $\g(0),\g(1)=*$, define $F^1_{(\w,u)}(\g)$ to be the unique element of $G$ such that $u={\mathcal{H}}_\w(\g,1,u)F^1_{(\w,u)}(\g)$. Then, if $\G$ is a 2-path, with $\d_l(\G)=\d_r(\G)=*$, it follows that the map $$s \in [0,1] \mapsto F^1_{(\w,u)}   (\g_s)\in G,$$ where $\G(t,s)=\g_s(t);s,t \in [0,1]$, is smooth. This follows from the fact that the map $t \in [0,1] \mapsto {\mathcal{H}}_\w(\g_s,t,u)$ is a solution of a differential equation in $t$. This differential equation depends smoothly on $s$ if $\G$ is smooth. For details see [@KN page 74].

The fact that $F^1_{(\w,u)}$ descends to a map $\pi_1^1(M,*)\to G$ follows from lemma [\[EEE\]](#EEE){reference-type="ref" reference="EEE"} and the fact that the horizontal lift of vectors defines a linear map. Finally the fact that $F^1_{(\w,u)}$ is a group morphism follows from the fact that ${\mathcal{H}}_\w\big (\g^2\g^1,1,u\big )={\mathcal{H}}_\w\big(\g^1,1,{\mathcal{H}}_\w(\g^2,1,u)\big)$, for any smooth curves $\g^1$ and $\g^2$ in $M$ starting and ending at $*$.
:::

It is proved in [@CP] that any holonomy $\pi_1^1(M,*) \to G$ arises from a bundle with connection in this way.
