---
doc_id: arxiv-1808.02836v2
doc_title: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds Introduction"
section_id: sec-002-12-minimal-ideal-triangulations-via-topology
section_title: "Minimal ideal triangulations via topology"
section_number: 1.2
pages: 2-3
source_pdf: 1808.02836v2.pdf
source_sha256: 0224a296253122a2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.995
doc_brief: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds Introduction — Previous work of the authors studies minimal triangulations of closed 3–manifolds using a characterisation of low"
---
In this paper, we are first concerned with the anatomy of a minimal ideal triangulation. In particular, in §[\[sec:anatomy\]](#sec:anatomy){reference-type="ref" reference="sec:anatomy"} we characterise edges of low degree, and analyse subcomplexes that we call *maximal layered $\partial$--punctured solid tori.* These are solid tori with a point missing on the boundary, and imbued with a special ideal triangulation. These subcomplexes were exhibited by Guéritaud and Schleimer [@Gueritaud-canonical-2010] in canonical decompositions of cusped hyperbolic 3--manifolds satisfying certain genericity hypotheses, and are thus a natural part of the structure of an ideal triangulation to analyse from a geometrical viewpoint. Our methods show that they also have an important topological role to play. In §[\[sec:normsurfs\]](#sec:normsurfs){reference-type="ref" reference="sec:normsurfs"} we describe normal surfaces representing $\mathbb{Z}_2$--homology classes in ideal triangulations. We use this in §[\[sec:quadsurfs\]](#sec:quadsurfs){reference-type="ref" reference="sec:quadsurfs"} to prove our main result Theorem [\[thm:sumofnorms\]](#thm:sumofnorms){reference-type="ref" reference="thm:sumofnorms"}, which is analogous to the main result of [@Jaco-Z2-2013]. Before we can state it, we need to introduce some extra definitions.

Let $M$ be a cusped hyperbolic 3--manifold, and let $S$ be an embedded closed surface representing a given $c \in H_2(M;\mathbb{Z}_2).$ We wish to emphasise that we do not work with $H_2(\overline{M}, \partial \overline{M} ;\mathbb{Z}_2).$ An analogue of Thurston's norm [@Thurston-norm-1986] is defined in [@Jaco-Z2-2013] as follows. If $S$ is connected, let $\chi_{-}(S) = \max \{ 0,-\chi(S)\},$ and otherwise let $$\chi_{-}(S) = \sum_{S_i\subset S} \max \{ 0,-\chi(S_i)\},$$ where the sum is taken over all connected components of $S.$ Note that $S_i$ is not necessarily orientable. Define: $$|| \ c \ || = \min \{ \chi_{-}(S) \mid [S]= c\}.$$ The surface $S$ representing a class $c \in H_2(M;\mathbb{Z}_2)$ is said to be *$\mathbb{Z}_2$--taut* if no component of $S$ is a sphere or torus and $\chi(S) = -|| \ c \ ||.$ Note that $M$ contains no projective plane or Klein bottle. As in [@Thurston-norm-1986], one observes that every component of a $\mathbb{Z}_2$--taut surface is non-separating and geometrically incompressible.

::: theorem
[]{#thm:sumofnorms label="thm:sumofnorms"} Let $\mathcal{T}$ be an ideal triangulation of the cusped hyperbolic $3$--manifold $M.$ If $H \le H_2 (M,\mathbb{Z}_2)$ is a rank $2$ subgroup, then $$|\mathcal{T}| \geq \sum \limits_{0 \neq c \in H} || \ c\ ||.$$ Moreover, in the case of equality the triangulation is minimal, each canonical normal representative of a non-zero element in $H\le H_2 (M,\mathbb{Z}_2)$ is taut and meets each tetrahedron in a quadrilateral disc, and the number of tetrahedra in the triangulation is even.
:::

As an application, we obtain the following statement.

::: theorem
[]{#thm:torusbundles label="thm:torusbundles"} Monodromy ideal triangulations of once-punctured torus bundles are minimal.
:::

Monodromy ideal triangulations of hyperbolic once-punctured torus bundles are described by Floyd and Hatcher [@Floyd-incompressible-1982] and attributed to Thurston. These triangulations are canonically determined by the monodromy of the bundle acting on the Farey graph; they are an early special case of Agol's veering triangulations. The fact that the monodromy ideal triangulation of each hyperbolic once-punctured torus bundle is canonical, and hence also geometric, is due to Akiyoshi [@Akiyoshi99CanonicityLayeredTorusBundles], Lackenby [@Lackenby-canonical-2003] and Guéritaud [@GueritaudPhDThesis].

Such a triangulation may contain edges of arbitrarily high degree, hence arbitrarily many ideal hyperbolic tetrahedra of arbitrarily small volume, a fact which is also highlighted by explicit upper bounds on the volume of torus bundles in [@Gueritaud-canonical-2006 Theorem B.1] and in [@Agol03SmallLargeGenus Corollary 2.4]. Thus, our family contains explicit minimal triangulations where the gap between complexity and volume can be arbitrarily large.

The monodromy ideal triangulation $\mathcal{T}$ of a hyperbolic once-punctured torus bundle $M$ with the property that $H_2(M,\mathbb{Z})$ contains a Klein 4--group $H$ satisfies the equality $$|\mathcal{T}| = \sum \limits_{0 \neq c \in H} || \ c\ ||.$$ There are other once-cusped hyperbolic 3--manifolds, for which this equality is achieved. These are not fibred, and are described in §[\[subsec:more examples\]](#subsec:more examples){reference-type="ref" reference="subsec:more examples"}. It remains an open problem to *classify all triangulations* for which the lower bound in Theorem [\[thm:sumofnorms\]](#thm:sumofnorms){reference-type="ref" reference="thm:sumofnorms"} is achieved. Such a classification is given in [@Jaco-Z2-2017] for our lower bound on the complexity for closed atoroidal 3--manifolds.
