---
doc_id: arxiv-2404.19155v2
doc_title: "Octahedral coordinates from the Wirtinger presentation"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 2-4
source_pdf: 2404.19155v2.pdf
source_sha256: 45b9ed90006536b3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.896
latex_coverage_ratio: 0.893
doc_brief: "Octahedral coordinates from the Wirtinger presentation — Let ρ be a representation of a knot group (or more generally, the funda- mental group of a tangle complement) into SL2(C) expressed in terms"
---
Studying representations of knot and $3$-manifold groups into $\slg$ is important in low-dimensional topology. The isometry group of hyperbolic $3$-space is $\pslg$, so this problem is closely related to the study of hyperbolic structures [@ThurstonNotes]. While one can study representations algebraically, say via the Wirtinger presentation of the knot group, it is sometimes better to work more geometrically. For example, for geometric invariants like the hyperbolic volume it is usually better to work with the geometric parameters of an ideal triangulation of the knot complement than directly with $\rho$.

In this paper we are concerned with a particular family of ideal triangulations adapted to knot diagrams. Given a diagram $D$ of a knot $K$ the decomposes $S^3 \setminus K$ minus two points into a union of octahedra, with one for each crossing of the diagram. By further subdividing into tetrahedra one can obtain an ideal triangulation of a standard form. This works just as well for links and tangles. The geometric data of the tetrahedra are naturally described by ; these are implicit in work of @Yokota2000 [@Yokota2000] and have been studied systematically by @Kim2016 [@Kim2016; @Kim2018]. When studying geometric properties of a representation the octahedral coordinates are quite useful; for example, they enable a direct computation of the hyperbolic volume and Chern-Simons invariant [@Cho2013]. Our version of these coordinates is motivated by connections to the representation theory of quantum groups [@McPhailSnyder2022; @McPhailSnyderAlgebra].

While the octahedral coordinates are geometrically natural they can be difficult to solve for in practice. Instead we might find representations of the knot group by some other method and then try to find the corresponding octahedral coordinates. Given a representation $\rho : \pi_1(S^3 \setminus K) \to \slg$ described by its values on Wirtinger generators one can use the methods of @Blanchet2018 [@Blanchet2018] to find octahedral coordinates corresponding to $\rho$. This gives a somewhat complicated inductive method that does not usually produce simple formulas. In addition, some representations do not come from octahedral coordinates (one might have to conjugate first) and there is not a simple way to check when this occurs.

In this paper we give an elementary method ([\[def:associated-octahedral,thm:holonomies-match\]](#def:associated-octahedral,thm:holonomies-match){reference-type="ref" reference="def:associated-octahedral,thm:holonomies-match"}) for determining the octahedral coordinates of a tangle diagram directly from $\rho$. As an application we give an explicit criterion ([\[thm:detection-condition\]](#thm:detection-condition){reference-type="ref" reference="thm:detection-condition"}) for whether a representation corresponds to a smooth critical point of the potential function of a knot diagram $D$; this question is relevant to the saddle-point method used in most approaches to the Volume Conjecture. Our characterization depends only on $\rho$ and $D$, not the details of the triangulation.

The Volume Conjecture proposes that the asymptotics of the Kashaev invariants of a hyperbolic knot recover geometric information like the hyperbolic volume [@Kashaev1997]. The Kashaev invariants are naturally associated with the octahedral decomposition, and most proofs of special cases of the conjecture proceed via studying an associated [@Yokota2000]. The potential function is defined on a space parametrizing the geometry of the ideal tetrahedra: it has singularities where they are degenerate and critical points at nondegenerate solutions of the gluing equations of the triangulation. To apply the saddle-point method to the asymptotics of the Kashaev invariant it is important to use a diagram whose potential function has a smooth critical point at the complete hyperbolic structure. This question has been previously studied using other techniques [@Sakuma2018; @Garoufalidis2016] and it is known that every hyperbolic knot that is alternating or has at most 12 crossings has such a diagram. We show in [\[thm:arc-faithful\]](#thm:arc-faithful){reference-type="ref" reference="thm:arc-faithful"} that for knot diagrams this condition is equivalent to being , meaning that the Wirtinger generators of the over and under arcs at each crossing are always distinct. This new characterization may prove useful for showing that the potential function has smooth critical points.

Quantum topology provides another motivation for our results. One can define [@McPhailSnyderThesis; @McPhailSnyderVolume] a geometrically twisted version of the Kashaev invariant that can also be understood as a quantization of the $\slg$ Chern-Simons invariant, which includes the hyperbolic volume. The construction of this invariant uses the octahedral coordinates in an essential way and we expect the results of this paper to be useful for computing and studying it.

This paper began as an attempt to re-derive and generalize a formula [@Cho2014 Theorem 3.2] of @Cho2014 for boundary-parabolic representations. is similar to but more general than [@Cho2014 Theorem 3.2] and our proof is quite different. @Cho2014's result is more closely connected to the quandle $\mathcal{P}$ of parabolic elements of $\pslg$, and in particular to a presentation of it due to @Inoue2014 [@Inoue2014]. It would be interesting to better understand how our results relate to $\mathcal{P}$ and if this can be generalized to the boundary non-parabolic case.

## Organization

[\[sec:octahedral-colorings\]](#sec:octahedral-colorings){reference-type="ref" reference="sec:octahedral-colorings"}

:   We define octahedral colorings of tangle diagrams and state how to derive them from a representation of the fundamental group of the tangle complement given in terms of the Wirtinger presentation.

[\[sec:holonomy\]](#sec:holonomy){reference-type="ref" reference="sec:holonomy"}

:   We describe the geometrically-derived holonomy of an octahedral coloring and use it to justify our definition of the octahedral coloring associated to a representation.

[\[sec:gauge-transformations\]](#sec:gauge-transformations){reference-type="ref" reference="sec:gauge-transformations"}

:   We explain how conjugating a representation $\rho$ acts on the induced octahedral coloring and use this to show that every representation is conjugate to one coming from a coloring.

[\[sec:potential\]](#sec:potential){reference-type="ref" reference="sec:potential"}

:   We give some applications of our results to the Neumann-Zagier--Yokota potential function and the Volume Conjecture.

## Acknowledgements

I would like to thank Andy Putman for a comment on my MathOverflow question [@MathoverflowMeridians] about knot groups that led me to the proof of [\[thm:arc-faithful\]](#thm:arc-faithful){reference-type="ref" reference="thm:arc-faithful"}. I would also like to thank Seonhwa Kim for some useful comments on an early draft of the paper and for introducing me to relevant work of @Sakuma2018 and @Garoufalidis2016. Finally, I thank the anonymous referee for helpful comments that lead to an improved exposition.

## Conventions

All tangles are smooth and oriented. Our convention is that tangle diagrams go from left to right, so composition of tangles is horizontal and disjoint union is vertical. Our sign conventions the and typical labeling of the parts of a crossing are given in [1](#fig:crossing-types){reference-type="ref" reference="fig:crossing-types"}. Composition of paths is also read left to right: $fg$ means follow $f$ then $g$. For this reason we usually assume an eigenvector is a row vector, not a column vector. However, we write $\evec{1}, \evec{2}$ for the standard *column* vector basis of $\mathbb{C}^{2}$. For (column) vectors $u_1, u_2$ we write $\det\left( u_1, u_2 \right)$ for the determinant of the matrix with columns $u_1, u_2$, i.e.for the standard antisymmetric pairing on $\mathbb{C}^2$.

<figure id="fig:crossing-types">

<figcaption>Positive (left) and negative (right) crossings with our standard labeling.</figcaption>
</figure>
