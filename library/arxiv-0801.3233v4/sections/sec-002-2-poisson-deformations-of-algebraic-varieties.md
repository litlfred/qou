---
doc_id: arxiv-0801.3233v4
doc_title: "Twisted Deformation Quantization of Algebraic Varieties (Survey)"
section_id: sec-002-2-poisson-deformations-of-algebraic-varieties
section_title: "Poisson Deformations of Algebraic Varieties"
section_number: 2
pages: 3-4
source_pdf: 0801.3233v4.pdf
source_sha256: d98f9d4a9ecb4c5e
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.938
doc_brief: "Twisted Deformation Quantization of Algebraic Varieties (Survey) — Let X be a smooth algebraic variety over a ﬁeld of characteristic 0. We introduce the notion of twisted associative (resp."
---
In algebraic geometry we have to consider deformations as sheaves. 

Let $X$ be a smooth algebraic variety over $\K$, with structure 
sheaf $\mcal{O}_{X}$. 
We view $\mcal{O}_{X}$ as a Poisson $\K$-algebra with zero bracket.

\begin{dfn}
A {\em Poisson deformation} of $\mcal{O}_X$ 
is a sheaf $\mcal{A}$ of flat, $\hbar$-adically complete,
commutative Poisson $\K[[\hbar]]$-algebras on $X$, with an 
isomorphism of Poisson algebras 
\[ \psi : \mcal{A} / (\hbar) \iso \mcal{O}_X , \]
called an augmentation. 

A {\em gauge equivalence} $\mcal{A} \to \mcal{A}'$
between Poisson deformations is a $\K[[\hbar]]$-linear 
isomorphism of sheaves of Poisson algebras, that commutes with the 
augmentations to $\mcal{O}_X$. 
\end{dfn}

It may happen that $\mcal{A} \cong \mcal{O}_X[[\hbar]]$ as sheaves of
commutative $\K[[\hbar]]$-algebras augmented to $\mcal{O}_X$; if this is so,
then we say that $\mcal{A}$ is a sheaf-theoretically trivial deformation.
A sufficient condition for that is the vanishing of the cohomology group 
$\mrm{H}^1(X, \mcal{T}_X)$, where $\mcal{T}_X$ is the tangent sheaf. 
The corresponding $\K[[\hbar]]$-bilinear Poisson bracket on
$\mcal{O}_X[[\hbar]]$ is called a {\em formal Poisson bracket}.

Given a Poisson deformation $\mcal{A}$ of $\mcal{O}_X$, we 
may define the {\em first order bracket}
\[ \{ -,- \}_{\mcal{A}} :  \mcal{O}_X \times \mcal{O}_X \to \mcal{O}_X
. \]
This is a Poisson bracket whose formula is
\[ \{ f,g \}_{\mcal{A}} := \psi \bigl( \smfrac{1}{\hbar} \{ \til{f},
\til{g} 
\} \bigr) , \]
where $f, g \in \mcal{O}_X$ are local sections, and 
$\til{f}, \til{g} \in \mcal{A}$ are arbitrary local lifts. 
The first order bracket  is invariant under gauge equivalences. 

\begin{exa} \label{exa10}
Let $\{ -,- \}_1$ be some Poisson bracket on $\mcal{O}_{X}$. 
Put on the commutative $\K[[\hbar]]$-algebra 
$\mcal{A} := \mcal{O}_X [[\hbar]]$
the formal Poisson bracket
$\hbar \{ -,- \}_1$, namely 
\[ \{ f, g \} = \hbar \{ f, g \}_1  \]
for $f, g \in \mcal{O}_X$. 
Then $\mcal{A}$ is a Poisson deformation of $\mcal{O}_X$. The first
order bracket in this case is just
\[ \{ -,- \}_{\mcal{A}} = \{ -,- \}_{1} . \]
\end{exa}

Poisson deformations are controlled by a coherent sheaf of DG (differential
graded) Lie algebras 
$\mcal{T}^{}_{\mrm{poly}, X}$,
called the {\em poly derivations}. 
This is explained in Appendix A.
