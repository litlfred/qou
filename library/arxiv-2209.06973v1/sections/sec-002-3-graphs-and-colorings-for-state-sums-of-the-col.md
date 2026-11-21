---
doc_id: arxiv-2209.06973v1
doc_title: "On the geometry of two state models for the colored Jones polynomial"
section_id: sec-002-3-graphs-and-colorings-for-state-sums-of-the-col
section_title: "Graphs and colorings for state-sums of the colored Jones polynomial"
section_number: 3
pages: 5-14
source_pdf: 2209.06973v1.pdf
source_sha256: cc3393a17c48b9df
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.993
doc_brief: "On the geometry of two state models for the colored Jones polynomial — Using the ﬂow property of the R-matrix deﬁning the colored Jones polynomial, we establish a natural bijection between the set of"
---
We will first consider *part arc-graphs* and *arc-graphs* following [@GL], which are defined from Morse projections $\mathcal{K}$. We will also introduce a third type of graph representation (and the corresponding colorings), which we call chord graphs, closely related to the chord diagrams in Vassiliev theory.

In the following sections we will restrict to closed braid diagrams.

A *Morse projection* $\mathcal{K}$ is a smooth regular embedding of an oriented link in $\mathbb{R}^2\times [0,1]$, which projects to a smooth immersion in the plane $\mathbb{R}^2$, and such that the composition with the projection onto the $y$-axis defines a Morse function on the components of $\mathcal{K}$. Note that each regular projection can be approximated with a Morse projection by planar isotopy. Sometimes we will identify $\mathcal{K}$ just with the embedded circles.

