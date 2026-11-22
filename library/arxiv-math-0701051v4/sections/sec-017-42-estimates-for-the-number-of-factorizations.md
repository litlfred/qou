---
doc_id: arxiv-math-0701051v4
doc_title: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e)"
section_id: sec-017-42-estimates-for-the-number-of-factorizations
section_title: "Estimates for the number of factorizations"
section_number: 4.2
pages: 13-15
source_pdf: 0701051v4.pdf
source_sha256: 4592a048c3b84a8d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.814
latex_coverage_ratio: 0.979
doc_brief: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e) — We prove an upper bound for characters of the symmetric groups."
---
Now, we have to find a bound of the number of factorizations of $\pi$ with a given value of the statistic $o(\sigma_1,\sigma_2)$.

::: lemma
[]{#lem:feray label="lem:feray"} Let $\pi,\sigma_1,\sigma_2\in S_l$ be such that $\pi=\sigma_1 \sigma_2$.

There exist permutations $\sigma_1',\sigma_2'\in S_l$ such that $\pi=\sigma_1' \sigma_2'$, $|\sigma_1'|+|\sigma_2'|=|\sigma_1|+|\sigma_2|$, $|\sigma_2'|= |\sigma_2'\sigma_2^{-1} |+|\sigma_2|$ and every cycle of $\sigma'_1$ is contained in some cycle of $\sigma_2'$. Furthermore, $|\sigma_1'| = o(\sigma_1,\sigma_2)$.
:::

::: proof
*Proof.* If every cycle of $\sigma_1$ is contained in some cycle of $\sigma_2$ then $\sigma_1'=\sigma_1$ and $\sigma_2'=\sigma_2$ have the required property.

Otherwise, there exist $a,b\in\{1,\dots,n\}$ such that $a$ and $b$ belong to the same cycle of $\sigma_1$ but not to the same cycle of $\sigma_2$. We define $\sigma_1'=\sigma_1 (a,b)$, $\sigma_2'=(a,b) \sigma_2$. Notice that $|\sigma_1'|=|\sigma_1|-1$, $|\sigma_2'|=|\sigma_2|+1$, and the orbits under the action of the subgroups $\langle \sigma_1,\sigma_2 \rangle$ and $\langle \sigma_1',\sigma_2' \rangle$ are the same.

We iterate this procedure if necessary (it will finish after a finite number of steps because the length of $\sigma_1$ decreases in each step). It remains to prove that

$|\sigma_2'| \geq |\sigma_2'\sigma_2^{-1} |+|\sigma_2|$ (the opposite inequality follows from the triangle inequality): notice that $|\sigma_2'|-|\sigma_2|$ is equal to $k$ (where $k$ is the number of steps after which the procedure has terminated) and $\sigma_2'\sigma_2^{-1}$ is a product of $k$ transpositions, hence $|\sigma_2'\sigma_2^{-1}|\leq k$.

Furthermore, as every cycle of $\sigma_1'$ is contained in some cycle of $\sigma_2'$, the set of orbits of the group $\langle
\sigma_1',\sigma_2'\rangle$ is equal to $C(\sigma_2')$, so

$$o(\sigma_1,\sigma_2)= o(\sigma_1',\sigma_2')= l-
|C(\sigma_1')|= |\sigma_1'|. \qedhere$$ ◻
:::

::: lemma
[]{#lem:nie-za-duzo label="lem:nie-za-duzo"} For any integers $l\geq 1$ and $i\geq 0$ and for any $\pi\in S_l$ $$\label{eq:iloscpermutacji}
 \# \{ \sigma\in S_l : | \sigma | = i \} \leq \frac{l^{2i}}{i!}.$$
:::

::: proof
*Proof.* Since every permutation in $S_l$ appears exactly once in the product $$[1+ (12) ] [1+ (13)+(23) ] \cdots [1+(1l)+\cdots+(l-1,l)],$$ we have $$\sum_i x^i\ \#\big\{ \sigma\in S_l : | \sigma | = i \big\} = (1+x) (1+2x)
\cdots \big(1+(l- 1) x\big).$$ Each of the coefficients of $x^k$ on the right-hand side is bounded from above by the corresponding coefficient of $e^{x} e^{2x} \cdots
e^{(l-1)x}=e^{\frac{l(l-1)x}{2}}$, finishing the proof. ◻
:::

::: lemma
[]{#lem:numer-of-cutted-graphs label="lem:numer-of-cutted-graphs"} There exists a constant $C_0$ with a property that for any $k$ the number of minimal factorisations $\sigma_1\sigma_2=\pi$, $|\sigma_1|+|\sigma_2|=|\pi|$ of a cycle $\pi=(1, \ldots ,k)$ and such that the associated graph $\tilde{G}$ consists of $s\geq 2$ components is bounded from above by $$\frac{(C_0 k)^{2s-2}}{(2s-2)!}.$$
:::

::: proof
*Proof.* Since the factorization is minimal therefore the graph $G$ associated to $\sigma_1,\sigma_2$ is a tree. We will give to $G$ a structure of planted planar tree: the root is the cycle of $\sigma_1$ containing $1$ and his left-most edge links it to the cycle of $\sigma_2$ containing $1$.

In each connected component of $\tilde{G}$ there is at most one vertex of degree higher than one and we shall decorate this vertex. If in some connected component of $\tilde{G}$ there are no such vertices we decorate any of them which is not a leaf in $G$. In this way the decorated vertices can be identified with connected components of $\tilde{G}$.

We consider the graph $G'$ obtained from $G$ by removing the leaves (except the root) and the graph $G''$ which consists of the decorated vertices of $\tilde{G}$; we connect two vertices $A,B\in G''$ by an edge if vertices $A,B$ are connected in $G$ (or, equivalently, $G'$) by a *direct path*, i.e. a path which does not pass through any connected component of $\tilde{G}$ other than the ones specified by $A$ and $B$.

It is easy to see that $G''$ inherits the structure of a plane rooted tree from $G$ (we define the root of $G''$ to be the connected component of $\tilde{G}$ of the root of $G$) and it has $s$ vertices. It follows that the number of such trees $G''$ is bounded from above by the Catalan number $\frac{1}{s+1}
\binom{2s}{s}<4^s$.

In order to reconstruct the tree $G'$ from $G''$ we have to specify for each edge of $G''$ if it comes from a single edge of $G'$ or from a pair or a triple of consecutive edges of $G'$; it follows that we have (at most) $3^{s-1}$ choices. It might happen also for two adjacent (with respect to the planar structure) edges $e_1,e_2$ of $G''$ that each of these edges $e_i$ corresponds to a pair or a triple of consecutive edges $f_i=(f_{i1},f_{i2}[,f_{i3}])$ of $G'$ and these tuples $f_1$ and $f_2$ have one edge in common. There are at most $2s-3$ such pairs of adjacent edges which accounts for at most $2^{2s-3}$ choices. If the root of $G$ is not a decorated vertex, it might happen that it is a leaf or that it belongs to the left-most and/or to the right-most edge of the root of $G'$: there are $4$ choices for that.

In order to reconstruct tree $G$ from $G'$ we have to specify if the root of $G$ is a decorated vertex or not. Furthermore we have to specify places in which we will add missing $l$ leaves to the tree $G'$ (note that $l\leq
k+1-s$); it is easy to see that this is equivalent to specifying a partition $l=a_1+\cdots+a_{2s-1}$, where $a_1,\dots,a_{2s-1}\geq 0$ are integers. It follows that the number of choices is bounded from above by $$2 \binom{l+2s-2}{2s-2}\leq 2 \binom{k+s-1}{2s-2}\leq 2

\frac{\left(k+\frac{1}{2}\right)^{2s-2}}{(2s-2)!}.$$

A minimal factorisation is determined by its bicolored map with a marked edge, for example the one linking the two cycles containing $1$ [@GouldenJackson1992]. With our construction, the coloring is determined by the root which always belongs to $C(\sigma_1)$ and the marked edge is its left-most edge.

It follows that the total number of choices is bounded from above by

$$2 \cdot 3^{s-1}\cdot 2^{2s-1} \cdot 4^s
\frac{\left(k+\frac{1}{2}\right)^{2s-2}}{(2s-2)!}.\qedhere$$ ◻
:::
