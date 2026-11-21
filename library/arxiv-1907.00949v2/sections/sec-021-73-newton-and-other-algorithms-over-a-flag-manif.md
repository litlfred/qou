---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-021-73-newton-and-other-algorithms-over-a-flag-manif
section_title: "Newton and other algorithms over a flag manifold"
section_number: 7.3
pages: 22-23
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 1.0
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
The closed-form analytic expressions derived in this article permit one to readily extend other optimization algorithms on Euclidean spaces to flag manifolds. For example, the *Newton search direction* is given by the tangent vector $X \in T_{\llbracket Y \rrbracket} \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ such that $$\nabla^2f(\llbracket Y \rrbracket) (X,X') = g_{\llbracket Y \rrbracket}\bigl(-\nabla f(\llbracket Y \rrbracket),X' \bigr) = -\mathop{\mathrm{tr}}(f_Y^{\scriptscriptstyle\mathsf{T}}X'),$$ for every $X'\in T_{\llbracket Y \rrbracket} \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$, which gives us a system of linear equations upon plugging in the expression for Riemannian Hessian in [\[eq:Hessian\]](#eq:Hessian){reference-type="eqref" reference="eq:Hessian"}. Using the Newton search direction for $G_i$ in Algorithm [\[alg:sd\]](#alg:sd){reference-type="ref" reference="alg:sd"} then gives us Newton method on the flag manifold. In a similar vein, one may derive other standard algorithms for unconstrained optimization, e.g., quasi-Newton method, accelerated gradient descent, stochastic gradient descent, trust region methods, etc, for the flag manifold. Nevertheless, given that the goal of our article is to develop foundational material, we will leave these to future work [@next].
