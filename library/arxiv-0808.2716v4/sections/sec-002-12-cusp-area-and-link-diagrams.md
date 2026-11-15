---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF FAREY MANIFOLDS"
section_id: sec-002-12-cusp-area-and-link-diagrams
section_title: "Cusp area and link diagrams"
section_number: 1.2
pages: 3-4
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.981
doc_brief: "CUSP AREAS OF FAREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on the cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2–bridge link complements."
---
[]{#sec:diagram-intro label="sec:diagram-intro"}

A closely related class of manifolds are complements of 2--bridge links. Using similar techniques, in this paper we are also able to bound the lengths of slopes on maximal cusps in hyperbolic 2--bridge links. Since all 2--bridge links can be represented by an alternating diagram, our results give further evidence for a conjectural picture of the cusp shapes and maximal cusp metrics of alternating knots.

For general alternating knots and links, there is increasing evidence that the cusp shape and maximal cusp metric ought to be bounded in terms of the twist number of a reduced diagram. We say that a link diagram is *reduced* if it does not contain any crossings that separate the diagram: that is, any crossings in the projection plane such that there is a simple closed curve meeting the diagram transversely in only that crossing. Similarly, two crossings are said to be equivalent if there exists a simple closed curve meeting the knot diagram transversely in those two crossings, disjoint from the knot diagram elsewhere. The *twist number* is the number of equivalence classes of crossings (called *twist regions*).

::: conjecture
The area of a maximal cusp metric on an alternating knot is bounded above and below by linear functions of the twist number of a reduced, alternating diagram. Similarly, the length of the shortest non-meridional slope of an alternating knot is bounded above and below by a linear function of the twist number of the diagram. []{#conj:alt-knot-cusp label="conj:alt-knot-cusp"}
:::

We first became aware of this conjecture several years ago by viewing slides of a talk by Thistlethwaite, in which he showed using SnapPea that the conjecture holds for many simple alternating knots. Lackenby proved a close variant the conjecture, relating the twist number of a diagram to the *combinatorial length* of slopes [@lackenby:word]. However, Lackenby's methods are purely combinatorial and cannot be applied to give the geometric information of the conjecture.

In this paper we prove the conjecture for 2--bridge link complements. In particular, we show the following.

::: named
Theorem [\[thm:2bridge\]](#thm:2bridge){reference-type="ref" reference="thm:2bridge"} Let $K$ be a 2--bridge link in $S^3$, whose reduced alternating diagram has twist number $t$. Let $C$ be a maximal neighborhood about the cusps of $S^3 {\smallsetminus}
K$, in which the two cusps have equal volume if $K$ has two components. Then $$\frac{8\sqrt{3}}{147}\,(t-1) \: \leq \: {\rm area}({\partial}C) \:
<\: 2\sqrt{3}\,\, \frac{v_8}{v_3}\,(t-1).$$ Furthermore, if $K$ is a knot, let $\gamma$ be any non-trivial arc that starts on a meridian and comes back to the same meridian (for example, a non-meridional simple closed curve). Then its length satisfies $$\ell(\gamma) \: \geq \: \frac{4\sqrt{6\sqrt{2}}}{147}\, (t-1).$$
:::

This result should be compared to that of Adams *et al.* [@adams-students:cusp-area], where they prove upper bounds on cusp area in terms of the crossing number $c$ of a knot. For alternating knots, including 2--bridge knots, they show that the cusp area satisfies ${\rm area}({\partial}C) \leq 9c - 36 + 36/c$. For those 2--bridge knots whose diagrams have very few crossings per twist region (in particular, when $c/t < 1.39$), the bound of Adams *et al.* is sharper than the upper bound of Theorem [\[thm:2bridge\]](#thm:2bridge){reference-type="ref" reference="thm:2bridge"}. For more general 2--bridge knots that have more crossings per twist region, the upper bound of Theorem [\[thm:2bridge\]](#thm:2bridge){reference-type="ref" reference="thm:2bridge"} is a significant improvement. To the best of our knowledge, the lower bound of Theorem [\[thm:2bridge\]](#thm:2bridge){reference-type="ref" reference="thm:2bridge"} does not have any predecessors in the literature.
