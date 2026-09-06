---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-089-151-categories-of-algebraically-graded-modules
section_title: "Categories of Algebraically Graded Modules"
section_number: 15.1
pages: 323-331
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
mutative base ring. An algebraically gradedK-module is aK-module M with a
direct sum decompositionM =⨁
i∈ZMi intoK-submodules. The submodule Mi
is called the homogeneous component ofM of algebraic degreei. If m∈Mi is a
nonzero element, then we writedeg(m) =i.
In Subsection 3.1 we discussedcohomologically graded rings and modules. There
are three features that distinguish between cohomologically gradedK-modules and
algebraically gradedK-modules. The ﬁrst distinguishing feature is the use of upper
vs. lower indices. The second is that in an algebraically graded module there is
never a diﬀerential involved; i.e. it is not the underlying graded module of a DG
module. The third and most important change is insigns of permutations, and
thus incommutativity. In the cohomologically graded setting the Koszul sign rule
dictates that for gradedK-modules M and N, the braiding isomorphismbrM,N :
M⊗N→N⊗M, where⊗:=⊗K, isbrM,N (m⊗n) = (−1)i·j·n⊗mforhomogeneous
elements m∈Mi and n∈Nj. But in the algebraically graded setting there are
no signs: brM,N (m⊗n) := n⊗m for m∈Mi and n∈Nj. This is reﬂected in
Deﬁnition 15.1.13 below.
Let M = ⨁
i∈Z Mi be an algebraically gradedK-module. A nonzero element
m∈M can be expressed uniquely as a sum
(15.1.1) m =m1 +···+mr,
such that r ≥1; each mi is a nonzero homogeneous element; and deg(mi) <
deg(mi+1). This is called the homogeneous component decompositionof m. Of
course m is homogeneous if and only ifr = 1.
Suppose M and N are algebraically gradedK-modules. A K-linear homomor-
phism φ: M →N is said to be of algebraic degreei if φ(Mj) ⊆Nj+i for all
j∈Z. The K-module of allK-linear homomorphisms of degreei is denoted by
HomK(M,N )i. Taking the direct sum we get an algebraically gradedK-module
(15.1.2) HomK(M,N ) :=
⨁
i∈Z
HomK(M,N )i.
Deﬁnition 15.1.3.Let M and N be algebraically gradedK-modules. A strict
homomorphism of algebraically gradedK-modules φ: M →N is K-linear homo-
morphism of algebraic degree0.
ThismaterialwillbepublishedbyCambridgeUniversityPressas Derived CategoriesbyAmnon
Yekutieli. This prepublication version is free to view and download for personal use only. Not for
redistribution, resale or use in derivative works.c© Amnon Yekutieli, 2019.
323
Derived Categories | Amnon Yekutieli | 14 Apr 2019
The category of algebraically gradedK-modules is the categoryM(K, gr), whose
objects are the algebraically gradedK-modules, and whose morphisms are the strict
homomorphisms.
Thus
HomM(K,gr)(M,N ) = HomK(M,N )0.
It is easy to see that M(K, gr) is a K-linear abelian category. The kernels and
cokernels are degreewise.
Suppose M,N ∈M(K, gr). Their tensor product is also algebraically graded:
(M⊗N)i =
⨁
j∈Z
(Mj⊗Ni−j)
and
M⊗N =
⨁
i∈Z
(M⊗N)i.
Deﬁnition 15.1.4.An algebraically graded centralK-ring is a centralK-ring A,
equipped with a direct sum decompositionA =⨁
i∈ZAi intoK-submodules, such
that 1A∈A0, andAi·Aj⊆Ai+j for alli,j.
A homomorphism of algebraically graded centralK-rings f :A→B is aK-ring
homomorphism such thatf(Ai)⊆Bi for alli.
The algebraically graded centralK-rings form a category, that we denote by
Rnggr/cK.
The base ringK is an algebraically graded ring, concentrated in degree0. It is
the initial object of the categoryRnggr/cK.
In the traditional ring theory literature (e.g. [106], [130], [8], [10], [161] and [182])
the algebraically graded centralK-rings were called “associative unital gradedK-
algebras”.
Example 15.1.5. Let M be an algebraically gradedK-module. Then EndK(M)
:= HomK(M,M )is an algebraically graded centralK-ring. The grading is according
to (15.1.2), and multiplication is composition.
Deﬁnition 15.1.6.Let A be an algebraically graded centralK-ring.
(1) An algebraically graded leftA-module is a leftA-module M, equipped with
a direct sum decompositionM =⨁
i∈Z Mi intoK-submodules, such that
Ai·Mj⊆Mi+j for alli,j.
(2) Suppose M and N are algebraically graded left A-modules. A K-linear
homomorphism φ: M →N of degree i is said to be a homomorphism
of algebraically gradedA-modules if φ(a·m) = a·φ(m) for all a∈A and
m∈M.
(3) The K-module of all A-linear homomorphisms of degreei is denoted by
HomA(M,N )i. Taking the direct sum we get an algebraically gradedK-
module
HomA(M,N ) :=
⨁
i∈Z
HomA(M,N )i.
Note that there is an inclusionHomA(M,N )⊆HomK(M,N ) in M(K, gr).
Deﬁnition 15.1.7.Let A be an algebraically graded centralK-ring.
(1) Suppose M and N are algebraically graded leftA-modules. The elements
of HomA(M,N )0 are called strict homomorphisms of algebraically graded
A-modules.
(2) The category of algebraically graded leftA-modules, with strict homomor-
phisms, is denoted byM(A, gr).
324
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Thus
(15.1.8) HomM(A,gr)(M,N ) = HomA(M,N )0.
Clearly, to put an algebraically graded left A-module structure on an alge-
braically graded K-module M is the same as to give a homomorphism A →
EndK(M) in Rnggr/cK.
Algebraically graded rightA-modules, and algebraically gradedA-B-bimodules,
are deﬁned similarly to Deﬁnition 15.1.6. There are no signs anywhere. All homo-
morphisms areK-linear, and all bimodules are central overK.
Deﬁnition 15.1.9.Let A be an algebraically graded ring. Given an algebraically
gradedA-moduleM and an integeri, thei-th degree twist ofM is the algebraically
gradedA-module M(i) whose degreej homogeneous component isM(i)j :=Mi+j.
The action ofA is not changed.
The degree twist is an automorphism of the abelian categoryM(A, gr). And
HomM(A,gr)(M,N (i)) = HomA(M,N )i.
There is a similar twisting for graded right modules and for graded bimodules.
There is a functorUngr : Rnggr/cK→Rng/cK that forgets the grading. For a
ﬁxed ringA∈Rnggr/cK there is a forgetful functor
(15.1.10) Ungr : M(A, gr)→M(Ungr(A)).
This is an exact faithfulK-linear functor.
Remark 15.1.11.The functorUngrin (15.1.10) is usually not full, for two reasons.
First, there could be nonzero homomorphisms of nonzero degree, so that
HomM(A,gr)(M,N ) = HomA(M,N )0⫋ HomA(M,N ).
Second, it is easy ﬁnd an example where
Ungr
(
HomA(M,N )
{
⫋ HomUngr(A)
(
Ungr(M), Ungr(N)
{
.
Just takeM :=⨁
i∈Z A(i) and N :=A. Then
Ungr
(
HomA(M,N )
{∼=
⨁
i∈Z
Ungr(A)
and
HomUngr(A)
(
Ungr(M), Ungr(N)
{∼=

i∈Z
Ungr(A)
in M(K).
Remark 15.1.12.Homomorphisms between algebraically graded modules and co-
homologically graded modules are distinct, not only in the position of the degree
indices. Compare Deﬁnition 15.1.6(2) to Deﬁnition 3.1.31. This distinction is due
to the Koszul sign rule, that is present only in the cohomologically graded setting.
Deﬁnition 15.1.13.Let A and B be algebraically graded centralK-rings.
(1) The opposite ring of A is the centralK-ring Aop, that is the same alge-
braically gradedK-module asA, with an isomorphismop := id :A
≃
− →Aop
in M(K, gr). The multiplication·op of Aop is
op(a1)·op op(a2) := op(a2·a1).
(2) The ring A is called a commutative graded ringif a2·a1 = a1·a2 for all
a1,a 2∈A.
(3) The tensor productA⊗B is made into an algebraically graded ring with
multiplication
(a1⊗b1)·(a2⊗b2) := (a1·a2)⊗(b1⊗b2).
325
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(4) The enveloping ring ofA is the algebraically graded ringAen :=A⊗Aop.
In terms of opposite rings, an algebraically graded ringA is commutative if and
only ifA =Aop. The category of algebraically graded rightA-modules is identiﬁed
with M(Aop, gr); and the category ofK-central algebraically gradedA-B-bimodules
is identiﬁed withM(A⊗Bop, gr).
There are graded ring homomorphismsA→A⊗B←B, and corresponding
restriction functors
(15.1.14) M(A, gr)
RestA
←−−−−M(A⊗B, gr)
RestB
−−−−→M(B, gr).
We shall usually omit any explicit reference to these restriction functors.
Given M∈M(A, gr) and N∈M(B, gr), the tensor productM⊗N belongs to
M(A⊗B, gr).
SupposeM∈M(Aop, gr) andN∈M(A, gr). Their tensor product overA is also
algebraically graded:
(15.1.15) M⊗AN =
⨁
i∈Z
(M⊗AN)i∈M(K, gr),
where (M⊗AN)i is the image of(M⊗N)i under the canonical surjectionM⊗N↠
M⊗AN in M(K, gr). See Lemma 3.1.30 for the corresponding statement in the
cohomologically graded setting.
There is an isomorphism of algebraically gradedK-rings
(15.1.16) (Aen)op ≃
− →Aen, a 1⊗a2↦→a2⊗a1.
From here on in this section, and in Sections 16 and 17, we assume the following
convention.
Convention 15.1.17.We ﬁx a nonzero commutative base ringK. The symbol⊗
means⊗K. All graded rings are assumed to be algebraically graded centralK-rings,
and all graded ring homomorphisms are overK. I.e. we work inside the category
Rnggr/cK.
LetA be a graded ring. Its enveloping ring is the graded ringAen :=A⊗Aop. All
gradedA-modulesareassumedbydefaulttobealgebraicallygradedleft A-modules.
ForM,N ∈M(A, gr) the expression HomA(M,N ) refers to the gradedK-module
in Deﬁnition 15.1.6(3). All graded bimodules are assumed to beK-central; i.e. a
graded A-B-bimodule is an object ofM(A⊗Bop, gr).
Proposition 15.1.18. LetA be a graded ring.
(1) The category M(A, gr) is abelian.
(2) The category M(A, gr) has inverse limits.
(3) The categoryM(A, gr) has direct limits. Moreover, direct limits inM(A, gr)
commute with the ungrading functor(15.1.10).
Proof. (1) The kernels and cokernels in M(A, gr) are degreewise, so the abelian
property of M(A, gr) is inherited from the abelian property ofM(K).
(2) Inverse limits inM(A, gr) are taken degreewise. Namely, given an inverse sys-
tem{Mx}x∈Xop of objects of M(A, gr), indexed by a directed setX, let Mi :=
lim←x(Mx)i ∈M(K). Then M := ⨁
i∈ZMi ∈M(A, gr) is the inverse limit of
{Mx}x∈Xop.
(3) Direct limits in M(A, gr) are taken degreewise. Namely, given a direct sys-
tem {Ny}y∈Y of objects of M(A, gr), indexed by a directed set Y, let Ni :=
limy→(Ny)i ∈M(K). Then N := ⨁
i∈ZNi ∈M(A, gr) is the direct limit of
{Ny}y∈Y.
Because direct sums and direct limits commute with each other, it follows that
limy→commutes with Ungr. □
326
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁnition 15.1.19.A graded ringA is callednonnegative if Ai = 0 for alli< 0;
i.e. ifA =⨁
i≥0Ai.
If A is a nonnegative graded ring A, then the two-sided graded ideal m :=⨁
i≥1Ai is called theaugmentation ideal. It is the kernel of the surjective graded
ring homomorphismA→A0, that we call theaugmentation homomorphism.
The augmentation ideal of the graded ringAop is denoted bymop.
Deﬁnition 15.1.20.LetA be a graded ringA and letM =⨁
i∈ZMi be a graded
A-module.
(1) We callM a bounded abovegraded module ifMi = 0 for i≫0.
(2) We callM a bounded belowgraded module ifMi = 0 for i≪0.
(3) We call M a bounded graded module if it is both bounded above and
bounded below.
Example 15.1.21. If A is a nonnegative graded ring, then as a graded module
A is bounded below. For suchA, the bounded below graded modules behave like
ﬁnitely generated modules over a noetherian local commutative ring – see Proposi-
tion 15.1.22 below.
The next proposition is the ﬁrst version of the graded Nakayama Lemma that
we present; the second is Proposition 15.2.30.
Proposition 15.1.22. Let A be a nonnegative graded ring, with augmentation
ideal m. LetM be a bounded below gradedA-module, and letM′⊆M be a graded
A-submodule. IfM′+ m·M =M then M′=M.
Proof. Say M =⨁
i≥i0
Mi for an integeri0. We will prove thatM′
i = Mi as A0-
modules for alli, by induction oni≥i0−1. For i = i0−1 this is clear because
both theseA0-modules are zero.
Now takei≥i0, and assume thatM′
j = Mj for all j < i. Suppose m∈Mi
is a nonzero element. Because M = M′+ m·M, we can express m as follows:
m =m′+∑r
k=1ak·mk, wherem′∈M′
i; r≥0; ak∈m and mk∈M are nonzero
homogeneous elements; anddeg(ak) + deg(mk) = i. But then deg(mk)< i, so by
the induction hypothesis we havemk∈M′. We conclude thatm∈M′
i. □
Deﬁnition 15.1.23.Let A be a graded ring.
(1) A gradedA-module M is called agraded-ﬁniteA-module if M can be gen-
erated by ﬁnitely many homogeneous elements.
(2) The full subcategory ofM(A, gr) on the graded-ﬁniteA-modules is denoted
by Mf(A, gr).
(3) A is called aleft graded-noetherian ringif every graded left ideala⊆A is
a graded-ﬁniteA-module, in the sense of item (1) above.
(4) A is called a graded-noetherian ring if both A and Aop are left graded-
noetherian rings.
An obvious modiﬁcation of item (1) above gives the deﬁnition of a graded-ﬁnite
rightA-module. Of course the ringA is called a right graded-noetherian ring ifAop
is a left graded-noetherian ring.
Proposition 15.1.24.IfA is left graded-noetherian ring, thenMf(A, gr) is a thick
abelian subcategory ofM(A, gr).
Exercise 15.1.25. Prove this proposition.
Proposition 15.1.26. Let A be a graded ring andM a gradedA-module. The
following two conditions are equivalent.
(i) M is a graded-ﬁniteA-module, in the sense of Deﬁnition15.1.23(1).
(ii) Ungr(M) is a ﬁnitely generatedUngr(A)-module.
327
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Exercise 15.1.27. Prove this proposition.
Theorem 15.1.28. Let A be a graded ring. The following two conditions are
equivalent.
(i) The graded ring A is left graded-noetherian, in the sense of Deﬁnition
15.1.23(3).
(ii) The ring Ungr(A) is left noetherian.
Proof. The case whenA is nonnegative is proved in many textbooks, and it is a
nice exercise for the reader.
The general case is much harder, and the few proofs in the literature are quite
complicated. Here is a short proof, that is due to S. Snigerov.
The implication (ii)⇒(i) is trivial. So let us assume that A is left graded-
noetherian, and we shall prove thatUngr(A) is left noetherian. The proof proceeds
in a few steps.
Step 1. Consider an A0-submodule V ⊆Aj for somej, and let b := A·V ⊆A,
which is a graded left ideal ofA. By assumption, b is generated by ﬁnitely many
homogeneous elements. An easy calculation shows thatV = b∩Aj, and thatV
is ﬁnitely generated as anA0-module. The consequence is that the ringA0 is left
noetherian, and that everyAj is a ﬁnitely generatedA0-module.
Step 2. Now we ﬁx a nonzero left idealL⊆A. We are going to ﬁnd a ﬁnite number
of generators forL as anA-module.
For a nonzero elementa∈L we consider its homogeneous component decompo-
sition (15.1.1), and we deﬁne its bottom degree componentbot(a) := a1, and its
top degree componenttop(a) :=ar. Let atop be the left ideal inA generated by the
elements top(a), wherea runs over all the nonzero elements ofL. By assumption
the graded idealatop is graded-ﬁnite; so we can choose a ﬁnite collection{ax}x∈Xtop
of nonzero elements ofL, such that their top degree componentstop(ax) generate
the left idealatop. Now let
d1 := max
{
deg(top(ax))|x∈Xtop
}
∈Z.
Step 3. Deﬁne abot to be the left ideal inA generated by the elements bot(a),
where a runs over all the nonzero elements ofL∩A≤d1. (It is possible that there
are no such elements.) By assumption the graded left idealabot is graded-ﬁnite; so
we can choose a ﬁnite collection{ax}x∈Xbot of nonzero elements ofL∩A≤d1, such
that their bottom degree componentsbot(ax) generate the left idealabot. Now we
let
d0 := min
({
deg(bot(ax))|x∈Xbot
}
∪{0}
{
∈Z.
Step 4. By step 1 theA0-module V := L∩
(⨁d1
i=d0
Ai
{
is ﬁnitely generated. We
choose a ﬁnite collection{ax}x∈Xmid that generatesV as anA0-module.
Step 5. Deﬁne the ﬁnite indexing setX := Xtop⊔Xbot⊔Xmid. We claim that
the collection{ax}x∈X generates the left idealL. Take any elementa∈L. By
subtracting froma a ﬁnite linear combination of elements from{ax}x∈Xtop, with
coeﬃcients taken fromA≥1, we can assume thata∈L∩A≤d1. Next, by subtracting
from a a ﬁnite linear combination of elements from{ax}x∈Xbot, with coeﬃcients
taken fromA≤−1, we can assume thata∈V, theA0-submodule from step 4. So
a is ﬁnite linear combination of elements from{ax}x∈Xmid, with coeﬃcients taken
from A0. □
In view of Proposition 15.1.26 and Theorem 15.1.28, we can use this more relaxed
terminology without danger of ambiguity:
Deﬁnition 15.1.29.Let A be a graded ring.
328
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(1) We call A a left noetherian graded ring if it is left graded-noetherian.
Likewise for the attributes “right noetherian graded ring” and “noether-
ian graded ring”.
(2) Let M be a gradedA-module. We callM a ﬁnite gradedA-module if it is
graded-ﬁnite. Likewise for right modules.
We do not assume the rings here are noetherian. Partly this is because of the
factsin theremark below. Instead weresort toderived graded-pseudo-ﬁnitemodules
and complexes, see Deﬁnition 15.3.22.
Remark 15.1.30. Unlike the commutative theory, the Hilbert Basis Theorem
does not hold in the noncommutative setting. Thus, a ﬁnitely generatedK-ring A
need not be noetherian; see Example 15.2.19. Likewise, ifA and B are noetherian
ﬁnitely generatedK-rings, the tensor productA⊗B need not be noetherian; there
is a counterexample in [128]. See [7] for a deep discussion of permanence properties
of NC noetherian rings.
We now pass to complexes of algebraically graded modules, retaining Convention
15.1.17. In Subsection 3.6 we introduced the category C(M) of complexes with
entries in an abelian category M. This is a DG category. Its strict subcategory
Cstr(M) is abelian. Here we take the abelian categoryM := M(A, gr) for a graded
ring A.
Deﬁnition 15.1.31.Let A be a graded ring.
(1) The category of complexes with entries in the abelian categoryM(A, gr) is
the DG categoryC(A, gr) := C(M(A, gr)).
(2) The strict subcategory of C(A, gr) is the abelian category Cstr(A, gr) :=
Cstr(M(A, gr)).
(3) Given a boundedness indicator⋆, we denote byC⋆(A, gr) the full subcate-
gory of C(A, gr) on the complexesM having boundedness condition⋆.
We now try to make Deﬁnition 15.1.31 more explicit. An objectM∈C(A, gr)
has these direct sum decompositions:
(15.1.32) M =
⨁
i∈Z
Mi =
⨁
i,j∈Z
Mi
j.
Here eachMi∈M(A, gr), and eachMi
j ∈M(K). We call Mi
j the homogeneous
component of M of bidegree
i
j

∈
Z
Z

= Z2. The upper index i is called the
cohomological degree, and the lower index j is called the algebraic degree. The
diﬀerentialdM of the complexM is anA-linear homomorphism dM : M→M of
bidegree
1
0

that satisﬁesdM◦dM = 0.
A morphismφ:M→N in the strict categoryCstr(A, gr) has bidegree
0
0

and
satisﬁesφ◦dM = dN◦φ.
Lastly, to clarify item (3) in the deﬁnition, a complexM belongs to C+(A, gr) if
Mi = 0 fori≪0, etc. Indicators can be combined, soC⋆
str(A, gr) is a thick abelian
subcategory of Cstr(A, gr).
Like for any abelian category, we have a homotopy category and a derived cate-
gory. Here is the speciﬁc notation:
Deﬁnition 15.1.33.Let A be a graded ring.
(1) The homotopy category of complexes with entries in the abelian category
M(A, gr) is the triangulated categoryK(A, gr) := K(M(A, gr)).
(2) The derived category of the abelian categoryM(A, gr) is the triangulated
category D(A, gr) := D(M(A, gr)).
329
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(3) Given a boundedness indicator⋆, we denote by D⋆(A, gr) the full trian-
gulated subcategory of D(A, gr) on the complexesM whose cohomology
H(M) has boundedness condition⋆.
As always for derived categories, there are functors
(15.1.34) Cstr(A, gr) P //
˜Q
’’
K(A, gr)
Q // D(A, gr).
By abuse of notation we sometimes writeQ rather than ˜Q; or, when there is no
danger of confusion, we suppress the categorical localization functors Q and ˜Q
altogether.
There is yet another category associated toA : it is the category G(A, gr) :=
G(M(A, gr)) of cohomologically graded objects inM(A, gr). It has its strict sub-
category Gstr(A, gr). This is the target of the cohomology functor
H : Cstr(A, gr)→Gstr(A, gr).
If A→B is a graded ring homomorphism that makesB into a ﬁnite leftA-
module, and ifA is left noetherian, then of courseB is also left noetherian. Here
is a partial converse:
Theorem 15.1.35.LetA be a nonnegative graded ring, and leta∈A be a nonzero
homogeneous central element of positive degree. Deﬁne the nonnegative graded ring
B :=A/(a). IfB is left noetherian, thenA is also left noetherian.
This result is very similar to [8, Lemma 8.2]. There are three changes: we do not
assume that the elementa is regular (i.e. not a zero-divisor), and we do not assume
that A is connected graded (only nonnegative). On the other hand, in [8] the
element a is only required to be normalizing, not central. Our proof is essentially
copied from [8].
Proof. Assume, for the sake of contradiction, that the graded ringA is not left
noetherian. Then (taking Theorem 15.1.28 into account) there is a graded left ideal
L⊆A that is not ﬁnitely generated. By Zorn’s Lemma we can assume thatL is
maximal with this property. Thus every graded left idealL†such thatL⊊L†⊆A
must be ﬁnitely generated.
Consider the gradedA-module M := A/L. Every graded A-module M†⊆M
is of the formM†=L†/L, and thereforeM†is a ﬁnitely generatedA-module. In
other words,M is a noetherian object ofM(A, gr).
Let i := deg(a). We examine the commutative diagram (15.1.36) inM(A, gr).
Viewing the columns of this diagram as complexes, whose nonzero terms are in
cohomological degrees0 and 1, this is a short exact sequence in the abelian category
Cstr(A, gr).
(15.1.36) 0 //L //A //M // 0
0 //L(−i)
a·(−)
OO
//A(−i)
a·(−)
OO
//M(−i)
a·(−)
OO
// 0
Deﬁne the gradedA-modules ¯M and ¯L by these exact sequences:
0→¯M→M(−i)
a·(−)
− −−− →M
and
(15.1.37) L(−i)
a·(−)
− −−− →L→¯L→0.
330
Derived Categories | Amnon Yekutieli | 14 Apr 2019
The long exact cohomology sequence of (15.1.36) gives rise to this exact sequence
in M(A, gr) :
(15.1.38) ¯M
φ
− →¯L
ψ
− →B.
Because M is a noetherian object ofM(A, gr), so is its degree twistM(−i), and
also the subobject ¯M⊆M(−i). On the other hand, we are given that the ringB is
noetherian; so it is a noetherian object ofM(A, gr). The exact sequence (15.1.38)
shows that ¯L is also a noetherian object ofM(A, gr). We see that ¯L is a ﬁnitely
generated A-module.
Finally, let us choose ﬁnitely many homogeneous generators of the gradedA-
module ¯L, and then lift them to homogeneous elements ofL. Let L′⊆L be the
A-submodule generated by this ﬁnite collection of elements. The exact sequence
(15.1.37) shows thatL = (a·L) +L′. The gradedA-module L is bounded below,
because L⊆A and A is nonnegative. The elementa belongs to the augmentation
ideal m ofA. Therefore, by Proposition 15.1.22 (the graded Nakayama Lemma), we
haveL′=L. This contradicts the assumption thatL is not ﬁnitely generated.□
