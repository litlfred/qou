---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF FAREY MANIFOLDS"
section_id: sec-009-22-oncepunctured-torus-bundles
section_title: "Once–punctured torus bundles"
section_number: 2.2
pages: 7-10
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.878
doc_brief: "CUSP AREAS OF FAREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on the cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2–bridge link complements."
---
[]{#sec:ptorus label="sec:ptorus"}

Let $V_\varphi$ be a hyperbolic punctured torus bundle with monodromy $\varphi$. The mapping class group of the punctured torus is isomorphic to $SL_2({\mathbb{Z}})$. By a well--known argument that we recall below, either $\varphi$ or $-\varphi$ is conjugate to an element of the form $$\Omega = R^{a_1}L^{b_1}\cdots R^{a_s}L^{b_s},$$

where $a_i, b_i$ are positive integers, and $R$ and $L$ are the matrices $$R := \begin{bmatrix} 1& 1 \\ 0&1\end{bmatrix}, \quad
    L := \begin{bmatrix} 1& 0 \\ 1& 1 \end{bmatrix}.$$

Moreover, $\Omega$ is unique up to cyclic permutation of its letters.

By projecting $\varphi$ down to $PSL_2({\mathbb{Z}}) \subset Isom({\mathbb{H}}^2)$, we may view the matrix $\pm \varphi$ as an isometry of ${\mathbb{H}}^2$ in the upper half--plane model, where the boundary at infinity of ${\mathbb{H}}^2$ is ${\mathbb{R}}\cup \{ \infty \}$. Then the slopes of the eigenvectors of $\varphi$ are the fixed points of its action on $\overline{{\mathbb{H}}^2}$.

Now, subdivide ${\mathbb{H}}^2$ into ideal triangles, following the *Farey tesselation* ${\mathcal{F}}$. In this tesselation, every vertex is a rational number (or $\infty$) in ${\partial}{\mathbb{H}}^2$. Each such vertex corresponds to a *slope* on the punctured torus $T$, that is, an isotopy class of arcs running from the puncture to itself. Two vertices are connected by an edge in ${\mathcal{F}}$ if and only if the corresponding arcs can be realized disjointly. Thus an ideal triangle of ${\mathcal{F}}$ corresponds to a triple of disjoint arcs, which gives an ideal triangulation of $T$. The monodromy $\varphi$ naturally acts on ${\mathcal{F}}$.

There is an oriented geodesic $\gamma_\varphi$ running from the repulsive fixed point of $\varphi$ to its attractive fixed point. This path crosses an infinite sequence of triangles of the Farey graph $(\dots, t_{-1}, t_0, t_1, t_2, \dots)$. We can write down a bi-infinite word corresponding to $\varphi$, where the $k$-th letter is $R$ (resp. $L$) if $\gamma_\varphi$ exits the $k$-th triangle $t_k$ to the right (resp. left) of where it entered. This bi-infinite word will be periodic of period $m$, where $m$ is some integer such that $t_0$ is taken by $\varphi$ to $t_m$. Then letting $\Omega$ be any subword of length $m$, and substituting the matrices above for $R$ and $L$, we find that $\pm \Omega$ is conjugate to $\varphi$.

Next, we review the relation between the word $\Omega$ and the triangulation of $V_\varphi$. The path $\gamma_\varphi$ through the Farey graph determines a sequence of triangulations of the punctured torus $T$. Every time $\gamma_\varphi$ crosses an edge $e \subset
{\mathcal{F}}$, moving from one triangle of ${\mathcal{F}}$ to an adjacent triangle, we change one ideal triangulation of $T$ (call it $\tau_-(e)$) into a different ideal triangulation $\tau_+(e)$, replacing a single edge with another. In other words, we are performing a diagonal exchange in a quadrilateral of $T$. This diagonal exchange determines an ideal tetrahedron $\Delta(e)$ as follows. The boundary of the tetrahedron is made up of two pleated surfaces homotopic to $T$, with triangulations corresponding to $\tau_-(e)$ and $\tau_+(e)$. These two pleated surfaces are glued together along the two edges in $T$ where $\tau_-(e)$ and $\tau_+(e)$ agree. The result is an ideal tetrahedron. See Figure [1](#fig:tetrahedra){reference-type="ref" reference="fig:tetrahedra"}.

![Copies of ideal tetrahedra in the cover $({\mathbb{R}}^2{\smallsetminus}
    {\mathbb{Z}}^2)\times {\mathbb{R}}$ of $T\times {\mathbb{R}}$.](figures/tetrahedra.eps){#fig:tetrahedra}

If $\gamma_\varphi$ crosses the edges $e_i$, $e_{i+1}$, then we may glue $\Delta(e_i)$ to $\Delta(e_{i+1})$ top to bottom, since $\tau_+(e_i) = \tau_-(e_{i+1})$. Thus $\gamma_\varphi$ determines a bi-infinite stack $U$ of tetrahedra. $U$ is homeomorphic to $T\times
{\mathbb{R}}$, and there is an orientation--preserving homeomorphism $\Phi$ of $U$, taking the $i$-th tetrahedron to the $(i+m)$-th tetrahedron, acting as $\varphi$ on $T$. The quotient $U/\Phi$ is homeomorphic to $V_\varphi$, and gives a triangulation of $V_\varphi$ into $m$ ideal tetrahedra. This is the Floyd--Hatcher triangulation of $V_\varphi$, also called the *monodromy triangulation*.

We summarize the discussion above as follows.

1.  The monodromy $\varphi$ of the bundle is conjugate to a word $$\Omega = \pm R^{a_1}L^{b_1}\cdots R^{a_s}L^{b_s}.$$

2.  Each letter $R$ or $L$ corresponds to a triangle in the Farey tesselation of ${\mathbb{H}}^2$.

3.  Each letter $R$ or $L$ corresponds to a pleated surface homotopic to $T$, pleated along arcs whose slopes are the vertices of the corresponding triangle of the Farey graph. This pleated surface forms the boundary between two tetrahedra of the canonical triangulation of $V_\varphi$.

::: define
Let $\Omega = \pm R^{a_1}L^{b_1}\dots R^{a_s}L^{b_s}$. A *syllable* of $\Omega$ is defined to be a subword $R^{a_i}$ or $L^{b_i}$. That is, a syllable is a maximal string of $R$'s or $L's$ in the word $\Omega$.
:::

A punctured torus bundle is a manifold with a single torus boundary component. It is often convenient to work with the universal cover ${\mathbb{H}}^3$ of the bundle, seen as the upper half space model, with the boundary lifting to the point at infinity in this model. Each of the pleated surfaces corresponding to the letters $R$ and $L$ will lift to ${\mathbb{H}}^3$. Their intersection with the boundary of a maximal cusp gives a triangulation of the boundary which is well understood. In particular, these intersections give a collection of *zigzags* that determine a triangulation of the boundary with combinatorics specified by the word $\Omega$. See Figure [2](#fig:stack){reference-type="ref" reference="fig:stack"}.

<figure id="fig:stack">
<div class="center">

</div>
<figcaption>Zigzags on the boundary torus of a punctured torus bundle. The pleated surfaces in this figure correspond to a sub-word <span class="math inline"><em>R</em><em>L</em><sup>4</sup><em>R</em><sup>4</sup><em>L</em> ⊂ <em>Ω</em></span>.</figcaption>
</figure>

::: define
A *zigzag* is defined to be the lift of one of the pleated surfaces corresponding to $R$ or $L$ to the universal cover ${\mathbb{H}}^3$, with the cusp lifting to infinity.
:::

Note that in pictures of zigzags, as in Figure [2](#fig:stack){reference-type="ref" reference="fig:stack"}, the vertices of the zigzag correspond to edges in ${\mathbb{H}}^3$ along which these zigzags meet. To distinguish separate zigzags, it is conventional to split them apart at the vertices. (In the manifold $M$, a sequence of pleated surfaces corresponding to a syllable of $\Omega$ will meet along a single edge. Thus, in a more topologically accurate but less enlightening picture, one would collapse together the split--apart vertices in Figure [2](#fig:stack){reference-type="ref" reference="fig:stack"}. See also [@gf:two-bridge Figure 4].)

Akiyoshi [@akiyoshi], Lackenby [@lackenby:punct], and Guéritaud [@gueritaud:thesis] have independently proved that this triangulation is geometrically canonical, i.e. dual to the Ford domain. As a result, each edge of the triangulation runs through the geometric center of a face of the Ford domain. (More precisely, each face of the Ford domain lifts to a hemisphere in ${\mathbb{H}}^3$, and each edge of the triangulation runs through the geometric center of the hemisphere.) Thus, when viewed from infinity, the "corners" of the zigzag lie over centers of hemispheres projecting to faces of the Ford domain. We will use this extensively below. See, for example, Figure [\[fig:zigzag\]](#fig:zigzag){reference-type="ref" reference="fig:zigzag"} below.
