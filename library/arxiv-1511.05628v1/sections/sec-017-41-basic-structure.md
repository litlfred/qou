---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-017-41-basic-structure
section_title: "Basic structure"
section_number: 4.1
pages: 15-16
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.943
doc_brief: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY — The Quantum Modularity Conjecture of Zagier predicts the existence of a for- mal power series with arithmetically interesting coeﬃcients that"
---
Chern-Simons theory with complex gauge group $G_\mathbb{C}$ (where $G$ is a compact Lie group) was initially studied by Witten in [@Witten-CSgrav; @Witten-cx]. It is a topological quantum field theory in three-dimensions, whose action is a sum of holomorphic and antiholomorphic copies of the usual Chern-Simons action

$$S(\mathcal A, \overline\mathcal A) = \frac{t}{8\pi} \,
I_{CS}(\mathcal A) + \frac{\tilde t}{8\pi}\, I_{CS}(\overline\mathcal A)\,,$$

where $\mathcal A$ is a connection on a $G_\mathbb{C}$ bundle over a 3-manifold $M$, and $I_{CS}(\mathcal A) = \int_M (\mathcal Ad\mathcal A+\frac23 \mathcal A^3)$ (with additional boundary terms if $M$ is not closed). In order for the path-integral measure $\exp(-iS)$ to be invariant under all gauge transformations of $\mathcal A$, the levels $t,\tilde t$ must obey the quantization condition

$$k:= \tfrac12(t + \tilde t)  \in \mathbb{Z}\,.$$

Additionally, the theory is unitary for $\sigma:=\frac12(t-\tilde t)\in i\mathbb R$, and less obviously so for $\sigma\in \mathbb R$. We will not require unitarity in the following, however.

The classical solutions of Chern-Simons theory are flat $G_\mathbb{C}$ connections. Indeed, in the limit $t,\tilde t\to \infty$, which corresponds to infinitely weak coupling, the partition function $\mathcal{Z}(t,\tilde t) = \int D\mathcal A\, D\overline{\mathcal A}\,e^{-iS}$ is dominated by flat connections

$$\begin{aligned}
\mathcal Z(t,\tilde t) &\sim \sum_{\text{flat $\mathcal A^*$}} \tau(\mathcal A^*)
\exp\bigg[\frac{t}{8\pi i}I_{CS}(\mathcal A^*) + \delta(\mathcal A^*)\log t 
+ \sum_{n=2}^\infty \bigg(\frac{8\pi i}{t}\bigg)^{n-1} S_n(\mathcal A^*)\bigg] \\
 &\hspace{.8in} \times 
 \tau(\overline{\mathcal A}^*)
\exp\bigg[\frac{\tilde t}{8\pi i}I_{CS}(\overline{\mathcal A}^*) + \delta(\overline{\mathcal A^*})\log t 
+ \sum_{n=2}^\infty \bigg(\frac{8\pi i}{\tilde t}\bigg)^{n-1} 
S_n(\overline{\mathcal A}^*)\bigg]
\notag
\end{aligned}$$

where $\tau(\mathcal A)^{-2}$ is a Ray-Singer torsion twisted by the flat connection $\mathcal A$ and the $S_n$ are "higher-loop" topological invariants. For $G_\mathbb{C}=SL(2,\mathbb{C})$ and $\mathcal A^*$ the hyperbolic flat connection, such an asymptotic expansion at weak coupling played a central role in the generalized Volume Conjecture [@Gu].
