---
doc_id: arxiv-math-0603444v2
doc_title: "QUASIHOMOGENEITY OF ISOLATED HYPERSURFACE SINGULARITIES AND LOGARITHMIC COHOMOLOGY"
section_id: sec-000-1-formulation-of-the-result
section_title: "Formulation of the result"
section_number: 1
pages: 1-2
source_pdf: 0603444v2.pdf
source_sha256: 46edfcddca963d08
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.809
doc_brief: "QUASIHOMOGENEITY OF ISOLATED HYPERSURFACE SINGULARITIES AND LOGARITHMIC COHOMOLOGY — We characterize quasihomogeneity of isolated hypersurface singu- larities by the injectivity of the map induced by"
---
We consider the germ of an isolated hypersurface singularity $D\subseteq(\mathbb{C}^n,0)$. Let $\mathcal{O}=\mathcal{O}_{\mathbb{C}^n,0}$ be the ring of germs of holomorphic functions on $\mathbb{C}^n$ at the origin with maximal ideal $\mathfrak{m}$ and $f\in\mathfrak{m}^2$ a reduced defining equation of $D$. For notational simplicity, we shall write $\mathbb{C}^n$ instead of $(\mathbb{C}^n,0)$. In terms of coordinates $x_1,\dots,x_n$ on $\mathbb{C}^n$, $\mathcal{O}=\mathbb{C}\{x_1,\dots,x_n\}$ is the ring of convergent power series and $\mathfrak{m}=\langle x_1,\dots,x_n\rangle$. We abbreviate by $f_i=\frac{\partial f}{\partial{x_i}}$, $i=1,\dots,n$, the partial derivatives of $f$.

Let $\Omega^\bullet=\Omega_{\mathbb{C}^n,0}^\bullet$ be the complex of holomorphic differential forms at the origin and denote by $\Omega^\bullet(\star D)=\Omega^\bullet[f^{-1}]$ the complex of meromorphic differential forms with poles along $D$. K. Saito [@Sai80 §1] introduced the subcomplex of logarithmic differential forms $\Omega^\bullet(\log D)\subseteq\Omega^\bullet(\star D)$ along $D$. It is the maximal subcomplex consisting of forms with at most a simple pole along $D$. Let $\mathop{\mathrm{Der}}=\mathop{\mathrm{Der}}_\mathbb{C}\mathcal{O}$ be the module of $\mathbb{C}$-linear derivations of $\mathcal{O}$. It is a free $\mathcal{O}$-module of rank $n$ with a basis formed by the partial derivatives $\partial_1,\dots,\partial_n$ with respect to $x_1,\dots,x_n$. The module of logarithmic vector fields $\mathop{\mathrm{Der}}(-\log D))\subseteq\mathop{\mathrm{Der}}$ consists of all vector fields tangent to the smooth part of $D$. Under the natural inner product, $\mathop{\mathrm{Der}}(-\log D))$ and $\Omega^1(\log D)$ are mutually $\mathcal{O}$-dual.

Our object of interest in this article is the natural map $$\SelectTips{cm}{}\xymatrix{
H^n_0(\mathcal{O})\ar[r]^-{d_1}&H^n_0(\Omega^1(\log D))
}$$ induced by the first differential of $\Omega^\bullet(\log D)$ in the top local cohomology supported at the origin. We shall show that its injectivity is equivalent to the quasihomogeneity of the singularity.

::: thm
[]{#0 label="0"} $D$ is quasihomogeneous if and only if $d_1$ is injective.
:::

For non--isolated singularities, at least one implication fails: The divisor $D\subseteq\mathbb{C}^3$ defined by $f=xy(x+y)(x+yz)$ is not quasihomogeneous but $d_1$ is injective.
