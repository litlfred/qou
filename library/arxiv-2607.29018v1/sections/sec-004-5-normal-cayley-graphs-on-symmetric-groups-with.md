---
doc_id: arxiv-2607.29018v1
doc_title: "The Aldous property for normal Cayley graphs on symmetric groups"
section_id: sec-004-5-normal-cayley-graphs-on-symmetric-groups-with
section_title: "Normal Cayley graphs on symmetric groups with strictly second largest eigenvalue at most 1"
section_number: 5
pages: 12-23
source_pdf: 2607.29018v1.pdf
source_sha256: 789faa122dd32290
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 0.686
---
[]{#line-graph label="line-graph"}

This section is a preparation for our proof of Theorem [\[thm:main2\]](#thm:main2){reference-type="ref" reference="thm:main2"} to be given in the next section. However, the main results in this section, Theorems [\[class-linegraph\]](#class-linegraph){reference-type="ref" reference="class-linegraph"} and [\[sn-cay-sec-1\]](#sn-cay-sec-1){reference-type="ref" reference="sn-cay-sec-1"}, are also of interest for their own sake.

## Normal Cayley graphs on $S_n$ that are line graphs

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

## Normal Cayley graphs on $S_n$ with strictly second largest eigenvalue at most $1$

A *cocktail party graph* is a graph obtained from a complete graph with even order by deleting a perfect matching. In 2010, Stanić [@Stanic2010] obtained the following complete classification of connected regular graphs with the second largest eigenvalue at most $1$.

::: thm
[]{#second-ev-1 label="second-ev-1"} Every connected regular graph with the second largest eigenvalue at most $1$ is the complement of a (not necessarily connected) regular graph, where each connected component is either a connected regular line graph, a cocktail party graph, or one of the 187 exceptional connected regular graphs with order from 8 to 28 and degree from 3 to 16 described in [@CRS2004 pp. 213--227].
:::

Using Theorems [\[second-ev-1\]](#second-ev-1){reference-type="ref" reference="second-ev-1"} and [\[class-linegraph\]](#class-linegraph){reference-type="ref" reference="class-linegraph"}, we obtain the following classification of normal Cayley graphs on $S_n$ with strictly second largest eigenvalue at most $1$.

::: thm
[]{#sn-cay-sec-1 label="sn-cay-sec-1"} Let $n\ge 5$, and let $S$ be a nonempty normal set in $S_n$. Then the strictly second largest eigenvalue of $\mathrm{Cay}(S_n,S)$ is at most $1$ if and only if one of the following holds:

1.  $S=S_n\setminus\{e\}$, and hence $\mathrm{Cay}(S_n,S)\cong K_{n!}$;

2.  $S=S_n\setminus \, A_n$, and hence $\mathrm{Cay}(S_n,S)\cong K_{n!/2,n!/2}$;

3.  $S=A_n\setminus\{e\}$, and hence $\mathrm{Cay}(S_n,S)\cong 2K_{n!/2}$.
:::

::: proof
*Proof.* Let $n\ge 5$ and $S$ be a nonempty normal set in $S_n$. If $S=S_n\setminus\{e\}, S_n\setminus A_n$ or $A_n\setminus\{e\}$, then $\mathrm{Cay}(S_n,S)\cong K_{n!}, K_{n!/2,n!/2}$ or $2K_{n!/2}$, respectively. Note that $K_{n!}$ has distinct eigenvalues $n!-1$ and $-1$, $K_{n!/2,n!/2}$ has distinct eigenvalues $n!/2$, $0$ and $-n!/2$, and $2K_{n!/2}$ has distinct eigenvalues $n!/2-1$ and $-1$. In all three cases, the strictly second largest eigenvalue of $\mathrm{Cay}(S_n,S)$ is at most $1$. This proves the sufficiency.

We now prove the necessity. Suppose that the strictly second largest eigenvalue of $\mathrm{Cay}(S_n,S)$ is at most $1$.

[Case 1.]{.sans-serif} $\mathrm{Cay}(S_n,S)$ is connected.

In this case, we have $\langle S \rangle = S_n$. Since $S$ is a normal set in $S_n$, so is $S^c=(S_n\setminus\{e\})\setminus S$, and hence $\langle S^c\rangle$ is a normal subgroup of $S_n$. As $n \ge 5$, we have $\langle S^c\rangle = \{e\},A_n$ or $S_n$. If $\langle S^c\rangle=\{e\}$, then $S^c=\emptyset$, so $S=S_n\setminus\{e\}$ and $\mathrm{Cay}(S_n,S)\cong K_{n!}$.

Assume that $\langle S^c\rangle$ is either $A_n$ or $S_n$. Since $n\ge 5$, every connected component of $\mathrm{Cay}(S_n,S^c)$ has at least $5!/2=60$ vertices. Since $\lambda_2(\mathrm{Cay}(S_n,S))\le 1$, by Theorem [\[second-ev-1\]](#second-ev-1){reference-type="ref" reference="second-ev-1"}, each connected component of $\mathrm{Cay}(S_n,S^c)$ is either a regular line graph, a cocktail party graph, or one of the 187 exceptional connected regular graphs. But all these exceptional graphs have at most $28$ vertices, so none of them can be a connected component of $\mathrm{Cay}(S_n,S^c)$.

Suppose that some connected component of $\mathrm{Cay}(S_n,S^c)$ is a cocktail party graph. Then the complement of the subgraph of $\mathrm{Cay}(S_n,S^c)$ induced by $\langle S^c\rangle$ is $1$-regular. Hence $S^c$ omits exactly one nonidentity element of $\langle S^c\rangle$. Since $S^c$ is a union of conjugacy classes of $S_n$, this would give a conjugacy class of size $1$ in $S_n$ other than $\{e\}$, contradicting the fact that the center of $S_n$ is trivial for $n\ge 5$. Therefore, no connected component of $\mathrm{Cay}(S_n,S^c)$ is a cocktail party graph.

Thus every connected component of $\mathrm{Cay}(S_n,S^c)$ is a regular line graph. Since a disjoint union of line graphs is again a line graph, $\mathrm{Cay}(S_n,S^c)$ is itself a line graph. It follows from Theorem [\[class-linegraph\]](#class-linegraph){reference-type="ref" reference="class-linegraph"} that either $S^c=S_n\setminus\{e\}$ or $S^c=A_n\setminus\{e\}$. The former is impossible since it would imply $S=\emptyset$. Thus, the only possibility is that $S^c=A_n\setminus\{e\}$. Hence $S=S_n\setminus A_n$ and therefore $\mathrm{Cay}(S_n,S)\cong K_{n!/2,n!/2}$.

[Case 2.]{.sans-serif} $\mathrm{Cay}(S_n,S)$ is disconnected.

In this case, we have $\langle S\rangle=A_n$. Set $S^*=(A_n\setminus\{e\})\setminus S.$ Then $\mathrm{Cay}(A_n,S^*)$ is the complement of $\mathrm{Cay}(A_n,S)$. If $S^*=\emptyset$, then $S=A_n\setminus\{e\}$, and hence $\mathrm{Cay}(S_n,S)\cong 2K_{n!/2}$.

Assume that $S^*\neq\emptyset$. Since $S$ is a normal set in $S_n$, $S^*$ is a union of conjugacy classes of both $S_n$ and $A_n$. Since $A_n$ is simple for $n\ge 5$, the nonempty normal set $S^*$ generates $A_n$, and hence $\mathrm{Cay}(A_n,S^*)$ is connected. As $\lambda_2(\mathrm{Cay}(A_n,S))\le 1$, Theorem [\[second-ev-1\]](#second-ev-1){reference-type="ref" reference="second-ev-1"} implies that $\mathrm{Cay}(A_n,S^*)$ is either a regular line graph, a cocktail party graph, or one of the 187 exceptional connected regular graphs. The same arguments as in Case 1 show that it is neither a cocktail party graph nor an exceptional graph. Hence $\mathrm{Cay}(A_n,S^*)$ must be a line graph. Therefore, $\mathrm{Cay}(S_n,S^*)$, which is the disjoint union of two copies of $\mathrm{Cay}(A_n,S^*)$, is also a line graph. Moreover, $S^*$ is a union of conjugacy classes of $S_n$. Therefore, by Theorem [\[class-linegraph\]](#class-linegraph){reference-type="ref" reference="class-linegraph"}, we have either $S^*=S_n\setminus\{e\}$ or $S^*=A_n\setminus\{e\}$. Since $S^*\subseteq A_n$, it follows that $S^*=A_n\setminus\{e\}$. This forces $S=\emptyset$, contradicting the fact that $\langle S\rangle=A_n$. ◻
:::

# Proofs of Theorem [\[thm:main2\]](#thm:main2){reference-type="ref" reference="thm:main2"} and Corollary [\[cor:main2\]](#cor:main2){reference-type="ref" reference="cor:main2"} {#supp-large}

With the preparation in the previous section, we can finally prove Theorem [\[thm:main2\]](#thm:main2){reference-type="ref" reference="thm:main2"} and Corollary [\[cor:main2\]](#cor:main2){reference-type="ref" reference="cor:main2"}.

::: proof
*Proof of Theorem [\[thm:main2\]](#thm:main2){reference-type="ref" reference="thm:main2"}.* Let $n\ge 5$, and let $S$ be a nonempty normal set in $S_n$. Let $A_S, B_S$ and $C_S$ be as in [\[eq:ABCS\]](#eq:ABCS){reference-type="eqref" reference="eq:ABCS"}. Then $S=A_S \cup B_S \cup C_S$. Since $\mathrm{Cay}(S_n, S)$ is normal, by [\[eq:eigen-chara\]](#eq:eigen-chara){reference-type="eqref" reference="eq:eigen-chara"} and Table [\[tab:tab1\]](#tab:tab1){reference-type="ref" reference="tab:tab1"}, its eigenvalue corresponding to the partition $(n-1,1)$ is $$\begin{aligned}
\lambda_{(n-1,1)}
& = \sum_{\sigma \in S} \tilde{\chi}_{(n-1,1)}(\sigma) \nonumber \\ 
& = \frac{1}{n-1} \sum_{\sigma \in S} (|\mathrm{fix}(\sigma)|-1) \nonumber \\ 
& = \frac{1}{n-1} \left(\sum_{\sigma \in A_S} (|\mathrm{fix}(\sigma)|-1) - \sum_{\sigma \in C_S} 1\right) \nonumber \\ 
& = \frac{1}{n-1} \left(\left(\sum_{\sigma \in A_S} |\mathrm{fix}(\sigma)|\right) - (|A_S|+|C_S|)\right). \label{eq:abc}
\end{aligned}$$

By our assumption [\[eq:ABC\]](#eq:ABC){reference-type="eqref" reference="eq:ABC"} and equation [\[eq:abc\]](#eq:abc){reference-type="eqref" reference="eq:abc"}, we have $\lambda_{(n-1,1)}\le 1$.

[Necessity.]{.sans-serif} Suppose that $\mathrm{Cay}(S_n,S)$ has the Aldous property. Then its strictly second largest eigenvalue, which is attained by the standard representation $\rho_{(n-1,1)}$, is $\lambda_{(n-1,1)}\le 1$. By Theorem [\[sn-cay-sec-1\]](#sn-cay-sec-1){reference-type="ref" reference="sn-cay-sec-1"}, we have $S \in \{S_n\setminus\{e\}, S_n\setminus A_n, A_n\setminus\{e\}\}$.

[Sufficiency.]{.sans-serif} If $S=S_n\setminus\{e\}$, then $\mathrm{Cay}(S_n,S)\cong K_{n!}$ has spectrum $\{(n!-1)^1,(-1)^{n!-1}\}.$ The eigenvalue $n!-1$ is attained by $\rho_{(n)}$, while the strictly second largest eigenvalue $-1$ is attained by $\rho_{(n-1,1)}$.

If $S=S_n\setminus A_n$, then $\mathrm{Cay}(S_n,S)\cong K_{n!/2,n!/2}$ has spectrum $\left\{\left(\frac{n!}{2}\right)^1,0^{n!-2},\left(-\frac{n!}{2}\right)^1\right\}.$ The eigenvalue $\frac{n!}{2}$ is attained by $\rho_{(n)}$, the eigenvalue $-\frac{n!}{2}$ is attained by $\rho_{(1^n)}$, and the strictly second largest eigenvalue $0$ is attained by $\rho_{(n-1,1)}$.

If $S=A_n\setminus\{e\}$, then $\mathrm{Cay}(S_n,S)\cong 2K_{n!/2}$ has spectrum $\left\{\left(\frac{n!}{2}-1\right)^2,(-1)^{n!-2}\right\}.$ The eigenvalue $\frac{n!}{2}-1$ is attained by both $\rho_{(n)}$ and $\rho_{(1^n)}$, while the strictly second largest eigenvalue $-1$ is attained by $\rho_{(n-1,1)}$.

Therefore, in all three cases, $\mathrm{Cay}(S_n,S)$ has the Aldous property. Moreover, since in each case the strictly second largest eigenvalue is $\lambda_{(n-1,1)}\leq 1$, it follows from [\[eq:abc\]](#eq:abc){reference-type="eqref" reference="eq:abc"} that all three sets $S$ satisfy [\[eq:ABC\]](#eq:ABC){reference-type="eqref" reference="eq:ABC"}.

This proves the sufficiency and completes the proof. ◻
:::

::: proof
*Proof of Corollary [\[cor:main2\]](#cor:main2){reference-type="ref" reference="cor:main2"}.* Let $n\ge 5$, and let $S$ be a nonempty normal set in $S_n$.

\(a\) Suppose that $S \subseteq \mathrm{Supp}_n(\{n-1,n\})$. Then $A_S = \emptyset$, so $S$ satisfies condition [\[eq:ABC\]](#eq:ABC){reference-type="eqref" reference="eq:ABC"}. Hence Theorem [\[thm:main2\]](#thm:main2){reference-type="ref" reference="thm:main2"} applies to $\mathrm{Cay}(S_n,S)$. Since $n\ge 5$, each of $S_n\setminus\{e\}, S_n\setminus A_n$ and $A_n\setminus\{e\}$ contains an element whose support size is neither $n-1$ nor $n$. Thus, $S \notin \{S_n\setminus\{e\}, S_n\setminus A_n, A_n\setminus\{e\}\}$ and therefore, by Theorem [\[thm:main2\]](#thm:main2){reference-type="ref" reference="thm:main2"}, $\mathrm{Cay}(S_n,S)$ does not have the Aldous property.

\(b\) Suppose that $|\overline{A}_S|-|\overline{C}_S|+2(n-1) \ge 0$ and $S \notin \{S_n\setminus\{e\}, S_n\setminus A_n, A_n\setminus\{e\}\}$. By [\[eq:ABCS\]](#eq:ABCS){reference-type="eqref" reference="eq:ABCS"} and [\[eq:barABCS\]](#eq:barABCS){reference-type="eqref" reference="eq:barABCS"}, $\{A_S, \overline{A}_S, B_S, \overline{B}_S, C_S, \overline{C}_S\}$ is a partition of $S_{n} \setminus \{e\}$. Hence $$\label{sum-set-sn}
|A_S|+|\overline{A}_S|+|B_S|+|\overline{B}_S|+|C_S|+|\overline{C}_S| = n!-1.$$ Set $$\mathcal{X} = \{ (\sigma, i) \in S_n \times [n] : \sigma(i) = i \}.$$ We use double counting to enumerate $\mathcal{X}$. First, for each fixed $i$, there are exactly $(n-1)!$ permutations $\sigma \in S_n$ satisfying $\sigma(i) = i$. Therefore, $$\label{eq:fac}
|\mathcal{X}| = \sum_{i=1}^n |\{ \sigma \in S_n : \sigma(i) = i \}| = \sum_{i=1}^n (n-1)! = n!.$$ Second, each permutation $\sigma$ contributes exactly $|\mathrm{fix}(\sigma)|$ to the cardinality of $\mathcal{X}$. Thus, $$\begin{aligned}
    |\mathcal{X}| 
    &= 
    \sum_{\sigma \in S_n} |\mathrm{fix}(\sigma)|  \\
    &= 
    \sum_{k=0}^n \sum_{\sigma \in \mathrm{Supp}_n(k)} |\mathrm{fix}(\sigma)|   \\
    &=
    \sum_{\sigma \in \mathrm{Supp}_n(0)} |\mathrm{fix}(\sigma)|
    +
    \sum_{\sigma \in \mathrm{Supp}_n(1)} |\mathrm{fix}(\sigma)|
    +
    \sum_{k=2}^{n-1} \sum_{\sigma \in \mathrm{Supp}_n(k)} |\mathrm{fix}(\sigma)|
    +
    \sum_{\sigma \in \mathrm{Supp}_n(n)} |\mathrm{fix}(\sigma)|  \\
    &=
    n+0+
    \sum_{k=2}^{n-1} \sum_{\sigma \in \mathrm{Supp}_n(k)} |\mathrm{fix}(\sigma)|
    +0  \\
    &=
    n+\sum_{\sigma \in \mathrm{Supp}_n(\{2, 3, \ldots, n-2\})} |\mathrm{fix}(\sigma)|+\sum_{\sigma \in \mathrm{Supp}_n(n-1)} |\mathrm{fix}(\sigma)|.  
\end{aligned}$$ This together with [\[sum-set-sn\]](#sum-set-sn){reference-type="eqref" reference="sum-set-sn"} and [\[eq:fac\]](#eq:fac){reference-type="eqref" reference="eq:fac"} yields $$\begin{aligned}
\sum_{\sigma \in A_S} |\mathrm{fix}(\sigma)| + \sum_{\sigma \in \overline{A}_S} |\mathrm{fix}(\sigma)|
&= \sum_{\sigma \in \mathrm{Supp}_n(\{2, 3, \ldots, n-2\})} |\mathrm{fix}(\sigma)| \nonumber \\
&= n! - n - \sum_{\sigma \in \mathrm{Supp}_n(n-1)} |\mathrm{fix}(\sigma)| \label{eq:fac1} \\
&= n! - n - \sum_{\sigma \in B_S} |\mathrm{fix}(\sigma)| - \sum_{\sigma \in \overline{B}_S} |\mathrm{fix}(\sigma)| \nonumber \\ 
&= n! - n - |B_S| - |\overline{B}_S| \nonumber \\ 
&= |A_S| + |\overline{A}_S| + |C_S| + |\overline{C}_S| + 1 - n. \nonumber 
\end{aligned}$$ Since $|\overline{A}_S|-|\overline{C}_S|+2(n-1) \ge 0$ by our assumption, it follows that $$\begin{aligned}
|A_S| + |C_S| + n - 1 - \sum_{\sigma \in A_S} |\mathrm{fix}(\sigma)| 
&= \sum_{\sigma \in \overline{A}_S} |\mathrm{fix}(\sigma)|-|\overline{A}_S|-|\overline{C}_S|+2(n-1) \\
&= \sum_{\sigma \in \overline{A}_S} (|\mathrm{fix}(\sigma)|-1)-|\overline{C}_S|+2(n-1) \\
& \geq |\overline{A}_S|-|\overline{C}_S|+2(n-1) \\
& \geq 0.
\end{aligned}$$ That is, $S$ satisfies condition [\[eq:ABC\]](#eq:ABC){reference-type="eqref" reference="eq:ABC"}. Since $S \notin \{S_n\setminus\{e\}, S_n\setminus A_n, A_n\setminus\{e\}\}$ by our assumption, it follows from Theorem [\[thm:main2\]](#thm:main2){reference-type="ref" reference="thm:main2"} that $\mathrm{Cay}(S_n,S)$ does not have the Aldous property.

\(c\) Suppose that $\mathrm{Supp}_n(n)\subseteq S$ and $S \neq S_n\setminus\{e\}$. Since $\mathrm{Supp}_n(n)$ contains both even and odd permutations, $S$ is neither $S_n\setminus A_n$ nor $A_n\setminus\{e\}$. Moreover, $C_S = \mathrm{Supp}_n(n)$ and hence $\overline{C}_S = \emptyset$. Thus, $|\overline{A}_S|-|\overline{C}_S|+2(n-1) = |\overline{A}_S|+2(n-1) \ge 0$ and therefore by (b), $\mathrm{Cay}(S_n,S)$ does not have the Aldous property. ◻
:::

**Acknowledgements**  Chenhui Lv was supported by the Outstanding Doctoral Students Overseas Study Program of the University of Science and Technology of China. Sanming Zhou was supported by a Discovery Project (DP250104965) of the Australian Research Council.
