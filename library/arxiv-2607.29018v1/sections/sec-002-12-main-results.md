---
doc_id: arxiv-2607.29018v1
doc_title: "The Aldous property for normal Cayley graphs on symmetric groups"
section_id: sec-002-12-main-results
section_title: "Main results"
section_number: 1.2
pages: 5-7
source_pdf: 2607.29018v1.pdf
source_sha256: 789faa122dd32290
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.886
latex_coverage_ratio: 0.986
doc_brief: "The Aldous property for normal Cayley graphs on symmetric groups — Aldous’ spectral gap conjecture states that the random walk and the interchange process on any connected graph have the same"
---
A subset $S$ of $S_n \setminus \{e\}$ is called [@PP] a *normal set* in $S_n$ if it is the union of some conjugacy classes of $S_n$. Since in $S_n$ every element is conjugate to its inverse element, a Cayley graph $\mathrm{Cay}(S_n,S)$ on $S_n$ is normal if and only if $S$ is a normal set in $S_n$. Clearly, for a normal set $S$ in $S_n$, the set $$S^c=(S_n\setminus\{e\})\setminus S$$ is also a normal set in $S_n$, and moreover $\mathrm{Cay}(S_n,S)$ and $\mathrm{Cay}(S_n,S^c)$ are complements of each other. Throughout the paper, we denote by $K_n$ the complete graph of order $n$, by $K_{m,n}$ the complete bipartite graph with $m$ and $n$ vertices in the two partite sets respectively, and by $t\Gamma$ the vertex-disjoint union of $t$ copies of a graph $\Gamma$. The first main result in this paper is as follows.

