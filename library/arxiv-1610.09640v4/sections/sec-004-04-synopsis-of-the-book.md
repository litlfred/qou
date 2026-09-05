---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-004-04-synopsis-of-the-book
section_title: "Synopsis of the Book"
section_number: 0.4
pages: 14-22
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
duction.
The book is based on notes for advanced courses given at Ben Gurion University,
in the academic years 2011-12, 2015-16 and 2016-17. The main sources for Sections
1-12 of the book are [62] and [75]; but the DG theory component is absent from
those earlier texts, and is pretty much our own interpretation of folklore results.
The material covered in Sections 13-18 is adapted from research papers.
0.4. Synopsis of the Book.Here is a section-by-section description of the mate-
rial in the book.
Sections 1-2. These sections are pretty much a review of the standard material
on categories and functors, especially abelian categories and additive functors, that
is needed for the book.
There is one new topic here – it is oursheaf tricks, in Subsection 2.4, that are a
“cheap substitute” for the Freyd-Mitchell Theorem, in the sense that they facilitate
proofs of various results in abstract abelian categories, yet they are themselves easy
to prove (and we provide these proofs).
A reader who is familiar with this material can skip these sections; yet we do rec-
ommend looking at our notational conventions, that are spelled out in Conventions
1.2.4 and 1.2.5.
Section 3. A good understanding ofDG algebra(“DG” is short for “diﬀerential
graded”) is essential in our approach to derived categories. By DG algebra we mean
DG rings, DG modules, DG categories and DG functors. There do not exist (to
our knowledge) detailed textbook references for DG algebra. Therefore we have
included a lot of basic material in this section.
We work over a ﬁxed nonzero commutative base ringK (e.g. a ﬁeld or the ring
of integersZ). All linear operations (rings, categories, functors, etc.) are assumed
to be K-linear. A DG module is a module M with a direct sum decomposition
M =⨁
i∈ZMi into submodules, with a diﬀerentialdM of degree 1 satisfying dM◦
dM = 0. The grading on M is called cohomological grading. Tensor products of
14
Derived Categories | Amnon Yekutieli | 14 Apr 2019
DG modules havesigned braiding isomorphisms: for DG modulesM and N, and
for homogeneous elementsm∈Mi and n∈Nj, we deﬁne
brM,N (m⊗n) := (−1)i·j·n⊗m∈N⊗KM.
This braiding is usually referred to as theKoszul sign rule.
A DG categoryis aK-linear categoryC in which the morphism setsHomC(M,N )
are endowed with DG module structures, and the composition functions are DG
bilinear. There are two important sources of DG categories: the categoryC(M) of
complexes in aK-linear abelian categoryM, and the category of DG modules over a
central DGK-ringA (traditionally called a unital associative DGK-algebra). Since
we want to consider both setups, but we wish to avoid repetition, we have devised
a new concept that combines both: the DG categoryC(A, M) of DG A-modules in
M. By deﬁnition, a DGA-module in M is a pair (M,f ), consisting of a complex
M∈C(M), together with a DGK-ring homomorphismf : A→EndM(M). The
morphisms in C(A, M) are the morphism in C(M) that respect the action ofA.
When A =K we are in the caseC(A, M) = C(M), and whenM = ModK we are in
the case C(A, M) = C(A).
A morphismφ:M→N in C(A, M) is called astrict morphismif it is a degree0
cocycle. The strict subcategoryCstr(A, M) is the subcategory ofC(A, M) on all the
objects, and its morphisms are the strict morphisms. The strict category is abelian.
It is important to mention thatC(A, M) has more structure than just a DG cate-
gory. Here the objects have DG structures too, and there is the cohomology functor
H : Cstr(A, M)→Gstr(M), where the latter is the category of graded objects inM.
The cohomology functor determines thequasi-isomorphisms: these are the mor-
phismsψin Cstr(A, M) s.t. H(ψ) is an isomorphism. The set of quasi-isomorphisms
is denoted byS(A, M).
Section4. Wetalkaboutthe translation functorandstandard trianglesin C(A, M).
This section consists mostly of new material, some of it implicit in the paper [25]
on pretriangulated DG categories.
The translation T(M) of a DG module M is the usual one (a shift by 1 in
degree, and diﬀerential−dM). A calculation shows thatT : C(A, M)→C(A, M) is
a DG functor. We introduce the “little t operator”, which is an invertible degree
−1 morphism t : Id →T of DG functors fromC(A, M) to itself. The operator t
facilitates many calculations.
A morphismφ:M→N in Cstr(A, M) gives rise to the standard triangle
M
φ
− →N
eφ
−→Cone(φ)
pφ
−→T(M)
in Cstr(A, M). As a graded module the standard cone is
Cone(φ) :=N⊕T(M) =
N
T(M)

