---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-010-43-angle-structure-equations
section_title: "Angle structure equations"
section_number: 4.3
pages: 17-18
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.919
latex_coverage_ratio: 0.877
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
[]{#sub.ge label="sub.ge"}

Recall the equations for a generalised angle structure as given in Definition [\[matrix equations\]](#matrix equations){reference-type="ref" reference="matrix equations"}. In this section, we will refer to the angle variables within the $i$th tetrahedron, $\alpha(q_i) ,\alpha(q_i'),\alpha(q_i'')$, as $Z_i,Z_i',Z_i''$ respectively.

We can view a quad-choice $Q$ for $\mathcal{T}$ (as in Definition [\[choice_of_quads\]](#choice_of_quads){reference-type="ref" reference="choice_of_quads"}) as a choice of pair of opposite edges at each tetrahedron $\Delta_i$ for $i=1,\dots,N$. The quad-choice $Q$ can be used to eliminate one of the three variables $Z_i,Z'_i,Z''_i$ at each tetrahedron using the relation $Z_i+Z'_i+Z''_i=\pi$. Doing so, equations [\[eq.angle1\]](#eq.angle1){reference-type="eqref" reference="eq.angle1"} take the form $$\mathbf A \, Z + \mathbf B \, Z'' = \pi \boldsymbol{\nu} \,,$$ where $\boldsymbol{\nu} \in \mathbb Z^{N}$. (For example, if we eliminate the variables $Z'_i$ then $\mathbf A = \overline{\mathbf A}-\overline{\mathbf B}$, $\mathbf B = \overline{\mathbf C}-\overline{\mathbf B}$ and $\boldsymbol{\nu} = 2 (1,\dots,1)^T - \overline{\mathbf B} (1,\dots,1)^T$.

The matrices $(\mathbf A|\mathbf B)$ have some key *symplectic properties*, discovered by Neumann-Zagier when $M$ is a hyperbolic 3-manifold (and $\mathcal{T}$ is well-adapted to the hyperbolic stucture) [@NZ], and later generalised to the case of arbitrary 3-manifolds in [@Neumann-combi]. Neumann-Zagier show that the rank of $(\mathbf A|\mathbf B)$ is $N-r$, where $r$ is the number of boundary components of $M$; all assumed to be tori.
