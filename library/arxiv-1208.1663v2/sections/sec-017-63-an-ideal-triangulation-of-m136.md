---
doc_id: arxiv-1208.1663v2
doc_title: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES"
section_id: sec-017-63-an-ideal-triangulation-of-m136
section_title: "An ideal triangulation of m136"
section_number: 6.3
pages: 21-21
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.936
latex_coverage_ratio: 1.0
doc_brief: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of ideal triangulations of 3-manifolds with r torii boundary"
---
[]{#sub.m136 label="sub.m136"}

Let $\mathcal T$ denote the ideal triangulation [@HRS Ex.7.7] of the 1-cusped census manifold `m136` using 7 tetrahedra. Its gluing equation matrices around the edges are given by:

$$\begin{aligned}
\bar{\mathbf A} &=\left(
\begin{array}{ccccccc}
 1 & 0 & 0 & 0 & 1 & 1 & 1 \\
 0 & 0 & 0 & 1 & 0 & 1 & 0 \\
 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
 0 & 1 & 1 & 1 & 0 & 0 & 1 \\
 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
 
 
\end{array}
\right), &
\bar{\mathbf B} &=
\left(
\begin{array}{ccccccc}
 0 & 0 & 0 & 1 & 0 & 0 & 1 \\
 1 & 0 & 0 & 0 & 1 & 0 & 0 \\
 0 & 1 & 1 & 1 & 1 & 1 & 0 \\
 1 & 0 & 0 & 0 & 0 & 0 & 1 \\
 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
 0 & 0 & 1 & 0 & 0 & 1 & 0 \\
 
 
\end{array}
\right), &
\bar{\mathbf C}&=
\left(
\begin{array}{ccccccc}
 1 & 0 & 0 & 1 & 0 & 1 & 1 \\
 0 & 0 & 0 & 0 & 1 & 1 & 0 \\
 1 & 2 & 0 & 1 & 0 & 0 & 0 \\
 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
 0 & 0 & 1 & 0 & 1 & 0 & 0 \\
 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
 
 
\end{array}
\right)
\end{aligned}$$

A generalized angle structure is a solution to Equations [\[eq.angle\]](#eq.angle){reference-type="eqref" reference="eq.angle"}.

In our example, the set of generalized angle structures $\mathrm{GA}(\mathcal T)$ is an affine $8$-dimensional subspace of $\mathbb R^{21}$ and the intersection $\mathrm{SA}(\mathcal T)=\mathrm{GA}(\mathcal T) \cap [0,\infty)^{21}$ is the polytope of semi-angle structures. `Regina` [@Bu] gives that $\mathrm{SA}(\mathcal T)$ is the convex hull of the following set of $11$ points $(\alpha_1,\beta_1,\gamma_1,\dots,\alpha_7,\beta_7,\gamma_7)$ in $\mathbb R^{21}$.

$$\left(
\begin{array}{ccc|ccc|ccc|ccc|ccc|ccc|ccc}
0 & 0 & 1 & 1 & 0 & 0 & 0 & 0 & 1 & 1 & 0 & 0 & 0 & 0 & 1 & 0 & 1 & 0 & 0 &
0 & 1 \\
0 & 1 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 1 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 & 1 & 0 & 0 
\\ 
1 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 & 1 & 0 & 0 & 0 & 0 & 1 & 0 & 1 & 0 & 0 & 1 & 0 
\\ 
1 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 1 & 0 & 0 & 0 & 1 
\\ 
1/2 & 1/2 & 0 & 1 & 0 & 0 & 0 & 1/2 & 1/2 & 1/2 & 1/2 & 0 & 0 & 0 & 1 & 0 & 1 & 0 & 1/2 & 0 & 1/2
\\ 
1/2 & 1/2 & 0 & 1 & 0 & 0 & 0 & 1/2 & 1/2 & 1/2 & 0 & 1/2 & 0 & 0 & 1 & 0 & 1 & 0 & 1/2 & 0 & 1/2
\\ 
1/2 & 1/2 & 0 & 1 & 0 & 0 & 1/2 & 0 & 1/2 & 1/2 & 1/2 & 0 & 0 & 0 & 1 & 0 & 1 & 0 & 0 & 0 & 1 
\\ 
1/2 & 1/2 & 0 & 1 & 0 & 0 & 1/2 & 0 & 1/2 & 1/2 & 0 & 1/2 & 0 & 0 & 1 & 0 & 1 & 0 & 0 & 0 & 1 
\\ 
1/2 & 1/2 & 0 & 1/2 & 0 & 1/2 & 0 & 0 & 1 & 1 & 0 & 0 & 1/2 & 0 & 1/2 & 0 & 1 & 0 & 1/2 & 0 & 1/2
\\ 
1/2 & 1/2 & 0 & 1/2 & 1/2 & 0 & 1/2 & 0 & 1/2 & 1 & 0 & 0 & 1/2 & 0 & 1/2 & 0 & 1 & 0 & 0 & 1/2 & 1/2
\\ 2/3 & 1/3 & 0 & 2/3 & 0 & 1/3 & 1/3 & 0 & 2/3 & 1 & 0 & 0 & 1/3 & 0 & 2/3 & 0 & 1 & 0 & 0 & 1/3 & 2/3
\end{array}
\right)$$ A computation shows that if $(\alpha,\beta,\gamma) \in \mathrm{SA}(\mathcal T)$, then $(a_6,b_6,c_6)=(t,1,-t)$ for some $t \in \mathbb R$ which explains why $\mathcal T$ has no strict angle structure. On the other hand, [@HRS Example 7.7] mention $\mathcal T$ has a solution $$(z_1,\dots,z_6)=\left(2 i,-1+2 i,\frac{3}{5}+\frac{1}{5}i,-1,
\frac{1}{5}+\frac{2}{5}i,2,\frac{1}{2}+\frac{1}{2}i \right)$$ of the gluing equations which recovers the complete hyperbolic structure on `m136`.
