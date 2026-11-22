---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-002-12-decorated-representations
section_title: "Decorated representations"
section_number: 1.2
pages: 2-2
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
toc_source: outline
text_source: latex
latex_prose_ratio: 0.863
latex_coverage_ratio: 1.0
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety for SL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
A convenient language for studying both the gluing equation variety and the Ptolemy variety is that of *decorated representations* (see [@ZickertDuke; @GaroufalidisThurstonZickert]). We give a brief overview assuming for simplicity that $M$ has a single torus boundary component (the general case and precise definitions are recalled in Section [\[sec:Decorations\]](#sec:Decorations){reference-type="ref" reference="sec:Decorations"}). Let $G$ be either $\mathop{\mathrm{PSL}}(2,\mathbb C)$ or $\mathop{\mathrm{SL}}(2,\mathbb C)$. A *decoration* of a representation $\rho\colon\pi_1(M)\to G$ may be thought of as a choice of a point in $\mathbb CP^1$ stabilized by $\rho(\pi_1(\partial M))$. In particular, a representation generically has two decorations[^1], but may have only one (if $\rho$ is boundary-unipotent), infinitely many (if $\rho(\pi_1(\partial M))$ is trivial), or none at all (if $\rho$ is not boundary-Borel). Any decorated representation determines shapes satisfying Thurston's gluing equations.

Since $\mathbb CP^1=\mathop{\mathrm{SL}}(2,\mathbb C)\big/B$ we shall sometimes refer to a decoration as a *B-decoration*. If $\rho$ is boundary-unipotent, a (stronger) decoration by points in $\mathop{\mathrm{SL}}(2,\mathbb C)\big/P$ exists which we refer to as a *P-decoration*.

In the language of decorations, Thurston's gluing equation variety parametrizes *generically $B$-decorated* boundary-Borel $\mathop{\mathrm{PSL}}(2,\mathbb C)$-representations, where a decoration is generic if the corresponding solution to Thurston's gluing equations is non-degenerate. Whether or not a representation has a generic decoration depends on the choice of triangulation.

[^1]: As an example, `m004(10,11)` and `m004(-10,-11)` in SnapPy give the same geometric representation but different shapes corresponding to different decorations.
