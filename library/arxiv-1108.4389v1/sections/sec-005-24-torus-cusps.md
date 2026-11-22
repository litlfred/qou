---
doc_id: arxiv-1108.4389v1
doc_title: "Gauge Theories Labelled by Three-Manifolds"
section_id: sec-005-24-torus-cusps
section_title: "Torus cusps"
section_number: 2.4
pages: 17-19
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 1.0
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
[]{#sec:cuspbdy label="sec:cuspbdy"}

The cusp boundaries of a 3-manifold $M$ arise from the resolution of line defects, and have the topology of annuli or tori, depending on whether the defects are open or closed. For simplicity, we will only consider the closed, toroidal case in the present paper, though we note that annular cusps share many of the the same properties, and can be analyzed in a similar way.

Suppose, then, that $\partial M$ contains a toroidal cusp boundary $T^2$. For example, $M$ could be the complement of a knot in $S^3$. To describe the associated phase space $\mathcal{P}_{T^2}$, we can choose a basis of "A and B cycles" on the torus --- typically called meridian and longitude cycles in the case of knot complements.

[^1]

Since the fundamental group $\pi_1(T^2)$ is abelian, the $SL(2,{\mathbb C})$ holonomies along these cycles are simultaneously diagonalizable, and $\mathcal{P}_{T^2}$ is simply parametrized by their eigenvalues, *cf.* [@cooper-1994]:

$$\mathcal{P}_{T^2} = \big\{(m,\ell)\,\in\,{\mathbb C}^*\times {\mathbb C}^*\big\}\big/{\mathbb Z}_2\,,$$

where the Weyl group ${\mathbb Z}_2$ acts by inversion $(m,\ell)\mapsto (m^{-1},\ell^{-1})$. As above, it is also convenient to take logarithms

[^2]

$\boxed{u\equiv \log m}$ and $\boxed{v+i\pi\equiv\log \ell}$ and to lift the phase space to

$$\mathcal{P}_{T^2} = \big\{(u,v)\,\in\,{\mathbb C}\times{\mathbb C}\big\}/{\mathbb Z}_2\,.$$

Then the symplectic structure of $\mathcal{P}_{T^2}$ becomes $\omega_{T^2}=\frac{2}\hbar dv\wedge du$ [@gukov-2003], or

$$\{v,u\}=\hbar/2\,.$$

![Gluing two tetrahedra, as indicated by calligraphic letters on the faces, to form the figure-eight knot complement. On the right is a map of the resulting torus cusp boundary, triangulated by Euclidean vertex triangles.](fig8cusp){#fig:fig8cusp width="6.3in"}

The logarithmic eigenvalues $u$ and $v$ can both be computed as linear combinations of edge parameters $Z_i,\,Z_i',\,Z_i''$ of tetrahedra in a triangulation of $M$. To see this, recall that a cusp boundary $T^2$ is composed of small truncated-vertex triangles of the tetrahedra $\Delta_i$. Thus, it comes with a (Euclidean) 2d triangulation, as illustrated in Figure [1](#fig:fig8cusp){reference-type="ref" reference="fig:fig8cusp"}. The dihedral angles of tetrahedra $\Delta_i$ become actual (complexified) angles in the 2d triangles. Logarithmic holonomies can be computed by adding and subtracting the angles subtended by a given path, then dividing by two [@NZ; @Neumann-combinatorics]. For example, in Figure [1](#fig:fig8cusp){reference-type="ref" reference="fig:fig8cusp"} we have drawn the meridian and longitude of the figure-eight knot complement on a boundary $T^2$. The corresponding holonomies are

$$\label{Uv41}
\begin{align} U\equiv 2u &= Z'-W \\
 2v &= 2(Z-Z')
\end{align}$$

As functions on the product phase space $\mathcal{P}_{\{\partial\Delta_i\}}\simeq \{(Z,Z'Z'',W,W'Z'')\,|\,Z+Z'+Z''=W+W'+W''=i\pi\}$, these satisfy the expected commutation relation $\{v,U\}=\hbar$.

Continuing with the example of the figure-eight knot complement, we find that the triangulation of Figure [1](#fig:fig8cusp){reference-type="ref" reference="fig:fig8cusp"} has two internal edges, with corresponding gluing constraints

$$\label{C41}
C_1 = 2Z+Z''+2W+W'' \to 2\pi i\,,\qquad C_2 = 2Z'+Z''+2W'+W'' \to 2\pi i\,.$$

(It is easy to read these off from the map of the cusp, since every internal edge begins and ends at a "vertex" on the cusp triangulation. One just adds the angles surrounding the vertex.) Note that $C_1$ and $C_2$ both commute with $U$ and $v$. Moreover, *prior to* enforcing the condition $C_1=C_2=2\pi i$, there is an automatic relation $C_1+C_2=4\pi i$, so that one of the two gluing constraints is redundant. In general, for every closed torus cusp in a 3-manifold $M$, there will be one such redundant gluing constraint. In the end, for our figure-eight example, we see that $\mathcal{P}_{\partial M}=\mathcal{P}_{T^2} = \mathcal{P}_{\{\partial\Delta_i\}}\big/\!\!\big/(C_1=2\pi i) = \mathcal{P}_{\{\partial\Delta_i\}}\big/\!\!\big/(C_2=2\pi i)$.

The Lagrangian submanifold for the figure-eight knot complement is obtained by the symplectic reduction procedure described at the end of Section [\[sec:geomglue\]](#sec:geomglue){reference-type="ref" reference="sec:geomglue"} above. One starts with the product Lagrangian

$$\mathcal{L}_{\{\Delta_i\}} = \{z+z'^{-1}-1=0,\,w+w'^{-1}-1=0\}\;\subset\; \mathcal{P}_{\{\partial\Delta_i\}}\,,$$

where $z=e^Z,z=e^{Z'},w=e^{W},$ and $w'=e^{W'}$; rewrites the equations in terms of $m^2=e^U$, $\ell=-e^v$, and one of the gluing monomials $c_j=e^{C_I}$; eliminates all remaining variables that do not commute with $c_j$; and sets $c_j=1$. The end result is

$$\label{A41}
 \mathcal{L}_{M} = \{\ell-(m^4-m^2-2-m^{-2}+m^{-4})+\ell^{-1}=0\}\;\subset\;\mathcal{P}_M\,,$$

and this equation is the well known "A-polynomial" of the figure-eight knot [@cooper-1994; @gukov-2003].

[^1]: For a knot complement in $S^3$, $M=S^3\backslash K$, there is actually a canonical choice of cycles. The meridian is an infinitesimally small loop linking the knot $K$ once, while the longitude intersects the meridian once and is nullhomologous in $M$ (in particular, it has zero linking number with the knot). Presently, however, we will allow ourselves the freedom of choosing any basis of cycles whatsoever.

[^2]: As discussed in [@Dimofte-QRS], the shift by $i\pi$ in $v+i\pi=\log\ell$ characterizes the correct lift from $PSL(2,{\mathbb C})$ structures (most naturally computed by triangulation data) to $SL(2,{\mathbb C})$.
