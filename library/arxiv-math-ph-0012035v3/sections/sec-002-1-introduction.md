---
doc_id: arxiv-math-ph-0012035v3
doc_title: "Non-Abelian Stokes theorem in action"
section_id: sec-002-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 0012035v3.pdf
source_sha256: 06a4c8096c8ebb10
text_source: latex
latex_prose_ratio: 0.662
latex_coverage_ratio: 0.974
doc_brief: "Non-Abelian Stokes theorem in action — In this short review main issues related to the non-Abelian S tokes theorem have been addressed."
---
For tens years the (standard, i.e. Abelian) *Stokes* theorem is one of the central points of (multivariable) analysis on manifolds. Lower-dimensional versions of this theorem, known as the (proper) Stokes theorem, in dimensions 1 and 2, and the, so-called *Gauss* theorem, in dimensions 2 and 3, respectively, are well-known and extremally useful in practice, e.g. in classical electrodynamics (Maxwell equations). In fact, it is difficult, if not impossible, to imagine lectures on classical electrodynamics without intensive use of the Stokes theorem. The standard Stokes theorem is also being called the *Abelian* Stokes theorem, as it applies to (ordinary, i.e. Abelian) differential forms. Classical electrodynamics is an Abelian (i.e. $U(1)$) gauge field theory (gauge fields are Abelian forms), therefore its integral formulas are governed by the Abelian Stokes theorem. But much of interesting and physically important phenomena is described by non-Abelian gauge theories. Hence it would be very desirable to have at our disposal a non-Abelian version of the Stokes theorem. Since non-Abelian differential forms need a bit different treatment, one is forced to use a more sophisticated formalism to deal with this new situation.

The aim of this chapter is to present a short review of the non-Abelian Stokes theorem. At first, we will give an account of different formulations of the non-Abelian Stokes theorem and next of various applications of thereof.

## Abelian Stokes theorem

Before we engage in the non-Abelian Stokes theorem it seems reasonable to recall its Abelian version. The (Abelian) Stokes theorem says (see, e.g. \[Spi65\], for an excellent introduction to the subject) that we can convert an integral around a closed curve $C$ bounding some surface $S$ into an integral defined on this surface. Namely, in e.g. three dimensions $$\begin{equation}
    \oint_C \vec{A} \cdot d\vec{s}
    =\int_S {\rm curl}\vec{A} \cdot
    \vec{n}\,d\sigma, 
    \label{prop.Stok.}
\end{equation}$$

<figure id="fig:ast" data-latex-placement="htb">
<div class="center">
<div class="picture">
<p>(58,60)</p>
</div>
</div>
<figcaption>Integration areas for the lowest-dimensional (non-trivial) version of the Abelian Stokes theorem.</figcaption>
</figure>

