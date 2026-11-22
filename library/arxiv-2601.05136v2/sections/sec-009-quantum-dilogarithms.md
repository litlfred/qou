---
doc_id: arxiv-2601.05136v2
doc_title: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant"
section_id: sec-009-quantum-dilogarithms
section_title: "Quantum dilogarithms"
section_number: null
pages: 9-9
source_pdf: 2601.05136v2.pdf
source_sha256: cee15456257d3028
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 1.0
doc_brief: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant — Previous work of the author and N."
---
[]{#sec:Quantum dilogarithms label="sec:Quantum dilogarithms"}

For a nonzero complex parameter $\mathsf b$ [@Faddeev2001] is $$\Phi_{\mathsf b}(z) \mathrel{:=}
  \exp
  \int_{\mathbb{R} + \ii \epsilon}
  \frac{
    \exp(-2 \ii zw)
  }{
    4 \sinh(w \mathsf b ) \sinh(w/\mathsf b)
  }
  \frac{dw}{w}$$ for $|\operatorname{Im}z| < |\operatorname{Im}c_{\mathsf b}|$, where $c_{\mathsf b} \mathrel{:=}\frac{i}{2} \left( \mathsf b + \mathsf b^{-1}\right).$ $\Phi_{\mathsf b}$ extends to a meromorphic function on $\mathbb{C}$ with an essential singularity at infinity. We consider the case where $\mathsf b = \sqrt N$ and the function $\pfl{}$ with $$\exp \pfl{t}
  =
  \Phi_{\sqrt N}\left(\ii \sqrt{N} t - c_{\sqrt N} +
  \frac{\ii}{\sqrt N} \right)
  .$$ Strictly speaking $\pfl{\zeta}$ depends on a choice of branch of the logarithm but our formulas only depend on the well-defined function $e^{\pfl{\zeta}}$. It is nonetheless convenient to use the logarithmic notation. The recurrence relation $$\label{eq:pfl recurrence}
  \exp \pfl{t} =
  \frac{
    \exp \pfl{t-1/N}
  }{
    1 - e^{\tu t}
  }$$ connects $\pfl{}$ to the $q$-factorial and shows that the poles and zeros of $e^{\pfl{t}}$ all occur when $t \in \frac{1}{N}
\mathbb{Z}$ and $t \not \in (0,1)$.
