---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-015-48-invariance-of-index-under-isotopy-of-peripher
section_title: "Invariance of index under isotopy of peripheral curve"
section_number: 4.8
pages: 26-29
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.946
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
::: thm
[]{#index_isotopy_invariance label="index_isotopy_invariance"} Let $\varpi$ be an oriented simple closed curve $\varpi$ in $\partial M$ which is a normal curve relative to the triangulation $\mathcal{T}_\partial$ of $\partial M$. Then the index $I_\mathcal{T}(\varpi)$ is invariant under isotopy of the curve $\varpi$ in $\partial M$.
:::

::: proof
*Proof.* Suppose we have two isotopic oriented normal curves $\varpi_1, \varpi_2$. Then we can convert one into the other via a sequence of moves (and their inverses) of the form shown in Figure [1](#isotopy moves){reference-type="ref" reference="isotopy moves"}. That is, we choose a point $p$ on the curve $\varpi$ and an arc $\alpha$, disjoint from $\varpi$ other than at $p$, and which joins $p$ to either a vertex or a point in the interior of an edge of $\mathcal{T}_\partial$. We then push the curve along and in a regular neighbourhood of $\alpha$ over the vertex or edge.

![The two kinds of isotopy move on a curve relative to the triangulation of $\partial M$.](draws_eps/isotopy_moves){#isotopy moves width="40%"}

We will show that $I_\mathcal{T}(\varpi)$ is invariant under these moves. Note that the result of these isotopies will not in general be normal curves, so we need to extend the definition of the index to deal with these cases as well. The class of curves we work in consists of oriented simple closed curves, transverse to $\mathcal{T}_\partial^{(1)}$ and disjoint from $\mathcal{T}_\partial^{(0)}$. For our purposes we will deal only with curves that are non trivial in $H_1(\partial M)$, and so none of our curves is disjoint from $\mathcal{T}_\partial^{(1)}$. Given such a curve, it enters a triangle somewhere on one edge, and can exit out either of the two other edges, or the same edge that it entered, either to the left or the right of its entry point. Thus there are four ways in which a component of a curve intersects a given triangle. These contribute to the index in the following way. See Figure [2](#4_types_of_curve_in_triangle2){reference-type="ref" reference="4_types_of_curve_in_triangle2"}.

<figure id="4_types_of_curve_in_triangle2">
<p><span class="math inline">+</span> at 25 15 <span class="math inline">−</span> at 200 15 <span class="math inline">⊕</span> at 274 10 <span class="math inline">⊖</span> at 431 10 <img src="draws_eps/4_types_of_curve_in_triangle2" style="width:80.0%" alt="image" /></p>
<figcaption>The four ways in which a curve can travel through a triangle. We call the last two possibilities a <em>positive backtrack</em> and <em>negative backtrack</em> respectively.</figcaption>
</figure>

If the curve turns either left or right around a corner of the triangle then it contributes to the index in exactly the same way as for a normal curve: we add $+1$ to the entry in the vector $(\bar{a}_\varpi | \bar{b}_\varpi | \bar{c}_\varpi)$ corresponding to the angle at the edge of the tetrahedron we are turning around if we are going anticlockwise around the corner, and add $-1$ if we are going clockwise. Compare with Figure [\[truncated_tetra2\]](#truncated_tetra2){reference-type="ref" reference="truncated_tetra2"}.

Here we define the effect of backtracks on the index calculation: (This is, of course, chosen in such a way as to be consistent with the index calculated with curves without backtracks.) We do not change the vector $(\bar{a}_\varpi | \bar{b}_\varpi | \bar{c}_\varpi)$. These backtracks only alter the power of $(-q^{1/2})$, either multiplying the expression by $(-q^{1/2})$ for a positive backtrack (turning to the left), or by $(-q^{1/2})^{-1}$ for a negative backtrack (turning to the right). We indicate these using the symbols $\oplus$ and $\ominus$.

Note that by ([\[eq.JD_add_tet_sol\]](#eq.JD_add_tet_sol){reference-type="ref" reference="eq.JD_add_tet_sol"}), a positive backtrack has the same effect on the index as anticlockwise turns around each of the three corners of a triangle. Note also that by ([\[JD_index_eq\]](#JD_index_eq){reference-type="ref" reference="JD_index_eq"}), an anticlockwise loop around a vertex of the triangulation produces a power of $(-q^{1/2})^{2}$. This follows since adding an anticlockwise loop around an end of the $i$th edge has the effect of shifting the sum by one in the $k_i$ component. The terms are unchanged after shifting other than the term $q^{\sum_i k_i}$, and the effect is to multiply the index by $q$.

Thus an anticlockwise loop around a vertex is cancelled by two negative backtracks, and anticlockwise turns around each of the three corners of a triangle are cancelled by one negative backtrack.

<figure id="index_changes_under_isotopies">
<p><span class="math inline">+</span> at 37 396 <span class="math inline">+</span> at 37 376 <span class="math inline">+</span> at 68 396 <span class="math inline">+</span> at 68 376 <span class="math inline">+</span> at 52.5 404 <span class="math inline">+</span> at 52.5 368 <span class="math inline">⊖</span> at 37 340 <span class="math inline">⊖</span> at 68 340</p>
<p><span class="math inline">+</span> at 165.1 396 <span class="math inline">+</span> at 165.1 376 <span class="math inline">+</span> at 196.1 396 <span class="math inline">+</span> at 196.1 376 <span class="math inline">+</span> at 180.6 404 <span class="math inline">⊖</span> at 196.1 340 <span class="math inline">−</span> at 145.1 305 <span class="math inline">−</span> at 216.1 305</p>
<p><span class="math inline">+</span> at 293.3 396 <span class="math inline">+</span> at 293.3 376 <span class="math inline">+</span> at 324.3 396 <span class="math inline">+</span> at 324.3 376 <span class="math inline">+</span> at 308.8 404 <span class="math inline">+</span> at 308.8 368 <span class="math inline">⊖</span> at 324.3 340 <span class="math inline">⊖</span> at 324.3 316.5</p>
<p><span class="math inline">+</span> at 421.5 396 <span class="math inline">+</span> at 421.5 376 <span class="math inline">+</span> at 452.5 396 <span class="math inline">+</span> at 452.5 376 <span class="math inline">+</span> at 437 404 <span class="math inline">⊖</span> at 437 310 <span class="math inline">−</span> at 401.7 305 <span class="math inline">−</span> at 472.7 305</p>
<p><span class="math inline">+</span> at 116.75 252 <span class="math inline">+</span> at 81.75 192 <span class="math inline">+</span> at 151.75 192 <span class="math inline">⊖</span> at 116.5 174.5</p>
<p><span class="math inline">⊕</span> at 229.6 199.5 <span class="math inline">⊖</span> at 244.6 174.5</p>
<p><span class="math inline">⊖</span> at 386.8 199.5 <span class="math inline">⊕</span> at 372.8 174.5</p>
<p><span class="math inline">⊖</span> at 116.5 75 <span class="math inline">⊕</span> at 116.5 30</p>
<p><span class="math inline">⊖</span> at 244.6 44 <span class="math inline">⊖</span> at 244.6 30 <span class="math inline">⊕</span> at 230.6 55 <span class="math inline">⊕</span> at 258.6 55</p>
<p><span class="math inline">⊖</span> at 386.8 55 <span class="math inline">⊕</span> at 372.8 30</p>
<img src="draws_eps/index_changes_under_isotopies" />
<figcaption>Four cases of isotopy across a vertex and six cases of isotopy across an edge. All other cases are symmetries of these.</figcaption>
</figure>

Now all we need to do is to show that each version of the moves from Figure [1](#isotopy moves){reference-type="ref" reference="isotopy moves"} preserves the index, using the above rules. There are different versions of the isotopy moves depending on where the curve we are acting on enters or exits the triangle. We show the possibilities in Figure [3](#index_changes_under_isotopies){reference-type="ref" reference="index_changes_under_isotopies"}. Here the $+,-,\oplus$ and $\ominus$ signs show the *difference* in the index calculation under the isotopy as we change from one curve to the other in the direction following the double head arrow. Note that reversing the arrow on the curve flips all of the signs, as does reflecting the picture. With combinations of these symmetries applied to the ten cases shown we obtain all possible ways in which the isotopy can be made relative to the position of the curve. Considering each case in turn, we can see that the signs cancel out and so the index is unchanged by these moves.

For example, consider the second diagram in the top row of Figure [3](#index_changes_under_isotopies){reference-type="ref" reference="index_changes_under_isotopies"}. We start with a curve that enters the right side of the triangle and exits the bottom. We isotope this curve by pushing it over the top vertex of the triangle. This has the following effects:

-   Remove an anticlockwise turn around the lower right corner of the triangle, this changes the coefficient at that angle by $-1$.

-   Add a negative backtrack to the right edge of the triangle.

-   Add an anticlockwise turn around each of the angles at the top vertex of the triangle other than the top corner of the triangle itself.

-   Add a clockwise turn around the lower left corner of the triangle.

We view the top corner of the triangle as having both a $+$ and a $-$, so that the total change in the index calculation consists of one anticlockwise turn around a vertex, one negative backtrack and clockwise turns around each of the three corners of the triangle. By our above rules, these cancel out and so the index is unchanged. ◻
:::

::: rmk
These calculations are exactly analogous to those for calculating the holonomy of a peripheral curve given shapes of ideal hyperbolic tetrahedra satisfying Thurston's gluing equations. Thus this argument can easily be adapted to reprove the well-known fact that the holonomy is independent of the choice of simple closed curve representing an element of $H_1(\partial M;\mathbb{Z}).$
:::
