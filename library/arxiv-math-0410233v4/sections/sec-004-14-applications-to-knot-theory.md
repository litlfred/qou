---
doc_id: arxiv-math-0410233v4
doc_title: "CUSP SHAPES UNDER CONE DEFORMATION"
section_id: sec-004-14-applications-to-knot-theory
section_title: "Applications to knot theory"
section_number: 1.4
pages: 5-7
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.979
doc_brief: "CUSP SHAPES UNDER CONE DEFORMATION — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp shape."
---
In the last part of this paper we give specific applications of Theorem [\[thm:main-norm-height\]](#thm:main-norm-height){reference-type="ref" reference="thm:main-norm-height"}. We determine bounds on the cusp shape of a knot based solely on a diagram of that knot.

Before we state the results, we review some definitions.

::: define
Let $K \subset S^3$ be a knot with diagram $D(K)$. Define a *twist region* to be a region of $D(K)$ where two strands of the diagram twist around each other maximally. Precisely, if $D(K)$ is viewed as a 4--valent planar graph with over--under crossing information at each vertex, then a twist region is a maximal string of bigons in the complement of the graph arranged end to end, or a single vertex of the graph adjacent to no bigons.
:::

We also require the diagram to be reduced, in the sense of the following two definitions. These definitions are illustrated elsewhere (see e.g. [@lackenby:surg], [@futer-purcell]).

::: define
A diagram $D(K)$ is *prime* if when any simple closed curve $\gamma$ intersects $D(K)$ transversely in two points in the interiors of edges, then $\gamma$ bounds a subdiagram containing no crossings of the original diagram. []{#def:prime label="def:prime"}
:::

::: define
The diagram $D(K)$ is *twist reduced* if when any simple closed curve $\gamma$ intersects $D(K)$ transversely in four points in the interiors of edges, with two of these points adjacent to one crossing and two others adjacent to another crossing, then $\gamma$ bounds a subdiagram consisting of a (possibly empty) collection of bigons arranged end to end between these two crossings. []{#def:twred label="def:twred"}
:::

Any diagram of a prime knot or link can be simplified into a prime, twist reduced diagram. If the diagram is not prime, then crossings on one side of a simple closed curve are extraneous and can be removed. If the diagram is not twist reduced, then performing flypes will amalgamate two twist regions adjacent to a simple closed curve into one, reducing the number of twist regions.

For a hyperbolic knot complement, we can choose a horoball neighborhood about the cusp such that a meridian on the boundary of that horoball has length $1$ (see e.g. [@adams:waist]). Consider the geodesic arc orthogonal to the meridian which runs from meridian to meridian on this horospherical torus. Define the length of this arc to be the *height* of the cusp. Note that when the meridian is the shortest curve on the cusp (as will be the case in the knots of this paper), this definition of height agrees with that in Theorem [\[thm:main-norm-height\]](#thm:main-norm-height){reference-type="ref" reference="thm:main-norm-height"}.

Let $K$ be a knot in $S^3$ which admits a prime, twist reduced diagram with at least $2$ twist regions, with each twist region containing at least $6$ crossings. Then it was shown in [@futer-purcell] that $S^3-K$ is hyperbolic. The following theorem gives bounds on the cusp shape.

::: theorem
Let $K$ be a knot in $S^3$ which admits a prime, twist reduced diagram with a total of $n\geq 2$ twist regions, with each twist region containing at least $c\geq 116$ crossings. In a hyperbolic structure on $S^3-K$, take a horoball neighborhood $U$ about $K$. Normalize so that the meridian on $\partial U$ has length $1$. Then the height $H$ of the cusp of $S^3-K$ satisfies: $$H\geq n\,(1-f(c))^2.$$ Here $f(c)$ is a positive function of $c$ which approaches $0$ as $c$ increases to infinity.

Additionally, $H\leq n(\sqrt{n-1} + f(c))^2$. []{#thm:main-knot-cusp label="thm:main-knot-cusp"}
:::

The function $f$ is given explicitly in Section [\[sec:knots\]](#sec:knots){reference-type="ref" reference="sec:knots"}. We can plug in values of $c$ to obtain more specific estimates. For example, in Corollary [\[cor:0.8\]](#cor:0.8){reference-type="ref" reference="cor:0.8"} we let $c=145$. Then $1-f(c)$ is approximately $0.8154$.

Note that the shortest non-meridional slope on the cusp of $S^3-K$ will have length at least that of the height. So Theorem [\[thm:main-knot-cusp\]](#thm:main-knot-cusp){reference-type="ref" reference="thm:main-knot-cusp"} implies that in this case, the shortest non-meridional slope has length at least $n\,(1-f(c))^2$.

By results of Hodgson and Kerckhoff [@hk:univ], Dehn filling along a slope with normalized length at least $7.515$ results in a hyperbolic manifold. Corollary [\[cor:0.8\]](#cor:0.8){reference-type="ref" reference="cor:0.8"} implies that for a complicated knot, the shortest non-meridional slope will have normalized length at least $\sqrt{n}(0.8154)$. Thus the normalized length of a slope will be larger than $7.515$ whenever $n\geq 85$. Thus we have the following corollary to Theorem [\[thm:main-knot-cusp\]](#thm:main-knot-cusp){reference-type="ref" reference="thm:main-knot-cusp"}:

::: corollary
Let $K$ be a knot in $S^3$ which admits a prime, twist reduced diagram with at least $85$ twist regions and at least $145$ crossings per twist region. Then any non-trivial Dehn filling of $S^3-K$ is hyperbolic. []{#cor:knot-cusp label="cor:knot-cusp"}
:::

Corollary [\[cor:knot-cusp\]](#cor:knot-cusp){reference-type="ref" reference="cor:knot-cusp"} is proven without any reference to the geometrization conjecture. If we assume that conjecture, then we recently proved (with Futer [@futer-purcell]) that the numbers $85$ and $145$ could be reduced to $4$ and $6$ respectively. However, note the proof of that result gives no geometric information on cusp geometry.

The numbers of crossings, 116 and 145, can be reduced significantly for certain classes of knots. We illustrate this in section [\[subsec:2bridge\]](#subsec:2bridge){reference-type="ref" reference="subsec:2bridge"} for 2--bridge knots.
