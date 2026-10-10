---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-031-32-compatible-unitary-coboundary-weak-hopf-algebra
section_title: "Compatible unitary coboundary weak Hopf algebras Uq(g) → AW (g, q, ℓ)"
section_number: 32
pages: 194-204
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
---
32. Compatible unitary coboundary weak Hopf algebras Uq(g) → AW (g, q, ℓ)
The aim of this section is to prove Theorem 2.5 stated in Sect. 2. The proof is divided
in three parts. In Theorem 32.6, we introduce a full strict tensor category Gq generated
tensorially by the fundamental representation V equivalent to C(g, q, ℓ). We define Wenzl
functor W : G˜
q → Vec on an equivalent concrete realization G˜q of Gq, in Def. 32.7. In
Theorems 32.12, 32.16 we construct a natural weak tensor structure on W and study the
algebraic and unitary aspects, respectively. In particular, the algebraic Theorem 32.12
considers more general roots of unity, and we hope it will be useful in other circumstances,
discussed in [161].
Our first aim is to construct a natural functor W : C(g, q, ℓ) → Vec associated to the
same dimension function D as in Sect. 19, and thus this functor is a particular case of the
former.
To do this, we consider the tensor structure of C(g, q, ℓ) (q not necessarily minimal)
of [185]. This gives rise to the mentioned forgetful functor W, and we shall construct
a natural weak tensor structure on W, and in this way we have a canonical weak Hopf
algebra AW (g, q, ℓ).
When q is a minimal root of unity, the work of [185] implies that Uq(g) is a Hermitian
coboundary Hopf algebra with compatible involution (in a topological sense), see Theorem
31.9. This Hermitian structure underlies the unitary structure of C
+(g, q, ℓ).
To ease notation we shall write R
U
∆(I) in place of π ⊗ π(R
U
)∆(I), and we shall use a
similar notation for other elements of AW (g, q, ℓ) ⊗ AW (g, q, ℓ) that come from elements of
Uq(g)⊗Uq(g).

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 195
Remark 32.1. Note that by the presence of the factor ∆(I), the element ∆(v)
1/2
involved
in (2.2) is diagonal on the irreducible components, and acts as q
−
⟨γ,γ+2ρ⟩
2 on an irreducible
component of highest weight γ.
The weak tensor structure is not unique but when we change it then the weak Hopf
algebra changes only by a trivial twist. The special case g = slN will be useful for the
construction of tensor equivalences studied in Sect. 25. We also note that in this case we
recover the example constructed in [25] with a different method.
Recall that the quotient category C(g, q, ℓ) was outlined in Sect. 19. We assume ℓ
′ < ∞.
Remark 32.2. By Lemma 1.1 in [70], composition of inclusion T
0 → T(g, q, ℓ) with projection T(g, q, ℓ) → C(g, q, ℓ) is an equivalence of linear categories. Hence T
0 becomes
a semisimple tensor category tensor equivalent to C(g, q, ℓ). In the following subsection
we shall construct among other things a specific tensor structure of a certain interesting equivalent full subcategory Gq ⊂ T
0 making Gq → C(g, q, ℓ) an equivalence of tensor
categories.
32.1. A specific construction, the weak Hopf algebras AW (g, q, ℓ). In this subsection
q is any root of unity of order in the sense of Def. 19.1. We obtain a functor C(g, q, ℓ) → Vec
together with a weak tensor structure (F, G) associated to the same dimension function D
as in the previous subsection, and correspondingly a weak Hopf algebra AW (g, q, ℓ). In the
next subsection we consider the case where q is a minimal root. For this construction we
mostly take into consideration ideas in [185] that we review and extend to a general root
of unity q such that ℓ is in the sense of Def. 19.1. When q is a minimal root, AW (g, q, ℓ)
becomes a unitary coboundary weak Hopf algebra. To do this, as briefly anticipated in
Remark 32.2, we shall introduce a linear category Gq of non-negligible tilting modules
associated to a fundamental representation of g. This category appears implicitly in [185].
In [25] we have shown that Gq has a natural structure of a strict (ribbon) tensor category
when Vec is regarded as strict and q is a minimal root and is unitarily ribbon equivalent
to C(g, q, ℓ). In this subsection we extend this to roots of order in the sense of Def. 19.1
and moreover we shall define a functor W : Gq → Vec and then introduce a weak tensor
structure on W that corresponds by Tannakian reconstruction to AW (g, q, ℓ).
We keep the notation of the previous section. Let
pλ,γ : Vλ ⊗ V → Vγ ⊗ C
mγ
, λ, γ ∈ Λ
+(q)
denote Wenzl idempotents defined in (31.4).
Definition 32.3. We define the projection p2 := P
γ∈Λ+(q)
pκ,γ and set V ⊗V = p2V ⊗ V .
We use pλ,γ to iteratively define projections pn : V
⊗n → V⊗n onto the maximal nonnegligible submodule V
⊗n
induced by the decomposition of V
⊗n−1 ⊗ V .
Remark 32.4. By the iterative argument in the construction, every representation V
⊗n
has a canonical decomposition into irreducible subrepresentations V
(n)
γ,j , where γ denotes
the highest weight of V
(n)
γ,j and j counts the multiplicity up to isomorphism.

