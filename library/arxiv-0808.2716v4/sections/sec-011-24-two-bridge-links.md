---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF FAREY MANIFOLDS"
section_id: sec-011-24-two-bridge-links
section_title: "Two-bridge links"
section_number: 2.4
pages: 11-12
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.98
doc_brief: "CUSP AREAS OF FAREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on the cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2–bridge link complements."
---
[]{#sec:2bridge label="sec:2bridge"}

If a $4$--punctured sphere bundle $N$ is cut along a pleated fiber $S$, the result is a manifold homeomorphic to $S \times I$, equipped with an ideal triangulation. To recover $N$, we reglue the top of this *product region* $S \times I$ to the bottom along faces of this triangulation. Meanwhile, the complement of a two-bridge link $K$ also contains a product region $S \times I$: namely, the complement of the $4$--string braid that runs between the minima and maxima in a diagram of $K$. It turns out that the combinatorics of this braid once again defines a layered triangulation of the product region, and that a particular folding of the top and bottom faces of $S \times I$ yields the canonical triangulation of $S^3 {\smallsetminus}K$.

A 4--punctured sphere $S$ can be viewed as a square pillowcase with its corners removed. Consider two such nested pillowcases, with an alternating $4$--string braid running between them, as in Figure [1](#fig:pillow-braid){reference-type="ref" reference="fig:pillow-braid"}(a). The combinatorics of this braid, as well as of the complementary product region $S \times I$, may be described by a (finite) monodromy word of the form $\Omega = R^{p_1}L^{q_1}\dots
R^{p_s}L^{q_s}$, as above, where the $p_i$, $q_i$ are all positive, except $p_1$ and $q_s$ are non-negative. Each syllable $R^{p_i}$ or $L^{q_i}$ determines a string of crossings in a vertical or horizontal band, corresponding to a *twist region* in which two strands of the braid wrap around each other $p_i$ times. To complete this picture to a link diagram, we connect two pairs of punctures of the outside pillowcase together with a crossing, and connect two pairs of punctures of the inside pillowcase together with a crossing, as in Figure [1](#fig:pillow-braid){reference-type="ref" reference="fig:pillow-braid"}(b). This creates an alternating diagram of a 2--bridge link $K(\Omega)$. It is well--known that any 2--bridge link can be created in this manner (see, for example, Murasugi [@murasugi Theorems 9.3.1 and 9.3.2]).

<figure id="fig:pillow-braid">
<div class="center">
<embed src="figures/Fig_pillow-braid.eps" />
</div>
<figcaption>(a) An alternating braid between two pillowcases, described by the word <span class="math inline"><em>Ω</em> = <em>R</em><sup>3</sup><em>L</em><sup>2</sup><em>R</em></span>. (b) The corresponding two-bridge link <span class="math inline"><em>K</em>(<em>Ω</em>)</span>.</figcaption>
</figure>

Just as in Sections [\[sec:ptorus\]](#sec:ptorus){reference-type="ref" reference="sec:ptorus"} and [\[sec:4ps\]](#sec:4ps){reference-type="ref" reference="sec:4ps"} above, the monodromy word $\Omega$ describes a layered ideal triangulation of the product region $S \times I$. To form a 4--punctured sphere bundle, one would glue the outer pillowcase $S_1$ to the inner pillowcase $S_c$. To obtain a 2--bridge link complement, we fold the surface $S_1$ onto itself, identifying its four ideal triangles in pairs. (See [@gf:two-bridge Figure 17].) We perform the same folding for the interior pillowcase $S_{c}$. This gives the desired canonical triangulation of $S^3 {\smallsetminus}K(\Omega)$.

Now consider the combinatorics of the cusp triangulation. The pleated surfaces between $S_1$ and $S_c$ are 4--punctured spheres with combinatorics identical to that of the 4--punctured sphere bundle with the same monodromy. The universal cover of the product region looks like a stack of zigzags, as in Figure [\[fig:stack\]](#fig:stack){reference-type="ref" reference="fig:stack"}. (Just as with $4$--punctured sphere bundles, a meridian of $K$ crosses three edges of a zigzag -- so Figure [\[fig:stack\]](#fig:stack){reference-type="ref" reference="fig:stack"} shows two meridians.) The folding along $S_1$ and $S_c$ creates "hairpin turns", as in [@gf:two-bridge Figure 19].

Note that when $K$ is a two-component link, we shall always choose the two cusp neighborhoods of $K$ to have equal volume, following the same principle as in Section [\[sec:4ps\]](#sec:4ps){reference-type="ref" reference="sec:4ps"}. This *equivariant cusp* neighborhood is the one whose Ford domain is dual to the layered triangulation described above. Also, because the symmetry group of $K$ interchanges the two cusps, it does not matter which cusp we look at in the calculations of Section [\[sec:horosphere\]](#sec:horosphere){reference-type="ref" reference="sec:horosphere"}.

Finally, it is worth remarking that every surface $S_i$, lying between two layers of tetrahedra, is a bridge sphere for the link $K$, and is thus compressible in $S^3 {\smallsetminus}K$. Despite being compressible, $S_i$ can nevertheless be realized as a pleated surface in the geometry of $S^3 {\smallsetminus}K$. With the exception of the folded surfaces $S_1$ and $S_c$, every other pleated $S_i$ is embedded, and carries the same geometric information as the incompressible fiber in a $4$--punctured sphere bundle.
