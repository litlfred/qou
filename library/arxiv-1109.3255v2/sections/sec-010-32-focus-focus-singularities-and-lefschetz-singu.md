---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE"
section_id: sec-010-32-focus-focus-singularities-and-lefschetz-singu
section_title: "Focus-focus singularities and Lefschetz singularities"
section_number: 3.2
pages: 22-25
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
toc_source: outline
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 0.986
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
[]{#sec:focus-focus-lefschetz label="sec:focus-focus-lefschetz"}

Now we consider the case where the affine structure on $B$ contains a focus-focus singularity, that is, a singularity with monodromy conjugate to $\begin{pmatrix}1& 0\\ 1 &1\end{pmatrix}$, and the monodromy invariant direction of this singularity is parallel to the fibers of the map $\eta: B \to I$. The goal is to construct a symplectic manifold $X(B)$, along with a Lefschetz fibration $w: X(B) \to X(I)$. Topologically $X(B)$ is a torus fibration over $B$ with a single pinched torus fiber over the singular point.

Let $B$ be an affine manifold with a single focus-focus singularity, and $\eta: B \to I$ a globally defined affine coordinate. Suppose $B$ has vertical boundary consisting of fibers of $\eta$, as before, and suppose that the horizontal boundary consists of line segments of rational slope. If we draw the singular affine structure with a branch cut, one side will appear straight while the other appears bent, though the bending is compensated by the monodromy of the focus-focus singularity. Figure [1](#fig:tropical-fibration){reference-type="ref" reference="fig:tropical-fibration"} shows the projection $B \to I$, with the fibers drawn as vertical lines.

![The fibration $B \to I$.](tropical-fibration){#fig:tropical-fibration width="3in"}

::: proposition
[]{#prop:focus-focus-lefschetz label="prop:focus-focus-lefschetz"} The manifold $X(B)$ admits an exact symplectic structure making $w : X(B)\to X(I)$ a symplectic Lefschetz fibration, with a single Lefschetz critical point. This critical point coincides with focus-focus singularity of the torus fibration $\pi : X(B)\to B$. There is a neighborhood $U \subset B$ of the fiber of $\eta$ through the singularity such that on the complement of $\pi^{-1}(U)$, the symplectic form is locally given by a Hessian metric of the form considered in Lemma [\[lem:monodromy-hessian\]](#lem:monodromy-hessian){reference-type="ref" reference="lem:monodromy-hessian"}.
:::

::: proof
*Proof.* Suppose for convenience that the singularity occurs at $\eta =
0$. For the first step, divide the base $B$ into regions $B_{-\epsilon}=
\eta^{-1}(-\infty,-\epsilon]$ and $B_{+\epsilon} =
\eta^{-1}[\epsilon,\infty)$. On these affine manifolds we may take the Hessian metrics and associated Kähler forms considered in Lemma [\[lem:monodromy-hessian\]](#lem:monodromy-hessian){reference-type="ref" reference="lem:monodromy-hessian"}, using functions $K_-$ and $K_+$ derived from the example following that Lemma. Hence we get a fibration with symplectic connection over the disjoint union of two annuli: $w: X(B_{-\epsilon}
\coprod B_{+\epsilon}) \to X(I_{-\epsilon} \coprod I_{+\epsilon})$

The second step is extend the Lefschetz fibration over a band connecting the two annuli. Consider the two annuli $X(I_{-\epsilon})\coprod
X(I_{+\epsilon}) \subset \C^*$. Choose a path connecting these two annuli, along the positive real axis, say. By identifying the fibers over the end points, the fibration extends over this path. By thickening the path up to a band and filling in the fibers over the band, we get a Lefschetz fibration over a surface which is topologically a pair of pants. Since the fibration over the band is trivial, the gluing can be done in such a way that the horizontal boundary components of the total space are still foliated by multi-sections of the symplectic connection.

The third step is to fill in the rest of the region between the two annuli with the standard model of a Lefschetz singularity. In order for this to make sense, we need the symplectic monodromy around the loop in the base being filled in to be a Dehn twist. This can be seen by comparing the symplectic monodromy transformations around the loops in $X(I_{-\epsilon})$ and $X(I_{+\epsilon})$. Let $z_{-}$ and $z_{+}$ denote complex coordinates on $X(B_{-\epsilon})$ and $X(B_{+\epsilon})$ corresponding to a direction transverse to the fibration $\eta : B \to I$, so that $z_{-}$ and $z_{+}$ give coordinates on the fibers of $w: X(B)\to X(I)$. Assume these coordinates match up in one of the bands connecting $B_{-\epsilon}$ to $B_{+\epsilon}$. Due to the monodromy of the affine manifold they do not coincide in the other band, where we put the branch cut. Let $F_1$ and $F_0$ denote the top and bottom faces of $\partial^h B$ respectively, and suppose that $F_0$ is split into two parts $F_{0+}$ and $F_{0-}$ by the branch cut. Associated to each of these we have a slope $\sigma_F$.

Now we compute the monodromy obtained when we traverse a loop in $X(I_{-\epsilon})$ in the negative sense followed by a loop in $X(I_{+\epsilon})$ in the positive sense, connecting these paths through the band connecting the two annuli. We use Lemma [\[lem:monodromy-hessian\]](#lem:monodromy-hessian){reference-type="ref" reference="lem:monodromy-hessian"} to measure the difference between the amounts of phase rotation in the $z_{-}$ and $z_{+}$ coordinates along the top and bottom horizontal boundaries under symplectic parallel transport, encoding this as an overall twisting. By Lemma [\[lem:monodromy-hessian\]](#lem:monodromy-hessian){reference-type="ref" reference="lem:monodromy-hessian"}, as we transport around the negative loop in $X(I_{-\epsilon})$, the $z_{-}$ coordinate on $\pi^{-1}(F_1)$ rotates through an angle $-2\pi\sigma_{F_1}$ and the $z_{-}$ coordinate on $\pi^{-1}(F_{0-})$ rotates through an angle $-2\pi\sigma_{F_{0-}}$. Thus the relative twist of the two ends of the fiber is $-(\sigma_{F_1} - \sigma_{F_{0-}})$ turns. By the same token, on the other side the $z_+$ coordinate on $\pi^{-1}(F_1)$ rotates through an angle $2\pi\sigma_{F_1}$, while the $z_+$ coordinate on $\pi^{-1}(F_{0+})$ rotates through $2\pi\sigma_{F_{0+}}$, and the overall relative twisting is $(\sigma_{F_1} -
\sigma_{F_{0+}})$ turns. Composing these monodromy transformations, we find that the fiber undergoes a twisting of $\sigma_{F_{0-}}-\sigma_{F_{0+}}$ turns. Because the monodromy of the affine structure is a shear, this difference of slopes equals $-1$. Thus the fiber undergoes a right-handed Dehn twist (whose local model is obtained by taking the annulus $\{1\leq |z|\leq 2\}$ and rotating the outer boundary by one *clockwise* turn).

This allows us to fill in the fibration with a standard fibration with a single Lefschetz singularity whose vanishing cycle is the equatorial circle on the cylinder fiber. Because the top and bottom boundaries are fixed under the monodromy transformation, the foliation of the horizontal boundary extends over the gluing. Since this local model is symmetric under the $S^1$--action which rotates the fibers, choosing an $S^1$--invariant gluing allows us to define a symplectic $S^1$--action on $X(B)$ which rotates the fibers of $w: X(B)\to X(I)$.

Since the total space is $S^1$--symmetric, we can construct the Lagrangian tori as in section [\[sec:torus-fibrations\]](#sec:torus-fibrations){reference-type="ref" reference="sec:torus-fibrations"}, by taking circles of constant $|w|$ in the base and $S^1$--orbits in the fiber. These actually coincide with the tori found in $X(B_{-\epsilon} \coprod
B_{+\epsilon})$ as fibers of the projection to $B$, so this construction extends the torus fibrations on $X(B_{-\epsilon} \coprod
B_{+\epsilon})$ to all of $X(B)$. ◻
:::

::: remark
Since this construction is local on the base $X(I)$, the construction extends in an obvious way to the situation where several focus-focus singularities with parallel monodromy-invariant directions are present. See Section [\[sec:other-manifolds\]](#sec:other-manifolds){reference-type="ref" reference="sec:other-manifolds"} for further discussion.
:::

::: remark
There is a more direct way to obtain the sort of symplectic structure we desire, based on a version of the mapping-torus construction. Start with a Lefschetz fibration over an rectangle, with a critical value corresponding to the singular point of $B$. Trivialize the fibration over the top and bottom sides of the base rectangle, and glue the top and bottom together, identifying the fibers using a symplectomorphism, yielding a fibration over an annulus that we identify with $X(I)$. Choosing the gluing symplectomorphism appropriately, we can ensure that the monodromies around the sub-annuli $X(I_{\pm \epsilon}) \subset X(I)$ agree with what is obtained from the Hessian metric construction. Our preference for the construction described above is that it proceeds more naturally from the affine geometry of $B$.
:::

::: remark
[]{#rem:cut-corner label="rem:cut-corner"} In the main example of this paper, the affine manifold does not have vertical boundary, but rather corners at the extreme values of $\eta$. To define the symplectic structure, we deal with this by cutting off arbitrarily small pieces of $B$ at the corners so that the result has vertical boundaries. However, in terms of the correspondence to tropical geometry, we still consider the unmodified manifold $B$.
:::

::: definition
Let $B$ be the affine manifold appearing in the mirror of $(\CP^2,D)$. We denote by $X(B)$ be the symplectic manifold obtained from Proposition [\[prop:focus-focus-lefschetz\]](#prop:focus-focus-lefschetz){reference-type="ref" reference="prop:focus-focus-lefschetz"}, after cutting off the corners of $B$ as in Remark [\[rem:cut-corner\]](#rem:cut-corner){reference-type="ref" reference="rem:cut-corner"}.
:::

Recall that the horizontal boundary $\partial^h X(B)$ is the union of two faces $(\partial^h X(B))_1$ and $(\partial^h X(B))_0$ corresponding to $F_1$ and $F_0$, the top and bottom faces of $B$. Likewise we speak of the top and bottom boundary circles of the fibers of $w$. The following proposition summarizes key properties of $X(B)$. It follows from the analysis of the monodromies in the proof of Proposition [\[prop:focus-focus-lefschetz\]](#prop:focus-focus-lefschetz){reference-type="ref" reference="prop:focus-focus-lefschetz"} and Lemma [\[lem:monodromy-hessian\]](#lem:monodromy-hessian){reference-type="ref" reference="lem:monodromy-hessian"}.

::: proposition
[]{#prop:key-properties label="prop:key-properties"} The Lefschetz fibration $w : X(B) \to X(I)$ has the following properties:

1.  The monodromy given by traversing the inner boundary loop *clockwise* fixes the top boundary circle of the fiber, and rotates the bottom boundary circle through a half turn, in such a way that the square of this operation is isotopic to a *right-handed* Dehn twist.

2.  The monodromy given by traversing the outer boundary loop *clockwise* fixes the top boundary circle and acts on the bottom boundary circle by a half-turn, except that the square of this operation is isotopic to a *left-handed* Dehn twist.

3.  As the top face $F_1$ has integral slope (zero in our diagrams), the leaves of the foliation on $(\partial^h
    X(B))_1$ are single-valued sections of the $w$-fibration.

4.  As the bottom face $F_2$ has half-integral slope ($\pm 1/2$ on either side of the cut in our diagrams), the leaves of the foliation on $(\partial^h X(B))_0$ are two-valued sections of the $w$-fibration.
:::

::: remark
[]{#rem:leaves-W label="rem:leaves-W"} The foliation of the boundary faces by horizontal sections is related to the superpotential $W= u +e^{-\Lambda}v^2/(uv-1)$ studied in the previous Section [\[sec:fiber-superpotential\]](#sec:fiber-superpotential){reference-type="ref" reference="sec:fiber-superpotential"}. The general fiber $W = \text{constant}$ is a twice-punctured torus. On the other hand, we can consider the curves defined by the individual terms of $W$. The equation $u = \text{constant}$ defines a curve such that the projection $w = uv-1: X^\vee \to \C$ is one-to-one, so this curve is a section of $w$. The curves defined by the second term $v^2/(uv-1) = \text{constant}$ are likewise two-valued sections of $w: X^\vee \to \C$. Our perspective is that the leaves of the foliations on the boundary components of $X(B)$ correspond roughly to these curves defined by the individual terms of the superpotential.
:::
