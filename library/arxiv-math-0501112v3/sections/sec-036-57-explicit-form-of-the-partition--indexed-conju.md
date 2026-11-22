---
doc_id: arxiv-math-0501112v3
doc_title: "arXiv:math/0501112v3 [math.CO] 31 May 2005"
section_id: sec-036-57-explicit-form-of-the-partition--indexed-conju
section_title: "Explicit form of the partition--indexed conjugacy class indicator $\Sigma_\pi$"
section_number: 5.7
pages: 33-35
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.913
latex_coverage_ratio: 0.917
doc_brief: "arXiv:math/0501112v3 [math.CO] 31 May 2005 — We study asymptotics of reducible representations of the symmetric groups Sq for large q."
---
[]{#subsec:explicit label="subsec:explicit"} Let $\pi$ be a partition of the set $\{1,\dots,n\}$. Since the fat partition $\pi_{\mathop{\mathrm{fat}}}$ connects every element of the set $\{1',2',\dots,n'\}$ with exactly one element of the set $\{1,2,\dots,n\}$, we can view $\pi_{\mathop{\mathrm{fat}}}$ as a bijection $\pi_{\mathop{\mathrm{fat}}}:\{1',2',\dots,n'\}\rightarrow\{1,2,\dots,n\}$. We also consider a bijection $c:\{1,2,\dots,n\}\rightarrow\{1',2',\dots,n'\}$ given by $\dots,3\mapsto 2', 2\mapsto 1', 1\mapsto n', n\mapsto
(n-1)',\dots$. Finally, we consider a permutation $\pi_{\mathop{\mathrm{fat}}}\circ
c$ of the set $\{1,2,\dots,n\}$.

For example, for the partition $\pi$ given by Figure [\[fig:przecinajacapartycja\]](#fig:przecinajacapartycja){reference-type="ref" reference="fig:przecinajacapartycja"} the composition $\pi_{\mathop{\mathrm{fat}}}\circ c$ has a cycle decomposition $(1,2,3,5,{4})({6},7)$, as it can be seen from Figure [1](#fig:tlustapartycja2){reference-type="ref" reference="fig:tlustapartycja2"}.

<figure id="fig:tlustapartycja2">
<embed src="figure09.eps" />
<figcaption>Bijection corresponding to the partition <span class="math inline"><em>π</em><sub>fat</sub></span> from Figure <a href="#fig:tlustapartycja" data-reference-type="ref" data-reference="fig:tlustapartycja">[fig:tlustapartycja]</a> plotted with a solid line and the bijection <span class="math inline"><em>c</em></span> plotted with a dashed line. </figcaption>
</figure>

We decompose the permutation $$\pi_{\mathop{\mathrm{fat}}}\circ c=(b_{1,1},b_{1,2},\dots,b_{1,j_1}) \cdots
(b_{t,1},\dots,b_{t,j_t})$$ as a product of disjoint cycles. Every cycle $b_s=(b_{s,1},\dots,b_{s,j_s})$ can be viewed as a closed clockwise path on a circle and therefore one can compute how many times it winds around the circle, cf Figure [2](#fig:tlustapartycja3){reference-type="ref" reference="fig:tlustapartycja3"}.

To a cycle $b_s$ we assign the number $$\begin{gathered}

k_s=(\text{number of elements in a cycle } b_s)-\\ (\text{number of
clockwise winds of }b_s).
\end{gathered}$$

In the above example we have $b_1=(1,2,3,5,4)$, $b_2=(6,7)$ and $k_1=2$, $k_2=1$, as it can be seen from Figure [2](#fig:tlustapartycja3){reference-type="ref" reference="fig:tlustapartycja3"}, where all lines clockwise wind around the central disc.

<figure id="fig:tlustapartycja3">
<embed src="figure10.eps" />
<figcaption>A version of Figure <a href="#fig:tlustapartycja2" data-reference-type="ref" data-reference="fig:tlustapartycja2">1</a> in which all lines wind clockwise around the central disc.</figcaption>
</figure>

In our recent work [@Sniady2003pushing] we proved that

$$\Sigma_\pi=\Sigma_{k_1,\dots,k_t},$$

where $\Sigma_{k_1,\dots,k_t}$ on the right--hand side should be understood as in Section [\[subsec:definicjasigma\]](#subsec:definicjasigma){reference-type="ref" reference="subsec:definicjasigma"}.
