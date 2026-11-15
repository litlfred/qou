---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-022-24-a-method-for-producing-proofs-in-abelian-cate
section_title: "A Method for Producing Proofs in Abelian Categories"
section_number: 2.4
pages: 38-42
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
diﬃculty in the theory of abelian categories is this: formulas that are easy to prove
for a module category M = Mod A, using elements, are often very hard to prove in
an abstract abelian category M (directly from the axioms).
A neat solution to this diﬃculty was found by P. Freyd and B. Mitchell:
Theorem 2.4.1 (Freyd-Mitchell). Let M be a small abelian category. Then M is
equivalent to a full abelian subcategory of Mod A, for a suitable ring A.
Remark 2.4.2. This is a deep and diﬃcult result. See [47], a book that’s basically
devoted to proving this theorem.
A modern proof can be found in in [76, Theorem 9.6.10] – but it too is very
involved. Roughly speaking, they show that the abelian category Ind(Mop) of ind-
objects of M has an injective cogenerator. This implies that the abelian category
Pro(M) of pro-objects, that’s equivalent to Ind(Mop)op, has a projective generator,
say P. Deﬁning the ring A := EndPro(M)(P)op, there is an equivalence of abelian
categories Pro(M) ≈Mod A.
On the other hand, the Yoneda functor is a fully
faithful embedding M →Pro(M).
The Freyd-Mitchell Theorem implies that for purposes of ﬁnitary calculations in
the abelian category M (e.g. checking whether a sequence is exact, see Deﬁnition
2.3.24) we can assume that objects of M have elements. This often simpliﬁes the
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
First an important technical lemma. In an abelian category M we have ﬁnite
products, and they are also coproducts (see Proposition 2.2.3).
Lemma 2.4.3. Let M be an abelian category. Consider a diagram
(D)
M1 × M2
p2
/
p1

M2
φ2

M1
φ1
/ N
in M, where pi are the projections. Deﬁne the object
L := Ker(φ1 ◦p1 −φ2 ◦p2) ⊆M1 × M2,
with inclusion morphism e : L →M1 ×M2. Next deﬁne the morphisms ψi := pi ◦e :
L →Mi.
38
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
(1) The diagram
L
ψ2
/
ψ1

M2
φ2

