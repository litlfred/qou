---
doc_id: arxiv-math-ph-0012035v3
doc_title: "Non-Abelian Stokes theorem in action"
section_id: sec-015-232-higher-dimensional-forms
section_title: "Higher-dimensional forms"
section_number: 2.3.2
pages: 33-34
source_pdf: 0012035v3.pdf
source_sha256: 06a4c8096c8ebb10
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Non-Abelian Stokes theorem in action — In this short review main issues related to the non-Abelian Stokes theorem have been addressed."
---
The theorem being considered up to now is a very particular, though seemingly the most important, non-Abelian version of the Stokes theorem. It connects a non-Abelian differential one-form in dimension $1$ and a two-form in dimension $2$. The forms are of a very particular shape, namely, the connection $1$-form and the curvature $2$-form. Now, we would like to discuss possible generalizations to arbitrary, higher-dimensional differential forms in arbitrary dimensions. Since there may be a lot of variants of such generalizations depending on a particular mathematical and/or physical context, we will start from giving a general recipe.

Our idea is very simple. First of all, working in the framework of the path-integral formalism, we should construct a topological field theory of auxiliary topological fields on $\partial N$, the boundary of the $d$-dimensional submanifold $N$, in (an) external (gauge) field(s) we are interested in. Next, we should quantize the theory, i.e. build the partition function in the form of a path-integral, where auxiliary topological fields are properly integrated out. Thus, the LHS of the non-Abelian Stokes theorem has been constructed. Applying the Abelian Stokes theorem to the (effective) action (in the exponent of the path-integral integrand) we obtain the "RHS" of the non-Abelian Stokes theorem. If we also wish to extend the functional measure to the whole $N$ we should additionaly quantize the theory on the RHS to eliminate the redundant functional integration inside $N$.

The example candidate for the topological field theory defining the LHS of the non-Abelian Stokes theorem could be given by the (classical) action $$S_{\rm Top}  = \frac{1}{2}\oint_{\partial N} {\left( {\bar zd_A \zeta  + d_A \bar \zeta z + \bar zBz} \right)}, 
    \label{STop}$$ where $z$ and $\bar z$ are zero-forms, $\zeta$ and $\bar\zeta$ are ($d-2$)-forms (all the forms are in an irreducible reprezentation $R(G)$), $d_A$ is the exterior covariant derivative $$d_A\zeta\equiv d\zeta+A\zeta,
\qquad
d_A\bar\zeta\equiv d\bar\zeta-A^T\bar\zeta.$$ The non-Abelian $B$-field naturally appears in the context of (topological) gauge theory (see, Eq.[\[SBF\]](#SBF){reference-type="ref" reference="SBF"}). Now, the Abelian Stokes theorem should do.

Generalization of the non-Abelian Stokes theorem to higher-degree forms in the operator language seems more difficult and practically has not been attempted (see, however \[Men83\] for an introductory discussion of this issue).
