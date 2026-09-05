---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-020-24-a-method-for-producing-proofs-in-abelian-cate
section_title: "A Method for Producing Proofs in Abelian Categories"
section_number: 2.4
pages: 38-42
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
diﬃculty in the theory of abelian categories is this: formulas that are easy to prove
for a module categoryM = ModA, usingelements, are often very hard to prove in
an abstract abelian categoryM (directly from the axioms).
A neat solution to this diﬃculty was found by P. Freyd and B. Mitchell:
Theorem 2.4.1 (Freyd-Mitchell). Let M be a small abelian category. ThenM is
equivalent to a full abelian subcategory ofModA, for a suitable ringA.
Remark 2.4.2.This is a deep and diﬃcult result. See [47], a book that’s basically
devoted to proving this theorem.
A modern proof can be found in in [76, Theorem 9.6.10] – but it too is very
involved. Roughly speaking, they show that the abelian categoryInd(Mop) of ind-
objects of M has an injective cogenerator. This implies that the abelian category
Pro(M) of pro-objects, that’s equivalent toInd(Mop)op, has a projective generator,
say P. Deﬁning the ringA := End Pro(M)(P )op, there is an equivalence of abelian
categories Pro(M)≈ModA. On the other hand, the Yoneda functor is a fully
faithful embedding M→Pro(M).
The Freyd-Mitchell Theorem implies that for purposes of ﬁnitary calculations in
the abelian category M (e.g. checking whether a sequence is exact, see Deﬁnition
2.3.24) we can assume that objects ofM have elements. This often simpliﬁes the
work.
Since we do not give a proof of the Freyd-Mitchell Theorem in our book, we feel
it is improper to use it. As a substitute, we provide the two “sheaf tricks” below,
namely Propositions 2.4.9 and 2.4.11, with full proofs. Later in the book these
sheaf tricks are used to give relatively easy proofs of several results on abstract
abelian categories, most notably Theorem 3.7.10 on the existence of the long exact
cohomology sequence. The method of proof using these tricks is explained in Re-
mark 2.4.6. It is not as slick as the method that the Freyd-Mitchell Theorem oﬀers;
but at least we have self-contained proofs. See Remark 2.4.12 for some background
(inﬂuence and history) on the sheaf tricks.
First an important technical lemma. In an abelian categoryM we have ﬁnite
products, and they are also coproducts (see Proposition 2.2.3).
Lemma 2.4.3. Let M be an abelian category. Consider a diagram
(D) M1×M2
p2 //
p1

M2
φ2

M1
φ1 //N
in M, wherepi are the projections. Deﬁne the object
L := Ker(φ1◦p1−φ2◦p2)⊆M1×M2,
with inclusion morphisme :L→M1×M2. Next deﬁne the morphismsψi :=pi◦e :
L→Mi.
38
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(1) The diagram
L
ψ2 //
ψ1

M2
φ2

