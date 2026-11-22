---
doc_id: arxiv-math-0410233v4
doc_title: "CUSP SHAPES UNDER CONE DEFORMATION"
section_id: sec-001-11-motivation
section_title: "Motivation"
section_number: 1.1
pages: 1-3
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 0.982
doc_brief: "CUSP SHAPES UNDER CONE DEFORMATION — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp shape."
---
The interplay between geometry and topology is an important theme in the study of 3--manifolds. Since Thurston's work in the late 1970's, it has been known that any Haken 3--manifold has a geometric decomposition [@thurston]. Recently Perelman has announced a proof that any closed, orientable 3--manifold has such a decomposition (the geometrization conjecture). However, it is important not only to know the existence of a geometric structure on a 3--manifold, but also to understand the relation between that structure and the topological description of the manifold.

Often a 3--manifold is described topologically, for example by a combinatorial diagram indicating a knot complement in $S^3$, or a Dehn filling description (see Definition [\[def:dehn\]](#def:dehn){reference-type="ref" reference="def:dehn"} below). However, relating this topological description to the geometry of the manifold seems to be very difficult, and remains an important problem in the area. There are few tools available to give geometric data from topological information. In this paper, we present a new such tool.

We are particularly interested in topological descriptions of 3--manifolds with torus boundary. These include all knot and link complements in $S^3$, as well as knot and link complements in other 3--manifolds. It is a classic result due to Wallace and Lickorish that every closed, orientable 3--manifold is given by a Dehn filling on a link complement in $S^3$ ([@wallace], [@lickorish]). Thus these manifolds are of fundamental importance in the subject.

We will also focus only on those manifolds which are hyperbolic. The link complements of Wallace and Lickorish above can be taken to be hyperbolic. Thurston showed that on any such cusped hyperbolic manifold "most" Dehn fillings are hyperbolic. That is, only a finite number of slopes per link component need be excluded, then any Dehn filling on remaining slopes yields a hyperbolic manifold [@thurston]. Additionally, for knots in $S^3$, any knot that is not a torus or satellite knot is known to be hyperbolic [@thurston:bulletin]. Therefore in some sense, most 3--manifolds are hyperbolic. Mostow--Prasad rigidity implies that the hyperbolic structure on these finite volume manifolds is unique [@mostow], [@prasad]. However, this unique structure is little understood.

Given a hyperbolic manifold with torus boundary components, i.e. given a *cusped* hyperbolic manifold, the geometric structure on the manifold allows us to associate a Euclidean similarity structure, called a cusp shape, to each boundary component. The cusp shapes of a manifold are geometric quantities which we will relate to a manifold's topological description.

There are several reasons one might be interested in knowing the cusp shape of a manifold. Cusp shape is an interesting piece of geometric information by itself. It also can be used to give a rough lower bound on the volume of the manifold, by calculating cusp volumes and using packing arguments such as those of Böröczky [@boroczky]. (See however [@eudave-munoz-luecke]: this lower bound may not be very sharp.) More importantly, knowing the cusp shape, we also obtain information on the geometry of manifolds obtained by Dehn filling. For example, we can find all filling slopes which might not yield a hyperbolic manifold [@agol:bounds], [@lackenby:surg], [@hk:univ].

Our main results give explicit bounds on the change in cusp shape of a 3--manifold with multiple cusps under all but finitely many Dehn fillings, where one cusp is left unfilled. This is essentially the content of Theorems [\[thm:main-cusp\]](#thm:main-cusp){reference-type="ref" reference="thm:main-cusp"}, [\[thm:main-norm-length\]](#thm:main-norm-length){reference-type="ref" reference="thm:main-norm-length"}, and [\[thm:main-norm-height\]](#thm:main-norm-height){reference-type="ref" reference="thm:main-norm-height"} below. The first, Theorem [\[thm:main-cusp\]](#thm:main-cusp){reference-type="ref" reference="thm:main-cusp"}, is the most general, bounding cusp information. In Theorem [\[thm:main-norm-length\]](#thm:main-norm-length){reference-type="ref" reference="thm:main-norm-length"}, we give a differential inequality bounding the normalized lengths of curves on cusps. In Theorem [\[thm:main-norm-height\]](#thm:main-norm-height){reference-type="ref" reference="thm:main-norm-height"}, we bound the change in height of the cusp shape.

We also apply these results to the case of knots in $S^3$. Given only a diagram of a large class of knots, we are able to determine bounds on the height of cusps. This is the content of Theorem [\[thm:main-knot-cusp\]](#thm:main-knot-cusp){reference-type="ref" reference="thm:main-knot-cusp"}. Note that similar results, relating the geometry of a knot to its diagram, are rare. In fact, we know only of results relating volumes to a diagram. Lackenby found lower bounds on volumes of alternating knots based on a condition of a diagram, and upper bounds for general knots [@lackenby:alt-volume]. The lower bounds were improved by Agol, Storm and Thurston [@ast:volumes], and the upper by Agol and D. Thurston in an appendix to Lackenby's paper [@lackenby:alt-volume]. Using cone deformations, we found similar bounds on volumes for another class of knots [@purcell:volume]. Using negatively curved metrics, we recently improved these results with Futer and Kalfagianni [@fkp:volumes].

However, as far as we are aware, the results of this paper are the first of their kind giving actual geometric bounds on cusp shape based only on a diagram.
