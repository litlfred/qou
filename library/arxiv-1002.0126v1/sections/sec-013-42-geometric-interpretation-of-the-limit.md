---
doc_id: arxiv-1002.0126v1
doc_title: "AN INTRODUCTION TO THE VOLUME CONJECTURE"
section_id: sec-013-42-geometric-interpretation-of-the-limit
section_title: "Geometric interpretation of the limit"
section_number: 4.2
pages: 26-29
source_pdf: 1002.0126v1.pdf
source_sha256: ea218a0586a13490
toc_source: outline
text_source: latex
latex_prose_ratio: 0.934
latex_coverage_ratio: 0.976
doc_brief: "AN INTRODUCTION TO THE VOLUME CONJECTURE — This is an introduction to the Volume Conjecture and its gener- alizations for nonexperts."
---
In this subsection I will give a geometric interpretation of the limit [\[eq:limit\]](#eq:limit){reference-type="eqref" reference="eq:limit"}.

Since $V(z_1,z_2,\dots,z_c)$ is the sum of the terms as in [\[eq:dilog\]](#eq:dilog){reference-type="eqref" reference="eq:dilog"}, we first describe a geometric meaning of $\operatorname{Li}_2(\zeta_N^{\pm i})$.

Recall that an ideal hyperbolic tetrahedron can be put in $\mathbb{H}^3$. Regarding the $xy$-plane as the complex plain, we can assume that the three of the four (ideal) vertices are at $0$, $1$ and $z\in\mathbb{C}$ ($\operatorname{Im}{z}>0$), respectively (Figure [1](#fig:tetrahedron_parameter){reference-type="ref" reference="fig:tetrahedron_parameter"}).

![Parametrization of ideal hyperbolic tetrahedra](tetrahedron_triangle_small.eps){#fig:tetrahedron_parameter}

Thus the set $\{z\in\mathbb{C}\mid\operatorname{Im}{z}>0\}$ gives a parametrization of ideal hyperbolic tetrahedra. We denote by $\Delta(z)$ the hyperbolic tetrahedron parametrized by $z$.

The volume of $\Delta(z)$ is given as follows (see for example [@Neumann/Zagier:TOPOL85 p. 324]): $$\label{eq:tetra_vol}
  \operatorname{Vol}(\Delta(z))
  =
  \operatorname{Im}\operatorname{Li}_2(z)+\log|z|\arg(1-z).$$

So we expect $V(x_1,x_2,\dots,x_c)$ gives the sum of the volumes of certain tetrahedra related to the knot.

In fact we can express the volume of the knot complement in terms of $V(z_1,z_2,\dots,z_c)$ [@D.Thurston:Grenoble; @Yokota:GTM02].

We follow [@D.Thurston:Grenoble] to describe this.

We decompose the knot complement into topological, truncated tetrahedra. To do this we put an octahedron at each positive crossing as in Figure [2](#fig:crossing_octa){reference-type="ref" reference="fig:crossing_octa"}, where $i$, $j$, $k$ and $l$ are labeling of the four arcs around the vertex.

<figure id="fig:crossing_octa">
<p><embed src="crossing_pos_ijkl_big_small.eps" /> <embed src="crossing_octa_small.eps" /></p>
<figcaption>An octahedron put at a crossing</figcaption>
</figure>

Then decompose the octahedron into five tetrahedra as in Figure [3](#fig:octa_tetra){reference-type="ref" reference="fig:octa_tetra"}, where the four of them are decorated with $\xi_N^i$, $\xi_N^{-j}$, $\xi_N^k$ and $\xi_N^{-l}$, respectively and the one in the center is decorated with $\xi_N^m$, where $m:=l-i=j-k$. Here each truncated tetrahedron is just a topological one with some decoration.

![decomposition of the octahedron into five tetrahedra](octa_small.eps){#fig:octa_tetra}

Now only two of the vertices are attached to the knot. We pull the two of the remaining four vertices to the top ($+\infty$) and the other two to the bottom ($-\infty$) as shown in Figure [4](#fig:octa_tetra_infinity){reference-type="ref" reference="fig:octa_tetra_infinity"}.

![Pull the vertices to $+\infty$ and $-\infty$.](crossing_octa_infinity_small.eps){#fig:octa_tetra_infinity}

We attach five tetrahedra to every crossing (if the crossing is negative, we change them appropriately) in this way. At each arc two faces meet, and we paste them together. Thus we have a decomposition of $S^3\setminus(K\cup\{+\infty,-\infty\})$. By deforming this decomposition a little we get a decomposition of $S^3\setminus{K}$ by (topological) truncated tetrahedra, decorated with complex numbers $\xi^{\pm i_k}_N$ (k=1,2,...,c).

Next we want to regard each tetrahedron as an ideal hyperbolic one.

Recall that when we approximate the summation in [\[eq:Jones_sum\]](#eq:Jones_sum){reference-type="eqref" reference="eq:Jones_sum"} by the integral in [\[eq:Jones_integral2\]](#eq:Jones_integral2){reference-type="eqref" reference="eq:Jones_integral2"} we replace $\xi_N^{i_k}$ with a complex variable $z_k$. Following this we replace the decoration $\xi_N^{i_k}$ for a tetrahedron with a complex number $z_k$. Then regard the tetrahedron decorated with $z_k$ as an ideal hyperbolic tetrahedron parametrized by $z_k$.

So far this is just formal parametrizations. We need to choose appropriate values for parameters so that the tetrahedra fit together to provide a complete hyperbolic structure to $S^3\setminus{K}$. To do this we choose $z_1,z_2,\dots,z_c$ so that:

-   Around each edge several tetrahedra meet. To make the knot complement hyperbolic, the sum of these dihedral angles should be $2\pi$,

-   Even if the knot complement is hyperbolic, the structure may not be complete. To make it complete, the parameters should be chosen as follows.

    Since we truncate the vertices of the tetrahedra, four small triangles appear at the places where the vertices were (see Figure [1](#fig:tetrahedron_parameter){reference-type="ref" reference="fig:tetrahedron_parameter"} for the triangle associated with the vertex at infinity). After pasting these triangles make a torus which can be regarded as the boundary of the regular neighborhood of the knot $K$. Each triangle has a similarity structure provided by the parameter $z_k$. We need to make this boundary torus Euclidean.

See [@Thurston:GT3M Chapter 4],[@Neumann/Zagier:TOPOL85 § 2] for more details.

Surprisingly these conditions are the same as the system of equations [\[eq:differential\]](#eq:differential){reference-type="eqref" reference="eq:differential"} that we used in the steepest descent method! Therefore we can expect that a solution $(x_1,x_2,\dots,x_c)$ to [\[eq:differential\]](#eq:differential){reference-type="eqref" reference="eq:differential"} gives the complete hyperbolic structure.

Then, what does $V(x_1,x_2,\dots,x_c)=2\pi\sqrt{-1}\lim_{N\to\infty}\log\bigl(J_N(K,\xi_N)\bigr)/N$ mean?

Recall the formula [\[eq:tetra_vol\]](#eq:tetra_vol){reference-type="eqref" reference="eq:tetra_vol"} and that $V(x_1,x_2,\dots,x_c)$ is a sum of dilogarithm functions and logarithm functions. Using these facts we can prove $$\operatorname{Im}{V(x_1,x_2,\dots,x_c)}
  =
  \operatorname{Vol}(S^3\setminus{K}),$$ that is, $$\operatorname{Im}
  \left(
    2\pi\sqrt{-1}\lim_{N\to\infty}\frac{\log\bigl(J_N(K,\xi_N)\bigr)}{N}
  \right)
  =
  \operatorname{Vol}(S^3\setminus{K}).$$ So we have proved $$2\pi\lim_{N\to\infty}\frac{\log|J_N(K,\xi_N)|}{N}
  =
  \operatorname{Vol}(S^3\setminus{K}),$$ which is the Volume Conjecture (Conjecture [\[conj:VC\]](#conj:VC){reference-type="ref" reference="conj:VC"}).
