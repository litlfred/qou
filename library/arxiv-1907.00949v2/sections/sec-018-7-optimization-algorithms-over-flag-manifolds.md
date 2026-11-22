---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-018-7-optimization-algorithms-over-flag-manifolds
section_title: "Optimization algorithms over flag manifolds"
section_number: 7
pages: 21-21
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 1.0
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
[]{#sec:optim label="sec:optim"}

With analytic expressions for points, tangent vectors, metric, geodesic, parallel transport, Riemannian gradient and Hessian in place, Riemannian manifold optimization algorithms are straightforward to derive from the usual ones. For example, for steepest descent, instead of adding a negative multiple of the gradient to the current iterate, we move the current iterate along the geodesic with initial velocity vector given by the negative of the gradient. Again, we may do this in any of the four coordinates system we have introduced although for the same reason in Section [\[sec:gH\]](#sec:gH){reference-type="ref" reference="sec:gH"}, we prefer the Stiefel coordinates. Thus here we will assume the identification [\[eq:identify\]](#eq:identify){reference-type="eqref" reference="eq:identify"} as before.
