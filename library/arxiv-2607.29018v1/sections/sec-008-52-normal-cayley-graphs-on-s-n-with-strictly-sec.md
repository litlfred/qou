---
doc_id: arxiv-2607.29018v1
doc_title: "The Aldous property for normal Cayley graphs on symmetric groups"
section_id: sec-008-52-normal-cayley-graphs-on-s-n-with-strictly-sec
section_title: "Normal Cayley graphs on $S_n$ with strictly second largest eigenvalue at most $1$"
section_number: 5.2
pages: 17-19
source_pdf: 2607.29018v1.pdf
source_sha256: 789faa122dd32290
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.652
latex_coverage_ratio: 1.0
doc_brief: "The Aldous property for normal Cayley graphs on symmetric groups — Aldous’ spectral gap conjecture states that the random walk and the interchange process on any connected graph have the same"
---
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
