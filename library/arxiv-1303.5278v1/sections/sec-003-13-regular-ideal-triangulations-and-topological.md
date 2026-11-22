---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-003-13-regular-ideal-triangulations-and-topological
section_title: "Regular ideal triangulations and topological invariance"
section_number: 1.3
pages: 4-5
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.991
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
[]{#sub.regular label="sub.regular"}

In view of Remark [\[rem.1\]](#rem.1){reference-type="ref" reference="rem.1"}, we restrict our attention to hyperbolic 3-manifolds $M$ with at least one cusp. All we need is a canonical set $\mathcal X_M$ of $1$--efficient ideal triangulations of $M$ such that any two of these triangulations are related by moves that preserve $I_{\mathcal{T}}$. From Theorem [\[thm.00\]](#thm.00){reference-type="ref" reference="thm.00"}, we know that we can use 2--3 and 3--2 moves for this purpose. Given the choice we will make for $\mathcal X_M$ below, it turns out that we will also need to use 0--2 and 2--0 moves to connect together the triangulations of $\mathcal X_M$. Using the dual language of special spines, it is shown in [@Ma2 Lem.2.1.11] and [@Pi] (see also [@Petronio:thesis Prop.I.1.13]) that the 0--2 and 2--0 moves can be derived from the 2--3 and 3--2 moves, as long as the triangulation has at least two tetrahedra. However, the required sequence of 2--3 and 3--2 moves takes us out of our set $\mathcal X_M$, and it is not clear that the triangulations the sequence passes through are 1--efficient.

Every cusped hyperbolic 3--manifold $M$ has a canonical *cell decomposition* [@EP] where the cells are convex ideal polyhedra in $\mathbb H^3$. The cells can be triangulated into ideal tetrahedra, with layered flat tetrahedra inserted to form a bridge between two polyhedron faces that are supposed to be glued to each other but whose induced triangulations do not match. Unfortunately, it is not known whether any two triangulations of a 3-dimensional polyhedron are related by 2--3 and 3--2 moves; the corresponding result trivially holds in dimension 2 and nontrivially fails in dimension $5$; [@DeLoera:book; @Santos:ICM]. Nonetheless, it was shown by Gelfand-Kapranov-Zelevinsky that any two *regular* triangulations of a polytope in $\mathbb R^n$ are related by a sequence of geometric bistellar flips; [@GKZ]. Using the Klein model of $\mathbb H^3$, we define the notion of a *regular ideal triangulation* of an ideal polyhedron and observe that every two regular ideal triangulations are related by a sequence of geometric 2--2, 2--3 and 3--2 moves. Our set $\mathcal X_M^{\mathrm{EP}}$ of ideal triangulations of a cusped hyperbolic manifold $M$ consists of all possible choices of regular triangulation for each ideal polyhedron, together with all possible "bridge regions" of layered flat tetrahedra joining the induced triangulations of each identified pair of polyhedron faces. From the geometric structure of the cell decomposition, we obtain a natural semi-angle structure on each triangulation of $\mathcal X_M^{\mathrm{EP}}$, which shows that they are all 1-efficient by Theorem [\[semi-angle =\> 1-efficient\]](#semi-angle => 1-efficient){reference-type="ref" reference="semi-angle => 1-efficient"}, and so the 3D index is defined for each triangulation by Theorems [\[thm.00\]](#thm.00){reference-type="ref" reference="thm.00"}(a) and [\[index_structure_iff_1-efficient\]](#index_structure_iff_1-efficient){reference-type="ref" reference="index_structure_iff_1-efficient"}. We show that any two of these triangulations are related to each other by a sequence of 2--3, 3--2, 0--2 and 2--0 moves through 1--efficient triangulations, the moves all preserving the 3D index, using Theorems [\[thm.00\]](#thm.00){reference-type="ref" reference="thm.00"}(b), [\[index_structure_iff_1-efficient\]](#index_structure_iff_1-efficient){reference-type="ref" reference="index_structure_iff_1-efficient"} and [\[thm.20move.index\]](#thm.20move.index){reference-type="ref" reference="thm.20move.index"}. (The intermediate triangulations are mostly also within $\mathcal X_M^{\mathrm{EP}}$, although we sometimes have to venture outside of the set briefly.) Therefore we obtain a topological invariant of cusped hyperbolic 3--manifolds $M$.

::: thm
[]{#thm.2 label="thm.2"} If $M$ is a cusped hyperbolic 3-manifold, and $\mathcal{T}\in \mathcal X_M^{\mathrm{EP}}$ we have $I_M:=I_{\mathcal{T}}$ is well-defined.
:::

The next theorem is of independent interest, and may be useful for the problem of contructing topological invariants of cusped hyperbolic 3-manifolds. For a definition of the gluing equations of an ideal triangulation, see [@NZ; @Th] and also Section [\[sub.ge\]](#sub.ge){reference-type="ref" reference="sub.ge"} below.

::: thm
[]{#thm.3 label="thm.3"} Fix a cusped hyperbolic 3-manifold $M$. (a) For every $\mathcal{T}\in \mathcal X_M^{\mathrm{EP}}$, there exists a solution $Z_{\mathcal{T}}$ to the gluing equations of $\mathcal{T}$ which recovers the complete hyperbolic structure on $M$. Moreover, all shapes of $Z_{\mathcal{T}}$ have non-negative imaginary part. (b) If $\mathcal{T}, \mathcal{T}' \in \mathcal X_M^{\mathrm{EP}}$ are related by 2--3, 3--2, 0--2 and 2--0 moves, then so are $Z_{\mathcal{T}}$ and $Z_{\mathcal{T}'}$. (c) For every $\mathcal{T}$, the arguments of $Z_{\mathcal{T}}$ give a semi-angle structure on $\mathcal{T}$.
:::

::: rmk
[]{#rmk.5 label="rmk.5"} In [@HRS], it is shown that a cusped hyperbolic 3--manifold $M$ admits an ideal triangulation with strict angle structure if $H_1(M, \partial M;\mathbb Z_2)=0$. All link complements in the 3--sphere satisfy this condition. Such triangulations admit index structures but it is not known if they can be connected by 2--3 and 0--2 moves within the class of 1--efficient triangulations.
:::

::: rmk
[]{#rmk.XEPM label="rmk.XEPM"} For a typical cusped hyperbolic manifold, one expects that the Epstein-Penner ideal cell decomposition consists of ideal tetrahedra, i.e., that $\mathcal X_M^{\mathrm{EP}}$ consists of one element. Many examples of such cusped hyperbolic manifolds appear in the census [@SnapPy] and also in [@Akiyoshi; @GS].
:::

::: rmk
In a later paper we will extend this work in the following ways:

-   extend the domain of the 3D index $I_\mathcal{T}([\varpi])$ to $[\varpi]\in H_1(\partial M; \frac{1}{2}\mathbb{Z})$ such that $2[\varpi] \in\mathrm{Ker}(H_1(\partial M; \mathbb{Z}) \to H_1(M; \mathbb{Z}/2\mathbb{Z}))$,

-   give a definition of the 3D index using singular normal surfaces in $M$.
:::

::: rmk
Theorem [\[thm.2\]](#thm.2){reference-type="ref" reference="thm.2"} constructs a family of $q$-series $I_M([\varpi])(q)$ (parametrized by $[\varpi] \in H_1(\partial M,\mathbb Z)$) associated to a cusped hyperbolic manifold $M$. When $M = S^3 \setminus K$ is the complement of a knot $K$, we can choose $[\varpi]=\mu$ to be the homology class of the meridian and consider the series $$\label{eq.indtotal}
I^{\mathrm{tot}}_K(q)=\sum_{e \in \mathbb Z} I_M(e \mu)(q)$$ Since the semi-angle structures of Theorem [\[thm.3\]](#thm.3){reference-type="ref" reference="thm.3"} have zero holonomy at all peripheral curves, it can be shown that $I^{\mathrm{tot}}_K(q)$ is well-defined. It turns out that $I^{\mathrm{tot}}_K(q)$ is closely related to the state-integral invariants of Andersen-Kashaev and Kashaev-Luo-Vartanov [@AK; @KLV]. The relation between state-integrals of the quantum dilogarithm and $q$-series is explained in detail in [@GK]. An empirical study of the asymptotics of the series $I^{\mathrm{tot}}_{4_1}(q)$ is given in [@GZ].
:::
