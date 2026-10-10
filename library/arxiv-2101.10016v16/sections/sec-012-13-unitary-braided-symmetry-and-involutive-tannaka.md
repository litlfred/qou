---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-012-13-unitary-braided-symmetry-and-involutive-tannaka
section_title: "Unitary braided symmetry and involutive Tannaka-Krein duality"
section_number: 13
pages: 96-100
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
doc_brief: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem — We construct, for every complex simple Lie algebra g and every positive integer level k, a unitary modular"
---
13. Unitary braided symmetry and involutive Tannaka-Krein duality
In this section we discuss properties of the involutive structure in a weak quasi-Hopf
algebra concerning the twisting operation, quasitriangular structure and Tannaka-Krein
duality. We start with categorical interpretation of a twist of the ∗-structure of a weak
quasi bialgebra, in analogy with Prop. 7.2 for a twisted bialgebra structure.
Let A be a (discrete) weak quasi bialgebra and (∗, Ω) an Ω-involution in the sense of
Def. 11.1. Let t ∈ A (or t ∈ M(A) if A is discrete) be a selfadjoint twist, and consider
the corresponding twisted involution (†, Ωt), see Prop. 11.14. We thus have two structures

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 97
(A, ε, ∆, Φ,
∗
, Ω) and (A, ε, ∆, Φ,
†
, Ωt) which differ only for their involution. For brevity, we
denote them respectively as A and At, in analogy with a twist of the bialgebra structure.
Consider the functor E : Reph(A) → Reph(At) defined as follows. If ρ is a ∗-representation
of A then we modify the Hermitian form (ξ, η)Vρ of Vρ as (ξ, η)t:= (ξ, ρ(t)η)Vρ, and
consider the representation ρt of At on the Hermitian space Vρtso obtained acting as ρ.
By construction, ρtis a †-representation of At.
Proposition 13.1. Let A be a unitary (discrete) weak quasi bialgebra and t a positive
twist for the involutive structure. Then the functor E : Rep+(A) → Rep+(At) taking ρ to
ρt, acting identically on morphisms and with identity natural transformations is a unitary
tensor equivalence of tensor C
∗
-categories.
Proof. Pick ρ, σ ∈ Rep+(A). For any linear map T : Vρ → Vσ, the adjoint of T with respect
to the original and modified Hermitian forms are related by T
† = σ(t−1
)T
∗ρ(t). Thus if
T ∈ (ρ, σ) then T
† = T∗
, and this shows that E is a ∗-functor, which is clearly full, faithful
and essentially surjective, hence a ∗-equivalence. On the other hand, the tensor structures
of Rep+(A) and Rep+(At) are identical, hence E is a tensor equivalence under the identity
natural transformations. To show unitarity we are left to verify that the inner products of
ρt ⊗ σt and (ρ ⊗ σ)t coincide, but this follows from a straightforward computation.
□
It is well known that if A is a quasitriangular quasi-Hopf algebra with R-matrix R, the
category Rep(A) has a braided symmetry ε, where the action of ε(ρ, σ) on the representation space Vρ ⊗ Vσ is given by ΣR, with Σ : Vρ ⊗ Vσ → Vσ ⊗ Vρ the permutation operator.
This construction extends to the weak case. Similarly, if A has an Ω-involution, Reph(A)
is a braided tensor category as well. We next observe a condition on R assuring unitarity
of ε in Reph(A).
Proposition 13.2. Let A be an Ω-involutive weak quasi-bialgebra with quasitriangular
structure defined by R and satisfying R˜ = RΩ. Then the associated braided symmetry of
Reph(A) is unitary. If A is discrete the converse holds.
Proof. Our assumption on the R-matrix means R∗−1 = Ω21RΩ
−1
. The relation between
the adjoint morphism ε(ρ, σ)
∗ with respect to the ∗
-structure of Reph(A) and the adjoint
ε(ρ, σ)
† with respect to the product form is ε(ρ, σ)∗ = Ω−1
ε(ρ, σ)
†Ω. Therefore
ε(ρ, σ)
∗ = Ω−1
(Σρ ⊗ σ(R))†Ω = Ω−1(ρ ⊗ σ(R
∗
))Ω21Σ = R
−1Σ = ε(ρ, σ)−1
.
□
Remark 13.3. The assumptions in Prop. 13.2 may be read as saying that the twist
relation A˜ = AΩ holds not only at the level of weak quasi-bialgebras, but also for their
natural quasitriangular structures, cf. Prop. 10.2. Furthermore if R˜ = RΩ holds for a
given Ω-involutive quasitriangular weak quasi-bialgebra with R-matrix R and involution
Ω then they hold for any twisted algebra with twisted R-matrix RT and twisted involution
ΩT , Ω−1
T
as defined in c) of Prop. 10.2 and Prop. 11.8 respectively.

