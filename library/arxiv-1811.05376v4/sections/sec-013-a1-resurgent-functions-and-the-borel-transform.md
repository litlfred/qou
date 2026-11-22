---
doc_id: arxiv-1811.05376v4
doc_title: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres"
section_id: sec-013-a1-resurgent-functions-and-the-borel-transform
section_title: "A.1 Resurgent functions and the Borel transform"
section_number: null
pages: 36-36
source_pdf: 1811.05376v4.pdf
source_sha256: a486709d0a78d19c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.942
latex_coverage_ratio: 1.0
doc_brief: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres — For a Seifert ﬁbered homology sphere X we show that the q-series invariant ˆZ0(X; q) introduced by"
---
The theory of resurgence was originally developed by Écalle in [@Ecalle81a] and [@Ecalle81b]. See [@MitschiSauzin16] for an introduction to the mathematical theory of resurgence and see [@DunneUnsal15] for an introduction to the general use of resurgence in quantum field theory. Garoufalidis [@Garoufalidis08] and Witten [@Witten11] where the pioneers of the use of resurgence in quantum Chern-Simons theory.

::: definition
[]{#def:res label="def:res"} For a Riemann surface $C$ with universal covering space $$\pi: \tilde{C}\rightarrow C$$ the algebra of resurgent functions is $\mathcal{R}(C)=\mathcal{M}(\tilde{C}).$
:::

One source of resurgent functions are the Borel transforms of Laplace integrals. We now introduce the Borel transform. Let $\Gamma \in \mathcal{M}(\mathbb{C})$ be the Gamma function, which for $z \in \mathbb{C}$ with $\mathop{\mathrm{Re}}(z)>0$ is defined by $$\Gamma(z)= \int_0^{\infty} e^{-t} t^{z-1} \mathop{\mathrm{{d}\hskip-.6mm}}t.$$

::: definition
[]{#def:Bor label="def:Bor"} Let $\{\alpha_j \}_{j=0}^{\infty}$ be an increasing sequence of positive real numbers, $\{\beta_j \}_{j=0}^{\infty}$ a sequence of non-negative integers and $\{c_j\}_{j=0}^{\infty}$ a sequence of complex numbers. Consider the formal series $$\tilde{\varphi}(\lambda)=\sum_{j=0}^{\infty} c_j \lambda^{-\alpha_j} \log(\lambda)^{\beta_j}.$$ The Borel transform of $\tilde{\varphi}(\lambda)$ is given by the formal series $$\label{def:Borel}
    \mathcal{B}(\tilde{\varphi})(\zeta) =\sum_{j=0}^{\infty} c_j (-1)^{\beta_j} \frac{\partial^{\beta_j}}{\partial {\alpha_j}^{\beta_j}} \left( \frac{\zeta^{\alpha_j-1}}{\Gamma(\alpha_j)}  \right).$$
:::
