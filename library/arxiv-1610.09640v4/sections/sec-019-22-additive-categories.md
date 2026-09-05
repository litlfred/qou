---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-019-22-additive-categories
section_title: "Additive Categories"
section_number: 2.2
pages: 33-38
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
Deﬁnition 2.2.1.An additive categoryis a linear categoryM satisfying these two
conditions:
(i) M has a zero object0.
(ii) M has ﬁnite coproducts.
ThismaterialwillbepublishedbyCambridgeUniversityPressas Derived CategoriesbyAmnon
Yekutieli. This prepublication version is free to view and download for personal use only. Not for
redistribution, resale or use in derivative works.c© Amnon Yekutieli, 2019.
33
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Observe that HomM(M,N )⁄= ∅ for everyM,N ∈M, since this is an abelian
group. For the zero object0∈M we have HomM(M, 0) = Hom M(0,M ) = 0, the
zero abelian group. We denote the unique arrows0→M and M→0 also by 0.
So the numeral0 has a lot of meanings; but they are always (hopefully) clear from
the context. The coproduct in a linear categoryM is usually denoted by⨁, and is
called thedirect sum; cf. Example 1.4.2.
Example 2.2.2. Let A be a centralK-ring. The category ModA is aK-linear
additive category. The full subcategory F⊆ModA on the free modules is also
additive.
Proposition 2.2.3. Let M be a linear category. Let{Mi}i∈I be a ﬁnite collection
of objects of M, and assume the coproductM =⨁
i∈IMi exists, with embeddings
ei :Mi→M.
(1) For eachi letpi :M→Mi be the unique morphism such thatpi◦ei = idMi,
and pi◦ej = 0 for j⁄=i. Then (M,{pi}i∈I) is a product of the collection
{Mi}i∈I.
(2) ∑
i∈Iei◦pi = idM.
Exercise 2.2.4. Prove this proposition.
Part (1) of Proposition 2.2.3 directly implies:
Corollary 2.2.5. An additive category has ﬁnite products.
Deﬁnition 2.2.6.Let M be an additive category, and letN be a full subcategory
of M. We say thatN is afull additive subcategoryof M if N contains the zero object,
and is closed under ﬁnite direct sums.
Exercise 2.2.7. In the situation of Deﬁnition 2.2.6, show that the categoryN is
itself additive.
Example 2.2.8. Consider the linear categoryM from Example 2.1.4, built from a
ring A. It does not have a zero object (unless the ringA is the zero ring), so it is
not additive.
A more puzzling question is this: DoesM have ﬁnite direct sums? This turns
out to be equivalent to whether or notA∼= A⊕A as rightA-modules. One can
show that whenA is nonzero and commutative, or nonzero and noetherian, then
A⁄∼=A⊕A in ModAop. On the other hand, if we take a ﬁeldK, and a countable
rankK-module N, thenA := EndK(N) will satisfyA∼=A⊕A.
Proposition 2.2.9. Let M be a linear category, andN∈M. The following condi-
tions are equivalent:
(i) The ring EndM(N) is trivial.
(ii) N is a zero object ofM.
Proof.
(ii)⇒(i): Since the setEndM(N) is a singleton, it must be the trivial ring.
(i)⇒(ii): If the ring EndM(N) is trivial, then all left and right modules over it
must be trivial. Now use Proposition 2.1.2(2). □
2.3. Abelian Categories.
Deﬁnition 2.3.1.Let M be an additive category, and let f : M →N be a
morphism in M. A kernel of f is a pair(K,k ), consisting of an objectK∈M and
a morphismk :K→M, with these two properties:
(i) f◦k = 0.
(ii) If k′: K′→M is a morphism inM such thatf◦k′= 0, then there is a
unique morphismg :K′→K such thatk′=k◦g.
34
Derived Categories | Amnon Yekutieli | 14 Apr 2019
In other words, the objectK represents the functorMop→Ab,
K′↦→{k′∈HomM(K′,M )|f◦k′= 0}.
The kernel off is of course unique up to a unique isomorphism (if it exists), and we
denote if byKer(f). Sometimes Ker(f) refers only to the objectK, and other times
it refers only to the morphismk; as usual, this should be clear from the context.
Deﬁnition 2.3.2.Let M be an additive category, and let f : M →N be a
morphism in M. Acokernel off is a pair(C,c ), consisting of an objectC∈M and
a morphismc :N→C, with these two properties:
(i) c◦f = 0.
(ii) If c′: N →C′is a morphism in M such thatc′◦f = 0, then there is a
unique morphismg :C→C′such thatc′=g◦c.
In other words, the objectC corepresents the functorM→Ab,
C′↦→{c′∈HomM(N,C′)|c′◦f = 0}.
The cokernel off is of course unique up to a unique isomorphism (if it exists), and
we denote if byCoker(f). Sometimes Coker(f) refers only to the objectC, and
other times it refers only to the morphismc; as usual, this should be clear from the
context.
Example 2.3.3. In ModA all kernels and cokernels exist. Givenf :M→N, the
kernel isk :K→M, whereK :={m∈M|f(m) = 0}, and thek is the inclusion.
The cokernel isc :N→C, whereC :=N/f(M), andc is the canonical projection.
Proposition 2.3.4. Let M be an additive category, and letf : M →N be a
morphism in M.
(1) If k :K→M is a kernel off, thenk is a monomorphism.
(2) If c :N→C is a cokernel off, thenc is an epimorphism.
Exercise 2.3.5. Prove the proposition.
Deﬁnition 2.3.6.Assume the additive categoryM has kernels and cokernels. Let
f :M→N be a morphism inM.
(1) Deﬁne theimage of f to be Im(f) := Ker(Coker(f)).
(2) Deﬁne thecoimage of f to be Coim(f) := Coker(Ker(f)).
The image is familiar, but the coimage is probably not. The next diagram should
help. We start with a morphismf : M→N in M. The kernel and cokernel off
ﬁt into this diagram:K
k
− →M
f
− →N
c
− →C. Insertingα:= Coker(k) = Coim(f) and
β:= Ker(c) = Im(f) we get the following commutative diagram (solid arrows):
(2.3.7) K k //
0 ##
M
f //
α

