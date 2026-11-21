---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-003-curvature
section_title: "Curvature"
section_number: null
pages: 5-6
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
[]{#curv label="curv"}

Let $P$ be a principal $G$-bundle over $M$. Let $\w \in \A^1(P,\lg)$ be a connection 1-form on $P$. Given an $n$-form $a$ on $P$, the exterior covariant derivative of $a$ is given by $$Da=d a \circ (\underbrace{H \times H \ldots \times  H}_{(n+1)\textrm{-times }} ).$$

Let $\W\in \A^2(P,\lg)$ be the curvature 2-form of the connection $\w$. It can be defined as the exterior covariant derivative $D\w$ of the connection 1-form $\w$, in other words: $$\W(X,Y)=d \w(X^H,Y^H),$$ where $X,Y \in \X(P)$. The curvature $2$-form $\W$ is $G$-equivariant, which means: $$R_g^*(\W)=g^{-1}\W g, \forall g \in G .$$ Recall also Cartan's structure equation: $$\label{cse}{d \w(X,Y) +[\w(X),\w(Y)]=\W(X,Y),}$$ valid for any vector fields $X,Y \in \X(P)$. The Bianchi identity can be stated by saying that the exterior covariant derivative $D \W$ of the curvature form is zero, in other words: $$D \W=d \W\circ (H \times H \times H)=0.$$ The Bianchi identity can also be written as: $${d \W(X,Y,Z)+[\w(X),\W(Y,Z)]+[\w(Y),\W(Z,X)]+[\w(Z),\W(X,Y)]=0,}$$ for any smooth vector fields $X,Y,Z \in \X(P)$.
