---
doc_id: arxiv-1204.5807v1
doc_title: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES"
section_id: sec-012-28-cospherical-hopf-algebras
section_title: "Cospherical Hopf algebras"
section_number: 2.8
pages: 14-16
source_pdf: 1204.5807v1.pdf
source_sha256: 4bf4f73b0c152b19
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.911
latex_coverage_ratio: 0.867
doc_brief: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES — This is a survey on spherical Hopf algebras. We give criteria to decide when a Hopf algebra is spherical and collect examples."
---
It is natural to look at the notions that insure that the category of comodules of a Hopf algebra is pivotal or spherical. This was done in [@Bi; @o].

::: Def
[]{#def:cospherical-ha label="def:cospherical-ha"} A *cospherical* Hopf algebra is a pair $(H, t)$, where $H$ is a Hopf algebra and $t\in \operatorname{Alg}(H, \Bbbk)$ is such that $$\begin{aligned}
\label{eq:copivot-square-antipode}
{\mathcal S}^2(x_{\left( 1 \right)})t(x_{\left( 2 \right)})&= t(x_{\left( 1 \right)})x_{\left( 2 \right)},  & x&\in H, \\
\label{eq:copivot-traza}
\operatorname{tr}_V((\operatorname{id}_V\otimes t)\rho_V \vartheta) &= tr_V((\operatorname{id}_V\otimes t^{-1})\rho_V \vartheta),  & \vartheta &\in \operatorname{End}_H(V), &&
\end{aligned}$$ for all $V\in \operatorname{Corep}H$. We say that $t\in \operatorname{Alg}(H, \Bbbk)$ is a *copivot* when it satisfies [\[eq:copivot-square-antipode\]](#eq:copivot-square-antipode){reference-type="eqref" reference="eq:copivot-square-antipode"}; pairs $(H, t)$ with $t$ a copivot are called *copivotal Hopf algebras*. A *cospherical element* is a copivot that fulfills [\[eq:copivot-traza\]](#eq:copivot-traza){reference-type="eqref" reference="eq:copivot-traza"}. Let $H$ be a cospherical Hopf algebra. Then the category $\operatorname{Corep}H$ is spherical; in fact, the left and right traces are given by the sides of [\[eq:copivot-traza\]](#eq:copivot-traza){reference-type="eqref" reference="eq:copivot-traza"}.
:::

The set $\operatorname{Alg}(H, \Bbbk)$ is a subgroup of the group $\operatorname{Hom}_{\star}(H, \Bbbk)$ of convolution-invertible linear functionals, which in turn acts on $\operatorname{End}(H)$ on both sides. Hence [\[eq:copivot-square-antipode\]](#eq:copivot-square-antipode){reference-type="eqref" reference="eq:copivot-square-antipode"} can be written as ${\mathcal S}^2 * t=t* id_H$ or else as ${\mathcal S}^2=t*id_H*t^{-1}$. The copivot is not unique but it is determined up to multiplication by an element in $\operatorname{Alg}(H, \Bbbk)$ that centralizes $\operatorname{id}_H$. The antipode of a copivotal Hopf algebra is bijective, with inverse given by ${\mathcal S}^{-1}(x)=\sum t^{-1}(x_{\left( 1 \right)}){\mathcal S}(x_{\left( 2 \right)})t(x_{\left( 3 \right)})$, $x\in H$.

The following statement is proved exactly as Proposition [\[prop:reduccion a irreducibles\]](#prop:reduccion a irreducibles){reference-type="ref" reference="prop:reduccion a irreducibles"}.

::: prop
[]{#prop:reduccion a coirreducibles label="prop:reduccion a coirreducibles"} A copivotal Hopf algebra $(H,t)$ is cospherical if and only if [\[eq:copivot-traza\]](#eq:copivot-traza){reference-type="eqref" reference="eq:copivot-traza"} holds for all simple $H$-comodules. 0◻
:::

::: Exs
1.  Assume that $H$ is finite-dimensional. Then $H$ is copivotal (resp., cospherical) iff $H^*$ is pivotal (resp., spherical).

2.  Any involutory Hopf algebra is cospherical with $t = \varepsilon$.

3.  A copivotal Hopf algebra with involutive copivot is cospherical.

4.  Condition [\[eq:copivot-square-antipode\]](#eq:copivot-square-antipode){reference-type="eqref" reference="eq:copivot-square-antipode"} is multiplicative on $x$; also, it holds for $x\in G(H)$.

5.  []{#item:pointed-pivotal label="item:pointed-pivotal"} Let $H$ be a pointed Hopf algebra generated as an algebra by $G(H)$ and a family $(x_i)_{i\in I}$, where $x_i$ is $(g_i,1)$ skew-primitive. Assume that $g_ix_ig_i^{-1} = q_ix_i$, with $q_i\in \Bbbk^{\times} \setminus \{1\}$ for all $i\in I$. If $t\in \operatorname{Alg}(H, \Bbbk)$, then $t(x_i) = 0$, $i\in I$. Hence $t$ is a copivot iff $t(g_i) = q_{i}^{-1}$, for all $i\in I$.

6.  Let $H$ be a pointed Hopf algebra as in item [\[item:pointed-pivotal\]](#item:pointed-pivotal){reference-type="eqref" reference="item:pointed-pivotal"} and $t\in \operatorname{Alg}(H, \Bbbk)$ a copivot. Then $H$ is cospherical iff $t(g) \in \{\pm 1\}$ for all $g\in G(H)$.

7.  The notion of coribbon Hopf algebra is formally dual to the notion of ribbon Hopf algebra, see [@h; @lt]. Coribbon Hopf algebras are cospherical. For instance, the quantized function algebra ${\mathcal O}_q(G)$ of a semisimple algebraic group is cosemisimple and coribbon, when $q$ is not a root of 1.
:::

We recall now the contruction of universal copivotal Hopf algebras.

::: Def
[@Bi] Let $F\in GL_n(k)$. The Hopf algebra $H(F)$ is the universal algebra with generators $(u_{ij})_{1\leq i,j\leq n}$, $(v_{ij})_{1\leq i,j\leq n}$ and relations $$\begin{aligned}
uv^t&=v^tu=1, & vFu^tF^{-1}&= Fu^tF^{-1}v=1.
\end{aligned}$$

The comultiplication is determined by $\Delta (u_{ij})= \sum_k u_{ik}\otimes u_{kj}$, $\Delta (v_{ij})= \sum_k v_{ik}\otimes v_{kj}$ and the antipode by ${\mathcal S}(u)=v^t$, ${\mathcal S}(v)=Fu^tF^{-1}$. The Hopf algebra $H(F)$ is copivotal, the copivot being $t_F(u)=(F^{-1})^t$ and $t_F(v)=F$.

Let $H$ be a Hopf algebra provided with $V\in \operatorname{Corep}H$ of dimension $n$ such that $V\cong V^{**}$. Then there exist a matrix $F\in GL_n(k)$, a coaction $\beta_V:V\to V\otimes H(F)$ and a Hopf algebra morphism $\pi:H(F)\to H$ such that $(\operatorname{id}_V\otimes \pi)\beta_V=\rho_V$.
:::

In conclusion, we would like to explore semisimple tensor categories arising from cospherical, not cosemisimple, Hopf algebras. The first step is the dual version of Theorem [\[prop:repoH-ss\]](#prop:repoH-ss){reference-type="ref" reference="prop:repoH-ss"}, which is proved exactly in the same way.

::: Thm
[]{#prop:corepoH-ss label="prop:corepoH-ss"} Let $H$ be a cospherical Hopf algebra. Then the non-degenerate quotient $\operatorname{\underline{Corep}}H$ of $\operatorname{Corep}H$ is a completely reducible spherical tensor category, and $\operatorname{Irr}\operatorname{\underline{Corep}}H$ is in bijective correspondence with the set of isomorphism classes of indecomposable finite-dimensional $H$-comodules with non-zero quantum dimension. 0◻
:::
