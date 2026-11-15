---
doc_id: arxiv-1108.4389v1
doc_title: "Gauge Theories Labelled by Three-Manifolds"
section_id: sec-001-2-geometry-of-3-manifolds
section_title: "Geometry of 3-manifolds"
section_number: 2
pages: 8-9
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.83
latex_coverage_ratio: 1.0
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
[]{#sec:geom label="sec:geom"}

In this section, we discuss the geometric construction of oriented 3-manifolds $M$ from basic building blocks: ideal tetrahedra. Such "ideal triangulations" in three dimensions were initiated by Thurston [@thurston-1980]. More precisely, we wish to build 3-manifolds that support irreducible flat $SL(2,{\mathbb C})$ connections $\mathcal{A}$. For this purpose, it is often convenient to replace flat $SL(2,{\mathbb C})$ connections with hyperbolic metrics [^1]

on $M$ --- that is, metrics of constant curvature $-1$. Then the $SL(2,{\mathbb C})$ structures become geometric, and can be manipulated in a much more intuitive manner.

The 3-manifolds we consider have two different types of boundary, *geodesic boundaries* and *generalized cusps*. Geometrically, the geodesic boundaries are (possibly punctured) geodesic surfaces of any genus, and come with an induced 2-dimensional hyperbolic metric. Any triangulation of $M$ will determine a triangulation of the geodesic boundary, which will be part of the data in eventually defining a 3d gauge theory.

In contrast, "cusp" boundaries do not have a triangulation that is relevant in defining 3d gauge theories. Geometrically, cusps are knotted loci where the hyperbolic metric on $M$ develops a cone angle, or the $SL(2,{\mathbb C})$ connection has a specified monodromy defect. Such loci can be resolved to boundaries with the topology of either tori $T^2$ or annuli $S^1\times I$. In either case, the induced metric on cusp boundaries is Euclidean. Well-studied examples of 3-manifolds with torus cusps are knot complements in $S^3$. More generally, a cusp might begin and end at punctures on the geodesic boundary of $M$ (Figure [\[fig:bdies\]](#fig:bdies){reference-type="ref" reference="fig:bdies"}). Then, the resolved cusp has the topology of an annulus.

The total boundary of $M$, with potential components of both types, determines a boundary moduli space of flat connections,

$$\mathcal{P}_{\partial M} = \{\text{flat $SL(2,{\mathbb C})$ connections on $\partial M$}\}\big/(\text{gauge equivalence}). \label{PdM}$$

This is a symplectic phase space, with a natural holomorphic symplectic form

$$\omega_{\partial M} = \frac{1}{\hbar}\int_{\partial M}{\rm Tr \,}\big(\delta\mathcal{A}\wedge\delta\mathcal{A}\big)\,. \label{omegadM}$$

The semiclassical parameter $\hbar$ here governs the normalization of the symplectic form. Geometrically, $\omega_{\partial M}$ is an analytic continuation of the Weil-Petersson form in 2-dimensional hyperbolic geometry. In addition to the phase space $\mathcal{P}_{\partial M}$, we can also define a Lagrangian submanifold [@gukov-2003]

$$\mathcal{L}_M = \{\text{flat $SL(2,{\mathbb C})$ connections on M}\}\big/(\text{gauge})\quad\subset\quad \mathcal{P}_{\partial M}\,,$$

which is the set of flat connections on $\partial M$ that can be extended as flat connections inside the 3-dimensional bulk of $M$. Mathematically, $\mathcal{L}_M$ is described as the image of the "character variety" of $M$ inside the character variety of $\partial M$.

Our goal now is to construct a manifold $M$ together with the pair $(\mathcal{P}_{\partial M},\mathcal{L}_M)$ from ideal hyperbolic tetrahedra. This will give us an extremely explicit realization of boundary phase spaces, Lagrangians, and the symplectic structure [\[omegadM\]](#omegadM){reference-type="eqref" reference="omegadM"}, which in turn will enable us in Section [\[sec:glue\]](#sec:glue){reference-type="ref" reference="sec:glue"} to explicitly build the 3d gauge theory associated to $M$. As previewed in the introduction, this 3d theory will depend on $M$, a triangulation of its geodesic boundary, and a *polarization* $\Pi$ of its phase space $\mathcal{P}_{\partial M}$ --- with additional ingredients such as $\mathcal{L}_M$ playing roles like moduli spaces of vacua.

[^2]\

[^1]: The equivalence between flat connections and hyperbolic geometry results from the fact that the isometry group of hyperbolic three-space is $(P)SL(2,{\mathbb C})$, *cf.* [@thurston-1980; @Witten-gravCS; @gukov-2003; @DGLZ]. Almost all flat connections can be realized as (possibly degenerate) hyperbolic metrics; for further remarks on this in the context of ideal triangulations, see [@Champ-hypA; @Dunfield-Mahler], and Section 4 of [@Dimofte-QRS].

[^2]: We note that topologically, one might engineer (resolved) cusp boundaries that look identical to geodesic boundaries. In particular, networks of annular cusps can assume the topology of nontrivial punctured Riemann surfaces [@DGGV-hybrid]. Formally, the phase spaces $\mathcal{P}_{\partial M}$ associated to the two types of boundary would then be equivalent. However, the natural coordinate systems --- and in particular the polarizations --- for phase spaces on cusp and geodesic boundaries are very different. In turn, the 3d gauge theories associated to 3-manifolds with the two different types of boundary will be quite different.
