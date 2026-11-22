---
doc_id: arxiv-math-0410233v4
doc_title: "CUSP SHAPES UNDER CONE DEFORMATION"
section_id: sec-023-64-example-2bridge-knots
section_title: "Example: 2–bridge knots"
section_number: 6.4
pages: 41-44
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.985
doc_brief: "CUSP SHAPES UNDER CONE DEFORMATION — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp shape."
---
[]{#subsec:2bridge label="subsec:2bridge"}

The requirement of Theorem [\[thm:main-knot-cusp\]](#thm:main-knot-cusp){reference-type="ref" reference="thm:main-knot-cusp"} that there be at least $116$ crossings per twist region was based on the worst case analysis. This came from Proposition [\[prop:proj-height\]](#prop:proj-height){reference-type="ref" reference="prop:proj-height"}, in which we showed that in the worst possible case, the normalized length of a slope was at least the square root of the number of crossings. When we are dealing with particular classes of knots, we can often make significantly better estimates, and reduce the number of crossings required. In this section, we present a particular example of such a class of knots: 2--bridge knots.

We will determine the circle packing obtained from the proof of Theorem [\[thm:Lhyp\]](#thm:Lhyp){reference-type="ref" reference="thm:Lhyp"} for a 2--bridge knot. A 2--bridge knot with an even number of twist regions will have a corresponding augmented link $L$ of the form of Figure [1](#fig:2bridge){reference-type="ref" reference="fig:2bridge"}, except possibly with single crossings added at some crossing circles. The picture for an odd number of twist regions is similar.

<figure id="fig:2bridge">
<div class="center">

</div>
<figcaption>Augmented link of a 2–bridge knot with an even number of twist regions, and an even number of crossings per region.</figcaption>
</figure>

In any case, the link will correspond to a trivalent graph $\Gamma$ of the form shown in Figure [2](#fig:2bridge_tri){reference-type="ref" reference="fig:2bridge_tri"}. Note each region of the graph complement gives a circle in the circle packing, with tangencies across edges. Thus each circle will be tangent to the circles corresponding to regions $A$ and $D$. The circle packing associated with this graph is of the form in Figure [3](#fig:2bridge_circ){reference-type="ref" reference="fig:2bridge_circ"}.

<figure id="fig:2bridge_tri">
<div class="center">

</div>
<figcaption>Trivalent graph associated with a 2–bridge knot.</figcaption>
</figure>

<figure id="fig:2bridge_circ">
<div class="center">

</div>
<figcaption>Circle packing associated with a 2–bridge knot.</figcaption>
</figure>

Recall that the shape of cusps can be determined by analyzing the rectangles we get from taking points of tangency of the circles in Figure [3](#fig:2bridge_circ){reference-type="ref" reference="fig:2bridge_circ"} to infinity. In particular, we are interested in the cusp shapes which correspond to crossing circles in the link $L$. The rectangles tiling these cusps come from the tangencies of circle $A$ with certain of the $B_i$ and $C_i$, and from tangencies of $D$ with certain of the $B_i$ and $C_i$. Thus we find the general shape of rectangles of this form.

When we take a point of tangency between $A$ and $B_i$ to infinity, $i=1$ or $2$, the two circles tangent to both $A$ and $B_i$ are $D$ and a $C_j$. These are tangent to each other. Thus our rectangle in this case is a square. Similarly for points of tangency between $D$ and $B_i$.

A crossing circle coming from one of these points of tangency will therefore be tiled by two squares, with a longitude running across two shaded sides. Then the slope $s_i$ along which Dehn filling is performed will have normalized length $\sqrt{1+c_i^2}/\sqrt{2}$. Note this is larger than $I(0.6624)$, implying that the results of Theorem [\[thm:main-knot-cusp\]](#thm:main-knot-cusp){reference-type="ref" reference="thm:main-knot-cusp"} apply, provided $c_i \geq 16$. It is larger than $I(1.0)$, implying the results of Corollary [\[cor:0.8\]](#cor:0.8){reference-type="ref" reference="cor:0.8"} hold, when $c_i \geq 17$. Thus the number of crossings in our theorem has gone from $116$ to $16$, and $145$ to $17$.

When we take a point of tangency between $A$ and $C_i$, or between $D$ and $C_i$ to infinity, we get a $1$ by $2$ rectangle. This is because the circles $A$ and $C_i$ are tangent to two distinct circles $C_{i-1}$ and $C_{i+1}$, or possibly a $B_i$, which are each tangent to $D$. Since $D$ is also tangent to $A$ and $C_i$, in the picture at infinity we have two parallel lines, $A$ and $C_i$, with three full sized circles tangent to each other and also to the lines $A$ and $C_i$.

In this case, the crossing circle is tiled by two $1$ by $2$ rectangles, stacked to form a square. The slope $s_i$ will have normalized length $\sqrt{4+c_i^2}/\sqrt{4}$. It will be larger than $I(0.6624)$ provided $c_i \geq 22$, and larger than $I(1.0)$ provided $c_i \geq 24$.

We can also make improvements on the initial normalized height, i.e. the value $h(X)$ of Theorem [\[thm:main-norm-height\]](#thm:main-norm-height){reference-type="ref" reference="thm:main-norm-height"}. To compute $h(X)$, we determine the shape of the rectangles tiling the cusp corresponding to the knot strand. These include all rectangles obtained by taking a point of tangency of the circle packing of Figure [3](#fig:2bridge_circ){reference-type="ref" reference="fig:2bridge_circ"} to infinity, except those tangencies corresponding to crossing circle cusps.

Each circle tangency of the form $C_{2k}$ tangent to $D$ will give a rectangle on the knot strand cusp. Similarly, those tangencies of circles $C_{2k+1}$ tangent to $A$ will give rectangles on the knot strand cusp. As we saw above, these rectangles will each have dimensions $1$ by $2$. The side of length $2$ will contribute to the height. There will be $(n-2)$ of these rectangles, since each $C_j$ contributes one. Thus these rectangles contribute $2n-4$ to the height.

Each circle tangency $C_i$ tangent to $C_{i+1}$ also gives a rectangle on the knot strand cusp, as do the tangencies $B_1$ with $C_1$ and $C_{n-2}$ with $B_2$. Each of these rectangles is a square, contributing $1$ to the height, and there are $(n-1)$ such rectangles.

The tangencies of $B_1$ and $D$ and of $B_2$ and $A$ (or $D$ if $n$ is odd) also contribute rectangles of dimension $1$ by $1$ to the knot strand. Finally, the tangency of $A$ to $D$ gives a rectangle with dimensions $1$ by $(n-1)$, contributing $(n-1)$ to the height. Thus the total height of the cusp is $$(2n-4) + (n-1) + 2 + (n-1) = 4n -4.$$

(When $n=2$ this argument needs to be modified slightly: there are no $C_i$'s, but $B_1$ and $B_2$ are tangent. Tangencies of $A$ and $B_2$, $D$ and $B_1$, and $A$ and $D$ also contribute to the height. These all give $1$ by $1$ rectangles, hence the height is $4 = 4n-4$ in this case as well.)

A meridian runs along the widths of two rectangles in the cusp tiling. Hence it has length $2$. Thus the normalized height $h(X)$ is given by: $$h(X) = \frac{4n-4}{\sqrt{(4n-4)(2)}} = \sqrt{2(n-1)}.$$

This information will show:

::: prop
Let $K$ be a 2--bridge knot in $S^3$ which admits a prime, twist reduced diagram with $n\geq 2$ twist regions and at least $c\geq 24$ crossings in each twist region. In a hyperbolic structure on $S^3-K$, normalized such that the meridian has length $1$, the height of the cusp of $S^3-K$ satisfies: $$\left(\sqrt{2(n-1)} - \sqrt{n}(0.18456)\right)^2 \leq H \leq
    \left(\sqrt{2(n-1)} + \sqrt{n}(0.18456)\right)^2.$$ []{#prop:2bridge label="prop:2bridge"}
:::

::: proof
*Proof.* Let $L$ be the augmented link corresponding to $K$. Provided we have at least $n\geq 2$ twist regions, Theorem [\[thm:Lhyp\]](#thm:Lhyp){reference-type="ref" reference="thm:Lhyp"} implies $S^3-L$ is hyperbolic. We have seen in the above discussion that, provided we have at least $c\geq 24$ crossings in each twist region, the slope on each crossing circle of $L$ on which we perform Dehn filling has normalized length at least $I(1.0)$. This implies that a cone deformation exists from $S^3-L$ to $S^3-K$ for which the tube radius is at least $R_1= 1.0$ throughout. Then Theorem [\[thm:main-norm-height\]](#thm:main-norm-height){reference-type="ref" reference="thm:main-norm-height"} implies the normalized height of the cusp of $S^3-K$ satisfies: $$-\frac{\sqrt{n}(2\pi)^2\sqrt{C(1.0)}}{(1-e^{-2.0})} \leq
 h_{\tau} - \sqrt{2(n-1)} \leq
 \frac{\sqrt{n}(2\pi)^2\sqrt{C(1.0)}}{(1-e^{-2.0})}.$$ Using the formulas for $C(1.0)$ from the proof of Lemma [\[lemma:b_j-bound\]](#lemma:b_j-bound){reference-type="ref" reference="lemma:b_j-bound"}, we find $$\sqrt{2(n-1)} - \sqrt{n}(0.18456) \leq h_{\tau} \leq
 \sqrt{2(n-1)} + \sqrt{n}(0.18456).$$ We obtain the final result by noting if we scale such that the meridian has length $1$, then the height is at least $(h_\tau)^2$. ◻
:::