98 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Corollary 13.4. Let A be a finite dimensional discrete weak quasi-Hopf algebra with a
quasitriangular structure R. Then any involution (∗, Ω) making A into a unitary weak
quasi bialgebra satisfies R˜ = RΩ.
Proof. The tensor C
∗
-category Rep+(A) is braided and fusion, hence by Theorem 3.2 in
[66] the braided symmetry is unitary. We may then apply Prop. 13.2.
□
We next discuss a version of Tannaka-Krein duality for Ω-involutive weak quasi bialgebras. Recall that unitarity of a weak quasi tensor ∗
-functor was defined in Def. 4.19, and
that triviality of an Ω-involution is introduced in Def. 11.9.
Theorem 13.5. Let C be a semisimple tensor ∗-category, with finite dimensional morphism
spaces F : C → Herm a faithful weak quasi tensor ∗-functor defined by (F, G) and A =
Nat0(F) be the discrete weak quasi bialgebra associated to F as in Th. 7.6 and Th. 9.10
endowed with its natural involution ∗. Then
a) the element Ω ∈ A ⊗ A defined by Ωρ,σ = F
∗
ρ,σ
◦ Fρ,σ makes A into an Ω-involutive
weak quasi bialgebra,
b) there is a canonical unitary tensor ∗-functor E : C → Reph(A) and is an equivalence.
Furthermore, the composite of E with the forgetful functor Reph(A) → Herm is
unitarily monoidally isomorphic to F,
c) (F, F, G) is (strongly) unitary if and only if A the Ω-involution of A as in a) is
(strongly) trivial,
d) when C is unitary and F : C → Hilb then A is a unitary weak quasi-bialgebra and
E is a unitary tensor equivalence between E : C → Rep+(A).
Proof. a) For simplicity in the following computations we drop the indices of the natural
transformations. Note that Ω is selfadjoint, and in particular positive when F takes values
in Hilb. Furtherore, Ω has ∆(I) = GF as domain and ∆(I)
∗ = (GF)∗ as range. We
set Ω−1:= GG∗. We have: Ω−1Ω = GG∗F
∗F = G(F G)∗F = GF = ∆(I) and similarly
ΩΩ−1 = ∆(I)
∗
. Furthermore, for η ∈ A,
Ω∆(η
∗
) = F
∗F∆(η∗
) = F
∗F Gη∗
ρ⊗σF =
F
∗
η
∗
ρ⊗σF = F
∗
η
∗
ρ⊗σG
∗F∗F = ∆(η)∗Ω.
We have thus verified axioms (11.1), (11.2), (11.3), while (11.4) follows easily from (4.2)
and (11.5) can be checked with computations similar to those above. b) By assumption,
F(ρ) is an Hermitian space and by Theorem 7.6 E(ρ) is a representation of A on F(ρ)
and E is a tensor equivalence with Rep(A) and therefore also with Reph(A). It is easy to
check that E is ∗-preserving, it follows that E takes values in Reph(A). To show unitarity
of E recall that the tensor structure of E regarded as a morphism in Reph(A) is Fρ,σ. We
compute the adjoint F
∗
ρ,σ in Reph
(A). As before, we momentarily denote by †the usual
adjoint of the tensor category of Hilbert spaces. We have
F
∗
ρ,σ = Ω−1ρ,σF
†
ρ,σ = Gρ,σG
†
ρ,σF
†
ρ,σ = Gρ,σ(Fρ,σGρ,σ)
† = Gρ,σ.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 99
c) By definition of unitarity of (F, F, G), F
∗F = P∗P and GG∗ = P P∗
, with P = GF and
this by construction corresponds to triviality of the Ω-involution of A, and similarly for the
relation between strong unitarity of the weak quasi-tensor structure and strong triviality
of the Ω-involution.
□
Remark 13.6. Theorem 13.5 for unitary weak quasi-bialgebras has origin in [82] where
the author assumes that F
∗
ρ,σ = Gρ,σ and are isometries, that is a strongly unitary structure
in our terminology. In this case he proves that the ∗-involution of A commutes with the
coproduct. We note that the examples that we discuss in Sect. 32 arising from quantum
groups at roots of unity do not satisfy this property, and this motivated us to consider the
more general case.
Example 13.7. Consider the ∗-category C = Hermω
G of G-graded Hermitian spaces. It
becomes a tensor ∗-category with natural tensor product and associator given by a T-valued
3-cocycle ω over G. For every g ∈ G, denote by C
+
g
(C
−
g
) the one-dimensional Hermitian
space of degree g with positive (negative) scalar product. Then C
+
g
and C
−
g
are two
irreducible equivalent but not unitarily equivalent objects of Hermω
G, and C
±
g
and C
±
h
are
inequivalent for g ̸= h. The category Hermω
G contains Hilbω
G as a full tensor C
∗
-subcategory
with restricted ∗-structure. Consider F : Hermω
G → Herm the forgetful functor. Note that
F preserves the Hermitian forms, thus it takes a definite sign on the unitarily inequivalent
simple objects. It follows that Nat0(F) is a pre-C
∗
-algebra that may be identified with
the C
∗
-algebra of complex-valued functions on G. Note that F(g) ⊗ F(h) and F(gh) are
unitarily equivalent Hermitian spaces with definite forms, thus every quasitensor structure
Fg,h on F satisfies Ω(g, h) := F
∗
g,hFg,h > 0. It follows from Theorem 13.5 that A = Nat0(F)
is a unitary pointed quasi-bialgebra which identifies with Cω(G) with unitary structure
defined by Ω as in Example 11.6. Note that by the last part of Example 11.6 there exist
examples of pointed tensor ∗-categories which are not unitarily equivalent to some Hermω
G.
Remark 13.8. In Sect. 11 we have constructed the unitarization AΩ1/2 associated to
a unitary discrete weak quasi-bialgebra A in the case where (Ω−1)
1/2
is a left inverse of
Ω
1/2
. This construction may be described categorically as follows. Let (F, F, G) be a
faithful weak quasi tensor ∗-functor of a semisimple unitary tensor category C and A the
associated unitary discrete weak quasi bialgebra with involution denoted (∗, Ω) following
Theorem 13.5. If this functor is non-unitary and for example we know that satisfies the
left inverse property (4.8) then we may consider the unitarized functor (F, F
′
, G′) as in
part a) of Prop. 4.22, see also Def. 4.23. This new structure in turn gives rise to a new
unitary weak quasi bialgebra B corresponding to the unitarization AΩ1/2 of A, by the proof
of Theorem 7.9 with trivial unitary structure by Cor. 11.12. This structure is also strongly
trivial by Prop. 4.21.
The notion of unitarization will have a useful extension in Sect. 30 in that will be applied
to more useful situations in subsequent sections.
We ask how to construct and parameterise faithful ∗-functors G : C → Hilb from a C
∗
-
category. If G is given, we may construct new ∗-functors to Hilb via a categorical analogue

