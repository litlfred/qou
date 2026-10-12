---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-004-2-definitions
section_title: "Definitions"
section_number: 2
pages: 6-9
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.853
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
[]{#sec.definitions label="sec.definitions"}

::: defn
Let $M$ be an orientable topologically finite 3-manifold which is the interior of a compact 3-manifold with torus boundary components. An *ideal triangulation* $\mathcal{T}$ of $M$ consists of a pairwise disjoint union of standard Euclidean 3--simplices, $\widetilde{\Delta} = \cup_{k=1}^{n} \widetilde{\Delta}_k,$ together with a collection $\Phi$ of Euclidean isometries between the 2--simplices in $\widetilde{\Delta},$ called *face pairings*, such that the quotient space $(\widetilde{\Delta} \setminus \widetilde{\Delta}^{(0)} )/ \Phi$ is homeomorphic to $M.$ The images of the simplices in $\mathcal{T}$ may be singular in $M$.
:::

::: defn
Let $\mathcal{T}$ be an ideal triangulation with at least 2 distinct tetrahedra. A *2--3 move* can be performed on any pair of distinct tetrahedra of $\mathcal{T}$ that share a triangular face $t$. We remove $t$ and the two tetrahedra, and replace them with three tetrahedra arranged around a new edge, which has endpoints the two vertices not on $t$. See Figure [\[2-3\]](#2-3){reference-type="ref" reference="2-3"}. A *3--2 move* is the reverse of a 2--3 move, and can be performed on any triangulation with a degree 3 edge, where the three tetrahedra incident to that edge are distinct.
:::

::: defn
Let $\mathcal{T}$ be an ideal triangulation. A *0--2 move* can be performed on any pair of distinct triangular faces of $\mathcal{T}$ that share an edge $e$[^1]. Around the edge $e$, the tetrahedra of $\mathcal{T}$ are arranged in a cyclic sequence, which we call a *book of tetrahedra*. (Note that tetrahedra may appear more than once in the book.) The two triangles and $e$ separate the book into two *half--books*. We unglue the tetrahedra that are identified across the two triangles, duplicating the triangles and also duplicating $e$. We glue into the resulting hole a pair of tetrahedra glued to each other in such a way that there is a degree 2 edge between them. See Figure [\[0-2\]](#0-2){reference-type="ref" reference="0-2"}. A *2--0 move* is the reverse of a 0--2 move, and can be performed on any triangulation with a degree 2 edge, where the two tetrahedra incident to that edge are distinct, there are no face pairings between the four external faces of the two tetrahedra, and the two edges opposite the degree 2 edge are not identified.
:::

<figure id="2-3 and 0-2 moves" data-latex-placement="htb">

<figcaption>Moves on (topological) triangulations.</figcaption>
</figure>

::: rmk
A 0--2 move is also called a *lune* move in the dual language of standard spines [@Ma1; @Ma2; @Pi; @BP]. In [@Ma1 Lem.2.1.11] and [@Pi] (see also [@Petronio:thesis Prop.I.1.13]) it was shown that a 0--2 move follows from a combination of 2--3 moves as long as the initial triangulation has at least $2$ ideal tetrahedra.
:::

::: defn
Let $\Delta^3$ be the standard 3--simplex with a chosen orientation. Each pair of opposite edges corresponds to a normal isotopy class of quadrilateral discs in $\Delta^3,$ disjoint from the pair of edges. We call such an isotopy class a *normal quadrilateral type*. Each vertex of $\Delta^3$ corresponds to a normal isotopy class of triangular discs in $\Delta^3,$ disjoint from the face of $\Delta^3$ opposite the vertex. We call such an isotopy class a *normal triangle type*. Let $\mathcal{T}^{(k)}$ be the set of all $k$--simplices in $\mathcal{T}$. If $\sigma \in \mathcal{T}^{(3)},$ then there is an orientation preserving map $\Delta^3 \to \sigma$ taking the $k$--simplices in $\Delta^3$ to elements of $\mathcal{T}^{(k)},$ and which is a bijection between the sets of normal quadrilateral and triangle types in $\Delta^3$ and in $\sigma$. Let $\square$ and $\triangle$ denote the sets of all normal quadrilateral and triangle types in $\mathcal{T}$ respectively.
:::

::: defn
Given a $3$-manifold $M$ with an ideal triangulation $\mathcal{T}$, the *normal surface solution space* $C(M; \mathcal{T})$ is a vector subspace of $\mathbb{R}^{7n},$ where $n$ is the number of tetrahedra in $\mathcal{T}$, consisting of vectors satisfying the *compatibility equations* of normal surface theory. The coordinates of $x \in \mathbb{R}^{7n}$ represent weights of the four normal triangle types and the three normal quadrilateral types in each tetrahedron, and the compatibility equations state that normal triangles and quadrilaterals have to meet the 2--simplices of $\mathcal{T}$ with compatible weights.

A vector in $\mathbb{R}^{7n}$ is called *admissible* if at most one quadrilateral coordinate from each tetrahedron is non-zero and all coordinates are non-negative. An integral admissible element of $C(M; \mathcal{T})$ corresponds to a unique embedded, closed *normal surface* in $(M,\mathcal{T})$ and vice versa.
:::

::: defn
(See [@JR], [@KR2]) An ideal triangulation $\mathcal{T}$ of an orientable $3$-manifold is *0-efficient* if there are no embedded normal 2-spheres or one-sided projective planes. An ideal triangulation $\mathcal{T}$ is *1-efficient* if it is 0-efficient, the only embedded normal tori are vertex-linking and there are no embedded one-sided normal Klein bottles. An ideal triangulation $\mathcal{T}$ is *strongly 1-efficient* if there are no immersed normal 2--spheres, projective planes or Klein bottles and the only immersed normal tori are coverings of the vertex-linking tori.
:::

Note that in some contexts, "atoroidal" is taken to mean that there is no immersed torus whose fundamental group injects into the fundamental group of the 3--manifold. In our context, we mean that there are no embedded incompressible tori or Klein bottles, other than tori isotopic to boundary components. In Corollary [\[atoroidal=\>1-efficient\]](#atoroidal=>1-efficient){reference-type="ref" reference="atoroidal=>1-efficient"} and Remark [\[small SFS lifted may not have index structure\]](#small SFS lifted may not have index structure){reference-type="ref" reference="small SFS lifted may not have index structure"} we highlight this distinction.

Note that if $M$ is orientable, it is sufficient to consider only normal 2-spheres and tori, except in the special case that $M$ is a twisted $I$-bundle over a Klein bottle. For any embedded normal projective plane or Klein bottle must be one-sided, so the boundary of a small regular neighbourhood is a normal 2-sphere or torus. However in the non-orientable case, one must consider two-sided projective planes and Klein bottles. In this paper we will consider only the orientable case.

::: defn
If $e\in \mathcal{T}^{(1)}$ is any edge, then there is a sequence $(q_{n_1}, ..., q_{n_k})$ of normal quadrilateral types facing $e,$ which consists of all normal quadrilateral types dual to $e$ listed in sequence as one travels around $e.$ Then $k$ equals the degree of $e,$ and a normal quadrilateral type may appear at most twice in the sequence. This sequence is called the *normal quadrilateral type sequence* for $e$ and is well-defined up to cyclic permutations and reversing the order.
:::

::: defn
[]{#angle structures label="angle structures"} A function $\alpha\colon\thinspace\square \to \mathbb{R}$ is called a *generalised angle structure on $(M,\mathcal{T})$* if it satisfies the following two properties:

1.  If $\sigma^3 \in \mathcal{T}^{(3)}$ and $q, q', q''$ are the three normal quadrilateral types supported by it, then $$\begin{equation*}
       \alpha(q) + \alpha(q') + \alpha(q'') =\pi.
    \end{equation*}$$

2.  If $e\in \mathcal{T}^{(1)}$ is any edge and $(q_{n_1}, ..., q_{n_k})$ is its normal quadrilateral type sequence, then $$\begin{equation*}
    \sum_{i=1}^k \alpha(q_{n_i})  =2\pi.
    \end{equation*}$$
:::

Dually, one can regard $\alpha$ as assigning angles $\alpha(q)$ to the two edges opposite $q$ in the tetrahedron containing $q$. The triangulations we consider are of oriented manifolds, so we may assume that the triangulation is also oriented. We fix an ordering $q\rightarrow q' \rightarrow q'' \rightarrow q$ on these quad types, well defined up to cyclic permutation. See Figure [2](#quad_types){reference-type="ref" reference="quad_types"}.\

<figure id="quad_types" data-latex-placement="htbp">
<p><span class="math inline"><em>q</em></span> at 135 20 <span class="math inline"><em>q</em><sup>′</sup></span> at 430 20 <span class="math inline"><em>q</em><sup>″</sup></span> at 725 20 <img src="draws_eps/quad_types" style="width:60.0%" alt="image" /></p>
<figcaption>The three quad types within an oriented tetrahedron, arranged in our chosen cyclic order.</figcaption>
</figure>

::: defn
If we restrict the angles of a generalised angle structure to be in

- $[0,\pi]$, then the generalised angle structure is a *semi-angle structure*.

- $(0,\pi)$, then the generalised angle structure is a *strict angle structure*.

- $\{0,\pi\}$, then the generalised angle structure is a *taut angle structure*.

The set of generalised angle structures is denoted by $\mathrm{GA}(\mathcal{T})$ and is an affine subspace of $\mathbb{R}^{3N}$, where $N$ is the number of tetrahedra in $\mathcal{T}$. The subset of semi-angle structures is denoted by $\mathrm{SA}(\mathcal{T})$, and is a closed polytope in $\mathrm{GA}(\mathcal{T})$.
:::

::: rmk
It is easy to see that a taut angle structure can only happen if every tetrahedron has a pair of opposite edges with angles $\pi$ and the other four edges have angles $0$.
:::

::: defn
[]{#choice_of_quads label="choice_of_quads"} For an ideal triangulation $\mathcal{T}$ with $N$ tetrahedra, a *quad-choice* is an element $Q=(Q_1, \ldots, Q_N) \in \square^N$ such that $Q_n$ is a choice of one of the three quad types in the $n$th tetrahedron. An *index structure* $\alpha$ on $\mathcal{T}$ consists of $3^N$ generalised angle structures, indexed by the quad-choices $Q$, with the property that $\alpha_Q(Q_n)>0$ for $n=1,\ldots,N$, for each quad-choice $Q.$
:::

::: defn
[]{#matrix equations label="matrix equations"} The equations determining a generalised angle structure can be read off as three $N\times N$ matrices $\overline{\mathbf A}=(\bar a_{ij})$, $\overline{\mathbf B}=(\bar b_{ij})$ and $\overline{\mathbf C}=(\bar c_{ij})$ whose rows are indexed by the $N$ edges of $\mathcal{T}$ and whose columns are indexed by the $\alpha(q_j) ,\alpha(q_j'),\alpha(q_j'')$ variables respectively, where $q_j, q_j', q_j''$ are the quads type in the $j$th tetrahedron. These are the so-called *Neumann-Zagier matrices* that encode the exponents of the *gluing equations* of $\mathcal{T}$, originally introduced by Thurston [@NZ; @Th]. In terms of these matrices, a generalised angle structure is a triple of vectors $Z, Z',  Z''  \in \mathbb R^N$ that satisfy the equations $$\begin{equation}
\label{eq.angle1}
\overline{\mathbf A} \, Z + \overline{\mathbf B} \, Z' 
+ \overline{\mathbf C} \, Z'' = 2 \pi (1,\dots,1)^T,  \qquad   Z+Z'+Z''=\pi (1,\dots,1)^T \,.
\end{equation}$$ Note that the matrix entries $\bar a_{ij},\bar b_{ij},\bar c_{ij}$ give the coefficients of $Z_j,Z'_j,Z''_j$ in the $i$th edge equation corresponding to the edges of tetrahedron $j$ facing quad types $q_j,q'_j,q''_j$ respectively.

We can combine these into a single matrix equation $$\begin{equation}
\label{full_matrix_eqn}
\begin{pmatrix} \overline{\mathbf A} & \overline{\mathbf B} & \overline{\mathbf C} \\ 
\mathbf I_N & \mathbf I_N & \mathbf I_N 
\end{pmatrix} \begin{pmatrix}Z \\ 
Z'\\
Z'' 
\end{pmatrix} = 
\begin{pmatrix} 2 \pi (1,\dots,1)^T \\ \pi (1,\dots,1)^T \end{pmatrix},
\end{equation}$$ where $\mathbf I_N$ is the $N\times N$ identity matrix. We call this matrix equation *the matrix form of the generalised angle structure equations*.
:::

[^1]: Unlike for the 2--3 move, it is possible to make sense of the 0--2 move when the two triangles are not distinct. However, we will not make use of this variant in this paper.