M1
φ1
/ N
is cartesian, and L = M1 ×N M2.
(2) If φ1 is an epimorphism, then ψ2 is an epimorphism.
Note that the diagram (D) is not assumed to be commutative. In case (D) does
happen to be commutative, then M1 ×N M2 = M1 × M2.
Proof. (1) The fact that L (with the morphisms ψi) is the ﬁbered product is im-
mediate from the deﬁnitions of product and kernel.
(2) Here we follow [Mac2, Sec VIII.4]. Let ρ be a morphism such that
ρ ◦(φ1 ◦p1 −φ2 ◦p2) = 0.
Consider the embedding
e1 : M1 →M1 ⊕M2 = M1 × M2.
Then
0 = ρ ◦(φ1 ◦p1 −φ2 ◦p2) ◦e1 = ρ ◦φ1.
Because φ1 is an epimorphism, it follows that ρ = 0. We conclude that
(2.4.4)
φ1 ◦p1 −φ2 ◦p2 : M1 × M2 →N
is an epimorphism. Thus (2.4.4) is the cokernel of e.
Next let σ : M2 →P be a morphism such that σ ◦ψ2 = 0. Since ψ2 = p2 ◦e,
we get σ ◦p2 ◦e = 0. Hence σ ◦p2 factors through Coker(e). Namely there is a
morphism σ′ : N →P such that
(2.4.5)
σ ◦p2 = σ′ ◦(φ1 ◦p1 −φ2 ◦p2) : M1 × M2 →P.
But p2 ◦e1 = 0, and therefore
0 = σ ◦p2 ◦e1 = σ′ ◦(φ1 ◦p1 −φ2 ◦p2) ◦e1 = σ′ ◦φ1.
As φ1 is an epimorphism, it follows that σ′ = 0. Finally, using (2.4.5), we get
σ = σ ◦p2 ◦e2 = σ′ ◦(φ1 ◦p1 −φ2 ◦p2) ◦e2 = −σ′ ◦φ2 = 0.
We conclude that ψ2 is an epimorphism.
□
Before giving the precise statements, here is a heuristic.
Remark 2.4.6. The sheaf tricks (Propositions 2.4.9 and 2.4.11) work like this:
we pretend that the objects of our K-linear abelian category M are “sheaves on
an imaginary topological space X”; objects playing this role are denoted by letters
M, N, . . .. The objects of M are also “open sets in the topological space X”; and
objects playing this role are denoted by letters U, V, . . ..
Given a sheaf M and
an open set U, there is a K-module Γ(U, M) of “sections of M over U”. These
“sections” can be added and subtracted, being elements of a K-module. Sometimes
we require “reﬁnement”, i.e. replacing an “open set U” by a “covering V ↠U”,
giving rise to an embedding K-modules Γ(U, M) ↣Γ(V, M). This allegory is made
precise in Deﬁnition 2.4.7 below.
Deﬁnition 2.4.7 (Sheaf Metaphor). Let M be a K-linear abelian category.
(1) Objects of M are called sheaves or open sets, depending on the role they
play in each context.
39
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
(2) For an open set U ∈M and a sheaf M ∈M we write Γ(U, M) :=
HomM(U, M). This is a K-module, and we call it the module of sections of
the sheaf M over the open set U.
(3) Given a morphism ρ : V →U of open sets in M, and a sheaf M ∈M, we
use this notation for the resulting K-module homomorphism:
ρ∗:= HomM(ρ, idM) : Γ(U, M) →Γ(V, M).
We call ρ∗the pullback along ρ.
(4) Given a morphism φ : M →N of sheaves in M, and an open set U ∈M,
we use this notation for the resulting K-module homomorphism:
Γ(U, φ) := HomM(idU, φ) : Γ(U, M) →Γ(U, N).
(5) If ρ : V →U is a morphism of open sets in M that is an epimorphism, then
we call ρ a covering of U. The homomorphism ρ∗in this case is called the
restriction of M from U to V .
Note that given a covering ρ : V ↠U, the restriction homomorphism ρ∗is
injective (see Proposition 2.3.27(2)). By slight abuse of notation, when the covering
ρ is clear from the context, we will often identify the K-module Γ(U, M) with its
image in Γ(V, M) under ρ∗.
Another convenient abuse of notation is writing φ
instead of Γ(U, φ), for a morphism φ : M →N in M and open set U. Combined,
these notations give sense to such a commutative diagram
(2.4.8)
Γ(U, M)
φ
/
⊆

Γ(U, N)
⊆

Γ(V, M)
φ
/ Γ(V, N)
in Mod K. This will be used in item (3) of the next proposition.
Proposition 2.4.9 (First Sheaf Trick). Let φ : M →N be a morphism in an
abelian category M.
(1) The morphism φ is zero if and only if for every U ∈M the homomorphism
Γ(U, φ) in Mod K is zero.
(2) The morphism φ is a monomorphism if and only if for every U ∈M the
homomorphism Γ(U, φ) in Mod K is injective.
(3) The morphism φ is an epimorphism if and only if for every U ∈M and
every section n ∈Γ(U, N), there exists a covering V ↠U and a section
m ∈Γ(V, M), such that φ(m) = n in Γ(V, N).
The heuristic interpretation of item (3) of the proposition is this: φ : M →N is
an epimorphism in M if and only if it is “locally surjective”.
Proof. (1) If φ = 0 then for every m ∈Γ(U, M) we have Γ(U, φ)(m) = φ ◦m = 0 in
Γ(U, N); thus Γ(U, φ) = 0. Conversely, if Γ(U, φ) = 0 for all U, then take U := M
and m := idM ∈Γ(U, M). We obtain φ = Γ(U, φ)(m) = 0.
(2) First assume φ is a monomorphism. Take an arbitrary object U and a section
m ∈Γ(U, M). So m : U →M is a morphism in M. If φ ◦m = 0, then, by the
deﬁnition of a monomorphism, we must have m = 0. Thus Γ(U, φ) is injective.
Conversely, assume that Γ(U, φ) is injective for every U. Take U := Ker(φ) and
let m : U →M be the inclusion. Then Γ(U, φ)(m) = φ ◦m = 0. But then m = 0
and U = 0. Thus φ is a monomorphism.
(3) First assume φ is an epimorphism. Consider a section n ∈Γ(U, N). So we have
morphisms φ : M ↠N and n : U →N. Let V := M ×N U, the ﬁbered product.
By Lemma 2.4.3(2) the projection ρ : V →U is an epimorphism, i.e. a covering in
40
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
our terminology. Now the other projection m : V →M satisﬁes φ◦m = n◦ρ. This
means that φ(m) = n in Γ(V, N).
Conversely, let us take U := N and n := idN ∈Γ(U, N).
There exists an
epimorphism ρ : V ↠U and a morphism m : V →M such that φ ◦m = n ◦ρ = ρ.
We see that φ ◦m is an epimorphism, and hence φ is an epimorphism.
□
Example 2.4.10. Suppose
S =
 0 →M ′
