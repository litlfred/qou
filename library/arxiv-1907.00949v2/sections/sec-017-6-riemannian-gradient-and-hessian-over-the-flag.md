---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-017-6-riemannian-gradient-and-hessian-over-the-flag
section_title: "Riemannian Gradient and Hessian over the flag manifold"
section_number: 6
pages: 19-21
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.927
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
[]{#sec:gH label="sec:gH"}

We will derive expressions for the Riemannian gradient and Riemannian Hessian of a real-valued function on a flag manifold, the main ingredients of optimization algorithms. Although in principle we may use any of the four extrinsic coordinate systems introduced in the last two sections --- orthogonal (as $n \times n$ orthogonal matrices), Stiefel (as $n \times n_d$ orthonormal matrices), projection or reduced projection (as $d$-tuples of $n \times n$ projection matrices) coordinates --- Stiefel coordinates give the most economical representation and we will use this as our coordinates of choice. So in the following we will identify $$\label{eq:identify}
\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n) = \mathop{\mathrm{V}}(n_d,n) / \bigl(\mathop{\mathrm{O}}(n_1) \times \mathop{\mathrm{O}}(n_2-n_1) \times \dots \times \mathop{\mathrm{O}}(n_d- n_{d-1})\bigr).$$ Our expressions for gradient and Hessian in Stiefel coordinates may of course be converted to other coordinates --- straightforward although the results may be notationally messy.

