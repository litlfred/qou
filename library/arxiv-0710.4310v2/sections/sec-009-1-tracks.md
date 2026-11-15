---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-009-1-tracks
section_title: "1-Tracks"
section_number: null
pages: 12-14
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 1.0
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
[]{#1-Tracks label="1-Tracks"}

::: Definition
A 1-path is given by a smooth map $\gamma\colon [0,1] \to M$ such that there exists an $\epsilon >0$ such that $\g$ is constant in $[0,\e] \cup [1-\e,1]$; in the terminology of [@CP], this can be abbreviated by saying that each end point of $\g$ has a sitting instant. Given a 1-path $\g$, define the source and target of $\g$ as $\sigma(\g)=\g(0)$ and $\tau(\g)=\g(1)$, respectively.
:::

Given two 1-paths $\g$ and $\f$ with $\tau(\g)=\sigma(\f)$, their concatenation $\g\f$ is defined in the usual way: $$(\g\f)(t)=\left \{ \begin{CD} \g(2t), \textrm{ if }t \in [0,1/2] \\ \f(2t-1), \textrm{ if } t \in [1/2,1]\end{CD} \right.$$ Note that the concatenation of two 1-paths is also a 1-path. The fact that any 1-path has sitting instants at its end points needs to be used to prove this.

::: Definition
A 2-path $\G$ is given by a smooth map $\G\colon [0,1]^2 \to M$ such that there exists an $\epsilon >0$ for which:

1.  $\G(t,s)=\G(0,0)$ if $0 \leq t \leq \epsilon$ and $s \in [0,1]$,

2.  $\G(t,s)=\G(1,0)$ if $1-\epsilon \leq t \leq 1$ and $s \in [0,1]$,

3.  $\G(t,s)=\G(t,0)$ if $0 \leq s \leq \epsilon$ and $t \in [0,1]$,

4.  $\G(t,s)=\G(t,1)$ if $1-\epsilon \leq s \leq 1$ and $t \in [0,1]$.
:::

Given a 2-path $\Gamma$, define the following 1-paths: $$\begin{aligned}
\d_l(\G)(s)&=\G(0,s), s \in [0,1],
&\d_r(\G)(s)&=\G(1,s),  s \in [0,1],\\
\d_d(\G)(t)&=\G(t,0), t \in [0,1],
&\d_u(\G)(t)&=\G(t,1), t \in [0,1].
\end{aligned}$$ Note that the paths $\d_l(\G)$ and $\d_r(\G)$ are necessarily constant, thus each of them can be identified with a point of $M$. In addition, given a 2-path $\G$ then the 1-paths $\d_u(\G)$ and $\d_d(\G)$ have the same initial and end points. If $x$ is a point of $M$ the constant 1- and 2-paths with value $x$ are both denoted by $x$.

If $\G$ and $\G'$ are 2-paths such that $\d_r(\G)=\d_l(\G')$ their horizontal concatenation $\G \circ_h \G'$ is defined in the obvious way, in other words:

$$\big (\G \circ_h \G' \big )(t,s)=\left \{ \begin{CD} \G(2t,s), \textrm{ if }t \in [0,1/2] \textrm{ and }  s \in [0,1] \\ \G'(2t-1,s), \textrm{ if } t \in [1/2,1] \textrm{ and }  s \in [0,1] \end{CD} \right.$$ Similarly, if $\d_u(\G)=\d_d(\G')$ we can define a vertical concatenation $\G \circ_v \G'$ as: $$\big(\G \circ_v \G' \big)(t,s)=\left \{ \begin{CD} \G(t,2s), \textrm{ if }s \in [0,1/2]  \textrm{ and }  t \in [0,1]\\ \G'(t,2s-1), \textrm{ if } s \in [1/2,1]  \textrm{ and }  t \in [0,1] \end{CD} \right.$$

We will also represent the $2$-paths $\G$ of $M$ in the following suggestive way: $$\G=\begin{CD} \d_u(\G )\\ @AA\G A \\ \d_d(\G) \end{CD}$$ In this notation, the vertical concatenation of two $2$-paths $\G$ and $\G'$ with $\d_d(\G')=\d_u(\G)$ can be represented as:

$$\G \circ_v \G'\quad=\quad \begin{CD} \d_u(\G\circ_v \G' )\\ @AA\G\circ_v \G' A \\ \d_d(\G\circ_v \G' ) \end{CD}\quad =\quad \begin{CD} \d_u(\G' )\\ @AA\G' A\\  \d_d(\G')=\d_u(\G)\\ @AA\G A\\ \d_d(\G) \end{CD}$$

::: Definition
Two 1-paths $\f$ and $\g$ are said to be rank-1 homotopic (and we write $\f\cong_1 \g$) if there exists a 2-path $\G$ such that:

1.  $\d_u(\G)=\g$ and $\d_d(\G)=\f$.

2.  $\Rank({{\EuScript{D}}}_{v} \G) \leq 1, \forall v \in [0,1]^2.$

Here ${\EuScript{D}}$ denotes derivative.
:::

In particular, if $\g$ and $\f$ are rank-1 homotopic, then they have the same initial and end-points. Note also that rank-1 homotopy is an equivalence relation. Given a 1-path $\g$, the equivalence class to which it belongs is denoted by $[\g]$. Rank-1 homotopy is one of a number of notions of "thin" equivalence between paths or loops, and was introduced in [@CP], following a suggestion by A. Machado.

We denote the set of $1$-paths of $M$ by $S_1(M)$. The quotient of $S_1(M)$ by the relation of thin homotopy is denoted by $\S_1(M)$. We call the elements of $\S_1(M)$ 1-tracks. The concatenation of $1$-tracks together with the source and target maps $\sigma, \tau \colon \S_1(M) \to M$, defines a groupoid $\Sc_1(M)$ whose set of morphisms is $\S_1(M)$ and whose set of objects is $M$.

::: Definition
Let $* \in M$ be a base point. The group $\pi_1^1(M,*)$ is defined as being the set of 1-tracks $[\g]\in \S_1(M)$ starting and ending at $*$, with the group operation being the concatenation of paths.
:::

It is easy to see directly that $\pi_1^1(M,*)$, a thin analogue of $\pi_1(M)$, is indeed a group. See [@CP; @MP] for details.
