---
doc_id: arxiv-hep-th-9304063v2
doc_title: "arXiv:hep-th/9304063v2 29 Jan 1999"
section_id: sec-000-1-introduction-and-statement-of-results
section_title: "Introduction and Statement of Results"
section_number: 1
pages: 1-3
source_pdf: 9304063v2.pdf
source_sha256: 14a82437462eae23
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.926
latex_coverage_ratio: 0.967
doc_brief: "arXiv:hep-th/9304063v2 29 Jan 1999 — 10 sections: Front matter; Introduction and Statement of Resu; The System of Partial Differential"
---
## Introduction

Scaling models of random $N\times N$ hermitian matrices and passing to the limit $N\ra\iy$ leads to integral operators whose Fredholm determinants describe the statistics of the spacing of the eigenvalues of hermitian matrices of large order [@mehta_book; @porter]. Which integral operators (or, more precisely, which kernels of integral operators) result depends on the matrix model one starts with and at which location in the spectrum the scaling takes place.

For the simplest model, the Gaussian Unitary Ensemble (GUE), and for many others as well (see, e.g., [@kpw; @mahoux_mehta91; @nagao_wadati; @pastur]), the kernel one obtains by scaling in the "bulk" of the spectrum is the "sine kernel" $$\frac{\sin\pi(x-y)}{\pi(x-y)}.$$ Precisely, this comes about as follows. If $\{\phi_{k}(x)\}_{k=0}^{\iy}$ is the sequence obtained by orthonormalizing the sequence $\{x^{k}\,e^{-x^{2}/2}\}$ over $(-\iy,\iy)$ and if K\_N(x,y) = \_k=0\^N-1 \_k(x) \_k(y)  , []{#KN label="KN"} then in the GUE the probability density that $n$ of the eigenvalues (irrespective of order) lie in infinitesimal intervals about $x_{1},\ldots,x_{n}$ is equal to $$R_{n}(x_{1},\ldots,x_{n})\,=\,\mbox{det}\ (K_{N}(x_{i},x_{j}))\,_{i,j=1,\ldots,n}.$$ The density of eigenvalues at a fixed point $z$ is $R_{1}(z)$, and this is $\sim\sqrt{2N}/\pi$ as $N\ra\iy$. Rescaling at $z$ leads to the sine kernel because of the relation $$\lim_{N\ra\iy}\frac{\pi}{\sqrt{2N}}K_{N}(z+\frac{\pi x}{\sqrt{2N}},z+\frac{\pi y}
{\sqrt{2N}})\,=\,\frac{\sin\pi(x-y)}{\pi(x-y)}.$$

Rescaling the GUE at the "edge" of the spectrum, however, leads to a different kernel. The edge corresponds to $z\sim\sqrt{2N}$, at which point the density is $\sim2^{\hf}N^{\frac{1}{6}}$, and we have there the scaling limit [@bowick_brezin; @forrester; @moore] $$\lim_{N\ra\iy}\frac{1}{2^{\hf}N^{\frac{1}{6}}} K_{N}(\sqrt{2N}+
\frac{x}{2^{\hf}N^{\frac{1}{6}}},\sqrt{2N}+\frac{y}{2^{\hf}N^{\frac{1}{6}}})\,
=\,\frac{{\rm Ai}(x)\,{\rm Ai}'(y)\,-{\rm Ai}'(x)\,{\rm Ai}(y)}{x-y}$$ where ${\rm Ai}$ is the Airy function. In previous work [@tw2] we found several analogies between properties of this "Airy kernel" and known properties of the sine kernel: a system of partial differential equations associated with the logarithmic differential of the Fredholm determinant when the underlying domain is a union of intervals [@jmms]; a representation of the Fredholm determinant in terms of a Painlevé transcendent in the case of a single interval [@jmms]; and, also in this case, asymptotic expansions for these determinants and related quantities [@dyson76; @btw; @widom92; @dyson92; @mehta_mahoux92b], achieved with the help of a differential operator which commutes with the integral operator. (See [@tw1] for further discussion of these properties of the sine kernel.)  

In this paper we show that there are completely analogous properties for a class of kernels which arise when one rescales the Laguerre or Jacobi ensembles at the edge of the spectrum. For the Laguerre ensemble the analogue of the sequence of functions $\{\phi_{k}(x)\}$ in ([\[KN\]](#KN){reference-type="ref" reference="KN"}) is obtained by orthonormalizing the sequence$$\{x^{k}\,x^{\al/2}\,e^{-x/2}\}$$over $(0,\iy)$ (here $\al>-1$), whereas for Jacobi one orthonormalizes $$\{x^{k}(1-x)^{\al/2}(1+x)^{\beta/2}\}$$ over $(-1,1)$. (Here $\al,\beta\,>\,-1$.) In the Laguerre ensemble of (positive) hermitian $N\times N$ matrices the eigenvalue density satisfies [@bronk; @nagao_wadati], for a fixed $x<1$, $$R_{1}(4Nx)\sim\frac{1}{2\pi}\sqrt{\frac{1-x}{x}}.$$ This limiting law is to be contrasted with the well-known Wigner semi-circle law in the GUE. The new feature here is the "hard edge" for $x\sim 0$. At this edge we have the scaling limit [@forrester]: $$\lim_{N\ra\iy}\frac{1}{4N}K_{N}(\frac{x}{4N},\frac{y}{4N}) 
=\,\frac{ J_{\al}(\sqrt{x})\,\sqrt{y} J_{\al}'(\sqrt{y})\,-
\sqrt{x} J_{\al}'(\sqrt{x})\, J_{\al}(\sqrt{y})}{2(x-y)}$$ where $J_\al(z)$ is the Bessel function of order $\al$. Both limits follow from the asymptotic formulas for the generalized Laguerre polynomials. (Scaling in the bulk will just lead to the sine kernel and scaling at the "soft edge," $x\sim 1$, will lead to the Airy kernel.) The same kernel arises when scaling the Jacobi ensemble at $-1$ or $1$. (Recall that in the Jacobi ensemble both $\pm 1$ are hard edges; see e.g. [@nagao_wadati].) 

For later convenience we introduce now a parameter $\la$ and define our "Bessel kernel" by

::: mathletters
$$\begin{aligned}
K(x,y):&=&\,\la\,\frac{J_{\al}(\sqrt{x})\,\sqrt{y}J_{\al}'(\sqrt{y})\,-
\sqrt{x}J_{\al}'(\sqrt{x})\,J_{\al}(\sqrt{y})}{2(x-y)}
\, ,\ \ \ (x\neq y)\label{Kdef}\\
&=&\, {\la\over 4}\left( J_{\al}(\sqrt{x})^2-J_{\al+1}(\sqrt{x})
 J_{\al-1}(\sqrt{x})
\right)\ \ \ (x=y).
\label{Kdiagdef}
\end{aligned}$$
:::

Before stating our results, we mention that in the cases $\al=\mp\hf$ we have, when $\la=1$,  K(x\^2,y\^2) =    , []{#dyson_kernels label="dyson_kernels"} which are kernels which arise when taking scaling limits in the bulk of the spectrum for the Gaussian orthogonal and symplectic ensembles [@mehta_book]. In particular, an asymptotic expansion we derive will generalize ones found by Dyson [@dyson76] for the Fredholm determinants of these kernels.

We now state the results we have obtained.
