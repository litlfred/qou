---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-003-4-preliminaries-on-tensor-categories-and-their-fun
section_title: "Preliminaries on tensor categories and their functors, generating object"
section_number: 4
pages: 23-32
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
---
4. Preliminaries on tensor categories and their functors, generating
object
In this section we recall the basic terminology concerning tensor categories and unitary
tensor categories. Our main references are [50, 137] and [141] respectively. We also give
the main definitions of certain functors between these categories. The most familiar notion
is that of tensor functor but we need suitable weak generalizations, known in the literature
as quasi-tensor functors and more importantly for us their weak versions, the weak quasitensor functors. We also introduce a new notion, that of weak tensor functor between
tensor categories as a slight generalisation of notions already considered in the literature.
We shall describe a cohomological interpretation in the setting of weak quasi-Hopf algebras
later on. Finally, we introduce a notion of unitarity for weak quasi-tensor functors between
unitary tensor categories and discuss a unitarization procedure for general weak quasitensor functors which will be fruitful later on.
All categories in this paper will be essentially small, thus they will admit a small skeleton.
The morphism space from an object ρ to σ is denoted by (ρ, σ). By a linear category C
we mean a category whose morphism spaces are complex vector spaces and such that
composition is bilinear.
The notion of semisimple category is central in this paper, we briefly recall the definition
directing our attention to linear categories, we refer the reader to Ch. 1 in [50] for details.
A linear additive category C is a linear category with a zero object 0, that is (0, 0) = 0,
and direct sums, that is for any pair of objects ρ, σ ∈ C there is an object τ ∈ C and
morphisms S ∈ (ρ, τ ), T ∈ (σ, τ ), S
′ ∈ (τ, ρ), T′ ∈ (τ, σ) such that S′S = 1, T′T = 1,
SS′ + T T′ = 1. The object τ is defined up to isomorphism and denoted ρ ⊕ σ. A linear
abelian category is a linear additive category with extra structure. The central additional

24 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
notion is that of kernel and symmetrically of cokernel of a morphism. For a morphism
A ∈ (ρ, σ) the kernel Ker(A) is an object k and a morphism K ∈ (k, ρ) such that AK = 0,
and universal with this property. Kernels and cokernels are assumed to exist for every
morphism, among other things. A subobject of an object ρ is an object σ together with a
morphism S ∈ (σ, ρ) with Ker(S) = 0. An object ρ is called simple, or irreducible, if ρ ̸= 0
and the only subobjects are 0 and ρ.
It follows from Schur’s Lemma, see e.g. Lemma 1.5.2 in [50] and Prop. 5.4.5 in [27]
that in a linear abelian category with finite dimensional morphism spaces, when ρ and σ
are simple, (ρ, σ) is either the trivial vector space or it is formed by scalar multiples of a
unique isomorphism, it follows that (ρ, ρ) = C1. In our paper, all our categories will have
finite dimensional morphism spaces.
A semisimple category is a linear abelian category such that every nonzero object is a
finite direct sum of simple objects, the decomposition is unique up to isomorphism.
A splitting idempotent, or a summand, of an object ρ is an object σ, an idempotent
E ∈ (ρ, ρ) together with morphisms S ∈ (σ, ρ), S
′ ∈ (ρ, σ) such that S′S = 1, SS′ = E. In
particular, σ is a subobject of ρ. For example, a direct sum ρ⊕σ as previously defined has
ρ and σ as summands defined by complementary idempotents. In a semisimple category
every idempotent splits, thus every subobject is a summand.
The next notion is that of tensor category. We follow Sect. 1.2 in [137], and the notion
of monoidal category of Ch. 2 in [50] except for we assume the linear structure.
Definition 4.1. By a pre-tensor category we mean a linear category C endowed with a
tensor product operation ⊗, which is a bilinear bifunctor C×C → C, a distinguished tensor
unit object ι satisfying the unit axioms, that is the functors ρ → ρ ⊗ ι and ρ → ι ⊗ ρ are
autoequivalences of C.
Definition 4.2. A tensor category is a pre-tensor category endowed with natural isomorphisms αρ,σ,τ : (ρ ⊗ σ) ⊗ τ → ρ ⊗ (σ ⊗ τ ).
The associativity morphisms αρ,σ,τ are required to satisfy the pentagon equation
((ρ ⊗ σ) ⊗ τ ) ⊗ υ
α

