---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF FAREY MANIFOLDS"
section_id: sec-010-23-4punctured-sphere-bundles
section_title: "4–punctured sphere bundles"
section_number: 2.3
pages: 10-11
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.947
doc_brief: "CUSP AREAS OF FAREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on the cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2–bridge link complements."
---
[]{#sec:4ps label="sec:4ps"}

Consider the universal abelian cover $X := {\mathbb{R}}^2 {\smallsetminus}{\mathbb{Z}}^2$ of the punctured torus, and define the following transformations of $X$: $$\alpha(x,y) = (x+1, y), \quad \beta(x,y) = (x,y+1), \quad
\sigma(x,y) = (-x,-y).$$

Then one obtains the punctured torus as $T = X/\langle\alpha, \beta
\rangle$ and the $4$--punctured sphere as $S = X/\langle\alpha^2,
\beta^2, \sigma \rangle$. Both $S$ and $T$ are covered by the 4--punctured torus $R = X/\langle\alpha^2, \beta^2 \rangle$. Then the action of $SL_2({\mathbb{Z}})$ on $T$ lifts to an action on $X$, and descends to an action on both $R$ and $S$. As a result, every hyperbolic punctured torus bundle $M$ is commensurable with a hyperbolic 4--punctured sphere bundle $N$, whose monodromy can be described by the same word $\Omega$. The common cover is a 4--punctured torus bundle $P$. In Figure [\[fig:tetrahedra\]](#fig:tetrahedra){reference-type="ref" reference="fig:tetrahedra"}, we see lifts of two pleated surfaces to the common cover.

The $4$--punctured sphere bundle $N$ can have anywhere from one to four cusps, depending on the action of its monodromy on the punctures of $S$. Thus, for the purpose of discussing Ford domains, it is important to choose the right horoball neighborhood of the cusps. Unless stated otherwise (e.g. in Theorem [\[thm:4ps-area\]](#thm:4ps-area){reference-type="ref" reference="thm:4ps-area"}), we shall always choose the cusp neighborhood in $N$ that comes from lifting a maximal cusp of the corresponding punctured torus bundle $M$ to the 4--punctured torus bundle $P$, and then projecting down to $N$. We call this the *equivariant* cusp neighborhood of a $4$--punctured sphere bundle.

By lifting the canonical monodromy triangulation of $M$ to $P$, and projecting down to $N$, we obtain the layered monodromy triangulation of a $4$--punctured sphere bundle. Every tetrahedron $\Delta(e)$ of this triangulation lifts to a layer of four tetrahedra in $P$, and projects down to a layer of two tetrahedra in $N$. (See [@gf:two-bridge Figure 16].) This triangulation is still geometrically canonical: it is dual to the Ford domain determined by the the equivariant cusp neighborhood. We refer to this Ford domain as an *equivariant* Ford domain. In particular, it still makes sense to talk about "syllables", "zigzags", etc. in relation to 4--punctured sphere bundles. Note that because of the rotational action of $\sigma$, a loop around a puncture of the fiber will only cross three edges in zigzag of $N$, instead of six edges as in a zigzag of the punctured torus bundle $M$.

::: define
[]{#def:fibered-meridian label="def:fibered-meridian"} In a punctured torus bundle $M$ or a $4$--punctured sphere bundle $N$, call the loop about a puncture of the fiber the *meridian* of the corresponding manifold. We shall denote the length of a meridian in a maximal cusp of a punctured torus bundle $M$ by $2\mu$. With this convention, the meridian of the corresponding $4$--punctured sphere bundle $N$ will have length $\mu$ in a maximal equivariant cusp.
:::

In the discussion of the geometry below, we will switch between descriptions of 4--punctured sphere bundles and punctured tori, depending on which leads to the simplest discussion. Because of the covering property, results on the geometry of the universal cover will apply immediately to both types of manifolds.
