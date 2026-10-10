---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-004-5-rigidity-weak-tensor-functors-braided-symmetry-r
section_title: "Rigidity, weak tensor functors, braided symmetry, ribbon and modular category"
section_number: 5
pages: 32-36
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
doc_brief: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem — We construct, for every complex simple Lie algebra g and every positive integer level k, a unitary modular"
---
5. Rigidity, weak tensor functors, braided symmetry, ribbon and modular
category
In this brief section we recall the notion of rigidity, braided and ribbon tensor category
and we show a simple result that weak tensor functors are always compatible with rigidity.
Definition 5.1. Let C be a tensor category with associativity morphisms αρ,σ,τ ∈ ((ρ ⊗
σ) ⊗ τ, ρ ⊗ (σ ⊗ τ )). An object ρ
∨
is a right dual of ρ if there are morphisms d ∈ (ρ
∨ ⊗ ρ, ι)
and b ∈ (ι, ρ ⊗ ρ
∨
) satisfying the right duality equations
1ρ ⊗ d ◦ αρ,ρ∨,ρ ◦ b ⊗ 1ρ = 1ρ, (5.1)
d ⊗ 1ρ∨ ◦ α
−1
ρ∨,ρ,ρ∨ ◦ 1ρ∨ ⊗ b = 1ρ∨ . (5.2)
A left dual object ∨ρ is defined by morphisms b
′ ∈ (ι, ∨ρ ⊗ ρ), d′ ∈ (ρ ⊗ ∨ρ, ι) satisfying the
left duality equations
d
′ ⊗ 1ρ ◦ α
−1
ρ,∨ρ,ρ
◦ 1ρ ⊗ b
′ = 1ρ, (5.3)
1∨ρ ⊗ d
′
◦ α∨ρ,ρ,∨ρ ◦ b
′ ⊗ 1∨ρ = 1∨ρ. (5.4)

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 33
A tensor category is called rigid if every object has left and right duals.
The following facts are well known: another right dual (˜ρ, ˜b, ˜d) is isomorphic to ρ
∨
, the
isomorphism is
ξ := ˜d ⊗ 1ρ∨ ◦ 1ρ˜ ⊗ b : ˜ρ → ρ
∨
, (5.5)
and similarly for left duals. If ρ and σ have right duals ρ
∨ and σ∨
, then so does ρ⊗σ , and it
is given by σ
∨⊗ρ∨ via the morphisms dρ⊗σ = dσ ◦1σ∨ ⊗(dρ⊗1σ)◦α ∈ ((σ
∨⊗ρ∨
)⊗(ρ⊗σ), ι),
bρ⊗σ = α
′ ◦ 1ρ ⊗ (bσ ⊗ 1ρ∨ ) ◦ bρ ∈ (ι,(ρ ⊗ σ) ⊗ (σ
∨ ⊗ ρ∨
)), where α and α
′ are suitable
associativity morphisms.
Definition 5.2. A right duality is defined by the choice of a right dual (ρ
∨
, bρ, dρ) for each
object ρ such that ι
∨ = ι with bι = dι = 1ι
. A left duality is defined in a similar way.
Every right duality gives rise to a contravariant functor D : C → C acting as
ρ → ρ
∨
, T ∈ (ρ, σ) → T
∨
:= dσ ⊗ 1ρ∨ ◦ 1σ∨ ⊗ T ⊗ 1ρ∨ ◦ 1σ∨ ⊗ bρ ∈ (σ
∨
, ρ∨), (5.6)
called the right duality functor, which turns out tensorial. A different right duality structure
(˜ρ, ˜bρ,
˜dρ) gives a corresponding duality functor D˜ related to D via the isomorphisms ξρ :
ρ˜ → ρ
∨ defined in (5.5), which is a natural monoidal isomorphism ξ : D˜ → D.
Right and left dualities naturally arise in representation categories of Hopf algebras and
their generalisations, where canonical choices are induced by the antipode, we shall discuss
this in detail in Sect. 7. A well-behaved choice of right and left dualities lead to the
notion of spherical category. In a spherical category a theory of categorical dimension can
be developed. By a theorem of Deligne [196], see also Sect. 27, when the category is
braided there is a correspondence between spherical structures and ribbon structures for
the braided symmetry.
Definition 5.3. Let C be a tensor category with right duality (ρ
∨
, bρ, dρ). A natural
isomorphism η ∈ (1, 1) of the identity functor of C is called compatible with duality if
ηρ∨ = (ηρ)
∨
.
If ρ is simple then ηρ is a nonzero scalar multiple of 1ρ. It is easy to see that the property
of being compatible with duality for an isomorphism η ∈ (1, 1) does not depend on the
choice of the right duality.
We recall the definition of braided symmetry, ribbon (or premodular) and modular
category category.
Definition 5.4. A braided symmetry for C is a natural isomorphism c(ρ, σ) ∈ (ρ⊗σ, σ⊗ρ)
satisfying the normalization property
c(ρ, ι) = c(ι, ρ) = 1ρ (5.7)
and such that the following two hexagonal diagrams commute
(ρ ⊗ σ) ⊗ τ
α −−−→ ρ ⊗ (σ ⊗ τ )c −−−→ (σ ⊗ τ ) ⊗ ρ
c⊗1


