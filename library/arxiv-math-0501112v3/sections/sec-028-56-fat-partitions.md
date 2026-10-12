---
doc_id: arxiv-math-0501112v3
doc_title: "arXiv:math/0501112v3 [math.CO] 31 May 2005"
section_id: sec-028-56-fat-partitions
section_title: "Fat partitions"
section_number: 5.6
pages: 32-35
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.917
---
[]{#subsec:fat label="subsec:fat"} Let $\pi=\{\pi_1,\dots,\pi_r\}$ be a partition of the set $\{1,\dots,n\}$. For every $1\leq s\leq r$ let $\pi_s=\{\pi_{s,1},\dots,\pi_{s,l_s}\}$ with $\pi_{s,1}<\cdots<\pi_{s,l_s}$. We define $\pi_{\mathop{\mathrm{fat}}}$, called fat partition of $\pi$, to be a pair partition of the $2n$--element ordered set $\{1,1',2,2',\dots,n,n'\}$ given by $$\pi_{\mathop{\mathrm{fat}}}=
\big\{  \{ \pi_{s,t}',\pi_{s,t+1}  \} :  1\leq s \leq r \text{ and }
1 \leq t \leq l_s  \big\},$$ where it should be understood that $\pi_{s,l_s+1}=\pi_{s,1}$.

<figure id="fig:tlustapartycja">
<embed src="figure04.eps" />
<figcaption>The fat partition <span class="math inline"><em>π</em><sub>fat</sub></span> corresponding to the partition <span class="math inline"><em>π</em></span> from Figure <a href="#fig:przecinajacapartycja" data-reference-type="ref" data-reference="fig:przecinajacapartycja">[fig:przecinajacapartycja]</a>.</figcaption>
</figure>

This operation can be easily described graphically as follows: we draw the blocks of the partition with a fat pen and take the boundary of each block, as it can be seen on Figure [1](#fig:tlustapartycja){reference-type="ref" reference="fig:tlustapartycja"}. This boundary is a collection of lines hence it is a pair partition. However, every vertex $k\in\{1,\dots,n\}$ of the original partition $\pi$ has to be replaced by its 'right' and 'left' copy (denoted respectively by $k$ and $k'$).

## Explicit form of the partition--indexed conjugacy class indicator $\Sigma_\pi$ {#subsec:explicit}

Let $\pi$ be a partition of the set $\{1,\dots,n\}$. Since the fat partition $\pi_{\mathop{\mathrm{fat}}}$ connects every element of the set $\{1',2',\dots,n'\}$ with exactly one element of the set $\{1,2,\dots,n\}$, we can view $\pi_{\mathop{\mathrm{fat}}}$ as a bijection $\pi_{\mathop{\mathrm{fat}}}:\{1',2',\dots,n'\}\rightarrow\{1,2,\dots,n\}$. We also consider a bijection $c:\{1,2,\dots,n\}\rightarrow\{1',2',\dots,n'\}$ given by $\dots,3\mapsto 2', 2\mapsto 1', 1\mapsto n', n\mapsto
(n-1)',\dots$. Finally, we consider a permutation $\pi_{\mathop{\mathrm{fat}}}\circ
c$ of the set $\{1,2,\dots,n\}$.

For example, for the partition $\pi$ given by Figure [\[fig:przecinajacapartycja\]](#fig:przecinajacapartycja){reference-type="ref" reference="fig:przecinajacapartycja"} the composition $\pi_{\mathop{\mathrm{fat}}}\circ c$ has a cycle decomposition $(1,2,3,5,{4})({6},7)$, as it can be seen from Figure [2](#fig:tlustapartycja2){reference-type="ref" reference="fig:tlustapartycja2"}.

<figure id="fig:tlustapartycja2">
<embed src="figure09.eps" />
<figcaption>Bijection corresponding to the partition <span class="math inline"><em>π</em><sub>fat</sub></span> from Figure <a href="#fig:tlustapartycja" data-reference-type="ref" data-reference="fig:tlustapartycja">1</a> plotted with a solid line and the bijection <span class="math inline"><em>c</em></span> plotted with a dashed line. </figcaption>
</figure>

We decompose the permutation $$\pi_{\mathop{\mathrm{fat}}}\circ c=(b_{1,1},b_{1,2},\dots,b_{1,j_1}) \cdots
(b_{t,1},\dots,b_{t,j_t})$$ as a product of disjoint cycles. Every cycle $b_s=(b_{s,1},\dots,b_{s,j_s})$ can be viewed as a closed clockwise path on a circle and therefore one can compute how many times it winds around the circle, cf Figure [3](#fig:tlustapartycja3){reference-type="ref" reference="fig:tlustapartycja3"}.

To a cycle $b_s$ we assign the number $$\begin{gathered}

k_s=(\text{number of elements in a cycle } b_s)-\\ (\text{number of
clockwise winds of }b_s).
\end{gathered}$$

In the above example we have $b_1=(1,2,3,5,4)$, $b_2=(6,7)$ and $k_1=2$, $k_2=1$, as it can be seen from Figure [3](#fig:tlustapartycja3){reference-type="ref" reference="fig:tlustapartycja3"}, where all lines clockwise wind around the central disc.

<figure id="fig:tlustapartycja3">
<embed src="figure10.eps" />
<figcaption>A version of Figure <a href="#fig:tlustapartycja2" data-reference-type="ref" data-reference="fig:tlustapartycja2">2</a> in which all lines wind clockwise around the central disc.</figcaption>
</figure>

In our recent work [@Sniady2003pushing] we proved that

$$\Sigma_\pi=\Sigma_{k_1,\dots,k_t},$$

where $\Sigma_{k_1,\dots,k_t}$ on the right--hand side should be understood as in Section [\[subsec:definicjasigma\]](#subsec:definicjasigma){reference-type="ref" reference="subsec:definicjasigma"}.
