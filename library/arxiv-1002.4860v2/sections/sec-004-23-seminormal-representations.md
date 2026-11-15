---
doc_id: arxiv-1002.4860v2
doc_title: "A STATE-SUM FORMULA FOR THE ALEXANDER POLYNOMIAL"
section_id: sec-004-23-seminormal-representations
section_title: "Seminormal representations"
section_number: 2.3
pages: 3-3
source_pdf: 1002.4860v2.pdf
source_sha256: a2cfe924f7a9f5a0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.952
doc_brief: "A STATE-SUM FORMULA FOR THE ALEXANDER POLYNOMIAL — We develop a diagrammatic formalism for calculating the Alexander polynomial of the closure of a braid as a state-sum."
---
This exposition follows [@Ram section 3], although the results were originally worked out in [@Hoefsmit]. For a new point of view and substantial generalization, see [@BK section 5].

Let $\operatorname {Par}(n)$ denote the set of all integer partitions of $n$. To the partition $\lambda= (\lambda_1 \ge \lambda_2 \ge \cdots)$, associate its *Young diagram*, that is, the left-justified diagram with $\lambda_1$ boxes on the first row, $\lambda_2$ boxes on the second row, etc.

Let $\operatorname {Tab}(\lambda)$ denote the set of $\lambda$-tableaux. These are fillings of the boxes in the Young diagram $\lambda$ by the numbers $1, \dots, n$. Let $\operatorname {Std}(\lambda)$ denote the set of *standard* $\lambda$-tableaux, namely those that increase across rows and down columns. The symmetric group $S_n$ acts on $\operatorname {Tab}(\lambda)$ via its natural action on the entries, although $\operatorname {Std}(\lambda)$ is not stable under this action. For a tableau $\mathtt{T} \in \operatorname {Tab}(\lambda)$, its *residue sequence* $(i_1,\dots,i_n) \in \mathbb{Z}^n$ is defined by setting $i_r = b-a$ where the box labeled $r$ in $\mathtt{T}$ appears in row $a$ and column $b$.

<figure>
<p><span class="math display">$$\lambda= \vcenter {\xy 0;/r.10pc/:
(0,0);(30,0)**@{-},
(0,-10);(30,-10)**@{-},
(0,-20);(10,-20)**@{-},
(0,0);(0,-20)**@{-},
(10,0);(10,-20)**@{-},
(20,0);(20,-10)**@{-},
(30,0);(30,-10)**@{-}
\endxy}
\qquad
\mathtt{T} = \vcenter {\xy 0;/r.10pc/:
(0,0);(30,0)**@{-},
(0,-10);(30,-10)**@{-},
(0,-20);(10,-20)**@{-},
(0,0);(0,-20)**@{-},
(10,0);(10,-20)**@{-},
(20,0);(20,-10)**@{-},
(30,0);(30,-10)**@{-},
(5,-5)*{1},
(15,-5)*{2},
(5,-15)*{3},
(25,-5)*{4}
\endxy}
\qquad
s_2 \mathtt{T} = \vcenter {\xy 0;/r.10pc/:
(0,0);(30,0)**@{-},
(0,-10);(30,-10)**@{-},
(0,-20);(10,-20)**@{-},
(0,0);(0,-20)**@{-},
(10,0);(10,-20)**@{-},
(20,0);(20,-10)**@{-},
(30,0);(30,-10)**@{-},
(5,-5)*{1},
(15,-5)*{3},
(5,-15)*{2},
(25,-5)*{4}
\endxy}$$</span></p>
<figcaption>The partition <span class="math inline"><em>λ</em> = (3,1) ∈ Par (4)</span> and standard tableaux <span class="math inline"><code>T</code></span> and <span class="math inline"><em>s</em><sub>2</sub><code>T</code></span>. Here, <span class="math inline"><code>T</code></span> has residue sequence <span class="math inline">(0,1,−1,2)</span>.</figcaption>
</figure>

Fix a partition $\lambda\in \operatorname {Par}(n)$ and let $S(\lambda)$ be the $\mathbb{C}(v)$-vector space on basis {$x_{\mathtt{T}} \;|\; \mathtt{T} \in \operatorname {Std}(\lambda)\}$. Let $(i_1, \ldots, i_n)$ be the residue sequence of $\mathtt{T}$ and define $a_r(\mathtt{T}), b_r(\mathtt{T}) \in \mathbb{C}(v)$ to be $$\label{abs}
a_r(\mathtt{T}) = \frac {v - v^{-1}} {1 - v^{2(i_r-i_{r+1})}},\qquad
b_r(\mathtt{T}) = v^{-1}+a_r(\mathtt{T}).$$ Define actions of the generators $H_1, \ldots, H_{n-1}$ of $\mathcal{H}_n$ on $S(\lambda)$ by $$\label {s-n formula}
H_r x_{\mathtt{T}} = a_r (\mathtt{T})x_{\mathtt{T}} + b_r (\mathtt{T}) x_{s_r\mathtt{T}},$$ where we interpret $x_{s_r \mathtt{T}} = 0$ if $s_r \mathtt{T}$ is not a standard tableau.

::: thm
[]{#irrep thm label="irrep thm"} This action extends to make $S(\lambda)$ into a well-defined $\mathcal{H}_n$-module. Furthermore, the modules $\{S(\lambda) \; | \; \lambda\in \operatorname {Par}(n) \}$ constitute a complete set of pairwise non-isomorphic irreducible modules for $\mathcal{H}_n$.
:::
