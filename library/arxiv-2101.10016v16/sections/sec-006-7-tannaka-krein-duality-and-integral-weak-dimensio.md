---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-006-7-tannaka-krein-duality-and-integral-weak-dimensio
section_title: "Tannaka-Krein duality and integral weak dimension functions (wdf)"
section_number: 7
pages: 43-52
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
---
7. Tannaka-Krein duality and integral weak dimension functions (wdf)
The problem of constructing weak quasi-Hopf algebras from an abstract fusion category was introduced in [125, 165] and developed in [82]. Their motivation was that the
framework of quasi-Hopf algebras is an important notion for conformal field theory but
too restrictive for many related fusion categories as they may not admit integral valued
dimension functions. Their central idea consists in a weakened notion of a dimension function taking integral values whose existence can easily be proven for all fusion categories
and still allows Tannakian recostruction theorems. In this section we review and expand
these results far beyond fusion categories.
In the first part of this section we describe how weak quasi-Hopf algebras lead to rigid
tensor categories. We then discuss Tannaka-Krein duality results for semisimple rigid
tensor categories. We shall then see that every fusion category may be described by a weak
quasi-Hopf algebra associated to an integral weak dimension function on the Grothendieck
ring of the category. Moreover, we shall extend this result far beyond the class of fusion
categories.

