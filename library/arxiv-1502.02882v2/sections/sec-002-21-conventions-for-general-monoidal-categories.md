---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams"
section_id: sec-002-21-conventions-for-general-monoidal-categories
section_title: "Conventions for general monoidal categories"
section_number: 2.1
pages: 4-5
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.994
doc_brief: "Fusion categories via string diagrams — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
\label{string_conventions}
The string diagram calculus for a monoidal category $\cat{C}$ is well-known (see \cite{s11-sgc} or \cite[Chap. 4]{BBthesis} for an overview). Each diagram refers to a certain morphism in $\cat{C}$. Our diagrams go from top to bottom, so that a morphism $f : A \rightarrow B \otimes C$ is drawn as
\[
\ig{d60.pdf} \, .
\] 
In these pictures there is no explicit parenthesis scheme on the input and output tensor products. Thus it is often supposed that one needs a a strict monoidal category in order to make this calculus well-defined. In fact, this is not so --- the calculus makes perfect sense when reasoning about {\em equations} between morphisms, which is all we will ever need. For instance, suppose $f : A \rightarrow A' \otimes E$, $g : B \otimes C \rightarrow D \otimes C'$, $h: E \otimes D \rightarrow B'$, $k : A \otimes (B \otimes C) \rightarrow F \otimes C'$, $l: F \rightarrow A' \otimes B'$, and consider the following equation:
\[
\ig{d67.pdf} = \ig{d68.pdf}
\]
How are we to interpret this? This equation should be regarded as an infinite number of equations, one for each fixed parenthesis scheme (this may include insertions of the unit object $1$ of the monoidal category) of the source and target objects, which are taken to be the same on both sides of the equation. For instance, $((1 \otimes A) \otimes (B \otimes 1)) \otimes C$ is a possible choice of parenthesis scheme for the source object in the above equation. For each such choice of parenthesis schemes, one should insert an appropriate sequence of associators and unit isomorphisms in order to make each side well-typed. Coherence for monoidal categories \cite{ml97-cwm} guarantees that the evaluation of the resultant morphism is independent of this choice. Each equation implies all the others (see \cite[Chap. 4]{BBthesis}). 

A monoidal category $\cat{C}$ is called {\em right rigid} if for each object $V$ there exists an object $V^*$ which can be equipped with unit and counit maps $\eta : 1 \rightarrow V^* \otimes V$, $\epsilon : V \otimes V^* \rightarrow 1$ such that the rigidity equations hold:
\begin{equation} \label{snake_eqns}
\ig{d69.pdf} = \ig{d70.pdf} \quad , \quad \ig{d71.pdf} = \ig{d72.pdf}
\end{equation}
Note that we have added orientations to the strands in \eqref{snake_eqns}, this is simply a visual aid. The monoidal category $\cat{C}$ is called {\em left rigid} if for each object $V$ there exists an object ${}^* V$ which can be equipped with unit and counit maps $n : 1 \rightarrow V \otimes {}^* V$, $e : {}^* V \otimes V \rightarrow 1$ satisfying the horizontally-reversed versions of \eqref{snake_eqns}. We say that $\cat{C}$ is {\em rigid} if it is both right rigid and left rigid. Our approach is to avoid making fixed initial choices of duals for each object, to keep constructions as canonical as possible (thus we do not refer to a right dual functor $* : \cat{C} \rightarrow \cat{C}^\text{op}$). 

Formally, the invariance of the evaluation of string diagrams under diffeomorphisms of the plane can be expressed as follows. We imagine each diagram as living in an outer disk $D$, with strands labelled by objects of the category, and coupons $C_i$ (drawn as discs or square regions) labelled by morphisms, which go from the tensor product of the objects labelling the strands in the northern hemisphere of the coupon to the tensor product of the objects labelling the strands in the southern hemisphere of the coupon. We define a {\em rigid isotopy} of such a diagram to be a smooth path of diffeomorphisms $\phi_t : D \rightarrow D$, $t \in [0,1]$ such that $\phi_0$ is the identity, $\phi_t$ is the identity on the boundary of $D$ for all $t$ and such that $\phi_t$ restricted to each coupon $C_i$ is a translation for all $t$.

The following theorem is well-known and combines coherence for monoidal categories, rigidity, and the interchange law.
\begin{thm}[{see eg. \cite{s11-sgc}}] \label{invariance_rigid}
The evaluation of a string diagram taking labels in a rigid monoidal category is invariant under diffeomorphisms which are rigid isotopic to the identity. 
\end{thm}
\begin{rem}
In a companion paper, motivated by \cite{kirillov2011-string-net}, we will express the diffeomorphism invariance for string diagrams taking labels in a {\em fusion category} in the language of spin structures. \label{spin_remark}
\end{rem}