M1
φ1 //N
is cartesian, andL =M1×N M2.
(2) If φ1 is an epimorphism, thenψ2 is an epimorphism.
Note that the diagram (D) is not assumed to be commutative. In case (D) does
happen to be commutative, thenM1×N M2 =M1×M2.
Proof. (1) The fact thatL (with the morphismsψi) is the ﬁbered product is im-
mediate from the deﬁnitions of product and kernel.
(2) Here we follow [Mac2, Sec VIII.4]. Letρbe a morphism such that
ρ◦(φ1◦p1−φ2◦p2) = 0.
Consider the embedding
e1 :M1→M1⊕M2 =M1×M2.
Then
0 =ρ◦(φ1◦p1−φ2◦p2)◦e1 =ρ◦φ1.
Because φ1 is an epimorphism, it follows thatρ= 0. We conclude that
(2.4.4) φ1◦p1−φ2◦p2 :M1×M2→N
is an epimorphism. Thus (2.4.4) is the cokernel ofe.
Next letσ: M2→P be a morphism such thatσ◦ψ2 = 0. Since ψ2 = p2◦e,
we getσ◦p2◦e = 0. Hence σ◦p2 factors through Coker(e). Namely there is a
morphism σ′:N→P such that
(2.4.5) σ◦p2 =σ′◦(φ1◦p1−φ2◦p2) :M1×M2→P.
But p2◦e1 = 0, and therefore
0 =σ◦p2◦e1 =σ′◦(φ1◦p1−φ2◦p2)◦e1 =σ′◦φ1.
As φ1 is an epimorphism, it follows thatσ′= 0. Finally, using (2.4.5), we get
σ=σ◦p2◦e2 =σ′◦(φ1◦p1−φ2◦p2)◦e2 =−σ′◦φ2 = 0.
We conclude thatψ2 is an epimorphism. □
Before giving the precise statements, here is a heuristic.
Remark 2.4.6. The sheaf tricks (Propositions 2.4.9 and 2.4.11) work like this:
we pretend that the objects of ourK-linear abelian category M are “sheaves on
an imaginary topological spaceX”; objects playing this role are denoted by letters
M,N,.... The objects of M are also “open sets in the topological spaceX”; and
objects playing this role are denoted by lettersU,V,.... Given a sheaf M and
an open set U, there is aK-module Γ(U,M ) of “sections ofM over U”. These
“sections” can be added and subtracted, being elements of aK-module. Sometimes
we require “reﬁnement”, i.e. replacing an “open setU” by a “coveringV ↠ U”,
giving rise to an embeddingK-modules Γ(U,M )↣ Γ(V,M ). This allegory is made
precise in Deﬁnition 2.4.7 below.
Deﬁnition 2.4.7(Sheaf Metaphor). Let M be aK-linear abelian category.
(1) Objects of M are called sheaves or open sets, depending on the role they
play in each context.
39
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(2) For an open set U ∈M and a sheaf M ∈M we write Γ(U,M ) :=
HomM(U,M ). This is aK-module, and we call it themodule of sections of
the sheafM over the open setU.
(3) Given a morphismρ: V →U of open sets inM, and a sheafM∈M, we
use this notation for the resultingK-module homomorphism:
ρ∗:= HomM(ρ,idM) : Γ(U,M )→Γ(V,M ).
We callρ∗the pullback alongρ.
(4) Given a morphismφ: M→N of sheaves inM, and an open setU∈M,
we use this notation for the resultingK-module homomorphism:
Γ(U,φ) := HomM(idU,φ) : Γ(U,M )→Γ(U,N ).
(5) Ifρ:V →U is a morphism of open sets inM that is an epimorphism, then
we callρa covering ofU. The homomorphismρ∗in this case is called the
restriction ofM fromU to V.
Note that given a coveringρ: V ↠ U, the restriction homomorphism ρ∗is
injective (see Proposition 2.3.27(2)). By slight abuse of notation, when the covering
ρis clear from the context, we will often identify theK-module Γ(U,M ) with its
image in Γ(V,M ) under ρ∗. Another convenient abuse of notation is writing φ
instead of Γ(U,φ), for a morphismφ: M→N in M and open setU. Combined,
these notations give sense to such a commutative diagram
(2.4.8) Γ(U,M )
φ //
⊆

Γ(U,N )
⊆

