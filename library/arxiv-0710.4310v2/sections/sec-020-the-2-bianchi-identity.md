---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-020-the-2-bianchi-identity
section_title: "The 2-Bianchi identity"
section_number: null
pages: 20-20
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
Fix a Lie crossed module ${\Gc= ( \d\colon E \to  G,\tr)}$. Let $P$ be a smooth principal $G$-bundle over $M$ with a connection $\w$. Choose a $\Gc$-categorical connection $(\w,m)$ on $P$.

::: Proposition
Let $\M\in \A^3(P,\le)$ be the 2-curvature 3-form of $(\w,m)$. Then the exterior covariant derivative $D \M$ of $M$ vanishes. In other words: $$d \M \circ (H \times H \times H \times H)=0,$$ which by lemma [\[ext\]](#ext){reference-type="ref" reference="ext"} is the same as: $$d \M +\w \wedge^{\tr} \M=0.$$
:::

::: Proof
Let us prove the second form of the 2-Bianchi identity. By the 2-structure equation it follows that: $$d \M=dd m{+}d(\w \wedge ^\tr m)=d \w \wedge ^\tr m{-} \w \wedge ^\tr d m 
=d \w \wedge ^\tr m{-} \w \wedge ^\tr \M + \w\wedge^{\tr} \left (\w \wedge^{\tr} m\right).$$ Given that $\w\wedge^{\tr} \left (\w \wedge^{\tr} m\right)=\frac{1}{2}(\w\wedge^{\ad } \w )\wedge ^\tr m$ we can conclude: $$d \M=(d \w+\frac{1}{2}\w\wedge^{\ad } \w ) \wedge ^\tr m{-} \w \wedge ^\tr \M 
=\W \wedge ^\tr m{-} \w \wedge ^\tr \M 
=\d(m) \wedge ^\tr m{-} \w \wedge ^\tr \M.$$ We now prove that $\d(m) \wedge ^\tr m=0$. Since ${\mathfrak{G}=(\d \colon \le \to  \lg,\tr )}$ is a differential crossed module we have, for any vector fields $X,Y,Z,W \in \X(P)$:$${\d(m)(X,Y) \tr m(Z,W)=\d\big (m(X,Y)\big ) \tr m(Z,W)
                     =[m(X,Y), m(Z,W)].}$$ Let us see that ${\rm Alt}[m,m]=0$, which implies that $\d(m) \wedge ^\tr m=0$. The permutation $r$ such that $r(X,Y,Z,W)=(Z,W,X,Y)$ is even. In particular ${\rm Alt}([m,m])= {\rm Alt}([m,m] \circ r)$. However, $[m,m] \circ r=-[m,m]$.
:::