y


yα
(σ ⊗ ρ) ⊗ τ
α −−−→ σ ⊗ (ρ ⊗ τ )1⊗c −−−→ σ ⊗ (τ ⊗ ρ)
(5.8)

34 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
(ρ ⊗ σ) ⊗ τ
c −−−→ τ ⊗ (ρ ⊗ σ)α−1
−−−→ (τ ⊗ ρ) ⊗ σ
α−1
x


x

c⊗1
ρ ⊗ (σ ⊗ τ )
1⊗c −−−→ ρ ⊗ (τ ⊗ σ)α−1
−−−→ (ρ ⊗ τ ) ⊗ σ
(5.9)
A weak quasi-tensor functor between braided tensor categories (F, F, G) : (C, c) → (D, d)
is called braided if the structure maps are compatible with the braided symmetries, meaning
F(c(ρ, σ)) = Fσ,ρd(F(ρ), F(σ))Gρ,σ,
F(c(ρ, σ)
−1
) = Fρ,σd(F(ρ), F(σ))−1Gσ,ρ.
For a tensor equivalence, the natural transformations F, G, are one another inverse isomorphisms, consequently only one equation suffices.
Proposition 5.5. Let C be a semisimple tensor category with associativity morphisms α.
Let c(τ, σ) ∈ (τ ⊗ σ, σ ⊗ τ ) be natural isomorphisms satisfying (5.7) and (5.8) (or (5.9
resp.) Let ρ be a generating object of C as in Def. 4.3. Then c is uniquely determined by
the morphisms c(ρλ, ρ) (c(ρ, ρλ) resp.) with ρλ varying in a complete set of simple objects
of C.
In particular, if c is a braided symmetry then it is determined by either class of morphisms of the form c(ρλ, ρ) or of the form c(ρ, ρλ).
Proof. By (5.8), if ρ is replaced by a fixed tensor power ρ
r of the given generating object,
σ = ρ, τ = ρ
t with t ≥ 0 and ρt a tensor power of the generating object with parentheses on
the right, it follows by induction that c(ρ
r
, ρs) for r, s > 0 is determined by c(ρ
r
, ρ). Thus
by naturality and semisimplicity, c is determined by all the c(ρλ, ρ). A similar reasoning
holds if c satisfies (5.9) and shows that c is determined by the collection of all c(ρ, ρλ). The
last statement follows from these two cases.
□
Definition 5.6. Let C be a rigid tensor category with braided symmetry c. A ribbon
structure is a natural isomorphism v ∈ (1, 1) such that c(σ, ρ) ◦ c(ρ, σ) = vρ ⊗ vσ ◦ v
−1
ρ⊗σ and
compatible with some right duality.
In a ribbon category one has a notion of C-valued categorical trace Trρ(T) for all morphisms T ∈ (ρ, ρ) see Sect. 27 for the definition. For any pair of objects ρ, σ, consider the
matrix
Sρ,σ = Trρ⊗σ(c(σ, ρ)c(ρ, σ)).
The number Sρ,σ depends on X and Y only up to isomorphism. When C is a fusion ribbon
category, let {ρi} be a complete set of irreducible objects.
Definition 5.7. A ribbon fusion category is called modular if the matrix S = (Sρi,ρj) is
invertible.
Let T = (Tρi,ρj) be the diagonal matrix defined by Tρi,ρj = δi,jv
−1
ρi
. If C is modular then
S → s =

0 1
−1 0 
T → t =

1 1
0 1 
(5.10)

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 35
defines a projective representation of SL(2,Z). Recall that SL(2, Z). is generated by s, t
with relation s
2 = −1, (st)3 = 1.
Let Z2(C) be symmetric center of C, defined in [19], [131] as the full subcategory of C
with objects the set of ρ ∈ C for which c(ρ, σ)c(σ, ρ) = 1σ⊗ρ for all σ ∈ C. We shall need
the following characterization of modularity, C is modular if and only if Z2(C) is trivial.
We refer to [137] for more complete information on modular categories, see also [50].
Unitary braided symmetries are central notions for this paper see e.g. Sect. 13, 28,
32, 25, 22, 23. In Sect. 27 we shall extend Deligne theorem to a class of symmetries
more general than braided symmetries which play a central role in the study of unitary
structures in this paper in Sect. 28, 30, 32. Ribbon structure and categorical dimension
are used in our applications, the classification result of slN,ℓ-type categories in Sect. 25.
Prop. 5.5 will be useful to describe the braiding of the representation category of the
Zhu algebra associated to an affine vertex operator algebra at positive integer with respect
to a ribbon braided tensor structure that we shall construct, see Theorem 33.11. See also
Sect. 21, for a statement of the main result and Sect. 34 for further comparison of our
braiding with previously known braided tensor structures in the setting of loop groups.
Proposition 5.8. Let (F, F, G) : C → C
′
be a weak tensor functor between tensor categories. If ρ
∨
is a right dual of ρ defined by d ∈ (ρ
∨ ⊗ ρ, ι) and b ∈ (ι, ρ ⊗ ρ∨
) then F(ρ
∨
)
is a right dual of F(ρ) defined by d1 = F(d) ◦ Fρ∨,ρ and b1 = Gρ,ρ∨ ◦ F(b), similarly for left
duals.
Proof. We only show that d1 and b1 solve (5.1) for F(ρ). We have
1F(ρ) ⊗ d1 ◦ α
′
F(ρ),F(ρ∨),F(ρ) ◦ b1 ⊗ 1F(ρ) =
Fρ,ι ◦ 1F(ρ) ⊗ d1 ◦ α
′
F(ρ),F(ρ∨),F(ρ) ◦ b1 ⊗ 1F(ρ) ◦ Gι,ρ =
Fρ,ι ◦ 1F(ρ) ⊗ F(d) ◦ 1F(ρ) ⊗ Fρ∨,ρ ◦ α
′
F(ρ),F(ρ∨),F(ρ) ◦ Gρ,ρ∨ ⊗ 1F(ρ) ◦ F(b) ⊗ 1F(ρ) ◦ Gι,ρ =
F(1ρ ⊗ d) ◦ Fρ,ρ∨⊗ρ ◦ 1F(ρ) ⊗ Fρ∨,ρ ◦ α
′
F(ρ),F(ρ∨),F(ρ) ◦ Gρ,ρ∨ ⊗ 1F(ρ) ◦ Gρ⊗ρ∨,ρ ◦ F(b ⊗ 1ρ) =
F(1ρ ⊗ d) ◦ F(αρ,ρ∨,ρ) ◦ F(b ⊗ 1ρ) = 1F(ρ).
□
Corollary 5.9. Let C be a rigid tensor category and F : C → Vec be a weak tensor functor.
Then dim(F(ρ)) = dim(F(ρ
∨
)) = dim(F(
∨ρ)) for every object ρ.
If a tensor category is rigid, left and right duals need not be isomorphic. It is easy to
see that this is the case if and only if ρ ≃ ρ
∨∨ and, following M¨uger, we call ρ∨ a two-sided
dual of ρ. We shall say that C has two-sided duals if every object has a two-sided dual.
For example, duals are two-sided if C is a semisimple tensor category, see e.g. Prop. 2.1 in
[51], a tensor category with a coboundary, e.g. a braided symmetry, by Prop. 27.7, or a
tensor ∗-category [118]. In the last case, a solution d and b of the right duality equations
gives one of the left duality equations via ρ
∨
:= ∨ρ, b
′ = d∗ and d′ = b∗
. This dual is

36 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
also called a conjugate of ρ and denoted ρ. The duality equations are written in terms of
r := d
∗ and r := b, and referred to as the conjugate equations:
r
∗ ⊗ 1ρ ◦ α
−1
ρ,ρ,ρ
◦ 1ρ ⊗ r = 1ρ, r∗ ⊗ 1ρ ◦ α
−1
ρ,ρ,ρ
◦ 1ρ ⊗ r = 1ρ. (5.11)
Let C be a tensor C
∗
-category. The intrinsic dimension of ρ is defined as d(ρ) = inf ∥r∥r∥
over all solutions of the conjugate equations for ρ [118].
Corollary 5.10. Let C and C
′
be tensor C
∗
-categories and F : C → C
′ a weak tensor
∗
-functor defined by (F, G). If ρ ∈ C has a conjugate then d(F(ρ)) ≤ ∥Fρ,ρ∥∥Gρ,ρ∥d(ρ).
Proof. Let b, d solve the right duality equations for ρ and consider the associated solution
b1, d1 for F(ρ) as in Prop. 5.8, so r1 = d
∗
1
, r1 = b1 solves the conjugate equations for
the same object. We have r
∗
1
r1 ≤ ∥Fρ,ρ∥
2F(r∗
r) so ∥r1∥ ≤ ∥Fρ,ρ∥∥r∥ by the C
∗
-property.
Similarly ∥r1∥ ≤ ∥Gρ,ρ∥∥r∥ and the conclusion follows. □
In particular if F is a unitary weak tensor functor we have d(F(ρ)) ≤ ∥d(ρ)∥, and if F
is in turn unitary tensor we recover a well known upper bound in representation theory of
compact quantum groups of the vector space dimension of a representation by the quantum
dimension. More precisely, this case corresponds to C the representation category of the
compact quantum group, C
′ = Hilb and F the forgetful functor, see Cor. 2.2.20 in [141].
As already remarked before Def. 4.19, we shall see that by Prop. 5.10 together with the
results in Sect. 16 and more specifically Cor. 16.8, in C and C
′ are rigid C∗
-tensor categories
and C is amenable then every unitary weak tensor functor F : C → C
′ preserves the intrinsic
dimensions. In particular, non-integrality of the intrinsic dimension is an obstruction to
the concurrence of both unitarity and weak tensoriality for a weak quasitensor structure
(F, F, G) to Hilb. In the non-weak case this result was shown in [118], see also Cor. 2.7.9
in [141] and references therein. Examples of non-unitary weak tensor structures or unitary
weak quasitensor structures arising from fusion categories associated to quantum groups
at roots of unity and conformal field theory will be discussed in Sect. 30, 25, 23.
