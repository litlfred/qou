---
doc_id: arxiv-2603.12136v1
doc_title: "Folding Mixed-Integer Linear Programs and Reflection Symmetries"
section_id: sec-009-equitable-partitions-of-split-reformulations
section_title: "Equitable partitions of split reformulations"
section_number: null
pages: 16-22
source_pdf: 2603.12136v1.pdf
source_sha256: e9c50616344b24e0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 1.0
doc_brief: "Folding Mixed-Integer Linear Programs and Reflection Symmetries — For mixed-integer linear programming and linear programming it is well known that symmetries can have a negative impact on the"
---
Throughout this section, we investigate the structure of equitable partitions of the split reformulation $F_S(A,b,\ell,u,c)$ for an arbitrary linear program $F(A,b,\ell,u,c)$ with $\ell \leq \zerovec$ and $u\geq \zerovec$.

Recall that for a split reformulation, its variable index sets $\widehat{W} = \widehat{W}^+ \cup \widehat{W}^-$ and $\widehat{V} = \widehat{V}^+ \cup \widehat{V}^-$ correspond to the original and negated variables and constraints, respectively. For $x\in \{-1,1\}$, we will use the synonyms $\widehat{V}^x\coloneqq \begin{cases}
    \widehat{V}^+ \text{ if $x= 1$}\\
    \widehat{V}^- \text{ if $x=-1$}\\
\end{cases}$ and $\widehat{W}^x\coloneqq  \begin{cases}
    \widehat{W}^+ \text{ if $x= 1$}\\
    \widehat{W}^- \text{ if $x=-1$}\\
\end{cases}$ to denote the corresponding signed sets and for $v\in V$ ($w\in W$) we similarly use $v^x$ ($w^x$) to indicate that $v$ lies in $\widehat{V}^x$ ($\widehat{W}^x$). For any $P\subseteq V$ and $\gamma \in \{-1,1\}^{P}$, and, we use $P^\gamma \coloneqq \{ v^{\gamma_v} \in \widehat{V}^{\gamma_v} \mid v\in P \}$ to denote the signed set of indices corresponding in $\widehat{V}^+$ (if $\gamma_v = 1)$ and $\widehat{V}^-$ (if $\gamma_v = -1$). For example, for $P=\{v_1,v_2,v_3\}$ and $\gamma \coloneqq \begin{bmatrix}
    \gamma_{v_1} & \gamma_{v_2} & \gamma_{v_3}
\end{bmatrix} = \begin{bmatrix}
    1 & -1 & -1
