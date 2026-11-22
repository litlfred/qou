---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-024-definition-of-a-categorical-holonomy
section_title: "Definition of a categorical holonomy"
section_number: null
pages: 23-25
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 1.0
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
::: Definition
[]{#K label="K"} Let $M$ be a manifold. A smooth map $J \colon[0,1]^3\to M$, say $J(t,s,x)=\G^x(t,s)=\g^x_s(t),$ where $t,s,x \in [0,1]$, is said to be a 3-path if:

1.  $J$ is constant over $\{0\} \times [0,1]^2$ and over $\{1\} \times [0,1]^2$.

2.  $J$ restricts to a rank-1 homotopy (connecting $\g^0_0$ with $\g^1_0$) over $[0,1] \times \{0\} \times [0,1]$ and over $[0,1] \times \{1\} \times [0,1]$ (connecting $\g^0_1$ with $\g^1_1$).

3.  $J$ has a product structure close to the boundary of $[0,1]^3$; see definition [\[thin2\]](#thin2){reference-type="ref" reference="thin2"}.
:::

In particular $J$ defines a homotopy connecting the 2-paths $\G^0$ and $\G^1$; see [\[2es\]](#2es){reference-type="ref" reference="2es"}. Note that it is not necessarily a rank-2 homotopy.

::: Definition
Let $M$ and $N$ be smooth manifolds. Consider the projection map $S_2(M) \to \S_2(M)$. A map $F\colon \S_2(M) \to N$ is said to be smooth if, for any 3-path $J$, the map $$x \in [0,1] \mapsto F([\G^x]) \in N$$ is smooth. Here $J(t,s,x)=\G^x(t,s)$, for each $(t,s,x) \in[0,1]^3$.
:::

Let ${\Gc= ( \d\colon E \to  G,\tr)}$ be a Lie crossed module. Consider the categorical group ${\mathcal C}(\Gc)$ constructed from $\Gc$, see [\[CCG\]](#CCG){reference-type="ref" reference="CCG"}. Its set of objects is $G$ and its set of morphisms is the semidirect product $G \ltimes E$ of $G$ and $E$; all of these are smooth manifolds. The following definition extends the definition of holonomy for principal $G$-bundles of [@CP] and should be compared with analogous non-strict constructions in [@BS; @MP; @M].

::: Definition
Let $M$ be a smooth manifold. Choose an element $* \in M$. A categorical holonomy is, by definition, a strict monoidal functor (in other words a categorical group morphism) $F\colon {\mathcal P}_{{2}}(M,*) \to \C(\Gc)$, such that the associated maps $F_1 \colon \pi_1^1(M) \to G$ and $F_2 \colon \P_2(M,*) \to G \ltimes   E$ on the sets of objects and morphisms of $\Pc_2(M,*)$ are smooth. Here ${\mathcal P}_{{2}}(M,*)$ is the thin fundamental categorical group of $M$; see [\[TCM\]](#TCM){reference-type="ref" reference="TCM"}.
:::

If we use the notation $$[\G]=\begin{CD} \d_u([\G]) \\ @AA [\G]A \\   \d_d([\G]) \end{CD}\quad \quad \quad \textrm{   and } \quad \quad \quad  (X,e)=\begin{CD} \d(e)^{-1}X\\ @AA eA \\   X\end{CD},$$ to denote the morphisms of $\Pc_2(M,*)$ and of $\C(\Gc)$, then the tensor product of two elements $[\G]$ and $[\G']$ of $\P_2(M,*)$ can be presented in the suggestive form: $$\begin{CD} \d_u([\G]) \\ @AA [\G]A \\   \d_d([\G]) \end{CD} \quad \tn \quad  \begin{CD} \d_u([\G']) \\ @AA [\G']A \\   \d_d([\G']) \end{CD} \quad = \quad \begin{CD} \d_u([\G]) \d_u([\G']) \\ @AA [\G] \circ_h [\G']A \\   \d_d([\G])  \d_d([\G']) \end{CD}$$ In this notation, the condition that a functor $F=(F_1,F_2)\colon \Pc_2(M,*) \to  \C(\Gc)$ be a strict monoidal functor means that: $$F\left ( \begin{CD} \d_u([\G]) \\ @AA [\G]A \\   \d_d([\G]) \end{CD} \quad \tn\quad \begin{CD} \d_u([\G']) \\ @AA [\G']A \\   \d_d([\G']) \end{CD} \right)=\begin{CD} F_1(\d_u([\G])) \\ @AA F_2([\G])A \\   F_1(\d_d([\G])) \end{CD} \quad \tn \begin{CD} F_1(\d_u([\G'])) \\ @AA F_2([\G'])A \\   F_1(\d_d([\G']) )\end{CD}$$ for each $[\G],[\G'] \in \P_2(M,*)$. In other words: $$\begin{CD} F_1\big (\d_u([\G]) \d_u([\G'])\big) \\ @AA F_2\left([\G] \circ_h [\G'] \right) A \\   F_1\big (\d_d([\G])  \d_d([\G']) \big)\end{CD} \quad   \quad= \quad  \begin{CD} F_1\big (\d_u([\G])) F_1\left( \d_u([\G'])\right) \\ @AA \Big (F_1\left(\d_d[\G] \right)\tr  F_2\left( [\G'] \right)\Big ) F_2\left( [\G] \right) A \\   F_1\left (\d_d([\G])\right) F_1\left(  \d_d([\G']) \right)\end{CD} \quad  \quad  \quad  \quad  \quad$$ for each $[\G],[\G'] \in \P_2(M,*) ;$ see [\[CCG\]](#CCG){reference-type="ref" reference="CCG"}. Recall that an arrow $g \ra{(g,e)} \d(e^{-1}) g$ in $\C(\Gc)$ is sometimes simply denoted by $g \ra{e} \d(e^{-1}) g,$ where $g \in G$ and $e \in E.$

Since the category of crossed modules and the category of categorical groups are equivalent, we can give an alternative definition of a categorical holonomy, and define it as being a smooth crossed module map $$\Pi_2^{2,1}(M,*) \to \Gc,$$ where the notion of a smooth crossed module map is the obvious one. Here $\Pi_2^{2,1}(M,*)$ is the thin fundamental crossed module of the smooth manifold $M$; see [\[fcm\]](#fcm){reference-type="ref" reference="fcm"}.
