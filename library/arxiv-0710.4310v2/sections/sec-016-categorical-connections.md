---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-016-categorical-connections
section_title: "Categorical connections"
section_number: null
pages: 17-18
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.985
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
::: Definition
Let $G$ be a Lie group. Let $M$ be a smooth manifold. Let $P \to M$ be a smooth principal bundle with structure group $G$. Denote the right action of $G$ on $P$ as $g \in G\mapsto {R_g} \in \diff(M)$. Let also ${\Gc=(\d\colon E \to G,\tr)}$ be a Lie crossed module, where $\tr$ is a Lie group left action of $G$ on $E$ by automorphisms. Let also ${\mathfrak{G}=(\d \colon \le \to  \lg,\tr )}$ be the associated differential crossed module. A $\Gc$-categorical connection on $P$ is a pair $(\w,m)$, where $\w$ is a connection 1-form on $P$, i.e. $\w\in \A^1(P,\lg)$ is a $1$-form on $P$ with values in $\lg$ such that:

1.  $R_g^*(\w)=g^{-1}\w g , \forall g \in G,$

2.  $\w(A^\#)=A,\forall A \in \lg$;

and $m\in \A^2(P,\le)$ is a 2-form on $P$ with values in $\le$, the Lie algebra of $E$, such that:

1.  The 2-form $m$ is $G$-equivariant. In other words we have $R_g^*(m)=g^{-1} \tr m$ for each $g \in G$.

2.  The 2-form $m$ is horizontal, in other words: $$m(X,Y)=m(X^H,Y^H), \textrm{ for each } X,Y \in \X(P).$$ In particular $m(X_u,Y_u)=0$ if either of the vectors $X_u,Y_u \in T_u P$ is vertical, where $u \in P$. Here the map $X \in \X(P) \mapsto X^H \in \X(P)$ denotes the horizontal projection of vector fields on $P$ with respect to the connection 1-form $\w$.

Finally we require that $$\d(m)=\W$$ where $\W\in \A^2(P,\lg)$ is the curvature 2-form of $\w$.
:::

is of course equivalent to the vanishing of the fake curvature of [@BS; @BrMe]; see [\[lform\]](#lform){reference-type="ref" reference="lform"}.

::: Example
Let $P$ be any principal $G$-bundle with a connection 1-form $\w$. Let $\W$ be the curvature $2$-form of $\w$. If $\Gc=(\id \colon G \to G,\tr)$, where $\tr$ is the adjoint action of $G$ on $G$, then $(\w,\W)$ is a $\Gc$-categorical connection on $P$. More generally we can take $\Gc$ to be given by the universal covering map $E \to G$ of $G$; see example [\[cv\]](#cv){reference-type="ref" reference="cv"}.
:::
