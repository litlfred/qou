---
doc_id: arxiv-math-ph-0012035v3
doc_title: "Non-Abelian Stokes theorem in action"
section_id: sec-001-11-abelian-stokes-theorem
section_title: "Abelian Stokes theorem"
section_number: 1.1
pages: 2-3
source_pdf: 0012035v3.pdf
source_sha256: 06a4c8096c8ebb10
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.981
doc_brief: "Non-Abelian Stokes theorem in action — In this short review main issues related to the non-Abelian Stokes theorem have been addressed."
---
Before we engage in the non-Abelian Stokes theorem it seems reasonable to recall its Abelian version. The (Abelian) Stokes theorem says (see, e.g. \[Spi65\], for an excellent introduction to the subject) that we can convert an integral around a closed curve $C$ bounding some surface $S$ into an integral defined on this surface. Namely, in e.g. three dimensions $$\oint_C \vec{A} \cdot d\vec{s}
    =\int_S {\rm curl}\vec{A} \cdot
    \vec{n}\,d\sigma, 
    \label{prop.Stok.}$$

<figure id="fig:ast">
<div class="center">
<div class="picture">
<p>(58,60)</p>
</div>
</div>
<figcaption>Integration areas for the lowest-dimensional (non-trivial) version of the Abelian Stokes theorem.</figcaption>
</figure>

where the curve $C$ is the boundary of the surface $S$, i.e. $C=\partial S$ (see, Fig.[1](#fig:ast){reference-type="ref" reference="fig:ast"}), $\vec{A}$ is a vector field, e.g. the vector potential of electromagnetic field, and $\vec{n}$ is a unit outward normal at the area element $d\sigma$.

More generally, in any dimension, $$\int_{\partial N} \omega=\int_N d\omega ,
    \label{ab.Stok.}$$ where now $N$ is a $d$-dimensional submanifold of the manifold $M$, $\partial N$ is its $(d-1)$-dimensional boundary, $\omega$ is a $(d-1)$-form, and $d\omega$ is its differential, a $d$-form. We can also rewrite Eq.[\[prop.Stok.\]](#prop.Stok.){reference-type="ref" reference="prop.Stok."} in the spirit of Eq.[\[ab.Stok.\]](#ab.Stok.){reference-type="ref" reference="ab.Stok."}, i.e. $$\oint_{\partial S=C} A_i\, dx^i=
    \frac {1}{2} \int_S
    \left( \partial_i A_j-\partial_j A_i \right) dx^i \wedge
    dx^j ,
    \label{ab.prop.Stok.}$$ where $A_i$ ($i=1,2,3$) are components of the vector $\vec A$, and the Einstein summation convention after repeating indices is assumed.

In electrodynamics, we define the stress tensor of electromagnetic field $$F_{ij}=\partial_i A_j -\partial_j A_i ,$$ and the magnetic induction, its dual, as $$B_k=\frac {1}{2} \varepsilon_{ijk}F_{ij},$$ where $\varepsilon_{ijk}$ is the totally antisymmetric (pseudo-)tensor. RHS of Eq.[\[ab.prop.Stok.\]](#ab.prop.Stok.){reference-type="ref" reference="ab.prop.Stok."} represents then the magnetic flux through $S$. Thus, we can rewrite Eq.[\[ab.prop.Stok.\]](#ab.prop.Stok.){reference-type="ref" reference="ab.prop.Stok."} in the form of [\[prop.Stok.\]](#prop.Stok.){reference-type="ref" reference="prop.Stok."} $$\begin{aligned}
    \oint_{\partial S=C} A_i\, dx^i
    &=& \frac {1}{2} \int_S F_{ij}\, dx^i \wedge dx^j
    \label{ab.prop.Stok.2}\\
    &=&\int_S B_in^i\, d\sigma.
    \nonumber
\end{aligned}$$

In turn, in geometry $\vec A$ plays the role of connection (it defines the parallel transport around $C$), and $F$ is the curvature of this connection. A "global version" of the Abelian Stokes theorem, $$\exp \left( i \oint_{\partial S=C}
    A_i(x)\, dx^i \right) =
    \exp \left( \frac {i}{2} 
    \int_S F_{ij}(x)\, dx^i \wedge dx^j \right),
    \label{glob.ab.Stok.}$$ which is rather a trivial generalization of Eq.[\[ab.prop.Stok.2\]](#ab.prop.Stok.2){reference-type="ref" reference="ab.prop.Stok.2"}, is a very good starting point for our further discussion concerning the non-Abelian Stokes theorem. The object on LHS of [\[glob.ab.Stok.\]](#glob.ab.Stok.){reference-type="ref" reference="glob.ab.Stok."} is called the holonomy, and more generally, for open curves $C$, global connection.