α⊗1
/(ρ ⊗ (σ ⊗ τ )) ⊗ υ
α /ρ ⊗ ((σ ⊗ τ ) ⊗ υ)
1⊗α

(ρ ⊗ σ) ⊗ (τ ⊗ υ) α
/ρ ⊗ (σ ⊗ (τ ⊗ υ))
(4.1)
By Sect. 2.9 in [50] one can identify ρ ⊗ ι and ι ⊗ ρ by a simple passage which uses only
the unit isomorphisms, in this way ι becomes strict, meaning that ι ⊗ ρ = ρ ⊗ ι = ρ for
every object and 1ι ⊗ T = T ⊗ 1ι = T for every morphism T. To simplify our discussion,
we shall assume that ι is strict in our abstract results, and we shall tacitly use this passage
in our applications where it is not natural to work with a strict unit, e.g. Sect. 22, 23.
Moreover, we assume the normalization condition αρ,ι,τ = 1.
Alternatively, one may adopt the definition of monoidal units originally given by Saavedra, following the treatment in [115]. This viewpoint has been adopted in [71]. (See also
Remark 25.2 for a brief description of the aims of the thesis and more closely related papers
in the setting of Kazhdan-Wenzl theory, Sect. 25.)

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 25
Here we just point out an interesting and quite handy feature: in terms of Saavedra
notion, a tensor functor F : C → C
′
is compatible with units exactly if it sends units into
units, or equivalently if it sends any one unit, say ι into a unit. Moreover, given any other
unit ι
′ of C′
, the compatibility is expressed by a unique isomorphism between ι
′ and F(ι).
We shall only deal with tensor categories for which the tensor unit satisfies (ι, ι) = C1.
The category is called strict if the tensor unit is strict and associativity morphisms are
identity. With abuse of language, we shall also regard the category Vec of finite dimensional
vector spaces as strict. Whenever convenient, for a given semisimple category C, we fix a
set Irr(C) of simple objects in C such that every simple object of C is isomorphic to exactly
one element of Irr(C). This can be done because we are assuming that C is essentially
small. A semisimple tensor category with finitely many inequivalent irreducible objects
will be called finite semisimple. If C is in addition rigid, it is a (complex) fusion category
[51].
The following definition will play an important role in our paper.
Definition 4.3. Let C be a semisimple pre-tensor category. An object ρ ∈ C is called
generating if every simple object of C is a summand of some tensor power of ρ defined by
some parenthesisation.
A tensor power of ρ is an object defined as the result of iterative applications of the
bifunctor ⊗ to pairs with entries ι or ρ. We define the order of a tensor power of ρ in
a natural way. Different parenthesisations of the same order of two tensor powers of ρ
are equivalent in a tensor category, thus it suffices to verify the generating property on a
preferred choice of parenthesisation in this case, and is independent of the choice of the
associativity morphisms.
Functors between linear categories are C-linear maps between morphism spaces.
Definition 4.4. A linear functor F : C → C
′ between linear categories is called a linear
equivalence if there is a linear functor, called a quasi-inverse, G : C
′ → C such that FG and
GF are naturally isomorphic to the identity functors of C
′ and C respectively.
Remark 4.5. It is well known (Theorem 1 in IV.4 of [123]) that a linear functor F : C → C
′
is a linear equivalence if and only if it is full and faithful (i.e. bijective between the
morphism spaces) and essentially surjective (every object of C
′
is isomorphic to one in
the image of F.) We shall use these definitions interchangeably. When C and C
′ are
semisimple, this is equivalent to the property that {F(ρ), ρ ∈ Irr(C)} is a complete set of
pairwise non-isomorphic simple objects in C
′
.
The following notion of weak quasi-tensor functor for a tensor category was introduced
by H¨aring-Oldenburg in [82] in connection with the study of duality for weak quasi-Hopf
algebras. We note that the definition ignores the associativity structure of C and C
′ and
thus is meanginful in the setting of pre-tensor categories.
Definition 4.6. Let C and C
′ be pre-tensor categories. A weak quasi-tensor functor is
defined by a C-linear functor F : C → C
′
satisfying F(ι) = ι together with two morphisms

