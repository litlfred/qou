---
doc_id: arxiv-math-0411647v2
doc_title: "Asymptotics of characters of symmetric groups, genus expansion and free probability"
section_id: sec-007-22-partitions
section_title: "Partitions"
section_number: 2.2
pages: 13-22
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
doc_brief: "Asymptotics of characters of symmetric groups, genus expansion and free probability — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear"
text_source: latex
latex_prose_ratio: 0.897
latex_coverage_ratio: 0.981
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

# The first main result: Calculus of partitions {#sec:calculus}

## Partition--indexed conjugacy class indicator $\Sigma_\pi$

### Definition of $\Sigma_\pi$ {#subsec:pierwszawzmiankaofppsq}

Let $\pi$ be a partition of the set $\{1,\dots,n\}$. Since the fat partition $\pi_{\mathop{\mathrm{fat}}}$ connects every element of the set $\{1',2',\dots,n'\}$ with exactly one element of the set $\{1,2,\dots,n\}$, we can view $\pi_{\mathop{\mathrm{fat}}}$ as a bijection $\pi_{\mathop{\mathrm{fat}}}:\{1',2',\dots,n'\}\rightarrow\{1,2,\dots,n\}$. We also consider a bijection $c:\{1,2,\dots,n\}\rightarrow\{1',2',\dots,n'\}$ given by $\dots,3\mapsto 2', 2\mapsto 1', 1\mapsto n', n\mapsto
(n-1)',\dots$. Finally, we consider a permutation $\pi_{\mathop{\mathrm{fat}}}\circ
c$ of the set $\{1,2,\dots,n\}$.

For example, for the partition $\pi$ given by Figure [1](#fig:przecinajacapartycja){reference-type="ref" reference="fig:przecinajacapartycja"} the composition $\pi_{\mathop{\mathrm{fat}}}\circ c$ has a cycle decomposition $(1,{2},3,5,{4})({6},7)$, as it can be seen from Figure [7](#fig:tlustapartycja2){reference-type="ref" reference="fig:tlustapartycja2"}.

<figure id="fig:tlustapartycja2">
<embed src="figure09.eps" />
<figcaption>Bijection corresponding to the partition <span class="math inline"><em>π</em><sub>fat</sub></span> from Figure <a href="#fig:tlustapartycja" data-reference-type="ref" data-reference="fig:tlustapartycja">2</a> plotted with a solid line and the bijection <span class="math inline"><em>c</em></span> plotted with a dashed line. Lines corresponding to two different cycles were plotted in different colors (gray and black). The meaning of the additional decoration of some of the vertices will be explained in Section <a href="#subsec:explicit" data-reference-type="ref" data-reference="subsec:explicit">[subsec:explicit]</a>.</figcaption>
</figure>

Alternatively, one can identify the set $\{1',2',\dots,n'\}$ with the set $\{1,2,\dots,n\}$; then $\pi_{\mathop{\mathrm{fat}}}$ becomes a permutation which coincides with the construction from [@Kreweras; @Biane1997crossings; @Biane1998] and $c$ is equal to the full cycle $(n,n-1,\dots,2,1)$.

We decompose the permutation $$\pi_{\mathop{\mathrm{fat}}}\circ c=(b_{1,1},b_{1,2},\dots,b_{1,j_1})
\cdots (b_{t,1},\dots,b_{t,j_t})$$ as a product of disjoint cycles. Every cycle $b_s=(b_{s,1},\dots,b_{s,j_s})$ can be viewed as a closed clockwise path on a circle and therefore one can compute how many times it winds around the circle. It might be useful to draw a line between the central disc and the starting point (cf Figure [8](#fig:tlustapartycja3){reference-type="ref" reference="fig:tlustapartycja3"}); the number of winds is equal to the number of times a given cycle crosses this line and therefore is equal to the number of indices $1\leq i\leq j_s$ such that $b_{s,i}\leq b_{s,i+1}$, where we use the convention that $b_{s,j_s+1}=b_{s,1}$.

To a cycle $b_s$ we assign the number $$\begin{gathered}
\label{eq:formulanak} k_s=(\text{number of elements in a cycle }
b_s)-\\ (\text{number of clockwise winds of }b_s).
\end{gathered}$$

In the above example we have $b_1=(1,{2},3,5,{4})$, $b_2=({6},7)$ and $k_1=2$, $k_2=1$, as it can be seen from Figure [8](#fig:tlustapartycja3){reference-type="ref" reference="fig:tlustapartycja3"}, where all lines clockwise wind around the central disc.

<figure id="fig:tlustapartycja3">
<embed src="figure10.eps" />
<figcaption>A version of Figure <a href="#fig:tlustapartycja2" data-reference-type="ref" data-reference="fig:tlustapartycja2">7</a> in which all lines wind clockwise around the central disc.</figcaption>
</figure>

Alternatively, we can treat every cycle $b_s$ of $\pi_{\mathop{\mathrm{fat}}} \circ
c$ as a closed counter--clockwise path on a circle (cf Figure [9](#fig:tlustapartycja4){reference-type="ref" reference="fig:tlustapartycja4"}). Equation [\[eq:formulanak\]](#eq:formulanak){reference-type="eqref" reference="eq:formulanak"} implies that $$\label{eq:formulanakk} k_s=(\text{number of counterclockwise winds
of the cycle } b_s).$$

<figure id="fig:tlustapartycja4">
<embed src="figure11.eps" />
<figcaption>A version of Figure <a href="#fig:tlustapartycja2" data-reference-type="ref" data-reference="fig:tlustapartycja2">7</a> in which all lines of <span class="math inline"><em>π</em><sub>fat</sub></span> wind counterclockwise around the central disc.</figcaption>
</figure>

Let a positive integer $q$ be given. In Section [\[sec:proofs\]](#sec:proofs){reference-type="ref" reference="sec:proofs"} we shall define the most important tool of this article: a certain map $\Phi^{\mathop{\mathrm{P}}}_{{\mathbb{C}}(\widetilde{{{S}}_{\infty}})}$ from the set of partitions to ${\mathbb{C}}(\widetilde{{{S}}_{\infty}})$. The following Claim states that $\Phi^{\mathop{\mathrm{P}}}_{{\mathbb{C}}(\widetilde{{{S}}_{\infty}})}(\pi)$ is closely related with the normalized conjugacy class indicators from Section [\[subsec:definicjasigma\]](#subsec:definicjasigma){reference-type="ref" reference="subsec:definicjasigma"} of Section [\[sec:preliminaries\]](#sec:preliminaries){reference-type="ref" reference="sec:preliminaries"} and hence $\Sigma_{\pi}:=\Phi^{\mathop{\mathrm{P}}}_{{\mathbb{C}}(\widetilde{{{S}}_{\infty}})}(\pi)$ can be viewed as a normalized conjugacy class indicator which is indexed by a partition $\pi$ instead of a tuple of integers $(k_1,\dots,k_t)$.

::: claim
[]{#claim:definicjasigma label="claim:definicjasigma"} Let $\pi$ be a partition of the set $\{1,2,\dots,n\}$ and let numbers $k_1,\dots,k_t$ be given by the above construction. Then $$\Sigma_\pi:=\Phi^{\mathop{\mathrm{P}}}_{{\mathbb{C}}(\widetilde{{{S}}_{\infty}})}(\pi)=\Sigma_{k_1,\dots,k_t},$$ where $\Sigma_{k_1,\dots,k_t}\in{\mathbb{C}}(\widetilde{{{S}}_{\infty}})$ on the right--hand side should be understood as in Section [\[subsec:definicjasigma\]](#subsec:definicjasigma){reference-type="ref" reference="subsec:definicjasigma"}.
:::

This Claim will follow from Theorem [\[theo:stwierdzeniepierwszejestprawda\]](#theo:stwierdzeniepierwszejestprawda){reference-type="ref" reference="theo:stwierdzeniepierwszejestprawda"}. Reader not interested in too technical details may even take this Claim as a very simple alternative definition of $\Sigma_\pi=\Phi^{\mathop{\mathrm{P}}}_{{\mathbb{C}}(\widetilde{{{S}}_{\infty}})}(\pi)$.

### Basic properties of $\Sigma_{\pi}$

We say that partitions $\pi$ and $\pi'$ are cyclic rotations of each other if one can obtain $\pi'$ from $\pi$ by a cyclic shift of labels of vertices. Graphically, this corresponds to a change of a marked starting point on a circle.

::: proposition
[]{#prop:rotacjajestok label="prop:rotacjajestok"} Let $\pi$ and $\pi'$ be two partitions of the same set which are cyclic rotations of each other. Then $$\Sigma_{\pi}=\Sigma_{\pi'}.$$
:::

::: proof
*Proof.* It is enough to observe that the winding numbers considered in the algorithm from Section [1.1.1](#subsec:pierwszawzmiankaofppsq){reference-type="ref" reference="subsec:pierwszawzmiankaofppsq"} do not depend on the choice of the starting point. ◻
:::

::: proposition
If partition $\pi$ connects some neighbor elements then $\Sigma_\pi=0$.
:::

::: proof
*Proof.* If partition $\pi$ connects some $r$ with $r+1$ then $\pi_{\mathop{\mathrm{fat}}}$ connects $r'$ with $r+1$, hence $\pi_{\mathop{\mathrm{fat}}}(r')=r+1$ and $(\pi_{\mathop{\mathrm{fat}}}\circ c)(r+1)=r+1$. One of the cycles of $\pi_{\mathop{\mathrm{fat}}}\circ c$ is a $1$--cycle $b_s=(r+1)$ and one can easily check that $k_s=0$. Claim [\[claim:definicjasigma\]](#claim:definicjasigma){reference-type="ref" reference="claim:definicjasigma"} implies that $\Sigma_\pi=\Sigma_{k_1,\dots,k_t}=0$. ◻
:::

### Degree of $\Sigma_\pi$ and its geometric interpretation

We keep the notation from the previous Section; in particular $t$ denotes the number of cycles of $\pi_{\mathop{\mathrm{fat}}}\circ c$ and $r$ the number of blocks of $\pi$. Observe that $$\sum_{1\leq s\leq t} (\text{number of elements in a cycle } b_s)=n.$$

Furthermore $\sum_{1\leq s\leq t} (\text{number of clockwise winds
of } b_s)$ is equal to the total number of clockwise winds of $\pi_{\mathop{\mathrm{fat}}}\circ c$. When we identify sets $\{1,2,\dots,n\}$ and $\{1',2',\dots,n'\}$ then $c$ is a full clockwise cycle and it contributes with a one wind. It is easy to observe that every block $\pi_s$ of partition $\pi$ is a counterclockwise cycle of the permutation $\pi_{\mathop{\mathrm{fat}}}$, hence when we treat it as a collection of clockwise steps it contributes with $|\pi_s|-1$ clockwise winds. It follows that $$\begin{gathered}
\sum_{1\leq s\leq t} (\text{number of clockwise winds of } b_s)=\\
1+\sum_{1\leq s\leq r} (|\pi_s|-1)=n-r+1
\end{gathered}$$ since $\sum_{1\leq s\leq r} |\pi_s|=n$. Therefore [\[eq:formulanak\]](#eq:formulanak){reference-type="eqref" reference="eq:formulanak"} gives us

$$\label{eq:formulanastopien} \deg \Sigma_{\pi}=
k_1+\dots+k_t+t=r+t-1,$$ where the degree is taken with respect to the filtration [\[eq:filtration\]](#eq:filtration){reference-type="eqref" reference="eq:filtration"}.

[]{#subsec:zaklejanie label="subsec:zaklejanie"} We can find a natural geometric interpretation of [\[eq:formulanastopien\]](#eq:formulanastopien){reference-type="eqref" reference="eq:formulanastopien"}: consider a large sphere with a small circular hole. The boundary of this hole is the circle that we consider in the graphical representations of partitions. Some pairs of points on this circle are connected by lines: the blocks of the partition $\pi_{\mathop{\mathrm{fat}}}$. To the arcs on the boundary of the circle between points $1,1',2,2',\dots,n,n'$ and to the lines of $\pi_{\mathop{\mathrm{fat}}}$ we shall glue two collections of discs. Every disc from the first collection corresponds to one of the blocks of $\pi$ (cf Figure [10](#fig:firstcollection){reference-type="ref" reference="fig:firstcollection"}).

<figure id="fig:firstcollection">
<embed src="figure12.eps" />
<figcaption>The first collection of discs for partition <span class="math inline"><em>π</em></span> from Figure <a href="#fig:przecinajacapartycja" data-reference-type="ref" data-reference="fig:przecinajacapartycja">1</a>.</figcaption>
</figure>

After gluing the first collection of discs, our sphere becomes a surface with a number of holes. The boundary of each hole corresponds to one of the cycles of $\pi_{\mathop{\mathrm{fat}}}\circ c$ and we shall glue this hole with a disc from the second collection.

Thus we obtained an orientable surface without a boundary. We define the genus of the partition $\pi$ to be the genus of this surface. The numbers of vertices, edges and faces of the polyhedron constructed above are the following: $V=2n$, $E=3n$, $F=1+r+t$ therefore the genus of this surface is equal to $$\label{eq:genus} \mathop{\mathrm{genus}}_\pi=\frac{2-V+E-F}{2}=\frac{n+1-r-t}{2}.$$ We proved therefore the following result.

::: proposition
[]{#prop:genusowatosc label="prop:genusowatosc"} For any partition $\pi$ of an $n$--element set $$\label{eq:genusowatosc} \deg \Sigma_{\pi}=n-2 \mathop{\mathrm{genus}}_\pi,$$ where the degree is taken with respect to the filtration [\[eq:filtration\]](#eq:filtration){reference-type="eqref" reference="eq:filtration"}.
:::

We leave the proof of the following simple result to the reader.

::: proposition
[]{#prop:genuszero label="prop:genuszero"} A partition is non--crossing if and only if its genus is equal to zero.
:::
