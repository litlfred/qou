---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-013-313-cusped-hyperbolic-3-manifolds
section_title: "Cusped hyperbolic 3-manifolds"
section_number: 3.1.3
pages: 18-19
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.986
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
[]{#section:cusped label="section:cusped"}

In this subsection, $M^3$ denotes a finite volume hyperbolic manifold, i.e. a manifold whose ends are cusps.

::: assumption
Assume that $M^3$ has a single cusp.
:::

This is done not only to simplify notation, but because with more cusps some further issues need to be discussed [@MFP14]. Again one has:

::: thm
Let $M^3$ be a closed, orientable, hyperbolic 3-manifold with one cusp. Then any lift to $\mathrm{SL}_2(\mathbb{C})$ of its holonomy representation is acyclic.
:::

This is proved for instance in [@MFP12], it is a particular case of Theorem [\[prop:dimHM\]](#prop:dimHM){reference-type="ref" reference="prop:dimHM"} in Appendix [\[sec:cohomology\]](#sec:cohomology){reference-type="ref" reference="sec:cohomology"}. With more cusps this is may not hold true for all lifts of the holonomy representation, i.e. for all spin structures. It is true provided that for each cusp the trace of the peripheral elements is not identically $+2$ (for some elements it is $-2$). This is always the case if there is a single cusp [@MFP12; @Calegari06].

One may as well define the same torsion as in Definition [\[defn:tor2closed\]](#defn:tor2closed){reference-type="ref" reference="defn:tor2closed"}:

::: definition
[]{#defn:tor2cusped label="defn:tor2cusped"} Let $M^3$ be a compact, oriented, hyperbolic 3-manifold with one cusp, and let $\sigma$ denote a spin structure on $M^3$. The torsion of $(M^3,\sigma)$ is defined as $$\label{eqn:taucusp}
 \tau(M^3,\sigma):=\operatorname{tor}(M^3,  \varrho_\sigma )\in \mathbb{C}^*\, ,$$ where $\varrho_\sigma=\widetilde{\mathrm{hol}}$ is the lift of the holonomy corresponding to $\sigma$.
:::

This torsion has the same properties as in the closed case, Proposition [\[prop:properties\]](#prop:properties){reference-type="ref" reference="prop:properties"}.
