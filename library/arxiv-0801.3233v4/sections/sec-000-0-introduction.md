---
doc_id: arxiv-0801.3233v4
doc_title: "Twisted Deformation Quantization of Algebraic Varieties (Survey)"
section_id: sec-000-0-introduction
section_title: "Introduction"
section_number: 0
pages: 1-2
source_pdf: 0801.3233v4.pdf
source_sha256: d98f9d4a9ecb4c5e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.876
doc_brief: "Twisted Deformation Quantization of Algebraic Varieties (Survey) — Let X be a smooth algebraic variety over a ﬁeld of characteristic 0. We introduce the notion of twisted associative (resp."
---
\label{sec:Int}

Let $\K$ be a field of characteristic $0$, and let $X$ be a
smooth algebraic variety over $\K$, with structure sheaf
$\mcal{O}_X$. An {\em associative deformation of $\mcal{O}_X$} is a
sheaf $\mcal{A}$ of flat complete associative $\K[[\hbar]]$-algebras on $X$,
with an isomorphism $\K \otimes_{\K[[\hbar]]} \mcal{A} \cong \mcal{O}_X$, called
an augmentation. Similarly, a {\em Poisson deformation of $\mcal{O}_X$} is a
sheaf $\mcal{A}$ of flat complete commutative Poisson $\K[[\hbar]]$-algebras
on $X$, with an augmentation to $\mcal{O}_X$. 

In this paper we introduce the notion of {\em twisted associative
\tup{(}resp.\ Poisson\tup{)} deformation of $\mcal{O}_X$}.  
A twisted deformation (or either kind) is a stack-like version of an
ordinary deformation. The precise definition is given in Section 
\ref{sec:twdefs}. But to give an idea, let us say that a twisted deformation 
$\gerbe{A}$ can be described as a collection of locally defined
deformations $\mcal{A}_i$, each living on an open set $U_i$ of $X$, that
are glued together in a loose way. We should also say that an
associative deformation $\gerbe{A}$ is a special kind of
{\em stack of algebroids}, in the sense of \cite{Ko2}.
Indeed, one reason for introducing twisted deformations is to have a
Poisson analogue of a stack of algebroids.

There is a notion of {\em twisted gauge equivalence} between  
twisted associative (resp.\ Poisson) deformation of
$\mcal{O}_X$. A twisted deformation $\gerbe{A}$ induces a {\em
first order bracket} $\{ -,- \}_{\gerbe{A}}$ on $\mcal{O}_X$.
The main result is Theorem \ref{thm_new}, which says that 
there is a canonical bijection of sets
\[ \begin{aligned}
& \opn{tw{.}quant} : 
\frac{ \{ \tup{twisted Poisson deformations of 
$\mcal{O}_X$} \} }
{\tup{ twisted gauge equivalence}} \\
& \qquad \qquad \iso \
\frac{ \{ \tup{twisted associative deformations of 
$\mcal{O}_X$} \} }
{\tup{ twisted gauge equivalence}}
\end{aligned} \] 
called the {\em twisted quantization map}. 
It preserves first order brackets, and commutes with \'etale morphisms 
$X' \to X$.

This survey article is an edited version of lectures that I gave on several
occasions. In addition to the main body of the article, there are four
appendices, that provide further details on certain aspects of the topic. 
Full details can be found in my papers listed in the bibliography. The
bibliography also covers work by other researchers in this area. 


\medskip \noindent
\textbf{Acknowledgments.}
Part of the work presented here is joint with Frederick Leitner.
Many of the ideas in this paper are influenced by the work
of Maxim Kontsevich, and I wish to thank him for discussing this
material with me.
Thanks also to Michael Artin, Pavel Etingof, Damien
Calaque, Michel Van den Bergh, Pierre Deligne, 
Lawrence Breen, Pierre Schapira and James Stasheff 
for their assistance on various aspects of the paper.
