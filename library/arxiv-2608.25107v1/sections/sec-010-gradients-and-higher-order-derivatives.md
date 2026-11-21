---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples"
section_id: sec-010-gradients-and-higher-order-derivatives
section_title: "Gradients and higher-order derivatives"
section_number: null
pages: 7-7
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.986
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples — 19 sections: ADoNIS: A Differentiable generatOr; Introduction; Differentiable programming in part"
---
[]{#sec:adonis_gradients label="sec:adonis_gradients"}

Because $\bm\theta \mapsto \{w_i\}$ is a JAX function, the Jacobian of the binned prediction, $$J_{bk} = \frac{\partial m_b}{\partial\theta_k},$$ is obtained by automatic differentiation. As the map takes few inputs (the parameter vector) to many outputs (the per-event weights, reduced to bins), we evaluate it in forward mode. A single Jacobian-vector product with a unit tangent $\mathbf{e}_k$ returns the full per-event derivative in the $k$-th parameter direction in one forward pass, and the columns for all parameters are batched into one vectorised evaluation whose cost is a small multiple of a single forward reweight.

The same construction extends to arbitrary derivative order by nesting Jacobian-vector products along the desired parameter directions, with no symbolic derivative code required. The first derivatives form the Gauss--Newton, or Fisher, matrix $$\label{eq:adonis_fisher}
F_{kl} = \sum_b \frac{1}{\sigma_b^{2}}\,
\frac{\partial m_b}{\partial\theta_k}\,
\frac{\partial m_b}{\partial\theta_l},$$ with $\sigma_b$ the per-bin uncertainty. This is the positive-semidefinite curvature approximation underlying the fits of Sec. [\[sec:fitting\]](#sec:fitting){reference-type="ref" reference="sec:fitting"}.
