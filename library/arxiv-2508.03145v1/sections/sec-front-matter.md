---
doc_id: arxiv-2508.03145v1
doc_title: "Θ -Categories and Tannakian duality"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-3
source_pdf: 2508.03145v1.pdf
source_sha256: 2bf03452cb503e96
toc_source: outline
doc_brief: "Θ -Categories and Tannakian duality — We introduce a notion of Θ-categories, which is a refinement of the notion of symmetric monoidal ∞-categories."
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
ity for ∞-categories based on the notion of symmetric monoidal ∞-categories
defined as functors out of Γ, the category of pointed finite sets. In [Toe06]
certain stacks, called schematic homotopy types, have been identified as the
expected duals to Tannakian ∞-categories and have been used notably in
the setting of non-abelian Hodge theory (see [KPT08]). Thanks to the foun-
dational work of Lurie, actual Tannaka duality statements have been proven
by several authors, see for instance [Lur11], [Wal12] and [Iwa18]. However,
except in the specific case of characteristic zero, these results are obtained
in the setting of E∞-algebras, which do not relate well to the theory of
schematic homotopy types of [Toe06], and therefore do not provide the ex-
pected Tannakian interpretations for schematic homotopy types.
The starting point of this work is the simple observation that any notion
of Tannakian ∞-category solely based on symmetric monoidal ∞-categories
will fail to relate nicely to schematic homotopy types, or to stacks in alge-
braic geometry in general. Indeed, for any stack F on the fpqc-site of affine
schemes, the symmetric monoidal ∞-category QCoh(F) of quasi-coherent
sheaves comes equipped with natural extra operations, namely the derived
symmetric power operations. These cannot be reconstructed purely from the
symmetric monoidal structure, and their existence is a theoretical obstruc-
tion for any Tannakian-type reconstruction result in algebraic geometry.
A second incarnation of this discrepancy can be seen at the level of com-
mutative algebras. The theory of schematic homotopy types from [Toe06]
uses co-simplicial commutative rings, a sub-class of the LSym-algebras (see
e.g. [BCN21, Rak20]) typically used in derived, as opposed to spectral, al-
gebraic geometry. In characteristic zero, these LSym-algebras coincide with
the E∞-algebras that exist naturally in any symmetric monoidal ∞-category,
but have an additional algebraic structure in general.
The purpose of this short note is to introduce a rudimentary notion of
Θ-categories, which is a refinement of the notion of symmetric monoidal
∞-categories suited for a Tannakian interpretation of schematic homotopy
types and similar stacks. The point of view adopted here will be somewhat
minimalist and takes the second discrepancy mentioned above as its starting
point. It is based on the principle that Θ-categories should morally be sym-
2
