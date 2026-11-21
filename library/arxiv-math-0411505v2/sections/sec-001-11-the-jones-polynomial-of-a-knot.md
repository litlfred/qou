---
doc_id: arxiv-math-0411505v2
doc_title: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION"
section_id: sec-001-11-the-jones-polynomial-of-a-knot
section_title: "The Jones polynomial of a knot"
section_number: 1.1
pages: 1-2
source_pdf: 0411505v2.pdf
source_sha256: a38cec365e0a227e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.805
doc_brief: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION — The colored Jones function of a knot is a sequence of Laurent polynomials that encodes the Jones polynomial of a knot and its parallels."
---
\lbl{sub.history}
In 1985, V. Jones discovered a celebrated invariant of knots, the Jones
polynomial, \cite{J1}. 
Jones's original formulation of the Jones polynomial was given in terms of
{\em representations of braid groups} and {\em Hecke algebras}, \cite{J1}. 
It soon
became apparent that the Jones polynomial can be defined as a {\em state sum} 
of a {\em statistical mechanics} model that uses as input a planar projection
of a knot, \cite{J2,Tu}.
As soon as the Jones polynomial was discovered, it was compared 
with the better-understood Alexander polynomial of a knot. The latter can be
defined using classical algebraic topology (such as the homology of 
the infinite cyclic cover of the knot complement), and its skein theory
can be understood purely topologically.
On the other hand, the Jones polynomial appears to be difficult to understand
topologically, and there is a good reason for this, as was explained by 
Witten, \cite{Wi}.
Namely, the Jones polynomial can be thought of as the expectation 
value of Wilson loops of a 3-dimensional gauge theory, the Chern-Simons theory;
 in general, this is hard to understand. Witten's approach leads to a number
of conjectures that relate limits of the Jones polynomial to geometric 
invariants of a knot, such as representations of the fundamental group
of its complement into compact Lie groups. 
A recent approach to the Jones polynomial 
in terms of $D$-{\em modules} and {\em holonomic functions} seems to relate 
well 
to the hyperbolic geometry of knot complements, \cite{GLe, Ga2} and
yet another approach to the Jones polynomial is via the {\em Kauffman bracket
skein theory}, \cite{KL}.

The goal of our paper is to present the colored Jones function
as {\em an evaluation of the inverse of a non-commutative fermionic partition 
function}.
 This result is in the form very familiar in quantum field theory, 
namely the inverse of
a generalized determinant.
Hence there should be a quantum field theoretic derivation of it, which may 
teach us new things about how to compute path integrals in topological 
quantum field theory.

About 10 years ago, Melvin-Morton and Rozansky independently conjectured
a relation among the limiting behavior of the colored Jones function 
of a knot and its Alexander polynomial (see Corollary \ref{cor.MMR}), 
\cite{MM,Ro1,Ro2}. D. Bar-Natan and 
the first author reduced the conjecture about knot invariants to a statement 
about their {\em combinatorial weight systems}, and then proved it for all 
weight systems that come from {\em semisimple Lie algebras} using 
combinatorial 
Lie algebraic methods, \cite{BG}. A combinatorial description of the 
corresponding
weight systems was obtained in \cite{GL}. Over the years, the MMR Conjecture 
has received 
attention by many researchers who gave alternative proofs, 
\cite{Ch,KSA,KM,Ro3,V}.

A comparison of Theorem \ref{thm.al} and Theorem \ref{thm.nonc} reveals a 
direct
relation between the Alexander polynomial and the colored 
Jones function. This should help us better understand the topological features
of the colored Jones function.

We will introduce an auxiliary weighted directed graph, the arc-graph, 
that encodes transitions of walks along a planar projection of a knot.
Our results are obtained by studying the non-negative integer flows on this 
arc-graph
and applying the recently discovered  q-MacMahon Master Theorem of \cite{GLZ}.
