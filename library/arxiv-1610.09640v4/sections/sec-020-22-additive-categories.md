---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories Amnon Yekutieli 14 Apr 2019 DERIVED CATEGORIES"
section_id: sec-020-22-additive-categories
section_title: "Additive Categories"
section_number: 2.2
pages: 33-38
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories Amnon Yekutieli 14 Apr 2019 DERIVED CATEGORIES — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge"
---
Deﬁnition 2.2.1. An additive category is a linear category M satisfying these two
conditions:
(i) M has a zero object 0.
(ii) M has ﬁnite coproducts.
This material will be published by Cambridge University Press as Derived Categories by Amnon
Yekutieli. This prepublication version is free to view and download for personal use only. Not for
redistribution, resale or use in derivative works. c⃝Amnon Yekutieli, 2019.
33
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Observe that HomM(M, N)̸ = ∅for every M, N ∈M, since this is an abelian
group. For the zero object 0 ∈M we have HomM(M, 0) = HomM(0, M) = 0, the
zero abelian group. We denote the unique arrows 0 →M and M →0 also by 0.
So the numeral 0 has a lot of meanings; but they are always (hopefully) clear from
the context. The coproduct in a linear category M is usually denoted by L, and is
called the direct sum; cf. Example 1.4.2.
Example 2.2.2. Let A be a central K-ring. The category Mod A is a K-linear
additive category. The full subcategory F ⊆Mod A on the free modules is also
additive.
Proposition 2.2.3. Let M be a linear category. Let {Mi}i∈I be a ﬁnite collection
of objects of M, and assume the coproduct M = L
i∈I Mi exists, with embeddings
ei : Mi →M.
(1) For each i let pi : M →Mi be the unique morphism such that pi◦ei = idMi,
and pi ◦ej = 0 for j̸ = i. Then (M, {pi}i∈I) is a product of the collection
{Mi}i∈I.
(2) P
i∈I ei ◦pi = idM.
Exercise 2.2.4. Prove this proposition.
Part (1) of Proposition 2.2.3 directly implies:
Corollary 2.2.5. An additive category has ﬁnite products.
Deﬁnition 2.2.6. Let M be an additive category, and let N be a full subcategory
of M. We say that N is a full additive subcategory of M if N contains the zero object,
and is closed under ﬁnite direct sums.
Exercise 2.2.7. In the situation of Deﬁnition 2.2.6, show that the category N is
itself additive.
Example 2.2.8. Consider the linear category M from Example 2.1.4, built from a
ring A. It does not have a zero object (unless the ring A is the zero ring), so it is
not additive.
A more puzzling question is this: Does M have ﬁnite direct sums? This turns
out to be equivalent to whether or not A ∼= A ⊕A as right A-modules. One can
show that when A is nonzero and commutative, or nonzero and noetherian, then
A̸ ∼= A ⊕A in Mod Aop. On the other hand, if we take a ﬁeld K, and a countable
rank K-module N, then A := EndK(N) will satisfy A ∼= A ⊕A.
Proposition 2.2.9. Let M be a linear category, and N ∈M. The following condi-
tions are equivalent:
(i) The ring EndM(N) is trivial.
(ii) N is a zero object of M.
Proof.
(ii) ⇒(i): Since the set EndM(N) is a singleton, it must be the trivial ring.
(i) ⇒(ii): If the ring EndM(N) is trivial, then all left and right modules over it
must be trivial. Now use Proposition 2.1.2(2).
□
2.3. Abelian Categories.
Deﬁnition 2.3.1. Let M be an additive category, and let f : M →N be a
morphism in M. A kernel of f is a pair (K, k), consisting of an object K ∈M and
a morphism k : K →M, with these two properties:
(i) f ◦k = 0.
(ii) If k′ : K′ →M is a morphism in M such that f ◦k′ = 0, then there is a
unique morphism g : K′ →K such that k′ = k ◦g.
34
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
In other words, the object K represents the functor Mop →Ab,
K′ 7→{k′ ∈HomM(K′, M) | f ◦k′ = 0}.
The kernel of f is of course unique up to a unique isomorphism (if it exists), and we
denote if by Ker(f). Sometimes Ker(f) refers only to the object K, and other times
it refers only to the morphism k; as usual, this should be clear from the context.
Deﬁnition 2.3.2. Let M be an additive category, and let f : M →N be a
morphism in M. A cokernel of f is a pair (C, c), consisting of an object C ∈M and
a morphism c : N →C, with these two properties:
(i) c ◦f = 0.
(ii) If c′ : N →C′ is a morphism in M such that c′ ◦f = 0, then there is a
unique morphism g : C →C′ such that c′ = g ◦c.
In other words, the object C corepresents the functor M →Ab,
C′ 7→{c′ ∈HomM(N, C′) | c′ ◦f = 0}.
The cokernel of f is of course unique up to a unique isomorphism (if it exists), and
we denote if by Coker(f). Sometimes Coker(f) refers only to the object C, and
other times it refers only to the morphism c; as usual, this should be clear from the
context.
Example 2.3.3. In Mod A all kernels and cokernels exist. Given f : M →N, the
kernel is k : K →M, where K := {m ∈M | f(m) = 0}, and the k is the inclusion.
The cokernel is c : N →C, where C := N/f(M), and c is the canonical projection.
Proposition 2.3.4. Let M be an additive category, and let f : M →N be a
morphism in M.
(1) If k : K →M is a kernel of f, then k is a monomorphism.
(2) If c : N →C is a cokernel of f, then c is an epimorphism.
Exercise 2.3.5. Prove the proposition.
Deﬁnition 2.3.6. Assume the additive category M has kernels and cokernels. Let
f : M →N be a morphism in M.
(1) Deﬁne the image of f to be Im(f) := Ker(Coker(f)).
(2) Deﬁne the coimage of f to be Coim(f) := Coker(Ker(f)).
The image is familiar, but the coimage is probably not. The next diagram should
help. We start with a morphism f : M →N in M. The kernel and cokernel of f
ﬁt into this diagram: K
k−→M
f−→N
c−→C. Inserting α := Coker(k) = Coim(f) and
β := Ker(c) = Im(f) we get the following commutative diagram (solid arrows):
(2.3.7)
K
k
/
0
#
M
f
/
α

