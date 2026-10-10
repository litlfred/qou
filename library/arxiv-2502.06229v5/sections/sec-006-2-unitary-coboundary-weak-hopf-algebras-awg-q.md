---
doc_id: arxiv-2502.06229v5
doc_title: "Constructing equivalences between fusion categories of quantum groups and of vertex operator algebras via quantum gauge groups"
section_id: sec-006-2-unitary-coboundary-weak-hopf-algebras-awg-q
section_title: "Unitary coboundary weak Hopf algebras AW(g, q)"
section_number: 2
pages: 10-12
source_pdf: 2502.06229v5.pdf
source_sha256: 3499c40ea150a617
toc_source: outline
---
The notion of weak quasi-Hopf algebra was first introduced by Mack and Schomerus
motivated by the work of Drinfeld on quasi-Hopf algebras, specifically the Drinfeld-Kohno
theorem [70].
The weakness refers to a non-unital coproduct, and is needed to construct a coalgebra
structure on the quotient A of Uq(g) with q a root of unity by the ideal of elements
annihilated by representations with zero quantum dimension.
Since the ideal is not a
coideal, the quotient algebra A is not a bialgebra in the natural way. For sl2, Mack and
Schomerus defined a weak coproduct on A and an associator derived from the fusion rules
of the semisimple fusion category C(sl2, q), a counit and a natural antipode derived from
Uq(sl2), and have verified the axioms of a weak quasi-Hopf algebra on their example. Their
construction is based on the special multiplicity free fusion rules of the category. In [10]
we have extended Mack and Schomerus construction to all Lie types and to all roots of
unity of the unitary type–i.e. the roots of unity appearing in the statement of our main
Theorem 1.6–and we have derived algebraic and analytic properties that were overlooked
in the literature.
The main algebraic property that our quotient algebra AW(g, q) of Uq(g) satisfies is
that of being the Hopf counterpart of a weak quasi-Hopf algebra, in a position completely
analogous to Hopf algebras among quasi-Hopf algebras. For this reason, we shall refer to
AW(g, q) as a weak Hopf algebra. We have established the weak Hopf algebra structure
of AW(g, q) building upon the quantum group fusion category C(g, q) and Wenzl’s linear
fibre functor W associated to it [99].
Here we limit ourselves to recall the axioms of the definition of weak Hopf algebra which
mostly differ from those of Hopf algebras. For the complete properties of antipode, counit
and R-matrix of weak Hopf algebras we refer the reader to Sects. 9–14 of [10].
Definition 2.1. Let A be a semisimple unital complex algebra endowed with a coproduct
∆: A →A⊗A given by a not necessarily unital homomorphism and a counit satisfying the
usual counit axioms for bialgebras. The tensor product ρ⊗σ of two f.d. representations of
A is the representation defined by ∆restricted to the range of ∆(I) in the tensor product
space.
We call A a weak bialgebra if the category Rep(A) of representations of A becomes a
tensor category with associativity morphisms
αρ,σ,τ : (ρ ⊗σ) ⊗τ →ρ ⊗(σ ⊗τ),
ρ, σ, τ ∈Rep(A)
defined by the action of 1 ⊗∆(∆(I))∆⊗1(∆(I)) between the representation spaces, with
I the unit of the algebra, and 1 the identity map. In particular, if the coproduct is unital,
A is a coassociative bialgebra.
A weak Hopf algebra is a weak bialgebra endowed with an antipode S : A →A satisfying
the axioms of a Hopf algebra antipode.
Among weak quasi-bialgebras, weak bialgebras admit a characterization in terms of weak
tensoriality of their fibre functor.
11
Proposition 2.2. A semisimple weak quasi-bialgebra A is a weak bialgebra if and only if
the fibre functor F : Rep(A) →Vec is a weak tensor functor. By this we mean that the
associated natural transformations given by projection and inclusion, respectively:
Fρ,σ : F(ρ) ⊗F(σ) →F(ρ ⊗σ)
and
Gρ,σ : F(ρ ⊗σ) →F(ρ) ⊗F(σ)
satisfy for all objects ρ, σ, τ,
Fρ,σ ◦Gρ,σ = 1F(ρ⊗σ)
(2.1)
Fρ′,σ′ ◦F(S) ⊗F(T) = F(S ⊗T) ◦Fρ,σ,
F(S) ⊗F(T) ◦Gρ,σ = Gρ′,σ′ ◦F(S ⊗T)
(2.2)
for objects ρ, σ, ρ′, σ′ ∈C and morphisms S : ρ →ρ′, T : σ →σ′.
F(αρ,σ,τ) = Fρ,σ⊗τ ◦1F(ρ) ⊗Fσ,τ ◦α′
F(ρ),F(σ),F(τ) ◦Gρ,σ ⊗1F(τ) ◦Gρ⊗σ,τ
(2.3)
F(α−1
ρ,σ,τ) = Fρ⊗σ,τ ◦Fρ,σ ⊗1F(τ) ◦α′−1
F(ρ),F(σ),F(τ) ◦1F(ρ) ⊗Gσ,τ ◦Gρ,σ⊗τ,
(2.4)
where α are the associativity morphisms of Rep(A) defined by the associator of A, and α′
are the (trivial) associativity morphisms of Vec.
We refer to Sect. 6, 7, 10 in [10] for the general definition of weak quasi-Hopf algebra,
their R-matrix how to obtain a rigid braided tensor category from it. This structure of
weak quasi-Hopf algebra is stable under a twist operation–first introduced by Drinfeld for
quasi-Hopf algebras–. The twist of a weak quasi-Hopf algebra is automatically a weak
quasi-Hopf algebra, and provides an equivalent rigid tensor category.
We next describe the properties concerning the unitary structure of weak quasi-Hopf
algebras that are most relevant for this paper.
Definition 2.3. A (compatible) unitary coboundary weak quasi-Hopf algebra A is defined
by the following data:
a) A unital weak quasi-Hopf algebra A endowed with a C∗-algebra involution with an
antipode (S, α, β)
b) a ribbon structure (R, v) for A associated to (S, α, β) such that the ribbon element
v ∈A is unitary,
c) a unitary central square root w ∈A of v such that ε(w) = 1, S(w) = w,
d) ˜A = Aop as quasitriangular weak quasi-bialgebras,
e) R = Rw−1 ⊗w−1∆(w) is positive.
The element R is the R-matrix; v ∈A is a central element defining the ribbon structure;
the operator R is Drinfeld coboundary matrix and gives the Ω-involution Ω= R in the
sense of Sect. 11, 12 in [10]. The Ω-involution induces a ∗-involution on Rep(A) making
it into a tensor ∗-category. In the case where the ∗-involution is induced by a coboundary
matrix, the braided symmetry of Rep(A) induced by the R-matrix is unitary by Theorem
27.9 in [10].
12
C. PINZARI
The triple (S, α, β) describes the antipode of a weak quasi-Hopf algebra, and makes
Rep(A) into a rigid category. The presence of invertible elements α, β is necessary in the
quasi-cases, it arises from twist deformations of the usual antipode of a Hopf algebra. If
A is weak Hopf algebra, its antipode is required to satisfy the same axioms as a Hopf
algebra antipode: is defined with α = β = I; ε denotes the counit and satisfies the same
axioms as in the Hopf algebra case; Aop and ˜A, denote the opposite and adjoint weak
quasi-Hopf algebras. The opposite structure Aop is widely used in the literature, while the
adjoint structure ˜A is defined by coproduct ˜∆(a) = ∆(a∗)∗, and similarly for the remaining
structure, see Sect. 10 in [10].
Except for the C∗-structure of the algebra and the positivity requirement of the cobound-
ary operator in e), the axioms are satisfied by the ∗-algebra of Uq(g), which for this reason
represents the motivating example of our definition. These properties of Uq(g) and positiv-
ity of a truncated coboundary operator operator of Uq(g) on certain special tensor products
are due to Wenzl [99], see also Sect. 30 in [10].
Compatible unitary weak quasi-Hopf algebras in the sense of Definition 2.3 have been
introduced and studied in Sect. 29 of [10]. They satisfy the stronger property d) than
their weaker variant considered in Sect. 27 of the same paper, where d) is relaxed up to a
so called trivial twist. If the coproduct is unital, the two definitions coincide. We do not
have examples in the weak case that distinguishes among the two definitions.
The weaker variant is interesting for the fact that it admits a categorical characteriza-
tion extending the notion of symmetric fibre functor –a core notion in Doplicher-Roberts
theory.– to the coboundary symmetry induced by R in Rep(A). The stronger notion on
the other hand allows a formulation of an abstract Drinfeld-Kohno theorem, see Theorem
29.4 in [10], that we use in our main theorem. In this paper we shall not need the weaker
version, therefore we shall always assume the compatibility condition given by property d)
when not clearly stated.
In [99] Wenzl has constructed a linear ∗-functor
W : C(g, q) →Hilb.
The following result has been shown in Theorem 31.16 in [10].
Theorem 2.4. The semisimple ∗-algebra AW(g, q) := Nat(W) of natural transformations
of W admits a natural structure of unitary compatible coboundary weak Hopf algebra derived
from C(g, q) and W.
Thanks to Theorem 29.4 in [10]–our version of Drinfeld-Kohno theorem–the Zhu algebras
A(Vgk) become unitary coboundary weak quasi-Hopf algebras with a Drinfeld twist from
AW(g, q), by our version of Drinfeld-Kohno theorem. This is summarized in the following
section, and detailed in Sect. 33 of [10].