100 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
of the twist deformation of the involution of an algebra of Prop. 11.14 in the following
way. Let t ∈ Nat0(G) be a positive invertible natural transformation and let Gt(ρ) be G(ρ)
as a vector space, but with modified inner product (ξ, η)t:= (ξ, tρη)G(ρ). The action of
Gt on morphisms is the same as that of G. The fact that G is ∗-preserving together with
naturality of t easily imply that Gtis ∗-preserving as well, hence a ∗-functor. The ∗-algebras
A = Nat0(G) and B = Nat0(Gt) are related by B = At.
Faithful functors F : C → Vec are described, up to isomorphism, by functions D :
Irr(C) → N thanks to Theorem 7.9 (a). We thus need to parameterize the ways how F can
be written as F = HG with G : C → Hilb is a ∗-functor and
H : Hilb → Vec
the forgetful functor.
Proposition 13.9. Let C be a C
∗
-category with finite dimensional morphism spaces and
F : C → Vec a faithful functor. Then F factors through F = HG where G : C → Hilb is a
faithful ∗-functor and H : Hilb → Vec the forgetful functor. Any other ∗-functor G
′ with
the same properties is of the form Gt for a unique positive invertible t ∈ Nat0(G).
Proof. We choose, for each ρ ∈ Irr(C), a positive inner product on F(ρ), and let G(ρ)
the corresponding Hilbert space. Note that F(T
∗
) = F(T)
∗ holds for T ∈ (ρ, ρ) for any
choice of inner product when ρ is irreducibile, since these morphisms are scalars and F
is linear. We use orthogonal complete reducibility of µ ∈ C via isometries Sρ,i ∈ (ρ, µ)
with ρ irreducibles, to extend the construction of a Hilbert space G(µ) to all objects µ via
(ξ, η)G(µ):= P
ρ,i(F(S
∗
ρ,i)ξ, F(S
∗
ρ,i)η)G(ρ)
. It follows that the inner product is independent
of the choice of the isometries Sρ,i. Letting G act as F on morphisms, one sees that
G(S
∗
ρ,i) = G(Sρ,i)
∗ and this implies G is ∗
-preserving. Another decomposition F = HG′
gives a new Hilbert space structure G
′
(ρ) on the same vector space as G(ρ), hence we may
find a unique positive invertible operator tρ on G(ρ) such that (ξ, η)G′(ρ) = (ξ, tρη)G(ρ). Since
G
′
is a ∗-functor, this implies that t ∈ Nat0(G).
□
We summarise the main results of this and previous sections.
Corollary 13.10. Let C be a tensor C
∗
-category with finite dimensional morphism spaces
and D a weak dimension function on C. Then there is a faithful weak quasi-tensor ∗-
functor G : C → Hilb such that D(ρ) = dim(G(ρ)). If A is the discrete unitary weak quasi
bialgebra corresponding to G via duality then all the others corresponding to different weak
quasi-tensor ∗-functors with the same dimension function are isomorphic to AF,t for some
twist F ∈ A ⊗ A and t ∈ A+ of the bialgebra and Ω-involutive structure of A respectively.
