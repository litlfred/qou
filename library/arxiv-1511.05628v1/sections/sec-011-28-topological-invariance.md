---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-011-28-topological-invariance
section_title: "Topological invariance"
section_number: 2.8
pages: 11-12
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.96
doc_brief: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY — The Quantum Modularity Conjecture of Zagier predicts the existence of a for- mal power series with arithmetically interesting coeﬃcients that"
---
[]{#sub.inv label="sub.inv"}

We conjectured in the introduction that $\phi_{\gamma,\zeta}(\hbar)$ is actually a topological invariant --- depending only on a knot $K$ and the root of unity $\zeta$, rather than on a full Neumann-Zagier datum --- and thus $\phi_{\gamma,\zeta}(\hbar) = \phi_{K,\zeta}(\hbar)$ is the series that appears in the right hand side of the Quantum Modularity Conjecture. We can now make this a bit more precise.

We begin with the following experimental observations:

-   For all 502 hyperbolic knots with at most 8 ideal tetrahedra in the `CensusKnots`, their default `SnapPy` triangulations are $\mathbb Z$-nondegenerate, in the sense that there is a gauge (for a definition, see Section [\[sub.NZ\]](#sub.NZ){reference-type="ref" reference="sub.NZ"}) for which $|\!\det\, \mathbf B|=1$.

-   The default and the canonical `SnapPy` triangulation of the $5_2$ and $6_1$ knots have several gauges for which $|\!\det\, \mathbf B|=1$. For each of the above knot we have checked that $(\tau_{\gamma,k})^{12k}$ is independent of the above gauges, and that $S_{\gamma,2,k}$ is independent up to addition of $\mathbb Z/{24k}$, and that $S_{\gamma,3,k}$ is independent. These are slightly better than the general ambiguities that appear in the nonperturbative level-$k$ state-integral (see Section [\[sec.CCS\]](#sec.CCS){reference-type="ref" reference="sec.CCS"}), which motivated the definitions above. Moreover, (local) triangulation-invariance of the level-$k$ state integral suggests that $S_{\gamma,n,k}$ should be independent of triangulation and $\gamma$ for all $n$.

We are therefore led to conjecture

::: conjecture
[]{#conj.inv label="conj.inv"} For any knot $K$, there exists a triangulation with a non-degenerate Neumann-Zagier datum $\gamma$. The series $\phi_{\gamma,\zeta}(\hbar)$ is independent of the choice of triangulation and $\gamma$, up to multiplication by $\zeta^{\frac1{12}}$ and $e^{\hbar/24k}$. Modulo these ambiguities, $\phi_{\gamma,\zeta}(\hbar)=\phi_{K,\zeta}(\hbar)$ equals the series on the right hand side of the Quantum Modularity Conjecture.
:::

Note that if $F_k$ does not contain a primitive third root of unity (for example, if $F$ is sufficiently generic and $3\nmid k$) then topological invariance of $(\tau_{k})^{12 k}$ together with Theorem [\[thm.1loop\]](#thm.1loop){reference-type="ref" reference="thm.1loop"} implies topological invariance of $(\tau_k)^{4k}$.