\end{bmatrix}$, we would have that $P^\gamma = \{v^+_1, v^-_2,v^-_3\}$ and that $P^{-\gamma} = \{v^-_1,v^+_2,v^+_3\}$, where $v^+_1,v^+_2,v^+_3 \in \widehat{V}^+_2$ and $v^-_1,v^-_2,v^-_3\in \widehat{V}^-_2$. Similarly, for any $Q\subseteq W$ and $\lambda \in \{-1,1\}^{Q}$, we define $Q^\lambda \coloneqq \{w^{\lambda_w} \in \widehat{W}^{\lambda_w} \mid w\in Q\}$.\
Then, we consider the structure of equitable partitions $(\widehat{\MP},\widehat{\MQ})$ of $F_S(A,b,\ell,u,c)$ in further detail. These equitable partitions have many symmetries that are a result of the redundancies introduced by the split reformulation. One property that will be important in this context, is the *polarity* of parts $\widehat{P}\in \widehat{\MP}$. If for some $v\in V$, both $v^+\in \widehat{P}$ and $v^-\in \widehat{P}$ hold then $\widehat{P}$ is said to be *bipolar*. If $\widehat{P}\subseteq \widehat{V}$ is not bipolar, then $|\widehat{P}\cap \{v^+,v^-\}|\leq 1$ holds for all $v\in V$ and we say it is *unipolar*. Note that for each unipolar part $\widehat{P}$ there exists a part $P\subseteq V$ and $\gamma\in\{-1,1\}^V$ such that $\widehat{P} = P^\gamma$ holds. Similarly, $\widehat{Q}\subseteq \widehat{W}$ is *bipolar* if there exists some $w\in W$ such that $w^+\in \widehat{Q}$ and $w^-\in Q$ hold, and $\widehat{Q}$ is said to be *unipolar* if $|\widehat{Q}\cap \{w^+,w^-\}|\leq 1$ holds for all $w\in W$. If $\widehat{Q}$ is unipolar, then there exists $Q\subseteq W$ and $\lambda\in \{-1,1\}^W$ such that $\widehat{Q} = Q^\lambda$ holds. In [\[def_symmetric\]](#def_symmetric){reference-type="ref" reference="def_symmetric"}, we define the symmetric structure of equitable partitions of the split reformulation $F_S(A,b,\ell,u,c)$ of any linear program $F(A,b,\ell,u,c)$ with row and column indices $V$ and $W$, respectively. The sets $\widehat{V}$ and $\widehat{W}$ are the row and column indices of $F_S(A,b,\ell,u,c)$ as defined in [\[def_split_reform\]](#def_split_reform){reference-type="ref" reference="def_split_reform"}.

::: definition
[]{#def_symmetric label="def_symmetric"} Let $(\widehat{\MP},\widehat{\MQ})$ be a partition of $\widehat{V}\times \widehat{W}$. We say that $(\widehat{\MP},\widehat{\MQ})$ is *symmetric* if the following hold.

1.  for every unipolar part $P\in \widehat{\MP}$ such that $P =P^\gamma$ holds, $P^{-\gamma} \in \widehat{\MP}$ holds too. []{#def_symmetric_row_unipolar label="def_symmetric_row_unipolar"}

2.  for every bipolar part $P\in \widehat{\MP}$ and any $v\in V$, $P$ either contains both $v^+$ and $v^-$ or none. []{#def_symmetric_row_bipolar label="def_symmetric_row_bipolar"}

3.  for every unipolar part $Q\in \widehat{\MQ}$ such that $Q =Q^\lambda$ holds, $Q^{-\lambda} \in \widehat{\MQ}$ holds too. []{#def_symmetric_col_unipolar label="def_symmetric_col_unipolar"}

4.  for every bipolar part $Q\in \widehat{\MQ}$ and any $w\in W$, $Q$ either contains both $w^+$ and $w^-$ or none. []{#def_symmetric_col_bipolar label="def_symmetric_col_bipolar"}
:::

For a symmetric equitable partition $(\widehat{\MP},\widehat{\MQ})$ of $F_S(A,b,\ell,u,c)$, we use $\widehat{\MP}_B \coloneqq \{P \in \widehat{\MP} \mid P \text{ is bipolar}\}$ and $\widehat{\MP}_U \coloneqq \{P\in \widehat{\MP} \mid P \text{ is unipolar}\}$ and note that $\widehat{\MP}_U$ and $\widehat{\MP}_B$ are a disjoint partition of $\widehat{\MP}$. Similarly, we define that $\widehat{\MQ}_B \coloneqq \{Q \in \widehat{\MQ} \mid Q \text{ is bipolar}\}$ and $\widehat{\MQ}_U \coloneqq \{Q \in\widehat{\MQ} \mid Q \text{ is unipolar}\}$, which also partitions $\widehat{Q}$ . Furthermore, we use $\widehat{V}_U \coloneqq \bigcup_{P\in \widehat{\MP}_U} P$, $\widehat{V}_B \coloneqq \bigcup_{P\in \widehat{\MP}_B} P$, $\widehat{W}_U \coloneqq \bigcup_{Q\in \widehat{\MQ}_U} Q$ and $\widehat{W}_B \coloneqq \bigcup_{Q\in \widehat{\MQ}_B} Q$ for the corresponding partitioned subsets of $\widehat{V}$ and $\widehat{W}$. To denote the corresponding sets in $V$ and $W$ we use $V_U \coloneqq \{v \in V \mid \{v^+,v^-\}\cap \widehat{V}_U\neq\emptyset\}$, $V_B \coloneqq \{v \in V \mid \{v^+,v^-\}\subseteq \widehat{V}_B\}$, $W_U \coloneqq \{w \in W \mid \{w^+,w^-\}\cap \widehat{W}_U\neq\emptyset\}$ and $W_B \coloneqq \{w \in W \mid \{w^+,w^-\}\subseteq\widehat{W}_B\}$ .

The notion of bipolar and unipolar parts in [\[def_symmetric\]](#def_symmetric){reference-type="ref" reference="def_symmetric"} is very similar to an observation by Bödi, Herr and Joswig [@Bodi2013], who show that the orbits of reflection symmetry groups are either unipolar or bipolar, where bipolar orbits must consist of only pairs $w^+,w^-$ for some subset of $W$. Similarly, we will show that the equitable partitions of $F_S(A,b,\ell,u,c)$, that the associated equitable partitions are indeed symmetric and satisfy [\[def_symmetric\]](#def_symmetric){reference-type="ref" reference="def_symmetric"}.\
Next, we show one important property of symmetric partitions: bipolar parts correspond to zero row and column sums.

::: lemma
[]{#thm_bipolar_symmetric_sum label="thm_bipolar_symmetric_sum"} Let $(\widehat{\MP},\widehat{\MQ})$ be any partition of $F_S(A,b,\ell,u,c)$ and let $(P',Q') \in \widehat{\MP} \times \widehat{\MQ}$. Then, the following hold:

1.  []{#thm_bipolar_symmetric_sum_column label="thm_bipolar_symmetric_sum_column"} If $P' = P^\onevec \cup P^{-\onevec}$ holds for some set $P\subseteq V$, then $\sum_{v\in P'} \widehat{M}_{v,w} = 0$ holds for all $w\in W$.

2.  []{#thm_bipolar_symmetric_sum_row label="thm_bipolar_symmetric_sum_row"} If $Q' = Q^\onevec \cup Q^{-\onevec}$ holds for some set $Q\subseteq W$, then $\sum_{w\in Q'} \widehat{M}_{v,w} = 0$ holds for all $v\in V$.
:::

::: proof
*Proof.* To prove [\[thm_bipolar_symmetric_sum_column\]](#thm_bipolar_symmetric_sum_column){reference-type="ref" reference="thm_bipolar_symmetric_sum_column"}, consider any $w\in W$. Then, we have that $$\sum_{v\in P'} \widehat{M}_{v,w} = \sum_{v^+\in P^{\onevec}} \widehat{M}_{v^+,w} + \sum_{v^-\in P^{-\onevec}} \widehat{M}_{v^-,w} = \sum_{v\in P} A_{v,w} + \sum_{v\in P} -A_{v,w} = 0,$$ where the first equality is given by the condition. The second equality can be observed through case distinction whether $w\in W^+$ or $w\in W^-$ holds. If $w\in W^+$ holds then by definition of $\widehat{M}$ we have $\widehat{M}_{v^+,w} = A_{v,w}$ and $\widehat{M}_{v^-,w} = -A_{v,w}$. For $w\in W^-$ we have $\widehat{M}_{v^+,w} = -A_{v,w}$ and $\widehat{M}_{v^-,w} = A_{v,w}$. In both cases, the equality follows.

The proof for [\[thm_bipolar_symmetric_sum_row\]](#thm_bipolar_symmetric_sum_row){reference-type="ref" reference="thm_bipolar_symmetric_sum_row"} is similar, where we have for all $v\in V$ that: $$\sum_{w\in Q'} \widehat{M}_{v,w} = \sum_{w^+\in Q^{\onevec}} \widehat{M}_{v,w^+} + \sum_{w^-\in Q^{-\onevec}} \widehat{M}_{v,w^-} = \sum_{w\in Q} A_{v,w} + \sum_{w\in Q} -A_{v,w} = 0.$$ ◻
:::

::: corollary
[]{#thm_bipolar_symmetric_equitable_sum label="thm_bipolar_symmetric_equitable_sum"} Let $(\widehat{\MP},\widehat{\MQ})$ be any symmetric equitable partition of $F_S(A,b,\ell,u,c)$ and let $(P,Q) \in (\widehat{\MP},\widehat{\MQ})$. If at least one of $P$ and $Q$ is bipolar, then $\sum_{v\in P} \widehat{M}_{v,w} = 0$ holds for all $w\in Q$ and $\sum_{w\in Q} \widehat{M}_{v,w} = 0$ holds for all $v\in P$.
:::

::: proof
*Proof.* We have $\sum_{v\in P} \sum_{w\in Q} \widehat{M}_{v,w} = \sum_{w\in Q} \sum_{v\in P} \widehat{M}_{v,w} = 0$, where the final equality holds by [\[thm_bipolar_symmetric_sum\]](#thm_bipolar_symmetric_sum){reference-type="ref" reference="thm_bipolar_symmetric_sum"}, since bipolarity of either $Q$ or $P$ implies that $\sum_{w\in Q} \widehat{M}_{v,w} = 0$ holds for all $v\in P$ or $\sum_{v\in P} \widehat{M}_{v,w} = 0$ holds for all $w\in Q$. By equitability of the block $(P,Q)$, the row and column sums are identical, and it follows that $\sum_{w\in Q} \widehat{M}_{v,w} = \frac{1}{|P|} \sum_{v'\in P} \sum_{w\in Q} \widehat{M}_{v',w} = 0$ holds for all $v\in P$ and $\sum_{v\in P} \widehat{M}_{v,w} = \frac{1}{|Q|} \sum_{w'\in Q} \sum_{v\in P} \widehat{M}_{v,w'} = 0$ holds for all $w'\in Q$. ◻
:::

In order to investigate symmetric equitable partitions of split reformulations, we need a key assumption that limits the structure of the equitable partitions for the split reformulation. One disadvantage of the split reformulation is that the $x^+$- and $x^-$-variables may interact in non-identical ways, which makes it tough to interpret the computed partition of $\widehat{V}$ and $\widehat{W}$ in the context of the original linear program $F(A,b,\ell,u,c)$. For example, for variables $w_1,w_2\in W$, it may be the case that there exists a part $\{w_1^+,w_1^-,w_2^+\}$ which acts identically on the whole domain of $w_1$ but only on the positive domain of $w_2$. To avoid such issues, we consider only partitions of the split reformulation such that for each part $Q\in \widehat{\MQ}$, the associated variables in $Q$ of the linear program $F(A,b,\ell,u,c)$ have identical variable bounds.

::: definition
[]{#def_part_domain_respecting label="def_part_domain_respecting"} A partition $(\widehat{\MP},\widehat{\MQ})$ of $\widehat{V} \times \widehat{W}$ is said to be *bound-respecting* if for all $Q\in \widehat{\MQ}$ and any $w^{s_1}_1,w^{s_2}_2\in Q$ we have:

1.  $\ell_{w_1} = \ell_{w_2}$ and $u_{w_1} = u_{w_2}$ if $s_1 = s_2$ holds

2.  $\ell_{w_1} = -u_{w_2}$ and $u_{w_1} = - \ell_{w_2}$ if $s_1 \neq s_2$ holds
:::

Then, we show that the split reformulation $F_S(A,b,\ell,u,c)$ admits a symmetric equitable partition in two steps. First, we show in [\[thm_initial_partition_symmetric\]](#thm_initial_partition_symmetric){reference-type="ref" reference="thm_initial_partition_symmetric"} that the initial coarsest bound-respecting equitable partition is symmetric. Second, we show in [\[thm_refinement_symmetric\]](#thm_refinement_symmetric){reference-type="ref" reference="thm_refinement_symmetric"} that any refinements of the initial partition from the constraint matrix preserve the symmetry of the partition.

::: lemma
[]{#thm_initial_partition_symmetric label="thm_initial_partition_symmetric"} Let $(\widehat{\MP},\widehat{\MQ})$ be the coarsest bound-respecting partition of $F_S(A,b,\ell,u,c)$ such that $\widehat{\MP}$ is equitable for $\widehat{b} \coloneqq \begin{bmatrix}
    b & - b
\end{bmatrix}$ and $\widehat{\MQ}$ is equitable for the $\widehat{c} \coloneqq \transpose{\begin{bmatrix}
    c & -c
\end{bmatrix}}$ and $\widehat{u} \coloneqq \transpose{\begin{bmatrix}
    u & -\ell
\end{bmatrix}}$. Then, $(\widehat{\MP},\widehat{\MQ})$ is symmetric. Moreover, $b_v = 0$ holds for all $v\in \widehat{V}_B$ and $c_w =0$ and $u_w = -\ell_w$ hold for all $w\in W_B$.
:::

::: proof
*Proof.* First, consider the coarsest equitable partition $\widehat{\MP}$ of the right-hand side $\widehat{b} \in \R^{\widehat{V}^+\cup \widehat{V}^-}$. Consider any bipolar part $P \in \widehat{\MP}$ such that for some $v \in V$, $\{v^+,v^-\} \subseteq P$ holds. Then, since $\widehat{\MP}$ is an equitable partition of $\widehat{b}$, it follows that $b_v = \widehat{b}_{v^+} = \widehat{b}_{v^-} = - b_v$ holds, which implies that $b_v = 0$. As this holds for all $v\in V$ with $b_{v} = 0$, it follows that the block $P$ in the coarsest equitable partition is exactly formed by those rows of $b$ that have right-hand side $0$, i.e. $P = \{ v^+,v^- \mid \text{ such that $b_v = 0$ for $v\in V$} \}$ is the only bipolar part in $\widehat{\MP}$. Clearly, $P$ satisfies [\[def_symmetric\]](#def_symmetric){reference-type="ref" reference="def_symmetric"}[\[def_symmetric_row_bipolar\]](#def_symmetric_row_bipolar){reference-type="ref" reference="def_symmetric_row_bipolar"}.

For any unipolar part $\widehat{P}\in \widehat{\MP}$ holds such that $\widehat{P} = P^\gamma$ for suitable $P \subseteq V$ and $\gamma \in \{-1,1\}^V$, it follows from equitability of $\widehat{\MP}$ for $\widehat{b}$ that for all $v^{\gamma}_1,v^\gamma_2\in \widehat{P}$ that $\widehat{b}_{v^\gamma_1} = \gamma_{v_1} b_{v_1} = \gamma_{v_2} b_{v_2} = \widehat{b}_{v^\gamma_2}$ holds. However, this directly implies for the set $P^{-\gamma} \subseteq \widehat{V}$ that $\widehat{b}_{v^{-\gamma}_1} = -\gamma_{v_1} b_{v_1} = -\gamma_{v_2} b_{v_2} = \widehat{b}_{v^{-\gamma}_1}$ holds, which shows that $P^{-\gamma}$ is also an equitable block. Thus, $\widehat{\MP}$ can only be the coarsest equitable partition of $\widehat{b}$ if there exists some block $\widehat{P}'$ such that $P^{-\gamma} \subseteq \widehat{P}'$. One can show using a similar argument that $P^{-\gamma} = \widehat{P}'$ holds: existence of any $v^{-\gamma}\in \widehat{P}' \setminus P^{-\gamma}$ contradicts that $\widehat{\MP}$ is the coarsest equitable partition of $\widehat{b}$ as then the part containing $v^\gamma$ can be merged with $\widehat{P}$ to form a coarser partition. Since the above reasoning holds for all unipolar blocks, it follows that [\[def_symmetric\]](#def_symmetric){reference-type="ref" reference="def_symmetric"}[\[def_symmetric_row_unipolar\]](#def_symmetric_row_unipolar){reference-type="ref" reference="def_symmetric_row_unipolar"} is satisfied.

Second, we consider the coarsest bound-respecting equitable partition $\widehat{\MQ}$ of $\widehat{c}$ and $\widehat{u}$. Then, for any $Q\in \widehat{\MQ}$ we have for $\widehat{w}_1, \widehat{w}_2 \in Q$ that $\widehat{c}_{\widehat{w}_1} = \widehat{c}_{\widehat{w}_2}$ and $\widehat{u}_{\widehat{w}_1} = \widehat{u}_{\widehat{w}_2}$ hold. First, consider the case where $Q\in \widehat{\MQ}$ is bipolar, and let $w_1\in W$ be some index such that $\{w_1^+,w_1^-\}\subseteq Q$ holds. Then, it follows from equitability for $\widehat{c}$ that $c_{w_1} = \widehat{c}_{w_1^+} = \widehat{c}_{w_1^-} = -c_{w_1}$ holds, which implies that $c_{w_1} = 0$. Furthermore, equitability for $\widehat{u}$ implies that $u_{w_1} = \widehat{u}_{w_1^+} = \widehat{u}_{w_1^-} = -\ell_{w_1}$ holds. Then, assume for the sake of contradiction that there exists any $w_2\in W$ such that $|\{w_2^+,w_2^-\} \cap Q| = 1$ holds. If $w_2^+\in Q$ holds, then $\widehat{u}_{w^-_2} = - \ell_{w_2} = - \ell_{w_1} = \widehat{u}_{w^-_1} =  \widehat{u}_{w^+_2}$ shows that $w_2^-$ has the same bound for $\widehat{u}$, where the second equality follows since $\widehat{\MQ}$ is a bound-respecting partition and $w_2^+$ and $w_1^+$ are both included in $Q$. Similarly, if $w_2^- \in Q$ holds, then $\widehat{u}_{w^+_2} = u_{w_2} = u_{w_1} = \widehat{u}_{w^+_1} = \widehat{u}_{w^-_2}$ holds since $\widehat{\MQ}$ is a bound-respecting partition and $Q$ contains both $w^-_1$ and $w^-_2$. In either case, it follows that $\widehat{u}_{w_2^+} = \widehat{u}_{w_2^-}$ holds. As one of $w_2^+$ and $w_2^-$ is in $Q$, it follows that $\widehat{c}_{w^+_2} = \widehat{c}_{w^-_2} = c_{w_2} = 0$ also holds, which contradicts that $\widehat{\MQ}$ is the coarsest bound-respecting partition as then both $w_2^+$ and $w_2^-$ may be included in $Q$. Thus, bipolar parts must always contain pairs of variables and [\[def_symmetric\]](#def_symmetric){reference-type="ref" reference="def_symmetric"}[\[def_symmetric_col_bipolar\]](#def_symmetric_col_bipolar){reference-type="ref" reference="def_symmetric_col_bipolar"} follows.

Finally, consider the case where $\widehat{Q}\in \widehat{\MQ}$ is unipolar and given by $\widehat{Q} = Q^{\lambda}$ with $Q\subseteq W$ and $\lambda \in \{-1,1\}^W$. By equitability of $\widehat{\MQ}$, we must have for all $w_1^\lambda,w_2^\lambda \in Q^\lambda$ that $\widehat{c}_{w_1^\lambda} = \widehat{c}_{w_2^\lambda}$ and $\widehat{u}_{w_1^\lambda} = \widehat{u}_{w_2^\lambda}$ hold. Then, consider $Q^{-\lambda}\subseteq \widehat{W}$. First of all, note that for any $w_1^{-\lambda},w_2^{-\lambda} \in Q^{-\lambda}$ that we have: $\widehat{c}_{w_1^{-\lambda}} = -\widehat{c}_{w_1^{\lambda}} = -\widehat{c}_{w_2^{\lambda}} =\widehat{c}_{w_2^{-\lambda}}$, where the first and last equalities follow by definition of $\widehat{c}$ and the second equality follows since $w_1^\lambda$ and $w_2^\lambda$ lie in the equitable part $Q^\lambda$. Now, let us show that for the bounds $\widehat{u}_{w_1^{-\lambda}} = \widehat{u}_{w_2^{-\lambda}}$ holds too: $$\begin{aligned}
    \widehat{u}_{w_1^{-\lambda}} &= \begin{cases}
        -\ell_{w_1} &\text{ if $\lambda_{w_1} =1$}\\
        u_{w_1} &\text{ if $\lambda_{w_1} = -1$}
    \end{cases} = \begin{cases}
        -\ell_{w_1} &\text{ if $\lambda_{w_1} =1$ and $\lambda_{w_2} = 1$}\\
        -\ell_{w_1} &\text{ if $\lambda_{w_1} =1$ and $\lambda_{w_2} = -1$}\\
        u_{w_1} &\text{ if $\lambda_{w_1} = -1$ and $\lambda_{w_2} = 1$} \\
        u_{w_1} &\text{ if $\lambda_{w_1} = -1$ and $\lambda_{w_2} = -1$}
    \end{cases}\\
    &\stackrel{\textup{(a)}}{=} \begin{cases}
        -\ell_{w_2} &\text{ if $\lambda_{w_1} =1$ and $\lambda_{w_2} = 1$}\\
        u_{w_2} &\text{ if $\lambda_{w_1} =1$ and $\lambda_{w_2} = -1$}\\
        -\ell_{w_2} &\text{ if $\lambda_{w_1} = -1$ and $\lambda_{w_2} = 1$} \\
        u_{w_2} &\text{ if $\lambda_{w_1} = -1$ and $\lambda_{w_2} = -1$}
    \end{cases} =
    \begin{cases}
        -\ell_{w_2} &\text{ if $\lambda_{w_2} =1$}\\
        u_{w_2} &\text{ if $\lambda_{w_2} = -1$}
    \end{cases} = \widehat{u}_{w_2^{-\lambda}}.
\end{aligned}$$ Here, [(a)]{.upright} follows since $\widehat{\MQ}$ is a bound-respecting partition and $w_1^\lambda$ and $w_2^\lambda$ are in $Q\in \widehat{\MQ}$. Thus $Q^{-\lambda}\subseteq Q'$ must hold for some $Q'\in \widehat{\MQ}$. Using a similar argument, one can show that existence of any $w^{-\lambda}_x \in Q' \setminus Q^{-\lambda}$ shows that the part containing $w^{\lambda}_x$ can be merged with $Q^\lambda$, which contradicts that $\widehat{\MQ}$ is the coarsest partition. Thus $Q^{-\lambda}$ belongs to $\widehat{\MQ}$, which shows that [\[def_symmetric\]](#def_symmetric){reference-type="ref" reference="def_symmetric"}[\[def_symmetric_col_unipolar\]](#def_symmetric_col_unipolar){reference-type="ref" reference="def_symmetric_col_unipolar"} is satisfied. ◻
:::

Note in [\[thm_initial_partition_symmetric\]](#thm_initial_partition_symmetric){reference-type="ref" reference="thm_initial_partition_symmetric"} that the lower bounds of variables $x^+$ and $x^-$ are not considered as they are all zero and thus do not affect the equitable partition of $\widehat{W}$. Next, let us show that refinement of symmetric partitions through the constraint matrix again yields a symmetric partition.

::: lemma
[]{#thm_refinement_symmetric label="thm_refinement_symmetric"} Consider the split reformulation $F_S(A,b,\ell,u,c)$ of a linear program, where the constraint matrix of $F_S(A,b,\ell,u,c)$ is given by $\widehat{M} = \begin{bmatrix}
        A & - A\\
        -A & A
    \end{bmatrix}$, and let $(\widehat{\MP}_0,\widehat{\MQ}_0)$ be a symmetric partition of $F(A,b,\ell,u,c)$. Then, the coarsest equitable partition $(\widehat{\MP}_\infty,\widehat{\MQ}_\infty)$ that refines $(\widehat{\MP}_0,\widehat{\MQ}_0)$ with respect to $\widehat{M}$ is symmetric.
:::

::: proof
*Proof.* By Theorem 2 in [@Paige1987], the coarsest equitable partition is unique. Thus, it suffices to show that there exists a sequence of refinements such that the coarsest equitable partition is symmetric. We prove the statement by showing that there exists a refinement algorithm that maintains a symmetric partition at every step. In particular, we assume that $(\widehat{\MP}_i,\widehat{\MQ}_i)$ is symmetric, and show that existence of any refinement of $(\widehat{\MP}_i,\widehat{\MQ}_i)$ implies that there exists a refinement into a partition $(\widehat{\MP}_{i+1},\widehat{\MQ}_{i+1})$ that is symmetric. The result then follows inductively, where the base case is satisfied by assumption.

Then, assume that $(\widehat{\MP}_i,\widehat{\MQ}_i)$ is a symmetric partition of $F_S(A,b,\ell,u,c)$ such that there exists some $(P',Q') \in (\widehat{\MP}_i,\widehat{\MQ}_i)$ such that $\widehat{M}_{P',Q'}$ is not an equitable block. We consider the case where $\widehat{M}_{P',Q'}$ does not satisfy [\[eq_folding_row_sums\]](#eq_folding_row_sums){reference-type="eqref" reference="eq_folding_row_sums"} for some $v,v'\in P'$ such that $\sum_{w\in Q'} \widehat{M}_{v,w} \neq \sum_{w\in Q'} \widehat{M}_{v',w}$, and show that then $\widehat{\MP}_i$ can be refined symmetrically so that $(\widehat{\MP}_{i+1},\widehat{\MQ}_i)$ is a symmetric partition that refines $(\widehat{\MP}_i,\widehat{\MQ}_i)$. The argumentation for the case where $\widehat{M}_{P',Q'}$ does not satisfy [\[eq_folding_col_sums\]](#eq_folding_col_sums){reference-type="eqref" reference="eq_folding_col_sums"} is identical up to transposition.

First, note that if $Q'$ is bipolar, that then it follows by symmetry of $\widehat{P}_i$ and [\[thm_bipolar_symmetric_sum\]](#thm_bipolar_symmetric_sum){reference-type="ref" reference="thm_bipolar_symmetric_sum"} that $\sum_{v,w} \widehat{M}_{v,w} = 0$ holds for all $v\in P'$. Hence [\[eq_folding_row_sums\]](#eq_folding_row_sums){reference-type="eqref" reference="eq_folding_row_sums"} is satisfied in this case, and it is sufficient to consider the case where $Q'$ is unipolar in the following. We let $Q' = Q^\lambda$ for some $Q\subseteq W$ and $\lambda\in \{-1,1\}^W$ and use $Q^+ \coloneqq \{w\in Q \mid w^+\in Q^\lambda\}$ and $Q^- \coloneqq \{w\in Q \mid w^-\in Q^\lambda\}$ to denote the positive and negative variables in $Q$, respectively. Next, we show that refinement of the block $\widehat{M}_{P',Q'}$ always produces a symmetric partition. To do so, we distinguish the cases whether $P'$ is bipolar or unipolar.\
**Case 1: $P'$ is bipolar.**\
If $P'$ is bipolar, then there exists $P\subseteq V$ such that $P' = P^\onevec \cup P^{-\onevec}$. Then, since $Q'$ is unipolar, we have that: $$\widehat{M}_{P',Q'} = \widehat{M}_{P',Q^\lambda} = \begin{bmatrix}
            \widehat{M}_{P^\onevec,Q^\lambda \cap W^+_2} & \widehat{M}_{P^\onevec,Q^\lambda \cap W^-_2} \\
            \widehat{M}_{P^{-\onevec},Q^\lambda \cap W^+_2} & \widehat{M}_{P^{-\onevec},Q^\lambda \cap W^-_2} 
        \end{bmatrix} = \begin{bmatrix}
            A_{P,Q^+} & -A_{P,Q^-} \\
            -A_{P,Q^+} & A_{P,Q^-} 
        \end{bmatrix} = \begin{bmatrix}
            G \\
            -G
        \end{bmatrix},$$ where $G\coloneqq \begin{bmatrix}
            A_{P,Q^+} & -A_{P,Q^-}
        \end{bmatrix}$. Then, consider the refinement of $\widehat{\MP}_i$ into $\widehat{\MP}_{i+1}$ obtained by splitting $P'$ into $k$ different classes based on the different row sums of $\widehat{M}_{P',Q'}$. Let $P'_j$ for $j=1,\cdots,k$ denote these parts, where we have for all $v,v'\in P'_j$ that $\sum_{w\in Q'} \widehat{M}_{v,w} = \sum_{w\in Q'} \widehat{M}_{v',w}$, and define $\widehat{\MP}_{i+1} \coloneqq (\widehat{\MP}_i \setminus \{P'\} )\cup \bigcup_{j=1}^k P'_j$. We show that [\[def_symmetric_row_unipolar\]](#def_symmetric_row_unipolar){reference-type="ref" reference="def_symmetric_row_unipolar"} and [\[def_symmetric_row_bipolar\]](#def_symmetric_row_bipolar){reference-type="ref" reference="def_symmetric_row_bipolar"} in [\[def_symmetric\]](#def_symmetric){reference-type="ref" reference="def_symmetric"} are satisfied for all $P'_j$, which is sufficient since they are satisfied by assumption for all $P''\in \widehat{\MP}_i \setminus \{P'\}$ .

First, consider the case where $P'_j$ is bipolar. Since $P'_j$ contains at least one pair $v^+,v^-\in P'_j$ for some $v\in V_2$, we can deduce that $\sum_{w\in Q'} G_{v,w} = \sum_{w\in Q'} \widehat{M}_{v,w} = \sum_{w\in Q'} \widehat{M}_{v',w} = \sum_{w\in Q'} -G_{v,w} = 0$ holds. Then, note that for any $\gamma\in \{-1,1\}$ such that $v^\gamma \in P'_j$, the rows of $v^\gamma$ and $v^{-\gamma}$ both sum to zero, which implies that also $v^{-\gamma}\in P'_j$ holds by definition of $P'_j$, where we use the assumption that [\[def_symmetric\]](#def_symmetric){reference-type="ref" reference="def_symmetric"}[\[def_symmetric_row_bipolar\]](#def_symmetric_row_bipolar){reference-type="ref" reference="def_symmetric_row_bipolar"} holds for $\widehat{\MP}_i$ to infer that $v^{-\gamma} \in P'$ holds. Thus, this shows that [\[def_symmetric\]](#def_symmetric){reference-type="ref" reference="def_symmetric"}[\[def_symmetric_row_bipolar\]](#def_symmetric_row_bipolar){reference-type="ref" reference="def_symmetric_row_bipolar"} is satisfied by $\widehat{\MP}_{i+1}$ in the case where $P'$ is bipolar.

If $P'_j$ is unipolar, then there exists some $\gamma\in \{-1,1\}^V$ and $P\subseteq V$ such that $P'_j = P^\gamma$, and we have for all $v\in P'_j$ that $\sum_{w\in Q'} \widehat{M}_{v,w} = \gamma_v \sum_{w\in Q'} G_{v,w} = \alpha$ for some $\alpha \in \R\setminus\{0\}$, where we can exclude $\alpha = 0$ because this corresponds to the bipolar parts treated above. Since $\MP_i'$ satisfies [\[def_symmetric\]](#def_symmetric){reference-type="ref" reference="def_symmetric"}[\[def_symmetric_row_bipolar\]](#def_symmetric_row_bipolar){reference-type="ref" reference="def_symmetric_row_bipolar"} by assumption, all elements of $P^{-\gamma}$ are also contained in $P'$, and must be partitioned according to their sums. Then we have for all $v\in P^{-\gamma}$ that $\sum_{w\in Q'} \widehat{M}_{v,w} = -\gamma_v \sum_{w\in Q'} G_{v,w} = -\alpha$, which shows that there exists some $j'$ such that $P'_{j'} = P^{-\gamma}$. Thus, we have shown that [\[def_symmetric\]](#def_symmetric){reference-type="ref" reference="def_symmetric"}[\[def_symmetric_row_unipolar\]](#def_symmetric_row_unipolar){reference-type="ref" reference="def_symmetric_row_unipolar"} holds for $\widehat{\MP}_{i+1}$ in the case where $P'$ is bipolar. Thus, we have shown that $(\widehat{\MP}_{i+1}, \widehat{\MQ}_i)$ is symmetric and refines $(\widehat{\MP}_i,\widehat{\MQ}_i)$.\
**Case 2: $P'$ is unipolar.**\
If $P'$ is unipolar, then there exists $P\subseteq V$ and $\gamma\in \{-1,1\}^V$ such that $P' = P^\gamma$ holds. By the assumption that $\widehat{\MP}_i$ is symmetric, it also holds that $P^{-\gamma} \in \widehat{\MP}_i$. Then, we show that for $P^\gamma$ and $P^{-\gamma}$ the corresponding blocks $\widehat{M}_{P^\gamma,Q'}$ and $\widehat{M}_{P^{-\gamma},Q'}$ can be simultaneously refined to preserve symmetry in $\widehat{\MP}_{i+1}$. For $x\in \{\gamma,-\gamma\}$, let $P^{x}_+ \coloneqq \{v\in P \mid v^+ \in P^x\}$ and $P^{x}_- \coloneqq \{ v\in P \mid v^- \in P^{x}\}$ denote the positive and negative variables associated to $P^x$, respectively. Note that $P^{\gamma}_+ = P^{-\gamma}_-$ and $P^{\gamma}_- = P^{-\gamma}_+$ hold. Then, for the considered blocks $P^\gamma$ and $P^{-\gamma}$, we have that: $$\begin{bmatrix}
        \widehat{M}_{P^\gamma,Q'} \\
        \widehat{M}_{P^{-\gamma},Q'} 
    \end{bmatrix} = \begin{bmatrix}
        \widehat{M}_{P^\gamma,Q^\lambda} \\
        \widehat{M}_{P^{-\gamma},Q^\lambda} 
    \end{bmatrix} = 
    \begin{bmatrix}
        A_{P^\gamma_+,Q^+} & -A_{P^\gamma_+,Q^-} \\
        -A_{P^\gamma_-,Q^+} & A_{P^\gamma_-,Q^-} \\
        -A_{P^{-\gamma}_-,Q^+} & A_{P^{-\gamma}_-,Q^-} \\
        A_{P^{-\gamma}_+,Q^+} & A_{P^{-\gamma}_+,Q^-}
    \end{bmatrix} = \begin{bmatrix}
        A_{P^\gamma_+,Q^+} & -A_{P^\gamma_+,Q^-} \\
        -A_{P^\gamma_-,Q^+} & A_{P^\gamma_-,Q^-} \\
        -A_{P^{\gamma}_+,Q^+} & A_{P^{\gamma}_+,Q^-} \\
        A_{P^{\gamma}_-,Q^+} & A_{P^{\gamma}_-,Q^-}
    \end{bmatrix} = \begin{bmatrix}
        G\\
        -G
    \end{bmatrix},$$ where $G=\widehat{M}_{P^\gamma,Q'} = \begin{bmatrix}
        A_{P^\gamma_+,Q^+} & -A_{P^\gamma_+,Q^-} \\
        -A_{P^\gamma_-,Q^+} & A_{P^\gamma_-,Q^-}
    \end{bmatrix}$. Thus, the block corresponding to $(P^{-\gamma},Q')$ is the negated block of $(P^\gamma,Q')$.

For $j=1,\dotsc,k$, let $P_j$ denote the partition of $P$ into $P_j$ so that the row sums of all $v\in P^\gamma_j$ are identical, and for $j\neq j'$ and $v\in P_j$ and $v\in P_{j'}$, the row sums of $v$ and $v'$ differ. Then, we similarly define the partition $P^{-\gamma}_j$ for $j=1,\dotsc,k$. For $v,v'\in P^{-\gamma}$, note that $$\sum_{w\in Q'} \widehat{M}_{v,w} = \sum_{w\in Q'} -G_{v,w} = - \sum_{w\in Q'} G_{v,w} \stackrel{\textup{(a)}}{=} - \sum_{w\in Q'} G_{v',w} =  \sum_{w\in Q'} -G_{v',w} = \sum_{w\in Q'} \widehat{M}_{v',w}$$ where [(a)]{.upright} holds because $P^\gamma_j$ has the same row sums by definition. Thus, the partitions $P^\gamma_j$ and $P^{-\gamma}_j$ are both valid refinements. Note that for each $j=1,\cdots,k$, the pair $P^\gamma_j$ and $P^{-\gamma}_j$ is a unipolar pair as in [\[def_symmetric\]](#def_symmetric){reference-type="ref" reference="def_symmetric"}[\[def_symmetric_row_unipolar\]](#def_symmetric_row_unipolar){reference-type="ref" reference="def_symmetric_row_unipolar"}. Then, the partition defined by $\widehat{\MP}_{i+1} \coloneqq \widehat{\MP}_{i}\setminus \{P^\gamma, P^{-\gamma}\} \cup \bigcup_{j=1}^k (P^\gamma_j\cup P^{-\gamma}_j)$ satisfies [\[def_symmetric\]](#def_symmetric){reference-type="ref" reference="def_symmetric"}[\[def_symmetric_row_unipolar\]](#def_symmetric_row_unipolar){reference-type="ref" reference="def_symmetric_row_unipolar"}, and [\[def_symmetric_row_bipolar\]](#def_symmetric_row_bipolar){reference-type="ref" reference="def_symmetric_row_bipolar"} follows since we did not alter any bipolar part in $\widehat{\MP}_i$. Thus, $(\widehat{\MP}_{i+1},\widehat{\MQ}_i)$ is symmetric and refines $(\widehat{\MP}_i,\widehat{\MQ}_i)$.\
Thus, we have shown that there exists a symmetric refinement $(\widehat{\MP}_{i+1}, \widehat{\MQ}_{i+1})$ in all cases, where $\widehat{\MQ}_{i+1} = \widehat{\MQ}_i$ holds. Using essentially the same proof, one can show that there exists a symmetric refinement $(\widehat{\MP}_{i+1},\widehat{\MQ}_{i+1})$ with $\widehat{\MP}_i = \widehat{\MP}_{i+1}$ if there exists some $(P',Q')\in \widehat{\MP}_i\times \widehat{\MQ}_i$ such that [\[eq_folding_col_sums\]](#eq_folding_col_sums){reference-type="eqref" reference="eq_folding_col_sums"} is not satisfied for $\widehat{M}$. This completes the proof. ◻
:::

::: theorem
[]{#thm_lp_symmetric label="thm_lp_symmetric"} The coarsest bound-respecting and equitable partition $(\widehat{\MP},\widehat{\MQ})$ of $F_S(A,b,\ell,u,c)$ is symmetric.
:::

::: proof
*Proof.* shows that the initial partition is symmetric, and it follows from [\[thm_refinement_symmetric\]](#thm_refinement_symmetric){reference-type="ref" reference="thm_refinement_symmetric"} shows that applying color refinement on the constraint matrix produces a symmetric equitable partition, given the symmetric initial partition. ◻
:::

shows that symmetric equitable partitions of split reformulations can be obtained by using the assumption that the partition is bound-respecting. Although this assumption seems a bit arbitrary for now, we will motivate it in further detail later on.\
A simple but crucial observation for symmetric partitions is that symmetric partition of the split reformulation induce partitions and signings for the original linear program.

::: proposition
[]{#thm_unipolar_original_mapping label="thm_unipolar_original_mapping"} Consider any symmetric partition $(\widehat{\MP},\widehat{\MQ})$. For its unipolar parts $\widehat{\MP}_U$ and $\widehat{\MQ}_U$, there exist $\gamma\in \{-1,1\}^{V_U}$ and a partition $\MP_U$ of $V_U$ such that $\widehat{\MP}_U = \bigcup_{P\in \MP}\{ P^\gamma, P^{-\gamma}\}$, and there exists $\lambda\in \{-1,1\}^{W_U}$ and a partition $\MQ_U$ of $W_U$ such that $\widehat{\MQ}_U = \bigcup_{Q\in \MQ} \{ Q^\lambda, Q^{-\lambda}\}$. For its bipolar parts $\widehat{\MP}_B$ and $\widehat{\MQ}_B$, there exist partitions $\MP_B$ of $V_B$ and $\MQ_B$ of $W_B$ such that $\widehat{\MP}_B = \{P^\onevec \cup P^{-\onevec} \mid P \in \MP_B\}$ and $\widehat{\MQ}_B = \{Q^\onevec \cup Q^{-\onevec} \mid  Q \in \MQ_B\}$ hold.
:::

::: proof
*Proof.* Consider any unipolar part $\widehat{P}\in \widehat{\MP}$. By unipolarity, there exists $P\subseteq V$ such that $\widehat{P} = P^\gamma$. Then, since $(\widehat{\MP},\widehat{\MQ})$ is symmetric, [\[def_symmetric\]](#def_symmetric){reference-type="ref" reference="def_symmetric"}[\[def_symmetric_row_unipolar\]](#def_symmetric_row_unipolar){reference-type="ref" reference="def_symmetric_row_unipolar"} holds and shows $P^{-\gamma}\in \widehat{\MP}$ holds too. Since this holds for all elements and $\widehat{\MP}$ is a partition, it follows that $\widehat{\MP}$ consists of pairs $P^\gamma$, $P^{-\gamma}$. Then, $\MP_U$ is generated by all such $P$ and $\gamma$ is defined by picking a representative part for each pair $P^\gamma$, $P^{-\gamma}$. A similar argument using [\[def_symmetric\]](#def_symmetric){reference-type="ref" reference="def_symmetric"}[\[def_symmetric_col_unipolar\]](#def_symmetric_col_unipolar){reference-type="ref" reference="def_symmetric_col_unipolar"}shows the result for $\lambda$ and $\MQ_U$. For the bipolar parts, the statement follows directly from [\[def_symmetric\]](#def_symmetric){reference-type="ref" reference="def_symmetric"}[\[def_symmetric_row_bipolar\]](#def_symmetric_row_bipolar){reference-type="ref" reference="def_symmetric_row_bipolar"}[\[def_symmetric_col_bipolar\]](#def_symmetric_col_bipolar){reference-type="ref" reference="def_symmetric_col_bipolar"}. ◻
:::

For any $\gamma\in \{-1,1\}^{V_U}$, $\lambda\in \{-1,1\}^{W_U}$, $\MP \coloneqq \MP_U \cup \MP_B$ and $\MQ\coloneqq \MQ_U \cup \MQ_B$ such as those in [\[thm_unipolar_original_mapping\]](#thm_unipolar_original_mapping){reference-type="ref" reference="thm_unipolar_original_mapping"} we say that they are *generated by* $(\widehat{\MP},\widehat{\MQ})$. We use $\widehat{P}^\gamma_U \coloneqq \{ P^\gamma \mid P \in \MP_U\}$ and $\widehat{Q}^\lambda_U \coloneqq \{ Q^\lambda \mid Q \in \MQ_U\}$, and define $\widehat{P}^{-\gamma}_U$ and $\widehat{Q}^{-\lambda}_U$ similarly. Note that the choice for $\gamma$ is not unique as for each $P\in \MP_U$ we can exchange $P^{\gamma}$ and $P^{-\gamma}$ by negating $\gamma_v$ for all $v\in P$, i.e. by using $\gamma' \coloneqq (-\gamma_P,\gamma_{V\setminus P})$. Similarly, one can also choose for each $Q\in \MQ$ to simultaneously negate $\lambda_{w}$ for all $w\in Q$. We note that these actions only affect the signs $\gamma$ and $\lambda$ and not the sets $\MP_U$ and $\MQ_U$.
