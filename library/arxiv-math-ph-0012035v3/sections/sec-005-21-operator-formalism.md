---
doc_id: arxiv-math-ph-0012035v3
doc_title: "Non-Abelian Stokes theorem in action"
section_id: sec-005-21-operator-formalism
section_title: "Operator formalism"
section_number: 2.1
pages: 7-9
source_pdf: 0012035v3.pdf
source_sha256: 06a4c8096c8ebb10
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.966
doc_brief: "Non-Abelian Stokes theorem in action — In this short review main issues related to the non-Abelian Stokes theorem have been addressed."
---
Unfortunately, it is not possible to automatically generalize the Abelian Stokes theorem (e.g. Eq.[\[ab.prop.Stok.2\]](#ab.prop.Stok.2){reference-type="ref" reference="ab.prop.Stok.2"}) to the non-Abelian one. In the non-Abelian case one faces a qualitatively different situation because the integrand on the LHS assumes values in a Lie algebra $\bf g$ rather than in the field of real or complex numbers. The picture simplifies significantly if one switches from the "local" language to a global one (see, Eq.[\[glob.ab.Stok.\]](#glob.ab.Stok.){reference-type="ref" reference="glob.ab.Stok."}). Therefore we should consider the holonomy [\[Pexp\]](#Pexp){reference-type="ref" reference="Pexp"} around a closed curve $C$, $${\rm P}\exp 
\left( i\oint_C A_i dx^i \right) .$$ The holonomy represents a parallel-transport operator around $C$ assuming values in a non-Abelian Lie group $G$. (Interestingly, in the Abelian case, the holonomy has a physical , it is an object playing the role of the phase which can be observed in the Aharonov-Bohm experiment, whereas $A_i$ itself has not such an interpretation.)

#### Non-Abelian Stokes theorem

The non-Abelian generalization of Eq.[\[glob.ab.Stok.\]](#glob.ab.Stok.){reference-type="ref" reference="glob.ab.Stok."} should read $${\rm P} \exp \left( i\oint_{\partial S=C}
A_i(x) dx^i \right)
= {\cal P} \exp \left( \frac{i}{2}
\int_S {\cal F}_{ij} (x) dx^i\wedge dx^j \right),$$ where the LHS has been already roughly defined. As far as the RHS is concerned, the symbol $\cal P$ denotes some "surface ordering", whereas ${\cal F}_{ij} (x)$ is a "path-dependent curvature" given by the formula $${\cal F}_{ij} (x)
\stackrel{\rm def}{=}
 U^{-1}(x,O) F_{ij}(x) U(x,O),$$ where $U(x,O)$ is a parallel-transport operator along the path $L$ in the surface $S$ joining

the base point $O$ of $\partial S$ with the point $x$, i.e. $$U(x,O)={\rm P} \exp \left( i\int_L
A_i(y)dy^i \right) .$$ See, Fig.[\[fig:oval\]](#fig:oval){reference-type="ref" reference="fig:oval"}, and further sections for more details.