,
written as a column module. The diﬀerential ofCone(φ) is left multiplication by
the matrix of degree1 operators
dCone :=
dN φ◦t−1
M
0 d T(M)

Consider a DG functor
(0.4.1) F : C(A, M)→C(B, N),
where B is another DG ring andN is another abelian category. In Theorem 4.4.3
we show that there is a canonical isomorphism
(0.4.2) τF :F◦T
≃
− →T◦F
15
Derived Categories | Amnon Yekutieli | 14 Apr 2019
of functors Cstr(A, M)→Cstr(B, N), called thetranslation isomorphism. The pair
(F,τF ) is called aT-additive functor. Then, in Theorem 4.5.5, we prove thatF
sends standard triangles inCstr(A, M) to standard triangles inCstr(B, N).
We end this section with several examples of DG functors. These examples are
prototypes – they can be easily extended to other setups.
Section 5. We start with the theory oftriangulated categoriesand triangulated
functors, mainly following [62]. Because the octahedral axiom plays no role in our
book, we give it minimal attention.
The homotopy category K(A, M) has the same objects asC(A, M), and its mor-
phisms are
HomK(A,M)(M,N ) := H0(
HomC(A,M)(M,N )
{
.
There is a functorP : Cstr(A, M)→K(A, M), which is the identity on objects and
surjective on morphisms.
In Subsection 5.4 we prove that the homotopy categoryK(A, M) is triangulated.
Its distinguished trianglesare the triangles that are isomorphic to the images under
the functor P of the standard triangles inCstr(A, M).
Theorem 5.5.1 says that given a DG functorF as in (0.4.1), with translation
isomorphism τF from (0.4.2), the T-additive functor
(0.4.3) (F,τF ) : K(A, M)→K(B, N)
is triangulated. This seems to be a new result, unifying well-known yet disparate
examples.
In Subsection 5.6 we put a triangulated structure on the opposite homotopy
category K(A, M)op. We prove that a contravariant DG functorF, like (0.4.1) but
with source C(A, M)op, induces a contravariant triangulated functor(F,τF ), like
(0.4.3) but with sourceK(A, M)op.
Section 6.In this section we take a close look atlocalization of categories. We give
a detailed proof of the theorem onOre localization(also known as noncommutative
localization). We then prove that the localizationKS of a linear categoryK at a
denominator set S is a linear category too, and the localization functorQ : K→KS
is linear.
Section 7. We begin by proving that ifK is a triangulated category andS⊆K
is a denominator set of cohomological origin, then the localized category KS is
triangulated, and the localization functorQ : K→KS is triangulated.
In the case of the triangulated categoryK(A, M), and the quasi-isomorphisms
S(A, M) in it, we get thederived category
(0.4.4) D(A, M) := K(A, M)S(A,M),
and the triangulated localization functor
(0.4.5) Q : K(A, M)→D(A, M).
We look at the full subcategoryK⋆(A, M) of K(A, M) corresponding to a bound-
edness condition⋆∈{+,−, b}. We prove that when the DG ringA is nonpositive,
the localization D⋆(A, M) of K⋆(A, M) with respect to the quasi-isomorphisms in
it embeds fully faithfully in D(A, M). We also prove that the obvious functor
M→D(M) is fully faithful.
The section ends with a study of the triangulated structure of the opposite
derived category D(A, M)op.
Section 8. In this section we talk aboutderived functors. To make the deﬁni-
tions of derived functors precise, we introduce some2-categorical notationhere (in
Subsections 8.1-8.2).
16
Derived Categories | Amnon Yekutieli | 14 Apr 2019
In Subsection 8.3 we look atabstract derived functors. Namely, K and E are
categories (without any extra structure), F : K →E is a functor, and S ⊆K
is a multiplicatively closed set of morphisms. The localization of K w.r.t. S is
Q : K →KS. A right derived functor of F w.r.t. S is a pair (RF,ηR), where
RF : KS→E is a functor, andηR : F →RF◦Q is a morphism of triangulated
functors. The pair (RF,ηR) has a universal property (it is initial among all such
pairs), making it unique up to a unique isomorphism. The left derived functor
(LF,ηL) is deﬁned similarly.
We provide a general existence theorem for derived functors. For the right de-
rived functor RF, existence is proved whenS is a left denominator set, and there
exists a full subcategoryJ⊆K which isF-acyclic and right-resolves all objects of
K. Likewise, for the left derived functorLF we prove existence whenS is a right
denominator set, and there exists a full subcategoryP⊆K which isF-acyclic and
left-resolves all objects ofK.
In Subsection 8.4 we specialize totriangulated derived functors. Here K and E
are triangulated categories, F : K→E is a triangulated functor, and S⊆K is
a multiplicatively closed set of cohomological origin (i.e.S consists of the quasi-
isomorphisms w.r.t. some cohomological functorH : K→M). The right and left
derived functorsRF, LF : KS→E are deﬁned like in the abstract setting, and their
uniqueness is also proved the same way. Existence requires resolving subcategories
J, P⊆K as above, that are also full triangulated subcategories.
The section is concluded with a discussion ofcontravariant triangulated derived
functors.
Section 9. This section is devoted toDG and triangulated bifunctors. We prove
that a DG bifunctor
F : C(A1, M1)×C(A2, M2)→C(B, N)
induces a triangulated bifunctor
(F,τ1,τ2) : K(A1, M1)×K(A2, M2)→K(B, N).
Then we deﬁne left and right derived bifunctors, and prove their uniqueness and
existence, under suitable conditions. Bifunctors that are contravariant in one or
two of the arguments are also studied.
Section 10. Here we deﬁneK-injective and K-projective objects in K(A, M), and
also K-ﬂatobjects in K(A). These constitute full triangulated subcategories of
K(A, M), and we refer to them asresolving subcategories. The categoryK⋆(A, M)inj
of K-injectives in K⋆(A, M), for a boundedness condition⋆, plays the role of the
category J in Section 8 above, and the category of K-projectivesK⋆(A, M)prj plays
the role of the categoryP there. The K-ﬂat DG modules are acyclic for the tensor
functor.
Furthermore, we prove that the functorsQ : K⋆(A, M)inj→D⋆(A, M) and Q :
K⋆(A, M)prj→D⋆(A, M), see equation (0.4.5), are fully faithful.
Section 11. In this section we proveexistence of K-injective, K-projective and
K-ﬂat resolutions in several important cases ofC⋆(A, M) :
•K-projective resolutions in C−(M), where M is an abelian category with
enough projectives. This is classical (i.e. it is already in [62]).
•K-projective resolutions in C(A), whereA is any DG ring. This includes
the category of unbounded complexes of modules over a ringA.
•K-injective resolutions in C+(M), where M is an abelian category with
enough injectives. This is classical too.
•K-injective resolutions inC(A), whereA is any DG ring.
17
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Our proofs are explicit, and we use limits of complexes cautiously (since this is
known to be a pitfall). We follow several sources: [62], [143], [79], [75] and private
notes provided by B. Keller.
Section12. Thissectionisquitevaried. InSubsections12.2-12.3thereisadetailed
look at the derived bifunctorsRHom(−,−) and (−⊗L−).
Next, in Subsection 12.4, we studycohomological dimensions of functors. This is
a reﬁnement of the notion ofway-out functorfrom [62]. It is used in Subsection 12.5
to prove a few theorems about triangulated functors, such as a suﬃcient condition
for a morphismζ:F→G of triangulated functors to be an isomorphism.
In Subsections 12.6-12.7 we study several adjunction formulas that involve the
bifunctors RHom(−,−) and (−⊗L−). We deﬁnederived forward adjunctionand
derived backward adjunction. These adjunction formulas hold for arbitrary DG
rings (without any commutativity or boundedness conditions). We prove that if
A→B is aquasi-isomorphism of DG rings, then the restriction functorRestB/A :
D(B)→D(A)is an equivalence, and it respects the derived bifunctorsRHom(−,−)
and (−⊗L−).
Resolutions of DG rings are important in several contexts. In Subsection 12.8
we provide a full proof that given a DGK-ring A, there exists anoncommutative
semi-free DG ring resolution˜A→A overK.
In Subsection 12.9 there is a very general theorem providing suﬃcient conditions
for thederived tensor-evaluation morphism
(0.4.6) evR,L
L,M,N : RHomA(L,M )⊗L
BN→RHomA(L,M⊗L
BN)
in D(K) to be an isomorphism. HereA and B are DGK-rings, L∈D(A), M∈
D(A⊗KBop) and N∈D(B).
Lastly, in Subsection 12.10 we present some adjunction formulas that pertain
only to weakly commutative DG rings.
Section 13. This section starts (in the ﬁrst three subsections) by retelling the
material in [62] ondualizing complexesand residue complexesover noetherian com-
mutative rings.
A complexR∈D(A) is calleddualizing if it has ﬁnitely generated cohomology
modules, ﬁnite injective dimension, and thederived Morita property, which says
that thederived homothety morphism
(0.4.7) hmR
R :A→RHomA(R,R )
in D(A) is an isomorphism. (This is a variant of the derived Hom-evaluation mor-
phism evR
M from equation (0.2.15), withM =A.)
To a dualizing complexR we associate theduality functor
D := RHomA(−,R ) : D(A)op→D(A).
The duality functor induces an equivalence of triangulated categoriesD : Df(A)op
→Df(A). Here Df(A)is the full subcategory ofD(A)on the complexes with ﬁnitely
generated cohomology modules.
A residue complex is a dualizing complexK that consists of injective modules
of the correct multiplicity in each degree. IfR =K is a residue complex, then the
associated duality functor isD = HomA(−,K).
We prove uniqueness of dualizing complexes over a noetherian commutative ring
A (up to the obvious twists), and existence whenA is essentially ﬁnite type over a
regular noetherian ringK. In this book the adjective “regular noetherian” includes
the condition thatK has ﬁnite Krull dimension.
There is a stronger uniqueness property for residue complexes. Residue com-
plexes exist whenever dualizing complexes exist: given a dualizing complexR, its
18
Derived Categories | Amnon Yekutieli | 14 Apr 2019
minimal injective resolutionK is a residue complex. To understand residue com-
plexes we review theMatlis classiﬁcation of injectiveA-modules.
In remarks we provide sketches of Matlis Duality, Local Duality and the inter-
pretation of Cohen-Macaulay complexes as perverse modules.
In the last two subsections we talk aboutVan den Bergh rigidity. Let K be a
regular noetherian ring, and letA be a ﬂat essentially ﬁnite type (FEFT)K-ring.
(The ﬂatness condition is just to simplify matters; see Remark 13.4.24.) Given a
complex M∈D(A), itssquare relative toK is the complex
SqA/K(M) := RHomA⊗KA(A,M⊗L
KM)∈D(A).
We prove thatSqA/K is aquadratic functor. A rigid complex overA relative toK
is a pair(M,ρ), whereM∈D(A) and ρ: M
≃
− →SqA/K(M) is an isomorphism in
D(A), called arigidifying isomorphism. Given another rigid complex(N,σ), arigid
morphism between them is a morphismφ:M→N in D(A) such that the diagram
(0.4.8) M
φ

ρ // SqA/K(M)
SqA/K(φ)

N σ // SqA/K(N)
in D(A) is commutative. We prove that if(M,ρ) is a rigid complex such thatM
has the derived Morita property, then the only rigid automorphism of(M,ρ) is the
identity.
A rigid dualizing complex overA relative toK is a rigid complex(R,ρ) such that
R is a dualizing complex. We prove that ifA has a rigid dualizing complex, then it
is unique up to a unique rigid isomorphism. Existence of a rigid dualizing complex
is harder to prove, and we just give a reference to it.
A rigid residue complex overA relative toK is a rigid complex(K,ρ) such that
K is a residue complex. These always exist, and they are unique in the following
very strong sense: if(K′,ρ′) is another rigid residue complex, then there is a unique
isomorphism φ:K
≃
− →K′in Cstr(A), such that Q(φ) is a rigid isomorphism in
D(A).
We end this section with two remarks (Remark 13.5.18 and 13.5.19) that ex-
plain how rigid residue complexes allow a new approach toresidues and duality on
schemes and Deligne-Mumford stacks, with references.
Section 14.We begin (in Subsection 14.1) with a systematic study ofalgebraically
perfect DG modules over a NC DG ringA. The abbreviation “NC” stands for
“noncommutative”. By deﬁnition, a DG moduleL∈D(A) is called algebraically
perfectifitbelongstothesaturatedfulltriangulatedsubcategoryof D(A)generated
by the DG moduleA. We give several characterizations of algebraically perfect DG
modules; one of them is thatL is acompact objectof D(A). WhenA is a ring, we
prove thatL is algebraically perfect if and only if it is isomorphic, inD(A), to a
bounded complex of ﬁnitely generated projectiveA-modules.
In Subsection 14.2 we prove the followingDerived Morita Theorem, Theorem
14.2.29: Let E⊆D(A) be a full triangulated subcategory which is closed under
inﬁnitedirectsums, letP beacompactgeneratorof EwhichiseitherK-projectiveor
K-injective, and letB := EndA(P )op. Then the functorRHomA(P,−) : E→D(B)
is an equivalence of triangulated categories, with quasi-inverseP⊗L
B (−).
From Subsection 14.3 to the end of this section we assume that the DG rings in
question are K-ﬂat over the base ringK. Note that every DGK-ring A admits a
NC semi-free DG ring resolution˜A→A. The DG ring ˜A is K-ﬂat overK, and the
restriction functor D(A)→D( ˜A) is an equivalence of triangulated categories; so
19
Derived Categories | Amnon Yekutieli | 14 Apr 2019
the ﬂatness restriction can be circumvented. Subsection 14.3 contains some basic
constructions of derived functors between categories of DG bimodules (that require
the ﬂatness over the base ring).
Next, in Subsection 14.4, we deﬁnetilting DG bimodules. A DG bimodule
T ∈D(B⊗K Aop) is called a tilting DGB-A-bimodule if there exists someS∈
D(A⊗K Bop) with isomorphisms S⊗L
B T ∼= A in D(Aen) and T⊗L
A S ∼= B in
D(Ben). Here Aen :=A⊗KAop is theenveloping DG ring ofA, and likewiseBen.
Among other results, we prove thatT ∈D(B⊗KAop) is tilting if and only ifT
is a compact generator on theB side (i.e. it is a compact generator of D(B)),
and it has theNC derived Morita propertyon the B side, namely the canonical
morphism A→RHomB(T,T ) in D(Aen) is an isomorphism. We also prove the
Rickard-Keller Theorem, asserting that ifA and B are rings, and there exists a
K-linear equivalence of triangulated categoriesD(A)→D(B), then there exists a
tilting DGB-A-bimodule.
Lastly, in Subsection 14.5, we introduce theNC derived Picard groupDPicK(A)
of a ﬂatK-ring A. The structure of this group is calculated whenA is either local
or commutative.
Section 15.This section, as well as Sections 16 and 17, are onalgebraically graded
rings, which is our name forZ-graded rings that have lower indices and do not
involve the Koszul sign rule. (This is in contrast with the cohomologically graded
rings mentioned above, that underly DG rings). Simply put, these are the usual
gradedringsthatoneencountersintextbooksoncommutativeandnoncommutative
algebra. With few exceptions, the base ringK in the four ﬁnal sections of the book
is a ﬁeld.
Let A =⨁
i∈ZAi be an algebraically graded centralK-ring. In Section 15 we
deﬁne the category of algebraically gradedA-modules M(A, gr). Its objects are
the algebraically graded (left)A-modules M =⨁
i∈ZMi, and the homomorphisms
are the degree 0 A-linear homomorphisms. It is aK-linear abelian category. We
talk about ﬁniteness in the algebraically graded context, and about various kinds
of homological properties, such asgraded-injectivity.
The category of complexes with entries in M(A, gr) is the DG category
C(A, gr) := C
(
M(A, gr)
{
. Its objects are bigraded: a complex M ∈C(A, gr)
has a direct sum decomposition M = ⨁
i,jMi
j into K-modules. Here i is the
cohomological degree andj is the algebraic degree. The diﬀerential goes like this:
dM :Mi
j→Mi+1
j .
Just like for any other abelian category, we have the derived categoryD(A, gr) :=
D
(
M(A, gr)
{
. This is a triangulated category. We present (quickly) the alge-
braically graded variants of K-projective resolutions etc., and the relevant derived
functors.
Special emphasis is given toconnected graded rings. An algebraically graded ring
A is called connected ifA =⨁
i∈NAi, A0 =K, and eachAi is a ﬁniteK-module.
In a connected graded ringA there is theaugmentation ideal m :=⨁
i>0Ai. We
view A/m∼=K as a gradedA-bimodule.
Amongtheconnectedgradedringswesingleoutthe Artin-Schelter regular graded
rings. A noetherian connected graded ringA is called AS regular if it has ﬁnite
graded global dimension, and if there are isomorphisms
(0.4.9) RHomA(K,A )∼= RHomAop(K,A )∼=K(l)[−n]
in D(K) for some integersl and n. One of the results is that ifA is a noetherian
connected graded ring,a∈A is a regular central homogeneous element of positive
degree, and the ringB :=A/(a) is AS regular, thenA is also AS regular.
20
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Section 16.LetA be a connected graded ring over the base ﬁeldK, with augmen-
tation ideal m. In this section we studyderived m-torsion, both for complexes of
graded A-modules and for complexes of graded bimodules. By this we mean that,
taking a second graded ringB, we look at the triangulated functor
RΓ m : D(A⊗KBop, gr)→D(A⊗KBop, gr).
One of the main results (Theorem 16.4.3) says that ifA is a left noetherian
connected graded ring, and if the functorRΓ m has ﬁnite cohomological dimension,
then there is a functorial isomorphism
(0.4.10) evR,L
m,M :P⊗L
AM
≃
− →RΓ m(M)
for M∈D(A⊗KBop, gr), where
(0.4.11) P := RΓ m(A)∈D(Aen, gr).
We also prove theNC MGM Equivalence in the connected graded context (see
Theorem 16.6.32).
Theχconditionof M. Artin and J.J. Zhang is introduced in Subsection 16.5. We
study how this condition interacts with derived torsion. To a complex of gradedA-
bimodules, namelyanobjectof D(Aen, gr), wecanalsoapplyderived m-torsionfrom
the right side, thus obtaining a complexRΓ mop(M)∈D(Aen, gr). Theorem 16.5.27
says that ifA is a noetherian connected graded ring of ﬁnite local cohomological
dimension (i.e. both functorsRΓ m and RΓ mop have ﬁnite cohomological dimension),
that satisﬁes theχcondition, then there is a functorial isomorphism
(0.4.12) ϵM : RΓ m(M)
≃
− →RΓ mop(M)
in D(Aen, gr) for all complexesM∈D(Aen, gr) whose cohomologies are ﬁniteA-
modules on both sides. We call this phenomenonsymmetric derived m-torsion.
Section 17. The focus of this section is on balanced NC dualizing complexes,
following [161]. LetA be a noetherian connected graded ring over the base ﬁeldK.
A complexR∈Db(Aen, gr) is called agraded NC dualizing complexif it satisﬁes
these three conditions:
(i) The bimodules Hq(R) are ﬁnitely generatedA-modules on both sides.
(ii) The complexR has ﬁnite graded injective dimension on both sides.
(iii) The complexR has the NC derived Morita property on both sides; namely
the canonical morphismsA→RHomA(R,R ) and A→RHomAop(R,R ) in
D(Aen, gr) are isomorphisms.
A balanced NC dualizing complex overAis a pair(R,β), whereR is a graded NC
dualizing complex overAwith symmetric derivedm-torsion, andβ: RΓ m(R)
≃
− →A∗
is an isomorphism inD(Aen, gr), called abalancing isomorphism. Here and later we
write M∗:= HomK(M,K), the gradedK-linear dual of a graded moduleM. The
graded bimoduleA∗is a graded-injectiveA-module on both sides.
To a balanced dualizing complexR we associate the duality functors
DA := RHomA(−,R ) : D(A, gr)op→D(Aop, gr)
and
DAop := RHomAop(−,R ) : D(Aop, gr)op→D(A, gr).
When restricted to the subcategories of complexes with ﬁnitely generated cohomol-
ogy modules, this gives an equivalence
(0.4.13) DA : Df(A, gr)op→Df(Aop, gr)
with quasi-inverseDAop.
A balanced dualizing complex(R,β) is unique up to a unique isomorphism (The-
orem 17.2.4), and it satisﬁes the NC Local Duality Theorem 17.2.7. Results of
21
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Yekutieli, Zhang and M. Van den Bergh say that a noetherian connected graded
ring A has a balanced dualizing complex if and only ifA satisﬁes theχcondition
and has ﬁnite local cohomological dimension. The formula for the balanced dual-
izing complex isR := P∗, where P is the complex from (0.4.11). See Corollary
17.3.24.
IfA is an AS regular (or more generally AS Gorenstein) graded ring, then it has
a balanced dualizing complexR =A(φ,−l)[n]. Herel and n are the integers from
formula (0.4.9), andφis a graded ring automorphism ofA. See Corollary 17.3.14.
Section 18.The ﬁnal section of the book deals withNC rigid dualizing complexes.
LetA be a NC centralK-ring (whereK is the base ﬁeld). ANC dualizing complex
overA is a complexR∈Db(Aen) whose cohomology bimodules are ﬁnitely gener-
ated on both sides; it has ﬁnite injective dimension on both sides; and it has the
NC derived Morita property on both sides. This is a modiﬁcation of the graded
deﬁnition given above.
Let M∈D(Aen). The NC squareof M is the complex
(0.4.14) SqA/K(M) := RHomAen(A,R⊗KR)∈D(Aen).
This formula is ambiguous, because the complex ofK-modules R⊗K R has on
it four distinct commuting actions by the ringA; but formula (0.4.14) is made
precise at the beginning of Subsection 18.2. Arigidifying isomorphism for M is
an isomorphismρ:M
≃
− →SqA/K(M) in D(Aen), and the pair(M,ρ) is aNC rigid
complex. A NC rigid dualizing complex is a NC rigid complex(R,ρ) such thatR
is a NC dualizing complex.
The deﬁnition of NC rigid dualizing complex was introduced by Van den Bergh
in his paper [153]. He also proved that a rigid NC dualizing complex is unique up to
isomorphism. Later, in [165], it was proved that this isomorphism is itself unique.
We reproduce these results in Subsection 18.2.
We also give Van den Bergh’s theorem on the existence of NC rigid dualizing
complexesfrom[153], withafullproof. ThisisTheorem18.5.4. Hereiswhatitsays:
Suppose the ringA admits a ﬁltrationF ={Fj(A)}j≥−1 such that the associated
graded ringGrF (A) is noetherian connected and has a balanced dualizing complex.
Then A has a rigid dualizing complex.
An important special case of the Van den Bergh Existence Theorem is Theorem
18.6.11. It says that if the graded ringGrF (A) from the previous paragraph is AS
regular, then the rigid NC dualizing complex ofA is R = A(µ)[n], where µis a
K-ring automorphism ofA that respects the ﬁltrationF, andn is an integer. The
automorphism ν:= µ−1 is called theNakayama automorphism of A. In modern
terminology the ringA is called ann-dimensional twisted Calabi-Yau ring.
Finally we state and prove theVan den Bergh Duality Theoremfor Hochschild
(co)homology, andgiveanexampleofa Calabi-Yau categoryoffractionaldimension.