26 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Fρ,σ : F(ρ) ⊗ F(σ) → F(ρ ⊗ σ) and Gρ,σ : F(ρ ⊗ σ) → F(ρ) ⊗ F(σ) satisfying
Fι,ρ = Fρ,ι = 1F(ρ), Gι,ρ = Gρ,ι = 1F(ρ), (4.2)
Fρ,σ ◦ Gρ,σ = 1F(ρ⊗σ) (4.3)
Fρ
′
,σ′ ◦ F(S) ⊗ F(T) = F(S ⊗ T) ◦ Fρ,σ, F(S) ⊗ F(T) ◦ Gρ,σ = Gρ
′
,σ′ ◦ F(S ⊗ T) (4.4)
for objects ρ, σ, ρ
′
, σ
′ ∈ C and morphisms S : ρ → ρ′
, T : σ → σ
′
.
Property (4.4) expresses naturality of F and G in ρ and σ, while the right inverse
condition (4.3) implies that
Pρ,σ = Gρ,σ ◦ Fρ,σ : F(ρ) ⊗ F(σ) → F(ρ) ⊗ F(σ) (4.5)
is an idempotent satisfying
Fρ,σ ◦ Pρ,σ = Fρ,σ, Pρ,σGρ,σ = Gρ,σ.
If Pρ,σ = 1F(ρ)⊗F(σ)for all ρ, σ (i.e. all Fρ,σ are isomorphisms), we recover the notion of
quasi-tensor functor of [47, 126].
Definition 4.7. Let F, F
′
: C → C
′ be two weak quasi-tensor functors between pretensor categories defined by (Fρ,σ, Gρ,σ), (F
′
ρ,σ, G′ρ,σ), respectively. A natural transformation
η : F → F
′
is called monoidal if ηι = 1ι and if
F
′
ρ,σ
◦ ηρ ⊗ ησ = ηρ⊗σ ◦ Fρ,σ, G′
ρ,σ
◦ ηρ⊗σ = ηρ ⊗ ησ ◦ Gρ,σ.
The following definition is motivated by the requirement of compatibility between the
functor and the associativity morphisms.
Definition 4.8. Let C and C
′ be tensor categories with associativity morphisms α and α′
respectively. A weak tensor functor is a weak quasi-tensor functor F : C → C
′
for which
the associated natural transformations Fρ,σ, Gρ,σ satisfy for all objects ρ, σ, τ ,
F(αρ,σ,τ ) = Fρ,σ⊗τ ◦ 1F(ρ) ⊗ Fσ,τ ◦ α
′
F(ρ),F(σ),F(τ) ◦ Gρ,σ ⊗ 1F(τ) ◦ Gρ⊗σ,τ (4.6)
F(α
−1
ρ,σ,τ ) = Fρ⊗σ,τ ◦ Fρ,σ ⊗ 1F(τ) ◦ α
′−1
F(ρ),F(σ),F(τ) ◦ 1F(ρ) ⊗ Gσ,τ ◦ Gρ,σ⊗τ . (4.7)
Definition 4.9. In the case that all Fρ,σ are isomorphisms then Gρ,σ = F
−1
ρ,σ thus only
one of the equations (4.6) and (4.7) suffices and we recover the notion of a tensor functor
[50, 105, 137, 141].
Remark 4.10. a) In Sect. 32 we shall construct a weak tensor structure (F, G) on a
certain faithful functor F : C(g, q, ℓ) → Hilb on the strict fusion tensor category C(g, q, ℓ)
associated to quantum groups at roots of unity to Hilb, the category of finite dimensional
Hilbert spaces. To this aim, the notion of negligible morphism in the category of tilting
modules for a suitable quantum group at root of unity Uq(g) plays a central role.
b) In the paper, see e.g. Sect. 8, 33, 37, 38, we shall also consider a notion weaker than
that of weak tensor functor, in that we shall need to work with functors for which (4.6)
or (4.7) hold for a subcollection V of triples of objects, which is sufficiently large in a way
that will be made precise.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 27
c) The following seems an interesting insight gained from the notion of weak tensor
functor, and more specifically from the utility of having the two equations (4.6), (4.7),
which were first noticed in the course of the construction of the examples of weak Hopf
algebras in [25], and then again in the course of the construction of the generalizations of
these examples to all Lie types in Sect. 32. These properties were shown to follow from
the properties of negligible morphisms in the representation category of Uq(g) at root of
unity, but have not been not used in [25] or for the most part of this paper, except for the
following possibly non trivial application.
If we have a faithful functor F : C → Vec on a semisimple pre-tensor category C and a
weak quasi-tensor structure (F, G) for F and an invertible natural transformation
αρ,σ,τ : (ρ ⊗ σ) ⊗ τ → ρ ⊗ (σ ⊗ τ )
making C into a tensor category and we have an understanding in a specific situation of
validity of one preferred equation among the two (4.6), (4.7) on a fixed triple (ρ, σ, τ ), and
if moreover β(ρ, σ, τ ) is a fixed invertible morphism associated to the same fixed triple
(ρ, σ, τ ) and acting a morphism of C between the same objects as αρ,σ,τ ,
βρ,σ,τ : (ρ ⊗ σ) ⊗ τ → ρ ⊗ (σ ⊗ τ )
and satisfies the same property as α among (4.6) or (4.7), then αρ,σ,τ = βρ,σ,τ on that fixed
triple by faithfulness of F and uniqueness of the inverse. If moreover one finds a collection
V of triples (ρ, σ, τ ) for which this property is known to hold on each element of V, which is
sufficiently large to determine α uniquely on all triples of objects of C (for example V is as
in Sect. 8, Corollary 8.15, Theorem 8.13) then β admits a unique extension to associativity
morphisms of C satisfying the axioms of a tensor category, and the extension is given by α.
In our main application, we wish to achieve this setting with F(α) and (F, G) defined by
a Drinfeld twist construction from a situation as in a) and moreover F(β) with the same
(F, G), arise from conformal field theory , see Sect. 38.
Definition 4.11. A tensor equivalence between tensor categories C and C
′
is a tensor
functor E : C → C
′ which is an equivalence of linear categories.
It is known that a quasi-inverse G : C
′ → C may be chosen tensorial and the natural
transformations 1C′ → FG, 1C → GF monoidal see Remark 2.4.10 in [50]. In particular, G
is a tensor equivalence as well.
In general, we are making no assumption on compatibility of α
′ with the two subobjects
of (F(ρ) ⊗ F(σ)) ⊗ F(τ ) and F(ρ) ⊗ (F(σ) ⊗ F(τ )) corresponding respectively to the right
invertible maps Fρ⊗σ,τ ◦ Fρ,σ ⊗ 1F(τ) and Fρ,σ⊗τ ◦ 1F(ρ) ⊗ Fσ,τ .
A weak quasi-tensor functor monoidally isomorphic to a weak tensor functor is itself
weak tensor.
The notion of weak (quasi) tensoriality for a functor applies to contravariant functors
C → C
′ as well, but in this case the defining natural transformations are required to act as
Fρ,σ : F(ρ) ⊗ F(σ) → F(σ ⊗ ρ), Gρ,σ : F(σ ⊗ ρ) → F(ρ) ⊗ F(σ) and the diagrams (4.6) and
(4.7) have to be appropriately modified. Equivalently, such functors may be regarded as
covariant (quasi) tensor functors after replacing C
′ with the opposite category (C′
)
op that

