---
doc_id: arxiv-1010.4386v5
doc_title: "ON THE HOMOLOGY OF COMPLETION AND TORSION"
section_id: sec-002-2-the-derived-completion-and-torsion-functors
section_title: "The Derived Completion and Torsion Functors"
section_number: 2
pages: 7-10
source_pdf: 1010.4386v5.pdf
source_sha256: 168226dbb5a479ed
doc_brief: "ON THE HOMOLOGY OF COMPLETION AND TORSION — Let A be a commutative ring, and a a weakly proregular ideal in A."
---
In this section A is a commutative ring, and a is an ideal in it. We do not assume
that a is ﬁnitely generated or that A is a-adically complete.
For anyi∈ N letAi :=A/ai+1. The collection of rings {Ai}i∈N forms an inverse
system. Following [GM, AJL1], for an A-module M we write
(2.1) Λ a(M ) := lim
←i
(Ai⊗AM )
for the a-adic completion of M , although we sometimes use the more conventional
(yet possibly ambiguous) notation ˆM . We get an additive functor Λ a : ModA→
ModA. Recall that there is a functorial homomorphism
(2.2) τM :M→ Λa(M )
for M∈ ModA, coming from the homomorphisms M→ Ai⊗AM . The module
M is called a-adically complete ifτM is an isomorphism. (Some texts, such as [Bo],
would say that M is separated and complete). As customary, when M is complete
we usually identify M with Λ a(M ) via τM .
8 MARCO PORTA, LIRAN SHAUL AND AMNON YEKUTIELI
If the ideal a is ﬁnitely generated, then the functor Λ a is idempotent, in the sense
that the homomorphism
τΛ a(M) : Λ a(M )→ Λa(Λa(M ))
is an isomorphism for every module M (see [Ye2, Corollary 3.6]).
Let ˆA := Λ a(A). Then ˆA is a ring, and τA : A→ ˆA is a ring homomorphism.
If A is noetherian then ˆA is also noetherian, and ﬂat over A. One can view the
completion as a functor Λ a : ModA→ Mod ˆA. But in this paper we shall usually
ignore this.
Remark 2.3. The full subcategory of ModA consisting of a-adically complete
modules is additive, but not abelian in general.
It is well known that when A is noetherian, the completion functor Λ a is exact
on ModfA, the category of ﬁnitely generated modules. However, on ModA the
functor Λ a is neither left exact nor right exact, even in the noetherian case (see
[Ye2, Examples 3.19 and 3.20]).
WhenA is not noetherian, we do not know if ˆA is ﬂat over A. Still, if a is ﬁnitely
generated, and we let ˆa := ˆAa⊂ ˆA, then ˆA is ˆa-adically complete; this follows from
[Ye2, Corollary 3.6].
If the ideal a is not ﬁnitely generated, things are even worse: the functor Λa can
fail to be idempotent; i.e. the completion Λ a(M ) of a module M could fail to be
complete. See [Ye2, Example 1.8].
As for any additive functor, the functor Λ a has a left derived functor
(2.4) LΛ a : D(ModA)→ D(ModA) , ξ : LΛ a→ Λa
constructed using K-projective resolutions.
The next result was proved in [AJL1]. Since this is so fundame ntal, we chose to
reproduce the easy proof.
Lemma 2.5 ([AJL1]). LetP be an acyclic K-ﬂat complex of A-modules. Then the
complex Λa(P ) is also acyclic.
Proof. Since P is both acyclic and K-ﬂat, for any i we have an acyclic complex
Ai⊗A P . The collection of complexes {Ai⊗A P}i∈N is an inverse system, and
the homomorphism Ai+1⊗APj→ Ai⊗APj is surjective for every i and j. But
Λa(Pj) = lim←i (Ai⊗APj). By the Mittag-Leﬄer argument (see [KS1, Proposition
1.12.4] or [We, Theorem 3.5.8]) the complex Λ a(P ) is acyclic. □
Proposition 2.6. If P is a K-ﬂat complex then the morphism ξP : LΛ a(P )→
Λa(P ) in D(ModA) is an isomorphism. Thus we can calculate LΛa using K-ﬂat
resolutions.
Proof. This is immediate from Lemma 2.5; cf. [RD, Theorem I.5.1]. □
Proposition 2.7 ([AJL1]). Let M∈ D(ModA). There is a morphism τ L
M :M→
LΛa(M ) in D(ModA), functorial in M , such that ξM◦τ L
M = τM as morphisms
M→ Λa(M ).
Proof. Given M∈ D(ModA) let us choose a K-projective resolution φ : P → M .
Sinceφ and ξP are isomorphisms in D(ModA), we can deﬁne
τ L
M := LΛ a(φ)◦ξ−1
P ◦τP◦φ−1 :M→ LΛa(M ).
This is independent of the the chosen resolution φ, and satisﬁes ξM◦τM =τ L
M . □
ON THE HOMOLOGY OF COMPLETION AND TORSION 9
Deﬁnition 2.8. (1) A complex M∈ D(ModA) is called a-adically cohomolog-
ically complete if the morphism τ L
M :M→ LΛa(M ) is an isomorphism.
(2) The full subcategory of D(ModA) consisting of a-adically cohomologically
complete complexes is denoted by D(ModA)a-com.
It is clear that the subcategory D(ModA)a-com is triangulated.
The notion of cohomologically complete complex is quite ill usive. See Example
3.33 .
For an A-module M and i∈ N we identify HomA(Ai,M ) with the submodule
{m∈M| ai+1m = 0}⊂ M.
The a-torsion submodule of M is
Γa(M ) :=
⋃
i∈N
HomA(Ai,M )⊂M.
The module M is called an a-torsion module if Γ a(M ) = M . We denote by
Moda-torA the full subcategory of ModA consisting of a-torsion modules.
We get an additive functor Γ a : ModA→ ModA. In fact this is a left exact
functor. There is a functorial homomorphism σM : Γ a(M )→M which is just the
inclusion. The functor Γ a is idempotent, in the sense that σΓ a(M) : Γ a(Γa(M ))→
Γa(M ) is bijective.
Like every additive functor, the functor Γ a has a right derived functor
(2.9) RΓ a : D(ModA)→ D(ModA) , ξ : Γ a→ RΓa
constructed using K-injective resolutions.
Proposition 2.10. There is a functorial morphism σR
M : RΓ a(M )→M , such that
σM =σR
M◦ξM as morphisms Γa(M )→M in D(ModA).
Proof. Choose a K-injective resolution φ :M→I, and deﬁne
σR
M :=φ−1◦σI◦ξ−1
I ◦ RΓa(φ).
This is independent of the resolution. □
Deﬁnition 2.11. (1) A complex M∈ D(ModA) is called cohomologically a-
torsion if the morphism σR
M : RΓ a(M )→M is an isomorphism.
(2) The full subcategory of D(ModA) consisting of cohomologically a-torsion
complexes is denoted by D(ModA)a-tor.
(3) We denote by Da-tor(ModA) the full subcategory of D(ModA) consisting
of the complexes whose cohomology modules are in Moda-torA.
It is clear that the subcategory D(ModA)a-tor is triangulated.
Since Moda-torA is a thick abelian subcategory of ModA, it follows that
Da-tor(ModA) is a triangulated category. Note that Γ a(I) ∈ Da-tor(ModA) for
any K-injective complex I. Therefore
(2.12) D(ModA)a-tors⊂ Da-tor(ModA).
Later (in Corollary 3.32) we shall see that there is equality in (2.12) under some
extra assumption.
10 MARCO PORTA, LIRAN SHAUL AND AMNON YEKUTIELI
