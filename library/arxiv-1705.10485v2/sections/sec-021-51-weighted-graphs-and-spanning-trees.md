---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-021-51-weighted-graphs-and-spanning-trees
section_title: "Weighted graphs and spanning trees"
section_number: 5.1
pages: 40-41
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.822
latex_coverage_ratio: 0.952
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
An *edge-weighted graph* $G$, or *weighted graph* for short, is a graph $G$ in which each edge $e$ is assigned a weight $w_G(e)$. Here we restrict ourselves to weights $w_G(e)$ with $w_G(e) \in \mathbb{R}_+$. Edges not in the graph can be thought of as edges of weight $0$, all our definitions being consistent with this convention.

If $B$ is a multiset of vertices of $G$, we can consider the graph $G[B]$ induced by $G$ on $B$ and defined as follows: the vertices of $G[B]$ correspond to elements of $B$ (if $B$ contains an element with multiplicity $m$, then $m$ vertices correspond to this element), and there is an edge between two vertices if the corresponding vertices of $G$ are equal or connected by an edge in $G$. This new graph has a natural weighted graph structure: put on each edge of $G[B]$ the weight of the corresponding edge in $G$ (if the edge connects two copies of the same vertex of $G$, we put weight $1$).

::: definition
A spanning tree of a graph $G=(V,E)$ is a subset $E'$ of $E$ such that $(V,E')$ is a tree. In other words, it is a subgraph of $G$ that is a tree and covers all vertices.
:::

The set of spanning trees of $T$ is denoted $\mathop{\mathrm{ST}}(G)$. If $G$ is a weighted graph, we say that the weight $w(T)$ of a spanning tree of $G$ is defined as the *product* of the weights of the edges in $T$.

<figure id="fig:weighteddependency">
<div class="center">

</div>
<figcaption>A weighted dependency graph <span class="math inline"><em>G</em></span> for <span class="math inline">7</span> random variables; the induced graph <span class="math inline"><em>G</em>[<em>B</em>]</span> with <span class="math inline"><em>B</em> = {1, 2, 3, 4, 4}</span>; and a spanning tree <span class="math inline"><em>T</em></span> of <span class="math inline"><em>G</em>[<em>B</em>]</span>, with <span class="math inline"><em>w</em>(<em>T</em>) = <em>w</em><sub>12</sub><em>w</em><sub>23</sub><em>w</em><sub>34</sub></span>.<span id="fig:weighteddependency" label="fig:weighteddependency"></span></figcaption>
</figure>
