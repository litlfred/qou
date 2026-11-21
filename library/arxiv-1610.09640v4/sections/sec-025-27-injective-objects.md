---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-025-27-injective-objects
section_title: "Injective Objects"
section_number: 2.7
pages: 47-51
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
Deﬁnition 2.7.1. An object I ∈M is called an injective object if for every mor-
phism γ : M →I and every monomorphism ψ : M ↣N, there exists a morphism
˜γ : N →I such that ˜γ ◦ψ = γ.
This is depicted in the following commutative diagram in M :
I
M
γ
O
/
ψ
/ N
˜γ
c
Proposition 2.7.2. The following conditions are equivalent for I ∈M:
(i) I is injective.
(ii) The additive functor HomM(−, I) : Mop →Ab is exact.
(iii) Every short exact sequence (2.6.1) with M ′ = I is split.
Exercise 2.7.3. Prove Proposition 2.7.2.
47
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Recall that Op : M →Mop is an exact functor.
Proposition 2.7.4. An object J ∈M is injective if and only if the object Op(J) ∈
Mop is projective.
Exercise 2.7.5. Prove Proposition 2.7.4.
Example 2.7.6. Let A be a ring. Unlike projectives, the structure of injective
objects in Mod A is very complicated, and not much is known (except that they
exist). However if A is a commutative noetherian ring then we know this: every
injective module I is a direct sum of indecomposable injective modules; and the
indecomposables are parameterized by Spec(A), the set of prime ideals of A. These
facts are due to Matlis; see Subsection 13.2 in the book.
Deﬁnition 2.7.7. We say M has enough injectives if every M ∈M admits a
monomorphism M →I to an injective object I.
Here are a few results about injective objects. Recall that modules over a ring
are always left modules by default.
Proposition 2.7.8. Let f : A →B be a ring homomorphism, and let I be an
injective A-module. Then J := HomA(B, I) is an injective B-module.
Proof. Note that B is a left A-module via f, and a right B-module. This makes
J into a left B-module. In a formula: for φ ∈J and b, b′ ∈B we have (b·φ)(b′) =
φ(b′·b).
Now given any N ∈Mod B there is an isomorphism
(2.7.9)
HomB(N, J) = HomB(N, HomA(B, I)) ∼= HomA(N, I).
This is a natural isomorphism (of functors in N). So the functor HomB(−, J) is
exact, and hence J is injective.
□
Theorem 2.7.10 (Baer Criterion). Let A be a ring and I an A-module. Assume
that every A-module homomorphism a →I from a left ideal a ⊆A extends to a
homomorphism A →I. Then the module I is injective.
Proof. Consider an A-module M, a submodule N ⊆M, and a homomorphism
γ : N →I. We have to prove that γ extends to a homomorphism M →I. Look
at the pairs (N ′, γ′) consisting of a submodule N ′ ⊆M that contains N, and a
homomorphism γ′ : N ′ →I that extends γ. The set of all such pairs is ordered by
inclusion, and it satisﬁes the conditions of Zorn’s Lemma. Therefore there exists a
maximal pair (N ′, γ′). We claim that N ′ = M.
Otherwise, there is an element m ∈M that does not belong to N ′.
Deﬁne
N ′′ := N ′ + A·m, so N ′ ⊊N ′′ ⊆M. Let a := {a ∈A | a·m ∈N ′}, which is a left
ideal of A. There is a short exact sequence
0 →a
α−→N ′ ⊕A →N ′′ →0
of A-modules, where α(a) := (a·m, −a). Let φ : a →I be the homomorphism
φ(a) := γ′(a·m). By assumption, it extends to a homomorphism ˜φ : A →I. We
get a homomorphism γ′ + ˜φ : N ′ ⊕A →I that vanishes on the image of α. Thus
there is an induced homomorphism γ′′ : N ′′ →I. This contradicts the maximality
of (N ′, γ′).
□
Lemma 2.7.11. The Z-module Q/Z is injective.
Proof. By the Baer criterion, it is enough to consider a homomorphism γ : a →Q/Z
for an ideal a = n·Z ⊆Z. We may assume that n̸ = 0. Say γ(n) = r + Z with
r ∈Q. Then we can extend γ to ˜γ : Z →Q/Z with ˜γ(1) := r/n + Z.
□
48
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Lemma 2.7.12. Let {Ix}x∈X be a collection of injective objects of M. If the product
Q
x∈X Ix exists in M, then it is an injective object.
Proof. Exercise.
□
Theorem 2.7.13. Let A be any ring. The category Mod A has enough injectives.
Proof. The proof is done in a few steps.
Step 1. Here A = Z. Take any nonzero Z-module M and any nonzero m ∈M.
Consider the cyclic submodule M ′ := Z·m ⊆M.
There is a homomorphism
γ′ : M ′ →Q/Z s.t. γ′(m)̸ = 0. Indeed, if M ′ ∼= Z, then we take any r ∈Q −Z;
and if M ′ ∼= Z/(n) for some n > 0, then we take r := 1/n. In either case, we
deﬁne γ′(m) := r + Z ∈Q/Z. Since Q/Z is an injective Z-module, γ′ extends to a
homomorphism γ : M →Q/Z. By construction we have γ(m)̸ = 0.
Step 2. Now A is any ring, M is any nonzero A-module, and m ∈M a nonzero
element. Deﬁne the A-module I := HomZ(A, Q/Z), which, according to Lemma
2.7.11 and Proposition 2.7.8, is an injective A-module. Let γ : M →Q/Z be a Z-
linear homomorphism such that γ(m)̸ = 0. Such γ exists by step 1. Let θ : I →Q/Z
be the Z-linear homomorphism that sends an element χ ∈I to χ(1) ∈Q/Z. The
adjunction formula (2.7.9) gives an A-module homomorphism ψ : M →I s.t.
θ ◦ψ = γ. We note that (θ ◦ψ)(m) = γ(m)̸ = 0, and hence ψ(m)̸ = 0.
Step 3. Here A and M are arbitrary. Let I be as in step 2. For every nonzero
m ∈M there is an A-linear homomorphism ψm : M →I such that ψm(m)̸ = 0.
For m = 0 let ψ0 : M →I be an arbitrary homomorphism (e.g. ψ0 = 0). Deﬁne the
A-module J := Q
m∈M I. There is a homomorphism ψ := Q
m∈M ψm : M →J, and
it is easy to check that ψ is a monomorphism. By Lemma 2.7.12, J is an injective
A-module.
□
Exercise 2.7.14. At the price of getting a bigger injective module, we can make the
construction of injective resolutions functorial. Let I := HomZ(A, Q/Z) as above.
Given an A-module M, consider the set X(M) := HomA(M, I) ∼= HomZ(M, Q/Z).
Let J(M) := Q
ψ∈X(M) I. There is a “tautological” homomorphism φM : M →
J(M).
Show that φM is a monomorphism, J : M 7→J(M) is a functor, and
φ : Id →J is a natural transformation.
Is the functor J : Mod A →Mod A additive?
Example 2.7.15. Let N be the category of torsion abelian groups, and M the
category of ﬁnite abelian groups.
Then N ⊆Ab and M ⊆N are full abelian
subcategories.
M has no projectives nor injectives except 0 (see Exercise 2.6.7
regarding projectives). The only projective in N is 0. However, it can be shown
that N has enough injectives; see [63, Lemma III.3.2] or [161, Proposition 4.6].
Proposition 2.7.16. If A is a left noetherian ring, then every direct sum of injec-
tive A-modules is an injective module.
Exercise 2.7.17. Prove Proposition 2.7.16. (Hint: use the Baer criterion.)
Exercise 2.7.18. Here we study injectives in the category Ab = Mod Z. By Lemma
2.7.11, the module I := Q/Z is injective. For a (positive) prime number p, we denote
by bZp the ring of p-adic integers, and by bQp its ﬁeld of fractions (namely the p-adic
completions of Z and Q respectively). Deﬁne the abelian group Ip := bQp/bZp.
(1) Show that Ip is an injective object of Ab.
(2) Show that Ip is indecomposable (i.e. it is not the direct sum of two nonzero
objects).
(3) Show that I ∼= L
p Ip.
49
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
(4) The theory (see Subsection 13.2) tells us that there is another indecompos-
able injective object in Ab, besides the Ip. Try to identify it.
The abelian category Mod A associated to a ringed space (X, A) was introduced
in Example 2.3.19.
Proposition 2.7.19. Let (X, A) be a ringed space. The category Mod A has enough
injectives.
Proof. Let M be an A-module. Take a point x ∈X. The stalk Mx is a module
over the ring Ax, and by Theorem 2.7.13 we can ﬁnd an embedding φx : Mx →Ix
into an injective Ax-module. Let gx : {x} →X be the inclusion, which we may view
as a map of ringed spaces from ({x}, Ax) to (X, A). Deﬁne Ix := gx∗(Ix), which is
an A-module (in fact it is a constant sheaf supported on the closed set {x} ⊆X).
The adjunction formula gives rise to a sheaf homomorphism ψx : M →Ix. Since
the functor g∗
x : Mod A →Mod Ax is exact, the adjunction formula shows that Ix
is an injective object of Mod A.
Finally let J := Q
x∈X Ix. This is an injective A-module. There is a homo-
morphism ψ := Q
x∈X ψx : M →J in Mod A. This is a monomorphism, since
for every point x, letting Jx be the stalk of the sheaf J at x, the composition
Mx
ψx
−−→Jx
px
−→Ix is the embedding φx : Mx →Ix.
□
Remark 2.7.20. Let A be a nonzero ring, and consider the abelian category
M := Mod A, the category of A-modules. A reasonable question to ask is this:
Are the abelian categories M and Mop equivalent?
The answer is negative.
In
fact, P. Freyd, in [47, Exercise 5.B.3], shows that (Mod A)op is not equivalent, as
an abelian category, to Mod B for any ring B. The argument involves a delicate
study of countable coproducts and products, and properties of Grothendieck abelian
categories.
Here is a special case of the previous remark, that might shed some more light
on the issue.
Example 2.7.21. Consider the category Mod Z = Ab of abelian groups. Here is a
proof that there does not exist an additive equivalence F : Abop →Ab. Suppose we
had such an equivalence. Consider the object P := Z ∈Ab, and let I := F(P) ∈Ab.
Because P is an indecomposable projective object, and F : Ab →Ab is a con-
travariant equivalence, the object I has to be an indecomposable injective. The
endomorphism rings are EndAb(I) ∼= EndAb(P)op = Zop = Z. However, the struc-
ture theorem for injective modules over commutative noetherian rings (Theorem
13.2.15) says that the only indecomposable injectives in Ab are I = bQp/bZp and
I = Q; and their endomorphism rings are bZp and Q respectively.
50
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
