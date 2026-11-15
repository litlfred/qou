---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.933
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
Launched around 20 years ago in a classic article of Edelman, Arias, and Smith [@EAS], Riemannian *manifold optimization* is now entrenched as a mainstay of optimization theory [@ABG2007; @AMS2009; @CDH2011; @WY2013]. While studies of optimization algorithms on Riemannian manifolds predate [@EAS], the distinguishing feature of Edelman et al.'s approach is that their algorithms are built entirely and directly from standard algorithms in numerical linear algebra; in particular, they do not require numerical solutions of differential equations. For instance, the parallel transport of a vector in [@EAS] is not merely discussed in the abstract but may be explicitly computed in efficient and numerically stable ways via closed-form analytic expressions involving QR and singular value decompositions of various matrices.

The requirement that differential geometric quantities appearing in a manifold optimization algorithms have analytic expressions in terms of standard matrix decompositions limits the type of Riemannian manifolds that one may consider. Aside from Euclidean spaces, we know of exactly three Riemannian manifolds [@AMS2009] on which one may define optimization algorithms in this manner:

1.  []{#it:V label="it:V"} Stiefel manifold $\mathop{\mathrm{V}}(k,n)$,

2.  []{#it:Gr label="it:Gr"} Grassmann manifold $\mathop{\mathrm{Gr}}(k,n)$,

3.  manifold of positive definite matrices $\mathbb{S}^n_{{\plus\plus}}$.

The main contribution of this article is to furnish a fourth: *flag manifolds*.

A flag in a finite-dimensional vector space $\mathbb{V}$ over $\mathbb{R}$ is a nested sequence of linear subspaces $\{\mathbb{V}_i\}_{i=1}^d$ of $\mathbb{V}$, i.e., $$\{0\} \subsetneq \mathbb{V}_1 \subsetneq \dots \subsetneq \mathbb{V}_d \subsetneq \mathbb{V}.$$ For any increasing integer sequence of length $d$, $0 < n_1 < \dots < n_d < n$, the set of all flags $\{\mathbb{V}_i\}_{i=1}^d$ with $\dim (\mathbb{V}_i) = n_i$, $i=1, \dots, d$, is a smooth manifold called a *flag manifold*, and denoted by $\mathop{\mathrm{Flag}}(n_1,\dots,n_d;\mathbb{V})$. This is a generalization of the Grassmannian $\mathop{\mathrm{Gr}}(k, \mathbb{V})$ that parameterizes $k$-dimensional linear subspaces in $\mathbb{V}$ as flags of length one are just subspaces, i.e., $\mathop{\mathrm{Flag}}(k; \mathbb{V}) =\mathop{\mathrm{Gr}}(k, \mathbb{V})$. Flag manifolds, sometimes also called flag varieties, were first studied by Ehresmann [@Ehresmann1934] and saw rapid development in 1950's [@borel1953b; @borel1953a; @Borel1953; @chern1953]. They are now ubiquitous in many areas of pure mathematics, and, as we will discuss next, they are also ubiquitous in applied mathematics, just hidden in plain sight.

The optimization algorithms on Grassmann and Stiefel manifolds originally proposed in [@EAS] have found widespread applications: e.g., computer vision [@WWF; @WSCG], shape analysis [@WW2012; @Schulz2014], matrix computations [@B2013; @LL2001], subspace tracking [@BNR], and numerous other areas --- unsurprising as subspaces and their orthonormal bases are ubiquitous in all areas of science and engineering. For the same reason, we expect optimization algorithms on flag manifolds to be similarly useful as flags are also ubiquitous --- any multilevel, multiresolution, or multiscale phenomena likely involve flags, whether implicitly or explicitly. We will discuss some examples from numerical analysis and statistics.