44 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Our description originates from the work in [82] and will be fruitful later on, for different
purposes. For example, the weak quasi-Hopf algebra representation provided by an integral
weak dimension function provides a cohomological insight into the category that will be
further investigated in the paper. Moreover, weak dimension functions will play a central
role in our study of unitary structures in fusion categories of affine vertex operator algebras.
Furthermore, we shall describe examples of algebras naturally associated to certain fusion
categories for which the integral dimensions arising from their representations satisfy the
weak dimension property, see Sect. 32 and 23.
Let A be a complex unital algebra. By a representation of A we mean a unital left action
of A, ρ : A → L(V ) on a finite dimensional complex vector space V . It is customary to
pass to the language of (left) A-modules, dropping reference to ρ. We shall conform to this
notation when no confusion arises. The representation category Rep(A) is the category
with objects representations of A and morphisms between two objects the subspace (ρ, ρ′)
of L(Vρ, Vρ
′) consisting of all A-linear maps. The forgetful functor is the functor
F : Rep(A) → Vec
associating a representation with its vector space, and acting trivially on morphisms.
If A admits the structure of a weak quasi-bialgebra (ε, ∆, Φ) then the counit ε is a 1-
dimensional representation. We may form the tensor product representation ρ⊗ρ
′ which
is the representation acting on the subspace
Vρ⊗ρ
′ := ∆(I)Vρ ⊗ Vρ
′
of the tensor product vector space Vρ ⊗ Vρ
′ with left action induced by the coproduct:
ρ⊗ρ
′
:= ρ ⊗ ρ
′
◦ ∆.
Given two morphisms S ∈ (ρ, σ), S
′ ∈ (ρ′
, σ′), the tensor product map S ⊗ S
′ ∈ L(Vρ ⊗
Vρ
′, Vσ ⊗ Vσ′) commutes with the action of ∆(I), thus takes Vρ⊗ρ
′ to Vσ⊗σ′. The restriction
S⊗T to Vρ⊗ρ
′ is a morphism in (ρ⊗ρ
′
, σ⊗σ
′
). Given representations ρ, σ, τ , (ρ⊗σ)⊗τ and
ρ⊗(σ⊗τ ) act respectively on the ranges of ∆⊗1◦∆(I) and 1⊗∆◦∆(I). The restriction of
the action of Φ to the space of (ρ⊗σ)⊗τ is an isomorphism αρ,σ,τ : (ρ⊗σ)⊗τ → ρ⊗(σ⊗τ ).
In this way Rep(A) becomes a tensor category with unit object the counit of A.
Proposition 7.1. The forgetful functor F : Rep(A) → Vec of a weak quasi-bialgebra A is
weak quasi-tensor with Fρ,σ = ∆(I) and Gρ,σ the inclusion map.
We give a categorical interpretation of the notion of twist of a weak quasi-Hopf algebra,
extending properties known for quasi-Hopf algebras. Let A be a unital discrete algebra
endowed with two weak quasi-bialgebra structures (A, ε, ∆, Φ), (A, ε, ∆′, Φ
′
). We may
correspondingly form two tensor categories Rep(A), Rep′(A) and the functor E : Rep(A) →
Rep′(A) acting identically on objects and morphisms. This functor fixes the tensor units,
it is full, faithful on morphisms and essentially surjective, and hence E is an equivalence
of linear categories. Furthermore, the two forgetful functors F : Rep(A) → Vec, F
′
:
Rep′(A) → Vec satisfy the property that F
′E = F just as linear functors. We would like
to make E into an equivalence of tensor categories.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 45
Proposition 7.2. Let the discrete unital algebra A be endowed with two weak quasibialgebra structures A = (A, ε, ∆, Φ) and A′ = (A, ε, ∆′
, Φ
′
). Then there is a bijective
correspondence between tensor structures on the identity linear equivalence E : Rep(A) →
Rep′(A) and twists F ∈ M(A ⊗ A) such that A′ = AF as weak quasi-bialgebras. Given F,
the tensor structure Eρ,σ : Eρ ⊗ Eσ → Eρ⊗σ is given by the action of F
−1
.
Proof. The proof is a straightforward extension of the case of quasi-bialgebras, for which
we refer the reader to Prop. 2.1 in [139]. We briefly comment on how to construct the
twist from the tensor structure. Given a tensor structure Eρ,σ on E : Rep(A) →: Rep′(A)
we consider the unique elements F
−1
, F ∈ M(A ⊗ A) having components Eρ,σ, and Eρ,σ
−1
respectively in the representation ρ ⊗ σ of A ⊗ A. Then ρ ⊗ σ(F
−1F) = Eρ,σ ◦ E−1
ρ,σ =
1F(ρ⊗σ) = ρ ⊗ σ(∆(I)), hence F
−1F = ∆(I). The relation ε ⊗ 1(F) = I = 1 ⊗ ε(F)
can be checked in a similar way, hence F is a twist. The relations ∆′ = ∆F and Φ′ = ΦF
correspond respectively to the intertwining relations Eρ,σ ∈ (Eρ⊗Eσ, Eρ⊗σ) and tensoriality
property. □
Extending the terminology of [141] to non-coassociative Hopf algebras, a twist V ∈ A⊗A
is called invariant if ∆V = ∆ and ΦV = Φ. For example, if v ∈ A is central invertible then
∆(v)v
−1 ⊗ v−1
is an invariant twist. By the previous proposition, invariant twists induce
tensor autoequivalence structures on the identity functor Rep(A) → Rep(A) and they are
all of this form in the discrete case.
More generally, if A is discrete, given (A, ε, ∆, Φ) and (A, ε, ∆′, Φ
′
), the weak quasitensor structures on E : Rep(A) → Rep′
(A) correspond to the twists F ∈ A ⊗ A such that
∆′ = ∆F . Given such a structure, the composite functor F
′E becomes a weak quasi-tensor
with the composed structure. Since F = F
′E as functors, this also induces a new weak
quasi-tensor structure on F. Of course, this is given by the action of F
−1
, with F the
twist corresponding to E, so the induced structure on F determines that of E. Thus the
construction of a tensor structure on E can be regarded as that of a weak quasi-tensor
structure of the forgetful functor F : Rep(A) → Vec defined by a twist F ∈ A ⊗ A solving
(A, ε, ∆′, Φ
′
) = AF .
Two weak quasi-tensor structures on F are monoidally isomorphic if and only if the
corresponding twists F1 and F2 are related by an invertible u ∈ M(A) such that F2 =
u ⊗ uF1∆(u
−1
). This corresponds to say that AF1 and AF2 are isomorphic as weak quasibialgebras. For example, the weak quasi-tensor structures on F monoidally isomorphic to
the original one correspond to twists of the form u⊗u∆(u
−1
), where u ∈ A is an invertible
element. These twists are called 2-coboundaries. The monoidal isomorphism ηρ acts as
ρ(u) on Vρ.
Rigidity in Rep(A) is described similarly to quasi-Hopf algebras.
Definition 7.3. Let ρ be a representation of a weak quasi-Hopf algebra. The contragredient representations ρ
c and cρ are the the representations of A acting on the dual space
V
′
ρ
respectively as
⟨ρ
c
(a)ϕ, ξ⟩ = ⟨ϕ, ρ(S(a))ξ⟩, ⟨
c
ρ(a)ϕ, ξ⟩ = ⟨ϕ, ρ(S
−1
(a))ξ⟩.

