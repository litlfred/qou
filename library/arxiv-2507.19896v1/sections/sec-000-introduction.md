---
doc_id: arxiv-2507.19896v1
doc_title: "Generalized Markov traces and Jucys-Murphy elements"
section_id: sec-000-introduction
section_title: "Introduction."
section_number: null
pages: 1-2
source_pdf: 2507.19896v1.pdf
source_sha256: a3f23d5a08b397ee
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.978
doc_brief: "Generalized Markov traces and Jucys-Murphy elements — We give a simple construction of Markov traces for Iwahori-Hecke algebras associated with infinite series of crystallographic Coxeter groups."
---
A two-variable link invariant -- the HOMFLY-PT polynomial -- can be recovered using a family of trace functions on Iwahori-Hecke algebras in type $A$ satisfying analogues of the conditions in Markov's theorem for the braid group (usually called ``Markov moves'') \cite{jonesHeckeAlgebraRepresentations1987}. The analogues of Markov moves can be formulated for Iwahori-Hecke algebras of other Coxeter groups, leading to a general notion of the Markov trace, see, for example, \cite{geckTraceFunctionsIwahoriHecke1998}, \cite{geckMarkovTracesKnot2004}, \cite{gomi2006markov},  \cite{websterGeometryMarkovTraces2009}. The Markov traces where classified in type $A$, where there is, up to some change of scaling, a unique Markov trace, by Ocneanu and Jones \cite{jonesHeckeAlgebraRepresentations1987}, and in types $B$ and $D$ by Geck and Lambropoulou \cite{geckMarkovTracesKnot2004}, \cite{geckTraceFunctionsIwahoriHecke1998}. In type $B$, Markov traces produce the invariants of the solid torus links \cite{lambropoulou1994solid} \cite{geckMarkovTracesKnot2004}.

Of particular interest are specializations of the general Markov traces in types $B, D$ coming from geometry (or, alternatively, from the theory of Soergel bimodules). These where studied in \cite{gomi2006markov} using the Lusztig's Fourier transform, in \cite{websterGeometryMarkovTraces2009} using the equivariant Hecke category, and in \cite{bezrukavnikovMonodromicModelKhovanov2022} using the monodromic Hecke category. Note that the latter two papers work in the setting of an arbitrary Weyl group and allow to categorify Markov traces to obtain a triply-graded link invariant known as Khovanov-Rozansky homology. Its earlier construction, using Soergel bimodules in type $A$ \cite{khovanovTriplygradedLinkHomology2007}, readily generalizes to an arbitrary Coxeter group.

Iwahori-Hecke algebras in types $A, B, D$ contain families of commuting operators whose properties are analogous to those of Jucys-Murphy elements in the group algebra of the symmetric group. 
Under a standard normalization, the Markov trace in type $A$ is polynomial in variable $a$. Its individual coefficients turn out to be ``represented'' (in the sense explained in the main text) by the elementary symmetric polynomials in multiplicative Jucys-Murphy elements. It was shown in \cite{bezrukavnikovMonodromicModelKhovanov2022} that this fact admits a categorification to the level of Khovanov-Rozansky homology. Moreover, in type $A$, multiplicative Jucys-Murphy elements themselves admit an interesting categorification, defining relative Serre functors with respect to the embedding of a smaller Hecke category into a larger one \cite{gorskySerreDualityKhovanov2019}, \cite{ho2025relative}.  Our investigation was motivated by a desire to see how far these patterns can be extended for other types.

In this paper, we give a new simple construction for Markov traces in types $B, D$ using the theory of Jucys-Murphy elements in Iwahori-Hecke algebras of these types.

The paper is organized as follows.
In Section \ref{sec:iwah-hecke-algebr-2} we collect the needed definitions about Coxeter groups and Iwahori-Hecke algebras. In Section \ref{sec:some-centr-elem} we define a family of commuting elements in Iwahori-Hecke algebras of type $A, B, D$ coming from the extended affine Hecke algebra in type $A$. See \cite{ram1997seminormal} for the history and an alternative definition. We follow \cite{Ram2003} in our treatment of these elements.

In Section \ref{sec:markov-traces-1} we first define the Markov traces and give, as a warm-up, a construction of a Markov trace defined by a uniform formula in all types $A, B, D$. See Theorem \ref{sec:markov-traces-via}. In Section \ref{sec:gener-mark-trac-3} we recall the results of Geck and Lambropoulou and give the formulas for the Markov traces in types $B$ and $D$ depending on a free parameter (Theorem \ref{sec:gener-mark-trac-2} and Corollary \ref{sec:gener-mark-trac-4}, respectively). In Section \ref{sec:geom-mark-trac} we specialize our results to obtain the geometric Markov traces.
