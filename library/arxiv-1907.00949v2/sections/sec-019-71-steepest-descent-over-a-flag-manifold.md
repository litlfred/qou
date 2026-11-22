---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-019-71-steepest-descent-over-a-flag-manifold
section_title: "Steepest descent over a flag manifold"
section_number: 7.1
pages: 21-22
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.905
latex_coverage_ratio: 0.881
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
We describe this in Algorithm [\[alg:sd\]](#alg:sd){reference-type="ref" reference="alg:sd"}. A point $\llbracket Y \rrbracket\in \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ is represented in Stiefel coordinates, i.e., as an orthonormal matrix $Y \in \mathbb{R}^{n \times n_d}$, $Y^{\scriptscriptstyle\mathsf{T}}Y=I$. As usual, $Y^{\perp} \in \mathbb{R}^{n \times (n-n_d)}$ is such that $X \coloneqq [ Y, Y^{\perp}] \in \mathop{\mathrm{O}}(n)$. The Riemannian gradient $\nabla f \in \mathbb{R}^{n \times n_d}$ is given by Proposition [\[prop:gradient\]](#prop:gradient){reference-type="ref" reference="prop:gradient"} and we set $G = - \nabla f$ to be the search direction. The exponential map direction $B\in \mathbb{R}^{n\times n}$ is uniquely obtained from $B I_{n,n_d} = [Y,Y^{\perp}]^{\scriptscriptstyle\mathsf{T}}G$, i.e., $B$ is the unique skew-symmetric matrix whose first $n_d$ columns is $[Y,Y^{\perp}]^{\scriptscriptstyle\mathsf{T}}G$. The next iterate is then found along the geodesic determined by the current iterate and the direction as in Proposition [\[prop:geodesic3a\]](#prop:geodesic3a){reference-type="ref" reference="prop:geodesic3a"}, although the exact line search may be substituted by any reasonable strategy for choosing step size. Note in particular that Algorithm [\[alg:sd\]](#alg:sd){reference-type="ref" reference="alg:sd"} does not involve parallel transport.

::: algorithm
::: algorithmic
$\llbracket Y_0 \rrbracket\in \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ with $Y_0 \in \mathbb{R}^{n\times n_d}$ and $Y_0^{\scriptscriptstyle\mathsf{T}}Y_0=I$; find $Y_0^{\perp} \in \mathbb{R}^{n \times (n-n_d)}$ such that $[Y_0,Y_0^\perp ] \in \mathop{\mathrm{O}}(n)$; set $X_{0} = [Y_0, Y_0^\perp ]$; set $G_{i} = -\nabla f(\llbracket Y_i \rrbracket)$; set $X_i = [Y_i, Y_i^\perp ]$; compute $\widehat{B} = X_{i}^{\scriptscriptstyle\mathsf{T}}G_{i}$; set $B \in \mathbb{R}^{n \times n}$ as $B_{ij} = \widehat{B}_{ij}$ for $j \leq n_d$; $B_{ij} = -\widehat{B}_{ji}$ for $j \geq n_d$ and $i \leq n_d$; $B_{ij} = 0$ otherwise; minimize $f\bigl(X_{i} \exp(tB) I_{n,n_d}\bigr)$ over $t \in \mathbb{R}$; set $X_{i+1} = X_{i} \exp(t_{\min}B)$; $\llbracket Y_{\operatorname{opt}} \rrbracket= \llbracket X_{\operatorname{opt}} I_{n,n_d} \rrbracket$
:::
:::