46 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Proposition 7.4. If A is a weak quasi-Hopf algebra the category Rep(A) is rigid. Right
and left duals of an object ρ are respectively given by
ρ
∨ = ρc
,
∨
ρ =
c
ρ.
Solutions of the right and left duality equations are respectively given by
dρ(ϕ ⊗ ξ) = ϕ(αξ) bρ =
X
i
βei ⊗ e
i
,
and
b
′
ρ =
X
i
e
i ⊗ S−1
(β)ei, d′
ρ
(ξ ⊗ ϕ) = ϕ(S
−1
(α)ξ)
where (ei) and (e
i
) is a dual pair of bases.
Thus Rep(A) is rigid and by the above proposition, an antipode of A induces right and
left duality structures, (bρ, dρ) and (b
′
ρ
, d′
ρ
), respectively, and consequently a (say, right)
duality functor c : ρ → ρ
c acting as transposition of αT β on a morphism T. By Prop.
6.13 the collection of operators fσ,ρ := Σσ
c ⊗ ρc
(S
−1 ⊗ S−1
(f21)) is an invertible natural
transformation σ
c ⊗ ρc → (ρ ⊗ σ)c making c into a contravariant tensor functor. We
compute the natural transformation associated to c
2
. We canonically identify the double
dual space V
′′
ρ
of a representation with Vρ, so ρ
cc identifies with ρ ◦ S2
. Reading (6.18)
as an intertwining relation f : ∆ → S ⊗ S ◦ ∆op ◦ S
−1
, it implies that S ⊗ S(f
−1
21 ) :
S ⊗S ◦ ∆op ◦S
−1 → S2 ⊗S2 ◦ ∆ ◦S−2
, hence we can form the composite which intertwines
S ⊗ S(f
−1
21 )f : ∆ → S
2 ⊗ S2
◦ ∆ ◦ S
−2
.
This implies that ρ⊗σ(f
−1S⊗S(f21)) can be regarded as an intertwiner ρcc⊗σcc → (ρ⊗σ)cc
,
and this is the natural transformation of c
2
.
Note that left and right duals of the same object of Rep(A) are equivalent whenever S
2
is an inner automorphism of A and a converse holds if A is discrete, that is S
2
is induced
by an invertible in M(A). For example if A is not assumed discrete, S
2
is inner whenever
A has an Ω-involution in the sense of the Sect. 11 commuting with S, by Cor. 11.17, or
for the class weak Hopf algebras introduced in Sect. 9 with a quasitriangular structure, by
Prop. 10.7.
If S
2
is inner, any invertible x ∈ A such that S
2
(a) = xax−1induces an invertible natural
transformation η : 1 → c
2
, where ηρ is defined by the action of ρ(x), but to construct a
pivotal structure we need a monoidal natural transformation.
Definition 7.5. A pivotal weak quasi-Hopf algebra is a pair (A, ω) with A a weak quasiHopf algebra and ω ∈ A an invertible element, called the pivot, such that S
2
(a) = ωaω−1
for all a ∈ A and f
−1S ⊗ S(f21) = ∆(ω)ω−1 ⊗ ω−1
.
The pivot is not unique but determined up to multiplication by an invertible central element z satisfying ∆(z) = z⊗z. In Sect. 10 we shall see that if A is a ribbon weak quasi-Hopf
algebra, then there is a canonically associated ω such that η becomes a monoidal. Note
that since the identity functor is tensorial, we may use this property to derive tensoriality of c
2 more easily for such class of algebras. Indeed, a quasi-tensor functor which is

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 47
monoidally isomorphic to a tensor functor must be tensorial as well. This endows Rep(A)
with the structure of a pivotal tensor category. But more is true: Rep(A) becomes a
spherical category in the sense of [9], a result extending to the weak case, results known
for ribbon Hopf algebras. Thus, there is a well-behaved theory of dimension in Rep(A),
see Sect. 16.
The following Tannakian reconstruction results are due to [82] and extend to the weak
case an earlier result of Majid for discrete quasi-Hopf algebras [126]. For a review for
discrete Hopf algebras, see [134]. The starting point is an abstract semisimple category
equipped with a fibre functor F : C → Vec. We let Nat0(F) denote the discrete algebra of
natural transformations of F to itself with finite support.
Theorem 7.6. Let C be a semisimple category and F : C → Vec a faithful functor. Then
(a) A = Nat0(F) is a discrete algebra and there is a linear equivalence E : C → Rep(A)
which, after composition with the forgetful functor FA : Rep(A) → Vec, is isomorphic to F. Up to isomorphism, A is determined by the last property among discrete
algebras.
(b) If C is tensorial and F has a weak quasi-tensor structure then A is a weak quasibialgebra, E is a tensor equivalence, the isomorphism FAE ≃ F is monoidal and A
is determined among discrete weak quasi-bialgebras.
Let (C, F) satisfy the same assumptions as in (b).
(c) If C is braided then A is a quasitriangular weak quasi-bialgebra and E is braided.
(d) If C is rigid and dim(F(ρ)) = dim(F(ρ
∨
)) then a solution of the right duality equations induces an antipode on A making it into a weak quasi-Hopf algebra.
(e) If C satisfies (d) and is ribbon then A is a ribbon weak quasi-Hopf algebra.
Proof. We briefly discuss a few aspects that we shall need. (a) A natural transformation
η ∈ Nat0(F) = A is determined by the values it takes on a complete set of simple objects
{ρi}i, and this gives an algebra isomorphism of A ≃
L
i L(Vi), with Vi = F(ρi), so A is
discrete. (b) As before, αρ,σ,τ : (ρ⊗σ)⊗τ → ρ⊗(σ⊗τ ) denote the associativity morphisms
of C and Fρ,σ and Gρ,σ the natural transformations defining the quasi-tensor structure of
F. Counit, coproduct, and associator of A are respectively defined as follows. We identify
A ⊗ A with natural transformations on two variables ζρ,σ : F(ρ) ⊗ F(σ) → F(ρ) ⊗ F(σ),
and similarly for A⊗3. We set: ε(η) = ηι,
∆(η)ρ,σ = Gρ,σ ◦ ηρ⊗σ ◦ Fρ,σ, (7.1)
Φρ,σ,τ = 1F(ρ) ⊗ Gσ,τ ◦ Gρ,σ⊗τ ◦ F(αρ,σ,τ ) ◦ Fρ⊗σ,τ ◦ Fρ,σ ⊗ 1F(τ). (7.2)
It follows that
Φ
−1
ρ,σ,τ = Gρ,σ ⊗ 1F(τ) ◦ Gρ⊗σ,τ ◦ F(α
−1
ρ,σ,τ ) ◦ Fρ,σ⊗τ ◦ 1F(ρ) ⊗ Fσ,τ .
The axioms can be checked with routine computations. In comparison with the quasitensor setting where the natural transformations are invertible, the relations Fρ,σ ◦ Gρ,σ =
1F(ρ⊗σ)is used here to show partial invertibility of Φ. The tensor equivalence E is F
regarded as a functor with values in Rep(A) and tensor structure obtained by restricting
that of F. (c), (e) The notion of braided or ribbon tensor category is recalled in Sect. 5,

