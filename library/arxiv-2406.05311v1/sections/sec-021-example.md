---
doc_id: arxiv-2406.05311v1
doc_title: "Draft of June 11, 2024 A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD"
section_id: sec-021-example
section_title: "Example"
section_number: null
pages: 30-31
source_pdf: A_quantum_Murnaghan--Nakayama_rule_for_the_flag_ma.pdf
source_sha256: c431fca150329547
toc_source: outline
text_source: latex
latex_prose_ratio: 0.703
latex_coverage_ratio: 0.932
doc_brief: "A quantum Murnaghan–Nakayama rule for the flag manifold — In this paper, we give a rule for the multiplication of a Schubert class by a tautological class in the (small) quantum cohomology ring of"
---
We illustrate Proposition [\[BS2002\]](#BS2002){reference-type="ref" reference="BS2002"} with a sequence of equivalences on a classical tree.

$$\begin{array}{c}
        \valuediagram[scale=1, padding=1]{{3, 4}, {1, 3}, {5, 6}, {3, 5}, {5, 7}, {2, 5}}
    \end{array}
    \equiv
    \begin{array}{c}
        \valuediagram[scale=1, xmax=7, padding=1]{{5, 6},{3, 4},{2, 3},{1, 2},{2, 7},{3, 5}}
    \end{array}
    \equiv
    \begin{array}{c}
        \valuediagram[scale=1, xmax=7, padding=1]{{2,7},{3,5}} \\
        \valuediagram[scale=1, xmax=7, padding=1]{{5,6},{3,4},{2,3},{1,2}}
    \end{array}
    \equiv
    \begin{array}{c}
        \valuediagram[scale=1, xmax=7, padding=1]{{3,5}} \\[-0.75ex]
        \valuediagram[scale=1, xmax=7, padding=1]{{2,7}} \\
        \valuediagram[scale=1, xmax=7, padding=1]{{3,4},{2,3},{1,2}} \\[-0.75ex]
        \valuediagram[scale=1, xmax=7, padding=1]{{5,6}}
    \end{array}$$

### Proof of Theorem [\[main-theorem\]](#main-theorem){reference-type="ref" reference="main-theorem"}

We use induction on the number of operators in ${\mathbf v}$. Let ${\mathbf v}_{ef}$ be its rightmost operator so that ${\mathbf v}=\mathbf{F}{\mathbf v}_{ef}$, where $\mathbf{F}$ is a forest. As ${\mathbf v}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}u$ is nonzero, ${\mathbf v}_{ef}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}u$ is nonzero. Then there exist $\alpha\in{\mathbb N}^{n-1}$ and $v\in S_n$ such that ${\mathbf v}_{ef}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}u=q^\alpha v$, and $\mathbf{F}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}v$ is nonzero. By induction, $\mathbf{F}$ is $(v,k)$-equivalent to $\mathbf{R}\mathbf{C}$, where $\mathbf{R}$ is a row and $\mathbf{C}$ is a column, and there exists $r \in {\mathbb N}$ such that $\mathfrak o^r(\mathbf{F})$ is $(\mathfrak o^r v, k)$-equivalent to $\mathfrak o^r(\mathbf{R})\mathfrak o^r(\mathbf{C})$, where the later is classical. Thus

$$\mathfrak o^r({\mathbf v}) \text{ is } (\mathfrak o^r u,k)\text{- equivalent to } \mathfrak o^r(\mathbf{R})\mathfrak o^r(\mathbf{C}){\mathbf v}_{cd}\,,$$

where $\mathfrak o^r(\mathbf{R})$ is a classical row, $\mathfrak o^r(\mathbf{C})$ is a classical column, and ${\mathbf v}_{cd}=\mathfrak o^r({\mathbf v}_{ef})$.

