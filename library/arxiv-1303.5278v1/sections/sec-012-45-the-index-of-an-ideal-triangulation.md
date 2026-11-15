---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-012-45-the-index-of-an-ideal-triangulation
section_title: "The index of an ideal triangulation"
section_number: 4.5
pages: 19-20
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.907
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
[]{#sub.defn.index label="sub.defn.index"}

Suppose that $M$ is a 3-manifold whose boundary $\partial M$ consists of $r \ge 1$ tori $T_1, \ldots, T_r$, and let $\mathcal{T}$ be an ideal triangulation of $M$. Let $\varpi=(\varpi_1, \ldots, \varpi_r)$ be a collection of oriented peripheral curves as above. By Theorem [\[pick_edges\]](#pick_edges){reference-type="ref" reference="pick_edges"}, proved below, we can order the edges of $\mathcal{T}$ so that the first $N-r$ rows of the Neumann-Zagier matrix $(\mathbf A \mid \mathbf B)$ form an *integer basis* for its integer row space (i.e. the $\mathbb{Z}$-module of all linear combinations of its rows with integer coefficients). Then we define $$\label{eq.indT}
I_{\mathcal{T}}(\varpi)(q)=\sum_{\boldsymbol{k}\in \mathbb Z^{N-r}\subset \mathbb{Z}^N}
(-q^{\frac{1}{2}})^{\boldsymbol{k}\cdot \boldsymbol{\nu}+ \nu_{\varpi}} 
\prod_{j=1}^N I_{\Delta}(-b_{\varpi,j} - \boldsymbol{k}\cdot \boldsymbol{b}_j  , 
a_{\varpi,j} +\boldsymbol{k}\cdot \boldsymbol{a}_j  ) \,.$$ where $\boldsymbol{a}_j$ and $\boldsymbol{b}_j$ for $j=1,\dots, N$ denote the columns of $\mathbf A$ and $\mathbf B$, and $$\mathbb{Z}^{N-r} = \left\{  (k_1, \ldots, k_N) \in \mathbb{Z}^N : k_j=0 \text{ for } j > N-r \right\} .$$

It can be checked that this definition is independent of the quad choice involved in forming $(\mathbf A \mid \mathbf B)$; see [\[JD_index_eq\]](#JD_index_eq){reference-type="eqref" reference="JD_index_eq"}. It is also independent of the choice of $N-r$ edges used to produce an integer basis for the integer row space of the Neumann-Zagier matrix, by Remark [\[basis_indept\]](#basis_indept){reference-type="ref" reference="basis_indept"}. In the case of a 1-cusped manifold $M$, any $N-1$ edges can be used; in other words we could replace the domain of summation $\mathbb{Z}^{N-1}$ by any of the coordinate hyperplanes $\left\{ (k_1, \ldots, k_N) \in \mathbb{Z}^N : k_s=0 \right\}$ with $s \in \{1, \ldots, N \}$. In general, we choose a set $\mathcal B$ of $N-r$ *basic edges* whose corresponding rows we sum over, for example by using Theorem [\[pick_edges\]](#pick_edges){reference-type="ref" reference="pick_edges"}. Equivalently, we choose the complementary set $\mathcal X$ of *excluded edges*.

Theorem [\[index_isotopy_invariance\]](#index_isotopy_invariance){reference-type="ref" reference="index_isotopy_invariance"} below shows that the index is unchanged by an isotopy of $\varpi$ so only depends on the homology class $$[\varpi]=\left[ \sum \varpi_i\right]  \in H_1(\partial M; \mathbb{Z}) = \bigoplus_{i=1}^N  H_1(T_i;\mathbb{Z}).$$ So the index gives a well-defined function $$I_{\mathcal{T}}: H_1(\partial M;\mathbb Z) \longrightarrow\mathbb Z((q^{1/2})) \text{ where } I_{\mathcal{T}}([\varpi])=I_{\mathcal{T}}(\varpi).$$

If $M$ is a 1-cusped manifold $M$, and $\mu$ and $\lambda$ in $H_1(\partial M;\mathbb{Z})$ are a fixed oriented meridian and longitude on $\partial M$ (a canonical choice exists when $M$ is the complement of an oriented knot in $S^3$). Then we can write $$\label{eq.varpiem}
[\varpi]=-m \lambda + e \mu$$ for integers $e,m$. The naming of the integers $e$ and $m$ (electric and magnetic charge) and the above choice of signs was chosen to make our index compatible with the definition of [@DGG2] and [@Ga:index].
