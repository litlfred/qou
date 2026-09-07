---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-021-25-additive-functors
section_title: "Additive Functors"
section_number: 2.5
pages: 42-46
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
Deﬁnition 2.5.1.Let M and N be K-linear categories. A functorF : M→N is
called aK-linear functorif for everyM0,M 1∈M the function
F : HomM(M0,M 1)→HomN
(
F (M0),F (M1)
{
is aK-linear homomorphism.
When the base ringK is implicit (cf. Convention 1.2.4), we sometimes say that
F is anadditive functor, with the same meaning asK-linear functor.
Additive functors commute with ﬁnite direct sums. More precisely:
Proposition 2.5.2. Let F : M→N be an additive functor between linear cate-
gories, let{Mi}i∈I be a ﬁnite collection of objects ofM, and assume that the direct
sum (M,{ei}i∈I) of the collection{Mi}i∈I exists in M. Then
(
F (M),{F (ei)}i∈I
{
is a direct sum of the collection{F (Mi)}i∈I in N.
Exercise 2.5.3. Prove Proposition 2.5.2. (Hint: use Proposition 2.2.3.)
Note that the proposition above also talks about ﬁnite products, because of
Proposition 2.2.3.
Proposition 2.5.4. Suppose F,G : K→L are additive functors between linear
categories, andη: F→G is a morphism of functors. LetM,M′,N be objects of
K, and assume thatN∼=M⊕M′. Then the following two conditions are equivalent.
(i) ηN :F (N)→G(N) is an isomorphism.
(ii) ηM :F (M)→G(M) and ηM′:F (M′)→G(M′) are isomorphisms.
Exercise 2.5.5. Prove Proposition 2.5.4.
Example 2.5.6. Letf :A→B be a ring homomorphism. There are two additive
functors associated tof : the restriction functor Restf : ModB→ModA and the
induction functor Indf : ModA→ModB. Given a B-module N, the A-module
Restf(N) has the same underlyingK-module, andA acts on it throughf. For an
A-module M, the inducedB-module is Indf(M) :=B⊗AM.
Proposition 2.5.7. Let F : M→N be an additive functor between linear cate-
gories. Then:
(1) For everyM ∈M the function F : End M(M)→EndN(F (M)) is a ring
homomorphism.
(2) For everyM0,M 1∈M the function
F : HomM(M0,M 1)→HomN
(
F (M0),F (M1)
{
is a homomorphism of left EndM(M1)-modules, and of right EndM(M0)-
modules.
(3) If M is a zero object ofM, thenF (M) is a zero object ofN.
Proof.
(1) By Deﬁnition 2.5.1 the functionF respects addition. By the deﬁnition of a
functor, it respects multiplication and units.
(2) Immediate from the deﬁnitions, like (1).
(3) Combine part (1) with Proposition 2.2.9. □
Deﬁnition 2.5.8.Let F : M→N be an additive functor between abelian cate-
gories.
(1) F is called left exact if it commutes with kernels. Namely for every mor-
phism φ: M0 →M1 in M, with kernel k : K →M0, the morphism
F (k) :F (K)→F (M0) is a kernel ofF (φ) :F (M0)→F (M1).
42
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(2) F is called right exact if it commutes with cokernels. Namely for every
morphism φ: M0→M1 in M, with cokernelc : M1→C, the morphism
F (c) :F (M1)→F (C) is a cokernel ofF (φ) :F (M0)→F (M1).
(3) F is calledexact if it is both left exact and right exact.
Let us illustrate this. Supposeφ: M0→M1 is a morphism inM, with kernel
K and cokernelC. ApplyingF to the sequenceK
k
− →M0
φ
− →M1
c
− →C in M we get
the solid arrows in this diagram
F (K)
F(k) //
ψ &&
F (M0)
F(φ) //F (M1)

F(c) //F (C)
KerN(F (φ))
OO
CokerN(F (φ))
χ
77
in N. Because N is abelian, we get the vertical dashed arrows: the kernel and
cokernel ofF (φ). The slanted dashed arrows exist and are unique becauseF (φ)◦
F (k) = 0 andF (c)◦F (φ) = 0. Left exactness ofF requiresψto be an isomorphism,
and right exactness requiresχto be an isomorphism.
Recall that a short exact sequence inM is an exact sequence of the form
(2.5.9) S =
(
0→M0
φ0
−→M1
φ1
−→M2→0
{
.
Proposition 2.5.10. LetF : M→N be an additive functor between abelian cate-
gories.
(1) The functorF is left exact if and only if for every short exact sequenceS
in M, with notation(2.5.9), the sequence
0→F (M0)
F(φ0)
−−−−→F (M1)
F(φ0)
−−−−→F (M2)
is exact inN.
(2) The functorF is right exact if and only if for every short exact sequenceS
in M, with the notation with notation(2.5.9), the sequence
F (M0)
F(φ0)
−−−−→F (M1)
F(φ1)
−−−−→F (M2)→0
is exact inN.
Exercise 2.5.11. Prove Proposition 2.5.10. (Hint:M0∼= Ker(M1→M2) etc.)
Example 2.5.12. Let A be a commutative ring, and letM be a ﬁxedA-module.
Deﬁne functorsF,G : ModA→ModA like this: F (N) := M⊗AN and G(N) :=
HomA(M,N ). ThenF is right exact andG is left exact.
Example 2.5.13. Let f : A→B be a ring homomorphism. In the notation of
Example 2.5.6, the restriction functor Restf is exact, and the induction functor
Indf is right exact.
Proposition 2.5.14. LetF : M→N be an additive functor between abelian cate-
gories. IfF is an equivalence then it is exact.
Proof. We will prove thatF respects kernels; the proof for cokernels is similar.
Take a morphismφ:M0→M1 in M, with kernelK. We have this diagram (solid
arrows):
M
ψ

θ
##
K k //M0
φ //M1
43
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Applying F we obtain this diagram (solid arrows):
N =F (M)
F(ψ)

¯θ
’’
F (K)
F(k) //F (M0)
F(φ) //F (M1)
in N. Suppose ¯θ: N →F (M0) is a morphism in N s.t. F (φ)◦¯θ= 0. Since F
is essentially surjective on objects, there is someM ∈M with an isomorphism
α: F (M)
≃
− →N. After replacingN with F (M) and ¯θwith ¯θ◦α, we can assume
that N =F (M).
Now since F is fully faithful, there is a uniqueθ: M →M0 s.t. F (θ) = ¯θ;
and φ◦θ= 0. So there is a uniqueψ: M →K s.t. θ= k◦ψ. It follows that
F (ψ) :F (M)→F (K) is the unique morphism s.t.¯θ=F (k)◦F (ψ). □
Here is a result that could aﬀord another proof of the previous proposition.
Proposition 2.5.15. Let F : M→N be an additive functor between linear cate-
gories. AssumeF is an equivalence, with quasi-inverseG. Then G : N→M is an
additive functor.
Exercise 2.5.16. Prove Proposition 2.5.15.
Deﬁnition 2.5.17.Consider abelian categoriesM and N. Suppose we are given a
sequence
···F−1
φ−1
−−→F0
φ0
−→F1
φ1
−→F2···
(ﬁnite or inﬁnite on either side), where eachFi : M→N is an additive functor, and
each φi : Fi→Fi+1 is a morphism of functors. We say that this sequence is an
exact sequence of additive functorsif for every objectM∈M the sequence
···F−1(M)
φ−1,M
−−−−→F0(M)
φ0,M
−−−→F1(M)
φ1,M
−−−→F2(M)···
in N is exact.
Proposition 2.5.18. Let M and N be abelian categories, and letF0
φ0
−→F1
φ1
−→F2
be a sequence of additive functorsM→N.
(1) If F0
φ0
−→F1
φ1
−→F2→0 is an exact sequence of additive functors, and if
the functors F0 and F1 are both right exact, then the functorF2 is right
exact.
(2) If 0→F0
φ0
−→F1
φ1
−→F2 is an exact sequence of additive functors, and if
the functorsF1 and F2 are both left exact, then the functorF0 is left exact.
Proof.
(1) Let M′σ
− →M
τ
− →M′′→0 be an exact sequence in M. We must show that
F2(M′)→F2(M)→F2(M′′)→0 is an exact sequence inN. Let us examine the
44
Derived Categories | Amnon Yekutieli | 14 Apr 2019
commutative diagram
(2.5.19) F0(M′)
φ0,M′
//
F0(σ)

F1(M′)
F1(σ)

φ1,M′
//F2(M′) //
F2(σ)

0
F0(M)
φ0,M //
F0(τ)

F1(M)
φ1,M //
F1(τ)

F2(M) //
F2(τ)

0
F0(M′′)
φ0,M′′
//

F1(M′′)
φ1,M′′
//

F2(M′′) //

0
0 0 0
in N. It is known that the rows and the ﬁrst two columns are exact. We must prove
that the third column is exact.
First let us prove thatF2(τ) is an epimorphism. This is easy: we know that
F1(τ) and φ1,M′′are epimorphisms; hence φ1,M′′◦F1(τ) = F2(τ)◦φ1,M is an
epimorphism; and thusF2(τ) is an epimorphism.
More challenging is the proof that the third column is exact atF2(M), namely
that Im(F2(σ))→Ker(F2(τ)) is an epimorphism. For this we shall use the ﬁrst
sheaf trick (Proposition 2.4.9) and a diagram chase. Consider a section m2 ∈
Γ(U, Ker(F2(τ))) on some “open set”U, i.e. for some objectU∈M. We shall prove
that there exist a coveringV ↠ U and a sectionm′
2 ∈Γ(V,F 2(M′)) such that
F2(σ)(m′
2) =m2 in Γ(V,F 2(M)).
Becauseφ1,M is an epimorphism, there is a coveringU1↠U and a sectionm1∈
Γ(U1,F 1(M)) such thatφ1,M(m1) =m2 in Γ(U1,F 2(M)). Letm′′
1 :=F1(τ)(m1)∈
Γ(U1,F 1(M′′)). We have φ1,M′′(m′′
1) = F2(τ)(m2) = 0 . This means that m′′
1 ∈
Γ(U1, Ker(φ1,M′′)).
The exactness of the third row says that for some coveringU2↠ U1 there is a
section m′′
0∈Γ(U2,F 0(M′′)) such thatφ0,M′′(m′′
0) =m′′
1 in Γ(U2,F 1(M′′)).
The exactness of the ﬁrst column implies that for some coveringU3↠U2 there is
a sectionm0∈Γ(U3,F 0(M)) such thatm′′
0 =F0(τ)(m0) in Γ(U3,F 0(M′′)). Deﬁne
˜m1 :=m1−φ0,M(m0) in Γ(U3,F 1(M)). Note thatφ1,M( ˜m1) =φ1,M(m1) =m2 in
Γ(U3,F 2(M)). AlsoF1(τ)( ˜m1) = 0, i.e. ˜m1∈Γ(U3, Ker(F1(τ))).
Due to the exactness of the second column, for some coveringV ↠ U3 there
is a sectionm′
1∈Γ(V,F 1(M′)) such that ˜m1 = F1(σ)(m′
1) in Γ(V,F 1(M)). De-
ﬁnem′
2 := φ1,M′(m′
1)∈Γ(V,F 2(M′)). Then F2(σ)(m′
2) = φ1,M( ˜m1) = m2 in
Γ(V,F 2(M)).
(2) See next exercise. □
Exercise 2.5.20.Prove part (2) of Proposition 2.5.17. (Hint: imitate the proof of
part (1); but this is easier.)
We end this subsection with a discussion of additive contravariant functors. Sup-
pose M and N are linear categories. A contravariant functorF : M→N is said to
be additive if it satisﬁes the condition in Deﬁnition 2.5.1, with the obvious changes.
Proposition 2.5.21. Let M and N be linear categories. Put onMop the canonical
linear structure(see Proposition2.3.20).
(1) The functor Op : M→Mop is an additive contravariant functor.
(2) If F : M→N is an additive contravariant functor, thenF◦Op : Mop→
N is an additive functor; and vice versa.
Exercise 2.5.22. Prove Proposition 2.5.21.
45
Derived Categories | Amnon Yekutieli | 14 Apr 2019
In view of Proposition 2.5.10, we can give an unambiguous deﬁnition of left and
right exact contravariant functors.
Deﬁnition 2.5.23.Let F : M→N be an additive contravariant functor between
abelian categories.
(1) F a left exact contravariant functorif for every short exact sequenceS in
M, in the notation of (2.5.9), the sequence
0→F (M2)
F(φ1)
−−−−→F (M1)
F(φ0)
−−−−→F (M0)
in N is exact.
(2) F is aright exact contravariant functorif for every short exact sequenceS
in M, the sequence
F (M2)
F(φ1)
−−−−→F (M1)
F(φ0)
−−−−→F (M0)→0
in N is exact.
(3) F is an exact contravariant functorif it sends every short exact sequence
S in M to a short exact sequence inN.
Proposition 2.5.24. Let M and N be abelian categories. Recall thatMop is also
an abelian category.
(1) The functor Op : M→Mop is an exact contravariant functor.
(2) If F : M→N is an exact contravariant functor, thenF◦Op : Mop→N
is an exact functor; and vice versa. Likewise for left exactness and right
exactness.
Exercise 2.5.25. Prove Proposition 2.5.24.
Example 2.5.26. Let A be a commutative ring, and letM be a ﬁxedA-module.
Deﬁne the contravariant functorF : ModA→ModA to beF (N) := HomA(N,M ).
Then F is a left exact contravariant function.
Sometimes M and Mop are equivalent as abelian categories, as the next exercise
shows. For a counterexample see Remark 2.7.20 below.
Exercise 2.5.27. Let K be a ﬁeld, and consider the categoryM := ModfK of
ﬁnitely generatedK-modules (traditionally known as “ﬁnite dimensional vector
spaces overK”). This is aK-linear abelian category. Find aK-linear equivalence
F : Mop→M.
