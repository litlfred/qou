---
doc_id: arxiv-math-0501112v3
doc_title: "arXiv:math/0501112v3 [math.CO] 31 May 2005"
section_id: sec-023-44-three-probability-spaces
section_title: "Three probability spaces"
section_number: 4.4
pages: 20-21
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.947
doc_brief: "arXiv:math/0501112v3 [math.CO] 31 May 2005 — We study asymptotics of reducible representations of the symmetric groups Sq for large q."
---
Commutative algebras ${\mathfrak{A}}$ and ${\mathfrak{A}}^{\bullet}$ can be regarded as algebras of random variables on a purely formal level (usually it is not possible to represent them as algebras of functions on some Kolmogorov probability space).

Algebras ${\mathfrak{A}}$ and ${\mathfrak{A}}^{\bullet}$ are trivially isomorphic as vector spaces; we will denote by ${\mathbb{E}}^{\text{id}}:{\mathfrak{A}}\rightarrow{\mathfrak{A}}^{\bullet}$ the identity map between them, in other words $${\mathbb{E}}^{\text{id}}(x)=x.$$ One can think that ${\mathbb{E}}^{\text{id}}$ is a kind of a conditional expectation.

If $\rho$ is a representation of $S_q$ we consider maps ${\mathbb{E}}:{\mathfrak{A}}\rightarrow{\mathbb{C}}$ and ${\mathbb{E}}^{\bullet}:{\mathfrak{A}}^{\bullet}\rightarrow{\mathbb{C}}$ given by $${\mathbb{E}}(x)={\mathbb{E}}^{\bullet}(x)=\chi_{\rho}(x).$$

In this way the following diagram commutes: $$\label{eq:diagram} \xymatrix{ {{\mathfrak{A}}} \ar[r]_-{{\mathbb{E}}^{\text{id}} }
\ar@/^1pc/[rr]^-{{\mathbb{E}}} & {{\mathfrak{A}}^{\bullet}} \ar[r]_-{{\mathbb{E}}^{\bullet}} & {{\mathbb{C}}}
}.$$ and we may consider three different probability structures:

-   algebra ${\mathfrak{A}}$ equipped with the expectation ${\mathbb{E}}$ (which gives rise to the natural cumulants $k$),

-   algebra ${\mathfrak{A}}^{\bullet}$ equipped with the expectation ${\mathbb{E}}^{\bullet}$ (which gives rise to the disjoint cumulants $k^{\bullet}$),

-   algebra ${\mathfrak{A}}$ equipped with the conditional expectation ${\mathbb{E}}^{\text{id}}:{\mathfrak{A}}\rightarrow{\mathfrak{A}}^{\bullet}$ (corresponding conditional cumulants belong to ${\mathfrak{A}}^{\bullet}$ and will be denoted by $k^{\text{id}}$).

The commutativity of the diagram [\[eq:diagram\]](#eq:diagram){reference-type="eqref" reference="eq:diagram"} implies that the relation between the corresponding three cumulants is given by the following formula of Brillinger [@Brillinger69] (see also [@Lehner04]).

::: proposition
[]{#prop:Brillinger label="prop:Brillinger"} If $x_1,\dots,x_n$ belong to the center of ${\mathfrak{A}}$ then $$k(x_1,\dots,x_n)=\sum_{\pi}
k^{\bullet}\big[ k^{\text{\rm{id}}}(x_i: i\in \pi_j   ): j=1,2,\dots
\big] , \label{eq:Brillinger}$$ where the sum runs over all partitions $\pi=\{\pi_1,\pi_2,\dots\}$ of the set $\{1,\dots,n\}$.
:::

::: example
Let us consider $n=2$: there are two partitions of $\{1,2\}$, namely $\big\{ \{1\}, \{2\} \big\}$ and $\big\{ \{1,2\} \big\}$ therefore $$k(x_1,x_2)= k^{\bullet}\big( k^{\text{\rm{id}}}(x_1), k^{\text{\rm{id}}}(x_2) \big)+
k^{\bullet}\big( k^{\text{\rm{id}}}(x_1,x_2) \big).$$ Similarly, for $n=3$ $$\begin{gathered}
 k(x_1,x_2,x_3)=
k^{\bullet}\big( k^{\text{\rm{id}}}(x_1),
k^{\text{\rm{id}}}(x_2),k^{\text{\rm{id}}}(x_2) \big)+
k^{\bullet}\big( k^{\text{\rm{id}}}(x_1,x_2),k^{\text{\rm{id}}}(x_3)
\big)+\\ k^{\bullet}\big(
k^{\text{\rm{id}}}(x_1,x_3),k^{\text{\rm{id}}}(x_2) \big)+
k^{\bullet}\big( k^{\text{\rm{id}}}(x_2,x_3),k^{\text{\rm{id}}}(x_1)
\big)+ \\ k^{\bullet}\big( k^{\text{\rm{id}}}(x_1)
,k^{\text{\rm{id}}}(x_2),k^{\text{\rm{id}}}(x_3) \big).
\end{gathered}$$
:::

The following result will be of great importance in this article.

::: theorem
[]{#theo:kumulantykombinatoryczne label="theo:kumulantykombinatoryczne"} For any $x_1,\dots,x_n\in{\mathfrak{A}}$ $$\label{eq:kumulantykombinatoryczne} \deg k^{\text{\rm
id}}(x_1,\dots,x_n) \leq \deg x_1+\cdots+ \deg x_n-2(n-1).$$ Furthermore, the highest-order term of the second cumulant is given by $$\begin{gathered}
\label{eq:a-tak-dokladnie?} k^{\text{\rm
id}}(\Sigma_{l_1},\Sigma_{l_2})=
\sum_{r\geq 1}\sum_{\substack{a_1,\dots,a_r\geq 1\\
a_1+\dots+a_r=l_1}}  \sum_{\substack{b_1,\dots,b_r\geq 1\\
b_1+\dots+b_r=l_2}} \frac{l_1 l_2}{r}
\Sigma_{(a_1+b_1-1),\dots,(a_r+b_r-1)}
+ \\
\text{terms of degree at most $(l_1+l_2-2)$}.
\end{gathered}$$
:::

We postpone its proof to Section [\[sec:Proof-Theorem-?????\]](#sec:Proof-Theorem-?????){reference-type="ref" reference="sec:Proof-Theorem-?????"}.
