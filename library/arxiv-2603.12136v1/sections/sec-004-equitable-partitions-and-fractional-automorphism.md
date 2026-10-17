---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-004-equitable-partitions-and-fractional-automorphism
section_title: "Equitable partitions and fractional automorphisms"
section_number: null
pages: 6-8
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 1.0
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
First, we introduce equitable partitions of linear programs as presented in [@Grohe2014]. Given a matrix $A\in \R^{V\times W}$, DRCR iteratively computes partitions $\MP_i$ and $\MQ_i$ of $V$ and $W$, the rows and columns of $A$. Let $\MP_0 = \{ V\}$ and $\MQ_0 = \{ W\}$. A partition $(\MP,\MQ)$ of the rows and columns of $A$ is said to be *equitable* if for all $P\in \MP,Q\in\MQ$ it holds that $$\begin{aligned}
    \label{eq_folding_row_sums}
    \sum_{w\in Q} A_{v,w} &= \sum_{w\in Q} A_{v',w}\text{ for all } v,v'\in P\\
    \label{eq_folding_col_sums}
    \sum_{v\in P} A_{v,w} &= \sum_{v\in P} A_{v,w'}\text{ for all } w,w'\in Q.
\end{aligned}$$ In words, for every block of $A$ defined by $P,Q$, the row sums and columns sums restricted to elements in the block must be equal. For a vector $b\in \R^V$, we similarly say that $\MP$ is an *equitable partition* of $b$ if $b_v = b_{v'}$ holds for all $v,v'\in P$ for all $P\in \MP$. If for $(P,Q)\in \MP \times \MQ$ both [\[eq_folding_row_sums\]](#eq_folding_row_sums){reference-type="eqref" reference="eq_folding_row_sums"} and [\[eq_folding_col_sums\]](#eq_folding_col_sums){reference-type="eqref" reference="eq_folding_col_sums"} hold, we also say that $(P,Q)$ defines an *equitable block* of $A$. A partition $\MP_1$ is said to *refine* a partition $\MP_2$ if for every $P_1\in \MP_1$ there exists some $P_2\in \MP_2$ such that $P_1\subseteq P_2$. Color refinement works by iteratively refining $\MP_i$ and $\MQ_i$, by splitting any classes $P\in \MP_i$ or $Q\in\MQ_i$ into multiple classes in $\MP_{i+1}$ and $\MQ_{i+1}$ if they do not satisfy the conditions [\[eq_folding_row_sums\]](#eq_folding_row_sums){reference-type="eqref" reference="eq_folding_row_sums"} and [\[eq_folding_col_sums\]](#eq_folding_col_sums){reference-type="eqref" reference="eq_folding_col_sums"} respectively. For some iteration $i$, this iterative process satisfies $\MP_i = \MP_{i+1}$ and $\MQ_i = \MQ_{i+1}$. For this $i$, the partition $(\MP_\infty,\MQ_\infty) \coloneqq (\MP_i,\MQ_i)$ is known as the *coarsest equitable partition* of $A$. The authors of [@Grohe2014] adapt the well-known fast color refinement algorithm by Paige and Tarjan [@Paige1987], that is based on ideas by Hopcroft [@Hopcroft1971], to compute the coarsest equitable partition. For $n = |V| + |W|$ and the total bitlength $m$ of the entries of $A$, they show that one can compute the coarsest equitable partition in $\orderO((n+m)\log n)$ time.\
Given a partition $\MP$ of a set $V$, its *partition matrix* is denoted by $\Pi_{\MP}\in \{0,1\}^{V\times\MP}$, for which $(\Pi)_{vP} = 1 \iff v\in P$ holds for all $v\in V$ and $P\in \MP$. A *scaled partition matrix* $\widetilde{\Pi_\MP}$ is a normalized partition matrix defined such that $(\widetilde{\Pi_\MP})_{vP} = \begin{cases} \frac{1}{|P|} \text{ if $v\in P$} \\
0\text{ otherwise}\end{cases}$ holds for all $v\in V$ and $P\in \MP$. summarizes a few identities for partition matrices and scaled partition matrices that are established and used in [@Grohe2014].

::: proposition
[]{#thm_part_id label="thm_part_id"} Given a partition $\MP$ of a set $V$, the following hold:

1.  []{#thm_part_id_id label="thm_part_id_id"}$\transpose{\widetilde{\Pi_\MP}} \Pi_\MP = \transpose{\Pi}_\MP \widetilde{\Pi_\MP} = I_{\MP\times \MP}$.

2.  []{#thm_part_id_ds label="thm_part_id_ds"}For $v,v'\in V$, $(\widetilde{\Pi_\MP}\transpose{\Pi_\MP})_{v,v'} = (\Pi_\MP \transpose{\widetilde{\Pi_\MP}})_{v',v} = \begin{cases}
            \frac{1}{|P|} \text{ if $v,v'\in P$ for some $P\in \MP$}\\
            0 \text{ otherwise.}
        \end{cases}$

3.  []{#thm_part_id_equitable label="thm_part_id_equitable"} If $\MP$ is an equitable partition of $b\in \R^V$, then $b= \widetilde{\Pi_{\MP}} \transpose{\Pi_{\MP}} b = \Pi_\MP \transpose{\widetilde{\Pi_\MP}}b$ holds.
:::

::: proof
*Proof.* For [\[thm_part_id_id\]](#thm_part_id_id){reference-type="ref" reference="thm_part_id_id"}, consider any $P,P'\in \MP$ and note that $(\transpose{\widetilde{\Pi_\MP}} \Pi_\MP)_{P,P'} = \begin{cases}
    \sum_{v\in P} \frac{1}{|P|} \text{ if $P=P'$}\\
    0 \text{ otherwise}
\end{cases} = I_{\MP\times\MP}$ holds. The identity in [\[thm_part_id_id\]](#thm_part_id_id){reference-type="ref" reference="thm_part_id_id"} follows since $I_{\MP\times \MP} = \transpose{(\transpose{\widetilde{\Pi_\MP}} \Pi_\MP)} = \transpose{\Pi}_\MP \widetilde{\Pi_\MP}$ holds. The proof of [\[thm_part_id_ds\]](#thm_part_id_ds){reference-type="ref" reference="thm_part_id_ds"} follows by the definition of matrix transpose and multiplication. For [\[thm_part_id_equitable\]](#thm_part_id_equitable){reference-type="ref" reference="thm_part_id_equitable"} we have for $v\in V$ and $P\in \MP$ such that $v\in P$ that $(\transpose{\widetilde{\Pi_\MP}} \Pi_\MP b)_v = \sum_{v'\in P} \frac{1}{|P|} b_{v'} = b_v$, where the last equality holds since $\MP$ is an equitable partition of $b$, which implies that $b_v = b_{v'}$ holds for all $v'\in P$. ◻
:::

A matrix $A\in \R^{V\times W}$ is said to be *stochastic* if it is nonnegative and $\sum_{w\in W} A_{v,w} = 1$ for all $v\in V$, and it is *doubly stochastic* if both $A$ and $\transpose{A}$ are stochastic. For a matrix $A\in \R^{V\times W}$, a pair $(X,Y) \in \R^{V\times V} \times \R^{W\times W}$ of doubly stochastic matrices is said to be a *fractional automorphism* of $A$ if $XA = AY$ holds. One of the key insights made by the authors of [@Grohe2014] is given in [\[thm_frac_aut_equitable_partition\]](#thm_frac_aut_equitable_partition){reference-type="ref" reference="thm_frac_aut_equitable_partition"}, and relates fractional automorphisms of $A$ to its equitable partitions.

::: proposition
([@Grohe2014]) []{#thm_frac_aut_equitable_partition label="thm_frac_aut_equitable_partition"} If $(\MP,\MQ)$ is an equitable partition of a matrix $A\in \R^{V\times W}$, then $(\Pi_\MP \transpose{\widetilde{\Pi_\MP}}, \Pi_\MQ \transpose{\widetilde{\Pi_\MQ}})$ is a fractional automorphism of $A$.
:::

In [\[thm_frac_aut_equitable_partition\]](#thm_frac_aut_equitable_partition){reference-type="ref" reference="thm_frac_aut_equitable_partition"}, it can be easily checked that $\Pi_\MP \transpose{\widetilde{\Pi_\MP}}$ and $\Pi_\MQ \transpose{\widetilde{\Pi_\MQ}}$ are both doubly stochastic due to [\[thm_part_id\]](#thm_part_id){reference-type="ref" reference="thm_part_id"}[\[thm_part_id_ds\]](#thm_part_id_ds){reference-type="ref" reference="thm_part_id_ds"}. From [\[thm_part_id\]](#thm_part_id){reference-type="ref" reference="thm_part_id"}[\[thm_part_id_ds\]](#thm_part_id_ds){reference-type="ref" reference="thm_part_id_ds"} and [\[thm_frac_aut_equitable_partition\]](#thm_frac_aut_equitable_partition){reference-type="ref" reference="thm_frac_aut_equitable_partition"} it also follows that if $(\MP,\MQ)$ is an equitable partition, that $(\widetilde{\Pi_\MP} \transpose{\Pi_\MP}, \widetilde{\Pi_\MQ} \transpose{\Pi_\MQ})$ is a fractional automorphism of $A$.