28 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
is the category with same objects and morphisms, but opposed morphisms and reversed
tensor products.
We shall also consider categories with involutions and involution preserving functors.
We shall follow [41] and [141]. These structures will not be needed until Sect. 12.
Definition 4.12. A ∗-category is a linear category C endowed with an antilinear, contravariant, involutive functor ∗
: C → C acting trivially on objects. A tensor ∗-category is a
tensor category equipped with the structure of a ∗-category satisfying (S ⊗ T)
∗ = S∗ ⊗ T∗
for any pair of morphisms S, T ∈ C. The associativity morphisms are assumed unitary,
α
∗
ρ,σ,τ = α
−1
ρ,σ,τ .
Definition 4.13. A C
∗
-category is a ∗-category where morphism spaces are Banach spaces
such that the norm satisfies ∥S ◦ T∥ ≤ ∥S∥∥T∥ and ∥T
∗ ◦ T∥ = ∥T∥2
for every pair of
morphisms S, T and S
∗S is positive (i.e. has positive spectrum) in the algebra (ρ, ρ) for
every morphism S ∈ (ρ, σ). Finally, a tensor C
∗
-category is a tensor ∗-category which is
also a C
∗
-category with respect to the given ∗-involution.
The positivity condition is equivalent to the existence of S
′ ∈ (ρ, ρ) such that S∗S =
S
′∗S′
. It follows in particular that (ρ, ρ) is a C
∗
-algebra for any object ρ. In a C
∗
-category,
two isomorphic objects ρ, σ are called unitarily isomorphic if there is a unitary U ∈ (ρ, σ),
that is U
∗U = 1, UU∗ = 1. An orthogonal summand of ρ is a summand defined by a
selfadjoint idempotent E ∈ (ρ, ρ) which is the range of an isometry (there is S ∈ (σ, ρ)
such that S
∗S = 1 and SS∗ = E). An orthogonal direct sum ρ ⊕ σ is defined by isometries
S1 ∈ (ρ, ρ ⊕ σ), S2 ∈ (σ, ρ ⊕ σ) such that S1S
∗
1 + S2S
∗
2 = 1.
It follows from the positivity of T
∗T that a left invertible morphism T ∈ (σ, ρ) admits
polar decomposition in C. Thus S = T(T
∗T)−1/2 ∈ (σ, ρ) is an isometry. In particular,
two isomorphic objects ρ, σ are also unitarily isomorphic.
It also follows that a summand or a direct sum is isomorphic to an orthogonal one. Indeed, by Prop. 4.6.2 in [16] every idempotent in a unital C
∗
-algebra is similar to a selfadjoint idempotent. Thus a summand σ of ρ up to isomorphism corresponds to a selfadjoint
idempotent in E ∈ (ρ, ρ), and it follows that polar decomposition of the corresponding
morphism S ∈ (σ, ρ) gives the needed isometry. Similarly, the defining complementary
idempotents of a direct sum ρ ⊕ σ may be assumed selfadjoint and it follows that the
direct sum is orthogonal.
In particular, a semisimple C
∗
-category has orthogonal summands and direct sums. It
is also easy to see that the positivity condition of T
∗T follows from the other properties of
a C
∗
-category and existence of orthogonal direct sums, cf. Ch. 2 in [141].
Definition 4.14. A ∗-functor F : C → C
′ between ∗
-categories is a linear functor satisfying
F(T
∗
) = F(T)
∗
for all morphisms T ∈ C. If C and C
′ are tensor ∗
-categories, a ∗-functor
endowed with a weak quasi tensor structure will be called a weak quasi tensor ∗-functor.
Let F be a weak quasi tensor ∗-functor defined by Fρ,σ, Gρ,σ. Then the adjoint pair
F
′
ρ,σ = G∗
ρ,σ, G′
ρ,σ = F
∗
ρ,σ defines another weak quasi tensor structure on F.
Definition 4.15. A ∗-equivalence between ∗-categories C and C
′
is an equivalence compatible with the ∗
-structure, that is a ∗-functor E : C → C
′ admitting a quasi-inverse E′
: C
′ → C

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 29
which is a ∗-functor with natural unitary transformations η : 1 → EE′ and η
′
: 1 → E
′E. If
C and C
′ are tensor ∗
-categories, E is a tensor ∗-equivalence if E and E
′ are tensor ∗
-functors.
We note the following C
∗
-version of the characterisation of equivalences between categories of Remark 4.5.
Proposition 4.16. Let F : C → C
′
be a ∗-functor between C
∗–categories. Then F is a
∗
-equivalence if and only if it is a ∗-functor which is an equivalence of linear categories. If
C and C
′ are tensor C∗
-categories then F is a tensor ∗–equivalence if and only if it is a
∗
-functor and a tensor equivalence.
Proof. We start with the definition of a linear equivalence as a full, faithful and essentially
surjective functor F, as in Remark 4.5. Theorem IV.4.1 [123] constructs a linear functor
G : C
′ → C and invertible natural transformations η : 1 → FG and η′
: 1 → GF. We
are thus left to show that we can always choose η and η
′ unitary and G a∗
-functor. To
this aim, it is not difficult to adapt the proof of that theorem to the needed framework
as follows. The isomorphisms ηc defined there, corresponding to our η, may be chosen
unitary passing to polar decomposition available with the C
∗
-structure of C
′
. This implies
that the quasi-inverse equivalence constructed there and denoted T, in turn corresponding
to G, satisfies that η : 1 → FG is a unitary natural transformation. This fact, together
with the fact that F is a faithful ∗-functor, implies that G is linear and ∗-preserving on
morphism spaces. If η
′′ : 1 → GF is any invertible natural transformation, one of which is
found in the same theorem, then the unitary part in the polar decomposition η
′ of η′′ will
be a unitary natural transformation between the same functors thanks to the ∗-preserving
properties of the involved functors. The last statement follows from the fact that when C
and C’ are tensor C
∗
-categories then we already know that we may construct a tensorial
quasi-inverse G and then we apply the first part of the proof. □
Remark 4.17. We note that a faithful and essentially surjective ∗-functor between ∗-
categories F : C → C
′ does not necessarily admit a quasi-inverse ∗
-functor. An example is
given by the immersion of the category Hilb of finite dimensional Hilbert spaces into the
category Herm of finite dimensional Hermitian spaces. This category will be introduced
and studied starting with Sect. 12. For the subclass of semisimple ∗-categories we have
the following useful criterion analogous in analogy to Remark 4.5. Let Irru(C) be a set of
pairwise unitarily inequivalent simple objects in C such that every other simple object is
unitarily isomorphic to one element of Irru(C). A faithful ∗-functor between ∗-categories
F : C → C
′
is a ∗-equivalence if and only if the set of objects F(ρ) with ρ ∈ Irru(C) is a
complete set of pairwise unitarily inequivalent simple objects in C
′
.
In the theory of C
∗
-tensor categories, or more generally of tensor ∗-categories, we have
the following notion of unitarity for a tensor functor and a tensor equivalence, see [141].
Definition 4.18. Let C and C
′ be tensor ∗
-categories. A unitary tensor functor (F, F, G =
F
−1
), is a tensor ∗-functor such that F is unitary. A unitary tensor equivalence is a tensor
∗
-equivalence which is unitary as a tensor ∗-functor and with a unitary quasi-inverse.

