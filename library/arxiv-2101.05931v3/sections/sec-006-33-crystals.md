---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-006-33-crystals
section_title: "Crystals"
section_number: 3.3
pages: 7-9
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
---
Deﬁnition 3.3 ([27]). A g-crystal is a ﬁnite set B together with maps:
rei, rfi : B → B ⊔ {0}, ε i,ϕ i : B → Z, wt : B →X
for all i ∈I, such that:
(1) for any b,b ′ ∈ B, rei(b) = b′ if and only if b = rfi(b′) ,
(2) for all b ∈ B, if rei(b) ∈ B then wt( rei(b)) = wt(b) +αi, and if rfi(b) ∈ B then wt( rfi(b)) =
wt(b) −αi,
(3) for all b ∈ B, εi(b) = max {n ∈ Z : ren
i (b) ⁄= 0}, ϕi(b) = max {n ∈ Z : rf n
i (b) ⁄= 0},
(4) for all b ∈ B, ϕi(b) −εi(b) = ⟨wt(b),h i⟩.
AnyUq(g)-representation V has a corresponding g-crystal B = BV . The underlying set of B is
in natural bijection with a particular basis of V (the “global crystal basis” or “canonical basis”).
The maps rei, rfi are related to the raising and lowering Chevalley operators ; vaguely speaking they
encode information about the leading terms of the Chevalley operators acting on this basis. In
particular, for an integral dominant weight λ, the canonical basis B(λ) of L(λ) carries a natural
crystal structure [20].
The crystal of V naturally arises via categorical representation theory. N amely, as we describe in
the next proposition, if C is a categoriﬁcation of V , then Irr(C) carries a crystal structure isomorphic
to BV . This follows from [16, Proposition 5.20] and [32], and is ex plained in detail in [7].
Proposition 3.4. ([7, Theorem 4.31] ) The set Irr(C) together with:
• Kashiwara operators deﬁned as rEi(X) = soc Ei(X), rFi(X) = soc Fi(X) for X ∈ Irr(C),
• wt(X) = µ for X ∈ C µ, and
• ε(X) = max{n | En
i (X) ⁄= 0}, and ϕ(X) = max{n | Fn
i (X) ⁄= 0},
is a g-crystal isomorphic to the crystal B = BV .
3.4. Jordan-H¨ older series.A categoriﬁcation of a simple representation (respectivel y an isotypic
representation) is called a simple categoriﬁcation (respectively an isotypic categoriﬁcation ).
There is a distinguished categoriﬁcation of L(λ) called the minimal categoriﬁcation and denoted
L(λ) [16, 26, 28, 41, 50]. It is characterized by the fact that L(λ)λ ∼
= L(λ)w0(λ) ∼
=
/CZ −modZ. We let
/CZ
low ∈ L(λ)w0(λ), /CZ
high ∈ L(λ)λ be the generators.
8 IV A HALACHEV A, ANTHONY LICATA, IV AN LOSEV, AND ODED YACOBI
The Jordan-H¨ older Theorem for categorical representatio ns will play an important role in our
work. This was originally developed by Rouquier for additiv e categoriﬁcations [41], and in this
section we transfer these results to the abelian setting. To set this up, recall that given ﬁnite
abelian /CZ -linear categories A, B the Deligne tensor product A ⊗
/CZ
B is universal for the functor
assigning to every such abelian category C the category of bilinear bifunctors A × B → C right
exact in both variables [39, Deﬁnition 1.11.1]. The tensor p roduct is again a ﬁnite abelian /CZ -linear
category, and there is a bifunctor A × B → A ⊗
/CZ
B, (X,Y ) ↦→X ⊗Y . This construction enjoys the
following properties:
(1) The tensor product is unique up to unique equivalence,
(2) for ﬁnite
/CZ -algebras A,B we have that (A−mod) ⊗
/CZ
(B−mod) ∼
= (A ⊗
/CZ
B)−mod, and
(3) Hom A⊗
/CZ
B(X1 ⊗Y1,X 2 ⊗Y2) ∼
= HomA(X1,Y 1) ⊗ HomB(X2,Y 2).
Let C be a categorical representation, and let A be a ﬁnite
/CZ -linear abelian category. We can
endow C ⊗
/CZ
A with a structure of a categorical representation, by settin g ( C ⊗
/CZ
A)µ = Cµ ⊗
/CZ
A,
deﬁning Chevalley functors Ei
/BD
µ ⊗ /BD
A, etc. If C is a simple categoriﬁcation, then clearly C ⊗
/CZ
A is
an isotypic categoriﬁcation. Conversely, we have:
Lemma 3.5. Let C be an isotypic categoriﬁcation of type λ ∈ X+. Then there exists an abelian
category A such that C ∼
= L(λ) ⊗
/CZ
A.
Proof. Since C is an isotypic categoriﬁcation, so is C−proj. By Rouquier’s Jordan-H¨ older series for
additive categoriﬁcations [41, Theorem 5.8], there exists an additive /CZ -linear category M such that
C−proj ∼
= (L(λ)−proj ⊗
/CZ
M)i.
Note that no ﬁltration appears here since, in the notation of [41], ( C−proj)lw
−λ = (C−proj)−λ.
Let {Pi} (respectively {Qj}) be a complete list of the projective indecomposable object s of L(λ)
(respectively M). Let P = ⨁
i,jPi ⊗Qj, and let B = End C(P )op. By Morita theory, B−mod ∼
= C.
On the other hand,
B ∼
= EndL(λ)(
⨁
i
Pi)op ⊗ EndM(
⨁
j
Qj)op.
Since L(λ) ∼
= EndL(λ)(⨁
iPi)op−mod we have the desired result with A = End M(⨁
jQj)op−mod.
□
Theorem 3.6. Let C be a categorical representation of Uq(g). Then there exists a ﬁltration by
Serre subcategories
0 = C0 ⊂ C1 ⊂ · · · ⊂ C n = C, (3.7)
such that for each i: Ci is a subrepresentation of C, Ci/Ci−1 is a simple categoriﬁcation of type
λi ∈X+, and the list of highest weights is weakly increasing so that λi ≺λj =⇒i<j .
Proof. The g-crystal Irr(C) is isomorphic to a ﬁnite direct sum of irreducible crystals B(λ) for
variousλ, i.e. we have an isomorphism
Irr(C) ∼
=
⨁
λ∈X+
B(λ)⊕mλ,
where mλ ≥ 0 and only ﬁnitely many are nonzero.
Deﬁne M = {λ ∈ X+ | mλ ⁄= 0 }, and let λ ∈ M . We claim that there exists a highest weight
simple object L ∈ C λ. Indeed, otherwise for any simple object L ∈ C λ there exists i ∈I such that
Ei(X) ⁄= 0. This implies that soc( Ei(X)) ⁄= 0, and by Proposition 3.4 we conclude that Irr(C) has
no highest weight elements of weight λ, a contradiction.
CATEGORICAL BRAID GROUP ACTIONS AND CACTUS GROUPS 9
Now take λ ∈M which is minimal with respect to ≼ , and let L ∈ C λ be a highest weight object.
Let C1 be the Serre subcategory of C generated by objects
{Fi1 · · ·Fiℓ(L) |ij ∈I,ℓ ≥ 0}. (3.8)
By the exactness and bi-adjunction of the Chevalley functor s, C1 is a subrepresentation of C.
Moreover it categoriﬁes L(λ). Indeed, by our choice of λ there cannot be any highest weight
objects with weight ≺λ occuring in C1, and by construction the only simple object in ( C1)λ is L.
Next consider the categorical representation C/C1 and repeat this construction. This produces
a Serre subcategory C′
2 ⊂ C/C1 which is again a simple categoriﬁcation. Let π : C → C /C1 be the
natural quotient functor, and deﬁne C2 =π−1(C′
2). Clearly, we have that C1 ⊂ C 2, C2 is Serre, it is
a subrepresentation, and C2/C1 ∼
= C′
2 is a simple categoriﬁcation.
Iterating this process produces a ﬁltration of C such that each composition factor is a simple
categoriﬁcation, and the highest weights of the subquotien ts are weakly increasing. □
Remark 3.9. Note that the construction in the proof of Theorem 3.6 can pro duce also an isotypic
ﬁltration with similar properties. Namely, if λ1,...,λ N is a list of the distinct isotypic types
appearing in [ C]C(q), and we choose any ordering of this list so that λi ≺λj =⇒i < j, then there
is a ﬁltration 0 = C′
0 ⊂ C ′
1 ⊂ · · · ⊂ C ′
N = C such that C′
k/C′
k−1 categoriﬁes the isotypic component
of [ C]C(q) of highest weight λk. To construct this isotypic ﬁltration, consider the Jordan -H¨ older
ﬁltration from the theorem. From the proof of Theorem 3.6, it ’s easy to see that one can ensure that
the subquotients which categorify the same simple represen tations appear in sequence. Assuming
then that our Jordan-H¨ older ﬁltration satisﬁes this property, a coarsening of it is the desired isotypic
ﬁltration.
Remark 3.10. Note that one can read oﬀ the isotypic ﬁltration of C from the crystal structure on
Irr(C). Indeed, suppose that Irr(C) decomposes into components
Irr(C) = X(λ1) ⊔ · · · ⊔ X(λN ),
where λ1,...,λ N ∈ X+ are distinct dominant integral weights, and X(λi) is a disjoint union of
copies of B(λi). Further, we arrange the weights as above so that λi ≺λj =⇒i<j . Let Ci be the
Serre subcategory of C generated by simple objects L such that [L] ∈ X(λj), where j ≤i. Then it
follows from Remark 3.9 that {0} ⊂ C 1 ⊂ C 2 ⊂ · · · ⊂ C N is an isotypic ﬁltration of C.
