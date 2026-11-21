---
doc_id: arxiv-2406.05311v1
doc_title: "Draft of June 11, 2024 A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD"
section_id: sec-018-56-crossing-products
section_title: "Crossing products"
section_number: 5.6
pages: 26-27
source_pdf: A_quantum_Murnaghan--Nakayama_rule_for_the_flag_ma.pdf
source_sha256: c431fca150329547
toc_source: outline
text_source: latex
latex_prose_ratio: 0.91
latex_coverage_ratio: 0.918
doc_brief: "A quantum Murnaghan–Nakayama rule for the flag manifold — In this paper, we give a rule for the multiplication of a Schubert class by a tautological class in the (small) quantum cohomology ring of"
---
[]{#crossing-products label="crossing-products"} For a composition ${\mathbf v}={\mathbf v}_{a_rb_r}\cdots {\mathbf v}_{a_1b_1}$, let $\min({\mathbf v})$ and $\max({\mathbf v})$ be the minimum and maximum elements of its support, $\{a_r,b_r,\dots, a_1,b_1\}$.

A composition ${\mathbf v}$ defines a (multi)graph whose vertices are its support. It has one edge between $a$ and $b$ for each operator ${\mathbf v}_{ab}$ appearing in ${\mathbf v}$. We say that ${\mathbf v}$ is if its graph is connected, that ${\mathbf v}$ is a if its graph is a path with $a_1$ or $b_1$ as an endpoint and $\#(\{a_i,b_i\}\cap\{a_{i+1},b_{i+1}\})=1$ for all $i$. It is a if its graph is tree. A composition of two connected compositions is if their supports are disjoint and crossing. Note that noncrossing products of trees are minimal. Indeed, each tree is minimal, so a noncrossing product of trees is a noncrossing product of minimal compositions of operators, and hence is minimal. Figure [\[fig:nonzero-touching-operators\]](#fig:nonzero-touching-operators){reference-type="ref" reference="fig:nonzero-touching-operators"} shows all nonzero paths of length two and Figure [\[F:symmetry-chains\]](#F:symmetry-chains){reference-type="ref" reference="F:symmetry-chains"} shows some compositions that are trees but not paths. Figure [\[fig:crossing-operators\]](#fig:crossing-operators){reference-type="ref" reference="fig:crossing-operators"} shows all crossing compositions ${\mathbf v}_{ab} {\mathbf v}_{cd}$, and all are equivalent to zero.

::: lemma
[]{#L:crossing-supports label="L:crossing-supports"} A crossing composition of connected minimal operators is equivalent to zero.
:::

::: proof
*Proof.* Suppose that ${\mathbf v}$ and ${\mathbf v}'$ are connected compositions whose supports are disjoint and crossing. Then there exists $l<r$ in $\mathop{\mathrm{supp}}({\mathbf v})$ and $l'<r'$ in $\mathop{\mathrm{supp}}({\mathbf v}')$ with $\{l,r\}$ and $\{l',r'\}$ crossing. We may assume that $l < l'$, which implies that $l < l' < r < r'$. As the graph of ${\mathbf v}$ is connected, it contains a sequence of edges connecting $l$ to $r$. Similarly, the graph of ${\mathbf v}'$ contains a sequence of edges connecting $l'$ to $r'$.

In the sequence of edges connecting $l$ to $r$, let $(a,b)$ be the first edge with exactly one endpoint between $l'$ and $r'$---this corresponds to an operator ${\mathbf v}_{ab}$ in ${\mathbf v}$. Thus either $l'$ is between $a$ and $b$, or $r'$ is between $a$ and $b$. Suppose that $r'$ is between $a$ and $b$. Let $(c,d)$ be the first edge in the path from $l'$ to $r'$ with exactly one endpoint between $a$ and $b$---it corresponds to an operator ${\mathbf v}_{cd}$ in ${\mathbf v}'$. Thus $\{a,b\}$ and $\{c,d\}$ are crossing. (If $l'$ is between $a$ and $b$, a similar argument gives an edge $(c,d)$ such that $\{a,b\}$ and $\{c,d\}$ are crossing.)

By Lemma [\[Lem:Rel\]](#Lem:Rel){reference-type="ref" reference="Lem:Rel"}(1)(ii), ${\mathbf v}_{ab} {\mathbf v}_{cd} \equiv{\mathbf 0}$. As $\mathop{\mathrm{supp}}({\mathbf v})\cap \mathop{\mathrm{supp}}({\mathbf v}')=\emptyset$, each operator in ${\mathbf v}$ commutes with each operator in ${\mathbf v}'$ by Lemma [\[Lem:Rel\]](#Lem:Rel){reference-type="ref" reference="Lem:Rel"}(1). By Remark [\[Rem:k-action\]](#Rem:k-action){reference-type="ref" reference="Rem:k-action"} [\[Rem:k-action:subword\]](#Rem:k-action:subword){reference-type="ref" reference="Rem:k-action:subword"}, these commutations give equivalent operators. Writing ${\mathbf v}=\mathbf{A} {\mathbf v}_{ab} \mathbf{B}$ and ${\mathbf v}'=\mathbf{C}  {\mathbf v}_{cd}  \mathbf{D}$, we have $${\mathbf v}{\mathbf v}'
        \ =\  \big(\mathbf{A} {\mathbf v}_{ab} \mathbf{B}
          \big)
          \big(\mathbf{C}  {\mathbf v}_{cd}  \mathbf{D}
          \big)
       \  \equiv\  \mathbf{AC} \big({\mathbf v}_{ab} {\mathbf v}_{cd}\big)\mathbf{BD}\  \equiv\  {\mathbf 0}\,.$$ The first equivalence is by commutation of operators and the second is by Remark [\[Rem:k-action\]](#Rem:k-action){reference-type="ref" reference="Rem:k-action"}[\[Rem:k-action:zero_compose\]](#Rem:k-action:zero_compose){reference-type="ref" reference="Rem:k-action:zero_compose"}. ◻
:::

We single out a special case of Lemma [\[L:crossing-supports\]](#L:crossing-supports){reference-type="ref" reference="L:crossing-supports"}.

::: corollary
[]{#corollary-classical-product-times-quantum label="corollary-classical-product-times-quantum"} Suppose that ${\mathbf u}$ is a connected composition of classical operators that is minimal, $a, b \notin \mathop{\mathrm{supp}}({\mathbf u})$, $a<b$, and ${\mathbf u}{\mathbf v}_{ba} \not\equiv {\mathbf 0}$. If $l = \min({\mathbf u})$ and $r = \max({\mathbf u})$, then $$\begin{gathered}
        a < b < l < r
        \quad\text{or}\quad
        l < r < a < b
        \quad\text{or}\quad
        l < a < b < r
        \quad\text{or}\quad
        a < l < r < b\ .






    
\end{gathered}$$
:::

::: proof
*Proof.* The graphs of ${\mathbf u}$ and ${\mathbf v}_{ba}$ are connected, as that of ${\mathbf v}_{ba}$ is a single edge. Since they have disjoint support and ${\mathbf u}{\mathbf v}_{ba} \not\equiv {\mathbf 0}$, Lemma [\[L:crossing-supports\]](#L:crossing-supports){reference-type="ref" reference="L:crossing-supports"} implies their supports are noncrossing. ◻
:::

We deduce that a crossing product of a classical tree (no cycle in its graph and no repeated edges) and a quantum operator is zero.

::: corollary
[]{#T*vq=0 label="T*vq=0"} Let $\mathbf{T}$ be a composition of classical operators whose graph is a tree. If $a<b$ with $\min(\mathbf{T}) < a < \max(\mathbf{T})$ and $a \notin \mathop{\mathrm{supp}}(\mathbf{T})$, then $\mathbf{T}{\mathbf v}_{ba} \equiv {\mathbf 0}$.
:::

::: proof
*Proof.* Note that $\mathbf{T}$ is minimal. Suppose that $\mathbf{T}{\mathbf v}_{ba} \not\equiv {\mathbf 0}$. Then there exist $k<n$ and a permutation $u\in S_n$ such that $\mathbf{T}{\mathbf v}_{ba}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}u\neq{\mathbf 0}$. Suppose that ${\mathbf v}_{ba}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}u = q_{i, j} v$. Then $i=u^{-1}(b)\leq k <j=u^{-1}(a)$ and $a=v(i)$. By Proposition [\[prop:quantum-k-bruhat-covers\]](#prop:quantum-k-bruhat-covers){reference-type="ref" reference="prop:quantum-k-bruhat-covers"}, if $i<l<j$, then $a<u(l)=v(l)<b$, and by Remark [\[Rem:k-action\]](#Rem:k-action){reference-type="ref" reference="Rem:k-action"}[\[Rem:k-action:chains\]](#Rem:k-action:chains){reference-type="ref" reference="Rem:k-action:chains"}, $\mathbf{T}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}v\neq{\mathbf 0}$.

Since $\min(\mathbf{T})<a<\max(\mathbf{T})$, $a\not\in\mathop{\mathrm{supp}}(\mathbf{T})$, and $\mathbf{T}$ is a classical tree, there is an operator ${\mathbf v}_{cd}$ in $\mathbf{T}$ with $c<a<d$. Write $\mathbf{T}=\mathbf{T}'' {\mathbf v}_{cd} \mathbf{T}'$ and set $w \vcentcolon= \mathbf{T}' \mathop{\mathrm{{\scriptstyle \bullet}}}_{k}v\neq {\mathbf 0}$. As $\mathbf{T}'$ is classical, $v\leq_k w$. By Proposition [\[nothing-in-between-is-in-between\]](#nothing-in-between-is-in-between){reference-type="ref" reference="nothing-in-between-is-in-between"}, if $l\leq k$, then $w(l)\geq v(l)$ and we have $a=w(i)$ as $a\not\in\mathop{\mathrm{supp}}(\mathbf{T}')$.

We also have ${\mathbf v}_{cd}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}w\neq{\mathbf 0}$, so that $w\lessdot_k (c,d)w$. Consider the position $l(\leq k)$ of $c$ in $w$, $c=w(l)$. As $c<a<d$ and $d$ is to the right of $k$ (and $i$), we cannot have $l<i$, by Proposition [\[nothing-in-between-is-in-between\]](#nothing-in-between-is-in-between){reference-type="ref" reference="nothing-in-between-is-in-between"}. If $i<l$, then $a<v(l)\leq w(l)=c$, contradicting $c<a$. Thus $\mathbf{T}{\mathbf v}_{ba}\equiv {\mathbf 0}$. ◻
:::
