---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-022-8-numerical-experiments
section_title: "Numerical experiments"
section_number: 8
pages: 23-23
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 1.0
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
[]{#sec:num label="sec:num"}

We will test our algorithm for steepest descent on the flag manifold numerically. As we explained in Section [\[sec:cg\]](#sec:cg){reference-type="ref" reference="sec:cg"}, the experiments for conjugate gradient algorithm is more involved and is deferred to [@next]. We run our numerical experiments on two problems: (i) the principal flag problem in Section [\[sec:dis\]](#sec:dis){reference-type="ref" reference="sec:dis"} is one for which the solution may be determined in closed-form analytically, and thus it serves to demonstrate the correctness of our algorithm, i.e., converges to the true solution; (ii) a variation of the previous problem with a more complicated objective function to show that the convergence behavior remains unchanged. In addition, neither problem can be solved by simply treating them as nonlinear optimization problems with equality constraints and applying standard nonlinear optimization algorithms.

In the following we will assume the identification in [\[eq:identify\]](#eq:identify){reference-type="eqref" reference="eq:identify"} and use Stiefel coordinates throughout.
