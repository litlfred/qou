---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-035-overview-of-analytic-methods-for-multivariate-gf
section_title: "Overview of analytic methods for multivariate GFs"
section_number: null
pages: 187-189
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
Overview of analytic methods for multivariate
GFs
We now return to the problem at the heart of this book: asymptotically ap-
proximating the coeﬃcients of a convergent Laurent series expansion F(z) =
P
r∈Zd arzr through the Cauchy integral representation
ar =
 1
2πi
!d Z
T
z−r−1F(z) dz ,
(7.1)
for a suitable domain of integration T. We accomplish this by deforming T
and using residue computations to reduce the Cauchy integral into a ﬁnite sum
of local integrals that can be asymptotically approximated using the results of
Chapter 5. When this approach succeeds, which it does in generic situations,
it provides asymptotic formulae of the form
ar ≈
X
w∈critical( ˆr)
nwΦw(r) ,
(7.2)
where the sum is over a ﬁnite set of certain critical points w, each Φw is
an asymptotic series that can be computed to any desired accuracy algorith-
mically, and the coeﬃcients nw are integers that may or may not be easy to
compute.
This textbook is designed so that combinatorialists can ﬁnd easy-to-apply
results with hypotheses and conclusions that are comprehensible with a mini-
mum of cross-referencing to lengthy deﬁnitions, while readers with topologi-
cal background can see the larger framework behind the results using advanced
methods, such as those described in Chapters 4–6 and the appendices. In or-
der to achieve this goal, the current chapter gives an overview of our approach
and its relationship to the higher-level theories we draw on. Chapter 8 takes a
computational view of the same material, giving explicit descriptions of how
to compute the quantities appearing in the analysis using a computer alge-
bra system. This material out of the way, Chapters 9–11 give our asymptotic
169
170
Overview of analytic methods for multivariate GFs
results for families of generating functions with increasingly complicated sin-
gular behavior, together covering most known examples of rational generating
functions in the combinatorial literature. Chapter 12 then gives a large variety
of examples and applications before Chapter 13 describes further extensions.
In order to guide intuition and introduce the high-level constructions to be
used in later chapters of the book, the current chapter begins by sketching the
analysis on some examples, showing how the computations in the simplest
case are a straightforward generalization of the univariate methods from Part I,
describing the limits of these methods, and illustrating why we require more
advanced techniques for our strongest results. After this we introduce the al-
gebraic and topological constructions necessary for our work, and prove the
theoretical results underpinning later chapters.
The computation of asymptotics is considerably simpler, and easier to ex-
plain, when the set of singularities V of F is smooth (meaning it is a manifold,
at least near points dictating asymptotics). Before going into technical details,
we illustrate the smooth case through extended examples in Section 7.1. Read-
ers who want to understand the method but not the details can quit after the
examples and skip to Chapters 8 and 9. In Section 7.2 we describe the theory
when V is smooth, allowing readers to understand the smooth point formulae
of Chapter 9 without the greater overhead of stratiﬁed Morse theory.
Section 7.3 gives a parallel treatment of everything in the previous sections,
without the assumption that V is smooth. This involves the introduction of
stratiﬁed Morse theory to explain the corresponding notions of critical points
and quasi-local cycles for non-smooth varieties. The quasi-local cycles are de-
ﬁned in terms of the tangential cycles γ j and homology generators βj for the
normal link at z j. Section 7.4 discusses the types of singular geometry that
arise frequently in combinatorial applications.
The results of (stratiﬁed) Morse theory describe the topology of a surface
using a height function mapping the surface to the real numbers. In classi-
cal Morse theory this height function is almost always assumed to be proper,
meaning the set of points with heights in a closed interval forms a compact
set. Unfortunately, we work in situations where the height function is usually
non-proper. To get around this diﬃculty, Section 7.5 introduces the concept of
critical points at inﬁnity (CPAI) and critical values at inﬁnity (CVAI), which
help characterize when the results of Morse theory we need apply without an
assumption of a proper height function. A fundamental lemma is stated con-
cerning the existence of certain deformations, provided there are no critical
values at inﬁnity, and its proof is cited from the literature. This lemma is then
used to prove the theorems previously stated in the chapter.
