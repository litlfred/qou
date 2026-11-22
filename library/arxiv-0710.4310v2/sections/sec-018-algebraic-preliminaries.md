---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-018-algebraic-preliminaries
section_title: "Algebraic preliminaries"
section_number: null
pages: 18-19
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.966
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
Let $M$ be a smooth manifold. Consider a differential crossed module ${\mathfrak{G}=(\d\colon \le \to \lg,\tr)}$. In particular the map $(X,e) \in \lg \times \le  \mapsto X \tr e \in \le$ is bilinear.

Let $a \in \A^n(M,\lg )$ and $b \in \A^m(M,\le)$ be $\lg$- and $\le$-valued (respectively) differential forms on $M$. We define $a \tn^\tr b$ as being the $\le$-valued covariant tensor field on $M$ such that $$(a \tn^\tr b)(A_1,\ldots, A_n,B_1,\ldots B_m)= a (A_1,\ldots, A_n)\tr b(B_1,\ldots, B_m);A_i,B_j \in \X(M).$$ We also define an alternating tensor field $a \wedge^\tr b \in \A^{n+m}(M,\le)$, being given by $${ a \wedge^\tr b=\frac{(n+m)!}{n! m!}{\rm Alt}(a  \tn^\tr b).}$$ Here ${\rm Alt}$ denotes the natural projection from the vector space of $\le$-valued covariant tensor fields on $M$ onto the vector space of $\le$-valued differential forms on $M$.

For example, if $a \in \A^1(M,\lg)$ and $b \in \A^2(M,\le)$, then $a \wedge^\tr b$ satisfies: $$\label{BB}
(a \wedge^\tr b)(X,Y,Z)=a(X) \tr b(Y,Z)+a(Y) \tr b(Z,X)+a(Z) \tr b(X,Y),$$ where $X,Y,Z \in \X(M).$

Note that the formula: $$d (a  \wedge^\tr b)=d a  \wedge^\tr b  +(-1)^n a  \wedge^\tr d b,$$ where $a \in \A^n(M,\lg)$ and $b \in \A^m(M,\le)$, holds trivially.

As as example of this notation, let $P\to M$ be a principal $G$-bundle over the manifold $M$. Let $\w \in \A^1(P,\lg)$ be a connection 1-form on $M$. Then the structure equation for the curvature form $\W=D \w$ of $\w$ can be written as: $$\W=d\w+{\frac{1}{2}}\w \wedge^{\ad} \w,$$ where $\ad$ denotes the adjoint action of $\lg$ on $\lg$. Furthermore the Bianchi identity can be written as: $$d \W+\w\wedge^{\ad} \W=0;$$ see [\[curv\]](#curv){reference-type="ref" reference="curv"}.
