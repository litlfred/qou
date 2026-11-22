---
doc_id: arxiv-0906.1500v4
doc_title: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds"
section_id: sec-012-4-examples-of-computations
section_title: "Examples of computations"
section_number: 4
pages: 12-12
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.915
latex_coverage_ratio: 0.987
doc_brief: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds — We study a computational method of the hyperbolic Reidemeister torsion (also called in the literature"
---
\label{section:exemples}

We compute the polynomial torsions for the figure knot exterior and
the Whitehead link exterior by using Fox differential calculus as
shown in~\cite{Milnor:1968,Kitano, KL}.

First, we consider the
Jacobian matrix using Fox free differential calculus associated to a
Wirtinger presentations of a link group.  
To express the polynomial torsion, we need a square minor in the
Jacobian matrix.  Since the number of relations in a Wirtinger
presentation is one less than that of generators, we have a square
minor in the Jacobian matrix by dropping one column.  For an
$\SL$-representation $\rho$ of the link group, when we replace each
element of the link group in the square minor of the Jacobian matrix
by the $3 \times 3$ matrix derived from the action of
$\otAd{\varphi}{\rho}$, we obtain a large matrix whose entries are
Laurent polynomials with coefficients in $\CC$.  Then we can express
the polynomial torsion for the link exterior as the rational function
whose numerator is the determinant of the square minor replaced each
component with $\otAd{\varphi}{\rho}$.  The denominator of the
polynomial torsion is the characteristic polynomial of the
$\mathrm{SL}_3(\CC)$-element given by the generator corresponding to
the dropped column from the Jacobian matrix.  It remains a problem to
construct $\SL$-representations of link group.  However we can find
explicit constructions for the figure eight knot
in~\cite{KirkKlassenMathAnn:ChernSimon} and for the Whitehead link
in~\cite{HLM92:characterization}.
