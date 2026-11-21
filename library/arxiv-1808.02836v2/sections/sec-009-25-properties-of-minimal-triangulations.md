---
doc_id: arxiv-1808.02836v2
doc_title: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds Introduction"
section_id: sec-009-25-properties-of-minimal-triangulations
section_title: "Properties of minimal triangulations"
section_number: 2.5
pages: 6-7
source_pdf: 1808.02836v2.pdf
source_sha256: 0224a296253122a2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.994
doc_brief: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds Introduction — Previous work of the authors studies minimal triangulations of closed 3–manifolds using a characterisation of low"
---
An ideal triangulation of a topologically finite 3--manifold $M$ is *minimal* if it uses the smallest number of simplices in an ideal triangulation of $M.$ The number of ideal simplices in a minimal ideal triangulation of $M$ is denoted $c(M)$ and termed the *complexity* of $M.$

We assume that the reader is familiar with normal surface theory. We refer to [@Tillmann-normal-2008] for a thorough introduction, but remark that we only need to study *closed* normal surfaces in ideal triangulations.

An ideal triangulation of $M$ is *0--efficient* if no normal surface is a 2--sphere. An ideal triangulation of $M$ is *$\partial$--efficient* if it has the property that any closed normal surface that is isotopic to a vertex linking surface is *normally isotopic* to that vertex-linking surface. A normal isotopy is an isotopy of $M$ that preserves each simplex of each dimension.

::: theorem
[]{#lem:bdEfficient label="lem:bdEfficient"} Suppose $M$ is the interior of a compact, irreducible, $\partial$--irreducible anannular 3--manifold. Then each minimal ideal triangulation of $M$ is 0--efficient and $\partial$--efficient.
:::

::: proof
*Proof.* It is shown in [@Jaco-0-efficient-2003 Corollary 7.3] that each minimal triangulation of $M$ is 0--efficient. In [@Jaco-annular-2011 Theorem 4.7], the existence of a $\partial$--efficient triangulation is proven by a crushing method. Since crushing reduces the number of tetrahedra, this means that a triangulation that fails to be $\partial$--efficient is not minimal. ◻
:::

We now give a definition of what we mean by an ideal edge to be homotopic or isotopic *into the boundary*. The key is that intermediate paths in the homotopy are not allowed to pass through the ideal vertices, except for their endpoints. The reader is reminded than an ideal edge of $M$ is an edge of $\widehat{M}.$ An expanded discussion of the following material can be found in [@Hodgson-triangulations-2015].

A path homotopy (resp. isotopy)[^1] $H\co [0,1] \times [0,1]\to \widehat{M}$ between two edge paths is *admissible* if $H(\; (0,1)\times [0,1]\;) \subset M,$ where the first factor parametrises the paths. The edge path $\gamma$ is *admissibly null-homotopic (resp. null-isotopic)* if there is a path homotopy (resp. isotopy) $H\co [0,1] \times [0,1]\to \widehat{M}$ with $H(x, 0) = \gamma(x),$ $H(x, 1) = \gamma(0)$ for all $x\in [0,1]$ and $H(\; (0,1)\times [0,1)\;) \subset M.$

We say that an ideal edge $e$ of $M$ is *homotopic (resp. isotopic) into the boundary* if it is admissibly null-homotopic (resp. null-isotopic) in $\widehat{M}.$

::: corollary
[]{#cor-min-bddry-eff label="cor-min-bddry-eff"} Suppose $M$ is the interior of a compact, irreducible, $\partial$--irreducible anannular 3--manifold other than a 3--ball, and $\mathcal{T}$ is a minimal ideal triangulation of $M.$ Then no ideal edge is isotopic into the boundary. In particular, no edge in $\widehat{M}$ bounds an embedded disc in $\widehat{M}.$
:::

::: proof
*Proof.* Suppose the edge $e$ is isotopic into the boundary. Choose a compact core $M^c$ of $M$ with the property that each boundary component of $M^c$ is a vertex linking surface. There exists an embedded disc $D$ in $M^c$ whose boundary consists of $e \cap M^c$ and a subarc on a boundary component $B$ of $M^c.$ The boundary of a regular neighbourhood of $B\cup D$ has two components; one is a vertex linking surface normally isotopic to $B$ and the other is a surface $S$ isotopic to $B$ and disjoint from $e.$ Since $S$ is incompressible and not a 2--sphere and $M$ is irreducible, it follows that there is a normal surface isotopic but not normally isotopic to $B.$ Since the triangulation is $\partial$--efficient according to Theorem [\[lem:bdEfficient\]](#lem:bdEfficient){reference-type="ref" reference="lem:bdEfficient"}, it follows that $M$ is homeomorphic with $S \times (0,1).$ However, this contradicts our topological hypotheses on $M.$ ◻
:::

Note that the above result does not apply to the unique minimal ideal triangulation $\mathcal{T}$ of the 3--ball. This is the 1--tetrahedron, 1--vertex triangulation of $S^3$ with the vertex removed. The triangulation of $S^3$ has precisely two edges; one is a trefoil knot in $S^3$ and the other the unknot in $S^3.$ The former gives an ideal edge in $\mathcal{T}$ that is only homotopic into the boundary, whilst the latter is isotopic into the boundary. The above proofs breaks down for the 3--ball because the surface $S$ in the proof shrinks to a sphere contained in a tetrahedron.

We now specialise to the class of manifolds of interest, namely cusped hyperbolic 3--manifolds, where more specific results can be shown about their minimal triangulations. In order to limit the cases to consider, we not only assume that all *vertex links are of Euler characteristic zero*, but also that the manifolds are *orientable*.

[^1]: i.e. a homotopy (resp. isotopy) keeping endpoints fixed