γ
##
N c //C
M′
f′
//N′
0
;;
β
OO
Sincec◦f = 0 there is a unique morphismγ(the dashed arrow) making the diagram
commutative. Nowβ◦γ◦k =f◦k = 0; andβis a monomorphism; soγ◦k = 0.
Hence there is a unique morphismf′:M′→N′making the diagram commutative.
We conclude thatf :M→N induces a morphism
(2.3.8) f′: Coim(f)→Im(f).
Deﬁnition 2.3.9.An abelian categoryis an additive categoryM with these two
extra properties:
(i) All morphisms inM admit kernels and cokernels.
35
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(ii) For every morphismf :M→N in M, the induced morphismf′in equation
(2.3.8) is an isomorphism.
Here is a less precise but (maybe) easier to remember way to state property (ii).
Because M′= Coker(Ker(f)) and N′= Ker(Coker(f)), we see that
(2.3.10) Coker(Ker(f)) = Ker(Coker(f)).
From now on we forget all about the coimage.
Exercise 2.3.11. For any ringA, prove that the categoryModA is abelian.
This includes the categoryAb = ModZ, from which the name derives.
Deﬁnition 2.3.12.Let M be an abelian category, and letN be a full subcategory
of M. We say thatN is afull abelian subcategoryof M if the zero object belongs to
N, and N is closed inM under taking ﬁnite direct sums, kernels and cokernels.
Exercise 2.3.13. In the situation of Deﬁnition 2.3.12, show that the categoryN
is itself abelian.
Example 2.3.14. Let M1 be the category of ﬁnitely generated abelian groups,
and let M0 be the category of ﬁnite abelian groups. Then M1 is a full abelian
subcategory of Ab, and M0 is a full abelian subcategory ofM1.
Exercise 2.3.15.Let N be the full subcategory ofAb whose objects are the ﬁnitely
generated free abelian groups. It is an additive subcategory ofAb (since it is closed
under direct sums).
(1) Show that N is closed under kernels inAb.
(2) Show that N is not closed under cokernels inAb, so it is not a full abelian
subcategory of Ab.
(3) Show that N has cokernels (not the same as those ofAb). Still, it fails to
be an abelian category.
Exercise 2.3.16.The categoryGrp is not linear of course. Still, it does have a zero
object (the trivial group). Show thatGrp has kernels and cokernels, but condition
(ii) of Deﬁnition 2.3.9 fails.
Exercise2.3.17. Let HilbbethecategoryofHilbertspacesover C. Themorphisms
are the continuousC-linear homomorphisms. Show thatHilb is aC-linear additive
category with kernels and cokernels, but it is not an abelian category.
Exercise 2.3.18. Let A be a ring. Show thatA is left noetherianiﬀ the category
ModfA of ﬁnitely generated left modules is a full abelian subcategory ofModA.
Example 2.3.19. Let (X,A) be a ringed space; namelyX is a topological space
andA is a sheaf of rings onX. There is a very detailed discussion of sheaves of
modules in [63, Section II.1] and [75, Sections 2.1-2.2]. Let us mention only one
aspect of it.
We denote byModprA the category ofpresheavesof leftA-modules onX. This
is an abelian category. Given a morphismφ:M→Nin ModprA, its kernel is the
presheaf Kerpr(φ) deﬁned by
Γ
(
U, Kerpr(φ)
{
:= Ker
(
φ: Γ(U,M)→Γ(U,N )
{
on every open setU⊆X. The cokernel ofφis the presheafCokerpr(φ) deﬁned by
Γ
(
U, Cokerpr(φ)
{
: Coker
(
φ: Γ(U,M)→Γ(U,N )
{
.
Now let ModA be the full subcategory ofModprA consisting ofsheaves. It is a
full additive subcategory ofModprA, closed under kernels. However,ModA is not
closed under cokernels insideModprA, and hence it is not a full abelian subcategory.
36
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Nonetheless, ModA is itself an abelian category, but with diﬀerent cokernels.
Given a morphism φ: M → Nin ModA, its cokernel in ModA is the sheaf
Coker(φ) that’s associated to the presheafCokerpr(φ).
Proposition 2.3.20. Let M be a linear category.
(1) The opposite categoryMop has a canonical structure of a linear category.
(2) If M is additive, thenMop is also additive.
(3) If M is abelian, thenMop is also abelian.
Proof. (1) Since HomMop(M,N ) = Hom M(N,M ), this is an abelian group. The
bilinearity of the composition inMop is clear.
(2) The zero objects inM and Mop are the same. Existence of ﬁnite coproducts in
Mop is because of existence of ﬁnite products inM; see Proposition 2.2.3(1).
(3) Mop has kernels and cokernels, since KerMop(Op(φ)) = Coker M(φ) and vice
versa. Also the symmetric condition (ii) of Deﬁnition 2.3.9 holds. □
Proposition 2.3.21. Letφ:M→N be a morphism in an abelian categoryM.
(1) φis a monomorphism if and only ifKer(φ) = 0.
(2) φis an epimorphism if and only ifCoker(φ) = 0.
(3) φis an isomorphism if and only if it is both a monomorphism and an
epimorphism.
Exercise 2.3.22. Prove this proposition.
Consider a diagram
(2.3.23) S =
(
···M−1
φ−1
−−→M0
φ0
−→M1
φ1
−→M2···
{
in an abelian category M, extending ﬁnitely or inﬁnitely to either side. Such a
diagram is called asequence in M. An objectMi appearing inS is calledinterior
in S if there is an objectMi−1 appearing to the left of it, and an objectMi+1
appearing to the right of it.
Deﬁnition 2.3.24.LetS be a sequence in the abelian categoryM, with notation
as in (2.3.23).
(1) Suppose Mi is an interior object inS. We say that the sequenceS is exact
at Mi if Im(φi−1) = Ker(φi), as subobjects ofMi.
(2) The sequenceS is said to beexact if it is exact at all of its interior objects.
Example 2.3.25.A morphismφ:M→N in an abelian categoryMis a monomor-
phism iﬀ0→M
φ
− →N is an exact sequence. The morphismφis an epimorphism
iﬀ the sequenceM
φ
− →N→0 is exact.
Deﬁnition 2.3.26.A short exact sequencein an abelian category M is as exact
sequence of the form
S =
(
0→M0
φ0
−→M1
φ1
−→M2→0
{
.
Proposition 2.3.27. Let M be aK-linear abelian category.
(1) Let 0→M′φ
− →M
ψ
− →M′′be an exact sequence inM. Then for every
L∈M the sequence
0→HomM(L,M′)
Hom(id,φ)
−−−−−−→HomM(L,M )
Hom(id,ψ)
− −−−−−− →HomM(L,M′′)
in ModK is exact.
37
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(2) Let M′φ
− →M
ψ
− →M′′→0 be an exact sequence inM. Then for every
N∈M the sequence
0→HomM(M′′,N )
Hom(ψ,id)
− −−−−−− →HomM(M,N )
Hom(φ,id)
−−−−−−→HomM(M′,N )
in ModK is exact.
Exercise 2.3.28. Prove Proposition 2.3.27. (Hint: use the deﬁnitions of kernel,
cokernel and image.)
