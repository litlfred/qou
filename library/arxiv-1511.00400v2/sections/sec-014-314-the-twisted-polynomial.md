---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-014-314-the-twisted-polynomial
section_title: "The twisted polynomial"
section_number: 3.1.4
pages: 19-19
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.989
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
It is relevant to mention the twisted polynomial for hyperbolic knot exteriors corresponding to a lift of the holonomy $\varrho$ constructed by Dunfield, Friedl, and Jackson in [@DFJ12]. Given a hyperbolic knot ${\mathcal K}\subset S^3$, choose the spin structure on $M^3=S^3-{\mathcal K}$ such that the trace of the meridian is $+2$ (the trace of the longitude is always -2 by [@Calegari06], see also [@MFP12 Corollary 3.10]) and consider the abelianization $\phi\colon\pi_1 
M^3\to \mathbb{Z}$. Dunfield, Friedl, and Jackson study the polynomial $$\Delta_{\mathcal K}(t):=\Delta_{M^3, \varrho\otimes\phi}(t)$$ following the notation of Subsection [\[subsection:polynomial\]](#subsection:polynomial){reference-type="ref" reference="subsection:polynomial"}. By Proposition [\[prop:degree\]](#prop:degree){reference-type="ref" reference="prop:degree"} its degree is $\leq 2 (2 g({\mathcal K})+1)$, where $g({\mathcal K})$ is the genus of the knot, i.e. the minimal genus of a Seifert surface. Numerical evidence (knots up to 15 crossings) yield them to conjecture:

::: conj
For a hyperbolic knot $\mathcal K$:

(a) $\deg \Delta_{\mathcal K}(t) = 2 (2 g({\mathcal K})+1)$.

(b) $\Delta_{\mathcal K}$ is monic if and only if ${\mathcal K}$ is s fibered knot.
:::

The equality of the degree has been proved by Morifuji and Tan for some families of two bridge knots, see [@Morifuji15] and references therein. Agol and Dunfield have shown:

::: thm
For libroid hyperbolic knots, $$\deg  \Delta_{\mathcal K}(t) = 2 (2 g({\mathcal K})+1).$$
:::

Being libroid means the existence of a collection of disjointly embedded minimal genus Seifert surfaces in the exterior of the knot so that their open complement is a union of books of $I$-bundles, in a way that respects the structure of sutured manifold. See [@AD15].

In the remarkable paper [@DFJ12] the authors also conjecture that being monic determines whether the knot is fibered or not, and rise many interesting questions about this polynomial and its relationship with other invariants.