γ
#
N
c
/ C
M ′
f ′
/ N ′
0
;
β
O
Since c◦f = 0 there is a unique morphism γ (the dashed arrow) making the diagram
commutative. Now β ◦γ ◦k = f ◦k = 0; and β is a monomorphism; so γ ◦k = 0.
Hence there is a unique morphism f ′ : M ′ →N ′ making the diagram commutative.
We conclude that f : M →N induces a morphism
(2.3.8)
f ′ : Coim(f) →Im(f).
Deﬁnition 2.3.9. An abelian category is an additive category M with these two
extra properties:
(i) All morphisms in M admit kernels and cokernels.
35
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
(ii) For every morphism f : M →N in M, the induced morphism f ′ in equation
(2.3.8) is an isomorphism.
Here is a less precise but (maybe) easier to remember way to state property (ii).
Because M ′ = Coker(Ker(f)) and N ′ = Ker(Coker(f)), we see that
(2.3.10)
Coker(Ker(f)) = Ker(Coker(f)).
From now on we forget all about the coimage.
Exercise 2.3.11. For any ring A, prove that the category Mod A is abelian.
This includes the category Ab = Mod Z, from which the name derives.
Deﬁnition 2.3.12. Let M be an abelian category, and let N be a full subcategory
of M. We say that N is a full abelian subcategory of M if the zero object belongs to
N, and N is closed in M under taking ﬁnite direct sums, kernels and cokernels.
Exercise 2.3.13. In the situation of Deﬁnition 2.3.12, show that the category N
is itself abelian.
Example 2.3.14. Let M1 be the category of ﬁnitely generated abelian groups,
and let M0 be the category of ﬁnite abelian groups.
Then M1 is a full abelian
subcategory of Ab, and M0 is a full abelian subcategory of M1.
Exercise 2.3.15. Let N be the full subcategory of Ab whose objects are the ﬁnitely
generated free abelian groups. It is an additive subcategory of Ab (since it is closed
under direct sums).
(1) Show that N is closed under kernels in Ab.
(2) Show that N is not closed under cokernels in Ab, so it is not a full abelian
subcategory of Ab.
(3) Show that N has cokernels (not the same as those of Ab). Still, it fails to
be an abelian category.
Exercise 2.3.16. The category Grp is not linear of course. Still, it does have a zero
object (the trivial group). Show that Grp has kernels and cokernels, but condition
(ii) of Deﬁnition 2.3.9 fails.
Exercise 2.3.17. Let Hilb be the category of Hilbert spaces over C. The morphisms
are the continuous C-linear homomorphisms. Show that Hilb is a C-linear additive
category with kernels and cokernels, but it is not an abelian category.
Exercise 2.3.18. Let A be a ring. Show that A is left noetherian iﬀthe category
Modf A of ﬁnitely generated left modules is a full abelian subcategory of Mod A.
Example 2.3.19. Let (X, A) be a ringed space; namely X is a topological space
and A is a sheaf of rings on X. There is a very detailed discussion of sheaves of
modules in [63, Section II.1] and [75, Sections 2.1-2.2]. Let us mention only one
aspect of it.
We denote by Modpr A the category of presheaves of left A-modules on X. This
is an abelian category. Given a morphism φ : M →N in Modpr A, its kernel is the
presheaf Kerpr(φ) deﬁned by
Γ
 U, Kerpr(φ)

