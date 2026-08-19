---
doc_id: arxiv-1409.2799v2
doc_title: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES AT ROOTS OF UNITY"
section_id: sec-008-35-the-tilting-category-t-and-its-graded-counter
section_title: "The tilting category T and its graded counterpart Tgr"
section_number: 3.5
pages: 27-31
source_pdf: 1409.2799v2.pdf
source_sha256: 2f2067b7b583e731
doc_brief: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES AT ROOTS OF UNITY — We give a diagrammatic presentation of the category of Uq(sl2)-tilting modules T for q being a root of unity and introduce a grading on"
---
consequences of Theorems 3.11 and 3.12 with respect to the question how the path length grading
l(·) (see Deﬁnition 3.1) of Khovanov-Seidel’s ∞-quiver algebra relates to the tilting category T.
We point out that this is non-trivial since Theorems 3.11 and 3.12 only say that Tλ(≤ m) and Tλ
are isomorphic to subcategories of pMod-Qm and pMod-Q∞.
Recall that, for every graded algebraA, there is aforgetful functor forget : Modgr-A → Mod-A
that forgets the grading. Using this functor, we say that an A-module M ∈ Ob(Mod-A) is grad-
able if there exists an A-module ˜M ∈ Ob(Modgr-A) such that forget( ˜M ) = M. Note that, by
abuse of notation, we usually do not distinguish between ˜M and M.
Recall that HomMod-A(M, M ′) consists of all (right) A-module homomorphisms f : M → M ′
and HomModgr-A( ˜M , ˜M ′) consists of (right) A-module homomorphisms ˜f : ˜M → ˜M ′ as in (13).
Hence, in the same vein as above, we can call anA-module homomorphism f : M → M ′ gradable,
if there exists ˜f : ˜M → ˜M ′ such that forget( ˜f ) = f. Consequently, we deﬁne the following.
Deﬁnition 3.18. We call a (left) Uq-tilting module M ∈ Ob(T) gradable, if T∞(M) is grad-
able viewed as a (right) Q∞-module. We call a Uq-intertwiner f : M → M ′ ∈ HomT(M, M ′)
gradable, if T∞(f ) : T∞(M) → T∞(M ′) is a gradable Q∞-module homomorphism.
We denote by Tgr the subcategory of T consisting of gradable Uq-tilting modules and gradable
Uq-intertwiners. We use similar notations and conventions for ≤ m and for ﬁxed λ or µ. ▲
The question concerning which objects M ∈ Ob(T) are gradable turns out to be surprisingly
simple in our case. We note that, with respect to the rather co mplicated situation for graded cate-
gory Op
0 discussed in e.g. [57, Theorem 4.1], the following proposition is quite remarkable.
Proposition 3.19. All objects M ∈ Ob(Tλ(≤ m)), M ∈ Ob(Tλ) and M ∈ Ob(T) are gradable.
The grading of each indecomposable module Tq(i) is unique up to shifts. □
Proof. We only prove the ∞ case and leave the other case to the reader. We start by consid ering
λ ∈ A 0 and discuss the semisimple case on the walls afterwards.
It is easy to check that, for any graded algebra A and any two gradable A-modules M and M ′,
the direct sum M ⊕ M ′ is also gradable. Thus, by Lemma 2.18 part (a), it is enough to consider
only the Tq(i)’s. As in the proof of the part (b) of Theorem 3.12 (or Theorem 3 .11 in the ﬁnite
case) we see that T∞(Tq(i)) ∼= iP . As discussed in Subsection 3.2, the iP can be given a grading
coming from the path length l(·). Thus, all the Tq(i)’s are gradable.
On the walls: Since this is the semisimple case by Lemma 2.26, we can just assign to any
simple T∞(Tq(µi)) a degree by demanding that all elements of T∞(Tq(µi)) are concentrated in
this particular degree. Thus, all Tq(µi) are gradable and concentrated in (up to shifts) degree zero.
The uniqueness (up to shifts) can be proven as in [7, Lemma 2.5.3]. ■
Corollary 3.20. We have isomorphisms of ungraded categories Tλ(≤ m) ∼=iso Tgr(≤ m) and
T ∼=iso Tgr. That is, also all morphisms are gradable and the gradings are unique up to a shift. □
Proof. As before, for any two gradable A-homomorphisms f and f ′, the direct sum f ⊕ f ′ is
also gradable. Thus, by Lemma 2.18 part (a) again together wi th Proposition 3.19, it is enough to
consider only HomUq(Tq(i), Tq(i′)). By Corollary 2.31 we see that this space has a basis consisting
of a subset of i, ui, di and εi (in the non-semisimple case) who are all gradable by Proposition 3.10.
The semisimple case and the uniqueness of the grading follow as above. This gives rise to an
isomorphism after collapsing the grading of Tgr (since each object M of T corresponds to objects
of Tgr of the form M⟨s⟩ for s ∈ Z). ■
27
Using Corollary 3.20 and abuse of language, we do not distinguish between Uq-tilting modules
or their graded versions. Moreover, as a consequence of Coro llary 3.20, we can choose a stan-
dard grading (since it will be unique up to shifts) by demanding that simpl e Uq-tilting modules
are concentrated in degree zero and proceed inductively alo ng the quiver. Note that, by Proposi-
tions 2.7 and 2.20 and Corollary 2.8, this gives inductively a graded lift of Lq(i), ∆ q(i) and ∇q(i)
as well. This choice gives rise to the following graded reﬁne ments of Propositions 2.7 and 2.20
and Corollary 2.8.
Proposition 3.21. Suppose i = al + b for some a, b ∈ Z≥0 with b ≤ l − 2. Set i′ = (a + 2)l − b − 2.
Then there exist short exact sequences
0 − →Lq(i)⟨+1⟩֒− →∆ q(i′) −։ Lq(i′) − →0, 0 − →Lq(i′)֒− → ∇q(i′) −։ Lq(i)⟨−1⟩ − →0,
0 − →∆ q(i′)֒− →Tq(i′) −։ ∆ q(i)⟨−1⟩ − →0, 0 − → ∇q(i)⟨+1⟩֒− →Tq(i′) −։ ∇q(i′) − →0.
Moreover, all involved morphisms are degree preserving. □
Proof. This follows from our choice for the grading convention and the degree (under the equiva-
lence in Theorems 3.11 and 3.12) of the morphisms in HomUq (Tq(i), Tq(i′)). To be more precise,
we know that the Tq(i)’s will be, under the functor T∞, mapped to iP . Then for example, as
explained in Proposition 2.30, the unique morphism
Tq(i) ։ ∇q(i)֒→Tq(i + 1 ) ↭ •
i+1
•
i
ui/d111/d111
is of degree 1. By our convention we see that moving to the left along the KS ∞-quiver always
increases the degree (starting in degree zero for the ﬁrst simple module). Thus,
0 − → ∇q(i)⟨+1⟩֒− →Tq(i′) −։ ∇q(i′) − →0.
All other cases follow similarly and are left to the reader. Note again that moving to the left along
the KS ∞-quiver always increases the degree, but, by duality, moving right decreases it. ■
Remark 3.22. As we already mentioned in Remark 3.17 the grading induced on T comes from
an Euler characteristic on a certain cobordism category associated to Khovanov’s arc algebraH m.
Thus, this is a “natural” grading from the viewpoint of topology.
As we mentioned above, we think that this should generalize i n type A. The degree will there
be given by an Euler characteristic on a certain “foam” category associated to the sln-web algebras
which generalize Khovanov’s arc algebra. See for example [38], [44], [48] or [60]. Or alternatively,
by a grading coming from certain cyclotomic KL-R algebras in the sense of [33] or [50]. ▲
We conclude this section by lifting the translation onto T µ
λ , the translation out of T λ
µ and the
translation through the wallΘ s and Θ t to their graded versions (we use the same notation for these).
To understand our notation, recall that a category ˜C is called a graded category, if there exists a
functor deg : ˜C → Z where we consider Z as a category Z with Ob(Z) = {•} and EndZ(•) = Z.
In addition, there is a Z-action ⟨s⟩ on the objects O ∈ Ob( ˜C), called shift by s ∈ Z, such that
a given morphism f ∈ Hom ˜C(O, O′) of degree d is of degree d + s′ − s in Hom ˜C(O⟨s⟩, O′⟨s′⟩)
(said otherwise, every morphism in ˜C has a degree which behaves additively under composition
and objects can be shifted via ⟨s⟩). Moreover, denote by C the ungraded version. We say a functor
F : C → D is gradable if there exists a lift ˜F : ˜C → ˜D such that forget ◦ ˜F = F ◦ forget. We say
28
that ˜F and ˜F ′ are the same up to a shift s ∈ Z if there is a natural isomorphism 10 between ˜F and
˜F ′⟨s⟩. As before, we are usually very careless with our distinction of ˜F and F.
Corollary 3.23. The functors T µ,i
λ , T λ,i
µ , T µ
λ , T λ
µ ∈ Ob(pEnd(T(≤ m))) are gradable (same in
the inﬁnite case). Moreover, any two lifts of T µ,i
λ , T λ,i
µ are the same up to shifts. □
Proof. This follows by Remark 3.13 and the fact that U t
i and U i
t are graded functors (similarly in
the ∞ case). The statement for T µ
λ and T λ
µ follows now by (9), since clearly sums of gradable,
additive functors in an additive category are gradable. For the inﬁnite case note that any sum
(ﬁnite or not) of gradable functors is gradable and the claim follows from (9) and the ﬁnite case.
The uniqueness up to shifts can again be veriﬁed as in [7, Lemm a 2.5.3], since T µ,i
λ and T λ,i
µ are
indecomposable by Proposition 2.39. ■
Corollary 3.24. The functors Θ λ,i
s , Θ λ,i
t , Θ λ
s , Θ λ
t ∈ Ob(pEnd(Tλ(≤ m))) are gradable (same in
the inﬁnite case). Moreover, any two lifts of Θ λ,i
s or t are the same up to a shift. □
Proof. We can use Corollary 3.23 since all functors involved can be o btained via sums and com-
positions of the functors T µ
λ,i and T λ,i
µ . The inﬁnite case follows as above, but using (8) instead
of (9). By Proposition 2.38 the functors Θ λ,i
s or t are indecomposable and the uniqueness up to shifts
follows as before. ■
We choose the graded versions of T µ,i
λ and out of T λ,i
µ in the evident way as induced by the
gradings on U t
i or U i
t . We get the following reﬁnement of Proposition 2.34.
Corollary 3.25. In the graded category Tgr we have for all i ∈ Z≥0 the following.
(a) The functors T µ
λ and T λ
µ are well-deﬁned (their deﬁnition gives gradable Uq-tilting mod-
ules in the right blocks), (up to shifts) adjoints (left and right) and exact. Thus, Θ λ
s and Θ λ
t
are exact and graded self-adjoint.
(b) We have (recalling that Lq(µi) ∼
= Tq(µi))
T µ
λ (Tq(λi)) ∼=
{
Tq(µi−1)⟨+1⟩ ⊕ Tq(µi+1)⟨+1⟩, if µi > λ i,
Tq(µi) ⊕ Tq(µi)⟨+2⟩, if µi < λ i,
T λ
µ (Tq(µi)) ∼=
{
Tq(λi+1)⟨−1⟩, if µi > λ i,
Tq(λi)⟨−1⟩, if µi < λ i.
(c) The dead-end relations Θ λ
s (Tq(λ0)) ∼= 0, Θ λ
s (Tq(λ1)) ∼= Tq(λ2) and Θ λ
t (Tq(λ0)) ∼= Tq(λ1).
Moreover, we have
Θ λ
s or t(Tq(λi)) ∼=
{
Tq(λi−1) ⊕ Tq(λi+1), if i > 1 is odd for s and even for t,
Tq(λi)⟨−1⟩ ⊕ Tq(λi)⟨+1⟩, if i > 0 is odd for t and even for s.
Here we set Tq(−1) = Tq(λ−1) = Tq(µ−1) = 0 . □
Proof. This follows directly from Theorem 3.12 parts (d), (f) and (g ) together with (14) and the
discussion in Subsection 3.3, for example Lemma 3.8. ■
10In the 2-category where objects are graded categories, where morphisms are graded functors between these cate-
gories and where 2-morphisms are graded natural transformations.
29
Proposition 3.26. All functors in pEnd(T) are gradable. Moreover, the grading is unique up to
shifts on the indecomposable projective functors. Similar for pEnd(Tλ). □
Proof. The uniqueness, up to shifts, of the grading on the indecomposable factors can be proven as
before. By the Krull-Schmidt property of pEnd(T) (see Lemma 2.37) and the fact that any direct
sum of gradable, additive functors in an additive category i s gradable, it sufﬁces to show that in-
decomposable projective functors are gradable. By Lemma 2.38 these are given by tensoring with
a Tq(i) for some i ∈ Z≥0. By Proposition 3.19 all objects of T are gradable and, by Lemma 2.18
part (b), the categoryT is preserved by ﬁnite tensor products. Thus, the indecomposable projective
functors are gradable. For pEnd(Tλ) this follows from Corollary 3.24. ■
Proposition 3.26 motivates the deﬁnition ofpEnd(Tgr
λ ) which can be deﬁned in the spirit of (13)
(thus, using graded hom-spaces of natural transformations). This is the same as saying that the
category pEnd(Tgr
λ ) is graded in the above sense.
In order to state the proposition, we write T∞F (Tq(∞ )) short for ⨁
i T∞F (Tq(i)). This is an
Q∞-bimodule via pre-composition (right) and post-composition (left) with F (·) or F (′)(·).
Moreover, recall that the superscript fs indicates that we are only considering ﬁnitely supported
homomorphisms. We have the following (similar of course for pEnd(Tgr
λ (≤ m))).
Proposition 3.27. Let F , F ′ be two functors in pEnd(Tgr
λ ). Then there exists an isomorphism of
graded Q(q)-vector spaces
Homfs
pEnd(Tgr
λ )(F , F ′) ∼= Homfs
Q∞-pModgr-Q∞(T∞F (Tq(∞ )), T∞F ′(Tq(∞ ))).
This is an isomorphism of graded rings if F = F ′. □
Proof. It sufﬁces to verify the statement for the translation onto T µ
λ , out of T λ
µ and the through the
wall functors Θ λ
s or t. By Theorem 3.12 part (d), (f) and (g) it sufﬁces to show the st atement for the
corresponding U’s.
Without loss of generality, we only discuss the “even” case,that is, U t
even, U even
t and U ∞
even which
correspond to T −1
λ , T λ
−1 and Θ λ
s respectively. Thus, by additivity, it sufﬁces to show the statement
for U t
i , U i
t and Ui for i > 0 even. Fix i and assume that i ≪ m. Recall that Khovanov and Seidel
have shown in [36, Proposition 2.9] that pMod-Qm and Op
0 for slm+1 and parabolic p of type
S1 × Sm−1 are equivalent. Moreover, as they explain below [36, Propos ition 2.9], U t
i , U i
t and Ui
correspond to the translation onto, out off and through the i-th wall functors.
Note now that the same holds for the graded version ofOp
0 introduced in [57] as Stroppel explains
in [58, Section 1]. Thus, we can use [58, Theorem 1.12] to ﬁnis h the proof in the “cut-off case”.
Taking the inductive limit now shows the statement. ■
Corollary 3.28. There is an isomorphism of graded rings
Endfs
gr(id) ∼= Z(Q∞),
where id is the identity functor on Tgr
λ , Z(Q∞) is the center of Q∞ and the endomorphism ring is
to be taken in pEnd(Tgr
λ ). □
Proof. From Proposition 3.10 combined with Proposition 3.27. Notethat we get the centerZ(Q∞)
and not Q∞ itself because the endomorphism ring from Proposition 3.10 is as Uq-intertwiners
while the one induced from Proposition 3.27 is as Q∞-pModgr-Q∞-bimodule intertwiners. ■
30
Remark 3.29. It is known that the split Grothendieck groupK ⊕
0 (·) = K ⊕
0 (·)⊗Z[v,v−1]Q(q) (viewed
as a module over Z[v, v−1] where the formal parameter v comes for the grading) of pModgr-Qm
categoriﬁes the Burau representation Bm+1 of the m + 1-strand braid group Bm+1 (the action of
Bm+1 is induced via functors constructed from Ui), see [36, Proposition 2.8 and Subsection 2.d].
Using Theorem 3.11, we see that the same is true for Tgr
λ (≤ m), that is K ⊕
0 (Tgr
λ (≤ m)) ∼
= Bm+1
as Bm+1-modules. Note now that the limit therefore categoriﬁes the corresponding ∞ version of
the Burau representation of the braid group B∞ with ∞-many strands. ▲
Remark 3.30. Fix slm+1 and denote by pi the parabolic for Si × Sm−i. Moreover, we denote
by Op
max = ⨁ m
i=0 Opi
0 the direct sum. We note that, as Bernstein-Frenkel-Khovano v conjectured
in [8, Conjectures 1-4] and Stroppel proved in [56], parabol ic category Op
max for slm+1 (compare
to Remark 3.16) can be used to categorify the m + 1-strand Temperley-Lieb algebra T Lv
m+1. The
split Grothendieck group K ⊕
0 of the category of projective endofunctors on Op
max gives11 T Lv
m+1.
The Grothendieck group behaves additive, i.e.
T Lv
m+1 ∼
= K ⊕
0 (pEnd(Op
max)) ∼=
m⨁
i=0
K ⊕
0 (pEnd(Op
i )).
Thus, pEnd(Op
1) gives a summand
T L
v
m+1 of T Lv
m+1 that corresponds to the “next to highest
weight” summand of V ⊗m (with notation as in Remark 3.17), see [16, Section 6].
Thus, as explained in Remark 3.16, by Proposition 3.27, the same is true for pEnd(Tgr
λ (≤ m)).
Moreover, it is easy to see that the embedding of categories
pEnd(Tgr
λ (≤ m))֒→pEnd(Tgr
λ (≤ m + 1 ))
gives rise to an embedding
T L
v
m+1 ∼= K ⊕
0 (pEnd(Tgr
λ (≤ m)))֒→K ⊕
0 (pEnd(Tgr
λ (≤ m + 1 ))) ∼=
T L
v
m+2.
Thus, by Proposition 3.10, pEnd(Tgr
λ ) governs all of them at once. ▲
4. D IAGRAMS FOR THE GRADED TILTING CATEGORY Tgr
In this section we give the diagrammatic presentation of the (graded) tilting category Tgr
λ and
the category of its projective endofunctors pEnd(Tgr
λ ).
