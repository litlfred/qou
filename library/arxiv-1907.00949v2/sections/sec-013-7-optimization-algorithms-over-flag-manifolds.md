---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-013-7-optimization-algorithms-over-flag-manifolds
section_title: "Optimization algorithms over flag manifolds"
section_number: 7
pages: 21-23
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.954
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
[]{#sec:optim label="sec:optim"}

With analytic expressions for points, tangent vectors, metric, geodesic, parallel transport, Riemannian gradient and Hessian in place, Riemannian manifold optimization algorithms are straightforward to derive from the usual ones. For example, for steepest descent, instead of adding a negative multiple of the gradient to the current iterate, we move the current iterate along the geodesic with initial velocity vector given by the negative of the gradient. Again, we may do this in any of the four coordinates system we have introduced although for the same reason in Section [\[sec:gH\]](#sec:gH){reference-type="ref" reference="sec:gH"}, we prefer the Stiefel coordinates. Thus here we will assume the identification [\[eq:identify\]](#eq:identify){reference-type="eqref" reference="eq:identify"} as before.

## Steepest descent over a flag manifold

We describe this in Algorithm [\[alg:sd\]](#alg:sd){reference-type="ref" reference="alg:sd"}. A point $\llbracket Y \rrbracket\in \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ is represented in Stiefel coordinates, i.e., as an orthonormal matrix $Y \in \mathbb{R}^{n \times n_d}$, $Y^{\scriptscriptstyle\mathsf{T}}Y=I$. As usual, $Y^{\perp} \in \mathbb{R}^{n \times (n-n_d)}$ is such that $X \coloneqq [ Y, Y^{\perp}] \in \mathop{\mathrm{O}}(n)$. The Riemannian gradient $\nabla f \in \mathbb{R}^{n \times n_d}$ is given by Proposition [\[prop:gradient\]](#prop:gradient){reference-type="ref" reference="prop:gradient"} and we set $G = - \nabla f$ to be the search direction. The exponential map direction $B\in \mathbb{R}^{n\times n}$ is uniquely obtained from $B I_{n,n_d} = [Y,Y^{\perp}]^{\scriptscriptstyle\mathsf{T}}G$, i.e., $B$ is the unique skew-symmetric matrix whose first $n_d$ columns is $[Y,Y^{\perp}]^{\scriptscriptstyle\mathsf{T}}G$. The next iterate is then found along the geodesic determined by the current iterate and the direction as in Proposition [\[prop:geodesic3a\]](#prop:geodesic3a){reference-type="ref" reference="prop:geodesic3a"}, although the exact line search may be substituted by any reasonable strategy for choosing step size. Note in particular that Algorithm [\[alg:sd\]](#alg:sd){reference-type="ref" reference="alg:sd"} does not involve parallel transport.

:::: algorithm
::: algorithmic
$\llbracket Y_0 \rrbracket\in \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ with $Y_0 \in \mathbb{R}^{n\times n_d}$ and $Y_0^{\scriptscriptstyle\mathsf{T}}Y_0=I$; find $Y_0^{\perp} \in \mathbb{R}^{n \times (n-n_d)}$ such that $[Y_0,Y_0^\perp ] \in \mathop{\mathrm{O}}(n)$; set $X_{0} = [Y_0, Y_0^\perp ]$; set $G_{i} = -\nabla f(\llbracket Y_i \rrbracket)$; set $X_i = [Y_i, Y_i^\perp ]$; compute $\widehat{B} = X_{i}^{\scriptscriptstyle\mathsf{T}}G_{i}$; set $B \in \mathbb{R}^{n \times n}$ as $B_{ij} = \widehat{B}_{ij}$ for $j \leq n_d$; $B_{ij} = -\widehat{B}_{ji}$ for $j \geq n_d$ and $i \leq n_d$; $B_{ij} = 0$ otherwise; minimize $f\bigl(X_{i} \exp(tB) I_{n,n_d}\bigr)$ over $t \in \mathbb{R}$; set $X_{i+1} = X_{i} \exp(t_{\min}B)$; $\llbracket Y_{\operatorname{opt}} \rrbracket= \llbracket X_{\operatorname{opt}} I_{n,n_d} \rrbracket$
:::
::::

## Conjugate gradient over a flag manifold {#sec:cg}

We present the conjugate gradient method in Algorithm [\[alg:cg\]](#alg:cg){reference-type="ref" reference="alg:cg"}. Unlike steepest descent, conjugate gradient requires that we construct our new descent direction from the $(k-1)$th and $k$th iterates, i.e., one needs to compare tangent vectors at two different points on the manifold and the only way to do this is to parallel transport the two tangent vectors to the same point. There is no avoiding parallel transport in conjugate gradient.

As the expression for parallel transport in [\[eq:pt2\]](#eq:pt2){reference-type="eqref" reference="eq:pt2"} indicates, we will need to compute $$e^{-\varphi_{tB}}(X) = \sum_{k=1}^{\infty} \frac{(-1)^k}{k!} \varphi_{tB}^k(X),\quad \varphi_{tB}(X) = \frac{t}{2}[B,X]_{\mathfrak{m}}.$$ The rapid decay of the exponential series allows us to to replace it by a finite sum, reducing the task to recursively computing the iterated brackets and projection onto $\mathfrak{m}$: $$\varphi_{tB}^k(X) =\varphi_{tB} \circ \cdots \circ \varphi_{tB} (X)
= \Bigl(\frac{t}{2}\Bigr)^k [B, [ B,\dots,[B,X]_{\mathfrak{m}} \dots ]_{\mathfrak{m}}]_{\mathfrak{m}}.$$ As we had pointed out at the end of Section [\[sec:ortho\]](#sec:ortho){reference-type="ref" reference="sec:ortho"}, this step is unnecessary for the Grassmannian as $[B,X]_{\mathfrak{m}} = 0$ if $d= 1$, i.e., for $\mathop{\mathrm{Flag}}(k;n) = \mathop{\mathrm{Gr}}(k,n)$. A careful treatment of the computation of $e^{-\varphi_{tB}}(X)$ requires more details than we could go into here and is deferred to [@next].

:::: algorithm
::: algorithmic
$\llbracket Y_0 \rrbracket\in \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ with $Y_0\in \mathbb{R}^{n\times n_d}$ and $Y_0^{\scriptscriptstyle\mathsf{T}}Y_0=I$; find $Y_0^\perp \in \mathbb{R}^{n \times (n-n_d)}$ such that $[ Y_0,Y_0^\perp] \in \mathop{\mathrm{O}}(n)$; set $X_{0} = [Y_0 ,  Y_0^\perp]$; set $G_{0} = -\nabla f(\llbracket Y_0 \rrbracket)$ and $H_0 = -G_0$; compute $\widehat{B} = X_{i}^{\scriptscriptstyle\mathsf{T}}H_{i};$ set $B \in \mathbb{R}^{n \times n}$ as $B_{ij} = \widehat{B}_{ij}$ for $j \leq n_d$; $B_{ij} = -\widehat{B}_{ji}$ for $j \geq n_d$ and $i \leq n_d$; $B_{ij} = 0$ otherwise; minimize $f\bigl(X_{i} \exp(tB) I_{n,n_d}\bigr)$ over $t \in \mathbb{R}$; set $X_{i+1} = X_i \exp(t_{\min} B)$; set $Y_{i+1} = X_{i+1} I_{n,n_d}$; set $Y_{i+1}^\perp = X_{i+1} I_{n,n-n_d}$; set $G_{i+1} = -\nabla f(\llbracket Y_{i+1} \rrbracket)$; find $\widetilde{G}_{i+1}\in \mathbb{R}^{n \times (n-n_d)}$ such that $\widehat{G}_{i+1} = [G_{i+1},\widetilde{G}_{i+1}]$ is skew-symmetric; $\tau H_{i} =  X_{i}  \exp(t_{\min}B) e^{-\varphi_{t_{\min}B}} ( B) I_{n,n_d}$; $\tau G_{i} = X_{i} \exp(t_{\min}B) e^{-\varphi_{t_{\min}B}} (\widehat{G}_{i} ) I_{n,n_d}$; $\gamma_i = g_{\llbracket Y_{i+1} \rrbracket} (G_{i+1}-\tau G_i, G_{i+1})/g_{\llbracket Y_i \rrbracket} (G_i, G_i)$; $H_{i+1} = -G_{i+1} + \gamma_{i} \tau H_i$; reset $H_{i+1} = -G_{i+1}$ if $i+1 \equiv 0 \bmod (k+1)(n-k)$; $\llbracket Y_{\operatorname{opt}} \rrbracket= \llbracket X_{\operatorname{opt}} I_{n,n_d} \rrbracket$
:::
::::

## Newton and other algorithms over a flag manifold

The closed-form analytic expressions derived in this article permit one to readily extend other optimization algorithms on Euclidean spaces to flag manifolds. For example, the *Newton search direction* is given by the tangent vector $X \in T_{\llbracket Y \rrbracket} \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ such that $$\nabla^2f(\llbracket Y \rrbracket) (X,X') = g_{\llbracket Y \rrbracket}\bigl(-\nabla f(\llbracket Y \rrbracket),X' \bigr) = -\mathop{\mathrm{tr}}(f_Y^{\scriptscriptstyle\mathsf{T}}X'),$$ for every $X'\in T_{\llbracket Y \rrbracket} \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$, which gives us a system of linear equations upon plugging in the expression for Riemannian Hessian in [\[eq:Hessian\]](#eq:Hessian){reference-type="eqref" reference="eq:Hessian"}. Using the Newton search direction for $G_i$ in Algorithm [\[alg:sd\]](#alg:sd){reference-type="ref" reference="alg:sd"} then gives us Newton method on the flag manifold. In a similar vein, one may derive other standard algorithms for unconstrained optimization, e.g., quasi-Newton method, accelerated gradient descent, stochastic gradient descent, trust region methods, etc, for the flag manifold. Nevertheless, given that the goal of our article is to develop foundational material, we will leave these to future work [@next].
