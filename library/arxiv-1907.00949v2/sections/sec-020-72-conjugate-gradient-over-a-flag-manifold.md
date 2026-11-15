---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-020-72-conjugate-gradient-over-a-flag-manifold
section_title: "Conjugate gradient over a flag manifold"
section_number: 7.2
pages: 22-22
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.916
latex_coverage_ratio: 0.899
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
[]{#sec:cg label="sec:cg"}

We present the conjugate gradient method in Algorithm [\[alg:cg\]](#alg:cg){reference-type="ref" reference="alg:cg"}. Unlike steepest descent, conjugate gradient requires that we construct our new descent direction from the $(k-1)$th and $k$th iterates, i.e., one needs to compare tangent vectors at two different points on the manifold and the only way to do this is to parallel transport the two tangent vectors to the same point. There is no avoiding parallel transport in conjugate gradient.

As the expression for parallel transport in [\[eq:pt2\]](#eq:pt2){reference-type="eqref" reference="eq:pt2"} indicates, we will need to compute $$e^{-\varphi_{tB}}(X) = \sum_{k=1}^{\infty} \frac{(-1)^k}{k!} \varphi_{tB}^k(X),\quad \varphi_{tB}(X) = \frac{t}{2}[B,X]_{\mathfrak{m}}.$$ The rapid decay of the exponential series allows us to to replace it by a finite sum, reducing the task to recursively computing the iterated brackets and projection onto $\mathfrak{m}$: $$\varphi_{tB}^k(X) =\varphi_{tB} \circ \cdots \circ \varphi_{tB} (X)
= \Bigl(\frac{t}{2}\Bigr)^k [B, [ B,\dots,[B,X]_{\mathfrak{m}} \dots ]_{\mathfrak{m}}]_{\mathfrak{m}}.$$ As we had pointed out at the end of Section [\[sec:ortho\]](#sec:ortho){reference-type="ref" reference="sec:ortho"}, this step is unnecessary for the Grassmannian as $[B,X]_{\mathfrak{m}} = 0$ if $d= 1$, i.e., for $\mathop{\mathrm{Flag}}(k;n) = \mathop{\mathrm{Gr}}(k,n)$. A careful treatment of the computation of $e^{-\varphi_{tB}}(X)$ requires more details than we could go into here and is deferred to [@next].

::: algorithm
::: algorithmic
$\llbracket Y_0 \rrbracket\in \mathop{\mathrm{Flag}}(n_1,\dots,n_d;n)$ with $Y_0\in \mathbb{R}^{n\times n_d}$ and $Y_0^{\scriptscriptstyle\mathsf{T}}Y_0=I$; find $Y_0^\perp \in \mathbb{R}^{n \times (n-n_d)}$ such that $[ Y_0,Y_0^\perp] \in \mathop{\mathrm{O}}(n)$; set $X_{0} = [Y_0 ,  Y_0^\perp]$; set $G_{0} = -\nabla f(\llbracket Y_0 \rrbracket)$ and $H_0 = -G_0$; compute $\widehat{B} = X_{i}^{\scriptscriptstyle\mathsf{T}}H_{i};$ set $B \in \mathbb{R}^{n \times n}$ as $B_{ij} = \widehat{B}_{ij}$ for $j \leq n_d$; $B_{ij} = -\widehat{B}_{ji}$ for $j \geq n_d$ and $i \leq n_d$; $B_{ij} = 0$ otherwise; minimize $f\bigl(X_{i} \exp(tB) I_{n,n_d}\bigr)$ over $t \in \mathbb{R}$; set $X_{i+1} = X_i \exp(t_{\min} B)$; set $Y_{i+1} = X_{i+1} I_{n,n_d}$; set $Y_{i+1}^\perp = X_{i+1} I_{n,n-n_d}$; set $G_{i+1} = -\nabla f(\llbracket Y_{i+1} \rrbracket)$; find $\widetilde{G}_{i+1}\in \mathbb{R}^{n \times (n-n_d)}$ such that $\widehat{G}_{i+1} = [G_{i+1},\widetilde{G}_{i+1}]$ is skew-symmetric; $\tau H_{i} =  X_{i}  \exp(t_{\min}B) e^{-\varphi_{t_{\min}B}} ( B) I_{n,n_d}$; $\tau G_{i} = X_{i} \exp(t_{\min}B) e^{-\varphi_{t_{\min}B}} (\widehat{G}_{i} ) I_{n,n_d}$; $\gamma_i = g_{\llbracket Y_{i+1} \rrbracket} (G_{i+1}-\tau G_i, G_{i+1})/g_{\llbracket Y_i \rrbracket} (G_i, G_i)$; $H_{i+1} = -G_{i+1} + \gamma_{i} \tau H_i$; reset $H_{i+1} = -G_{i+1}$ if $i+1 \equiv 0 \bmod (k+1)(n-k)$; $\llbracket Y_{\operatorname{opt}} \rrbracket= \llbracket X_{\operatorname{opt}} I_{n,n_d} \rrbracket$
:::
:::
