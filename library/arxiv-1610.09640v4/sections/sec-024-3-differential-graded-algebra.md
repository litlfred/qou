---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-024-3-differential-graded-algebra
section_title: "Differential Graded Algebra"
section_number: 3
pages: 51-59
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
Recall that according to Convention 1.2.4 there is a nonzero commutative base
ring K. By default all rings are K-central, all linear categories areK-linear, all
linear operations (such as ring homomorphisms and linear functors) areK-linear,
and⊗means⊗K.
Throughout “DG” stands for “diﬀerential graded”. There is some material about
DG algebra in a few published references, such as the book [101] and the papers
[79], [151], [133] and [12]. However, for our purposes we need a much more detailed
understanding of this theory, and this is what the present section provides.
3.1. Graded Algebra. Before entering the DG world, it is good to understand
the graded world.
Deﬁnition 3.1.1.A cohomologically gradedK-module is aK-module M equipped
with a direct sum decompositionM =⨁
i∈ZMi intoK-submodules. TheK-module
Mi is called the homogeneous component of cohomological degreei of M. The
nonzero elements ofMi are calledhomogeneous elements of cohomological degreei.
From here until Section 15 we are going to respect the following convention,
which will simplify the discussion.
Convention 3.1.2.By “gradedK-module” we mean acohomologically gradedK-
module, as deﬁned above.
In Section 15 we shall introducealgebraically graded rings and modules, and then
we shall have to make a careful distinction between these notions. See Remark
3.1.25 regarding commutativity in the two settings.
Suppose M and N are gradedK-modules. For an integeri let
(M⊗N)i :=
⨁
j∈Z
(Mj⊗Ni−j).
Then
(3.1.3) M⊗N =
⨁
i∈Z
(M⊗N)i
is a gradedK-module.
AK-linear homomorphismφ:M→N is said to behomogeneous of degreei if
φ(Mj)⊆Nj+i for allj. We denote by HomK(M,N )i the K-module of degreei
homomorphisms M→N. In other words
(3.1.4) HomK(M,N )i :=