φ−→M
ψ−→M ′′ →0

is a sequence in M. Here is how exactness of S is tested using the ﬁrst sheaf trick.
By item (1) of the ﬁrst sheaf trick, the condition ψ◦φ = 0 is same as Γ(U, ψ◦φ) =
0 for every U ∈M.
Exactness at M ′ is the same as this condition: for every U ∈M and every section
m′ ∈Γ(U, M ′), if φ(m′) = 0 then m′ = 0. This is by item (2).
Exactness at M ′′ is the same as this condition: for every U ∈M and every
section m′′ ∈Γ(U, M ′′), there exists a covering V ↠U and a section m ∈Γ(V, M),
such that ψ(m) = m′′ in Γ(V, M ′′).
Finally, exactness at M is the same as this condition (given that ψ ◦φ = 0): for
every U ∈M and every section m ∈Γ(U, M) such that ψ(m) = 0, there exists a
covering V ↠U and a section m′ ∈Γ(V, M ′), such that φ(m′) = m in Γ(V, M ′′).
Proposition 2.4.11 (Second Sheaf Trick). Let M be an object in an abelian cat-
egory M. Suppose ρ1 : V1 →U and ρ2 : V2 →U are morphisms in M, such that
(ρ1, ρ2) : V1 ⊕V2 →U is an epimorphism. Let W := V1 ×U V2, with projection
morphisms σ1 : W →V1 and σ2 : W →V2. Then the sequence
0 →Γ(U, M)
(ρ∗
1,ρ∗
2)
−−−−→Γ(V1, M) × Γ(V2, M)
(σ∗
1,−σ∗
2)
−−−−−−→Γ(W, M)
in Mod K is exact.
Proof. Note that V1 × V2 = V1 ⊕V2. By Lemma 2.4.3(1) there is an exact sequence
0 →W
(σ1,−σ2)
−−−−−−→V1 ⊕V2
(ρ1,ρ2)
−−−−→U →0
in M. By Proposition 2.3.27(2) we get an exact sequence
0 →Γ(U, M)
(ρ∗
1,ρ∗
2)
−−−−→Γ(V1 ⊕V2, M)
(σ1,−σ2)∗
−−−−−−→Γ(W, M)
in Ab. But
Γ(V1 ⊕V2, M) ∼= Γ(V1, M) × Γ(V2, M).
□
Remark 2.4.12. As can be seen in the practical application of our sheaf tricks
(e.g. in the proofs of Proposition 2.5.18 and Theorem 3.7.10) these tricks reduce
proofs about an abstract abelian category M, to proofs that are just like in the
concrete case of the abelian category M = Ab X of sheaves of abelian groups on a
topological space X. This is not as easy as the case M = Mod A of modules over a
ring A, that the Freyd-Mitchell Theorem permits, but – at least for someone with
experience in algebraic geometry – our method is quite straightforward.
Our sheaf tricks are inspired by [144, tag 05PL]. There it is shown that the
geometric allegory is genuine, except that instead of a topological space X, there is
a site X (in the sense of Grothendieck). The underlying category of the site X is
the abelian category M itself, and the coverings of X are the epimorphisms in M.
It is proved in [144] that the category M embeds as a full abelian subcategory of
Ab X, the category of sheaves of abelian groups on X.
Proposition 2.4.9 is very similar to [102, Theorem VIII.3], where what we call
“sections” are called “members”. But S. MacLane’s method loses the abelian group
structure (the members are not elements of abelian groups). An improvement of
MacLane’s method can be found in an unpublished note of G. Bergman [18].
41
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
