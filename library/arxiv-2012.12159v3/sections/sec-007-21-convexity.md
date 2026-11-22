---
doc_id: arxiv-2012.12159v3
doc_title: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME"
section_id: sec-007-21-convexity
section_title: "Convexity"
section_number: 2.1
pages: 7-8
source_pdf: 2012.12159v3.pdf
source_sha256: 473ec6959e82cd98
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.516
doc_brief: "A FUNK PERSPECTIVE ON BILLIARDS, PROJECTIVE GEOMETRY AND MAHLER VOLUME — We explore connections furnished by the Funk metric, a relative of the Hilbert metric, between projective geometry, billiards"
---
A convex body $K\subset V=\mathbb{R}^n$ is a compact convex set, which we will henceforth assume to have non-empty interior. We write $|K|$ for the Euclidean volume of $K$, and $\mathcal H^{n-1}$ for the Hausdorff measure on $\partial K$.

The Euclidean unit ball is $B^n$, and $\omega_n:=|B^n|=\frac{\pi^{\frac n 2}}{\Gamma(\frac n 2 +1)}$. The support function of $K\subset V$ is $h_K(\xi)=\sup_{x\in K}\langle x,\xi\rangle:V^*\to \mathbb{R}$, which is a convex function. We say that $K$ is smooth and strictly convex if $\partial K$ is $C^2$-smooth of strictly positive gaussian curvature.

By $\mathcal K_0(V)$ we denote the class of convex bodies with $0\in\mathop{\mathrm{int}}(K)$. For $K\in\mathcal K_0(V)$, the *Minkowski functional* of $K$ is $\|x\|_K=\inf\{t>0: \frac{x}{t}\in K\}$. If $K=-K$, it is a norm for which $K$ is the unit ball. The cone measure on $\partial K$ is denoted $\mu_K$, and has $\int_K d\mu_K=n|K|$. If $\partial K$ is $C^1$ smooth, it is given by $d\mu_K(x)=\langle x, \nu_x\rangle d\mathcal H^{n-1}(x)$, where $\nu_x$ is the outward unit normal.

The *polar* (or *dual*) convex body is $K^o=\{\xi\in V^*: \langle \xi,x\rangle\leq 1\}\in\mathcal K_0(V^*)$. It holds that $\|\xi\|_{K^o}=h_K(\xi)$. For $z\in \mathop{\mathrm{int}}(K)$, we write $K^z=(K-z)^o$.

For a Borel function $\phi:V\to \mathbb{R}\cup\{+\infty\}$, its *Legendre transform* is $$\label{eq:legendre}\mathcal L\phi(\xi)=\sup_{x\in\mathbb{R}^n} (\langle x,\xi\rangle -\phi(x)): V^*\to \mathbb R\cup\{+\infty\}.$$ If $\phi$ is defined on a subset of $V$, we first extend it by $+\infty$.

The function $\mathcal L\phi$ is always convex, and if $\phi$ is convex then $\mathcal L^2\phi=\phi$. An easy computation shows that $\mathcal L(\frac1p\|x\|_K^p)=\frac1q\|\xi\|_{K^o}^q$ for $p^{-1}+q^{-1}=1$. This includes the case $p=\infty, q=1$ which reads $\mathcal L(-\log \mathbbm 1_K)(\xi)=\|\xi\|_{K^o}=h_K(\xi)$.

Writing $\phi_z=\phi(z+\bullet)$, one immediately finds that $$\mathcal L\phi_z(\xi)=\sup_{x} (\langle x,\xi\rangle-\phi(x+z))=\mathcal L\phi(\xi)-\langle z,\xi\rangle.$$ For much more information on convexity, we refer to [@schneider_book].
