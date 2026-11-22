---
doc_id: arxiv-math-0411647v2
doc_title: "Asymptotics of characters of symmetric groups, genus expansion and free probability"
section_id: sec-008-22-partitions
section_title: "Partitions"
section_number: 2.2
pages: 13-17
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.838
latex_coverage_ratio: 0.673
doc_brief: "Asymptotics of characters of symmetric groups, genus expansion and free probability — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear"
---
[]{#sec:combinatorial label="sec:combinatorial"}

### Partitions {#subsec:partitions}

We recall that $\pi=\{\pi_1,\dots,\pi_r\}$ is a partition of a finite ordered set $X$ if sets $\pi_1,\dots,\pi_r$ are nonempty and disjoint and if $\pi_1\cup\cdots\cup\pi_r=X$. We denote the set of all partitions of a set $X$ by $\mathop{\mathrm{P}}(X)$. We call sets $\pi_1,\dots,\pi_r$ blocks of the partition $\pi$. We say that elements $a,b\in X$ are connected by the partition $\pi$ if they are the elements of the same block.

We will call elements of the set $X$ the labels of the vertices of the partition $\pi$. As usually, the numbers $|\pi_1|,\dots,|\pi_r|$ denote the numbers of elements in consecutive blocks of $\pi$.

We say that a block $\pi_s$ is trivial if it contains only one element and a trivial partitions has all blocks trivial. We say that a partition is a pair partition if all its blocks contain exactly two elements.

We say that a partition $\pi$ is finer than a partition $\rho$ of the same set if every block of $\pi$ is a subset of some block of $\rho$ and we denote it by $\pi\leq\rho$. The restriction of a partition $\pi$ to a set $Y\subseteq X$ is a partition of $Y$ which connects elements $a,b\in Y$ if and only if $a,b$ are connected by $\pi$.

In the following we present some constructions on partitions of the set $X=\{1,2,\dots,n\}$. However, it should be understood that by a change of labels these constructions can be performed for any finite ordered set $X$.

It is very useful to represent partitions graphically by arranging the elements of the set $X$ counterclockwise on a circle and joining elements of the same block by a line, as it can be seen on Figure [1](#fig:przecinajacapartycja){reference-type="ref" reference="fig:przecinajacapartycja"}. Note that we do not need to write labels on the vertices in order to recover the partition from its graphical representation if we mark the first element as the 'starting point'.

<figure id="fig:przecinajacapartycja">
<embed src="figure03.eps" />
<figcaption>Graphical representation of a partition <span class="math inline">{{1, 3}, {2, 5, 7}, {4}, {6}}</span>.</figcaption>
</figure>

### Fat partitions

[]{#subsec:fat label="subsec:fat"} Let $\pi=\{\pi_1,\dots,\pi_r\}$ be a partition of the set $\{1,\dots,n\}$. For every $1\leq s\leq r$ let $\pi_s=\{\pi_{s,1},\dots,\pi_{s,l_s}\}$ with $\pi_{s,1}<\cdots<\pi_{s,l_s}$. We define $\pi_{\mathop{\mathrm{fat}}}$, called fat partition of $\pi$, to be a pair partition of the $2n$--element ordered set $\{1,1',2,2',\dots,n,n'\}$ given by $$\pi_{\mathop{\mathrm{fat}}}=
\big\{  \{ \pi_{s,t}',\pi_{s,t+1}  \} :  1\leq s \leq r \text{ and }
1 \leq t \leq l_s  \big\},$$ where it should be understood that $\pi_{s,l_s+1}=\pi_{s,1}$.

<figure id="fig:tlustapartycja">
<embed src="figure04.eps" />
<figcaption>Fat partition <span class="math inline"><em>π</em><sub>fat</sub></span> corresponding to the partition <span class="math inline"><em>π</em></span> from Figure <a href="#fig:przecinajacapartycja" data-reference-type="ref" data-reference="fig:przecinajacapartycja">1</a>.</figcaption>
</figure>

This operation can be easily described graphically as follows: we draw blocks of a partition with a fat pen and take the boundary of each block, as it can be seen on Figure [2](#fig:tlustapartycja){reference-type="ref" reference="fig:tlustapartycja"}. This boundary is a collection of lines hence it is a pair partition. However, every vertex $k\in\{1,\dots,n\}$ of the original partition $\pi$ has to be replaced by its 'right' and 'left' copy (denoted respectively by $k$ and $k'$). Please note that in the graphical representation of $\pi_{\mathop{\mathrm{fat}}}$ we mark the space between $1$ and $1'$ as the 'starting point'.

### Non--crossing partitions

We say that a partition $\pi$ is non--crossing [@Kreweras; @SimionUllman; @Speicher1994; @Speicher1997; @Speicher1998] if for every $i\neq j$ and $a,c\in\pi_i$ and $b,d\in\pi_j$ it cannot happen that $a<b<c<d$. For example, the partition from Figure [1](#fig:przecinajacapartycja){reference-type="ref" reference="fig:przecinajacapartycja"} is crossing (as it can be easily seen from its graphical representation) while a partition from Figure [3](#fig:nieprzecinajacapartycja){reference-type="ref" reference="fig:nieprzecinajacapartycja"} is non--crossing. The set of all non--crossing partitions of a set $X$ will be denoted by $\mathop{\mathrm{NC}}(X)$ and the set of all non--crossing pair partitions of a set $X$ will be denoted by $\mathop{\mathrm{NC_2}}(X)$.

<figure id="fig:nieprzecinajacapartycja">
<embed src="figure05.eps" />
<figcaption> Graphical representation of a non–crossing partition <span class="math inline">{{1}, {2, 5, 6}, {3, 4}}</span>.</figcaption>
</figure>

### Kreweras complementation map

The function $\pi\mapsto\pi_{\mathop{\mathrm{fat}}}$ which maps partitions of a $n$--element set to pair partitions of a $2n$--element set is one to one but in general is not a bijection. However, it is a bijection between $\mathop{\mathrm{NC}}(1,2,\dots,n)$ and $\mathop{\mathrm{NC_2}}(1,1',\dots,n,n')$ [@Kreweras].

<figure id="fig:tlustapartycjanieprzecinajaca">
<embed src="figure06.eps" />
<figcaption>Fat partition <span class="math inline"><em>π</em><sub>fat</sub></span> for a non–crossing partition <span class="math inline"><em>π</em></span> from Figure <a href="#fig:nieprzecinajacapartycja" data-reference-type="ref" data-reference="fig:nieprzecinajacapartycja">3</a>.</figcaption>
</figure>

If $\rho$ is a pair partition of the set $\{1,1',2,2',\dots,n,n'\}$, we denote by $r(\rho)$ a pair partition of the same set $\{1,1',\dots,n,n'\}$ which is obtained by cyclic change of labels $\cdots\rightarrow 2'\rightarrow 2\rightarrow 1'\rightarrow
1\rightarrow n'\rightarrow n \rightarrow\cdots$ carried by the vertices. In the graphical representation of a partition this corresponds to a shift of the starting point by one counterclockwise (cf Figure [5](#fig:rotacja){reference-type="ref" reference="fig:rotacja"}). Of course $r$ is a bijection of the set $\mathop{\mathrm{NC_2}}(1,1',\dots,n,n')$.

<figure id="fig:rotacja">
<embed src="figure07.eps" />
<figcaption>Graphical representation of <span class="math inline"><em>r</em>(<em>ρ</em>)</span> where <span class="math inline"><em>ρ</em></span> is given by Figure <a href="#fig:tlustapartycjanieprzecinajaca" data-reference-type="ref" data-reference="fig:tlustapartycjanieprzecinajaca">4</a>.</figcaption>
</figure>

It follows that the map $\pi\mapsto\pi_{\mathop{\mathrm{comp}}}$, called Kreweras complementation map, given by $(\pi_{\mathop{\mathrm{comp}}})_{\mathop{\mathrm{fat}}}=r(\pi_{\mathop{\mathrm{fat}}})$ is well--defined and is a permutation of $\mathop{\mathrm{NC}}(1,2,\dots,n)$. Due to the canonical bijection between $\{1,2,\dots,n\}$ and $\{1',2',\dots,n'\}$ we can identify $\mathop{\mathrm{NC}}(1,2,\dots,n)$ with $\mathop{\mathrm{NC}}(1',2',\dots,n')$ and in the future we shall sometimes regard $\pi_{\mathop{\mathrm{comp}}}$ as an element of $\mathop{\mathrm{NC}}(1,2,\dots,n)$ and sometimes as an element of $\mathop{\mathrm{NC}}(1',2',\dots,n')$. It will be clear from the context which of the options we choose.

One can also state the above definition as follows: $\pi_{\mathop{\mathrm{comp}}}$ is the biggest non--crossing partition of the set $\{1',2',\dots,n'\}$ with a property that $\pi\cup\pi_{\mathop{\mathrm{comp}}}$ is a non--crossing partition of the set $\{1,1',2,2',\dots,n,n'\}$ (cf Figure [6](#fig:Kreweras){reference-type="ref" reference="fig:Kreweras"}).

<figure id="fig:Kreweras">
<embed src="figure08.eps" />
<figcaption>Partition <span class="math inline"><em>π</em></span> from Figure <a href="#fig:nieprzecinajacapartycja" data-reference-type="ref" data-reference="fig:nieprzecinajacapartycja">3</a> in a solid line and its Kreweras complement in a dashed line.</figcaption>
</figure>

We shall also consider the inverse of the Kreweras complementation map: for $\pi, \rho\in\mathop{\mathrm{NC}}(1,2,\dots,n)$ we have $\pi_{{\mathop{\mathrm{comp}}^{-1}}}=\rho$ if and only if $\pi=\rho_{\mathop{\mathrm{comp}}}$. One can observe that $\rho_{{\mathop{\mathrm{comp}}^{-1}}}$ and $\rho_{\mathop{\mathrm{comp}}}$ are always cyclic rotations of each other.