where the curve $C$ is the boundary of the surface $S$, i.e. $C=\partial S$ (see, Fig.[1](#fig:ast){reference-type="ref" reference="fig:ast"}), $\vec{A}$ is a vector field, e.g. the vector potential of electromagnetic field, and $\vec{n}$ is a unit outward normal at the area element $d\sigma$.

More generally, in any dimension, $$\begin{equation}
    \int_{\partial N} \omega=\int_N d\omega ,
    \label{ab.Stok.}
\end{equation}$$ where now $N$ is a $d$-dimensional submanifold of the manifold $M$, $\partial N$ is its $(d-1)$-dimensional boundary, $\omega$ is a $(d-1)$-form, and $d\omega$ is its differential, a $d$-form. We can also rewrite Eq.[\[prop.Stok.\]](#prop.Stok.){reference-type="ref" reference="prop.Stok."} in the spirit of Eq.[\[ab.Stok.\]](#ab.Stok.){reference-type="ref" reference="ab.Stok."}, i.e. $$\begin{equation}
    \oint_{\partial S=C} A_i\, dx^i=
    \frac {1}{2} \int_S
    \left( \partial_i A_j-\partial_j A_i \right) dx^i \wedge
    dx^j ,
    \label{ab.prop.Stok.}
\end{equation}$$ where $A_i$ ($i=1,2,3$) are components of the vector $\vec A$, and the Einstein summation convention after repeating indices is assumed.

In electrodynamics, we define the stress tensor of electromagnetic field $$F_{ij}=\partial_i A_j -\partial_j A_i ,$$ and the magnetic induction, its dual, as $$B_k=\frac {1}{2} \varepsilon_{ijk}F_{ij},$$ where $\varepsilon_{ijk}$ is the totally antisymmetric (pseudo-)tensor. RHS of Eq.[\[ab.prop.Stok.\]](#ab.prop.Stok.){reference-type="ref" reference="ab.prop.Stok."} represents then the magnetic flux through $S$. Thus, we can rewrite Eq.[\[ab.prop.Stok.\]](#ab.prop.Stok.){reference-type="ref" reference="ab.prop.Stok."} in the form of [\[prop.Stok.\]](#prop.Stok.){reference-type="ref" reference="prop.Stok."} $$\begin{eqnarray}
    \oint_{\partial S=C} A_i\, dx^i
    &=& \frac {1}{2} \int_S F_{ij}\, dx^i \wedge dx^j
    \label{ab.prop.Stok.2}\\
    &=&\int_S B_in^i\, d\sigma.
    \nonumber
\end{eqnarray}$$

In turn, in geometry $\vec A$ plays the role of connection (it defines the parallel transport around $C$), and $F$ is the curvature of this connection. A "global version" of the Abelian Stokes theorem, $$\begin{equation}
    \exp \left( i \oint_{\partial S=C}
    A_i(x)\, dx^i \right) =
    \exp \left( \frac {i}{2} 
    \int_S F_{ij}(x)\, dx^i \wedge dx^j \right),
    \label{glob.ab.Stok.}
\end{equation}$$ which is rather a trivial generalization of Eq.[\[ab.prop.Stok.2\]](#ab.prop.Stok.2){reference-type="ref" reference="ab.prop.Stok.2"}, is a very good starting point for our further discussion concerning the non-Abelian Stokes theorem. The object on LHS of [\[glob.ab.Stok.\]](#glob.ab.Stok.){reference-type="ref" reference="glob.ab.Stok."} is called the holonomy, and more generally, for open curves $C$, global connection.

## Historical remarks

The birth of the ideas related to the (non-)Abelian Stokes theorem dates back to the ninetenth century and is connected with the emergence of the Abelian Stokes theorem. The Abelian Stokes theorem can be treated as a prototype of the non-Abelian Stokes theorem or a version of thereof when we confine ourselves to an Abelian group.

A work closer to the proper non-Abelian Stokes theorem, by Schlesinger \[Sch27\], where generally non-commuting matrix-values functions have been considered appeared in 1927. In fact no work on the genuine non-Abelian Stokes theorem could appear before the birth of very idea of non-Abelian gauge fields in the beginning of fifthies. And really, first papers on the non-Abelian Stokes theorem appeared in the very end of seventhies. At first, the non-Abelian Stokes theorem emerged in the operator version \[Hal79\] (the first appearance of the non-Abelian Stokes theorem, see Eq.3.8 therein), \[Are80\], \[Bra80\], \[FGK81\], and later on, in the very end of eighties, in the path-integral one \[DP89\], \[Bro92\].

## Contents

The propert part of the paper consists of two sections. The first section is devoted to the non-Abelian Stokes theorem itself. In the beginning, we introduce necessary notions and conventions. The operator version of the non-Abelian Stokes theorem is formulated in the first subsection. The second subsection concerns the path-integral versions of the non-Abelian Stokes theorem: coherent-state approach and holomorphic approach. The last subsection describes generalizations of the non-Abelian Stokes theorem. First of all, to topologically more general situations, and also to higher-degree forms. The second section is devoted to applications of the non-Abelian Stokes theorem in mathematical and theoretical physics. In the first subsection an approach to the computation of Wilson loops in two-dimensional Yang-Mills theory is presented. The second subsection deals with the analogous problem for three-dimensional (topological) Chern-Simons gauge theory. Other possibilities, including higher-dimensional gauge theories and QCD are mentioned in the last subsection.
