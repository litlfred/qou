---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.913
---
The Ptolemy variety $P_n(\mathcal T)$ of a topological ideal triangulation $\mathcal T$ of a compact $3$-manifold $M$ was defined by Garoufalidis, Thurston and Zickert [@GaroufalidisThurstonZickert]. It gives coordinates (called Ptolemy coordinates) for boundary-unipotent $\mathop{\mathrm{SL}}(n,\mathbb C)$-representations of $\pi_1(M)$ in the sense that each point in $P_n(\mathcal T)$ determines a representation (up to conjugation). The Ptolemy variety is explicitly computable for many census manifolds when $n=2$ or $3$ (see [@CURVE; @FalbelKoseleffRouillier] for a database), and invariants such as volume and Chern-Simons invariant can be explicitly computed from the Ptolemy coordinates. The Ptolemy variety, however, depends on the triangulation and may miss several components of representations.

We focus exclusively on the case when $n=2$, so we omit the subscript $n$ on the Ptolemy variety. Our goal is to define a refined Ptolemy variety $\overline P(\mathcal T)$, which is a topological invariant of $M$ and is guaranteed to detect all irreducible boundary-unipotent $\mathop{\mathrm{SL}}(2,\mathbb C)$-representations. We also define refined variants of the Ptolemy variety for $\mathop{\mathrm{PSL}}(2,\mathbb C)$-representations [@GaroufalidisThurstonZickert; @PtolemyField], and for the enhanced Ptolemy variety [@ZickertEnhancedPtolemy] for $\mathop{\mathrm{SL}}(2,\mathbb C)$-representations that are not necessarily boundary-unipotent. The refined variant of the latter detects all irreducible $\mathop{\mathrm{SL}}(2,\mathbb C)$-representations.

A representation in $\mathop{\mathrm{SL}}(2,\mathbb C)$ or $\mathop{\mathrm{PSL}}(2,\mathbb C)$ is *boundary-unipotent*, respectively *boundary-Borel*, if it takes each peripheral subgroup to a conjugate of the subgroup $P$, respectively $B$, where $B$ is the group of upper triangular matrices, and $P\subset B$ is the subgroup of matrices with $1$ on the diagonal.

## Motivation: Thurston's gluing equations

In his famous notes Thurston [@ThurstonNotes] wrote down a system of polynomial equations (called *gluing equations*) for a compact 3-manifold $M$ with a topological ideal triangulation. The system consists of a variable (called a *shape*) $z_i$ for each simplex, and an equation for each edge. The set of solutions with $z_i\in\mathbb CP^1\setminus\{0,1,\infty\}$ is called the *gluing equation variety*, and each point in this variety determines (up to conjugation) a $\mathop{\mathrm{PSL}}(2,\mathbb C)$-representation of $\pi_1(M)$. Solutions with some $z_i$ being 0, 1 or $\infty$ are called *degenerate*, and may not give rise to a unique representation, or to any representation at all. The gluing equation variety and the set of representations detected depend on the triangulation and may be empty.

In [@Segerman] Segerman considers a generalization of Thurston's gluing equation variety, where the shapes $z_i$ are replaced by variables in the field $\mathbb C((\zeta))$ of Laurent series in a variable $\zeta$. He proves the existence of a triangulation such that his generalized variety detects all irreducible representations except those that have image in a generalized dihedral group. His approach uses normal surfaces and it does not yield explicit defining equations for the generalized variety. Our approach focuses on Ptolemy coordinates and is completely combinatorial, and detects all irreducible representations, even those with image in a generalized dihedral group. It is possible that our methods could also be used to make Segerman's generalized variety more explicit, but we shall not pursue this idea here. Our paper does not require prior knowledge of Thurston's gluing equations or Segerman's work.
