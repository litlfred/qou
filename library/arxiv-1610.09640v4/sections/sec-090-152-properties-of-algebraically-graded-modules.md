---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-090-152-properties-of-algebraically-graded-modules
section_title: "Properties of Algebraically Graded Modules"
section_number: 15.2
pages: 331-338
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
continue with Convention 15.1.17, to which we add:
Convention 15.2.1.The base ringK is a ﬁeld.
See Remark 15.3.35 regarding the requirement thatK be a ﬁeld. In a sense the
category M(K, gr) is boring under Convention 15.2.1 :
Proposition 15.2.2. For an objectM∈M(K, gr) there is an isomorphismM∼=⨁
x∈XK(−ix), whereX is an indexing set and{ix}x∈X is a collection of integers.
Proof. This is a variation on the usual proof forK-modules: by Zorn’s Lemma there
is a maximal linearly independent collection{mx}x∈X of homogeneous elements of
M. This is a basis ofM. The numberix is the degree ofmx. □
Deﬁnition 15.2.3.Let A be a graded ring. We deﬁne the graded bimodule
A∗:= HomK(A,K)∈M(Aen, gr),
see formula (15.1.2).
Deﬁnition 15.2.4.Let A be a graded ring.
(1) A graded A-module P is called a graded-free A-module if P ∼=⨁
x∈XA(−ix) in M(A, gr) for some collection{ix}x∈X of integers.
(2) A gradedA-module P is called agraded-projectiveA-module if it is a pro-
jective object in the abelian categoryM(A, gr).
(3) A graded A-module I is called a graded-cofree A-module if I ∼=∏
x∈XA∗(−px) in M(A, gr) for some collection{px}x∈X of integers.
(4) A gradedA-module I is called agraded-injectiveA-module if it is an injec-
tive object in the abelian categoryM(A, gr).
(5) A gradedA-module P is called agraded-ﬂatA-module if the functor
(−)⊗AP : M(Aop, gr)→M(K, gr)
is exact.
Note that a graded-freeA-module P is of the formP ∼= A⊗V for someV ∈
M(K, gr); and a graded-cofreeA-module I is of the formI∼= HomK(A⊗W,K) for
some W∈M(K, gr).
Proposition 15.2.5. LetA and B be graded rings.
331
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(1) There is an isomorphism
HomA(−,A∗)∼= HomK(−,K)
of functors
M(A⊗Bop, gr)op→M(B⊗Aop, gr).
(2) The graded bimoduleA∗is graded-injective overA, namely it is an injective
object in the categoryM(A, gr).
Proof. This is by the adjunction isomorphism
HomA
(
M, HomK(A,K)
{∼= HomK(M,K)
in M(K, gr). □
The ungrading functor (15.1.10) preserves ﬁniteness (i.e. being a ﬁnitely gener-
ated module). It also preserves freeness and projectivity, as the next proposition
shows.
Proposition 15.2.6. LetA be a graded ring, and letP∈M(A, gr).
(1) If P is a graded-freeA-module, then Ungr(P ) is a freeUngr(A)-module.
(2) P is a graded-projectiveA-module if and only if it is a direct summand, in
M(A, gr), of a graded-freeA-module.
(3) IfP is a graded-projectiveA-module, thenUngr(P ) is a projectiveUngr(A)-
module.
Exercise 15.2.7. Prove Proposition 15.2.6.
Remark 15.2.8. In the situation of Proposition 15.2.6, one can show thatP is a
graded-ﬂatA-module if and only ifUngr(P ) is a ﬂatUngr(A)-module. The proof
is not easy. See [111, Proposition 3.4.5].
For injectives things are much more complicated, as the next theorem and ex-
ample show.
Theorem 15.2.9(Van den Bergh). LetA be a left noetherian nonnegative graded
ring, and letI be graded-injectiveA-module. Then Ungr(I) has injective dimension
at most 1 as an Ungr(A)-module.
Proof. See [181]. A more general statement can be found in [142]. □
Example 15.2.10. Consider the graded ringA :=K[t], the ring of polynomials
in a variablet of degree 1. The gradedA-module I :=K[t,t−1] is graded-injective,
but Ungr(I) has injective dimension1 over Ungr(A).
Proposition 15.2.11.
(1) A graded-freeA-moduleP is graded-projective.
(2) A graded-projectiveA-moduleP is graded-ﬂat.
(3) A graded-cofreeA-moduleI is graded-injective.
Exercise 15.2.12. Prove this proposition.
Proposition 15.2.13. LetA and B be graded rings.
(1) If P∈M(A⊗B, gr) is projective, then it is projective inM(A, gr).
(2) If P∈M(A⊗B, gr) is ﬂat, then it is ﬂat inM(A, gr).
(3) If I∈M(A⊗B, gr) is injective, then it is injective inM(A, gr).
Proof. (1) TakeN∈C(A, gr). We have isomorphisms
HomA(P,N )∼= HomA⊗B(P, HomA(A⊗B,N ))
∼= HomA⊗B(P, HomK(B,N ))
332
Derived Categories | Amnon Yekutieli | 14 Apr 2019
in Cstr(K, gr). As an object ofM(K, gr), B is projective. Hence, ifN is an acyclic
complex, then so isHomA(P,N ).
(2, 3) Like item (1), but using the fact thatB is graded-ﬂat overK, and using
suitable adjunction isomorphisms. □
Deﬁnition 15.2.14.Let A be a graded ring.
(1) LetM be a gradedA-module, and letN⊆M be a graded submodule. We
say thatN is agraded-essential submoduleofM if for every nonzero graded
submodule M′⊆M the intersectionN∩M′is nonzero.
(2) A homomorphism φ: N →M in M(A, gr) is called a graded-essential
monomorphism if φis an injective homomorphism, andφ(N) is a graded-
essential submodule ofM.
Item (2) of the deﬁnition is a special case of the usual deﬁnition of an essential
monomorphism in an abelian category.
Exercise 15.2.15. Let N⊆M be gradedA-modules. Show thatN is a graded-
essential submodule ofM if and only ifUngr(N) is an essentialUngr(A)-submodule
of Ungr(M). (Hint: prove that for every nonzero element m ∈M there is a
homogeneous elementa∈A such thata·m∈N anda·m⁄= 0. Do this by induction
on the numberr appearing in the decomposition (15.1.1). See the proof of [111,
Lemma 3.3.13], which is not totally correct, but can be ﬁxed using our hint.)
Proposition 15.2.16. LetA be a graded ring.
(1) The category M(A, gr) has enough projectives.
(2) The category M(A, gr) has enough injectives. Moreover, every M ∈
M(A, gr) has an injective hull, namely there is a graded-essential mono-
morphism M↣I to a graded-injective moduleI.
Proof. (1) Given a moduleM ∈M(A, gr) and a homogeneous elementm∈Mi,
there is a homomorphismA(−i)→M that sends 1A↦→m. Therefore, by taking
a suﬃciently large direct sum of degree twists ofA, there is a surjectionP↠ M
from a graded-free moduleP. And graded-free modules are graded-projective, by
Proposition 15.2.11.
(2) For every nonzero homogeneous elementm∈Mq there is a homomorphism
M →K(−q) in M(K, gr) that is nonzero on m. By Proposition 15.2.5(1) we
get a homomorphismM→A∗(−q) in M(A, gr) that is nonzero onm. Thus, by
taking a suﬃciently large productI := ∏
x∈XA∗(−qx) in M(A, gr) we obtain a
monomorphism M ↣ I. And according Proposition 15.2.11, the graded-cofree
object I is injective inM(A, gr).
As for injective hulls: this is the same as in the ungraded case; see [129, Theorem
3.30] or [93, Section 3.D]. □
Now a structural result on injective objects inM(A, gr).
Theorem 15.2.17. LetA be a left noetherian graded ring.
(1) If{Ix}x∈X is a collection of graded-injectiveA-modules, thenI :=⨁
x∈XIx
is a graded-injectiveA-module.
(2) Every graded-injectiveA-moduleI is a direct sum of indecomposable graded-
injectiveA-modules.
Proof. This is because M(A, gr) is a locally noetherian Grothendieck abelian cat-
egory. See [148, Section V.4]. Item (1) can be proved directly using the graded
version of the Baer criterion (Theorem 2.7.10). □
333
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁnition 15.2.18.A connected gradedK-ring is a nonnegative gradedK-ring
A (see Conventions 15.1.17 and 15.2.1, and Deﬁnition 15.1.19), such that the ring
homomorphism K→A0 is bijective, andAi is a ﬁnitely generatedK-module for
all i≥0.
Here are a few examples of connected graded rings.
Example 15.2.19. Consider the noncommutative polynomial ring A :=
K⟨x1,...,xn⟩in n≥1 variables, all of algebraic degree 1. This is a connected
gradedK-ring. If n≥2 then A is not commutative and not noetherian (on either
side). Ifn = 1 thenK⟨x1⟩=K[x1], see next example.
Example 15.2.20. Let A :=K[x1,...,xn], the commutative polynomial ring in
n ≥1 variables, all of algebraic degree 1. This is a connected graded K-ring,
commutative and noetherian.
Example 15.2.21.LetK[t] be the commutative polynomial ring in a variablet of
algebraic degree 1. Next let
A :=K[t]⟨x,y⟩/(y·x−x·y−t2),
where x and y are noncommuting variables of algebraic degree1 (that commute
with t). This is the homogeneous ﬁrst Weyl algebra. It is a connected gradedK-
ring, noetherian, but not commutative. Indeed, ifchar(K) = 0, then the center of
A isK[t].
Example 15.2.22. Let g be a ﬁnite Lie algebra overK. Choose a basisv1,...,vn
for g as aK-module, and letγi,j,k∈K be the constants describing the Lie bracket,
i.e.
[vi,vj] =

k
γi,j,k·vk∈g.
LetK[t] be the commutative polynomial ring in a variablet of algebraic degree1.
Let x1,...,xn be variables of algebraic degree1, and deﬁne the graded ring
A :=K[t]⟨x1,...,xn⟩/ (I),
where I is the two-sided ideal generated by the quadratic elements
xi·xj−xj·xi−
n
k=1
γi,j,k·xk·t.
This is thehomogeneous universal enveloping ringof g. The quotientA/(t−1) is
the universal enveloping ringU(g). The ring A is connected graded, noetherian,
but often noncommutative (since the Lie algebrag embeds into the quotient ring
U(g) with its commutator Lie bracket).
Example 15.2.23. Suppose A and B are both connected gradedK-rings. Then
A⊗B is a connected gradedK-ring.
Deﬁnition 15.2.24.A gradedK-moduleM =⨁
i∈Z Mi is calleddegreewise ﬁnite
if theK-module Mi is ﬁnitely generated for everyi∈Z.
The full subcategory ofM(K, gr) on the degreewise ﬁnite modules is denoted by
Mdwf(K, gr).
It is obvious that the category Mdwf(K, gr) is a thick abelian subcategory of
M(K, gr), closed under subobjects and quotient objects.
Deﬁnition 15.2.25.ForM∈M(K, gr) we let
M∗:= HomK(M,K)∈M(K, gr).
This is thegradedK-linear dual ofM.
334
Derived Categories | Amnon Yekutieli | 14 Apr 2019
According to formula (15.1.2) we haveM∗=⨁
i∈Z(M∗)i, where
(M∗)i = HomK(M,K)i = HomK(M−i,K) = (M−i)∗.
Lemma 15.2.26. If M ∈Mdwf(K, gr) then M∗∈Mdwf(K, gr), and the Hom-
evaluation homomorphism evM : M→M∗∗= (M∗)∗in Mdwf(K, gr) is bijective.
Thus (−)∗is a duality of the categoryMdwf(K, gr).
The easy proof is omitted.
Deﬁnition 15.2.27.Let A be a graded ring. A moduleM∈M(A, gr) is called
degreewiseK-ﬁniteif it is degreewise ﬁnite as a gradedK-module.
The full subcategory ofM(A, gr) on the degreewiseK-ﬁnite modules is denoted
by Mdwf(A, gr).
Of course Mdwf(A, gr) is a thick abelian subcategory ofM(A, gr), closed under
subobjects and quotients.
Proposition 15.2.28. Let A be a graded ring. IfM ∈Mdwf(A, gr) then M∗∈
Mdwf(Aop, gr), and the Hom-evaluation homomorphism evM : M →M∗∗in
M(A, gr) is bijective. Thus
(−)∗: Mdwf(A, gr)op→Mdwf(Aop, gr)
is an equivalence of categories.
Exercise 15.2.29. Prove this proposition. (Hint: use Lemma 15.2.26.)
Noncommutative connected graded rings are very similar to complete commu-
tative local rings. Here is the second variant of the graded Nakayama Lemma (the
ﬁrst was Proposition 15.1.22).
Proposition 15.2.30. LetA be a connected graded ring, and letM∈M(A, gr) be
a bounded below graded module. DeﬁneV :=K⊗AM∈M(K, gr).
(1) There is a surjectionπ:A⊗V ↠M in M(A, gr), such that the diagram
A⊗V π //
β

M
α

V id //V
in which the morphismsαand βare the canonical projections, is commu-
tative.
(2) If V = 0 then M = 0.
(3) If M is a graded-projectiveA-module, then the surjectionπabove is bijec-
tive. HenceM is a graded-freeA-module.
Note that the projectionβis induced by the augmentation homomorphismA→
K, so Ker(β) = m⊗V. Likewise, Ker(α) = m·M⊆M.
Proof.
(1) SayM =⨁
i≥i0 Mi. Choose a sectionπ0 :V ↣M in M(K, gr) of the canonical
projection α: M↠ V. Since A⊗V is a graded-freeA-module, π0 extends to a
homomorphismπ:A⊗V →M in M(A, gr). See the commutative diagram below,
in whichγ(v) := 1A⊗v.
V
π0
%%
γ

A⊗V π //M
By Proposition 15.1.22 the homomorphismπis surjective.
335
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(2) Clear from the existence of the surjectionπ.
(3) LetN := Ker(π)⊆A⊗V, so there is a short exact sequence
0→N→A⊗V
π
− →M→0
in M(A, gr), andN is a bounded below gradedA-module. IfM is graded-projective,
then this sequence is split. It follows thatK⊗AN = 0. By part (2) we see that
N = 0. □
Deﬁnition 15.2.31.Let A be a connected gradedK-ring, and letM∈M(A, gr).
The socle of M is the gradedA-submodule Soc(M) := HomA(K,M )⊆M.
In other words, Soc(M) = {m∈M |m·m = 0}. The A-module structure of
Soc(M) is through the augmentation homomorphismA→K; so Proposition 15.2.2
applies to it.
Here is a dual to the graded Nakayama Lemma.
Proposition 15.2.32. LetA be a connected gradedK-ring, letN∈M(A, gr) be a
bounded above graded module, and letW := Soc(N).
(1) There is an injectionσ: N ↣ HomK(A,W ) in M(A, gr), such that the
diagram
W id //
α

W
β

N σ // HomK(A,W )
in whichαand βare the canonical embeddings, is commutative.
(2) If W = 0 then N = 0.
(3) If N is a graded-injectiveA-module, then the homomorphismσabove is
bijective. HenceN is a graded-cofreeA-module.
Note that βis induced from the augmentation homomorphismA→K, and
Im(β) = Soc
(
HomK(A,W )
{
.
Proof.
(1) SayN =⨁
i≤i1 Ni for somei1∈Z. Choose a splittingσ0 :N↠W in M(K, gr)
of the inclusionα:W↣N. By adjunction there is an isomorphism
HomK(N,W )∼= HomA(N, HomK(A,W ))
in M(K, gr), so there is a homomorphismσ: N→HomK(A,W ) in M(A, gr) that
lifts σ0. See the commutative diagram below, whereγ(χ) :=χ(1A).
N
σ0
&&
σ // HomK(A,W )
γ

W
A descending induction on degree, starting fromi1, shows thatσis an injection.
(2) Clear from the existence ofσ.
(3) LetM := Coker(σ). IfN is graded-injective, then the exact sequence
0→N
σ
− →HomK(A,W )→M→0
in M(A, gr)issplit. Applyingtheadditivefunctor Soc toit, weseethat Soc(M) = 0.
Since M is a bounded above graded module, item (2) says thatM = 0. □
336
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁnition 15.2.33.Let A be a graded ring. A moduleN∈M(Aop, gr) is called
a coﬁnite gradedAop-module if N∼=M∗for some ﬁnite gradedA-module M.
The full subcategory ofM(Aop, gr)on the coﬁnite gradedAop-modules is denoted
by Mcof(Aop, gr).
Recall that an objectM in an abelian category M is called noetherian (resp.
artinian) if it satisﬁes the ascending (resp. descending) chain condition on subob-
jects. Let us denote the corresponding full subcategories ofM by Mnot and Mart
respectively. Then Mnot, Mart⊆M are thick abelian subcategories, closed under
subobjects and quotient objects.
Here is a variant of the Matlis Duality Theorem (see Remark 13.3.23):
Theorem 15.2.34 (NC Graded Matlis Duality). Assume A is a left noetherian
connected graded ring.
(1) The categoryMf(A, gr) is a thick abelian subcategory ofMdwf(A, gr), closed
under subobjects and quotient objects.
(2) The categoryMcof(Aop, gr) is a thick abelian subcategory ofMdwf(Aop, gr),
closed under subobjects and quotient objects.
(3) The functor
(−)∗: Mf(A, gr)op→Mcof(Aop, gr)
is an equivalence.
(4) The modules inMf(A, gr) are the noetherian objects in the abelian category
M(A, gr).
(5) The modules inMcof(Aop, gr) are the artinian objects in the abelian category
M(Aop, gr).
Proof.
(1) Since A is connected, as a left module it belongs toMdwf(A, gr). Therefore
every ﬁnite gradedA-module belongs toMdwf(A, gr), i.e.Mf(A, gr)⊆Mdwf(A, gr).
Because A is left noetherian, it follows thatMf(A, gr) is a thick abelian subcat-
egory of M(A, gr), closed under subobjects and quotient objects.
(2, 3) By deﬁnitionMcof(Aop, gr) is the essential image under the functor(−)∗of
the category Mf(A, gr). Now use the equivalence of Proposition 15.2.28 and part
(1).
(4) This is proved the same way as for ungraded left noetherian rings.
(5) We know by (2, 3, 4) that the objects ofMcof(Aop, gr) are artinian objects in
M(Aop, gr).
For the opposite direction, let N ∈M(Aop, gr) be an artinian object. The
descending chain condition forces N to be bounded above, namely Ni = 0 for
i≫0. Consider the socleW := HomAop(K,N ). This is a gradedAop-submodule
of N, isomorphic to ⨁
x∈XK(−ix) for some indexing set X and a collection of
integers{ix}x∈X. By the descending chain condition the setX has to be ﬁnite.
Hence ⨁
x∈X
A∗(−ix)∼=A∗⊗W∼= HomK(A,W ).
Proposition 15.2.32 tells us that there is an injective homomorphism N ↣⨁
x∈XA∗(−ix). We know thatA∗(−ix)∈Mcof(A, gr); and hence so isN. □
Remark 15.2.35.IfA is connected graded but not left noetherian, then there are
coﬁnite gradedAop-modules that are not artinian. Take the ringA :=K⟨x1,x 2⟩
from Example 15.2.19. ThenA∗∈M(Aop, gr) is coﬁnite but not artinian.
337
Derived Categories | Amnon Yekutieli | 14 Apr 2019