30 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Unitary tensor functors from C
∗
-tensor categories to Hilb arise as forgetful functors of
compact quantum groups see e.g. [141]. As fusion categories do not in general admit tensor
functors to Vec, but always admit weak quasi-tensor functors, we introduce a notion of
unitarity in the following more general setting.
We next begin to discuss a problem that has relevence in how paper, that is how to
associate to a given weak quasi-tensor structure (F, G) another one that has in some sense
a more trivial unitary structure. Historically, the first condition considered in the literature
is G = F
∗ and G unitary see e.g. [141], or more generally isometry [82].
Definition 4.19. Let C and C
′ be tensor ∗
-categories. A unitary weak quasi tensor functor
is a weak quasi tensor ∗-functor F : C → C
′ defined by (F, G) such that F∗ and G are
isometries. A strongly unitary weak quasi tensor functor we have in addition F
∗ = G.
For quasi-tensor ∗-functors we recover the usual notion of unitarity F
∗
ρ,σ = F
−1
ρ,σ .
Remark 4.20. The definition of unitarity may equivalently be formulated by the properties
F
∗
ρ,σFρ,σ = P
∗
ρ,σPρ,σ, Gρ,σG
∗
ρ,σ = Pρ,σP
∗
ρ,σ
where Pρ,σ is the idempotent defined in (4.5).
In general, if (F, G) is unitary then we may have two new strongly unitary structures
(F, F∗) and (G∗, G) arising from (F, G). However, in the C
∗
-case all these structures
coincide. More precisely, we note the following simple result.
Proposition 4.21. Let C be a tensor ∗-category, C
′ a tensor C∗
-category and (F, G) a
weak quasi-tensor structure for a ∗-functor F : C → C
′
. Let ρ, σ ∈ C be a pair of objects. If
F
∗
ρ,σ and Gρ,σ are isometries then F
∗
ρ,σ = Gρ,σ. In particular, any unitary weak quasi-tensor
structure is automatically strongly unitary.
Proof. We have that Fρ,σGρ,σ = 1F(ρ⊗σ) = G∗
ρ,σGρ,σ = Fρ,σF
∗
ρ,σ. It follows that
G
∗
ρ,σ(1F(ρ)⊗F(σ) − F
∗
ρ,σFρ,σ)Gρ,σ = G
∗
ρ,σGρ,σ − (Fρ,σGρ,σ)
∗
(Fρ,σGρ,σ) = 0.
The C
∗
-property of C
′
implies (1 − F
∗
ρ,σFρ,σ)Gρ,σ = 0 thus Gρ,σ = F
∗
ρ,σ. □
To construct unitary weak quasi-tensor structures from a given weak quasi-tensor structure, structure it is natural to try with polar decomposition.
We consider a weak quasi tensor ∗-functor (F, F, G) : C → C
′ between C∗
-tensor categories and we describe a a unitarization of the weak quasitensor structure (F, G). We
set
Ωρ,σ := F
∗
ρ,σ
◦ Fρ,σ ∈ (F(ρ) ⊗ F(σ), F(ρ) ⊗ F(σ)).
Note that Ωρ,σ is partially invertible (in the sense of Def. 6.1) with partial inverse
Ω
−1
ρ,σ := Gρ,σ ◦ G
∗
ρ,σ ∈ (F(ρ) ⊗ F(σ), F(ρ) ⊗ F(σ))
satisfying Ω−1
ρ,σΩρ,σ = Pρ,σ and Ωρ,σΩ
−1
ρ,σ = P
∗
ρ,σ. Since they are both positive, we may take
the respective square roots Ω1/2
ρ,σ and (Ω−1
ρ,σ)
1/2
.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 31
It can easily be shown that these operators are partially invertible between the same
idempotents as Ωρ,σ and Ω−1
ρ,σ respectively. If we in addition know that (Ω−1ρ,σ)
1/2
is a left
inverse of Ω1/2
ρ,σ , that is
(Ω−1
ρ,σ)
1/2Ω1/2
ρ,σ = Pρ,σ (4.8)
then we shall just write Ω−1/2
ρ,σ for (Ω−1
ρ,σ)
1/2
. We have
F = S
∗
◦ Ω
1/2
, G = Ω−1/2◦ T, (4.9)
where S and T are isometries as G is a right inverse of F.
Proposition 4.22. Let F : C → C
′
be a weak quasi-tensor ∗-functor between tensor C
∗
-
categories defined by (F, G) such that (Ω−1
ρ,σ)
1/2Ω
1/2
ρ,σ = Pρ,σ (e.g. P = 1). Then
a) the pair (F
′
, G′), where
F
′ = FΩ−1/2 = S∗Ω1/2Ω−1/2
, G′ = Ω1/2G = Ω1/2Ω
−1/2T,
is a unitary weak quasi-tensor structure for F, and therefore strongly unitary, F
′ =
G′∗,
b) In particular, if (F, F, G) is quasi tensor then F
′ = S∗
, G′ = S = T is always well
defined and is a unitary quasi-tensor structure,
c) if F is full and if (F, G) is a tensor structure then (S
∗
, S) is a unitary tensor
structure for F.
Proof. a) It follows from ∗-invariance of F that Ωρ,σ is natural in ρ, σ, and from continuous
functional calculus that Ω1/2
ρ,σ and Ω−1/2
ρ,σ are natural as well, hence the same holds for F
′
and G′. We have F
′G′ = F P G = 1, so (F′
, G′) is a weak quasi tensor structure. The
associated idempotent is given by P
′
:= G′F
′ = Ω1/2PΩ−1/2 = Ω1/2Ω−1/2
. Furthermore
F
′F′∗ = F(Ω−1
)
1/2
(Ω−1)
1/2F∗ = F GG∗F∗ = 1, G′∗G′ = G∗Ω1/2Ω1/2G = G∗F∗F G = 1,
thus (F
′
, G′) is unitary, and by Prop. 4.21 also strongly unitary. c) In this case F, G
are invertible and G = F
−1
, thus P = 1, S, T are unitary and S
∗T = 1. d) Since
(G∗
ρ,σ
◦ Gρ,σ)
1/2
is a positive invertible element in the C
∗
-algebra (F(ρ ⊗ σ), F(ρ ⊗ σ)) and
F is full, we may write (G∗
ρ,σ
◦ Gρ,σ)
1/2 = F(Aρ,σ) with Aρ,σ ∈ (ρ ⊗ σ, ρ ⊗ σ) positive, and
Gρ,σ = Sρ,σ ◦F(Aρ,σ) with S unitary. It follows that F(1ρ ⊗Aσ,τ ) is positive by ∗-invariance
of F and also invertible by naturality of G. Furthermore,
1F(ρ) ⊗ Gσ,τ ◦ Gρ,σ⊗τ = 1F(ρ) ⊗ Sσ,τ ◦ F(1ρ) ⊗ F(Aσ,τ ) ◦ Gρ,σ⊗τ =
1F(ρ) ⊗ Sσ,τ ◦ Gρ,σ⊗τ ◦ F(1ρ ⊗ Aσ,τ ) = 1F(ρ) ⊗ Sσ,τ ◦ Sρ,σ⊗τ ◦ Bρ,σ,τ ,
where Bρ,σ,τ := F(Aρ,σ⊗τ ) ◦ F(1ρ ⊗ Aσ,τ ). A similar computation starting with the same
element but relying now on naturality of S in place of G, see a), leads to conclude that
F(Aρ,σ⊗τ ) and F(1ρ ⊗ Aσ,τ ) commute, and this implies that Bρ,σ,τ is positive, besides
invertible. In a similar way Gρ,σ ⊗ 1F(τ) ◦ Gρ⊗σ,τ = Sρ,σ ⊗ 1F(τ) ◦ Sρ⊗σ,τ ◦ Cρ,σ,τ for some
other positive invertible morphism Cρ,σ,τ . Inserting these relations into the tensoriality
diagram 1F(ρ) ⊗ Gσ,τ ◦ Gρ,σ⊗τ ◦ F(α) = α
′ ◦ Gρ,σ ⊗ 1F(τ) ◦ Gρ⊗σ,τ gives another tensoriality
diagram satisfied by S in place of G by unitarity of the associativity morphisms and
uniqueness of polar decomposition. □