196 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Definition 32.5. Let Gq denote the completion with idempotents and direct sums of the
full linear subcategory of T(g, q, ℓ) with objects the truncated tensor powers V
⊗n
.
Thus by construction Gq is a semisimple linear category, that we regard it as an abstract
category. Let Vec be realized as a strict tensor category. We regard V
⊗n as a summand
on V
⊗n via pn, and identify the morphism space (V⊗m, V ⊗n
) in Gq with the subspace of
morphisms T ∈ (V
⊗m, V ⊗n
) in T(g, q, ℓ) satisfying T pm = pnT = T. We set
V
⊗m⊗V
⊗n
:= V
⊗m+n
, (32.1)
S⊗T := pm′+n′ ◦ S ⊗ T ◦ pm+n, S ∈ (V
⊗m, V ⊗m′
), T ∈ (V
⊗n
, V ⊗n
′
). (32.2)
Theorem 32.6. With the above tensor product and trivial associativity morphisms Gq,
becomes a ribbon strict ribbon tensor category ribbon tensor equivalent to C(g, q, ℓ).
The previous theorem is essentially in [185], perhaps the strictness property was noticed
in Theorem 5.4 in [25]. This property plays a role in our proof of Theorem 2.11, in Sect.
33. Moreover, we describe the equivalence in this section, see Remark 32.13. We next
introduce a concrete version of Gq.
Definition 32.7. Let G˜
q denote the full representation subcategory of T(g, q, ℓ) with objects representations which are finite direct sums of summands of the representations V
⊗n
.
Then G˜
q is also a linear semisimple category. There is a canonical linear equivalence
G˜
q → Gq
taking the summand P
(n)V⊗n of V
⊗n defined by an idempotent P(n)
regarded as an object
of G˜
q to P
(n)
regarded as an object of Gq and acting trivially on morphisms. We shall make
G˜
q into a tensor category with a tensor structure (G˜q, ⊠, α) in such a way that E becomes
a tensor equivalence (E, E).
Let then
W : G˜
q → Vec
be the forgetful functor. To define a tensor structure on G˜
q we first define linear maps
(Fλ,µ, Gλ,µ) on W defined on pairs (λ, µ) ∈ Λ
+(q) × Λ+(q) that will correspond to a tensor
structure (⊠, α) of G˜
q and subsequently also to a weak tensor structure for W.
For every λ ∈ Λ
+(q) choose an integer nλ such that λ appears as the dominant weight
of a summand Vλ of V
⊗nλ as observed in Remark 32.4. Let pλ : V
⊗nλ → Vλ denote the
corresponding idempotent onto Vλ for each λ ∈ Λ
+(q). In the following formulae we extend
pλ to V
⊗nλ in a trivial way on (1 − pnλ
)V
⊗nλ .
Proposition 32.8. We have that pλ⊗pµ = pnλ+nµ pλ ⊗ pµpnλ+nµ
is an idempotent in the
semisimple category G˜
q onto a module isomorphic to a maximal non-negligible submodule
of Vλ ⊗ Vµ in T(g, q, ℓ).
Proof. Notice that pλ⊗pµ is a morphism in T(g, q, ℓ) and is an idempotent by (2) in Subsect. 19.6 with range in the semisimple part V
⊗(nλ+nµ)
, thus this range is a semisimple

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 197
representation depending only on λ, µ up to isomorphism. If Mλ,µ is a maximal idempotent onto a nonnegligible summand of pλV
⊗nλ ⊗ pµV⊗nµ then pλ⊗pµ = pnλ+nµMλ,µpnλ+nµ
.
We have that T = pnλ+nµMλ,µ ∈ (Mλ,µ, pnλ+nµ) and T
−1 = Mλ,µpnλ+nµ ∈ (pnλ+nµ
, Mλ,µ)
satisfy T
−1T = Mλ,µ and T T −1 = pλ⊗pµ. □
We define Vλ⊠Vµ := pnλ⊗pµV
⊗(nλ+nµ) as a module of G˜
q, thus W(Vλ⊠Vµ) = pnλ+nµ pλ⊗
pµV
⊗(nλ+nµ) as a linear space.
Definition 32.9. For λ, µ ∈ Λ
+(q), let
Fλ,µ : Vλ ⊗ Vµ → Vλ ⊠ Vµ, Gλ,µ : Vλ ⊠ Vµ → Vλ ⊗ Vµ
be the morphisms in T(g, q, ℓ) respectively defined as the restriction of pλ⊗pµ = pnλ+nµ pλ⊗
pµpnλ+nµto Vλ ⊗ Vµ and that of pλ ⊗ pµ to Vλ ⊠ Vµ. Thus we have linear maps
Fλ,µ : W(Vλ) ⊗ W(Vµ) → W(Vλ ⊠ Vµ), Gλ,µ : W(Vλ ⊠ Vµ) → W(Vλ) ⊗ W(Vµ).
Proposition 32.10. We have that Fλ,µGλ,µ = 1 and Gλ,µFλ,µ is an idempotent of T(g, q, ℓ)
onto a maximal non-negligible submodule of Vλ ⊗ Vµ.
Proof. The first statement is again a simple consequence of (2) in Subsect. 19.6 the remaining part follows from this and Prop. 32.8. □
We next extend ⊠ and Fλ,µ, Gλ,µ to all objects of G˜
q. Let P
(n) ∈ (V⊗n
, V ⊗n), P
(m) ∈
(V
⊗m, V ⊗m) be idempotents in Gq and consider morphisms describing decomposition into
irreducibles, that is
Sλ,j : Vλ → P
(n)V⊗n
, S′
λ,j : P
(n)V⊗n → Vλ,
Tµ,k : Vµ → P
(m)V⊗m, T′
µ,k : P
(m)V⊗m → Vµ,
S
′
λ,jSλ′
,j′ = δ(λ,j),(λ′
,j′)
,
X
λ,j
Sλ,jS
′
λ,j = P
(n)
,
T
′
µ,kTµ′
,k′ = δ(µ,k),(µ′
,k′)
,
X
µ,k
Tµ,kT
′
µ,k = P
(m)
.
We set
FP(n)V
⊗n,P(m)V
⊗m =
X
λ,j,µ,k
Sλ,j⊗Tµ,k ◦ Fλ,µ ◦ S
′
λ,j ⊗ T
′
µ,k, (32.3)
P
(n)V⊗n ⊠ P
(m)V⊗m = FP(n)V
⊗n,P(m)V⊗n (P
(n)V⊗n ⊗ P
(m)V⊗m) (32.4)
and we let GP(n)V
⊗n,P(m)V⊗m be the restriction of
X
λ,j,µ,k
Sλ,j ⊗ Tµ,k ◦ Gλ,µ ◦ S
′
λ,j⊗T
′
µ,k (32.5)
to P
(n)V⊗n ⊠ P(m)V⊗m. Notice that FP(n)V
⊗n,P(m)V
⊗m and GP(n)V⊗n,P(m)V⊗m are independent of the choice of Sλ,j , S
′
λ,j , Tµ,k, T
′
µ,k by bilinearity of ⊗. In particular, these maps and
tensor products extend the previous ones on the chosen class of irreducibles. Finally, we
extend this structure to any object of G˜
q by bilinearity.

