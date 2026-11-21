---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-001-11-quantum-modular-forms
section_title: "Quantum modular forms"
section_number: 1.1
pages: 2-3
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 1.0
doc_brief: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY — The Quantum Modularity Conjecture of Zagier predicts the existence of a for- mal power series with arithmetically interesting coeﬃcients that"
---
[]{#sub.QMF label="sub.QMF"}

Quantum modular forms are fascinating objects introduced by Zagier [@Za:QMF]. In the simplest formulation, a quantum modular form is a complex valued function $f$ on the set of complex roots of unity that comes equipped with a suitable formal power series expansion $\phi_\zeta(\hbar) \in \mathbb C[\![\hbar]\!]$ at each complex root of unity $\zeta$. Usually $f$ is given explicitly. On the other hand, the power series $\phi_\zeta$, although uniquely determined by $f$, are not easy to obtain.

One of the most interesting examples of quantum modular forms is conjectured to be the logarithm of the Kashaev invariant of a knot. This is Zagier's Quantum Modularity Conjecture [@Za:QMF]. Evidence for this conjecture includes ample numerical computations performed by Zagier and the first author [@GZ1] as well as a proof in the case of the $4_1$ knot [@GZ1].

Our goal is to construct an explicit formula for the power series that appear in the Quantum Modularity Conjecture of a knot. We highlight some features of our results.

(a) The formulas for our series $\phi_{\gamma,\zeta}(\hbar)$ use as input a complex root of unity $\zeta$ and Neumann-Zagier datum $\gamma$, i.e., an ideal triangulation of a knot complement and a geometric solution to the gluing equations. Such a datum is readily available from `SnapPy`.

(b) Our series have arithmetically interesting coefficients; see Theorems [\[thm.1loop\]](#thm.1loop){reference-type="ref" reference="thm.1loop"} and [\[thm.1\]](#thm.1){reference-type="ref" reference="thm.1"}.

(c) Our series lead to exact computations that match the numerically computed asymptotics of the Kashaev invariant at various roots of unity. The details of our computations are given in Section [\[sec.compute\]](#sec.compute){reference-type="ref" reference="sec.compute"}.

(d) Our construction is motivated by the analysis of singular limits in complex Chern-Simons theory, with gauge group $SL(2,\mathbb{C})$. Complex Chern-Simons theory depends on two coupling constants or *levels* $(k,\sigma)\in (\mathbb{Z},\mathbb{C})$ [@Witten-cx], and the series $\phi_{\gamma,\zeta}(\hbar)$ at $\zeta=e^{2\pi i/k}$ is obtained by sending $\sigma\to k$ (while keeping $k$ fixed). We describe this limit in greater detail in Section [\[sec.CCS\]](#sec.CCS){reference-type="ref" reference="sec.CCS"}, after introducing the definition of $\phi_{\gamma,\zeta}(\hbar)$ and proving its number-theoretic properties in Sections [\[sec.def\]](#sec.def){reference-type="ref" reference="sec.def"}-[\[sec.proofs\]](#sec.proofs){reference-type="ref" reference="sec.proofs"}.