::: proposition
[]{#prop:gradient label="prop:gradient"} Let $f:\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n) \to \mathbb{R}$ be a smooth function expressed in Stiefel coordinates $Y \in \mathop{\mathrm{V}}(n_d, n)$. Define the $n\times n_d$ matrix of partial derivatives, $$\label{eq:fY}
f_Y \coloneqq \biggl[  \frac{\partial f}{\partial y_{ij}} \biggr]_{i,j=1}^{n,n_d}.$$ Write $Y = [Y_1,\dots, Y_d]$ where $Y_i\in \mathbb{R}^{n\times (n_i-n_{i-1})}$ and $f_Y = [f_{Y_1},\dots, f_{Y_d}]$ where $f_{Y_i}$ is the $n\times (n_i-n_{i-1})$ submatrix, $i=1,\dots, d$. Then its Riemannian gradient at $\llbracket Y \rrbracket\in \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ is given by $\nabla f(\llbracket Y \rrbracket) = [\Delta_1, \dots, \Delta_d]$ where $$\label{eq:gradient variable delta}
\Delta_i = f_{Y_i} - \Bigl(Y_i Y_i^{\scriptscriptstyle\mathsf{T}}f_{Y_i} + \sum\nolimits_{j\ne i } Y_j f_{Y_j}^{\scriptscriptstyle\mathsf{T}}Y_i\Bigr), \quad i=1,\dots,d.$$
:::

::: proof
*Proof.* For any $X\in T_{\llbracket Y \rrbracket} \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$, let $X_a\in \mathbb{R}^{n\times n}$ be the unique skew-symmetric matrix such that $X = Q X_a I_{n,n_d}$, where $Q\in \mathop{\mathrm{O}}(n)$ is such that $Y = QI_{n,n_d}$. Since the metric expressed in Stiefel coordinates [\[eq:g2\]](#eq:g2){reference-type="eqref" reference="eq:g2"} and expressed in orthogonal coordinates [\[eq:metric1\]](#eq:metric1){reference-type="eqref" reference="eq:metric1"} must be equal, $$\label{eq:tmp1}
g_{\llbracket Y \rrbracket} \bigl( \nabla f (\llbracket Y \rrbracket),X \bigr)  = g_{\llbracket Q \rrbracket} \bigl(\nabla f  (\llbracket Y \rrbracket)_a, X_a\bigr) = \frac{1}{2} \mathop{\mathrm{tr}}( \nabla f  (\llbracket Y \rrbracket)_a^{\scriptscriptstyle\mathsf{T}}X_a).$$ By definition of Riemannian gradient [\[eq:gH\]](#eq:gH){reference-type="eqref" reference="eq:gH"}, we also have $$\label{eq:tmp2}
g_{\llbracket Y \rrbracket}(\nabla f(\llbracket Y\rrbracket), X) =  \mathop{\mathrm{tr}}(f_Y^{\scriptscriptstyle\mathsf{T}}X_a).$$ Comparing [\[eq:tmp1\]](#eq:tmp1){reference-type="eqref" reference="eq:tmp1"} and [\[eq:tmp2\]](#eq:tmp2){reference-type="eqref" reference="eq:tmp2"}, we see that $\nabla f(\llbracket Y\rrbracket)$ is the projection of $f_Y$ onto $T_{\llbracket Y \rrbracket} \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$, i.e., $f_Y = \nabla f(\llbracket Y\rrbracket)  + Z$ for some $Z$ orthogonal to $T_{\llbracket Y \rrbracket} \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$. We may take $Z = [Z_1,\dots, Z_d]$ to be $$Z_i \coloneqq Y_i Y_i^{\scriptscriptstyle\mathsf{T}}f_{Y_i} + \sum\nolimits_{j\ne i } Y_j f_{Y_j}^{\scriptscriptstyle\mathsf{T}}Y_i,\quad i=1,\dots,d,$$ and verify that because of [\[eq:tangent space\]](#eq:tangent space){reference-type="eqref" reference="eq:tangent space"}, we indeed have $f_Y - Z\in T_{\llbracket Y \rrbracket} \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ and thus $Z$ is orthogonal to $T_{\llbracket Y \rrbracket} \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$. ◻
:::

The Riemannian gradient $\nabla f$ may also be derived by solving an optimization problem as in [@NSP2006]. Note that if $d = 1$, [\[eq:gradient variable delta\]](#eq:gradient variable delta){reference-type="eqref" reference="eq:gradient variable delta"} becomes $\nabla f (\llbracket Y \rrbracket) = \Delta = f_Y -  Y Y^{\scriptscriptstyle\mathsf{T}}f_Y$, the well-known expression for Riemannian gradient of Grassmannian in [@EAS].

::: proposition
[]{#prop:Hessian label="prop:Hessian"} Let $f:\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n) \to \mathbb{R}$ be a smooth function expressed in Stiefel coordinates $Y \in \mathop{\mathrm{V}}(n_d, n)$ and let $f_Y$ be as in [\[eq:fY\]](#eq:fY){reference-type="eqref" reference="eq:fY"}. Then its Riemannian Hessian $\nabla^2f(\llbracket Y \rrbracket)$ at $\llbracket Y \rrbracket\in \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ is the symmetric bilinear form given by $$\label{eq:Hessian}
\nabla^2f(\llbracket Y \rrbracket) (X,X') = f_{Y,Y} ( X, X') - \frac{1}{2} \bigl[ \mathop{\mathrm{tr}}(f_Y^{\scriptscriptstyle\mathsf{T}}Q B^{\scriptscriptstyle\mathsf{T}}Q^{\scriptscriptstyle\mathsf{T}}X') +  \mathop{\mathrm{tr}}(f_Y^{\scriptscriptstyle\mathsf{T}}Q C^{\scriptscriptstyle\mathsf{T}}Q^{\scriptscriptstyle\mathsf{T}}X)  \bigr) \bigr],$$ for $X,X'\in T_{\llbracket Y \rrbracket} \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$, where $$\label{eq:fYY}
f_{Y,Y} (X,X') \coloneqq \sum_{i,k=1}^n \sum_{j,l=1}^{n_d} \frac{\partial^2 f}{\partial y_{ij} \partial y_{kl}} x_{ij} x'_{kl},$$ $Q\in \mathop{\mathrm{O}}(n)$ is such that $Q I_{n,n_d} = Y$, and $B,C \in \mathbb{R}^{n \times n}$ are the unique skew-symmetric matrices such that $X = Q B I_{n,n_d}$, $X' = Q C I_{n,n_d}$ respectively.
:::

::: proof
*Proof.* By Proposition [\[prop:geodesic3a\]](#prop:geodesic3a){reference-type="ref" reference="prop:geodesic3a"}, a geodesic $\gamma$ with $\gamma'(0) = X$ and $\gamma(0) = \llbracket Y \rrbracket$ takes the form $\gamma(t) = \llbracket Q\exp(tB) I_{n,n_d} \rrbracket$ where $Q \in \mathop{\mathrm{O}}(n)$ is such that $Y = QI_{n,n_d}$ and $X = Q B I_{n,n_d}$. Applying chain rule, $$\frac{d}{dt} f(\gamma(t)) = \mathop{\mathrm{tr}}\bigl( f_Y^{\scriptscriptstyle\mathsf{T}}\gamma'(t)\bigr),\qquad
\frac{d^2 }{dt^2} f(\gamma(t))  = \mathop{\mathrm{tr}}\bigl(\gamma'(t)^{\scriptscriptstyle\mathsf{T}}f^{\scriptscriptstyle\mathsf{T}}_{\gamma(t),\gamma(t)} \gamma'(t)\bigr) + \mathop{\mathrm{tr}}\bigl(f_Y^{\scriptscriptstyle\mathsf{T}}\gamma''(t)\bigr);$$ followed by evaluating at $t = 0$ gives $$\nabla^2f(\llbracket Y \rrbracket)(X,X) =  \frac{d^2 }{dt^2} f(\gamma(t)) \Big|_{t=0} = f_{Y,Y} (X, X)  - \mathop{\mathrm{tr}}(f_Y^{\scriptscriptstyle\mathsf{T}}Q B^{\scriptscriptstyle\mathsf{T}}Q ^{\scriptscriptstyle\mathsf{T}}X).$$ The required expression [\[eq:Hessian\]](#eq:Hessian){reference-type="eqref" reference="eq:Hessian"} then follows from [\[eq:gH\]](#eq:gH){reference-type="eqref" reference="eq:gH"} and [\[eq:polar\]](#eq:polar){reference-type="eqref" reference="eq:polar"}. ◻
:::

If $d = 1$, [\[eq:Hessian\]](#eq:Hessian){reference-type="eqref" reference="eq:Hessian"} reduces to the well-known expression for Riemannian Hessian of the Grassmannian [@EAS Section 2.5.4] since $$\begin{gathered}
\nabla^2f(\llbracket Y \rrbracket) (X,X') = f_{Y,Y} (X, X') - \mathop{\mathrm{tr}}(f_Y^{\scriptscriptstyle\mathsf{T}}Q B^{\scriptscriptstyle\mathsf{T}}Q^{\scriptscriptstyle\mathsf{T}}X') \\
 = f_{Y,Y} (X, X') - \mathop{\mathrm{tr}}(f_Y^{\scriptscriptstyle\mathsf{T}}Y (X')^{\scriptscriptstyle\mathsf{T}}X)  = f_{Y,Y} (X, X') - \mathop{\mathrm{tr}}(X^{\scriptscriptstyle\mathsf{T}}X' Y^{\scriptscriptstyle\mathsf{T}}f_Y).
\end{gathered}$$

There is slight inconsistency in our definitions of $f_Y$ and $f_{YY}$ to make these expressions easily portable into computer codes. To be consistent with [\[eq:fYY\]](#eq:fYY){reference-type="eqref" reference="eq:fYY"}, we could define $f_Y$ as a linear form: $$f_Y(X) = \sum_{i,j=1}^{n,n_d} \frac{\partial f}{\partial y_{ij}}  x_{ij}$$ for $X \in  T_{\llbracket Y \rrbracket} \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$. Alternatively, to be consistent with [\[eq:fY\]](#eq:fY){reference-type="eqref" reference="eq:fY"}, we could define $f_{YY}$ to be a hypermatrix of partials (this is not a $4$-tensor, just a convenient way to represent a $2$-tensor): $$f_{YY} =\biggl[ \frac{\partial^2 f}{\partial y_{ij} \partial y_{kl}} \biggr]_{i,j,k,l=1}^{n,n_d, n, n_d}.$$