198 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Remark 32.11. It follows that Fλ,µ, Gλ,µ of Def. 32.9 and Prop. 32.10 are morphisms of
the tilting category onto a maximal non-negligible addendum. This property extends to
all pairs of objects of G˜
q in place of Vλ and Vµ. Note that this property is not needed in
the definition of weak quasi-tensor structure, but it turns out useful to construct the weak
Hopf algebra of this section. Moreover, this flexibility of the notion of weak quasi-tensor
structure will turn out useful in Sect. 33, where we shall construct a strongly unitary weak
quasi-tensor structure (F0, F∗
0
) for the Zhu algebra AVgk
associated to an affine VOA for
a suitable positive integer k that is a morphism for the action of the simple Lie algebra g
via a twist that is not a morphism of the tilting category.
We next define a tensor product between morphisms and associativity morphisms in G˜
q
as follows. Let ρ, σ, τ be objects of G˜
q. For S : ρ → ρ
′
, T : σ
′ → σ′
, set
S ⊠ T = Fρ
′
,σ′S ⊗ T Gρ,σ. (32.6)
We endow G˜
q with associativity morphisms
αρ,σ,τ = Fρ,σ⊠τ ◦ 1ρ ⊗ Fσ,τ ◦ Gρ,σ ⊗ 1τ ◦ Gρ⊠σ,τ (32.7)
Note that the maps F and G are defined up to varying the choice of the integers nλ or
the definition of the idempotents pn.
Theorem 32.12. Let g be a complex simple Lie algebra, q a complex root of unity such
that q
2 has order ℓ in the sense of Def. 19.1. Then
a) (G˜
q, ⊠, α) is a semisimple tensor category,
b) the canonical linear equivalence E : G˜
q → Gq admits a unique structure of tensor
equivalence (E, E) : (G˜
q, ⊠, α) → (Gq, ⊗, 1) such that
Eλ,µ : E(Vλ)⊗E(Vµ) → E(Vλ ⊠ Vµ), λ, µ ∈ Λ
+(q)
acts as Fλ,µ and we have that E
−1
λ,µ acts as Gλ,µ,
c) the pair (F, G) is a weak tensor structure for the forgetful functor W : G˜
q → Vec,
therefore AW (g, q, ℓ) = Nat0(W) is a ribbon weak Hopf algebra,
d) a different choice of pn, pλ changes AW (g, q, ℓ) by a trivial twist.
Proof. a) Note that S ⊠ T is composition of morphisms in T(g, q, ℓ) with domain and
range representations of G˜
q, thus it is a morphism in G˜q. By Remark 32.11, for any pair
of objects ρ, σ ∈ G˜
q, Gρ,σFρ,σ is an idempotent in T(g, q, ℓ) with range a maximal nonnegligible summand of the tensor product tilting module ρ ⊗ σ. Thus 1 − Gρ,σFρ,σ is an
idempotent onto the negligible summand. This observation together with property (2) in
Subsect. 19.6 implies that ⊠ is a bifunctor of G˜
q. The pentagon equation can be shown
again taking into account property (2) and we also need (3). For example computing the
short side of the pentagon equation (4.1)
αν,ρ,στανρ,σ,τ =
Fν,ρ(στ) ◦ 1ν ⊗ Fρ,στ ◦ Gν,ρ ⊗ 1στ ◦ Gνρ,στFνρ,στ ◦ 1νρ ⊗ Fσ,τ ◦ Gνρ,σ ⊗ 1τ ◦ G(νρ)σ,τ

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 199
we may first eliminate the central term Gνρ,στFνρ,στ , then use the commutation relation
Gν,ρ ⊗ 1στ ◦ 1νρ ⊗ Fσ,τ = 1νρ ⊗ Fσ,τ ◦ Gν,ρ ⊗ 1στ
thus
αν,ρ,στανρ,σ,τ = Fν,ρ(στ) ◦ 1ν ⊗ Fρ,στ ◦ 1νρ ⊗ Fσ,τ ◦ Gν,ρ ⊗ 1στ ◦ Gνρ,σ ⊗ 1τ ◦ G(νρ)σ,τ .
The computation involving the long side of the pentagon equation is slightly longer because
of the use of ⊠ at both sides. However it can patiently be carried out and it leads to
equating the left hand side. b) It is clear that Eλ,µ and E
−1
λ,µ are morphisms and are inverse
of each other. Furthermore extending these morphisms by naturality to every pair of
objects we see that they act as F and G respectively. Then we may verify the tensoriality
equation (4.6) for (E, E). To do this, notice that the tensor product ⊗ at right hand side
of (4.6) modifies ⊗ by inserting suitable idempotents pn which may then be disregarded
thanks to (2) again. c) Naturality of F and G as transformations from G˜ → Vec may be
checked with direct computation. Notice also that by construction F and G are natural
as transformations Gq → Vec, therefore by composition G˜
q → Gq → Vec we find that they
are also natural with respect to ⊠. Property d) follows again from (2).
□
Remark 32.13. It follows from part b) of the previous theorem that the composition
Q : G˜
q → T(g, q, ℓ) → C(g, q, ℓ)
of the natural inclusion followed by quotient is an equivalence of tensor categories. In
this way, G˜
q admits a unique structure of a ribbon category in a way that Q is a ribbon
equivalence. On the other hand, this can also be seen directly.
32.2. Unitary coboundary structure of AW (g, q, ℓ). In this subsection we consider the
case of unitary structures, thus we assume that q = e
iπ/ℓ is a minimal root of order in the
sense of Def. 19.1 and we study the unitarity property of AW (g, q, ℓ). Note that by Remark
31.1, most of the constructions hold for non-minimal roots of this kind of order.
We recall from Theorem 31.9 that Uq(g) is a (topological) Hermitian coboundary Hopf
algebra with compatible involution and antipode of Kac type. Furthermore recall also that
by Prop. 2.4 in [185], for λ ∈ Λ
+(q) the natural Hermitian form of Vλ in the sense of Sect.
14 is a positive definite inner product, so Vλ is a C
∗
-representation of Uq(g).
Definition 32.14. Let TW denote the full subcategory of T(g, q, ℓ) with objects orthogonal
direct sums of summands defined by selfadjoint idempotents of finite tensor products of
Vλ with λ ∈ Λ
+(q) endowed with the non-degenerate Hermitian form induced by iterates
of R of Uq(g).
Consider a finite tensor product W of Vλ with λ ∈ Λ
+(q) endowed with the nondegenerate Hermitian form induced by iterates of R of Uq(g), or more generally a an
orthogonal direct sum of summands defined by selfadjoint idempotents of a module of
this kind such that the form is nondegenerate on W. For any morphism T : W → W ′

