---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-003-13-prior-work-and-our-contributions
section_title: "Prior work and our contributions"
section_number: 1.3
pages: 4-4
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.915
latex_coverage_ratio: 1.0
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
Some elements of optimization theory on flag manifolds have been considered in [@NSP2006], although optimization is not its main focus and only analytic expressions for tangent spaces and gradients have been obtained. In particular, no actual algorithm appears in [@NSP2006] --- note that a Riemannian steepest descent algorithm in the spirit of [@EAS] would at least require analytic expressions for geodesics and, to the best of our knowledge, they have never been derived; in fact prior to this article it is not even known if such expressions exist.

The main contribution of our article is in providing all necessary ingredients for optimization algorithms on flag manifolds in full details, and from two different perspectives --- representing a flag manifold as (i) a homogeneous space, where a flag is represented as an equivalence class of matrices; and as (ii) a compact submanifold of $\mathbb{R}^{n \times n}$, where every flag is uniquely represented by a matrix. We will provide four systems of extrinsic coordinates for representing a flag manifold that arise from (i) and (ii) --- while modern differential geometry invariably adopts an intrinsic coordinate-free approach, we emphasize that such suitable extrinsic coordinate systems are indispensable for performing computations on manifolds.

In particular, the analytic expressions for various differential geometric objects and operations required for our optimization algorithms will rely on these coordinate systems. We will supply ready-to-use formulas and algorithms, rigorously proven but also made accessible to applied mathematicians and practitioners. For the readers' convenience, the following is a road map to the formulas and algorithms:

::: center
  [object on flag manifold]{.smallcaps}   [results]{.smallcaps}
  --------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  point                                   Propositions [\[prop:equivalent definition of flag manifold\]](#prop:equivalent definition of flag manifold){reference-type="ref" reference="prop:equivalent definition of flag manifold"}, [\[prop:Stiefel\]](#prop:Stiefel){reference-type="ref" reference="prop:Stiefel"}, [\[prop:representation of flags\]](#prop:representation of flags){reference-type="ref" reference="prop:representation of flags"}, [\[prop:reduced coord\]](#prop:reduced coord){reference-type="ref" reference="prop:reduced coord"}
  tangent vector                          Propositions [\[prop:tangent1\]](#prop:tangent1){reference-type="ref" reference="prop:tangent1"}, [\[prop:tangent2a\]](#prop:tangent2a){reference-type="ref" reference="prop:tangent2a"}, [\[prop:tangent2\]](#prop:tangent2){reference-type="ref" reference="prop:tangent2"}, [\[prop:tangent3\]](#prop:tangent3){reference-type="ref" reference="prop:tangent3"}, Corollary [\[prop:tangent2b\]](#prop:tangent2b){reference-type="ref" reference="prop:tangent2b"}
  metric                                  Propositions [\[prop:metric\]](#prop:metric){reference-type="ref" reference="prop:metric"}, [\[prop:metric2\]](#prop:metric2){reference-type="ref" reference="prop:metric2"}, [\[prop:metric3\]](#prop:metric3){reference-type="ref" reference="prop:metric3"}
  geodesic                                Propositions [\[prop:geodesics1\]](#prop:geodesics1){reference-type="ref" reference="prop:geodesics1"}, [\[prop:geodesics2\]](#prop:geodesics2){reference-type="ref" reference="prop:geodesics2"}, [\[prop:geodesic3a\]](#prop:geodesic3a){reference-type="ref" reference="prop:geodesic3a"}, [\[prop:geodesics3\]](#prop:geodesics3){reference-type="ref" reference="prop:geodesics3"}
  arclength                               Corollary [\[cor:arc-length\]](#cor:arc-length){reference-type="ref" reference="cor:arc-length"}, Proposition [\[prop:geodesic3a\]](#prop:geodesic3a){reference-type="ref" reference="prop:geodesic3a"}
  geodesic distance                       Proposition [\[prop:geodist\]](#prop:geodist){reference-type="ref" reference="prop:geodist"}
  parallel transport                      Propositions [\[prop:pt\]](#prop:pt){reference-type="ref" reference="prop:pt"}, [\[prop:pt2\]](#prop:pt2){reference-type="ref" reference="prop:pt2"}, [\[prop:pt1\]](#prop:pt1){reference-type="ref" reference="prop:pt1"}
  gradient                                Proposition [\[prop:gradient\]](#prop:gradient){reference-type="ref" reference="prop:gradient"}
  Hessian                                 Proposition [\[prop:Hessian\]](#prop:Hessian){reference-type="ref" reference="prop:Hessian"}
  steepest descent                        Algorithm [\[alg:sd\]](#alg:sd){reference-type="ref" reference="alg:sd"}
  conjugate gradient                      Algorithm [\[alg:cg\]](#alg:cg){reference-type="ref" reference="alg:cg"}
:::