48 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Definitions 5.4 and 27.9 respectively. Quasitriangular and ribbon structures for weak quasibialgebras are given in Sect. 10, Definition 10.1 and 10.5. If c(ρ, σ) is a braided symmetry
in C, and Σ(V, W) is the permutation symmetry of Vec, then the element R ∈ M(A ⊗ A)
defined by Σ(F(ρ), F(σ)) ◦ Rρ,σ = Gσ,ρ ◦ F(c(ρ, σ)) ◦ Fρ,σ makes A quasitriangular. When
C has a ribbon structure vρ then A has a ribbon structure defined by the ribbon element
v ∈ M(A), where v is the natural transformation F(vρ). (d) A weak quasi-Hopf algebra
antipode (S, α, β) is constructed as follows. For ρ ∈ Irr(C), we fix linear isomorphisms
from the dual vector spaces Uρ : F(ρ)
′ → F(ρ∨
), and extend U to a natural transformation
from the functor ρ → F(ρ)
′
to the functor ρ → F(ρ
∨
). We set S(η)ρ = U
t
ρ
η
t
ρ∨ U
t
ρ
−1
, where
L
t
: W′ → V
′
is the transposed of the linear map L : V → W, and α, β are determined by
F(dρ) ◦Fρ∨,ρ ◦Uρ ⊗1(f ⊗ξ) = f(αρξ), 1⊗U
−1
ρ
◦Gρ,ρ∨ ◦F(bρ) = P
i
βρei ⊗e
i
, for ρ ∈ Irr(C),
f ∈ F(ρ)
′
, ξ ∈ F(ρ), ei ∈ F(ρ) a linear basis and e
i ∈ F(ρ)′
the dual basis. We refer to
Lemma 12 in [82] or to Prop. 2.5 in [139] for the verification of the antipode axioms.
The equivalence E takes an object ρ ∈ C to the representation E(ρ) : η → ηρ of Nat0(F)
on the vector space F(ρ). The natural transformation Eρ,σ making E into a tensor equivalence is the restriction of Fρ,σ to ∆(I)F(ρ) ⊗ F(σ) → F(ρ ⊗ σ), with inverse E
−1
ρ,σ given by
G considered as a map F(ρ ⊗ σ) → ∆(I)F(ρ) ⊗ F(σ).
□
Remark 7.7. a) By semisimplicity of C, faithfulness of F is equivalent to requiring that
F(ρ) ̸= 0 for all simple objects ρ. In particular, F is always faithful on the morphism
spaces (ρ, σ) where both ρ and σ are ̸= 0. b) The requirement of dimension equality in
(d) is automatic in the case where C has finitely many inequivalent simple objects, (i.e. is
a fusion category), see [139] for a discussion and references, and also where F is a weak
tensor functor, by Cor. 5.9. c) When we start with a given semisimple weak quasi-Hopf
algebra A then Tannakian reconstruction of Theorem 7.6 applied to the forgetful functor
F : Rep(A) → Vec with the natural weak quasi-tensor structure provides a discrete weak
quasi-Hopf structure on Nat0(F) which corresponds to the original structure of A under the
natural inclusion of A with Nat0(F). Note that the construction of an antipode of Nat0(F)
as in the proof of Theorem 7.6 depends on the choice of a right duality (ρ
∨
, bρ, dρ) of Rep(A)
and the natural transformation U. In particular, by Prop. 7.4 a given antipode (S, α, β) of
A corresponds to the antipode of Nat0(F) defined by the canonical right duality associated
to ρ
∨ = ρc as in Prop. 7.4 and to the identity natural transformation U (note that this is
an admissible choice as the functor ρ → F(ρ
∨
) coincides with ρ → F(ρ)
′
). d) In general,
the algebras Nat0(F) and Nat(F) of general natural transformations of F to itself may have
different representation categories, see [78]. However, regarding Nat(F) = M(Nat0(F)) as
a topological algebra with the strict topology defined by Nat0(F) the category of nondegenerate representations of Nat0(F) coincides with the full subcategory of strictly continuous
representations of Nat(F). We shall touch on again the relevance of the Tannakian algebra Nat(F) as a topological algebra for the forgetful functor associated to Uq(g) for the
construction of the R-matrix, see Sects. 28, 30, 32.
We next introduce the notion positive weak dimension function.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 49
Definition 7.8. Let C be a semisimple tensor category. A positive weak dimension function
is a positively valued function D defined on a complete set Irr(C) of irreducible objects
and satisfying D(ι) = 1, and
X
τ∈Irr(C)
D(τ )dim(τ, ρ ⊗ σ) ≤ D(ρ)D(σ). (7.3)
When C is rigid a weak dimension function satisfying D(ρ) = D(ρ
∨
) = D(
∨ρ), for all ρ, is
called symmetric.
If the inequality is always an equality we recover the notion of positive dimension function. We tacitly extend a weak dimension function to all the objects of C via additivity
and isomorphism invariance, and (7.3) reads as
D(ρ ⊗ σ) ≤ D(ρ)D(σ)
for every pair of objects ρ and σ. A weak dimension function D for C may be regarded as
a (unital, additive, and submultiplicative) function on the Grothendieck ring Gr(C), and
Irr(C) as a Z-basis.
For a large part of this paper, we shall consider weak dimension functions taking positive integral values. Furthermore, when the categories have duals, we shall also assume
the symmetry condition. However, in Sect. 16 and 25 we shall also consider dimension
functions for a different purpose, which may not be positive or integral, but the context
should lead to no confusion.
If A is a weak quasi bialgebra and F : Rep(A) → Vec is the forgetful functor of A then
D(ρ) = dim(F(ρ)) is an integral weak dimension function. It follows that a semisimple
(rigid) tensor category C equivalent to the representation category of a weak quasi-bialgebra
(quasi-Hopf algebra) admits an integral (symmetric) weak dimension function. The following result shows that under suitable conditions existence of an integral weak dimension
on C function is also a sufficient to represent C in this way.
Theorem 7.9. Let C be a semisimple linear category.
(a) The assignment F → D, D(ρ) := dim(F(ρ)), is a bijective correspondence between
faithful functors F : C → Vec up to natural isomorphism and functions D : Irr(C) →
N.
(b) If C is tensorial then the functor F admits a weak quasi-tensor structure if and only
if D is an integral weak dimension function. Furthermore, quasi-tensor structures
correspond to genuine dimension functions.
(c) The weak quasi bialgebra structures on A = Nat0(F) associated to the various weak
quasi-tensor structures on F of dimension D as in Theorem 7.6 are pairwise twist
isomorphic.
Proof. (a) Obviously naturally isomorphic functors are associated to the same function
D : Irr(C) → N. Conversely, given D, choosing, for ρ ∈ Irr(C), a vector space F(ρ)
with dim(F(ρ)) = D(ρ) gives rise to a faithful functor F : C → Vec, determined up to
natural isomorphism. (b) If F : C → Vec admits a (weak) quasi-tensor structure then
D(ρ) := dim(F(ρ)) is a (weak) dimension function. For the converse, since by assumption,