200 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
of TW , the adjoint T
∗
: W′ → W is well defined. We next consider in particular the
canonical decomposition into indecomposable tilting modules recalled in the previous subsection Vλ ⊗ V = ⊕γTγ ⊗ C
mγ
. The Hermitian form induced by R is positive definite on
the on the isotypic component Tγ ⊗ C
mγ = Vγ ⊗ Cmγ
for γ ∈ Λ
+(q). The idempotents
pλ,γVλ ⊗ V → Vγ ⊗ C
mγ are selfadjoint with respect to this inner product. It follows that
the iterated tensor powers V
⊗n are Hilbert space representations of Uq(g) with this iterated
Hermitian form. Let Gℓ denote the completion under selfadjoint idempotents and orthogonal direct sums of the full subcategory of T(g, q, ℓ) with objects V
⊗n
. Thus Gℓ has the
structure of a linear semisimple C
∗
-category. Furthermore with tensor product ⊗ defined
as in the previous subsection, Gℓ becomes a unitary strict tensor category.
Proposition 32.15. The idempotents pλ and pλ⊗pµ are selfadjoint in Gℓ.
Proof. Notice that for all n, the idempotents say pγ,j onto the irreducible decomposition
V
(n) by the V
(n)
γ,j described in Remark 32.4 have pairwise orthogonal ranges with respect
to the inner product by orthogonality of the addenda of Vλ ⊗ V with dominant weights in
Λ
+(q) and the iterative construction of V⊗n
. It follows in particular that pλ are selfadjoint
idempotent in Gℓ. Let c
w(λ, µ) be the coboundary operators in T(g, ℓ, q) associated to the
R matrix of Uq(g). By naturality we have pλ ⊗ pµc
w(µ, λ) = cw(µ, λ)pµ ⊗ pλ, and thus R
commutes with pλ ⊗ pµ. It follows that pλ ⊗ pµ is selfadjoint with respect to the iterated
Hermitian form of V
⊗nλ+nµ , and therefore also pλ⊗pµ are selfadjoint. □
We then similarly introduce the concrete category G˜
ℓ of T(g, q, ℓ) taking into consideration summands defined by selfadjoint idempotents and orthogonal direct sums. By
the previous proposition, for λ, µ ∈ Λ
+(q), Fλ,µ and Gλ,µ introduced as in the previous
subsection are morphisms in TW and satisfy in addition the property F
∗
λ,µ = Gλ,µ. Using
orthogonal decompositions of objects of G˜
ℓ
, we obtain natural transformations Fρ,σ, Gρ,σ as
in (32.3), and (32.5), satisfying F
∗
ρ,σ = Gρ,σ in TW . Then we introduce in G˜
ℓ the structure
of a tensor category (G˜
ℓ
, ⊠, α) as in (32.4), (32.6), and (32.7). Finally, we consider the
forgetful functor,
W : G˜
ℓ → Hilb
and is a ∗-functor endowed with the weak tensor structure (F, G) regarded with values in
Hilb. (Notice that as natural transformations of W, we do not have F
∗
ρ,σ = Gρ,σ, more
details will be discussed in the proof of the following result.)
Theorem 32.16. Let q be a minimal root of order in the sense of Def. 19.1, then
a) (G˜
ℓ
, ⊠, α) is a unitary semisimple tensor category and the tensor equivalence (E, E) :
(G˜
ℓ
, ⊠, α) → (Gℓ, ⊗, 1) is unitary,
b) AW (g, q, ℓ) = Nat0(W) becomes a unitary coboundary weak weak Hopf algebra with
compatible involution, weak tensor structure defined by (F, G) and antipode of Kac
type such that Gℓ → Rep(AW (g, q, ℓ)) is a unitary equivalence of ribbon categories.
Proof. a) The property (S ⊠ T)
∗ = S∗ ⊠ T∗
follows from the relation F
∗ = G in TΛ+(q) and
arguments similar to those in the proof of Prop. 32.15. Unitarity of the associator follows

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 201
from F
∗ = G and (2), and (3). b) By theorem Theorem 29.1 we need to show (29.1) and
(29.2). We only show the former. By Remark 29.3 a), it is enough to do this for ρ = V
⊗n
,
σ = V . In this case Fρ,σ = pn+1 as (1 − pn) ⊗ 1V is negligible. This follows by construction
as F
∗
ρ,σ = p
∗
n+1R = Rpn+1 where p
∗
n+1 is the adjoint with respect to the standard inner
product of V
⊗n ⊗ V . We next show that AW (g, q, ℓ) has an antipode of Kac type. It is
shown in the proof of Lemma 10.4 in [25] that a solution of the conjugate equations in Gℓ
is of the form (14.2) with α = β = I, µi = 1. It follows from the proof of Theorem 7.6 that
the corresponding antipode is strong and therefore of Kac type. The proof of compatibility
with the ∗-involution is the content of the following lemmas 32.17, 32.18, 32.19.
□
Lemma 32.17. Let cU (ρ, σ) be the natural coboundary symmetry associated to Uq(g). Then
the unitary coboundary weak Hopf algebra AW has compatible ∗-involution if and only if
cU (Vλ, V ⊗k)GVλ,V ⊗k FVλ,V ⊗k cU (V
⊗k
, Vλ) = GV
⊗k
,Vλ
FV
⊗k
,Vλ
λ ∈ Λ
+(q), k = 1, 2.
(32.8)
It suffices that the following two equations involving the braided symmetries cU and c
−1
U
associated to Uq(g) and also the braided symmetries c and c
−1 associated to AW , hold,
c(Vλ, V ⊗k
)FVλ,V ⊗k cU (Vλ, V ⊗k)
−1 = FV
⊗k
,Vλ
, λ ∈ Λ
+(q), k = 1, 2, (32.9)
c(V
⊗k
, Vλ)
−1FVλ,V ⊗k cU (V
⊗k
, Vλ) = FV
⊗k
,Vλ
, λ ∈ Λ
+(q), k = 1, 2. (32.10)
Proof. Taking the adjoint of equations (32.9), (32.10) and multiplying them term by term
we get
cU (Vλ, V ⊗k)GVλ,V ⊗k FVλ,V ⊗k cU (Vλ, V ⊗k)
−1 = GV
⊗k
,Vλ
FV
⊗k
,Vλ
λ ∈ Λ
+(q), k = 1, 2.
(32.11)
cU (V
⊗k
, Vλ)
−1GVλ,V ⊗k FVλ,V ⊗k cU (V⊗k
, Vλ) = GV
⊗k
,Vλ
FV
⊗k
,Vλ
λ ∈ Λ
+(q), k = 1, 2.
(32.12)
In turn it follows that c
2
U
commutes with GV
⊗k
,Vλ
FV
⊗k
,Vλ
. It follows that the principal
branch square root commutes also, and this implies (32.8).
We next show the first statement. By Prop. 30.2, compatibility of the ∗-involution is
equivalent to ∆op(I) = ∆(I)
∗ on the spaces of V⊗k ⊗ Vλ and Vλ ⊗ V⊗k
for k = 1, 2.
We have ∆(I)
∗ = R
U
∆(I)(R
U
)
−1
, and it follows that the desired equalities reduce to our
assumptions. Note that equation (32.8) together with the coboundary property c
2
U = 1,
see Prop. 31.7, d), imply that the symmetric equation with Vλ on the right and V
⊗k on
the left at the l.h.s. of the equation holds and this completes the proof. □
Lemma 32.18. The natural transformation F defining AW satisfies equations (32.9),
(32.10) for k = 1.
Proof. Assume g ̸= E8. For k = 1, by [185], V ⊗Vλ is completely reducible into irreducible
components ⊕µmµVµ (with multiplicity 0 or 1 except for g = F4 where µµ > 1 only for
µ = λ) and we have that µ ∈ Λ+(q). Thus there is a unique morphism idempotent

