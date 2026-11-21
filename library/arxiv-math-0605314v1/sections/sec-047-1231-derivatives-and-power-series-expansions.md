---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-047-1231-derivatives-and-power-series-expansions
section_title: "Derivatives and power series expansions"
section_number: 12.3.1
pages: 41-41
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.949
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:power-seri-expans-1 label="sec:power-seri-expans-1"}

Like polynomials and analytic functions, the elements of $\Zqh$ can be differentiated arbitrarily many times. In fact, the derivation $\frac{d}{dq}\zzzcolon \modZ [q]\rightarrow \modZ [q]$ is continuous with respect to the topology defined by the ideals $(q)_n\modZ [q]$, $n\ge 0$, since we have $$\frac{d}{dq}(q)_{2n}\in (q)_n\modZ [q].$$ Therefore, $\frac d{dq}$ induces a continuous $\modZ$-linear derivation $$\frac{d}{dq}\zzzcolon \Zqh\rightarrow \Zqh.$$ This implies that there are higher derivations $$\frac{1}{k!}\frac{d^k}{dq^k}=\frac{1}{k!}
  (\frac{d}{dq})^k\zzzcolon \Zqh\rightarrow \Zqh.$$ for all $k\ge 0$. (Recall that $(\frac{d}{dq})^k(\modZ [q])\subset k!\modZ [q]$. This implies that $(\frac{d}{dq})^k(\Zqh)\subset k!\Zqh$.) Suppose $f(q)\in \Zqh$ and $\zeta \in \calZ$. Define the "Taylor series at $\zeta$" of $f(q)$ by $$T_\zeta (f(q))=\sum_{k\ge 0}\frac{1}{k!}\frac{d^kf}{dq^k}(\zeta )(q-\zeta )^k
  \in \modZ [\zeta ][[q-\zeta ]].$$ Then one can easily check $T_\zeta (f(q))=\iota _\zeta (f(q))$.
