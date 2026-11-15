---
doc_id: arxiv-2205.01282v2
doc_title: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES"
section_id: sec-004-22-the-inverse-matrix-of-the-linking-matrix
section_title: "The inverse matrix of the linking matrix"
section_number: 2.2
pages: 4-5
source_pdf: 2205.01282v2.pdf
source_sha256: 00f656afa60db838
toc_source: outline
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 0.984
doc_brief: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES — In this paper, we prove a conjecture by Gukov–Pei–Putrov–Vafa for a wide class of plumbed 3-manifolds."
---
[]{#subsec:S label="subsec:S"}

In this subsection, we calculate the inverse matrix of the linking matrix.

Let $S \in \Aut(\Q^{V_{\ge 2}}) \cap \End(\Z^{V_{\ge 2}})$ be the $V_{\ge 2} \times V_{\ge 2}$ submatrix of $-W^{-1} \in \Aut(\Q^V)$. Here we recall $V_{\ge 2} = \{ v \in V \mid \deg v \ge 2 \}$. We also denote $T \coloneqq  -W_1^{-1} W_{1, \ge 2}$. Here we remark that $S$ is positive definite since $W$ is negative definite.

The inverse matrices $W^{-1}$ and $S^{-1}$ have the following properties.

::: prop
[]{#prop:S label="prop:S"}

1.  []{#item:prop:S1 label="item:prop:S1"} $$-W^{-1} = \pmat{T \\ I} S \pmat{{}^t\!T & I} - \pmat{W_1^{-1} & \\ & O}.$$

2.  []{#item:prop:S2 label="item:prop:S2"} $$\det S =  \det W \prod_{i \in V_1} w_i
            = \prod_{i \in V_1} \abs{w_i}.$$

3.  []{#item:prop:S3 label="item:prop:S3"} $$S^{-1} = -W_{\ge 2} + \mathop{\mathrm{diag}}\left( \sum_{i \in \overline{v}} \frac{1}{w_i} \right)_{v \in V_{\ge 2}}.$$ Here, we denote $\mathop{\mathrm{diag}}(a_v)_{v \in V_{\ge 2}}$ the diagonal matrix whose $(v, v)$-component is $a_v$.

4.  []{#item:prop:S4 label="item:prop:S4"} For distinct vertices $v, v' \in V_{\ge 2}$, the $(v, v)$-component of $S$ is in $M_v \Z$ and the $(v, v')$-component of $S$ is in $M_v M_{v'} \Z$.

5.  []{#item:prop:S5 label="item:prop:S5"}

    $$S^{-1} \left(\Z^{V_{\ge 2}} \right) = \bigoplus_{v \in V_{\ge 2}} \frac{1}{M_v} \Z \subset \Q^{V_{\ge 2}}.$$
:::

To prove this proposition, we prepare a lemma for the inverse matrices of symmetric block matrices.

::: lem
[]{#lem:block_matrix label="lem:block_matrix"} For a symmetric block matrix $$X = \pmat{A & B \\ {}^t\!B & C} \in \GL_{m+n} (\bbC)$$ such that $A \in \GL_m(\bbC)$ and $C \in \GL_n(\bbC)$ be symmetric matrices and $B \in \Mat_{m, n}(\bbC)$, let $$S \coloneqq (C - {}^t\!B A^{-1} B)^{-1} \in \GL_n(\bbC), \quad
    T \coloneqq -A^{-1} B \in \Mat_{m, n}(\bbC).$$ Then, it holds that $$X^{-1} = \pmat{T \\ I} S \pmat{{}^t\!T & I} + \pmat{A^{-1} & \\ & O}, \quad
    \det S = \frac{\det A}{\det X}.$$ In particular, $S$ is the $n \times n$ bottom right submatrix of $X^{-1}$.
:::

::: proof
*Proof.* The first equality follows from $$X \left( \pmat{T \\ I} S \pmat{{}^t\!T & I} + \pmat{A^{-1} & \\ & O} \right) 
    = \pmat{ (AT+B) S {}^t\!T + I & (AT+B)S \\ ({}^t\!B T + C)S{}^t\!T + {}^t\!B A^{-1} & ({}^t\!B T + C)S }$$ and the second equality follows from $$X = \pmat{ I &  \\  -{}^t\!T & I} \pmat{A & \\ &S^{-1}} \pmat{I & -T \\ & I}.$$ ◻
:::

Here we remark that [\[lem:block_matrix\]](#lem:block_matrix){reference-type="ref" reference="lem:block_matrix"} is a generalisation of the completing the square $ax^2 + bx + c = a(x + b/2a)^2 - (b^2 - 4ac)/4a$ for symmetric block matrices.

::: proof
*Proof of $\cref{prop:S}$.* We obtain [\[item:prop:S1\]](#item:prop:S1){reference-type="ref" reference="item:prop:S1"} and the equalities $$S^{-1} = -W_{\ge 2} + W_{\ge 2, 1} W_1^{-1} W_{1, \ge 2}, \quad
    \det S = \frac{\det W_1}{\det W}$$ by applying [\[lem:block_matrix\]](#lem:block_matrix){reference-type="ref" reference="lem:block_matrix"} for the block matrix $$W = \pmat{W_1 & W_{1, \ge 2} \\ W_{\ge 2, 1} & W_{\ge 2}} \in \GL_{m+n} (\Z).$$ Since $\det W \in \{ \pm 1 \}, W_1 = \mathop{\mathrm{diag}}(w_i)_{i \in V_1}$, and $\det S > 0$, we get [\[item:prop:S2\]](#item:prop:S2){reference-type="ref" reference="item:prop:S2"}. [\[item:prop:S3\]](#item:prop:S3){reference-type="ref" reference="item:prop:S3"} follows from the fact that the $(v, v')$-component of $W_{\ge 2, 1} W_1^{-1} W_{1, \ge 2}$ is $$\sum_{i \in V_1, \, \{ i, v \}, \{ i, v' \} \in E} \frac{1}{w_i} = \delta_{v, v'} \sum_{i \in V_1, \, \{ i, v \} \in E} \frac{1}{w_i}.$$ We prove [\[item:prop:S4\]](#item:prop:S4){reference-type="ref" reference="item:prop:S4"}. By [\[item:prop:S3\]](#item:prop:S3){reference-type="ref" reference="item:prop:S3"}, the $(v, v')$-cofactor of $S^{-1}$ is an element of $\left( \prod_{v^{\prime \prime} \in V_{\ge 2} \smallsetminus \{ v, v' \}} 1/M_{v^{\prime \prime}} \right) \Z$. Since $\det S =  \pm \prod_{v \in V_{\ge 2}} M_v$ by [\[item:prop:S3\]](#item:prop:S3){reference-type="ref" reference="item:prop:S3"}, we obtain the claim. Finally, we prove [\[item:prop:S5\]](#item:prop:S5){reference-type="ref" reference="item:prop:S5"}. Let $W'_{\ge 2} \coloneqq \mathop{\mathrm{diag}}(M_v)_{v \in V_{\ge 2}} \in \Aut(\Q^{\abs{V_{\ge 2}}})$. It suffices to show $S^{-1} W'_{\ge 2} \in \Aut(\Q^{\abs{V_{\ge 2}}})$. Since $\det S = \pm \det W'_{\ge 2}$, we need only check that each component of $S^{-1} W'_{\ge 2}$ is an integer, which follows from [\[item:prop:S3\]](#item:prop:S3){reference-type="ref" reference="item:prop:S3"}. ◻
:::
