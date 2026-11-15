---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-002-12-the-neumann-zagier-datum
section_title: "The Neumann-Zagier datum"
section_number: 1.2
pages: 4-5
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.986
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sec.introNZ label="sec.introNZ"}

All manifolds and all ideal triangulations in this paper will be oriented. The volume of a hyperbolic manifold $M$, appearing in the Volume Conjecture and contributing to $S_{M,0}$, is already known to have a simple expression in terms of shape parameters of a regular ideal triangulation, *i.e.*, one that recovers the complete hyperbolic structure of $M$. (For extended discussion on regular triangulations, see Section [\[sec.extensions\]](#sec.extensions){reference-type="ref" reference="sec.extensions"}.) If $\mathcal{T}=\{\Delta_i\}_{i=1}^N$ is a regular ideal triangulation of $M$ with shape parameters $z_i \in \mathbb C\setminus\{0,1\}$ for $i=1,\dots,N$, then (*cf.* [@DuS; @NZ])

$$\mathrm{Vol}(M) 
= \sum_{i=1}^N D(z_i)\,,
\label{eq.Dz}$$

where $D(z) := \mathrm{Im}\big({\rm Li}_2(z)\big)+\arg(1-z)\log|z|$ is the Bloch-Wigner dilogarithm function. This formula can also be interpreted as calculating the image of the class $[M]:=\sum_i[z_i]\,\in\,\mathcal{B}$ of $M$ in the Bloch group $\mathcal{B}$ under the natural map $D:\mathcal{B} \to \mathbb R$. An analogous formula, using the class of $M$ in the "extended" Bloch group $\widehat{\mathcal{B}}$, gives the full complexified volume $S_{M,0}$ [@Neumann-combi; @N; @GoZi; @Zickert-rep].

It is natural to ask whether the class of $M$ in $\mathcal{B}$ determines not only $S_{M,0}$ but the higher $S_{M,n}$ as well. This question was posed to the authors several years ago by D. Zagier. Subsequent computations [@GZ; @Ga2] indicated that a positive answer was not possible. For example, there is a family of pairs of pretzel knots $\big((-2,3,3+2p),\,(-2,3,3-2p)\big)$ for $p=2,3,...$, as well as the figure-eight knot and its sister, which all have the same class in the Bloch group (and classes differing by 6-torsion in the extended Bloch group), but different invariants $S_{M,n}$ for $n \geq 1$.

The extra information necessary to determine the $S_{M,n}$ can be described as follows. Recall that if $\mathcal{T}$ is a regular ideal triangulation of $M$ with $N$ tetrahedra, its shapes $z=(z_1,\dots,z_N)$ satisfy a system of polynomial equations, one equation for every edge, and one imposing parabolic holonomy around the meridian of the cusp [@Th; @NZ]. Let us set

$$z_i' = (1-z_i)^{-1}\,,\qquad z_i''=1-z_i^{-1}\,.$$

The equations can then be written in the form

$$\qquad

z^{\mathbf A} z''{}^{\mathbf B} :=
\prod_{j=1}^N z_j^{\mathbf A_{ij}}\big(1-z_j^{-1}\big)^{\mathbf B_{ij}}=\pm 1\,,
\qquad (i=1,...,N)\,, \label{NZintro}$$

where $\mathbf A$ and $\mathbf B$ are $N\times N$ square matrices with integer entries, which we call the *Neumann-Zagier matrices* following [@NZ].

::: definition
[]{#def.NZdatum label="def.NZdatum"} If $\mathcal{T}$ is a regular ideal triangulation of $M$, its *Neumann-Zagier datum* (resp., *enhanced Neumann-Zagier datum*) is given by the triple $$\beta_\mathcal{T}=(z,\mathbf A,\mathbf B) \qquad \text{resp.,}
\qquad\widehat\beta_{\mathcal T}=(z,\mathbf A,\mathbf B, f)\,,$$ where $z$ is a solution to the gluing equations and $f$ is a combinatorial flattening of $\mathcal T$, a collection of integers that we define in Section [\[sub.flat\]](#sub.flat){reference-type="ref" reference="sub.flat"}.
:::

As we will discuss in detail in Section [\[sec.triang\]](#sec.triang){reference-type="ref" reference="sec.triang"}, implicit in the above definition is the dependence of $\beta_{\mathcal{T}}$ and $\widehat\beta_{\mathcal T}$ on the following choices:

1.  a pair of opposite edges for every oriented ideal tetrahedron (a so-called choice of *quad type*),

2.  an edge of $\mathcal T$,

3.  a meridian loop in the boundary of $M$ in general position with respect to $\mathcal T$,

4.  a combinatorial flattening.
