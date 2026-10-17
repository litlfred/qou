---
doc_id: arxiv-2508.03145v1
doc_title: "Θ -Categories and Tannakian duality"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-2
source_pdf: 2508.03145v1.pdf
source_sha256: 2bf03452cb503e96
toc_source: outline
---
Θ-Categories and Tannakian duality
Joost NUITEN, Bertrand TOEN
July 2025
Abstract
We introduce a notion of Θ-categories, which is a refinement of the
notion of symmetric monoidal ∞-categories.
We use this notion to
prove a Tannakian duality statement, relating Θ-categories with fpqc-
stacks by means of a certain stack of fiber functors in the context of
Θ-categories. This provides, over a base ring of arbitrary characteris-
tic, a strong link between Tannakian Θ-categories and the schematic
homotopy types of [Toe06].
Contents
1
Θ-Categories
3
1.1
µ-Categories . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
1.2
Θ-Categories
. . . . . . . . . . . . . . . . . . . . . . . . . . .
6
1.3
Θ-Categories of modules . . . . . . . . . . . . . . . . . . . . .
11
2
Tannaka duality
14
2.1
Θ-Categories of quasi-coherent and ind-perfect sheaves . . . .
15
2.2
Tannakian Θ-categories and Tannakian gerbes . . . . . . . . .
21
2.3
The Tannakian duality theorem . . . . . . . . . . . . . . . . .
23
A Positive tor-dimension descent
29
Introduction
The idea that homotopy theory can be approached from a Galois or Tan-
nakian point of view goes back to Grothendieck. This perspective was first
incarnated in his theory of the fundamental group, both pro-finite and pro-
algebraic (see for instance [Ray71], [Del89]). To the best of our knowledge,
1
arXiv:2508.03145v1  [math.AG]  5 Aug 2025
the fact that this point of view on the fundamental group can be fruit-
fully extended to more general homotopy invariants appears in two letters of
Grothendieck: to Serre, dated 18.07.1959 for the pro-finite case (see [CS01,
p. 75]), and to Breen, dated 19.07.1975, for the pro-algebraic case (see [Gro,
cote 134-2, p. 75]).
In [Toe00], the second author suggested an approach to Tannakian dual-
