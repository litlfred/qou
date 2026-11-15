---
doc_id: arxiv-0801.3233v4
doc_title: "Twisted Deformation Quantization of Algebraic Varieties (Survey)"
section_id: sec-003-3-associative-deformations-of-algebraic-varietie
section_title: "Associative Deformations of Algebraic Varieties"
section_number: 3
pages: 4-5
source_pdf: 0801.3233v4.pdf
source_sha256: d98f9d4a9ecb4c5e
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.976
doc_brief: "Twisted Deformation Quantization of Algebraic Varieties (Survey) — Let X be a smooth algebraic variety over a ﬁeld of characteristic 0. We introduce the notion of twisted associative (resp."
---
Let $X$ be a smooth algebraic variety over $\K$ as before.

\begin{dfn}
An {\em associative deformation of $\mcal{O}_X$} 
is a sheaf $\mcal{A}$ 
of flat, $\hbar$-adically complete, associative, unital 
$\K[[\hbar]]$-algebras on $X$, with an isomorphism of algebras
\[ \psi : \mcal{A} / (\hbar) \iso \mcal{O}_X , \]
called an augmentation.

A {\em gauge equivalence} $\mcal{A} \to \mcal{A}'$
between associative deformations is a $\K[[\hbar]]$-linear 
isomorphism of sheaves of unital algebras, that commutes with the 
augmentations to $\mcal{O}_X$. 
\end{dfn}

It may happen that $\mcal{A} \cong \mcal{O}_X[[\hbar]]$ as sheaves of
$\K[[\hbar]]$-modules augmented to $\mcal{O}_X$; if this is so,
then we say that $\mcal{A}$ is a sheaf-theoretically trivial deformation.
A sufficient condition for that is the vanishing of the cohomology group 
$\mrm{H}^1(X, \mcal{D}_X)$, where $\mcal{D}_X$ is the sheaf of differential
operators on $X$. (This fact is quite hard to prove, and it relies on Theorem
\ref{thm:diff}.)
The corresponding $\K[[\hbar]]$-bilinear multiplication on
$\mcal{O}_X[[\hbar]]$ is called a {\em star product}, like in Section 1.

Given an associative deformation $\mcal{A}$ we 
may define the first order bracket
\[ \{ -,- \}_{\mcal{A}} :  \mcal{O}_X \times \mcal{O}_X \to \mcal{O}_X
. \]
The formula, in terms of local sections, is
\[ \{ f,g \}_{\mcal{A}} :=
\psi \bigl( \smfrac{1}{2 \hbar} (\til{f} \star 
\til{g} - \til{g} \star \til{f}) \bigr) . \]
The first order bracket is invariant under gauge equivalences.

Associative deformations are controlled by a quasi-coherent sheaf of
DG Lie algebras $\mcal{D}^{}_{\mrm{poly}, X}$,
called the {\em poly differential operators}. 
This is explained in Appendix A.

Note that both kinds of deformations -- Poisson and associative --
include as special cases the classical commutative deformations of $\mcal{O}_X$.