::: thm
[]{#thm:complement label="thm:complement"} Let $n \ge 5$, and let $S$ be a nonempty normal set in $S_n$ with $S\neq S_n\setminus\{e\}$.

1.  If neither $S$ nor $S^c$ is equal to $A_n\setminus\{e\}$, then at most one of $\mathrm{Cay}(S_n,S)$ and $\mathrm{Cay}(S_n,S^c)$ has the Aldous property.

2.  If either $S$ or $S^c$ is equal to $A_n\setminus\{e\}$, then one of $\mathrm{Cay}(S_n, S)$ and $\mathrm{Cay}(S_n, S^c)$ is isomorphic to $2K_{n!/2}$ and the other to $K_{n!/2,n!/2}$, and moreover both graphs have the Aldous property.
:::

Theorem [\[thm:complement\]](#thm:complement){reference-type="ref" reference="thm:complement"} implies that at most half of all normal Cayley graphs on $S_n$ exhibit the Aldous property. This is true no matter whether isomorphism is taken into consideration because two normal Cayley graphs are isomorphic if and only if their complements are isomorphic.

The second main result in this paper, Theorem [\[thm:main1\]](#thm:main1){reference-type="ref" reference="thm:main1"} below, settles Problem [\[prob\]](#prob){reference-type="ref" reference="prob"} for sufficiently large $n$ and normal Cayley graphs whose connection sets consist of permutations with support size between $2$ and $n-2$. For a subset $S\subseteq S_n$, denote by $O(S)$ and $E(S)$ the sets of odd and even permutations in $S$, respectively.

::: thm
[]{#thm:main1 label="thm:main1"} There exists a positive integer $N \geq 5$ such that, for every $n\ge N$ and every nonempty normal set $S$ in $S_n$ satisfying $2 \le |\mathrm{supp}(\sigma)| \le n-2$ for all $\sigma\in S$, the following statements hold:

1.  if $E(S)=\emptyset$ or $O(S)=\emptyset$, then $\mathrm{Cay}(S_n,S)$ has the Aldous property;

2.  if $E(S)\ne\emptyset$ and $O(S)\ne\emptyset$, then $\mathrm{Cay}(S_n,S)$ has the Aldous property if and only if $$\label{eq:fix}
    \sum_{\sigma\in S} |\mathrm{fix}(\sigma)| \ge n|E(S)|-(n-2)|O(S)|;$$ moreover, if $\mathrm{Cay}(S_n,S)$ does not have the Aldous property, then its strictly second largest eigenvalue is attained by the sign representation of $S_n$.
:::

If $2 \le |\mathrm{supp}(\sigma)| \le n-2$ for all $\sigma\in S$, then $\sum_{\sigma\in S} |\mathrm{fix}(\sigma)| \geq 2|S| = 2|E(S)|+2|O(S)|$, and hence [\[eq:fix\]](#eq:fix){reference-type="eqref" reference="eq:fix"} is satisfied when $n|O(S)| \ge (n-2)|E(S)|$. So we obtain the following corollary of Theorem [\[thm:main1\]](#thm:main1){reference-type="ref" reference="thm:main1"} immediately.

::: cor
[]{#odd-even label="odd-even"} There exists a positive integer $N \ge 5$ such that, for every $n \ge N$ and every nonempty normal set $S$ in $S_n$ satisfying $2 \le |\mathrm{supp}(\sigma)| \le n-2$ for all $\sigma \in S$, if $n|O(S)| \ge (n-2)|E(S)|$, then $\mathrm{Cay}(S_n, S)$ has the Aldous property.
:::

Another corollary of Theorem [\[thm:main1\]](#thm:main1){reference-type="ref" reference="thm:main1"} is the following explicit formula for the second largest eigenvalue of normal Cayley graphs on the alternating group $A_n$.

::: cor
[]{#An-sec-eigen label="An-sec-eigen"} There exists a positive integer $N \ge 5$ such that, for every $n \ge N$ and every nonempty normal set $S$ in $S_n$, if $S \subseteq A_n$ and $2 \le |\mathrm{supp}(\sigma)| \le n-2$ for all $\sigma \in S$, then the strictly second largest eigenvalue of $\mathrm{Cay}(S_n, S)$ is given by $$\frac{1}{n-1} \big(\sum_{\sigma \in S} |\mathrm{fix}(\sigma)| - |S| \big),$$ and moreover $\mathrm{Cay}(S_n, S)$ is disconnected with two components each isomorphic to $\mathrm{Cay}(A_n, S)$.
:::

For a subset $S \subseteq S_n$, let $$\label{eq:ABCS}
A_S = S \cap \mathrm{Supp}_n(\{2,3,\ldots,n-2\}),\; B_S = S \cap \mathrm{Supp}_n(n-1),\; C_S = S \cap \mathrm{Supp}_n(n)$$ and $$\label{eq:barABCS}
\overline{A}_S = \mathrm{Supp}_n(\{2,3,\ldots,n-2\}) \setminus A_S,\; \overline{B}_S = \mathrm{Supp}_n(n-1)\setminus B_S,\; \overline{C}_S = \mathrm{Supp}_n(n)\setminus C_S.$$ The following theorem classifies all normal Cayley graphs $\mathrm{Cay}(S_n, S)$ that have the Aldous property under an easy-to-check condition.

::: thm
[]{#thm:main2 label="thm:main2"} Let $n\ge 5$, and let $S$ be a nonempty normal set in $S_n$. If $$\label{eq:ABC}
\sum_{\sigma\in A_S} |\mathrm{fix}(\sigma)| \le |A_S|+|C_S|+n-1,$$ then $\mathrm{Cay}(S_n, S)$ has the Aldous property if and only if $S = S_n\setminus\{e\}, S_n\setminus A_n$ or $A_n\setminus\{e\}$, or, equivalently, $\mathrm{Cay}(S_n,S)\cong K_{n!}, K_{n!/2,n!/2}$ or $2K_{n!/2}$, respectively.
:::

Note that condition [\[eq:ABC\]](#eq:ABC){reference-type="eqref" reference="eq:ABC"} holds only if either $A_S$ is empty or $C_S$ is nonempty. Theorem [\[thm:main2\]](#thm:main2){reference-type="ref" reference="thm:main2"} implies the following corollary.

::: cor
[]{#cor:main2 label="cor:main2"} Let $n\ge 5$, and let $S$ be a nonempty normal set in $S_n$. Then $\mathrm{Cay}(S_n,S)$ does not have the Aldous property if one of the following conditions holds:

1.  $S \subseteq \mathrm{Supp}_n(\{n-1,n\})$;

2.  $|\overline{A}_S|-|\overline{C}_S|+2(n-1) \ge 0$ and $S \notin \{S_n\setminus\{e\}, S_n\setminus A_n, A_n\setminus\{e\}\}$;

3.  $\mathrm{Supp}_n(n)\subseteq S$ and $S \neq S_n\setminus\{e\}$.
:::

In [@LXZ Problem 1.2], Li, Xia and Zhou ask for a necessary and sufficient condition for $\mathrm{Cay}(S_n, \mathrm{Supp}_n(I))$ with $\{n\} \subset I \subseteq \{2,3,\ldots,n-2,n\}$ to have the Aldous property for sufficiently large $n$. Solving this problem, part (c) of Corollary [\[cor:main2\]](#cor:main2){reference-type="ref" reference="cor:main2"} implies that such a graph $\mathrm{Cay}(S_n, \mathrm{Supp}_n(I))$ does not have the Aldous property for any $n \geq 5$.

Theorem [\[thm:main1\]](#thm:main1){reference-type="ref" reference="thm:main1"} and Corollary [\[cor:main2\]](#cor:main2){reference-type="ref" reference="cor:main2"} together resolve Problem [\[prob\]](#prob){reference-type="ref" reference="prob"} for all normal Cayley graphs $\mathrm{Cay}(S_n, S)$ with sufficiently large $n$ except when $S \cap \mathrm{Supp}_n(\{2, 3, \dots, n-2\}) \neq \emptyset$, $S \cap \mathrm{Supp}_n(\{n-1, n\}) \neq \emptyset$, and $\mathrm{Supp}_n(n) \not\subseteq S$.

The rest of the paper is organized as follows. The next section is a quick review of representation theory preliminaries. We prove Theorem [\[thm:complement\]](#thm:complement){reference-type="ref" reference="thm:complement"} in Section [\[sec:complements\]](#sec:complements){reference-type="ref" reference="sec:complements"} and establish Theorem [\[thm:main1\]](#thm:main1){reference-type="ref" reference="thm:main1"} and Corollary [\[An-sec-eigen\]](#An-sec-eigen){reference-type="ref" reference="An-sec-eigen"} in Section [\[supp-small\]](#supp-small){reference-type="ref" reference="supp-small"}. To prove Theorem [\[thm:main2\]](#thm:main2){reference-type="ref" reference="thm:main2"}, we first need to determine all normal Cayley graphs on $S_n$ that are line graphs (see Theorem [\[class-linegraph\]](#class-linegraph){reference-type="ref" reference="class-linegraph"}). Using this and the classification [@Stanic2010] of connected regular graphs with second largest eigenvalue at most $1$, we obtain a classification of all normal Cayley graphs on $S_n$ whose strictly second largest eigenvalue is at most $1$ (see Theorem [\[sn-cay-sec-1\]](#sn-cay-sec-1){reference-type="ref" reference="sn-cay-sec-1"}). With the help of this classification, which is of interest for its own sake, we prove Theorem [\[thm:main2\]](#thm:main2){reference-type="ref" reference="thm:main2"} and Corollary [\[cor:main2\]](#cor:main2){reference-type="ref" reference="cor:main2"} in Section [\[supp-large\]](#supp-large){reference-type="ref" reference="supp-large"}.