If $c<d$, then $\mathfrak o^r(\mathbf{R})\mathfrak o^r(\mathbf{C}){\mathbf v}_{cd}$ is a classical forest and by Proposition [\[BS2002\]](#BS2002){reference-type="ref" reference="BS2002"}, it is $(\mathfrak o^r u, k)$-equivalent to the composition of a classical row and a classical column, $\mathbf{R}' \mathbf{C}'$. But then ${\mathbf v}$ is $(u, k)$-equivalent to $\mathfrak o^{-r}(\mathbf{R}')\mathfrak o^{-r}(\mathbf{C}')$, which is a composition of a row and a column that admits a cyclic shift that is classical.

Suppose now that $c>d$. Set $a=d$ and $b=c$ so that ${\mathbf v}_{cd}={\mathbf v}_{ba}$ with $a<b$, to conform to our running notation for quantum operators. Since $\mathbf{F}$ is a forest, $\mathfrak o^r(\mathbf{R})\mathfrak o^r(\mathbf{C})$ is a classical forest. Grouping components of $\mathfrak o^r(\mathbf{R})\mathfrak o^r(\mathbf{C})$ together gives noncrossing (classical) trees $\mathbf{T}_1,\dotsc,\mathbf{T}_m$ such that $\mathfrak o^r({\mathbf v})$ is $(\mathfrak o^r u, k)$-equivalent to $(\mathbf{T}_m\dotsb\mathbf{T}_1){\mathbf v}_{ba}$. The proof of Theorem [\[main-theorem\]](#main-theorem){reference-type="ref" reference="main-theorem"} follows from Lemma [\[cyclic-shift-classical-trees-times-quantum\]](#cyclic-shift-classical-trees-times-quantum){reference-type="ref" reference="cyclic-shift-classical-trees-times-quantum"} below, and since ${\mathbf v}$ is a forest, an application of Proposition [\[BS2002\]](#BS2002){reference-type="ref" reference="BS2002"}.

::: lemma
[]{#cyclic-shift-classical-trees-times-quantum label="cyclic-shift-classical-trees-times-quantum"} Let $a<b$ and suppose that

1.  $\mathbf{T}_1, \ldots, \mathbf{T}_m$ are disjoint, noncrossing, classical trees;

2.  $\mathbf{T}_m \cdots \mathbf{T}_1 {\mathbf v}_{ba} \not\equiv {\mathbf 0}$; and

3.  the graph of $\mathbf{T}_m \cdots \mathbf{T}_1 {\mathbf v}_{ba}$ is a forest.

Then $\mathbf{T}_m \cdots \mathbf{T}_1 {\mathbf v}_{ba}$ admits a cyclic shift that is a product of classical operators.
:::

::: proof
*Proof.* We have three cases according to $\#(\{a,b\}\cap \mathop{\mathrm{supp}}(\mathbf{T}_m \cdots \mathbf{T}_1))$.

Suppose that $\emptyset=\{a,b\}\cap \mathop{\mathrm{supp}}(\mathbf{T}_m \cdots \mathbf{T}_1)$. Since for each $i \in [m]$, we have $\mathbf{T}_i {\mathbf v}_{ba}\not\equiv {\mathbf 0}$, Corollary [\[T\*vq=0\]](#T*vq=0){reference-type="ref" reference="T*vq=0"} implies that either $\max(\mathbf{T}_i)<a$ or $a<\min(\mathbf{T}_i)$, for each $i\in[m]$. Hence, $\mathfrak o^{-a}(\mathbf{T}_m \cdots \mathbf{T}_1 {\mathbf v}_{ba})$ is a composition of classical operators. We present an example.

$$\begin{array}{c}
      \valuediagram[scale=1, critical windows={(5,6)}]{
                    {12,5},
                    {10,11}, {9,10},
                    {1,3}, {3,4}, {2,3},
                    {14,15}, {15,16}, {13,15},
                    {6,7}, {7,8}}
    \end{array}
 
        \xrightarrow{~~\mathfrak o^{11}~}
    \begin{array}{c}
      \valuediagram[scale=1]{
                    {7,16},
                    {5,6}, {4,5},
                    {12,14}, {14,15}, {13,14},
                    {9,10}, {10,11}, {8,10},
                    {1,2}, {2,3}}
     \end{array}$$

Suppose that $1=\#(\{a,b\}\cap \mathop{\mathrm{supp}}(\mathbf{T}_m \cdots \mathbf{T}_1))$. Applying $\omega_0$ if necessary, we may assume that $b\in\mathop{\mathrm{supp}}(\mathbf{T}_m \cdots \mathbf{T}_1)$. As the trees have disjoint support, $b$ lies in the support of exactly one tree. As the trees commute, we may replace this operator by an equivalent operator (obtained by commuting the trees) and assume that $b \in \mathop{\mathrm{supp}}(\mathbf{T}_m)$. By Corollary [\[T\*vq=0\]](#T*vq=0){reference-type="ref" reference="T*vq=0"}, $a < \min(\mathbf{T}_m)$ for otherwise $\mathbf{T}_m {\mathbf v}_{ba} \equiv {\mathbf 0}$, contradicting that $\mathbf{T}_m \cdots \mathbf{T}_1{\mathbf v}_{ba}$ is nonzero.

Since $\emptyset=\{a,b\}\cap\mathop{\mathrm{supp}}(\mathbf{T}_{m-1}\dotsb\mathbf{T}_1)$, the previous argument implies that for $i\in[m{-}1]$ either $\max(\mathbf{T}_i)<a$ or $a<\min(\mathbf{T}_i)$. Thus $\mathfrak o^{-a}(\mathbf{T}_m \cdots \mathbf{T}_1 {\mathbf v}_{ba})$ is a composition of classical operators. We present an example. $$\begin{array}{c}
         \valuediagram[scale=1, critical windows={(5,6)}]{
             {11,5},
             {7,8}, {6,7},
             {1,3}, {3,4}, {2,3},
             {14,15}, {15,16}, {13,15},
             {9,11}, {11,12}, {10,11}}
     \end{array}
       \xrightarrow{~~\mathfrak o^{11}~}
     \begin{array}{c}
         \valuediagram[scale=1]{
             {6,16},
             {2,3},{1,2},
             {12,14},{14,15},{13,14},
             {9,10},{10,11},{8,10},
             {4,6},{6,7},{5,6}}
     \end{array}$$

Finally, suppose that $\{a,b\}\subset \mathop{\mathrm{supp}}(\mathbf{T}_m \cdots \mathbf{T}_1)$. As the trees are disjoint, each of $a$ and $b$ lies in the support of a unique tree. These cannot be the same tree, for if $a,b\in\mathop{\mathrm{supp}}(\mathbf{T}_i)$, then the graph of $\mathbf{T}_i {\mathbf v}_{ba}$ is not a tree, contradicting that $\mathbf{T}_m \cdots \mathbf{T}_1 {\mathbf v}_{ba}$ is a forest.

As the $\mathbf{T}_i$ commute, we may replace this operator by an equivalent operator and assume that $a \in \mathop{\mathrm{supp}}(\mathbf{T}_{m})$ and $b \in \mathop{\mathrm{supp}}(\mathbf{T}_{m-1})$. Let $i\in[m{-}1]$. As $\mathbf{T}_i v_{ba}\not\equiv{\mathbf 0}$, Corollary [\[T\*vq=0\]](#T*vq=0){reference-type="ref" reference="T*vq=0"} implies that either $\max(\mathbf{T}_i)<a$ or $a<\min(\mathbf{T}_i)$.

If $\max(\mathbf{T}_i)<a$, then as $a\in\mathop{\mathrm{supp}}(\mathbf{T}_m)$, we have $\max(\mathbf{T}_i)<\max(\mathbf{T}_m)$.

If $a<\min(\mathbf{T}_i)$, then as $a\in\mathop{\mathrm{supp}}(\mathbf{T}_m)$ and the trees $\mathbf{T}_i$ and $\mathbf{T}_m$ are noncrossing, we have $\max(\mathbf{T}_m)<\min(\mathbf{T}_i)$.

Since $a\leq \max(\mathbf{T}_m) < b$, this implies that $\mathfrak o^{-\max(\mathbf{T}_{m})}(\mathbf{T}_m \cdots \mathbf{T}_1 {\mathbf v}_{ba})$ is a composition of classical operators, which completes the proof. We present an example. $$\begin{array}{c}
         \valuediagram[scale=1, critical windows={(7,8)}]{
             {11,6},
             {2,3},{1,2},{2,4},
             {14,16},{13,14},{14,15},
             {10,11},{9,10},{10,12},{8,9},
             {5,6},{6,7}}
     \end{array}
       \xrightarrow{~~\mathfrak o^{-7}~}
     \begin{array}{c}
         \valuediagram[scale=1]{
             {4,14},
             {10,11},{9,10},{10,12},
             {7,9},{6,7},{7,8},
             {3,4},{2,3},{3,5},{1,2},
             {13,14},{14,15}}
     \end{array}
     \qedhere$$ ◻
:::

## Proof of Theorem [\[Th:nonZero\]](#Th:nonZero){reference-type="ref" reference="Th:nonZero"} {#sec:final}

Let $[u,q^\alpha w]^q_k$ be a minimal interval, and consider a composition ${\mathbf v}$ corresponding to some saturated chain in $[u,q^\alpha w]^q_k$. Then ${\mathbf v}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}u= q^\alpha w$. As explained in Section [\[sec:Qminim\]](#sec:Qminim){reference-type="ref" reference="sec:Qminim"}, as $[u,q^\alpha w]^q_k$ is a minimal interval, $\ell(q^\alpha w)-\ell(u)=\#\mathop{\mathrm{supp}}(wu^{-1}) - s(wu^{-1})$. This implies that the graph of ${\mathbf v}$ contains no cycles, and is therefore a forest. As ${\mathbf v}$ is nonzero, it is a forest.

By Theorem [\[main-theorem\]](#main-theorem){reference-type="ref" reference="main-theorem"}, ${\mathbf v}$ is $(u,k)$-equivalent to a composition of operators of the form $\mathbf{R}\mathbf{C}$ where $\mathbf{R}$ is a row and $\mathbf{C}$ is a column, and there exists a suitable cycle shift $\mathfrak o^r$ such that applying it to $[u,q^\alpha w]^q_k$ gives a classical interval with a classical chain $\mathfrak o^r(\mathbf{R})\mathfrak o^r(\mathbf{C})$ that is peakless. Let $a$ be its height and $a+b-1=\ell(q^\alpha w)-\ell(u)$ its length.

By Postnikov's cyclic symmetry [@Postnikov_symmetry Thm. 4] (and using the notation of [@Postnikov_symmetry]), $$C_{v(\lambda,k),u,w_0w}\ =\ q^{\beta(r,u,w)}C_{v(\lambda,k),\mathfrak o^{r} u,\mathfrak o^{-r}w_0w}\ =\ 
   q^{\beta(r,u,w)}C_{\mathfrak o^{r} u,v(\lambda,k),w_0\mathfrak o^{r}w}\,,$$ where $q^{\beta(r,u,w)}$ is some monomial in the $q_i$'s determined by $u$, $w$ and the power $r$ in $\mathfrak o^r$. Translating the notation of [@Postnikov_symmetry] to our notation gives $$C_{u,v,w_0w}\ =\ \sum_\alpha q^\alpha N_{u,v}^{w,\alpha}=\ \sum_\alpha C_{u,v}^{q^\alpha w} \,.$$

Thus if $\lambda=(b,1^{a-1})$ is the hook partition, then the peakless chain $\mathfrak o^r(\mathbf{R})\mathfrak o^r(\mathbf{C})$ in the classical interval $[\mathfrak o^{r} u,\mathfrak o^{r}w]_k$ implies that $$C_{u,v(\lambda,k)}^{q^\alpha w}\ =\ C_{\mathfrak o^{r} u,v(\lambda,k)}^{ q^{\beta(r,u,w)}q^\alpha \mathfrak o^{r}w}\ =\
   C_{\mathfrak o^{r} u,v(\lambda,k)}^{ \mathfrak o^{r}w} \ne 0\,,$$ by Proposition [\[P:peaklessChains\]](#P:peaklessChains){reference-type="ref" reference="P:peaklessChains"} and Lemma [\[P:classical_hook\]](#P:classical_hook){reference-type="ref" reference="P:classical_hook"}. This completes the proof.$\Box$
