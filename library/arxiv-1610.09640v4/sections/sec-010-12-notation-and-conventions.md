---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-010-12-notation-and-conventions
section_title: "Notation and Conventions"
section_number: 1.2
pages: 25-26
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
as an abbreviation forC∈Ob(C). For an objectC, its identity automorphism is
denoted by idC. The identity functor ofC is denoted byIdC.
Theoppositecategoryof Cis Cop. Ithasthesameobjectsas C, butthemorphism
sets are HomCop(C0,C 1) := HomC(C1,C 0), and composition is reversed. Of course
(Cop)op = C. The identity functor of C can be viewed as a contravariant functor
Op : C→Cop. To be explicit, on objects we takeOp(C) :=C. As for morphisms,
given a morphismφ: C0→C1 in C, we let Op(φ) : Op(C1)→Op(C0) be the
morphism Op(φ) :=φin Cop. The inverse functorCop→C is also denoted byOp.
Thus Op◦Op = Id.
A contravariant functorF : C→D is the same as a covariant functorF◦Op :
Cop →D. By default all functors will be covariant, unless explicitly mentioned
otherwise. Contravariant functors will almost always we dealt with by replacing
the source category with its opposite.
Deﬁnition 1.2.1.LetK be a commutative ring. By acentralK-ring we mean a
ring A, together with a ring homomorphismK→A, called the structural homo-
morphism, such that the image ofK is inside the center ofA.
The category of centralK-rings, whose morphisms are the ring homomorphisms
f : A→B that respect the structural homomorphisms fromK, is denoted by
Rng/cK.
ThismaterialwillbepublishedbyCambridgeUniversityPressas Derived CategoriesbyAmnon
Yekutieli. This prepublication version is free to view and download for personal use only. Not for
redistribution, resale or use in derivative works.c© Amnon Yekutieli, 2019.
25
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Traditionally, a centralK-ring was called a “unital associativeK-algebra”. Of
course all rings and ring homomorphisms are unital. WhenK =Z, a centralK-ring
is just a ring, and then we sometimes use the notationRng.
Example 1.2.2. Let K be a nonzero commutative ring, and letn be a positive
integer. Then Matn(K), the ring ofn×n matrices with entries inK, is a central
K-ring.
Deﬁnition 1.2.3.Let A be a ring. We denote byModA, or by the abbreviated
notation M(A), the category of leftA-modules.
Rings and modules are very important for us, so let us also put forth the next
convention.
Convention1.2.4. Belowarethedefaultimplicitassumptionsforlinearstructures
and operations.
(1) There is a nonzero commutative base ringK (e.g. the ring of integersZ of
a ﬁeld).
(2) The unadorned tensor symbol⊗means⊗K.
(3) All rings are centralK-rings (see Deﬁnition 1.2.1), all ring homomorphisms
are overK, and all bimodules areK-central.
(4) Generalizing (3), all linear categories areK-linear (see Deﬁnition 2.1.1),
and all linear functors areK-linear (see Deﬁnition 2.5.1).
(5) For a ringA, by allA-modules are leftA-modules, unless explicitly stated
otherwise.
RightA-modules are left modules over the opposite ringAop, and this is the way
we shall most often deal with them. Morphisms in the categories of groups, rings,
A-modules, etc. will usually be called group homomorphism, ring homomorphisms,
A-module homomorphisms, etc., respectively.
Convention 1.2.5.We will try to keep the following font and letter conventions:
•f :C→D is a morphism between objects in a category.
•F : C→D is a functor between categories.
•η:F→G is morphism of functors (i.e. a natural transformation) between
functors F,G : C→D.
•φ,ψ,φi : M→N are morphisms between objects in an abelian category
M.
•F : M→N is a linear functor between abelian categories.
•The category of complexes in an abelian categoryM is C(M).
•If M is a module category, andM∈Ob(M), then elements ofM will be
denoted bym,n,m i,....
