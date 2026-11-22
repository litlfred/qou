---
doc_id: arxiv-0710.4310v2
doc_title: "On Two-Dimensional Holonomy"
section_id: sec-010-2-tracks
section_title: "2-Tracks"
section_number: null
pages: 14-14
source_pdf: 0710.4310v2.pdf
source_sha256: 9a7757f998b7f680
toc_source: outline
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 1.0
doc_brief: "On Two-Dimensional Holonomy — We deﬁne the thin fundamental categorical group P2(M, ∗) of a based smooth manifold (M, ∗) as the categorical group whose objects are rank-1 homotopy classes of based"
---
[]{#2-Tracks label="2-Tracks"}

::: Definition
[]{#thin2 label="thin2"}

Two 2-paths $\G$ and $\G'$ are said to be rank-2 homotopic (and we write $\G\cong_2 \G'$) if there exists a smooth map ${J}\colon [0,1]^2 \times [0,1] \to M$ such that:

1.  $J(t,s,0)=\G(t,s),\, J(t,s,1)=\G'(t,s)$ for $s,t\in [0,1]$.

2.  ${J}$ is constant over $\{0\} \times [0,1]^2$ and $\{1\} \times [0,1]^2$.

3.  Over $[0,1] \times \{0\} \times [0,1]$ the map ${J} \colon [0,1]^2 \times [0,1] \to M$ restricts to a rank-1 homotopy $\d_d(\G) \to \d_d(\G')$.

4.  ${J}$ restricts to a rank-1 homotopy $\d_u(\G) \to \d_u(\G')$ over $[0,1] \times \{1\} \times [0,1]$.

5.  There exists an $\epsilon >0$ such that $J(t,s,x)={J}(t,s,0)$ if $x\leq \epsilon$ and $s,t \in [0,1]$, and analogously for all the other faces of $[0,1]^3$. We will denote this condition as saying that $J$ has a product structure close to the boundary of $[0,1]^3$.

6.  $\Rank ( {{\EuScript{D}}}_{v} {J}) \leq 2$ for any $v \in {[0,1]}^3$.
:::

Note that rank-2 homotopy is an equivalence relation. To prove transitivity we need to use the penultimate condition of the previous definition. We denote by $S_2(M)$ the set of all 2-paths of $M$. The quotient of $S_2(M)$ by the relation of rank-2 homotopy is denoted by $\S_2(M)$. We call the elements of $\S_2(M)$ 2-tracks. If $\G \in S_2(M)$, we denote the equivalence class in $\S_2(M)$ to which $\G$ belongs by $[\G]$.