The image of the immersion defined by $\mathcal{K}$ in $\mathbb{R}^2$ is the part arc-graph $P\mathcal{K}$ and is a four-valent planar directed graph, with signs $\pm$ assigned to each vertex. We will color part arc-graphs by $n$-bounded flows according to Definition [\[defn:edge coloring\]](#defn:edge coloring){reference-type="ref" reference="defn:edge coloring"} such that at all crossings the colors are increasing (respectively decreasing) along the overcrossing arc in the direction of the link orientation. Because of the flow condition, correspondingly the colors are decreasing (respectively increasing) along the undercrossing arc. This defines subsets $\mathcal{F}^n_{\pm }(P\mathcal{K})$ of $\mathcal{F}^n(\mathcal{P}\mathcal{K})$. The corresponding states are called $(+)$-colorings (respectively $(-)$-colorings).

Next we enhance the notion of arc graph as defined in [@GL] by adding additional decoration. Again we assume that the Morse projection $\mathcal{K}$ of a link is given as above.

::: center
![image](Figure1.pdf){width="80%"}
:::

*Figure 1*

::: defn
[]{#defn:arc-graph label="defn:arc-graph"} Let $G\mathcal{K}=G_+\mathcal{K}$ be the bichromatic *labeled* fat digraph with (fat) vertices corresponding to overcrossing-arcs of $\mathcal{K}$. The edges of the graph are *decorated* by colors blue and red. The directed blue edge $e_v^b$ from a vertex $v$ to the vertex $w$ corresponds to the transition at the undercrossing at which we switch from the overcrossing arc ending at vertex $v$ to the next overcrossing arc ending at $w$. The red arc $e_v^r$ corresponds to the *jump up* transition at the end of arc $v$, as in the picture to the overcrossing arc (or circle) $w'$. The vertices corresponding to overcrossing arcs of $G\mathcal{K}$ are decorated by the signs of the vertices of $\mathcal{K}$ at which the corresponding overcrossing arc ends. Note that the vertices corresponding to overcrossing circles are not decorated by a sign. The boundary of each fat vertex is also decorated by an orientation. For a vertex corresponding to an arc this is from the incoming blue edge in the direction of the outgoing red edge.

There will be additional decorations $\pm$, called *rotation numbers* along the boundaries of fat vertices, which indicate when part arcs of $P\mathcal{K}$ run through a right oriented maximum respectively minimum. (We explain below in more detail how the part arcs on the boundaries of fat vertices are identified with the edges of $P\mathcal{K}$.) If a part arc runs through a sequence of right oriented extrema the contributions from maxima and minima will cancel, so that each part arc will carry at most one $\pm$.

The order of incoming red and blue arcs at a fat vertex is according to the corresponding order of overcrossings in $\mathcal{K}$. We call this enhanced graph the *arc graph* for the given projection $\mathcal{K}$. In the setting of [@GL] no preferred ordering between the outgoing edges is given. But, our correspondence between states will suggest that the outgoing red edge precedes the outgoing blue edge. There is a graph defined from undercrossing arcs in the same way, denoted $G_-\mathcal{K}$.
:::

::: rem
\(a\) There is exactly one red edge $e_v^r$ and one blue edge $e_v^b$ out of each vertex $v$ of $G\mathcal{K}$ corresponding to an overcrossing arc. For an overcrossing *circle* there are no outgoing edges and there is no incoming blue edge. Depending on possible overcrossings, there will be an even number of incoming red edges. A special case of an overcrossing arc is the projection of a figure eight. In this case there are one blue edge and one red edge incident with this vertex, which are both outgoing and ingoing. There can be additional incoming red edges corresponding to the figure eight component overcrossing other components of $\mathcal{K}$. We will usually not consider projections of this form because we could isotope into a *split* projection.

\(b\) We divide the boundary of each fat vertex corresponding to an overcrossing arc into an *active half-circle*, starting at the incoming blue edge and ending at the outgoing red edge. The complementary half-circle is the *passive* half-circle, and is colored yellow in Figure 1. The boundary of the fat vertex corresponding to an overcrossing circle will be considered active. Note that the part-arcs of the active part of the boundaries of fat vertices of $G\mathcal{K}$ exactly correspond to the part-arcs of $P\mathcal{K}$.

\(c\) Suppose that a Morse projection $\mathcal{K}$ of a link is equipped with a preferred part arc of the corresponding part arc graph $P\mathcal{K}$ as in Figure 2, i. e. the only part of the projection outside of the box is the right maxima arc.

::: center
![image](Figure2.pdf){width="60%"}
:::

*Figure 2*

In this case we can open the projection naturally to include a long component, and consider this *long component* projection $\overline{\mathcal{K}}$ (the dashed half arcs replace the semi-circle). Usually we will omit the dash in notation and denote by $\mathcal{K}$ also the Morse projection of a long component projection. The corresponding part arc-graph is defined from the new projection just as in the closed case but the special arc is now cut into the two oriented half arcs. Note that a long component Morse projection closes uniquely to a projection by closing long component with a right oriented maximum. The two processes are inverse to each other. Suppose that the long component is not an overcrossing arc and the crossing adjacent to the bottom half arc is an undercrossing at the end of the half arc as in Figure 2. We will usually not introduce a different notation for long component projections. In this case we associate to the long component projection the *reduced arc-graph*, see the discussion in section 7 below.

\(d\) A Morse projection $\mathcal{K}$ is alternating if and only if each fat vertex of $G\mathcal{K}$ has exactly one incoming red edge, or no incoming red edge for a circle arc without crossings.

\(e\) Note that $P\mathcal{K}$ is a planar graph while $G\mathcal{K}$ is an abstract graph. Not every bichromatic enhanced graph as defined above is the arc graph of a Morse projection. This is due to the missing horizontal compatibility of red edges in the graph. Below we define chord graphs, which will include this information. It seems interesting to extend arc graphs to the setting of virtual projections by adding undirected red edges corresponding to virtual crossings.
:::

::: defn
A coloring of $G\mathcal{K}$ is a coloring of all blue and red edges. Moreover, for each fat vertex corresponding to an overcrossing circle there will be a color assigned to a part-arc of the boundary, if there are incoming red edges, or to the whole boundary circle otherwise. The coloring will be $n$-bounded at each vertex corresponding to an overcrossing arc, and it will satisfy that the sum of all incoming red edge colors is $0$. Note that if we run through a component of $\mathcal{K}$ we run through the active edges of $G\mathcal{K}$ (we will jump across blue edges whenever we switch from one overcrossing arc to the next one), thereby traversing a connected component of $G\mathcal{K}$. While traversing the active boundaries of the corresponding fat vertices following the orientations we cross red incoming edges. We require that the sum of the colors of all incoming red edges minus the sum of the colors of all outgoing red edges adds to zero for each component. We require additionally that the $n$-flow condition is met at each vertex corresponding to an arc. See the definition of potential below to understand these conditions. The set of all those colorings of $G\mathcal{K}$ is denoted $\mathcal{F}_n(G\mathcal{K})$. This is a subset of the set of functions $f: E\rightarrow \underline{n}$, except if $G$ contains vertices corresponding to overcrossing circles. In this case $f$ is defined on the union of the set of all red and blue edges and a part arc in the boundary of the fat vertex or the whole boundary of the fat vertex as discussed above.
:::

Let $\mathcal{P}\mathcal{K}$ the part arc-graph of a Morse projection $\mathcal{K}$ of a link $K$ with $\mu$ components. Let $V$ be the set of vertices corresponding to crossings of distinct components of $P\mathcal{K}$, and $V=\sqcup _{1\leq j\leq k\leq \ell} V_{jk}$ with $V_{jk}$ corresponding to the set of crossings of the $j$-th and $k$-th component, $V_{jk}=V_{kj}$. In the following we will assume that the components of $\mathcal{K}$ are ordered and a part arc is chosen on each component, which is not an overcrossing circle. We call this a *basing*. The chosen part arc will usually be the first part arc on an overcrossing arc but exceptions are possible. Note that when considering braid projections there is a natural way to choose the basing. For long component projections the long component will always be chosen as the first component and the part arc can be chosen by one of the two long half-arcs. We call a projection with ordering and basing of components *based*.

::: defn
[]{#defn=potential label="defn=potential"} A *potential* on a based projection $\mathcal{K}$ is a pair of functions $(r,\beta )$ with $r: V\rightarrow \mathbb{N}_0$ and $\beta :\{2,\ldots ,\mu \}\rightarrow \mathbb{N}_0$. Here $V$ is the vertex set of the part arc-graph. We call $\beta_i$ the *base values* of the potential, and the function $r$ defines the *jump values*. For $\mu >1$ the following relations are required for $1\leq i\leq \mu$: $$\sum_{ i\neq j\\ ,c\in V_{i,j}}\lambda_i(c)r(c)=0$$ We call these relations *cycle relations*. Here $\lambda_i(c)=\pm 1$ depending on whether while walking along the $i$-th component the crossing $c$ is an overcrossing respectively an undercrossing. We will sometimes work with $\mathbb{Z}$-potentials defined as above but with $\beta ,r$ possibly taking values in $\mathbb{Z}$.
:::

::: rem
\(a\) It is important to note that the cycle relations are not independent, e. g. the relation for $i=1$ is the negative of the sum of the relations for $2\leq j\leq \mu -1$. This follows because each $r(c)$ appears in exactly two relations but with different signs. So if we sum relations for $1\leq i\leq \mu$ then the result is $0$.

\(b\) For a long component projection we will assume that the first component is long component. Moreover, the part arc on the first component chosen

\(c\) A braid induces framing, orientation, ordering and basing (choice of base-point) of the components of the link. The base-point on a component is determined by the part-arc at the bottom of the link on the first arc on the component from the left.
:::

Each potential determines an edge-coloring of $P\mathcal{K}$ in $\mathbb{Z}$ as follows: Use the function $\beta$ to define the coloring of part-arcs at basings for all components except the first one. For the left-bottom part-arc on the first component define the color to be $0$. Then, along each component, at crossing $c$ change the edge-coloring according to the diagram below. This means adding the value $r(c)$ along an overcrossing and subtracting along an undercrossing (flow condition). We think of the potential as giving the derivative and base values for the coloring of $P\mathcal{K}$. A *contributing potential* is a potential for which all resulting edge-colorings take values in $\mathbb{N}_0$. We use this language to indicate that this means that the state will be contributing to the state-sum of the $n$-colored Jones polynomial for a large value of $n$. The potential is $n$-contributing (usually we just say only contributing if $n$ is clear from the context) if all resulting edge colors are in $\underline{n}$. This implies that $r,\beta$ have to take values in $\underline{n}$. It follows from the formulas for state-sum contributions discussed in sections 5 and 6 that $n$-contributing states are exactly those which will be contributing to the state-sum of the $n$-th colored Jones polynomial. Of course, restricting the values of $r,\beta$ to $\underline{n}$ does not necessarily define $n$-bounded flows. But any negative edge coloring will result in non-contributing states. This will follow from the definitions of quantum binomials and Pochhammer symbols in section 5. See Definition [\[defn:edge coloring\]](#defn:edge coloring){reference-type="ref" reference="defn:edge coloring"} above. We will discuss the inequalities defining contributing states in section 7.

The cycle conditions guarantee that returning to the basepoints along each component means returning to the starting color $\beta (j)=:\beta_j, \beta_0:=0$ along each component. Note that starting from the base-points each self-crossing is traversed twice and the color changes cancel.

::: defn
Each Morse projection $\mathcal{K}$, which is equipped with an ordering of the components and a choice of base point on each component, defines a *chord graph* as follows: The chord graph $C\mathcal{K}$ of $\mathcal{K}$ is given by $\mu$ ordered, based and oriented circles. Each crossing is represented by an oriented chord. If the orientation of the circle followed by the orientation of an incoming chord at a point on a circle is the positive orientation of the plane then proceeding along the circle in the direction of its orientation at this point is an overcrossing of the correspond arc on the circle, correspondingly at outgoing chords the arcs along circles correspond to undercrossing arcs of $\mathcal{K}$. The sign of the crossing is added as $\pm$ decorating the chords by pairs $(r,\varepsilon )$. Sometimes we do not need this additional decoration. If we want to emphasize the crossing signs we also talk about *signed* chord graphs.

A coloring of a chord graph is given by adding the data from a potential to the chords, and basepoints on the circles ordered $2,\ldots ,\mu$.
:::

The chords subdivide the circles into arcs corresponding to the edges of $\mathcal{K}$. A potential on $\mathcal{K}$ induces a coloring of the chord graph. We will usually work with $\mathbb{Z}$-chord graph colorings, so allow functions $r,\beta$ to take values in $\mathbb{Z}$. Note that changing the orientation of a chord and the sign of the color of the chord will not change the corresponding part-arc coloring on $\mathcal{K}$. By definition, a chord graph is the graph of an abstract collection of $\mu$ circles and chords, which is not necessarily induced from the chord graph on a part arc-graph $\mathcal{K}$. But we assume that all chord graph colorings satisfy the cycle conditions. Note that for each chord graph induced from a projection $\mathcal{K}$ the number of chords between different circles is even, while we do not require this for abstract chord graphs.

If $\mathcal{K}$ is defined from a closed braid projection then we will furthermore assume that chords *respect* the *horizontal* positions induced from a braid in the following way: For this imagine that we label the strings of the braid $1,2,\ldots , \mathfrak{s}$. Then we can assign numbers between $1$ and $\mathfrak{s}$ to each part-arc represented by a segment between chords on a circle of the chord graph. Here we assume that the part-arcs run vertically upwards along the braid except at a crossing represented by a braid generator $\sigma_i$ corresponding to the permutation $(i,i+1)$ and the incoming left bottom part-arc will get an additional horizontal position label $i$. Note that crossing an *incoming* chord (means that the orientation of the chord is positive) with positive sign means that the horizontal position increases. The same will be true for an outgoing chord carrying a negative sign. The point here is that in order to be induced from a braid the horizontal positions have to match as in the following picture. Note that the two vertical arcs represent arcs on component circles but can also be arcs on the same circle. This is just the representation of the braid generator $\sigma_k^{\varepsilon }$. Compare with the discussion of *special* Morse projections as discussed following Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"}.

::: center
![image](Figure3.pdf){width="45%"}
:::

*Figure 3*

Note that switching sign and orientation of the chord and replacing $r$ by $-r$ simultaneously, we get both the same jumps in colors and horizontal positions on the two circle segments. Using negative chord colors $r$ will be essential for some of our arguments.

::: exmp
Below is the braid (long) projection of $\sigma_1\sigma_2^{-1}\sigma_1$, which is a $2$-component link. The cycle relation is $r_2=r_3$. For contributing states we further have to restrict to $r_1\leq r_3\leq \beta_2$. The chord graph gives a very transparent way of recording the coloring of all part-arcs. Note that we use the overcrossing arc ordering of the vertices and corresponding values for $r(i)=r_i$. In this case we placed the base color on the part arc following the first undercrossing from the bottom on the second component. Where the base values are placed is not important for part arc graph or chord graph. But since we color blue edges of the arc graph we usually place base values on the specific part arcs leaving the crossing on the undercrossing.

::: center
![image](Figure4.pdf){width="95%"}
:::

*Figure 4*

Figure 5 below shows the corresponding arc graph as defined in section 2. Note that ${\color{green}*}$ are labeling the part-arcs, which run downwards in the braid closure. Note that the the $f(e_3^b)=\beta_2-r_3$ is not a base value.

::: center
![image](Figure5.pdf){width="75%"}
:::

*Figure 5*
:::

From the colored arc-graph the corresponding Garoufalidis-Loebl state-sum contribution will be determined without reference to the part arc-graph, see section 6.

::: rem
For each Morse projection $\mathcal{K}$, $P\mathcal{K}$ determines $C\mathcal{K}$, from which $G\mathcal{K}$ can be deduced as follows. Just cut the fat vertices from disks bounding the circles of the chord graph by introducing cut arcs (see Figure 6) following each outgoing chord. The blue edges then are easily added like in the picture. Note that the cut arcs added correspond to the passive half arcs in the boundaries of fat vertices. Also colorings of $C\mathcal{K}$ induce the colorings on $G\mathcal{K}$.

::: center
![image](Figure6.pdf){width="70%"}
:::

*Figure 6*
:::
