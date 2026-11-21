---
doc_id: arxiv-2205.01282v2
doc_title: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES"
section_id: sec-003-21-notations-for-graphs
section_title: "Notations for graphs"
section_number: 2.1
pages: 3-4
source_pdf: 2205.01282v2.pdf
source_sha256: 00f656afa60db838
toc_source: outline
text_source: latex
latex_prose_ratio: 0.823
latex_coverage_ratio: 0.97
doc_brief: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES — In this paper, we prove a conjecture by Gukov–Pei–Putrov–Vafa for a wide class of plumbed 3-manifolds."
---
[]{#subsec:graph label="subsec:graph"}

In this subsection, we prepare settings for graphs. As in [\[sec:intro\]](#sec:intro){reference-type="ref" reference="sec:intro"}, let $\Gamma = (V, E, (w_v)_{v \in V})$ be a plumbing graph and $W$ be its linking matrix such that it is negative definite and $\det W = \pm 1$. Here we consider the edge set $E$ as the subset of $\{ \{ v, v' \} \mid v, v' \in V \}$. We identify $M_{\abs{V}}(\Z)$ and $\End(\Z^V)$ and consider $W$ as the element of $\End(\Z^V)$. We remark that $w_v \in \Z_{<0}$ for any vertex $v \in V$.

For two plumbing graphs $\Gamma$ and $\Gamma'$, Neumann ([@Neumann_Lecture Proposition 2.2], [@Neumann_work Theorem 3.1]) proved that two $3$-manifolds $M(\Gamma)$ and $M(\Gamma')$ are homeomorphic if and only if $\Gamma$ and $\Gamma'$ are related by Neumann moves shown in [1](#fig:Neumann){reference-type="ref" reference="fig:Neumann"}. Thus, we can assume $w_i \le -2$ for a vertex $i$ with $\deg(i) = 1$.

<figure id="fig:Neumann">

<figcaption>Neumann moves</figcaption>
</figure>

For a positive integer $d$, let $$V_d \coloneqq \{ v \in V \mid \deg(v) = d \}, \quad
V_{\ge d} \coloneqq \{ v \in V \mid \deg(v) \ge d \}.$$ Let $W_d \in \End(\Z^{V_d})$ and $W_{\ge d} \in \End(\Z^{V_{\ge d}})$ be the submatrices of $W$ with $V_d \times V_d$ and $V_{\ge d} \times V_{\ge d}$ components respectively. Moreover, for a positive integer $e$, let $W_{d, \ge e} \in \Hom(\Z^{V_{\ge e}}, \Z^{V_d})$ and $W_{\ge d, e} \in  \Hom(\Z^{V_e}, \Z^{V_{\ge d}})$ be the submatrices of $W$ with $V_d \times V_{\ge e}$ and $V_{\ge d} \times V_e$ components respectively.

We need to focus on vertices with degree $1$ to calculate WRT invariants and homological blocks. For this reason, we define $$\overline{v} \coloneqq \{ i \in V_1 \mid \{ i, v \} \in E \}, \quad
M_v \coloneqq \prod_{i \in \overline{v}} w_i$$ for each vertex $v \in V_{\ge 2}$. Here we define $M_v \coloneqq 1$ if $\overline{v} = \emptyset$.

The condition $\det W = \pm 1$ implies the following lemma, which Akihito Mori told the author.

::: lem
[]{#lem:coprime label="lem:coprime"} For a vertex $v \in V_{\ge 2} = \{ v \in V \mid \deg v \ge 2 \}$ and distinct vertices $i, j \in \overline{v}$, it holds that $\gcd(w_i, w_j) = 1$.
:::

::: proof
*Proof.* Let $\{ e_{v} \}_{v \in V}$ be the standard basis of $\R^V$. Since $$W e_i - W e_j 
    =
    (e_{v} + w_i e_i) - (e_{v} + w_j e_j)
    =
    w_i e_i - w_j e_j,$$ $\gcd(w_i, w_j)$ divides $\det W = \pm 1$. ◻
:::