50 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
dim(F(ρ) ⊗ F(σ)) ≥ dim(F(ρ ⊗ σ)) for all ρ, σ ∈ Irr(C), we may pick epimorphisms
Fρ,σ : F(ρ) ⊗ F(σ) → F(ρ ⊗ σ) and monomorphisms Gρ,σ : F(ρ ⊗ σ) → F(ρ) ⊗ F(σ)
satisfying Fρ,σ ◦ Gρ,σ = 1 and acting identically if either ρ or σ is the tensor unit. We
extend these maps to all the objects µ, ν using complete reducibility: choose α
i
ρ ∈ (ρ, µ),
β
i
ρ ∈ (µ, ρ) with β
j
ρα
i
ρ = δi,j1ρ,
P
i,ρ α
i
ρβ
i
ρ = 1µ, and similarly for γ
j
σ ∈ (σ, ν), δ
i
σ ∈ (ν, σ).
Set Fµ,ν =
PF(α
i
ρ ⊗ γ
j
σ
) ◦ Fρ,σ ◦F(β
i
ρ
) ⊗ F(δ
j
σ
). It is easy to see that naturality holds, that
is Fµ′
,ν′ ◦F(S)⊗F(T) = F(S ⊗T) ◦Fµ,ν. Naturality also shows that Fµ,ν is independent of
the choice of the morphisms involved in the decompositions. We similarly obtain a natural
transformation Gµ,ν and it is easy to see that Fµ,ν ◦ Gµ,ν = 1. We thus have a weak quasitensor structure, which is quasi-tensor if D is a dimension function. (c) If (F, G), (F
′
, G′)
define two weak quasi-tensor structures on F then we know from Theorem 7.6 and its proof
that the coproduct associated to the latter is defined by ∆′(η)ρ,σ = G′
ρ,σ
◦ ηρ⊗σ ◦ F
′
ρ,σ, and
similarly for ∆. We may then write ∆′(η) = G′F∆(η)GF′since F G = 1. Setting T = G′F
and T
−1 = GF′ we see that these natural transformations may be regarded as elements of
A⊗A and that T
−1T = GF = ∆(I), T T −1 = G′F′ = ∆′
(I). A similar computation shows
that the corresponding associators are related by the corresponding twist relation. □
It follows from Remark 17.4 and Theorem 7.9 that any finite semisimple (fusion) category is tensor equivalent to that of a weak quasi bialgebra (Hopf algebra), and a tensor
equivalence corresponds to a twist isomorphism between two associated such algebras.
Corollary 7.10. Let C and C
′
be semisimple tensor categories endowed with integral weak
dimension functions D and D′respectively compatible with a linear equivalence E : C → C
′
.
Then E admits the structure of a tensor equivalence if and only if the corresponding weak
quasi-bialgebras are isomorphic up to twist.
Proof. If the categories are tensor equivalent then we apply Th. 7.9 and Th. 7.6. Conversely, let F : C → Vec and F
′
: C
′ → Vec be weak quasi-tensor functors of dimensions
D and D′ and associated weak quasi-bialgebras A and A′respectively. Then F
′E and
F : C → Vec have the same dimension D, so they are isomorphic by Th. 7.9 (a). It follows that F
′E admits a weak quasi-tensor structure with weak quasi-bialgebra isomorphic
to A, thus there is a tensor equivalence E1 : C → Rep(A) and a monoidal isomorphism
F
′E ≃ FAE1 with FA : Rep(A) → Vec the forgetful functor. On the other hand, we
similarly have a monoidal isomorphism of F
′ ≃ FA′E2 with E2 : C′ → Rep(A′
) a tensor
equivalence and FA′ : Rep(A′
) → Vec the forgtful functor. Since A is isomorphic to a
twist of A′, there is a tensor equivalence E3 : Rep(A′) → Rep(A) and an isomorphism
FAE3 ≃ FA′ by Prop. 7.2. We have an isomorphism of functors FAE1 ≃ FAE3E2E and
since E1 admits the structure of a tensor equivalence, the same holds for E3E2E. Let E
′
2
and E
′
3 be quasi-inverse tensor equivalences of E2 and E3 respectively. Then E
′
2E
′
3E3E2E is
a tensor equivalence naturally isomorphic to E as a linear equivalence, thus E admits the
structure of a tensor equivalence. □
In Sect. 23 we shall use weak quasi-Hopf algebras associated to tensor equivalent fusion
categories to gain insight into the study of unitarizability of fusion categories and this will

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 51
find fruitful applications to CFT. We formulate a simple criterion that will eventually be
useful to construct ribbon tensor equivalences, see Sect. 25.
If a weak quasi bialgebra A′is obtained from another such bialgebra A by replacing the
associator of the latter with a new one but leaving the rest of the structure unchanged,
then Rep(A) and Rep(A′) have isomorphic Grothendieck rings. The following proposition,
inspired by a similar statement in [142] for Hopf algebras, shows that at an abstract level
an isomorphism of Grothendieck rings of fusion categories can always be visualized in this
way.
Proposition 7.11. Let C and C
′
be semisimple tensor categories and let f : Gr(C) →
Gr(C
′
) be an isomorphism between their Grothendieck rings. Let (A, ∆, Φ
′
) be a weak quasi
bialgebra corresponding to an integral weak dimension function D′ on C
′
. Then there is an
associator Φ for A defining a new weak quasi bialgebra (A, ∆, Φ) which corresponds to C
with respect to D = D′f. In particular, if C
′
is a finite semisimple tensor category then C
is tensor equivalent to one with the same category and tensor product structure as C
′
but
possibly different associativity morphisms.
Proof. Consider a complete set Irr(C
′
) of irreducible objects of C
′
. Let F
′
: C
′ → Vec be
a weak quasi-tensor functor corresponding to D′ and defining (A, ∆, Φ
′
). By Theorem
7.9 a weak quasi-tensor structure on F
′
is determined by the choice, for ρ, σ ∈ Irr(C
′
),
of (normalized) epimorphisms Fρ,σ : F
′
(ρ) ⊗ F
′
(σ) → F
′
(ρ ⊗ σ) and monomorphisms
Gρ,σ : F
′
(ρ⊗σ) → F
′
(ρ)⊗F
′
(σ) satisfying Fρ,σ ◦Gρ,σ = 1. These maps are in turn specified
by the choice of linear maps maps Gτ,i
ρ,σ : F
′
(τ ) → F
′
(ρ) ⊗ F
′
(σ), F
τ,j
ρ,σ : F
′
(ρ) ⊗ F
′
(σ) →
F
′
(τ ) for τ ∈ Irr(C
′
), via P
τ,i Gτ,i
ρ,σF
′
(T
τ
i
) =: Gρ,σ and P
τ,i F
′
(S
τ
i
)F
τ,i
ρ,σ =: Fρ,σ, where
S
τ
i ∈ (τ, ρ ⊗ σ), T
τ
i ∈ (ρ ⊗ σ, τ ) satisfy T
τ
j S
τ
i = δi,j ,
P
τ,i S
τ
i T
τ
i = 1, in turn subject to
F
τ,i
ρ,σGυ,j
ρ,σ = δτ,υδi,j . Writing A = Nat0(F
′
), the coproduct formula of A given in (7.1) can
be written as ∆(η)ρ,σ =
P
τ,i Gτ,i
ρ,σητF
τ,i
ρ,σ by naturality of η.
Note that we may establish a bijective correspondence ρ ∈ Irr(C) → ρ
′ ∈ Irr(C′
) and
linear isomorphisms (τ, ρ ⊗ σ) → (τ
′
, ρ′ ⊗ σ
′
). We then set F(ρ) := F
′
(ρ
′
), extend F
to a faithful functor F : C → Vec, and consider the weak quasi-tensor structure of F
defined by the same maps F
τ,i
ρ,σ, Gτ,iρ,σ under the correspondence ρ → ρ
′
. It follows that the
corresponding weak quasi bialgebras may be chosen with the same algebra and coproduct
structures. □
Example 7.12. Let G be a finite group. Consider the category C = VecG of finite
dimensional G-graded vector spaces with tensor product defined by convolution and trivial
associativity morphisms. The representation ring is ZG. The constant function D = 1 is
a dimension function, giving rise to the commutative bialgebra C(G) of complex functions
f on G with usual coproduct ∆(f)(g, h) = f(gh). Prop. 7.11 reduces to the known
classification of tensor categories with this representation ring. Indeed, in this special case
it shows that any such category is tensor equivalent to some Vecω
G, obtained from VecG with
a new associativity morphism given by a normalised C
×-valued 3-cocycle ω. It corresponds
to the quasi-bialgebra Cω(G) coinciding with C(G) except for the associator, which is given
by ω. Since Vecω
G is a pointed fusion category, D = 1 is the only dimension function on ZG.

