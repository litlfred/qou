---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-004-21-ideal-triangulations-and-neumann-zagier-data
section_title: "Ideal triangulations and Neumann-Zagier data"
section_number: 2.1
pages: 4-6
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.946
doc_brief: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY — The Quantum Modularity Conjecture of Zagier predicts the existence of a for- mal power series with arithmetically interesting coeﬃcients that"
---
[]{#sub.NZ label="sub.NZ"}

Ideal triangulations were introduced by Thurston as an efficient way to describe (algebraically, or numerically) 3-dimensional hyperbolic manifolds. For a leisure introduction, the reader may consult Thurston's original notes [@Th], the exposition of Neumann--Zagier [@NZ] and Weeks [@Weeks] and the documentation of `SnapPy` [@snappy]. The shape of a 3-dimensional hyperbolic tetrahedra is a complex number $z \in\mathbb C\setminus\{0,1\}$. Letting $z' = (1-z)^{-1}$ and $z''=1-z^{-1}$, the edges of an oriented ideal tetrahedron of shape $z$ can be assigned complex numbers according to Figure [1](#fig.tet){reference-type="ref" reference="fig.tet"}.

![An ideal tetrahedron with a shape assignement.](draws/tet.pdf){#fig.tet width="2in"}

Let $M$ be an oriented hyperbolic manifold with one cusp (for instance a hyperbolic knot complement) and $\mathcal T$ an ideal triangulation of $M$ containing $N$ tetrahedra. In [@DG] the authors introduced a Neumann-Zagier datum of $\mathcal T$. The latter is a tuple $\gamma=(\mathbf A, \mathbf B,\nu,z,f,f'')$ that consists of:

-   Two matrices $\mathbf A, \mathbf B\in \mathrm{GL}(N,\mathbb{Z})$ and a vector $\nu\in \mathbb{Z}^N$ encoding the coefficients of Thurston's gluing equations for the triangulation ($N-1$ independent equations imposing trivial holonomy around edges, and one equation imposing parabolic holonomy around the cusp).

-   An $N$-tuple $z=(z_1,...,z_N)\in \mathbb{C}\backslash\{0,1\}$ of shape parameters, with each $z_i$ parametrizing the shape of the $i$-th tetrahedron, satisfying the gluing equations in the form $z^{\mathbf A}z''{}^{\mathbf B} = (-1)^\nu$, *i.e.* 

    $$\prod_i z_i^{A_{ji}}(1-z_i^{-1})^{B_{ji}} = (-1)^{\nu_j} \quad 
    \text{for all} \quad j=1,\ldots, N\,.$$

-   Two $N$-tuples $f,f''\in \mathbb{Z}^N$ satisfying

    $$\mathbf A f + \mathbf B f'' = \nu\,.$$

    These provide a combinatorial flattening in the sense of [@Neumann-combi]. The integers $f,f''$, and $f'=1-f-f''$ also label edges of tetrahedra, with the property that the sum around any edge of the triangulation is $2$.

The Neumann-Zagier datum depends not just on the triangulation $\mathcal T$ but also on which edges of each tetrahedron are labelled by the distinguished shape parameter $z_i$; this $3^N$-fold choice has been called a choice of "quad" or "gauge.".

Neumann and Zagier [@NZ] proved that $(\mathbf A\;\mathbf B)$ forms the top half of a symplectic matrix, *i.e.* that $\mathbf A\mathbf B^T$ is symmetric and $(\mathbf A\;\mathbf B)$ has full rank. It follows that if $\mathbf B$ is invertible, then $\mathbf B^{-1}\mathbf A$ is symmetric. We will call a Neumann-Zagier datum $\mathbb Z$-*nondegeretate* if $\mathbf B$ is invertible over the integers.

Fix a positive integer $k$. If $\gamma$ is a Neumann-Zagier datum, let

$$\label{eq.zeta.theta}
\zeta = e^{\frac{2\pi i}{k}}\,,\qquad \theta_i = z_i^{1/k}\,,$$

where $\theta_i$ are chosen so that $\theta_i^k=z_i$. This defines number fields $F = \mathbb Q(z_1,...,z_N)$, $F_k = F(\zeta)$, and $F_{G,k} 
=F_k(\theta_1,...,\theta_N)$, such that

$$F\subset F_k\subset F_{G,k}\,.$$

Observe that $F_{G,k}/F_k$ is the abelian Galois (Kummer) extension with group $G=(\mathbb Z/k\mathbb Z)^N=\langle\sigma_1,\dots, \sigma_N \rangle$ where $$\label{eq.sigma}
\sigma_j(\theta_i)=\zeta^{-\delta_{i,j}} \theta_i$$ where $\delta_{i,j}$ is Kronecker's delta function. For the basic properties of Kummer theory, see [@Lang Sec.VI.8].

Below, we will construct a series $\phi_{\gamma,\zeta}(\hbar)$

for the $k$-th root of unity $\zeta = \exp(2\pi i/k)$. Then, after proving in Theorems [\[thm.1loop\]](#thm.1loop){reference-type="ref" reference="thm.1loop"} and [\[thm.1\]](#thm.1){reference-type="ref" reference="thm.1"} that the coefficients in this series belong to $F_k$, the series $\phi_{\gamma,\zeta^p}(\hbar)$ for any other $k$-th root of unity $\zeta^p = \exp(2\pi ip/k)$ can be obtained from $\phi_{\gamma,\zeta}(\hbar)$ by a Galois automorphism.