32 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Definition 4.23. Let (F, F, G) : C → C
′ be a weak quasi-tensor ∗
-functor between tensor
C
∗
-categories satisfying the left inverse property (4.8). Then the same functor F together
with the new unitary weak quasi-tensor structure (F
′
, G′) defined in part a) of Prop. 4.22
will be called the unitarization of (F, F, G).
Remark 4.24. We would like to warn the reader that it is not clear to us whether (4.8)
holds in our main late applications as in Sect. 30 and following. It follows that it is unclear
whether the polar decomposition construction of Prop. 4.22 can be used. We shall need
to develop a modification of the unitarization construction for a functor in Sect. 30. On
the other hand, the unitarization of a functor will be fruitful for us in case of full domains
(P = 1), see Sect. 17, where we shall discuss uniqueness of unitary structures in tensor
categories.
Part c) shows that in the important case of tensor ∗-equivalence the unitarization gives
a unitary tensor equivalence. We have the following consequence.
Corollary 4.25. Two tensor ∗-equivalent tensor C
∗
-categories are also unitarily tensor
equivalent.
Remark 4.26. Note that we do not have a statement about unitarization of a weak
tensor ∗-functor. On this subject we shall see that the notion of unitary weak tensor ∗-
functor is too strong for unitary fusion categories of interest for us. Specifically, a unitary
weak tensor ∗-functor to the category of Hilbert spaces is automatically tensor for large
classes of semisimple unitary tensor tensor categories and the category necessarily has an
integer-valued dimension function, we refer to Corollary 16.8 for details. It follows that
the unitarization of a weak tensor ∗-functor in general is only a unitary weak quasi-tensor
∗
-functor. In Sect. 32 we shall construct examples of weak tensor ∗-functors associated to
unitary fusion categories of quantum groups at roots of unity, and part a) of Prop. 4.22
will turn out useful.