52 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Thus Cω(G) is, up to twist, the only quasi-bialgebra that can be associated to Vecω
G. Twist
isomorphism corresponds to cohomologous cocycles. It follows that the fusion categories
Vecω
G are parameterised by H3
(G, C
×). It also follows that Vecω
G admits a faithful tensor
functor to Vec if and only if ω is cohomologically trivial.
For example, the category Vecω
Z2
, with ω the non trivial element of H3(Z2, C
×), arises
from the representation theory of the affine vertex operator algebra associated to sl2 at
level 1, a topic that will be discussed in more detail in Sections 25, 22, 23. We shall come
back to this in more detail and generality later on. We shall see that this category also
admits a weak tensor functor to Vec with weak dimension function D(ρ) = 2, and ρ the
unique non trivial irreducible object, cf. Example 18.1.
The following result will be useful to construct a tensor structure on a given linear
equivalence between semisimple tensor categories.
Proposition 7.13. Let C and C
′
be semisimple tensor categories, G : C → C
′ a tensor
equivalence and F : C → C
′ a linear equivalence. If F and G induce the same isomorphism
between the corresponding Grothendieck rings then F can be made into a tensor equivalence.
Proof. By assumption, for every simple object ρ ∈ C, F(ρ) and G(ρ) are equivalent simple
objects in C
′
, and any simple object of C
′
is equivalent to one of them. It follows that F and
G are related by an invertible natural transformation η, and therefore F may be endowed
with a unique weak quasi-tensor structure making η monoidal. It also follows that this is
a tensor structure for F since so is the quasi-tensor structure of G.
□
In Sect. 8 we shall study methods to construct tensor equivalences between tensor
categories motivated by fusion categories of quantum groups at roots of unity, vertex
operator algebras and conformal nets.