202 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
onto a maximal non-negligible submodule V ⊗ Vλ → ⊕µ∈Λ+(q)Vµ which then coincides
with FV,Vλ. This uniqueness property and unitarity of the braided symmetries imply that
(32.9), (32.10) hold for k = 1. The case g = E8 is more delicate that the others, and is
not covered by the above proof. In this case we consider the decomposition of Vλ ⊗ V
and of V ⊗ Vλ into indecomposable tilting modules given at page 274 in [185]. Let FVλ,V
and FV,Vλ be the corresponding idempotents onto the maximal non-negligible submodules.
Then it follows from the proof therein and unitarity of the braided symmetry, that (32.9),
(32.10) hold in this case. More precisely, we consider Wl = Vλ ⊗ V considered in the
mentioned proposition of [185] and we pair it with Wr = V ⊗ Vλ, thus Wlis W in [185].
Similarly, for the submodules of Wl and Wr we follow the same notation, with an addition
of a subscript l or r, for example Ml = (pλ + pλ+k)Wl and Mr = (pλ + pλ+k)Wr. The
braiding cU intertwines Wl with Wr, and therefore also Ml with Mr, as each addendum
isomorphic to some Vµ(q) with µ ̸= λ has multiplicity 1. Moreover Ml and Mr contain
a submodule isomorphic to Vλ+κ(q). We note that these submodules, that we denote by
Vλ+κ(q)l and Vλ+κ(q)r are generated by the (λ + k)-weight space, that is one dimensional,
thus cU takes Vλ+κ(q)l to Vλ+κ(q)r. Moreover cU is unitary. It follows from these two facts
that choosing T(q)r = cU T(q)l, cU takes (Mλ)l to (Mλ)r, and therefore cU (pλ)l = (pλ)rcU
and cU (pλ+κ)l = (pλ+κ)rcU . Note that T(q) involve a choice. More in detail, T(q)/Vλ+κ
complements the submodule N(q)
⊥/Vλ+κ(q) of M(q)/Vλ+κ(q) (this is semisimple). By the
property of c, we may choose T(q)r = cT(q)l. □
Lemma 32.19. The natural transformation F defining AW satisfies equations (32.9),
(32.10) for k = 2 and all Lie types.
Proof. We use the weak Hopf property in categorical form (4.6), (4.7). Working with Vec
strict,
F(αVλ,V,V ) = FVλ,V ⊗V ◦ 1⊗FV,V ◦ GVλ,V ⊗1 ◦ GVλ⊗V,V , (32.13)
F(αVλ,V,V )
−1 = FVλ⊗V,V ◦ FVλ,V ⊗1 ◦ 1⊗GV,V ◦ GVλ,V ⊗V , (32.14)
F(αV,V,Vλ) = FV,V ⊗Vλ◦ 1⊗FV,Vλ◦ GV,V ⊗1 ◦ GV ⊗V,Vλ, (32.15)
F((αV,V,Vλ)
−1
) = FV ⊗V,Vλ
◦ FV,V ⊗1 ◦ 1⊗GV,Vλ◦ GV,V ⊗Vλ. (32.16)
We set
F˜
1,2 := FVλ,V ⊗V ◦ 1⊗FV,V ,
G2,1 = GVλ,V ⊗1 ◦ GVλ⊗V,V ,
F2,1 = FVλ⊗V,V ◦ FVλ,V ⊗1,
G˜
1,2 = 1⊗GV,V ◦ GVλ,V ⊗V .
F
′
1,2 = FV,V ⊗Vλ
◦ 1⊗FV,Vλ
,
G˜′
2,1 = GV,V ⊗1 ◦ GV ⊗V,Vλ
,

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 203
F˜′
2,1 = FV ⊗V,Vλ
◦ FV,V ⊗1,
G
′
1,2 = 1⊗GV,Vλ
◦ GV,V ⊗Vλ
.
Note that by Lemma 32.18, naturality of all the transformations and the braiding, and
the two hexagonal equations (5.8), (5.9), the map G2,1, (F2,1 resp.), is conjugate to G′
1,2
,
(F
′
1,2
resp.) via a specific braiding (that is the representative of the braid group element
b1b2b1 = b2b1b2 in the category) For example,
FV,V ⊗Vλ = c(V ⊗Vλ, V )FV ⊗Vλ,V cU (V ⊗Vλ, V )
−1
1⊗FV,Vλ = 1⊗c(Vλ, V ) ◦ 1 ⊗ FVλ,V ◦ 1 ⊗ cU (Vλ, V )
−1
imply
F
′
1,2 = c(V ⊗Vλ, V )c(Vλ, V ) ⊗ 1 ◦ F2,1 ◦ (1 ⊗ cU (Vλ, V )cU (V ⊗Vλ, V ))−1 =
c(V ⊗Vλ, V )c(Vλ, V ) ⊗ 1 ◦ F2,1 ◦ (cU (V ⊗Vλ, V )cU (Vλ, V ) ⊗ 1)−1
.
Multiplying together (32.13) and (32.14) and then (32.15) and (32.16) gives respectively
1 = F2,1 ◦ 1⊗GV,V ◦ PVλ,V ⊗V ◦ 1⊗FV,V ◦ G2,1, (32.17)
1 = F
′
1,2 ◦ GV,V ⊗1 ◦ PV ⊗V,Vλ
◦ FV,V ⊗1 ◦ G
′
1,2
. (32.18)
Conjugating (32.18) by the same braid group element gives
1 = F2,1 ◦ 1 ⊗ GV,V ◦ P
c
V ⊗V,Vλ
◦ 1 ⊗ FV,V ◦ G2,1, (32.19)
where
PVλ,V ⊗V = GVλ,V ⊗V FVλ,V ⊗V ,
P
c
V ⊗V,Vλ = cU (V ⊗V, Vλ) ◦ GV ⊗V,Vλ
◦ FV ⊗V,Vλ◦ cU (V ⊗V, Vλ)
−1
.
It follows from (32.17) and (32.19) that
0 = F2,1 ◦ 1 ⊗ GV,V ◦ A ◦ 1 ⊗ FV,V ◦ G2,1, (32.20)
where A = PVλ,V ⊗V − P
c
V ⊗V,Vλ
is a morphism of the tilting category may be regarded
a selfadjoint element of a C
∗
-algebra, hence it can be written as the difference of two
orthogonal positive operators still morphisms of the tilting category
A = A+ − A−, A+A− = A−A+ = 0.
Being G2,1F2,1 an idempotent onto a maximal non-negligible submodule, we have by the
Gelfand-Kazhdan properties (1)-(3) in Sect. 20
0 = F2,1 ◦ 1 ⊗ GV,V ◦ A+ ◦ 1 ⊗ FV,V ◦ G2,1F2,1 ◦ 1 ⊗ GV,V ◦ A− ◦ 1 ⊗ FV,V ◦ G2,1.
The right hand side (32.20) is selfadjoint, thus its square is positive. By the last equation,
the square takes the same form as (32.20) with A replaced by A2 = (A+)
2 + (A−)2
. Both
F2,1 ◦ 1 ⊗ GV,V ◦ A2
+ ◦ 1 ⊗ FV,V ◦ G2,1 and F2,1 ◦ 1 ⊗ GV,V ◦ A2− ◦ 1 ⊗ FV,V ◦ G2,1 are positive,
thus
0 = F2,1 ◦ 1 ⊗ GV,V ◦ A
2
+ ◦ 1 ⊗ FV,V ◦ G2,1, (32.21)
0 = F2,1 ◦ 1 ⊗ GV,V ◦ A
2
− ◦ 1 ⊗ FV,V ◦ G2,1 (32.22)

