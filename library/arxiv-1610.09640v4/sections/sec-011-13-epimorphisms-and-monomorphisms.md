---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-011-13-epimorphisms-and-monomorphisms
section_title: "Epimorphisms and Monomorphisms"
section_number: 1.3
pages: 26-27
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
a morphism f : C →D in C is called an isomorphism if there is a morphism
g : D→C such thatf◦g = idD and g◦f = idC. The morphismg is called the
inverse off, it is unique (if it exists), and it is denoted byf−1. An isomorphism is
often denoted by this shape of arrow:f :C
≃
− →D.
A morphism f : C →D in C is called an epimorphism if it has the right
cancellation property: for every g,g′: D →E, g◦f = g′◦f implies g = g′.
An epimorphism is often denoted by this shape of arrow:f :C↠D.
A morphismf :C→D is called amonomorphism if it has the left cancellation
property: for everyg,g′:E→C, f◦g =f◦g′implies g =g′. A monomorphism
is often denoted by this shape of arrow:f :C↣D.
26
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Example 1.3.1. In Set the monomorphisms are the injections, and the epimor-
phisms are the surjections. A morphismf :C→D in Set that is both a monomor-
phism and an epimorphism is an isomorphism. The same holds in the category
ModA of left modules over a ringA.
This example could be misleading, because the property of being an epimorphism
is often not preserved by forgetful functors, as the next exercise shows.
Exercise 1.3.2.Consider the category of ringsRng. Show that the forgetful func-
tor Rng→Set respects monomorphisms, but it does not respect epimorphisms.
(Hint: show that the inclusionZ→Q is an epimorphism inRng.)
By a subobject of an objectC∈C we mean a monomorphismf : C′↣ C in
C. We sometimes writeC′⊆C in this situation, but this is only notational (and
does not mean inclusion of sets). We say that two subobjectsf0 : C′
0↣ C and
f1 :C′
1↣C ofC are isomorphic if there is an isomorphismg :C′
0
≃
− →C′
1 such that
f1◦g =f0.
Likewise, by aquotient of C we mean an epimorphismg :C↠C′′in C. There
is an analogous notion of isomorphic quotients.
Exercise 1.3.3. Let C be a category, and letC be an object ofC.
(1) Suppose f0 : C′
0↣ C and f1 : C′
1↣ C are subobjects ofC. Show that
there is at most one morphismg :C′
0→C′
1 such thatf1◦g =f0; and ifg
exists, then it is a monomorphism.
(2) Show that isomorphism is an equivalence relation on the set of subobjects
ofC. Show that the set of equivalence classes of subobjects ofC is partially
ordered by “inclusion”. (Ignore set-theoretical issues.)
(3) Formulate and prove the analogous statements for quotient objects.
An initial objectin a categoryC is an objectC0∈C, such that for every object
C∈C there is exactly one morphismC0→C. Thus the set HomC(C0,C ) is a
singleton. A terminal objectin C is an objectC∞∈C, such that for every object
C∈C there is exactly one morphismC→C∞.
Deﬁnition 1.3.4.A zero objectin a categoryC is an object which is both initial
and terminal.
Initial, terminal and zero objects are unique up to unique isomorphisms (but
they need not exist).
Example 1.3.5. In Set, ∅ is an initial object, and every singleton is a terminal
object. There is no zero object.
Example 1.3.6. In ModA, every trivial module (with only the zero element) is a
zero object, and we denote this module by0. This is allowed, since any other zero
module is uniquely isomorphic to it.
