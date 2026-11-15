---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-011-12-notation-and-conventions
section_title: "Notation and Conventions"
section_number: 1.2
pages: 25-26
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
as an abbreviation for C ∈Ob(C). For an object C, its identity automorphism is
denoted by idC. The identity functor of C is denoted by IdC.
The opposite category of C is Cop. It has the same objects as C, but the morphism
sets are HomCop(C0, C1) := HomC(C1, C0), and composition is reversed. Of course
(Cop)op = C. The identity functor of C can be viewed as a contravariant functor
Op : C →Cop. To be explicit, on objects we take Op(C) := C. As for morphisms,
given a morphism φ : C0 →C1 in C, we let Op(φ) : Op(C1) →Op(C0) be the
morphism Op(φ) := φ in Cop. The inverse functor Cop →C is also denoted by Op.
Thus Op ◦Op = Id.
A contravariant functor F : C →D is the same as a covariant functor F ◦Op :
Cop →D. By default all functors will be covariant, unless explicitly mentioned
otherwise. Contravariant functors will almost always we dealt with by replacing
the source category with its opposite.
Deﬁnition 1.2.1. Let K be a commutative ring. By a central K-ring we mean a
ring A, together with a ring homomorphism K →A, called the structural homo-
morphism, such that the image of K is inside the center of A.
The category of central K-rings, whose morphisms are the ring homomorphisms
f : A →B that respect the structural homomorphisms from K, is denoted by
Rng/c K.
This material will be published by Cambridge University Press as Derived Categories by Amnon
Yekutieli. This prepublication version is free to view and download for personal use only. Not for
redistribution, resale or use in derivative works. c⃝Amnon Yekutieli, 2019.
25
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Traditionally, a central K-ring was called a “unital associative K-algebra”. Of
course all rings and ring homomorphisms are unital. When K = Z, a central K-ring
is just a ring, and then we sometimes use the notation Rng.
Example 1.2.2. Let K be a nonzero commutative ring, and let n be a positive
integer. Then Matn(K), the ring of n × n matrices with entries in K, is a central
K-ring.
Deﬁnition 1.2.3. Let A be a ring. We denote by Mod A, or by the abbreviated
notation M(A), the category of left A-modules.
Rings and modules are very important for us, so let us also put forth the next
convention.
Convention 1.2.4. Below are the default implicit assumptions for linear structures
and operations.
(1) There is a nonzero commutative base ring K (e.g. the ring of integers Z of
a ﬁeld).
(2) The unadorned tensor symbol ⊗means ⊗K.
(3) All rings are central K-rings (see Deﬁnition 1.2.1), all ring homomorphisms
are over K, and all bimodules are K-central.
(4) Generalizing (3), all linear categories are K-linear (see Deﬁnition 2.1.1),
and all linear functors are K-linear (see Deﬁnition 2.5.1).
(5) For a ring A, by all A-modules are left A-modules, unless explicitly stated
otherwise.
Right A-modules are left modules over the opposite ring Aop, and this is the way
we shall most often deal with them. Morphisms in the categories of groups, rings,
A-modules, etc. will usually be called group homomorphism, ring homomorphisms,
A-module homomorphisms, etc., respectively.
Convention 1.2.5. We will try to keep the following font and letter conventions:
• f : C →D is a morphism between objects in a category.
• F : C →D is a functor between categories.
• η : F →G is morphism of functors (i.e. a natural transformation) between
functors F, G : C →D.
• φ, ψ, φi : M →N are morphisms between objects in an abelian category
M.
• F : M →N is a linear functor between abelian categories.
• The category of complexes in an abelian category M is C(M).
• If M is a module category, and M ∈Ob(M), then elements of M will be
denoted by m, n, mi, . . ..
