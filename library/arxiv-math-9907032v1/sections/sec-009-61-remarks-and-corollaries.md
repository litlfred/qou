---
doc_id: arxiv-math-9907032v1
doc_title: "Combinatorial optimization in geometry"
section_id: sec-009-61-remarks-and-corollaries
section_title: "Remarks and Corollaries"
section_number: 6.1
pages: 19-20
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.989
doc_brief: "Combinatorial optimization in geometry (Rivin) — extends and unifies results on ideal polyhedra in H³ to singular Euclidean structures on surfaces, possibly with infinitely many singularities."
---
Let us assume that the complex $T$ has no boundary, and that the function $\Delta$ is such that all of the cone angles (computed using Lemma [\[cona\]](#cona){reference-type="ref" reference="cona"}) are equal to $2\pi$, so that any realization is Euclidean (and hence can be developed into the plane). Then, we can combine theorems [\[infmain\]](#infmain){reference-type="ref" reference="infmain"} and [\[andreevthm\]](#andreevthm){reference-type="ref" reference="andreevthm"} to get

::: corollary
[]{#infandreev label="infandreev"} Let $T$ be an infinite locally finite triangulation, and let $\Delta:
E(T) \rightarrow (0, \pi]$ be an assignment of dihedral angles to the edges of $T$, let Then there exists a flat surface $S$, and a collection of points $p_1, \ldots, p_n, \ldots$ in $S$ whose Delaunay triangulation is combinatorially equivalent to $T$ and which has dihedral angles given by $\Delta$ if and only if:

-   []{#sumvv1 label="sumvv1"} If $v$ is an interior vertex of $T$, then $$\sum_{\mbox{$e \in E(T)$ incident to $v$}} (\pi - \Delta(e)) = 2\pi.$$

-   []{#sumintcyc1 label="sumintcyc1"} If $\mathcal{E}$ is a non-coterminous minimal cutset, then $$\sum_{e \in \mathcal{E}} (\pi - \Delta(e)) > 2\pi.$$
:::

The above Corollary can be viewed as an extension of Theorem 0.1 of [@steiner] to the case of ideal polyhedra with infinitely vertices (and hence also of Andre'ev's theorem for ideal polyhedra [@Andr70b]), but not without certain caveats: even when $T$ is topologically a disk, it is not at all obvious whether the metric on the surface $S$ (or, even, *any* surface $S$) is geodesically complete. If it is complete, it follows that $S$ is the Euclidean plane, and that the developing map is a global isometry, but otherwise the developing map is, only an immersion. Checking if the given simply-connected Euclidean surface $S$ is the Euclidean plane is nothing other than the *type problem* -- that is, we want to know whether a Riemann surface is parabolic, hyperbolic, or elliptic. If we know the shapes of all the triangles, this can be shown to be equivalent to the recurrence of a random walk on the $1$-skeleton of the complex $T$, where an edge $AB$, incident to triangles $ABC$ and $ABD$ has weight $1/(\cot C +
\cot D)$ ([@irivp]). Using this, it can be shown without too much difficulty that in the case where all of the dihedral angles are rational multiples of $\pi$, bounded away from $0$ and $\pi$, then this is equivalent to the recurrence of the symmetric random walk on the $1$-skeleton of $T$.

In the special case of all dihedral angles being equal to $\pi$ or $\pi/2$, corollary [\[infandreev\]](#infandreev){reference-type="ref" reference="infandreev"} reduces to an existence theorem for infinite locally finite circle packings. In this case, the type problem, and a number of others, has been studied at great length by a number of authors, starting with Koebe, but more recently by A. Marden (in the context of Schottky groups), W. Thurston, B. Rodin and D. Sullivan, Z.-X. He, O. Schramm, and others.

It should be noted the Theorem [\[infmain\]](#infmain){reference-type="ref" reference="infmain"} says nothing about uniqueness, and the proof certainly does not show any form of uniqueness. In view of Theorem [\[uniqueness\]](#uniqueness){reference-type="ref" reference="uniqueness"} one might suspect that perhaps this could be shown with more work. In fact, it is quite clear from the above-mentioned work on circle packing that uniqueness fails, though in a controlled manner described in the conjecture below:

::: conjecture
Let $T$ be a infinite locally finite complex, $\Delta$ a system of dihedral angles satisfying the hypotheses of Theorem [\[infmain\]](#infmain){reference-type="ref" reference="infmain"}. If there is a realization of $T$ supported on a simply-connected domain $\Omega_0 \subset \mathbf{C}$, then there is one supported on *every* simply-connected domain $\Omega \subset \mathbf{C}$. Furthermore, such a realization is determined uniquely by $\Omega$ (up to the group of Möbius transformations fixing $\Omega$).
:::
