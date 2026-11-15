---
doc_id: arxiv-1108.0687v3
doc_title: "Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures"
section_id: sec-010-51-matroids
section_title: "Matroids"
section_number: 5.1
pages: 14-16
source_pdf: 1108.0687v3.pdf
source_sha256: 66ba88e13a429a0a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.961
doc_brief: "Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures — Let {X1, . . ."
---
[]{#ss:matroids label="ss:matroids"}

A collection ${\cal C}$ of subsets of a finite set $E$, all of a given cardinality, $k$, is said to be the set of bases of a matroid if it satisfies the base exchange axiom (see, e.g., [@tutte]): if $A$ and $B$ are distinct members of ${\cal C}$ and $a \in A
\setminus B$, then there exists $b \in B \setminus A$ such that $A \cup \{ b \} \setminus \{ a \} \in {\cal C}$. Given a matroid, it is natural to consider the uniform measure on ${\cal C}$. More generally, the **weighted random base** is chosen from the probability measure $$\nu_w (B) := C \prod_{e \in B} w(e) \, ,$$ where $\{ w(e) : e \in E \}$ is a collection of nonnegative real numbers (weights) and $C$ is a normalizing constant. Identifying $E$ with the set $\{ 1 , \ldots , |E| \}$, the measure $\nu_w$ and the random variables $X_e := 1_{e \in B}$ can be thought of as living on ${\mathcal B}_{|E|}$.

For general matroids, ${\mathbb E}X_e X_f$ may be greater than $({\mathbb E}X_e) ({\mathbb E}X_f)$. Some speculation has been given to the most natural class of matroids for which negative correlation or negative association must hold. Feder and Mihail [@feder-mihail] define a balanced matroid to be a matroid all of whose minors satisfy pairwise negative correlation. Their proof of the following fact was the basis for the original proof of negative association for determinantal processes [@lyons03 Theorem 6.5].

::: pr
[]{#pr:matroids label="pr:matroids"} The law $\nu_w$ of a random base of a balanced matroid, multiplicatively weighted by the weighting function $w$, has the SCP. $\hfill \Box$
:::

Because measures supported on the bases of a matroid are homogeneous, there is nothing gained by improving the SCP to the strong Rayleigh property, and we have the following immediate corollary.

::: cor
[]{#cor:balanced label="cor:balanced"} Let $f$ be a Lipschitz-1 function with respect to Hamming distance on the bases of a balanced matroid of rank $k$ on $n$ elements. Then $${\mathbb P}(f - {\mathbb E}f > a) \leq \exp \left ( - \frac{a^2}{8k} \right ) \, .$$ $\hfill \Box$
:::

::: example
[]{#eg:spanning tree label="eg:spanning tree"} One of the most important examples of a matroid is the set of spanning trees of a finite, connected, undirected graph. To spell this out, a spanning tree for a finite graph $G = (V,E)$ is a subset $E' \subseteq E$ such that $(V,E')$ is a connected and acyclic. The set of spanning trees is a matroid on $E$. The weighted random spanning tree was shown to be a balanced matroid by [@burton-pemantle Theorem 1]. In fact they showed it is determinantal (see also [@lyons03 Example 1.1] and [@HKPV Example 4.3.2]), though at the time consequences of being determinantal, such as the Strong Rayleigh property, had not been developed. Spanning trees are the only well known class of matroid whose uniform (or weighted) measure is determinantal.

Let $f_0: \{ 0 , 1 \}^E \to \mathbb{Z}$ count the number of vertices of odd degree in the graph defined by any subset of the edges. Deleting or adding an edge changes $f_0$ by at most 2. Let $f$ be the random variable resulting from applying $(1/2) f_0$ to a the weighted random spanning tree on a graph $G$. Thus $f$ is a Lipschitz 1 function that counts half the number of vertices that have odd degree in the random tree. Random variables that count local properties such as this are of natural graph theoretic interest. Parity counting variables similar to $f$ play a role, for example in the randomized TSP approximation algorithm of [@saberi]. The number of edges in any spanning tree is $|V| - 1$. An application of Corollary [\[cor:balanced\]](#cor:balanced){reference-type="ref" reference="cor:balanced"} immediately gives the concentration inequality in Theorem [\[th:sp tree\]](#th:sp tree){reference-type="ref" reference="th:sp tree"}; note that $|V|$, rather than $|E|$, appears in the denominator of the exponent.
:::

::: example
[]{#eg:cond bern label="eg:cond bern"} Let $\lambda_1 , \ldots , \lambda_n > 0$ be real numbers and let $\mu$ be the measure on the subsets of $[n]$ of cardinality $k$ given by $$\mu (x_1 , \ldots , x_n) = \frac{\prod_{j=1}^n \lambda_j^{x_j}}
   {\sum_{N ({\bf y}) = k} \prod_{j=1}^n \lambda_j^{y_j}} \, .$$ We may think of $\mu$ in two ways. The first is as a special case of the weighted random base, specialized to $M(n,k)$, the matroid whose bases are all the subsets of $[n]$ that have cardinality $k$. The second is that it is the law of independent Bernoulli variables $X_j$ with ${\mathbb E}X_j =
\lambda_j / (1 + \lambda_j)$, conditioned on $\sum_{j=1}^n X_j = k$. We see from Proposition [\[pr:matroids\]](#pr:matroids){reference-type="ref" reference="pr:matroids"} that $\mu$ is strong Rayleigh. Alternatively, we may deduce this from the strong Rayleigh property for product measures along with closure under conditioning on the sum [@borcea-branden-liggett Corollary 4.18]. Restricting to $[m]$, for $m < n$, gives a joint distribution on ${\mathcal B}_m$ which may be thought of as a multivariate generalization of the hypergeometric distribution. Because the strong Rayleigh property is inherited, this restriction is strong Rayleigh as well. The resulting concentration properties of these measures have been exploited in [@saberi] in connection with TSP approximation. We remark that more general conditioning, such as conditioning $N := \sum_j X_j$ to lie in an interval of more than two points, does not preserve the strong Rayleigh property.
:::