j∈Z
HomK(Mj,N j+i).
Deﬁnition 3.1.5.Let M and N be gradedK-modules.
(1) The module of gradedK-linear homomorphismsfromM toN is the graded
K-module
HomK(M,N ) :=
⨁
i∈Z
HomK(M,N )i.
(2) A degree 0 homomorphism φ:M→N is called astrict homomorphism of
gradedK-modules.
ThismaterialwillbepublishedbyCambridgeUniversityPressas Derived CategoriesbyAmnon
Yekutieli. This prepublication version is free to view and download for personal use only. Not for
redistribution, resale or use in derivative works.c© Amnon Yekutieli, 2019.
51
Derived Categories | Amnon Yekutieli | 14 Apr 2019
If M0,M 1,M 2 are gradedK-modules, andφk :Mk→Mk+1 areK-linear homo-
morphisms of degreesik, thenφ1◦φ0 :M0→M2 is aK-linear homomorphism of
degree i0 +i1. The identity automorphismidM :M→M has degree 0.
Deﬁnition 3.1.6.The strict category of gradedK-modulesis the categoryGstr(K),
whose objects are the cohomologically gradedK-modules, and whose morphisms are
the strict homomorphisms of cohomologically gradedK-modules.
It is easy to see thatGstr(K) is aK-linear abelian category – the kernels and
cokernels are degreewise.
Remark 3.1.7. Let Ungr : Gstr(K) →M(K) be the functor that forgets the
grading. It is faithful, but often not full. Namely the obvious homomorphism
Ungr
(
HomK(M,N )
{
→HomK
(
Ungr(M), Ungr(N)
{
is injective but not bijective. See Remark 15.1.11 for a discussion.
The tensor operation (−⊗−) from (3.1.3) makes Gstr(K) into a monoidal K-
linear category, with monoidal unitK. This means that the bifunctor
(−⊗−) : Gstr(K)×Gstr(K)→Gstr(K)
satisﬁes the monoidal axioms (associativity up to a trifunctorial cocycle, etc., see
[102, Chapter XI]), and it isK-bilinear. Moreover, given M,N ∈Gstr(K), let us
deﬁne thebraiding isomorphism
(3.1.8) brM,N :M⊗N
≃
− →N⊗M,
(3.1.9) brM,N (m⊗n) := (−1)i·j·n⊗m
for homogeneous elementsm∈Mi andn∈Nj. Because brN,M◦brM,N = idM⊗N,
this makes Gstr(K) into a symmetric monoidal K-linear category. The braiding
isomorphism (3.1.9) is often called theKoszul sign rule. See Remark 3.1.25 for a
background discussion.
Exercise 3.1.10. For an integerl≥1 letτbe a permutation of the set{1,...,l}.
Show that for everyM1,...,Ml∈Gstr(K) there is an isomorphism
brτ:M1⊗···⊗Ml
≃
− →Mτ(1)⊗···⊗Mτ(l)
in Gstr(K), which is functorial in the sequence of objects{Mi}i=1,...,l, functorial in
the permutationτ, monoidal (for a partitionl =l1 +l2), and brτ= brM1,M2 when
l = 2 and τis the transposition. See [102, Theorem XI.1.1] or [17] for the answer.
Deﬁnition 3.1.11.A cohomologically graded centralK-ring is a centralK-ringA,
equipped with a direct sum decompositionA =⨁
i∈ZAi intoK-submodules, such
that 1A∈A0, andAi·Aj⊆Ai+j.
Deﬁnition 3.1.12.LetA andB be cohomologically graded centralK-rings. Aho-
momorphism of cohomologically graded centralK-rings is aK-ring homomorphism
f :A→B that respects the gradings, namelyf(Ai)⊆Bi.
The category of cohomologically graded centralK-rings is denoted byGRng/cK.
As always for ring homomorphisms,f must preserve units, i.e.f(1A) = 1B. Note
thatK itself is a graded ring, concentrated in degree0; and it is the initial object
of GRng/cK.
To simplify the discussion, we shall follow the next convention (until Section 15).
Convention 3.1.13. By “graded ring” we mean acohomologically graded central
K-ring, as deﬁned above.
52
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Recall that by Convention 1.2.4, all ring homomorphisms, and that includes
graded rings, are overK.
Example 3.1.14. Let M be a gradedK-module. Then the graded module
EndK(M) := HomK(M,M ) =
⨁
i∈Z
HomK(M,M )i,
with the operation of composition, is a gradedK-ring.
The prototypical manifestation of the Koszul sign rule is the next deﬁnition.
Deﬁnition 3.1.15.Let A = ⨁
i∈ZAi be a gradedK-ring. We say that A is a
weakly commutative graded ringif b·a = (−1)i·j·a·b for alla∈Ai and b∈Aj.
Remark 3.1.16. Let us give a categorical explanation of Deﬁnition 3.1.15, using
the symmetric monoidal structure ofGstr(K).
The general categorical way to deﬁne aring objectin the symmetric monoidal
linear category
(
Gstr(K),⊗,K, br
{
is as an objectA∈Gstr(K) equipped with a
multiplication morphism m : A⊗A→A and a unit morphismu : K→A, such
that the triple(A, m, u) obeys the ring axioms. In our case it is precisely Deﬁnition
3.1.11.
The categorical commutativity conditionfor the ring object(A, m, u) is that the
diagram
A⊗A
m
""
br

A⊗A m //A
in Gstr(K)iscommutative. Thisiswhatweakcommutativityis, inDeﬁnition3.1.15.
Here is a deﬁnition similar to Deﬁnition 3.1.15.
Deﬁnition 3.1.17.Let A =⨁
i∈ZAi be a graded ring.
(1) Homogeneous elementsa∈Ai andb∈Aj are said tograded-commutewith
each other ifb·a = (−1)i·j·a·b.
(2) A homogeneous element a ∈Ai is called a graded-central element if it
graded-commutes with all homogeneous elements ofA.
(3) The graded-centerofA is theK-submodule Cent(A)⊆A generated by the
homogeneous graded-central elements.
Exercise 3.1.18. Let A be a graded ring. Show that:
(1) Cent(A) is a graded subring ofA, it is weakly commutative, and it contains
the image of the base ringK.
(2) A is weakly commutative iﬀCent(A) =A.
Below are several sign formulas that are more subtle consequences of the Koszul
sign rule. They can be traced – with eﬀort – to thebiclosed monoidal structureof
Gstr(K), namely to the interaction between the bifunctors(−⊗−)and HomK(−,−).
Suppose that fork = 0, 1 we are given gradedK-module homomorphismsφk :
Mk→Nk of degreesik. Then the homomorphism
φ0⊗φ1∈HomK
(
(M0⊗M1,N 0⊗N1
{i0+i1
acts on a tensorm0⊗m1∈M0⊗M1, withmk∈Mjk
k , like this:
(3.1.19) (φ0⊗φ1)(m0⊗m1) := (−1)i1·j0·φ0(m0)⊗φ1(m1)∈N0⊗N1.
The rule of thumb explaining this formula is thatφ1 and m0 were transposed.
53
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Suppose we are given gradedK-module homomorphisms φ0 : N0 →M0 and
φ1 :M1→N1 of degreesi0 and i1. Then the homomorphism
Hom(φ0,φ1)∈HomK
(
HomK(M0,M 1), HomK(N0,N 1)
{i0+i1
acts onγ∈HomK(M0,M 1)j as follows: for an elementn0∈Nk
0 we have
(3.1.20) Hom(φ0,φ1)(γ)(n0) := (−1)i0·(i1+j)(φ1◦γ◦φ0)(n0)∈Nk+i0+i1+j
1 .
The sign is becauseφ0 jumped acrossφ1 and γ.
Deﬁnition 3.1.21.Let A and B be graded rings. ThenA⊗B is a graded ring,
with multiplication
(a0⊗b0)·(a1⊗b1) := (−1)i1·j0·(a0·a1)⊗(b0·b1)
for elementsak∈Aik and bk∈Bjk.
We shall require another notion of commutativity, that is not of categorical
nature.
Deﬁnition 3.1.22.Let A =⨁
i∈ZAi be a graded ring.
(1) Thegradedring Aiscalled strongly commutativeifitisweaklycommutative
(Deﬁnition 3.1.15), and alsoa2 = 0 if a∈Ai and i is odd.
(2) The graded ringA is callednonpositive if Ai = 0 for alli> 0.
(3) The graded ringA is called acommutative graded ringif it is nonpositive
and strongly commutative.
This deﬁnition is taken from [173]. In [188] the term “super-commutative” was
used instead of “strongly commutative”. The name “strongly commutative” was
suggested to us by J. Palmieri.
Example 3.1.23. By agraded setwe mean a setX partitioned asX =∐
i∈ZXi.
The elements ofXi are called variables of degreei. The noncommutative graded
polynomial ring on the graded setX is the graded ringK⟨X⟩, which is the free
gradedK-module spanned by the monomials (i.e. words)x1···xn in the elements
of X, and its multiplication is by concatenation of monomials.
The strongly commutative graded polynomial ringon the graded setX is the
graded ringK[X] :=K⟨X⟩/I, whereI is the two-sided ideal ofK⟨X⟩generated by
the elementsy·x−(−1)i·j·x·y for all variablesx∈Xi and y∈Xj, together with
the elementsz·z for allz∈Xk and oddk. This is a strongly commutative graded
ring.
Exercise 3.1.24. Show that ifA and B are weakly (resp. strongly) commutative
graded rings, then so isA⊗B.
Remark 3.1.25. Weak commutativity is the obvious commutativity condition
in the cohomologically graded setting, when the Koszul sign rule is imposed; see
Remark 3.1.16. Of course there are many instances of commutative graded rings
that do not involve the Koszul sign rule; see e.g. [46] or [105]. In our book we call
them algebraically graded rings, and they are studied in Sections 15-17.
Strong commutativity has another reason. Its role is to guarantee that the
strongly commutative graded polynomial ringK[X] from Example 3.1.23 above
will be a graded-free K-module. Without this condition, the square of an odd
variablez would be a nonzero2-torsion element.
Of course, if 2 is invertible inK (e.g. ifK containsQ), then weak and strong
commutativity of a graded centralK-ring coincide. Since most texts dealing with
DG rings assume thatQ⊆K, the subtle distinction we make is absent from them.
54
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Remark 3.1.26. Let A = ⨁
i∈ZAi be a weakly commutative graded ring, and
assumeA has nonzero odd elements. Then, after we forget the grading, the ringA
is no longer commutative (except in special cases, like in characteristic2).
This phenomenon will reappear often in the study of DG algebra.
Remark 3.1.27. The origin of the Koszul sign rule, predating the work of J.L.
Koszul, appears to be in the formula for the diﬀerentiald of the tensor product of
two complexes, that occurs in classical homological algebra (and is repeated here
in Deﬁnition 3.2.3). Without the sign we won’t haved◦d = 0.
In his thesis [89], Koszul talks about the sign rule explicitly, when discussing the
Chevalley-Eilenberg complex. See [17] for a detailed study of the Koszul sign rule
and its group-theoretic interpretation.
It should be noted that there are some sign inconsistencies in the book [62]. The
Koszul sign rule could have prevented them.
In our book we made a strenuous eﬀort to have correct (namely consistent) signs.
This did not always produce satisfactory outcomes – for instance, in the context
of the triangulated structure of the opposite homotopy category, as explained in
Remark 5.6.12.
Deﬁnition 3.1.28.Let A be a graded ring. Agraded leftA-module is a leftA-
module M, equipped with aK-module decomposition M = ⨁
i∈ZMi, such that
Ai·Mj⊆Mi+j for alli,j.
We can also talk about graded rightA-modules, and graded bimodules. But our
default option (see Convention 1.2.4) is that modules are left modules.
Exercise 3.1.29. Let M be a gradedK-module, A a graded centralK-ring, and
f :A→EndK(M) a homomorphism inGRng/cK.
(1) Show thatM becomes a gradedA-module, with actiona·m :=f(a)(m).
(2) Show that every gradedA-module structure onM, that is consistent with
the given gradedK-module structure, arises this way.
Lemma 3.1.30. Let A be a graded ring, letM be a graded rightA-module, and
let N be a graded leftA-module. Then the K-module M⊗AN has a direct sum
decomposition
M⊗AN =
⨁
i∈Z
(M⊗AN)i,
where (M⊗AN)i is theK-linear span of the tensorsm⊗n, for allj∈Z, m∈Mj
and n∈Ni−j.
Proof. There is a canonical surjection ofK-modulesM⊗N→M⊗AN. Its kernel is
theK-submoduleL⊆M⊗N generated by the elements(m·a)⊗n−m⊗(a·n), for
m∈Mj,n∈Nk anda∈Al. SoL is a graded submodule ofM⊗N, and therefore
so is the quotient. Finally, by formula (3.1.3) thei-th homogeneous component of
M⊗AN is precisely (M⊗AN)i. □
Deﬁnition 3.1.31.Let A be a graded ring, and letM,N be gradedA-modules.
For eachi∈Z deﬁneHomA(M,N )i to be the subset ofHomK(M,N )i consisting
of the homomorphismsφ: M →N such thatφ(a·m) = (−1)i·k·a·φ(m) for all
a∈Ak. Next deﬁne the gradedK-module
HomA(M,N ) :=
⨁
i∈Z
HomA(M,N )i.
Suppose C is aK-linear category (Deﬁnition 2.1.1). Since the composition of
morphisms isK-bilinear, for every triple of objectsM0,M 1,M 2∈C, composition
can be expressed as aK-linear homomorphism
HomC(M1,M 2)⊗HomC(M0,M 1)− →HomC(M0,M 2),
55
Derived Categories | Amnon Yekutieli | 14 Apr 2019
φ1⊗φ0↦→φ1◦φ0. We refer to it as the composition homomorphism. It will be
used in the following deﬁnition.
Deﬁnition 3.1.32.A gradedK-linear categoryis aK-linear category C, endowed
with a grading on each of theK-modules HomC(M0,M 1). The conditions are these:
(a) For every objectM, the identity automorphismidM has degree 0.
(b) Foreverytripleofobjects M0,M 1,M 2∈C, thecompositionhomomorphism
HomC(M1,M 2)⊗HomC(M0,M 1)− →HomC(M0,M 2)
is a strict homomorphism of gradedK-modules.
Initem(b)weusethegradedmodulestructureonatensorproductfromequation
(3.1.3). A morphismφ∈HomC(M0,M 1)i is called a morphism of degreei.
Deﬁnition 3.1.33.Let C be a gradedK-linear category. Thestrict subcategory of
C is the subcategoryStr(C) on all objects ofC, whose morphisms are the degree0
morphisms of C.
Example 3.1.34.LetAbe a graded ring. DeﬁneGModAto be the category whose
objects are the gradedA-modules. For M,N ∈GModA, the set of morphisms is
the gradedK-module HomGModA(M,N ) := HomA(M,N ) from Deﬁnition 3.1.31.
Then GModA is a gradedK-linear category. The morphisms in the subcategory
GModstrA := Str( GModA) are the strict homomorphisms of gradedA-modules.
We often write G(A) := GModA and Gstr(A) := GModstrA. In the special case
A =K, the categoryGstr(K) already appeared in Deﬁnition 3.1.6.
Remark 3.1.35. The name “strict homomorphism of graded modules”, and the
corresponding notations GModstrA = Gstr(A), are new. We introduced them to
distinguish the abelian categoryGModstrA from the graded categoryGModA that
contains it. See Deﬁnitions 3.4.1 and 3.4.6 for the DG versions of these notions.
Deﬁnition 3.1.36.Let C and D be gradedK-linear categories. A functorF : C→
D is called agradedK-linear functorif it satisﬁes this condition:
⊿ For every pair of objectsM0,M 1∈C, the function
F : HomC(M0,M 1)→HomD
(
F (M0),F (M1)
{
is a strict homomorphism of gradedK-modules.
Convention 3.1.37. To simplify the terminology, we shall often use the expres-
sions “graded category” and “graded functor” as abbreviations for “gradedK-linear
category” and “gradedK-linear functor”, respectively.
Example 3.1.38. Let A be a graded ring. We can viewA as a category A with
a single object, and it is a graded category. Iff : A→B is a homomorphism
of graded rings, then passing to single-object categories we get a graded functor
F : A→B.
Recall that “morphism of functors” is synonymous with “natural transforma-
tion”.
Deﬁnition 3.1.39.Let F,G : C→D be graded functors between graded cate-
gories, and let i∈Z. A degreei morphism of graded functorsη: F →G is a
collection η={ηM}M∈C of morphismsηM∈HomD
(
F (M),G (M)
{i
, such that for
every morphismφ∈HomC(M0,M 1)j there is equality
G(φ)◦ηM0 = (−1)i·j·ηM1◦F (φ)
inside HomD
(
F (M0),G (M1)
{i+j
.
56
Derived Categories | Amnon Yekutieli | 14 Apr 2019
If i is odd in the deﬁnition above, then after we forget the grading,η: F →
G is usually no longer a morphism of functors; this is another instance of the
phenomenon mentioned in Remark 3.1.26.
Deﬁnition 3.1.40.Let M be an abelian category. A graded object in M is a
collection{Mi}i∈Z of objectsMi∈M.
Because we did not assume thatM has countable direct sums, the graded objects
are “external” toM; cf. Exercise 3.1.44.
Suppose M ={Mi}i∈Z and N ={Ni}i∈Z are graded objects in M. For an
integeri we deﬁne theK-module
(3.1.41) HomM(M,N )i :=

j∈Z
HomM(Mj,N j+i).
We get a gradedK-module
(3.1.42) HomM(M,N ) :=
⨁
i∈Z
HomM(M,N )i.
Deﬁnition 3.1.43.Let M be an abelian category. Thecategory of graded objects
in M is the graded linear categoryG(M), whose objects are the graded objects in
M, and the morphism sets are the graded modules
HomG(M)(M,N ) := HomM(M,N )
from equation (3.1.42). The composition operation is the obvious one.
Exercise 3.1.44. Suppose M = M(A), the category of modules over a centralK-
ring A. For everyM ={Mi}i∈Z∈G(M) let F (M) :=⨁
i∈ZMi. Then F (M) is a
graded A-module, as discussed earlier, soF (M) is an object of the categoryG(A)
from Example 3.1.34. Prove thatF : G(M)→G(A) is an isomorphism of graded
categories.
In the next deﬁnition we combine graded rings and linear categories, to concoct
a new hybrid.
Deﬁnition 3.1.45.Let M be an abelian category, and letA be a graded ring.
A graded A-module in M is an object M ∈G(M), together with a graded ring
homomorphism f :A→EndM(M). The set of gradedA-modules in M is denoted
by G(A, M).
What the deﬁnition says is that an elementa ∈Ai gives rise to a degree i
endomorphism f(a) of the graded objectM ={Mj}j∈Z. In turn, this means that
for every j, f(a) : Mj →Mj+i is a morphism in M. The operation f satisﬁes
f(1A) = idM and f(a1·a2) =f(a1)◦f(a2).
Example 3.1.46. If A = K, then G(A, M) = G(M); and if M = ModK, then
G(A, M) = G(A).
The next deﬁnition is a variant of Deﬁnition 3.1.31.
Deﬁnition 3.1.47.Let M be an abelian category, and letA be a graded ring.
For M,N ∈G(A, M) and i∈Z we deﬁneHomA,M(M,N )i to be the subset of
HomM(M,N )i consisting of the morphismsφ:M→N such that
φ◦fM(a) = (−1)i·k·fN(a)◦φ
for alla∈Ak. Next let
HomA,M(M,N ) :=
⨁
i∈Z
HomA,M(M,N )i.
This is a gradedK-module.
57
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁnition 3.1.48.Let M be an abelian category, and letA be a graded ring. The
category of gradedA-modules in M is the graded categoryG(A, M) whose objects
are the gradedA-modules in M, and the morphism gradedK-modules are
HomG(A,M)(M0,M 1) := HomA,M(M0,M 1)
from Deﬁnition 3.1.47. The compositions are those ofG(M).
In the special case thatA is a ring (i.e. a graded ring concentrated in degree0),
this is [76, Deﬁnition 8.5.1].
Notice that forgetting the action ofA is a faithful graded functorG(A, M)→
G(M). As in every graded category, there is the subcategory
(3.1.49) Gstr(A, M) := Str(G(A, M))⊆G(A, M)
of strict (i.e. degree0) morphisms.
Exercise 3.1.50. Show that Gstr(A, M) is an abelian category.
Remark 3.1.51. The reader may have noticed that we can talk about the graded
category G(M) for every linear categoryM, regardless if it is abelian or not. We
chose to restrict attention to the abelian case for a pedagogical reason: this will
hopefully reduce confusion between the many sorts of graded (and later DG) cate-
gories that occur in our discussion.
3.2. DGK-Modules. Recall that Conventions 1.2.4 and 3.1.2 are in force.
Deﬁnition 3.2.1.A DGK-moduleis a gradedK-moduleM =⨁
i∈ZMi, together
with aK-linear homomorphism dM : M→M of degree 1, called thediﬀerential,
satisfying dM◦dM = 0.
When there is no danger of confusion, we may writed instead of dM.
Deﬁnition 3.2.2.Let M and N be DGK-modules. A strict homomorphism of
DGK-modulesis aK-linear homomorphismφ:M→N of degree0 that commutes
with the diﬀerentials. The resulting category is denoted byDGModstrK, or by the
abbreviated notation Cstr(K).
It is easy to see thatCstr(K) is aK-linear abelian category. There is a forgetful
functor Cstr(K)→Gstr(K), (M, dM)↦→M.
Deﬁnition 3.2.3.Suppose M and N are DGK-modules.
(1) The gradedK-module structure on the tensor productM⊗N was given in
equation (3.1.3). We put on it the diﬀerential
d(m⊗n) := dM(m)⊗n + (−1)i·m⊗dN(n)
form∈Mi andn∈Nj. In this wayM⊗N becomes a DGK-module. We
sometimes write dM⊗N for this diﬀerential.
(2) The graded module HomK(M,N ) was introduced in Deﬁnition 3.1.5. We
give it this diﬀerential:
d(φ) := dN◦φ−(−1)i·φ◦dM
for φ∈HomK(M,N )i. Thus HomK(M,N ) becomes a DGK-module. We
sometimes denote this diﬀerential bydHomK(M,N).
Deﬁnition 3.2.4.Let M be a DGK-module, and leti be an integer.
(1) The module of degreei cocyclesof M is
Zi(M) := Ker
(
Mi dM
−−→Mi+1{
.
(2) The module of degreei coboundariesof M is
Bi(M) := Im
(
Mi−1 dM
−−→Mi{
.
58
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(3) The module of degreei decocyclesof M is
Yi(M) := Coker
(
Mi−1 dM
−−→Mi{
.
(4) The i-th cohomologymodule ofM is
Hi(M) := Zi(M)/ Bi(M)∼= Coker
(
Mi−1 dM
−−→Zi(M)
{
.
The deﬁnition above is standard, with the exception of item (3), which is a new
contribution (both the notationYi(M) and the name “decocycles”). The fact that
dM◦dM = 0 implies that Bi(M)⊆Zi(M)⊆Mi, so item (4) makes sense. On the
other hand, sinceYi(M) =Mi/ Bi(M), there is a canonical isomorphism
(3.2.5) Hi(M)∼= Ker
(
Yi(M)
dM
−−→Mi+1{
.
The modules deﬁned above are functorial inM; to be precise, these areK-linear
functors
(3.2.6) Zi, Bi, Yi, Hi : Cstr(K)→M(K).
We can rephrase Deﬁnition 3.2.2 using the notion of cocycles: for DGK-modules
M and N there is equality
(3.2.7) HomCstr(K)(M,N ) = Z0(
HomK(M,N )
{
of submodules ofHomK(M,N ).
