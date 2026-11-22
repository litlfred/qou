---
doc_id: arxiv-math-0410233v4
doc_title: "CUSP SHAPES UNDER CONE DEFORMATION"
section_id: sec-003-12-cone-deformations
section_title: "Cone deformations"
section_number: 1.2
pages: 3-5
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.644
doc_brief: "CUSP SHAPES UNDER CONE DEFORMATION — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp shape."
---
Our primary technique is cone deformation, which we will now describe. Using properties of cone deformations, we obtain geometric information on the topological process of Dehn filling.

::: define
Given a manifold $M$ with torus boundary $\partial M$ and specified slope $s$ on $\partial M$, we obtain a new manifold by gluing a solid torus to $\partial M$ such that $s$ bounds a disk in the solid torus. This is called the *Dehn filling of $M$ along $s$*, or sometimes *Dehn surgery*, and the resulting manifold is denoted $M(s)$. More generally, if $M$ has $n$ torus boundary components with slopes $s_1, \dots, s_n$, then we obtain $M(s_1, \dots, s_n)$ in the same manner. []{#def:dehn label="def:dehn"}
:::

A geometric description of Dehn filling was investigated by Thurston [@thurston]. Given a complete hyperbolic structure on a manifold $M$ with torus boundary, he showed the structure could be deformed through incomplete hyperbolic structures with singularities at the core of the added solid torus to structures whose completion is again non-singular. These structures are exactly hyperbolic structures on Dehn filled manifolds $M(s)$. The space of deformations is called hyperbolic Dehn surgery space.

We restrict our attention to particular paths through hyperbolic Dehn surgery space in which the incomplete hyperbolic manifolds are all cone manifolds. That is, the completion gives a manifold with cone singularities along the core of the added solid torus, with cone angle $\alpha$. (A more complete definition of a cone deformation is given in Definition [\[def:cone-deform\]](#def:cone-deform){reference-type="ref" reference="def:cone-deform"} below.)

We have some control over cone deformations. Local rigidity results due to Hodgson and Kerckhoff [@hk:cone-rigid], extended by Bromberg in the case of geometrically finite manifolds [@bromberg:cone-rigid], give control on the change in geometry of the entire manifold, knowing only information on the change in a neighborhood of the singular locus.

This geometric control has been used recently to prove several interesting results in 3--manifold theory. Hodgson and Kerckhoff used it to give universal bounds on the number of exceptional Dehn surgery slopes for finite volume manifolds [@hk:univ]. In the infinite volume case, cone deformations lie at the heart of drilling and grafting theorems, described by Bromberg in [@bromberg:cone]. These have recently been used to resolve problems in the field of Kleinian groups, such as the Bers density conjecture [@brock-bromberg:density], and existence of type preserving sequences of Kleinian groups [@brock-bromberg-evans-souto:tame]. This paper gives another application of cone deformations, to finite volume manifolds with cusps.