:= Ker
 φ : Γ(U, M) →Γ(U, N)

on every open set U ⊆X. The cokernel of φ is the presheaf Cokerpr(φ) deﬁned by
Γ
 U, Cokerpr(φ)

: Coker
 φ : Γ(U, M) →Γ(U, N)

.
Now let Mod A be the full subcategory of Modpr A consisting of sheaves. It is a
full additive subcategory of Modpr A, closed under kernels. However, Mod A is not
closed under cokernels inside Modpr A, and hence it is not a full abelian subcategory.
36
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Nonetheless, Mod A is itself an abelian category, but with diﬀerent cokernels.
Given a morphism φ : M →N in Mod A, its cokernel in Mod A is the sheaf
Coker(φ) that’s associated to the presheaf Cokerpr(φ).
Proposition 2.3.20. Let M be a linear category.
(1) The opposite category Mop has a canonical structure of a linear category.
(2) If M is additive, then Mop is also additive.
(3) If M is abelian, then Mop is also abelian.
Proof. (1) Since HomMop(M, N) = HomM(N, M), this is an abelian group. The
bilinearity of the composition in Mop is clear.
(2) The zero objects in M and Mop are the same. Existence of ﬁnite coproducts in
Mop is because of existence of ﬁnite products in M; see Proposition 2.2.3(1).
(3) Mop has kernels and cokernels, since KerMop(Op(φ)) = CokerM(φ) and vice
versa. Also the symmetric condition (ii) of Deﬁnition 2.3.9 holds.
□
Proposition 2.3.21. Let φ : M →N be a morphism in an abelian category M.
(1) φ is a monomorphism if and only if Ker(φ) = 0.
(2) φ is an epimorphism if and only if Coker(φ) = 0.
(3) φ is an isomorphism if and only if it is both a monomorphism and an
epimorphism.
Exercise 2.3.22. Prove this proposition.
Consider a diagram
(2.3.23)
S =
 · · · M−1
φ−1
−−→M0
φ0
−→M1
φ1
−→M2 · · ·

in an abelian category M, extending ﬁnitely or inﬁnitely to either side. Such a
diagram is called a sequence in M. An object Mi appearing in S is called interior
in S if there is an object Mi−1 appearing to the left of it, and an object Mi+1
appearing to the right of it.
Deﬁnition 2.3.24. Let S be a sequence in the abelian category M, with notation
as in (2.3.23).
(1) Suppose Mi is an interior object in S. We say that the sequence S is exact
at Mi if Im(φi−1) = Ker(φi), as subobjects of Mi.
(2) The sequence S is said to be exact if it is exact at all of its interior objects.
Example 2.3.25. A morphism φ : M →N in an abelian category M is a monomor-
phism iﬀ0 →M
φ−→N is an exact sequence. The morphism φ is an epimorphism
iﬀthe sequence M
φ−→N →0 is exact.
Deﬁnition 2.3.26. A short exact sequence in an abelian category M is as exact
sequence of the form
S =
 0 →M0
φ0
−→M1
φ1
−→M2 →0

.
Proposition 2.3.27. Let M be a K-linear abelian category.
(1) Let 0 →M ′
φ−→M
ψ−→M ′′ be an exact sequence in M. Then for every
L ∈M the sequence
0 →HomM(L, M ′)
Hom(id,φ)
−−−−−−→HomM(L, M)
Hom(id,ψ)
−−−−−−−→HomM(L, M ′′)
in Mod K is exact.
37
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
(2) Let M ′
φ−→M
ψ−→M ′′ →0 be an exact sequence in M. Then for every
N ∈M the sequence
0 →HomM(M ′′, N)
Hom(ψ,id)
−−−−−−−→HomM(M, N)
Hom(φ,id)
−−−−−−→HomM(M ′, N)
in Mod K is exact.
Exercise 2.3.28. Prove Proposition 2.3.27. (Hint: use the deﬁnitions of kernel,
cokernel and image.)
