---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-023-27-injective-objects
section_title: "Injective Objects"
section_number: 2.7
pages: 47-51
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
Deﬁnition 2.7.1.An objectI∈M is called aninjective objectif for every mor-
phism γ:M→I and everymonomorphism ψ:M↣N, there exists a morphism
˜γ:N→I such that ˜γ◦ψ=γ.
This is depicted in the following commutative diagram inM :
I
M
γ
OO
//
ψ
//N
˜γ
cc
Proposition 2.7.2. The following conditions are equivalent forI∈M:
(i) I is injective.
(ii) The additive functorHomM(−,I ) : Mop→Ab is exact.
(iii) Every short exact sequence(2.6.1) with M′=I is split.
Exercise 2.7.3. Prove Proposition 2.7.2.
47
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Recall that Op : M→Mop is an exact functor.
Proposition 2.7.4. An objectJ∈M is injective if and only if the objectOp(J)∈
Mop is projective.
Exercise 2.7.5. Prove Proposition 2.7.4.
Example 2.7.6. Let A be a ring. Unlike projectives, the structure of injective
objects in ModA is very complicated, and not much is known (except that they
exist). However if A is a commutative noetherian ring then we know this: every
injective module I is a direct sum of indecomposable injective modules; and the
indecomposables are parameterized bySpec(A), the set of prime ideals ofA. These
facts are due to Matlis; see Subsection 13.2 in the book.
Deﬁnition 2.7.7.We say M has enough injectives if every M ∈M admits a
monomorphism M→I to an injective objectI.
Here are a few results about injective objects. Recall that modules over a ring
are always left modules by default.
Proposition 2.7.8. Let f : A→B be a ring homomorphism, and letI be an
injectiveA-module. ThenJ := HomA(B,I ) is an injectiveB-module.
Proof. Note thatB is a leftA-module viaf, and a rightB-module. This makes
J into a leftB-module. In a formula: forφ∈J and b,b′∈B we have(b·φ)(b′) =
φ(b′·b).
Now given anyN∈ModB there is an isomorphism
(2.7.9) HomB(N,J ) = HomB(N, HomA(B,I ))∼= HomA(N,I ).
This is a natural isomorphism (of functors inN). So the functor HomB(−,J ) is
exact, and henceJ is injective. □
Theorem 2.7.10 (Baer Criterion). Let A be a ring andI an A-module. Assume
that every A-module homomorphism a→I from a left ideala⊆A extends to a
homomorphism A→I. Then the moduleI is injective.
Proof. Consider an A-module M, a submodule N ⊆M, and a homomorphism
γ: N→I. We have to prove thatγextends to a homomorphismM→I. Look
at the pairs (N′,γ′) consisting of a submoduleN′⊆M that containsN, and a
homomorphism γ′:N′→I that extendsγ. The set of all such pairs is ordered by
inclusion, and it satisﬁes the conditions of Zorn’s Lemma. Therefore there exists a
maximal pair (N′,γ′). We claim thatN′=M.
Otherwise, there is an element m∈M that does not belong to N′. Deﬁne
N′′:=N′+A·m, soN′⊊N′′⊆M. Let a :={a∈A|a·m∈N′}, which is a left
ideal ofA. There is a short exact sequence
0→a
α
− →N′⊕A→N′′→0
of A-modules, where α(a) := ( a·m,−a). Let φ: a→I be the homomorphism
φ(a) := γ′(a·m). By assumption, it extends to a homomorphism˜φ: A→I. We
get a homomorphismγ′+ ˜φ:N′⊕A→I that vanishes on the image ofα. Thus
there is an induced homomorphismγ′′:N′′→I. This contradicts the maximality
of (N′,γ′). □
Lemma 2.7.11. TheZ-moduleQ/Z is injective.
Proof. By the Baer criterion, it is enough to consider a homomorphismγ: a→Q/Z
for an ideal a = n·Z⊆Z. We may assume thatn⁄= 0. Say γ(n) = r +Z with
r∈Q. Then we can extendγto ˜γ:Z→Q/Z with ˜γ(1) :=r/n +Z. □
48
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Lemma 2.7.12.Let{Ix}x∈X be a collection of injective objects ofM. If the product∏
x∈XIx exists in M, then it is an injective object.
Proof. Exercise. □
Theorem 2.7.13. LetA be any ring. The categoryModA has enough injectives.
Proof. The proof is done in a few steps.
Step 1. Here A = Z. Take any nonzeroZ-module M and any nonzerom∈M.
Consider the cyclic submodule M′:= Z·m ⊆M. There is a homomorphism
γ′: M′→Q/Z s.t. γ′(m)⁄= 0. Indeed, if M′∼=Z, then we take anyr∈Q−Z;
and if M′∼= Z/(n) for some n > 0, then we taker := 1/n. In either case, we
deﬁneγ′(m) :=r +Z∈Q/Z. SinceQ/Z is an injectiveZ-module, γ′extends to a
homomorphism γ:M→Q/Z. By construction we haveγ(m)⁄= 0.
Step 2. Now A is any ring,M is any nonzeroA-module, and m∈M a nonzero
element. Deﬁne theA-module I := Hom Z(A,Q/Z), which, according to Lemma
2.7.11 and Proposition 2.7.8, is an injectiveA-module. Let γ:M→Q/Z be aZ-
linear homomorphism such thatγ(m)⁄= 0. Suchγexists by step 1. Letθ:I→Q/Z
be theZ-linear homomorphism that sends an elementχ∈I to χ(1)∈Q/Z. The
adjunction formula (2.7.9) gives an A-module homomorphism ψ: M →I s.t.
θ◦ψ=γ. We note that(θ◦ψ)(m) =γ(m)⁄= 0, and henceψ(m)⁄= 0.
Step 3. Here A and M are arbitrary. Let I be as in step 2. For every nonzero
m∈M there is anA-linear homomorphismψm : M→I such thatψm(m)⁄= 0.
Form = 0 letψ0 :M→I be an arbitrary homomorphism (e.g.ψ0 = 0). Deﬁne the
A-moduleJ :=∏
m∈MI. There is a homomorphismψ:=∏
m∈Mψm :M→J, and
it is easy to check thatψis a monomorphism. By Lemma 2.7.12,J is an injective
A-module. □
Exercise2.7.14. Atthepriceofgettingabiggerinjectivemodule, wecanmakethe
construction of injective resolutions functorial. LetI := HomZ(A,Q/Z) as above.
Given anA-module M, consider the setX(M) := HomA(M,I )∼= HomZ(M,Q/Z).
Let J(M) := ∏
ψ∈X(M)I. There is a “tautological” homomorphismφM : M →
J(M). Show that φM is a monomorphism, J : M ↦→J(M) is a functor, and
φ: Id→J is a natural transformation.
Is the functorJ : ModA→ModA additive?
Example 2.7.15. Let N be the category of torsion abelian groups, and M the
category of ﬁnite abelian groups. Then N ⊆Ab and M ⊆N are full abelian
subcategories. M has no projectives nor injectives except 0 (see Exercise 2.6.7
regarding projectives). The only projective in N is 0. However, it can be shown
that N has enough injectives; see [63, Lemma III.3.2] or [161, Proposition 4.6].
Proposition 2.7.16. If A is a left noetherian ring, then every direct sum of injec-
tive A-modules is an injective module.
Exercise 2.7.17. Prove Proposition 2.7.16. (Hint: use the Baer criterion.)
Exercise2.7.18. Here we study injectivesin the categoryAb = ModZ. ByLemma
2.7.11, themoduleI :=Q/Zisinjective. Fora(positive)primenumber p, wedenote
byˆZp the ring ofp-adic integers, and byˆQp its ﬁeld of fractions (namely thep-adic
completions ofZ andQ respectively). Deﬁne the abelian groupIp :=ˆQp/ˆZp.
(1) Show thatIp is an injective object ofAb.
(2) Show thatIp is indecomposable (i.e. it is not the direct sum of two nonzero
objects).
(3) Show thatI∼=⨁
pIp.
49
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(4) The theory (see Subsection 13.2) tells us that there is another indecompos-
able injective object inAb, besides theIp. Try to identify it.
The abelian categoryModA associated to a ringed space(X,A) was introduced
in Example 2.3.19.
Proposition2.7.19. Let (X,A) be a ringed space. The categoryModA has enough
injectives.
Proof. LetM be anA-module. Take a pointx∈X. The stalkMx is a module
over the ringAx, and by Theorem 2.7.13 we can ﬁnd an embeddingφx :Mx→Ix
into an injectiveAx-module. Letgx :{x}→X be the inclusion, which we may view
as a map of ringed spaces from({x},Ax) to (X,A). DeﬁneIx :=gx∗(Ix), which is
anA-module (in fact it is a constant sheaf supported on the closed set{x}⊆X).
The adjunction formula gives rise to a sheaf homomorphismψx :M→Ix. Since
the functorg∗
x : ModA→ModAx is exact, the adjunction formula shows thatIx
is an injective object ofModA.
Finally letJ := ∏
x∈XIx. This is an injectiveA-module. There is a homo-
morphism ψ:= ∏
x∈Xψx :M→J in ModA. This is a monomorphism, since
for every pointx, lettingJx be the stalk of the sheafJ at x, the composition
Mx
ψx
−−→Jx
px
−→Ix is the embeddingφx :Mx→Ix. □
Remark 2.7.20. Let A be a nonzero ring, and consider the abelian category
M := ModA, the category of A-modules. A reasonable question to ask is this:
Are the abelian categories M and Mop equivalent? The answer is negative. In
fact, P. Freyd, in [47, Exercise 5.B.3], shows that(ModA)op is not equivalent, as
an abelian category, toModB for any ringB. The argument involves a delicate
studyofcountablecoproductsandproducts, andpropertiesofGrothendieckabelian
categories.
Here is a special case of the previous remark, that might shed some more light
on the issue.
Example 2.7.21. Consider the categoryModZ = Ab of abelian groups. Here is a
proof that there does not exist an additive equivalenceF : Abop→Ab. Suppose we
had such an equivalence. Consider the objectP :=Z∈Ab, and letI :=F (P )∈Ab.
Because P is an indecomposable projective object, andF : Ab→Ab is a con-
travariant equivalence, the objectI has to be an indecomposable injective. The
endomorphism rings areEndAb(I)∼= EndAb(P )op =Zop =Z. However, the struc-
ture theorem for injective modules over commutative noetherian rings (Theorem
13.2.15) says that the only indecomposable injectives inAb are I = ˆQp/ˆZp and
I =Q; and their endomorphism rings areˆZp andQ respectively.
50
Derived Categories | Amnon Yekutieli | 14 Apr 2019
