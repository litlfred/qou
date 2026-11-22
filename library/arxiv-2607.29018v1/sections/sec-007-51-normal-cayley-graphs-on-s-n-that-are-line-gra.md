---
doc_id: arxiv-2607.29018v1
doc_title: "The Aldous property for normal Cayley graphs on symmetric groups"
section_id: sec-007-51-normal-cayley-graphs-on-s-n-that-are-line-gra
section_title: "Normal Cayley graphs on $S_n$ that are line graphs"
section_number: 5.1
pages: 12-17
source_pdf: 2607.29018v1.pdf
source_sha256: 789faa122dd32290
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.904
latex_coverage_ratio: 1.0
doc_brief: "The Aldous property for normal Cayley graphs on symmetric groups — Aldous’ spectral gap conjecture states that the random walk and the interchange process on any connected graph have the same"
---
The *line graph* of a graph $\Gamma$ is the graph whose vertices correspond to the edges of $\Gamma$, where two vertices are adjacent if and only if the corresponding edges in $\Gamma$ share exactly one end-vertex. A graph is called a *line graph* if it is isomorphic to the line graph of some graph. The following result gives a classification of normal Cayley graphs on $S_n$ that are line graphs.

::: thm
[]{#class-linegraph label="class-linegraph"} Let $n\ge 2$, and let $S$ be a nonempty normal set in $S_n$. Then $\mathrm{Cay}(S_n,S)$ is a line graph if and only if one of the following holds:

1.  $S=S_n\setminus\{e\}$, and hence $\mathrm{Cay}(S_n,S)\cong K_{n!}$;

2.  $S=A_n\setminus\{e\}$, and hence $\mathrm{Cay}(S_n,S)\cong 2K_{n!/2}$;

3.  $n=4$ and $S=\{(1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\}$, and hence $\mathrm{Cay}(S_n,S)\cong 6K_4$.
:::

Our proof of Theorem [\[class-linegraph\]](#class-linegraph){reference-type="ref" reference="class-linegraph"} is based on Beineke's characterization of line graphs. In 1970, he proved [@Beineke1970] that a graph is a line graph if and only if it does not contain any one of the nine forbidden graphs as an induced subgraph. For our purposes, we only show two of these nine forbidden subgraphs, denoted by $H_1$ and $H_2$, in Figure [3](#fig:H1H2){reference-type="ref" reference="fig:H1H2"}.

<figure id="fig:H1H2">
<figure id="fig:sub-a">

<figcaption><span class="math inline"><em>H</em><sub>1</sub></span></figcaption>
</figure>
<figure id="fig:sub-b">

<figcaption><span class="math inline"><em>H</em><sub>2</sub></span></figcaption>
</figure>
<figcaption>Two forbidden subgraphs for line graphs</figcaption>
</figure>

The following lemma deals with the case when the connection set contains all transpositions. In its proof we write $x\sim y$ to denote that $x$ and $y$ are adjacent in the Cayley graph $\mathrm{Cay}(S_n, S)$ under consideration.

::: lem
[]{#2-cycle-linegraph label="2-cycle-linegraph"} Let $n \ge 2$, and let $S$ be a nonempty normal set in $S_n$ which contains the conjugacy class of all transpositions. Then $\mathrm{Cay}(S_n, S)$ is a line graph if and only if $S = S_n \setminus \{e\}$, or equivalently, $\mathrm{Cay}(S_n, S) \cong K_{n!}$.
:::

::: proof
*Proof.* The sufficiency is obvious. It remains to prove the necessity.

Suppose that $\mathrm{Cay}(S_n, S)$ is a line graph. Then by Beineke's characterization it does not contain $H_1$ or $H_2$ (see Figure [3](#fig:H1H2){reference-type="ref" reference="fig:H1H2"}) as an induced subgraph. We aim to prove that every permutation $\sigma \in S_n$ with $|\mathrm{supp}(\sigma)| \ge 2$ belongs to $S$. We prove this statement by induction on $|\mathrm{supp}(\sigma)|$. If $|\mathrm{supp}(\sigma)|=2$, then the statement follows from the assumption that $S$ contains all transpositions. If $|\mathrm{supp}(\sigma)|=3$, then $\sigma \in S$, for otherwise an induced subgraph of $\mathrm{Cay}(S_n, S)$ isomorphic to $H_2$ can be easily found by taking $\delta=e$, $\tau_1=(1\,2)$, $\tau_2=(2\,3)$, and $\tau_3=(1\,3)$ in Figure [3](#fig:H1H2){reference-type="ref" reference="fig:H1H2"}.

Assume inductively that for some $k \ge 4$ every permutation in $S_n$ with support size at most $k-1$ belongs to $S$. We now show that for an arbitrary permutation $\sigma \in S_n$ with $|\mathrm{supp}(\sigma)|=k$ we must have $\sigma \in S$. Suppose first that the cycle decomposition of $\sigma$ contains a cycle of length at least $3$. Then we may write without loss of generality that $\sigma=(1\,2\,\cdots\,t)\sigma'$ for some $t\ge 3$ and $\sigma' \in S_n$. Set $$\delta=e,\qquad
\tau_1=(2\,3\,\cdots\,t)\sigma',\qquad
\tau_2=(1\,3\,\cdots\,t)\sigma',\qquad
\tau_3=(3\,\cdots\,t)\sigma',\qquad
\omega=\sigma.$$ By the induction hypothesis, $e \sim \tau_i$ for $1\le i\le 3$. Moreover, a direct computation shows that $\tau_i^{-1}\tau_j$ for $1\le i<j\le 3$ and $\tau_i^{-1}\sigma$ for $1\le i\le 3$ are $2$-cycles or $3$-cycles. Since by our induction hypothesis all $2$-cycles and $3$-cycles belong to $S$, we have $\tau_i \sim \sigma$ for $1\le i\le 3$ and $\tau_i\sim\tau_j$ for all $1\le i<j\le 3$. Since $\mathrm{Cay}(S_n,S)$ does not contain an induced subgraph isomorphic to $H_1$, we must have $e\sim\sigma$ and therefore $\sigma\in S$.

It remains to consider the case when the cycle decomposition of $\sigma$ contains only cycles of lengths $1$ and $2$. Since $|\mathrm{supp}(\sigma)| = k \ge 4$, we may assume without loss of generality that $\sigma=(1\,2)(3\,4)\sigma'$ for some $\sigma' \in S_n$. Let $$\delta=e,\qquad
\tau_1=(1\,2\,3)\sigma',\qquad
\tau_2=(1\,2\,3\,4)\sigma',\qquad
\tau_3=(1\,2\,4\,3)\sigma',\qquad
\omega=\sigma.$$ By what we proved in the previous paragraph, we have $e\sim\tau_i$ for $1\le i\le 3$. Moreover, a direct computation shows that $\tau_i^{-1}\tau_j$ for $1\le i<j\le 3$ and $\tau_i^{-1}\sigma$ for $1\le i\le 3$ have supports of size at most $3$. Since by our induction hypothesis all $2$-cycles and $3$-cycles belong to $S$, we have $\tau_i \sim \sigma$ for $1\le i\le 3$ and $\tau_i\sim\tau_j$ for all $1\le i<j\le 3$. Since $\mathrm{Cay}(S_n,S)$ does not contain an induced subgraph isomorphic to $H_1$, we must have $e\sim\sigma$ and hence $\sigma\in S$.

So, by mathematical induction, we have proved that $S$ contains every permutation in $S_n$ with support size at least $2$. Therefore, $S=S_n\setminus\{e\},$ or equivalently, $\mathrm{Cay}(S_n,S) \cong K_{n!}.$ ◻
:::

The next lemma deals with the case when the connection set does not contain the conjugacy class of transpositions but contains the conjugacy class of $3$-cycles.

::: lem
[]{#3-cycle-linegraph label="3-cycle-linegraph"} Let $n\ge 3$, and let $S$ be a nonempty normal set in $S_n$ which contains the conjugacy class of $3$-cycles but not the conjugacy class of transpositions. Then $\mathrm{Cay}(S_n,S)$ is a line graph if and only if $S=A_n\setminus\{e\}$, in which case $\mathrm{Cay}(S_n,S) \cong 2 K_{n!/2}$.
:::

::: proof
*Proof.* The sufficiency is obvious. We prove the necessity.

Suppose that $\mathrm{Cay}(S_n, S)$ is a line graph. Then by Beineke's characterization it does not contain $H_1$ or $H_2$ (see Figure [3](#fig:H1H2){reference-type="ref" reference="fig:H1H2"}) as an induced subgraph. We first show that $A_n\setminus\{e\}\subseteq S,$ that is, every permutation $\sigma\in A_n$ with $|\mathrm{supp}(\sigma)|\ge 3$ belongs to $S$. We prove this statement by induction on $|\mathrm{supp}(\sigma)|$. Clearly, if $|\mathrm{supp}(\sigma)|=3$, the statement follows from our assumption that $S$ contains all 3-cycles.

Let $\sigma \in A_n$ be such that $|\mathrm{supp}(\sigma)|=4$. Since $\sigma$ is an even permutation, without loss of generality we may assume that $\sigma=(1\,2)(3\,4).$ Suppose, for a contradiction, that $\sigma \notin S$. Since $S$ is a union of conjugacy classes, this assumption implies that no permutation with cycle type $(2,2, 1, \ldots, 1)$ belongs to $S$. Let $$\delta=e,\qquad
\tau_1=(1\,2\,3),\qquad
\tau_2=(1\,3\,4),\qquad
\tau_3=(2\,4\,3).$$ Then, by our assumption, $e \sim \tau_i$ for $1\le i\le 3$. A direct calculation leads to $$\begin{aligned}
\tau_1^{-1}\tau_2 =  (1\,4)(2\,3), \qquad
\tau_1^{-1}\tau_3 =  (1\,2)(3\,4), \qquad
\tau_2^{-1}\tau_3 =  (1\,3)(2\,4).
\end{aligned}$$ Therefore, $\tau_1$, $\tau_2$, and $\tau_3$ are mutually nonadjacent in $\mathrm{Cay}(S_n,S)$. Consequently, the subgraph induced by $\{e, \tau_1, \tau_2, \tau_3\}$ is isomorphic to the forbidden subgraph $H_2$ in Figure [3](#fig:H1H2){reference-type="ref" reference="fig:H1H2"}, a contradiction. Hence $\sigma \in S$.

Assume inductively that for some $k\ge 5$ every even permutation with support size at most $k-1$ belongs to $S$. Let $\sigma\in A_n$ be such that $|\mathrm{supp}(\sigma)|=k$. We aim to show that $\sigma\in S$. If the cycle decomposition of $\sigma$ contains an odd cycle of length at least $5$, then we may assume without loss of generality that $\sigma=(1\,2\,3\,\cdots\,t)\sigma'$ for some odd $t\ge 5$ and $\sigma' \in A_n$. Note that $t \le k$. Let $$\delta=e,\qquad
\tau_1=(1\,2\,3)\sigma',\qquad
\tau_2=(2\,3\,4)\sigma',\qquad
\tau_3=(1\,3\,4)\sigma',\qquad
\omega=\sigma.$$ Then each $\tau_i$ is an even permutation with support size at most $k-2$, and hence $e\sim\tau_i$ for $1\le i\le 3$ by the induction hypothesis. Moreover, each $\tau_i^{-1}\omega$ is an even permutation with support size at most $t-1$ ($\le k-1$), and so $\tau_i \sim \sigma$ for $1\le i\le 3$. Also, each $\tau_i^{-1}\tau_j$ is an even permutation with support size at most $4$, and hence $\tau_i\sim\tau_j$ for $1\le i<j\le 3$ by the induction hypothesis. Since $\mathrm{Cay}(S_n,S)$ is a line graph, it does not contain $H_1$ as an induced subgraph. Thus, we must have $e \sim \sigma$, that is, $\sigma\in S$.

If the cycle decomposition of $\sigma$ contains an even cycle of length at least $4$, then we may assume without loss of generality that $\sigma=(1\,2\,3\,\cdots\,t)\sigma'$ for some even $t\ge 4$ and $\sigma' \in S_n$, and we set $$\delta=e,\qquad
\tau_1=(1\,2)\sigma',\qquad
\tau_2=(2\,3)\sigma',\qquad
\tau_3=(1\,3)\sigma',\qquad
\omega=\sigma.$$ If the cycle decomposition of $\sigma$ contains both a $2$-cycle and a $3$-cycle, then we may assume without loss of generality that $\sigma=(1\,2\,3)(4\,5)\sigma'$ for some $\sigma' \in S_n$, and we set $$\delta=e,\qquad
\tau_1=(1\,2)\sigma',\qquad
\tau_2=(2\,3)\sigma',\qquad
\tau_3=(1\,3)\sigma',\qquad
\omega=\sigma.$$ If the cycle decomposition of $\sigma$ contains only $3$-cycles, then since $|\mathrm{supp}(\sigma)|=k\ge 5$ we may assume without loss of generality that $\sigma=(1\,2\,3)(4\,5\,6)\sigma'$ for some $\sigma' \in A_n$, and we set $$\delta=e,\qquad
\tau_1=(1\,2)(4\,5)\sigma',\qquad
\tau_2=(2\,3)(4\,5)\sigma',\qquad
\tau_3=(1\,3)(4\,5)\sigma',\qquad
\omega=\sigma.$$ Finally, if the cycle decomposition of $\sigma$ contains only $2$-cycles, then since $|\mathrm{supp}(\sigma)|=k\ge 5$ we may assume without loss of generality that $\sigma=(1\,2)(3\,4)(5\,6)\sigma'$ for $\sigma' \in S_n$, and we set $$\delta=e,\qquad
\tau_1=(1\,2)\sigma',\qquad
\tau_2=(3\,4)\sigma',\qquad
\tau_3=(5\,6)\sigma',\qquad
\omega=\sigma.$$ In each case, arguing exactly as in the previous paragraph, we obtain that $\sigma\in S$.

So, by mathematical induction, we have proved that $A_n\setminus\{e\}\subseteq S.$ To prove $S=A_n\setminus\{e\},$ it suffices to show that no odd permutation $\sigma\in S_n$ with $|\mathrm{supp}(\sigma)|\ge 4$ belongs to $S$. Assume for a contradiction that $\sigma\in S$ is odd and $|\mathrm{supp}(\sigma)|\ge 4$. Since $|\mathrm{supp}(\sigma)|\ge 4$, we can find two distinct permutations $\sigma_1$ and $\sigma_2$ in the conjugacy class $C(S_n,\sigma)$, both different from $\sigma$. Since $\sigma\in S$ and $S$ is a normal set, we have $\sigma_1, \sigma_2\in S$. Let $$\delta=e,\qquad
\tau_1=\sigma,\qquad
\tau_2=\sigma_1,\qquad
\tau_3=\sigma_2,\qquad
\omega=(1\,2).$$ Then $\delta\sim\tau_i$ for $1\le i\le 3$. Moreover, each $\tau_i^{-1}\omega$ is an even permutation, and hence $\tau_i\sim\omega$ for $1\le i\le 3$. Also, each $\tau_i^{-1}\tau_j$ is an even permutation, and hence $\tau_i\sim\tau_j$ for $1\le i<j\le 3$. On the other hand, since by our assumption the transposition $(1\,2)$ does not belong to $S$, $\delta$ and $\omega$ are not adjacent in $\mathrm{Cay}(S_n,S)$. Therefore, the subgraph of $\mathrm{Cay}(S_n,S)$ induced by $\{\delta,\tau_1,\tau_2,\tau_3,\omega\}$ is isomorphic to $H_1$, a contradiction. Therefore, $S=A_n\setminus\{e\}$ and consequently $\mathrm{Cay}(S_n,S) \cong 2 K_{n!/2}$. ◻
:::

We are now ready to prove Theorem [\[class-linegraph\]](#class-linegraph){reference-type="ref" reference="class-linegraph"}.

::: proof
*Proof of Theorem [\[class-linegraph\]](#class-linegraph){reference-type="ref" reference="class-linegraph"}.* The sufficiency is obvious, so it remains to prove the necessity.

Suppose that $S$ is a nonempty normal set in $S_n$ such that $\mathrm{Cay}(S_n,S)$ is a line graph. If $S$ contains the conjugacy class of transpositions, then by Lemma [\[2-cycle-linegraph\]](#2-cycle-linegraph){reference-type="ref" reference="2-cycle-linegraph"}, $S=S_n\setminus\{e\}$, and hence $\mathrm{Cay}(S_n,S)\cong K_{n!}$. If $S$ does not contain the conjugacy class of transpositions but contains the conjugacy class of $3$-cycles, then by Lemma [\[3-cycle-linegraph\]](#3-cycle-linegraph){reference-type="ref" reference="3-cycle-linegraph"}, $S=A_n\setminus\{e\}$, and hence $\mathrm{Cay}(S_n,S)\cong 2K_{n!/2}$. Therefore, we may assume in the sequel that $|\mathrm{supp}(\sigma)|\ge 4$ for every $\sigma\in S$.

If $S$ contains an element $\sigma$ whose cycle decomposition contains a cycle of length at least $4$, then we may assume without loss of generality that $\sigma=(1\,2\,3\,4\,\cdots\,t)\sigma'$ for some $t\ge 4$ and $\sigma' \in S_n$. Let $$\delta=e,\qquad
\tau_1=(1\,2\,3\,4\,\cdots\,t)\sigma',\qquad
\tau_2=(1\,3\,4\,\cdots\,t\,2)\sigma',\qquad
\tau_3=(1\,3\,2\,4\,\cdots\,t)\sigma'.$$ Since $\tau_1$, $\tau_2$, and $\tau_3$ all lie in the conjugacy class of $\sigma$, we have $\tau_i\in S$ for $1\le i\le 3$, and hence $\delta\sim\tau_i$ for $1\le i\le 3$. Moreover, each $\tau_i^{-1}\tau_j$ is a $3$-cycle, and hence by our assumption $\tau_i$ and $\tau_j$ are not adjacent in $\mathrm{Cay}(S_n,S)$ for $1\le i<j\le 3$. Therefore, the subgraph induced by $\{\delta,\tau_1,\tau_2,\tau_3\}$ is isomorphic to $H_2$ in Figure [3](#fig:H1H2){reference-type="ref" reference="fig:H1H2"}, but this contradicts our assumption that $\mathrm{Cay}(S_n,S)$ is a line graph.

If $S$ contains an element $\sigma$ whose cycle decomposition contains both a $2$-cycle and a $3$-cycle, then we may assume without loss of generality that $\sigma=(1\,2)(3\,4\,5)\sigma'$ for some $\sigma' \in S_n$. Let $$\delta=e,\qquad
\tau_1=(1\,2)(3\,4\,5)\sigma',\qquad
\tau_2=(1\,2)(3\,5\,4)\sigma',\qquad
\tau_3=(3\,5)(1\,4\,2)\sigma'.$$ Arguing as above, we have $\delta\sim\tau_i$ for $1\le i\le 3$ and $\tau_i$ and $\tau_j$ are not adjacent in $\mathrm{Cay}(S_n,S)$ for $1\le i<j\le 3$. Therefore, the subgraph of $\mathrm{Cay}(S_n,S)$ induced by $\{\delta,\tau_1,\tau_2,\tau_3\}$ is isomorphic to $H_2$ in Figure [3](#fig:H1H2){reference-type="ref" reference="fig:H1H2"}, contradicting the assumption that $\mathrm{Cay}(S_n,S)$ is a line graph.

If $S$ contains an element $\sigma$ whose cycle decomposition contains only $3$-cycles, then, since $|\mathrm{supp}(\sigma)|\ge 4$, we may assume without loss of generality that $\sigma=(1\,2\,3)(4\,5\,6)\sigma'$ for some $\sigma' \in S_n$. Let $$\delta=e,\qquad
\tau_1=(1\,2\,3)(4\,5\,6)\sigma',\qquad
\tau_2=(1\,6\,2)(3\,4\,5)\sigma',\qquad
\tau_3=(1\,4\,2)(3\,5\,6)\sigma'.$$ Then $\delta\sim\tau_i$ for $1\le i\le 3$. Moreover, each $\tau_i^{-1}\tau_j$ is a $5$-cycle. Since we have already shown that no $5$-cycle lies in $S$, it follows that $\tau_i$ and $\tau_j$ are not adjacent in $\mathrm{Cay}(S_n,S)$ for $1\le i<j\le 3$. Therefore, the subgraph of $\mathrm{Cay}(S_n,S)$ induced by $\{\delta,\tau_1,\tau_2,\tau_3\}$ is isomorphic to $H_2$ in Figure [3](#fig:H1H2){reference-type="ref" reference="fig:H1H2"}, a contradiction.

If $n\ge 5$ and $S$ contains an element $\sigma$ with at least one fixed point whose cycle decomposition contains only $2$-cycles, then, since $|\mathrm{supp}(\sigma)|\ge 4$, we may assume without loss of generality that $5 \notin \mathrm{supp}(\sigma)$ and $\sigma=(1\,2)(3\,4)\sigma'$ for some $\sigma' \in S_n$. Let $$\delta=e,\qquad
\tau_1=(1\,2)(3\,4)\sigma',\qquad
\tau_2=(1\,5)(3\,4)\sigma',\qquad
\tau_3=(2\,5)(3\,4)\sigma'.$$ Arguing as above, we have $\delta\sim\tau_i$ for $1\le i\le 3$ and $\tau_i$ and $\tau_j$ are not adjacent in $\mathrm{Cay}(S_n,S)$ for $1\le i<j\le 3$. Therefore, the subgraph of $\mathrm{Cay}(S_n,S)$ induced by $\{\delta,\tau_1,\tau_2,\tau_3\}$ is isomorphic to $H_2$ in Figure [3](#fig:H1H2){reference-type="ref" reference="fig:H1H2"}, and hence $\mathrm{Cay}(S_n,S)$ cannot be a line graph, a contradiction.

If $n\ge 5$ and $S$ contains an element $\sigma$ with no fixed point whose cycle decomposition consists only of $2$-cycles, then, since $n\ge 5$, we may assume without loss of generality that $\sigma=(1\,2)(3\,4)(5\,6)\sigma'$ for some $\sigma' \in S_n$. Let $$\delta=e,\qquad
\tau_1=(1\,2)(3\,4)(5\,6)\sigma',\qquad
\tau_2=(1\,3)(2\,5)(4\,6)\sigma',\qquad
\tau_3=(1\,4)(2\,6)(3\,5)\sigma'.$$ Then $\delta\sim\tau_i$ for $1\le i\le 3$. Moreover, the cycle decomposition of each $\tau_i^{-1}\tau_j$ consists of two $3$-cycles for $1\le i<j\le 3$. Since we have already shown that no element of $S$ contains a $3$-cycle, it follows that $\tau_i$ and $\tau_j$ are not adjacent in $\mathrm{Cay}(S_n,S)$ for $1\le i<j\le 3$. Therefore, the subgraph of $\mathrm{Cay}(S_n,S)$ induced by $\{\delta,\tau_1,\tau_2,\tau_3\}$ is isomorphic to $H_2$ in Figure [3](#fig:H1H2){reference-type="ref" reference="fig:H1H2"}, and hence $\mathrm{Cay}(S_n,S)$ cannot be a line graph, a contradiction.

Summing up, the only remaining case is that $n=4$ and $S$ contains an element $\sigma$ whose cycle decomposition contains only $2$-cycles. In this case, we have $S=\{(1\,2)(3\,4), \allowbreak (1\,3)(2\,4), \allowbreak (1\,4)(2\,3)\}$, and hence $\mathrm{Cay}(S_n,S)\cong 6K_4$. This completes the proof. ◻
:::
