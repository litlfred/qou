---
doc_id: arxiv-2209.06973v1
doc_title: "On the geometry of two state models for the colored Jones polynomial"
section_id: sec-003-4-the-flow-lemma
section_title: "The flow lemma"
section_number: 4
pages: 14-17
source_pdf: 2209.06973v1.pdf
source_sha256: cc3393a17c48b9df
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.994
doc_brief: "On the geometry of two state models for the colored Jones polynomial — Using the ﬂow property of the R-matrix deﬁning the colored Jones polynomial, we establish a natural bijection between the set of"
---
::: lem
[]{#lem: flow lemma label="lem: flow lemma"} Let $\mathcal{K}$ be the Morse projection of a link. Then there is a natural bijection $\phi_{\pm }$ from the set of $\mathbb{Z}$-flows on $G_{\pm}\mathcal{K}$ to the set of $\mathbb{Z}$-flows of $P\mathcal{K}$. For $(+)$ it assigns the color of a blue edge of $G\mathcal{K}$ to the color of the part arc of $P\mathcal{K}$ following the transition, and assigns the red edge colors to the changes in the colors of the two incoming part arcs at the crossing corresponding to the transition. This map restricts for each $n\geq 1$ and $\pm$ to bijections of flows: $$\phi_{\pm}: \mathcal{F}_n(G_{\pm}\mathcal{K})\rightarrow \mathcal{F}^n_{\pm}(P\mathcal{K})$$
:::

::: proof
*Proof.* We will only consider the $(+)$-case and let $\mu$ be the number of components of the link in the morse projection. A given general potential as above defines a $(+)$-coloring on $P\mathcal{K}$ in $\mathbb{Z}$ as explained following Definition 3.3. But it also defines a corresponding coloring $f$ of the arc graph $G\mathcal{K}$. In fact, define $f(e_v^r)=r(v)$ for all vertices $v$, with vertices identified with overcrossing arcs. Define $f(e_v^b)=\beta_j$ for the vertex $v$ corresponding to the overcrossing arc containing the specific part arc chosen for the basing of the projection in Definition 3.3 for all $v$ of $G\mathcal{K}$ corresponding to overcrossing arcs. There can be vertices of $G\mathcal{K}$ corresponding to overcrossing circles. Assign the corresponding base value $\beta_i$ if this vertex represents the $i$-th component. Note that the part arcs of $P\mathcal{K}$ uniquely correspond to part arcs in the boundaries of the fat vertices. So $(+)$-coloring of $G\mathcal{K}$ defined following Definition 3.3 also defines a coloring of all part-arcs, which are following a vertex $v$ at which an overcrossing arc $v$ ends. So this defines $f(e_v^b)$ for all vertices $v$ of $G\mathcal{K}$. Note that conversely the coloring of $G\mathcal{K}$ extends to all part arcs in the boundaries of fat vertices by using red arcs adjacent to the vertex. In fact, using the orientation of the boundary of each fat vertex, add the value $f(e_w^r)$ for each edge $e_w^r$ ending at vertex $v$. Figure 7 below shows how the colors are mapped *locally*. The left hand side shows the overcrossing arc $u$ and the colorings of $P\mathcal{K}$ defining the corresponding colorings of the edges at the vertex $u$ of $G\mathcal{K}$. If we are given $i,j,k,\ell$ then the colorings of $G\mathcal{K}$ are as given in the Figure. Conversely if we have given the edge colorings of the blue and red edges at the vertex $u$ of $G\mathcal{K}$ with the $f(e_u^r)=r$ then the color $i$ is determined by considering the segment of the overcrossing arc $w$ from its beginning until the crossing $w$. The coloring at the beginning is given by $f(e_{w'}^b)$ where $w'$ is the overcrossing arc preceding $w$. Then $i$ is defined by adding the jumps at all overcrossings before reaching the vertex $w$. Then $\ell =i+r$ and $j,k$ are defined as $j_0+r_1+\ldots +r_{\rho }$ and $k=j-r$. Since $r\leq j$ it follows $k\geq 0$. It also follows immediately that the flow conditions correspond to each other, and moreover a flow in $\mathcal{F}_+^n(P\mathcal{K})$ defined in this way, corresponds to a flow in $\mathcal{F}_n(G\mathcal{K})$. For contributing states we assume that all colorings are nonnegative. We have $i,j,k,\ell \leq n$ for the coloring of the edges at vertex $u$ of $P\mathcal{K}$ (corresponding to the overcrossing arc vertex of $G\mathcal{K})$). Because we have a $(+)$-coloring of $P\mathcal{K}$ it follows $i+j=k+\ell$ and $\ell \geq i$. It follows $\ell -i\geq 0$. The numbers $r_1,\ldots ,r_{\rho }\geq 0$ are the jumps along the overcrossing arc $u$. It follows that $j=j_0+r_1+\ldots +r_{\rho }=\ell -i+k$. This is the flow condition also at the vertex $u$ of $G\mathcal{K}$. Moreover $j\leq n \Longleftrightarrow (\ell -i)+k\leq n$. If we begin with an $n$-flow on $G\mathcal{K}$ we have $j\leq n$, which implies $k=j-r\leq n$. Also $\ell =i_0+r_1'+\ldots +r_{\rho '}'+r\leq n$ because this is a sum of colorings of incoming edges at the vertex $w$, and $i=\ell -r\leq n$. So the $n$-bounded $(+)$-flows on $P\mathcal{K}$ exactly correspond to the $n$-flows on $G\mathcal{K}$.

::: center
![image](Figure7.pdf){width="99%"}
:::

*Figure 7* ◻
:::

::: rem
\(a\) The boundedness restrictions determine the contributing states in each model.

\(b\) It was pointed out in the proof of [@GL] in the knot case that colorings of the arc graph are determined by the colors of the red edges through the flow condition. Similarly Garoufalidis and Le point out that in the knot case the jumps at the crossings determine the part arc colorings of a long knot. It is in fact only this basic observation, which we generalize in the above lemma.

\(e\) Our formula generalization for [@GL] differs from the formula by the replacement of $t$ with $t^{-1}$, corresponding to the various conventions for the skein relation of the Jones polynomial.

\(f\) The flow condition is not special to the colored Jones polynomial. The $R$-matrix for the standard representation of $\mathfrak{sl}(N)$ given in [@T], 4.2.1 gives non-trivial contributions only $i=j\leq k=\ell$, with $i,j$ denoting the incoming colors and $k,\ell$ the outgoing colors at a crossing. Note that this condition transfers to $$f(e_v^b)=\sum_{e<e_v^r}f(e)$$ for the vertex colorings of $G\mathcal{K}$, additionally to the flow condition.
:::