Γ(V,M )
φ // Γ(V,N )
in ModK. This will be used in item (3) of the next proposition.
Proposition 2.4.9 (First Sheaf Trick). Let φ: M →N be a morphism in an
abelian categoryM.
(1) The morphismφis zero if and only if for everyU∈M the homomorphism
Γ(U,φ) in ModK is zero.
(2) The morphism φis a monomorphism if and only if for everyU∈M the
homomorphism Γ(U,φ) in ModK is injective.
(3) The morphism φis an epimorphism if and only if for everyU ∈M and
every sectionn∈Γ(U,N ), there exists a coveringV ↠ U and a section
m∈Γ(V,M ), such thatφ(m) =n in Γ(V,N ).
The heuristic interpretation of item (3) of the proposition is this:φ:M→N is
an epimorphism inM if and only if it is “locally surjective”.
Proof. (1) Ifφ= 0 then for everym∈Γ(U,M ) we haveΓ(U,φ)(m) =φ◦m = 0 in
Γ(U,N ); thus Γ(U,φ) = 0. Conversely, ifΓ(U,φ) = 0 for allU, then takeU :=M
and m := idM∈Γ(U,M ). We obtainφ= Γ(U,φ)(m) = 0.
(2) First assumeφis a monomorphism. Take an arbitrary objectU and a section
m∈Γ(U,M ). So m : U →M is a morphism in M. If φ◦m = 0, then, by the
deﬁnition of a monomorphism, we must havem = 0. Thus Γ(U,φ) is injective.
Conversely, assume thatΓ(U,φ) is injective for everyU. TakeU := Ker(φ) and
let m :U→M be the inclusion. ThenΓ(U,φ)(m) = φ◦m = 0. But thenm = 0
and U = 0. Thusφis a monomorphism.
(3) First assumeφis an epimorphism. Consider a sectionn∈Γ(U,N ). So we have
morphisms φ: M↠ N and n : U→N. Let V := M×N U, the ﬁbered product.
By Lemma 2.4.3(2) the projectionρ:V →U is an epimorphism, i.e. a covering in
40
Derived Categories | Amnon Yekutieli | 14 Apr 2019
our terminology. Now the other projectionm :V →M satisﬁesφ◦m =n◦ρ. This
means thatφ(m) =n in Γ(V,N ).
Conversely, let us takeU := N and n := idN ∈Γ(U,N ). There exists an
epimorphism ρ:V ↠U and a morphismm :V →M such thatφ◦m =n◦ρ=ρ.
We see thatφ◦m is an epimorphism, and henceφis an epimorphism. □
Example 2.4.10. Suppose
S =
(
0→M′φ
− →M
ψ
− →M′′→0
{
is a sequence inM. Here is how exactness ofS is tested using the ﬁrst sheaf trick.
By item (1) of the ﬁrst sheaf trick, the conditionψ◦φ= 0 is same asΓ(U,ψ◦φ) =
0 for everyU∈M.
Exactness atM′is the same as this condition: for everyU∈M and every section
m′∈Γ(U,M′), ifφ(m′) = 0 then m′= 0. This is by item (2).
Exactness at M′′is the same as this condition: for every U ∈M and every
sectionm′′∈Γ(U,M′′), there exists a coveringV ↠U and a sectionm∈Γ(V,M ),
such thatψ(m) =m′′in Γ(V,M′′).
Finally, exactness atM is the same as this condition (given thatψ◦φ= 0): for
every U∈M and every sectionm∈Γ(U,M ) such thatψ(m) = 0, there exists a
coveringV ↠U and a sectionm′∈Γ(V,M′), such thatφ(m′) =m in Γ(V,M′′).
Proposition 2.4.11 (Second Sheaf Trick). LetM be an object in an abelian cat-
egory M. Suppose ρ1 : V1→U and ρ2 : V2→U are morphisms in M, such that
(ρ1,ρ2) : V1⊕V2→U is an epimorphism. Let W := V1×U V2, with projection
morphisms σ1 :W→V1 and σ2 :W→V2. Then the sequence
0→Γ(U,M )
(ρ∗
1,ρ∗
2)
−−−−→Γ(V1,M )×Γ(V2,M )
(σ∗
1,−σ∗
2)
−−−−−−→Γ(W,M )
in ModK is exact.
Proof. Note thatV1×V2 =V1⊕V2. By Lemma 2.4.3(1) there is an exact sequence
0→W
(σ1,−σ2)
−−−−−−→V1⊕V2
(ρ1,ρ2)
−−−−→U→0
in M. By Proposition 2.3.27(2) we get an exact sequence
0→Γ(U,M )
(ρ∗
1,ρ∗
2)
−−−−→Γ(V1⊕V2,M )
(σ1,−σ2)∗
−−−−−−→Γ(W,M )
in Ab. But
Γ(V1⊕V2,M )∼= Γ(V1,M )×Γ(V2,M ). □
Remark 2.4.12. As can be seen in the practical application of our sheaf tricks
(e.g. in the proofs of Proposition 2.5.18 and Theorem 3.7.10) these tricks reduce
proofs about an abstract abelian category M, to proofs that are just like in the
concrete case of the abelian categoryM = AbX of sheaves of abelian groups on a
topological spaceX. This is not as easy as the caseM = ModA of modules over a
ring A, that the Freyd-Mitchell Theorem permits, but – at least for someone with
experience in algebraic geometry – our method is quite straightforward.
Our sheaf tricks are inspired by [144, tag 05PL]. There it is shown that the
geometric allegory is genuine, except that instead of a topological spaceX, there is
a site X (in the sense of Grothendieck). The underlying category of the siteX is
the abelian category M itself, and the coverings ofX are the epimorphisms inM.
It is proved in [144] that the categoryM embeds as a full abelian subcategory of
AbX, the category of sheaves of abelian groups onX.
Proposition 2.4.9 is very similar to [102, Theorem VIII.3], where what we call
“sections” are called “members”. But S. MacLane’s method loses the abelian group
structure (the members are not elements of abelian groups). An improvement of
MacLane’s method can be found in an unpublished note of G. Bergman [18].
41
Derived Categories | Amnon Yekutieli | 14 Apr 2019