204 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Taking the categorical trace we have Tr(A2
+) = Tr(A2−) = 0, hence A+ = A− = 0 by the
C
∗
-property and it follows that A = 0, that is PVλ,V ⊗V = P
c
V ⊗V,Vλ
.
□
The following proposition concludes the proof of Theorem 2.5.
Proposition 32.20. Let R
U
be the coboundary associated to Uq(g) as in Theorem 31.9.
Then R
U
∆(I) is a 2-cocycle for the weak Hopf algebra AW (g, q, ℓ) as defined in Def. 9.12.
.
Proof. Formula (2.1) in the statement of Theorem 2.5 describes the relation between
the coproducts of Uq(g) and AW (g, q, ℓ). Using this relation with F = R
U
∆(I) F
−1 =
∆(I)(R
U
)
−1
the left hand side of the first displayed equation of Def. 9.12, becomes
1 ⊗ ∆(∆(I))[1 ⊗ ∆
U
((R
U
)
−1
)I ⊗ (R
U
)
−1RU ⊗ I∆U ⊗ I(R
U
)]∆ ⊗ 1(∆(I)),
with ∆Uthe coproduct of Uq(g) and ∆ that of AW (g, q, ℓ). By Theorem 31.9, R
U
is a
2-cocycle for Uq(g), thus the central part of this equation equals I ⊗ I ⊗ I, and the proof
of the first displayed formula of Def. 9.12 is complete. One similarly shows the second
formula. (Note that by Remark 32.1, see also Remark 31.11, the action of R
U
∆(I) on
Vλ(q) ⊗ Vµ(q) on a simple component of highest weight γ, with λ, µ, γ ∈ Λ
+(q) is given by
RUΘw, where Θw acts as q0
⟨λ,λ+2ρ⟩+⟨µ,µ+2ρ⟩−⟨γ,γ+2ρ⟩
2 .)
□
