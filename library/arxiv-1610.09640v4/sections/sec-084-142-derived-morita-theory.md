---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-084-142-derived-morita-theory
section_title: "Derived Morita Theory"
section_number: 14.2
pages: 295-302
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
particular all DG rings areK-central, and⊗=⊗K.
Deﬁnition 14.2.1.LetA andB be DG rings. The objects of the categoryC(A⊗
Bop) are calledDG A-B-bimodules.
There is a commutative diagram (14.2.2) inDGRng/cK.
(14.2.2) A⊗Bop
A
99
Bop
ff
K
ee 88
OO
By restriction there is a commutative diagram of DG functors, and a commuta-
tive diagram of triangulated functors, see (14.2.3).
295
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(14.2.3)
C(A⊗Bop)
RestA
ww
RestBop
((
RestK

C(A)
RestK ’’
C(Bop)
RestKvv
C(K)
D(A⊗Bop)
RestA
ww
RestBop
((
RestK

D(A)
RestK ’’
D(Bop)
RestKvv
D(K)
There are several manipulations of DG bimodules that we are going to use. First
we note that(Aop)op =A. Next, given DGK-modules M and N, let
(14.2.4) brM,N :M⊗N
≃
− →N⊗M
be the isomorphism inC(K) deﬁned by
(14.2.5) brM,N (m⊗n) := (−1)i·j·n⊗m
for homogeneous elementsm∈Mi andn∈Nj. In Subsection 3.1 the isomorphism
brM,N was called the braiding of the symmetric monoidal categoryC(K). If M∈
C(Aop), then we can viewM either as a left DGAop-module, or as a right DG
A-module. The opposite holds forN∈C(A). It is not hard to see that there is an
isomorphism
(14.2.6) M⊗AN
≃
− →N⊗AopM
in C(K) with the same formula (14.2.5). This works also for DG rings: there are
isomorphisms
(14.2.7) A⊗Bop ≃
− →Bop⊗A
and
(14.2.8) A⊗Bop ≃
− →(B⊗Aop)op
in DGRng/cK, with a formulas like (14.2.5).
There is a DG bifunctor
(14.2.9) (−⊗B−) : C(A⊗Bop)×C(B)→C(A).
Here is a variation of Theorem 12.3.1.
Proposition 14.2.10. The bifunctor (14.2.9) has a triangulated left derived bi-
functor
(−⊗L
B−) : D(A⊗Bop)×D(B)→D(A).
IfP∈D(B) is a K-ﬂat DG module, then for everyM∈D(A⊗Bop) the morphism
ηL
M,P :M⊗L
BP→M⊗BP
in D(A) is an isomorphism.
Proof. This is because C(B) has enough K-ﬂat objects. See Theorem 9.3.16 and
Lemma 12.3.2. □
Remark 14.2.11.There is a delicate issue here. Even though the categoryC(A⊗
Bop) has enough K-ﬂat objects, they can not be used to calculate(−⊗L
B−). The
reason is this: givenN∈C(B), the DG(A⊗Bop)-modules that are acyclic for the
DG functor (−)⊗BN are those that areK-ﬂat overBop. In general, a K-ﬂat DG
(A⊗Bop)-module M is not K-ﬂat as aBop-module.
A suﬃcient condition for a K-ﬂat DG(A⊗Bop)-module M to be K-ﬂat over
Bop is thatA is K-ﬂat as a DGK-module. In Subsection 14.3 we will make heavy
use of this fact.
296
Derived Categories | Amnon Yekutieli | 14 Apr 2019
There is another DG bifunctor we shall want to use:
(14.2.12) HomA(−,−) : C(A⊗Bop)op×C(A)→C(B).
Here is a variation of Theorem 12.2.1.
Proposition 14.2.13. The bifunctor (14.2.12) has a triangulated right derived
bifunctor
RHomA(−,−) : D(A⊗Bop)op×D(A)→D(B).
If I ∈D(A) is a K-injective DG module, then for everyM ∈D(A⊗Bop) the
morphism
ηR
M,I : HomA(M,I )→RHomA(M,I )
in D(B) is an isomorphism.
Proof. This is because C(A) has enough K-injective objects. See Theorem 9.2.16,
Theorem 9.3.11 and Lemma 12.2.2. □
Remark 14.2.14. Like in Remark 14.2.11, even though the categoryC(A⊗Bop)
has enough K-projective DG modules, they can not be used to calculate
RHomA(−,N ). This is because a K-projective DG (A⊗Bop)-module P is not,
in general, K-projective overA.
A suﬃcient condition for a K-projective DG (A⊗Bop)-module P to be K-
projective overA is thatB is K-projective overK. This is a bit stronger than the
condition thatB is K-ﬂat overK.
Proposition 14.2.15.LetL∈D(A⊗Bop), and consider theK-linear triangulated
functors
F := RHomA(L,−) : D(A)→D(B)
and
G :=L⊗L
B (−) : D(B)→D(A).
Then:
(1) The functorF is a right adjoint ofG.
(2) The functorF is an equivalence if and only if the functorG is an equiva-
lence.
Proof.
(1) GivenM∈D(B) and N∈D(A) we choose a K-projective resolutionP→M
in Cstr(B) and a K-injective resolutionN→I in Cstr(A). We get isomorphisms
F (N)∼= F (I)∼= HomA(L,I ) and G(M)∼= G(P )∼= L⊗B P in D(B) and D(A)
respectively. These give rise to isomorphisms ofK-modules
HomD(B)
(
M,F (N)
{∼=⋄H0(
RHomB
(
M,F (N)
{{
∼= H0(
HomB
(
P, HomA(L,I )
{{∼=†H0(
HomA(L⊗BP,I )
{
∼= H0(
RHomA
(
G(M),N
{{∼=⋄HomD(A)
(
G(M),N
{
.
The isomorphism∼=†is due to the noncommutative Hom-tensor adjunction (see
[129, Theorem 2.11]), and the isomorphisms∼=⋄are by Corollary 12.2.8. The com-
posed isomorphism
HomD(B)
(
M,F (N)
{∼= HomD(A)
(
G(M),N
{
is functorial inM and N.
(2) Clear from (1). □
Deﬁnition 14.2.16.Let A and B be DG rings. A DG moduleL∈D(A⊗Bop)
is called a pretilting DGA-B-bimodule if it satisﬁes the equivalent conditions in
Proposition 14.2.15(2).
297
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Remark 14.2.17.The literature has several diﬀerent meanings for the word “tilt-
ing”. See Remark 14.2.39 for a historical survey. The commonly perceived meaning
of a tilting object, say as in the book [3], is very close to what we call a pretilting
DG bimodule (whenA and B are rings).
Notice that there is a lack of symmetry in the deﬁnition of a pretilting DGA-B-
bimodule L. This lack of symmetry will disappear when we talk abouttilting DG
bimodules in Subsection 14.3.
Deﬁnition 14.2.18.Let A and B be DG rings, and letM ∈C(A⊗Bop). We
say that M is K-ﬂat(resp. K-injective, resp. K-projective, resp. semi-free, resp.
algebraically perfect) over A, oron theA side, if RestA(M)∈C(A) is K-ﬂat (resp.
K-injective, resp.K-projective, resp. semi-free, resp. algebraicallyperfect). Likewise
we deﬁne the propertieson theBop side.
Proposition 14.2.19. SupposeL∈D(A⊗Bop) is a pretilting DGA-B-bimodule.
Then L is an algebraically perfect DGA-module.
Proof. Under the equivalenceG : D(B)→D(A) from Proposition 14.2.15 we have
G(B)∼= L. Of course B∈D(B) is an algebraically perfect DGB-module. Now
use Corollary 14.1.24. □
Observe that an objectN ∈D(A) is nonzero if it is not a zero object of the
category D(A), i.e. if N ⁄∼= 0 in D(A). This is equivalent to the condition that
H(N)⁄= 0. The clariﬁcation is important for the next deﬁnition.
Deﬁnition 14.2.20.Let E⊆D(A) be a full triangulated subcategory that’s closed
under inﬁnite direct sums.
(1) An objectL∈D(A) is called acompact object relative toE if the functor
HomD(A)(L,−) : E→M(K)
commutes with inﬁnite direct sums.
(2) An objectL∈D(A) is called agenerator relative toE if for every nonzero
object N∈E there exists somei∈Z such that HomD(A)(L,N [i])⁄= 0.
(3) An objectL∈E is called acompact generator ofE if it is both a compact
object relative toE and a generator relative toE.
Example 14.2.21. For every positive integerr the free DG moduleP :=Ar is a
compact generator ofE := D(A).
Example 14.2.22. Assume A is a commutative noetherian ring and a =
(a1,...,an) is a ﬁnite sequence of elements in it. (Or, more generally,A is com-
mutative anda is a weakly proregular sequence, as in [118].) Let a⊆A be the
ideal generated bya. A complex M ∈D(A) is called cohomologically a-torsion
if all its cohomology modulesHi(M) are a-torsion. Consider the full subcategory
E := Da-tor(A) of D(A) on the cohomologicallya-torsion complexes. This is full tri-
angulated subcategory that’s closed under inﬁnite direct sums. The Koszul complex
K(A;a) is a compact generator ofDa-tor(A). See [119, Proposition 5.1].
Proposition 14.2.23.LetA andB be DG rings,F : D(A)→D(B) an equivalence
of triangulated categories, E⊆D(A) a full triangulated subcategory that’s closed
under inﬁnite direct sums, andL∈D(A).
(1) L is a compact object relative toE if and only ifF (L) is a compact object
relative toF (E).
(2) L is a generator relative toE if and only ifF (L) is a generator relative to
F (E).
Proof. For item (1) use the proof of Proposition 14.1.8. Item (2) is trivial. □
298
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁnition 14.2.24.LetA andB be DG rings, letE⊆D(A) be a full triangulated
subcategory that is closed under inﬁnite direct sums, and letL∈D(A⊗Bop).
(1) We say thatL is acompact object relative toE on theA side if RestA(L)∈
D(A) is a compact object relative to E, in the sense of Deﬁnition
14.2.20(1).
(2) We say thatL is agenerator relative toE on theA side if RestA(L)∈D(A)
is a generator relative toE, in the sense of Deﬁnition 14.2.20(2).
(3) We say thatL is acompact generator ofE on theA side if RestA(L)∈D(A)
is a compact generator ofE, in the sense of Deﬁnition 14.2.20(3).
Lemma 14.2.25. Let E⊆D(A) be a full triangulated subcategory that is closed
under inﬁnite direct sums, and letL∈D(A⊗Bop). The following two conditions
are equivalent.
(i) The functor RHomA(L,−)|E : E →D(B) commutes with inﬁnite direct
sums.
(ii) L is a compact object relative toE on theA side.
Proof. Let’s writeF := RHomA(L,−). We know that for everyM ∈D(A) and
j∈Z there are isomorphisms
HomD(A)(L,M [j])∼= H0(F (M[j]))∼= Hj(F (M))
in M(K), and they are functorial inM. We see thatL is a compact object relative
to E on theA side iﬀ the functorH◦F|E : E→Gstr(K) commutes with inﬁnite
direct sums. But the functor H : D(B)→Gstr(K) commutes with inﬁnite direct
sums and is conservative (see Corollary 7.2.13). SoH◦F|E commutes with inﬁnite
direct sums iﬀF|E does. □
Lemma 14.2.26. Let A and B be DG rings, letF,G : D(A)→D(B) be trian-
gulated functors that commute with inﬁnite direct sums, and letη: F →G be a
morphism of triangulated functors. Assume thatηA :F (A)→G(A) is an isomor-
phism. Thenηis an isomorphism.
Proof. Let us denote byE the full subcategory ofD(A) on the objectsM such that
ηM :F (M)→G(M) is an isomorphism. We have to prove thatE = D(A).
By Proposition 5.3.22, the categoryE is a full triangulated subcategory ofD(A).
Since both functors F,G commute with inﬁnite direct sums, we know thatE is
closed under inﬁnite direct sums.
We are given that the free DG moduleA belongs to E. Hence every free DG
A-module P is in E. Because E is triangulated, it follows that every semi-free DG
A-module P of ﬁnite extension length (Deﬁnition 14.1.1) belongs to it.
Next consider an arbitrary semi-free DGA-module P. Let {Fj(P )}j≥−1 be a
semi-free ﬁltration ofP (see Deﬁnition 11.4.3). ThenP is a homotopy colimit of
the direct system{Fj(P )}j≥−1, and we have a distinguished triangle
(14.2.27)
⨁
j∈N
Fj(P )
φ
−−→
⨁
j∈N
Fj(P )−→P
∆
−→
in D(A); see Deﬁnition 14.1.11. EachFj(P ) is a semi-free DGA-module of ﬁnite
extension length. It follows thatP∈E.
Finally, every DGA-module M admits a quasi-isomorphismP →M with P
semi-free. ThereforeM∈E. □
Lemma 14.2.28.LetA andB be DG rings, letE be a full triangulated subcategory
of D(A) which is closed under inﬁnite direct sums and isomorphisms, and letG :
D(B)→D(A) be a triangulated functor that commutes with inﬁnite direct sums.
Assume thatG(B)∈E. Then the essential image ofG is contained inE.
Proof. This is like the proof of Lemma 14.2.26. □
299
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Let A be a DG ring. Given a DGA-module M, the DG ringEndA(M) acts on
M from the left; and thusB := EndA(M)op acts onM from the right. Because
the right action ofB on M commutes with the left action ofA on it, we see that
M∈C(A⊗Bop).
Recall that the categoryC(A) has enough K-projective and K-injective objects.
Theorem 14.2.29 (Derived Morita). Let A be a DG ring, let E⊆D(A) be a
full triangulated subcategory which is closed under inﬁnite direct sums, and letL
be a compact generator of E. Choose an isomorphism L ∼= P in D(A), where
the DGA-module P is either K-projective or K-injective, and deﬁne the DG ring
B := EndA(P )op. Consider the triangulated functors
F := RHomA(P,−) : D(A)→D(B)
and
G :=P⊗L
B (−) : D(B)→D(A).
Then the functor
F|E : E→D(B)
is an equivalence, with quasi-inverseG.
This theorem is a variant of [79, Theorem 8.2] by B. Keller. In fact, Keller
worked in the more general setting of a DG categoryA, whereas we only treat a
DG ringA. For the history of these ideas see Remark 14.2.39. A comparison to
classical Morita theory can be found in Example 14.2.36.
Note that if we choose P to be a K-projective DG A-module, then F ∼=
HomA(P,−). However, even then,P will rarely be K-ﬂat as a DGBop-module, so
G is only the left derived functor ofP⊗B (−).
Proof. The proof is in four steps.
Step 1. We can assume that the categoryE is closed under isomorphisms inD(A).
The functor G commutes with inﬁnite direct sums (see Proposition 12.3.8), and
G(B)∼=L∈E. According to Lemma 14.2.28 the image ofG is contained inE.
Step 2. We already know that the functorF is right adjoint toG, by Proposition
14.2.15. The corresponding morphisms of triangulated functors are denoted by
(14.2.30) θ: IdD(B)→F◦G and ζ:G◦F→IdD(A).
By step 1 we see thatF|E : E→D(B) is the right adjoint ofG : D(B)→E. Hence
(14.2.30) restricts to morphisms of triangulated functors
(14.2.31) θ: IdD(B)→F|E◦G and ζ:G◦F|E→IdE.
We will prove thatθand ζin (14.2.31) are isomorphisms. By Lemma 14.2.25 the
functorF|E commutes with inﬁnite direct sums. Therefore bothF|E◦G andG◦F|E
commute with inﬁnite direct sums.
Step 3. Now we will prove thatθis an isomorphism of functors; i.e. for everyN∈
D(B)the morphismθN :N→(F|E◦G)(N)is an isomorphism. The functorsIdD(B)
andF|E◦G both commute with inﬁnite direct sums. Therefore, by Lemma 14.2.26,
it suﬃces to check thatθB is an isomorphism inD(B). ButθB is represented (both
whenP is K-projective and when it is K-injective) by the canonical homomorphism
˜θB :B→HomA(P,P ⊗BB), in Cstr(B), which is clearly bijective.
Step 4. Finally we will prove thatζis an isomorphism of functors. Take anyM∈E,
and consider the distinguished triangle
(14.2.32) (G◦F|E)(M)
ζM
−−→M→M′∆
−→
in E, in whichM′∈E is the cone ofζM (see Deﬁnition 5.3.7).
300
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Applying F and using the functorial isomorphismθwe get a distinguished tri-
angle
(14.2.33) F|E(M)
idF|E(M)
−−−−−→F|E(M)→F|E(M′)
∆
−→
in D(B). This implies that F|E(M′)∼= 0 in D(B), and thus, after applying the
forgetful functor, we getF|E(M′)∼= 0 in D(K). ButF|E(M′)∼= RHomA(L,M′), so
HomD(A)(L,M′[i]) = 0 for alli. BecauseL is generator ofE, it follows thatM′∼= 0
in E. Going back to the distinguished triangle (14.2.32) we conclude thatζM is an
isomorphism. □
Remark 14.2.34. Suppose that in the theorem we were to choose some other
isomorphism L∼= P′in D(A) to a K-projective or K-injective DGA-module P.
Then the DG ringB′:= EndA(P′)op would be related toB as follows. Without
loss of generality we can assume that eitherP is K-projective orP′is K-injective.
Then there is a quasi-isomorphismφ:P→P′in Cstr(A), unique up to homotopy,
that respects the given isomorphismsL∼= P and L∼= P′in D(A). Deﬁne the
DG bimodule N := HomA(P,P′)∈C(B⊗B′op), and the matrix DG ringC :=
B N[−1]
0 B′

, which has a diﬀerential depending onφ. Then the obvious DG ring
homomorphismsC→B andC→B′arequasi-isomorphisms. See[119, Proposition
3.3].
Example 14.2.35. In case E = D(A), the theorem shows that the DG bimodule
P∈D(A⊗Bop) is a pretilting DGA-B-bimodule.
Example 14.2.36.AssumeA is a ring, andP∈M(A) = ModA is aprogenerator,
i.e.P is a ﬁnitely generated projectiveA-module, such that every nonzeroA-module
N admits a nonzero homomorphismP→N. Let B := EndA(P )op. Because P is
a compact generator ofD(A), the theorem says that
F := HomA(P,−) : D(A)→D(B)
is an equivalence of triangulated categories.
Classical Morita Theory (see e.g. [130, Section 4.1]) says thatF restricts to an
equivalence of abelian categories
F = HomA(P,−) : M(A)→M(B).
Furthermore, classical Morita theory tells us that there is a bijection between the
set of isomorphism classes of suchA-B-bimodules P, and the set of isomorphism
classes of linear equivalencesF : M(A)→M(B). This last assertion is an open
problem in derived Morita theory; see Remark 14.4.36.
Remark 14.2.37. Here is a geometric variant of Theorem 14.2.29. Let(X,OX)
be a scheme. We denote byDqc(X) = Dqc(ModOX) the derived category of (un-
bounded) complexes ofOX-modules with quasi-coherent cohomology sheaves. This
is a triangulated category with inﬁnite direct sums, and with enough K-injective
resolutions (by [143, Theorem 4.5]).
SupposeL∈Dqc(X) is a compact generator. Choose a K-injective resolution
L→Iin Cstr(X), and deﬁne the DG ringB := EndX(I)op. Then the functor
(14.2.38) RHomX(I,−) : Dqc(X)→D(B)
is an equivalence, with quasi-inverse
I⊗L
B (−) : D(B)→Dqc(X).
This result is stated as [26, Corollary 3.1.8], without such a precise formulation,
and the proof is attributed to B. Keller. Presumably the proof of Theorem 14.2.29
above, with slight changes, would work also in this geometric context.
301
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Having a compact generator ofDqc(X) is quite a general feature – by [26, The-
orem 3.1.1] this is true ifX is quasi-compact and quasi-separated.
The ﬁrst such result is perhaps due to A. Beilinson [15], who showed that for
X = Pn
K, then-dimensional projective space over a ﬁeldK, the sheaf
L :=
⨁n
i=0
OX(i)
is a compact generator ofDqc(X). The DG ringB appearing in the equivalence
(14.2.38) is actually a ﬁniteK-ring (the path ring of a Kronecker quiver modulo
commutation relations).
Remark 14.2.39. Tilting theory and derived Morita theory have their origins in
the representation theory of ﬁnite dimensional algebras(in our terminology these
are “ﬁnite centralK-rings”, whereK is a base ﬁeld). Among the ﬁrst examples of
tilting are thereﬂection functorsin the paper [19] by I.N. Bernstein, I.M. Gelfand
and V.A. Ponomarev. Later these functors were understood to be of the form
HomA(T,−) for atilting A-moduleT.
These ideas were generalized by M. Auslander, M. Platzeck and I. Reiten [11],
and later by S. Brenner and M.C.R. Butler [29], who coined the termtilting functor.
These concepts were further clariﬁed by D. Happel, C.M. Ringel and K. Bongartz
(see [58], [59] and [61]). In [58] Happel showed that for a tilting A-module T,
with opposite endomorphism ringB := EndA(T )op, the functor RHomA(T,−) is
an equivalence of triangulated categoriesDb
f (A)→Db
f (B). This result was slightly
generalized by E. Cline, B. Parshall and L. Scott [41].
J. Rickard [126], [127] was the ﬁrst to talk abouttilting complexes(as opposed to
tilting modules). He introduced two-sided tilting complexes (that we will discuss in
Subsection 14.4), and proved the celebrated Theorem 14.4.30 (under some bounded-
ness conditions). The generalization of derived Morita theory to unbounded derived
categories, and from rings to DG categories, was done by B. Keller [79]. In this
seminal paper Keller also gave new construction of two-sided tilting complexes, and
characterized algebraic triangulated categories with a compact generator as those
that are equivalent to derived categories of DG rings.
For a thorough survey of tilting theory see the book [3].
