---
doc_id: arxiv-math-0203206v1
doc_title: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories"
section_id: sec-013-2-ι-εab-1-ab
section_title: "(ι ⊗ε)(∆(a)(b ⊗ 1)) = ab,"
section_number: 2
pages: 7-9
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
doc_brief: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups"
---
3. m(S ⊗ι)(∆(a)(1 ⊗b)) = ε(a)b,
4. m(ι ⊗S)(∆(a)(b ⊗ 1)) = ε(a)b
for all a,b ∈A. We call ε the counit and S the coinverse. Conversely, if (A⊗1)∆( A) ⊂A⊗A and (A⊗1)∆( A) ⊂
A ⊗A and there exist linear maps ε : A → C and S : A → A satisfying properties 1-4 with S invertible, then
(A, ∆) is a multiplier Hopf ∗-algebra.
We denote mop = mσ and ∆ op = σ∆ where σ(a ⊗b) = b ⊗a is the ﬂip ∗-automorphism of A ⊗A and
M (A ⊗A). Aop denotes the vector space A with multiplication mop. The following result follows easily from
the uniqueness of the counit and coinverse.
Proposition 2.5 The antipode S is invertible and
1. S−1(a) = S(a∗)∗ ∀a ∈A.
2. (S ⊗S)(∆(a)(1 ⊗b)) = (1 ⊗S(b))∆ opS(a) ∀a,b ∈A.
3. εS =ε.
4. (Aop, ∆) and (A, ∆ op) are multiplier Hopf ∗-algebras with counit ε and coinverse S−1.
Definition 2.6 A linear functional ω on a multiplier Hopf ∗-algebra (A, ∆) is called
1. positive iﬀ ω(a∗a) ≥ 0 ∀a ∈A,
2. faithful iﬀ it is positive and ω(a∗a) = 0 ⇒a = 0 ∀a ∈A,
3. left-invariant iﬀ (ι ⊗ω)(∆(a)(b ⊗ 1)) = ω(a)b ∀a,b ∈A,
4. right-invariant iﬀ (ω ⊗ι)((1 ⊗b)∆( a)) = ω(a)b ∀a,b ∈A.
Thusω is left-invariant iﬀ ωS is right-invariant.
Definition 2.7 An aqg is a multiplier Hopf ∗-algebra (A, ∆) which admits a non-zero left-invariant positive
linear functional ϕ.
Theorem 2.8 Let (A, ∆) be an aqg with positive left-invariant functional ϕ. Then
1. ϕ is faithful.
7
2. If ω is a left-invariant functional, there exists c ∈ C such that ω =cϕ.
3. If ω is a right-invariant functional, there exists c ∈ C such that ω =cϕS.
An immediate consequence is that the ∗-operation is positive, viz. a∗a = 0 ⇒ a = 0, which clearly is
stronger than non-degeneracy. Furthermore, there exists a u nique complex number µ such that ϕS2 =µϕ. It
can be proved that |µ| = 1, but it has recently been discovered that µ ⁄= 1 for the quantum group version of
ax +b [38]. Every aqg ( A, ∆) has the property that to any a ∈ A, there exists c ∈ A such that ac = ca = a.
Two aqg are said to be isomorphic if they are isomorphic as multiplier Hopf ∗-algebras and we use the same
notation ∼= to denote this.
Set ψ = ϕS. Then ψ is a non-zero right-invariant linear functional on A. However, in general, ψ will not
be positive. It is known that there exists a non-zero positive right- invariant linear functional on A. To ϕ there
existence a unique automorphism ρ onA such that ϕ(ab) = ϕ(bρ(a)), for every a,b ∈A. We refer to this as the
weak KMS-property of ϕ. Moreover, we have ∆ ρ = (S2 ⊗ρ)∆ and ρ(ρ(a∗)∗) = a, for every a ∈A. Also there
exists an automorphism ρ′ for the right-invariant functional ψ, that is, ρ′ is an automorphism on A such that
ψ(ab) = ψ(bρ′(a)), for every a,b ∈A.
It is possible to introduce a modular function for aqg. It is an invertib le element δ in M (A) such that
(ϕ ⊗ι)(∆(a)(1 ⊗b)) = ϕ(a)δb, for every a,b ∈A. This modular function satisﬁes
∆( δ) = δ ⊗δ, ε (δ) = 1, S (δ) = δ−1.
As in the classical case we have
ϕ(S(a)) = ϕ(aδ) = µϕ(δa) ∀a ∈A.
We now discuss duality within the category of aqg. Deﬁne a subspace ˆA of A′ by
ˆA = {ϕa | a ∈A} = {aϕ | a ∈A}.
Then ˆA is a non-degenerate ∗-algebra under the deﬁnitions:
1. For every ω1,ω 2 ∈ ˆA and a ∈A, we have (ω1ω2)(a) = (ω1 ⊗ω2)(∆(a)).
2. For every ω ∈ ˆA and a ∈A, deﬁne ω∗(a) = ω(S(a)∗).
The comultiplication ˆ∆ is deﬁned on ˆA by ˆ∆( ω)(x ⊗y) = ω(xy), for every ω ∈ ˆA and x,y ∈A. For this to
make sense, M (A ⊗A) should be embedded in ( A ⊗A)′ in a proper way. A deﬁnition of the comultiplication
ˆ∆ that does not use such an embedding can be found in [18]. Then ( ˆA, ˆ∆) is a multiplier Hopf ∗-algebra with
counit ˆε and the antipode ˆS given by:
1. ˆε(ω) = ω(1), for every ω ∈ ˆA.
2. ˆS(ω)(a) = ω(S(a)), for every ω ∈ ˆA and a ∈A.
Deﬁne ˆa =aϕ ∈ ˆA, for a ∈A. The map A → ˆA sendinga to ˆa is a bijection, and is referred to as the Fourier
transform. Next deﬁne the linear functional ˆψ on ˆA by setting ˆψ(ˆa) = ε(a), for every a ∈ A. It is possible
to prove that ˆψ is right-invariant, and that ˆψ(ˆa∗ˆa) = ϕ(a∗a), for every a ∈ A. It follows that ˆψ is a non-zero
positive linear functional on ˆA, and that the dual ( ˆA, ˆ∆) is an aqg. Let ˆ ρ denote the automorphism of ˆA such
that ˆψ(ˆaˆb) = ˆψ(ˆb ˆρ(ˆa)), for all a,b ∈ A. The aqg version of Pontryagin’s duality theorem takes the following
form:
Theorem 2.9 Let (A, ∆) be an aqg. Then the double dual ( ˆAˆ, ˆ∆ˆ ) is an aqg isomorphic to (A, ∆) . More
precisely, there exists a canonical ∗-isomorphism θ :A → ˆˆA such that θ(a)(ω) = ω(a), for all a ∈ ˆA, and that
satisﬁes the equation (θ ⊗θ)∆ = ˆˆ∆ θ.
8
Note that an aqg ( A, ∆) is commutative iﬀ ( ˆA, ˆ∆) is cocommutative.
We shall need to consider an object associated to an aqg called its an alytic extension. See [20] for full details.
If A is a C*-algebra, then M (A) denotes the usual multiplier algebra of A, and ∗-homomorphism between C*-
algebras are assumed to be non-degenerate in the usual operato r algebraic sense. We need ﬁrst to recall the
concept of a GNS pair. Suppose given a positive linear functional ω on a ∗-algebraA. Let H be a Hilbert space,
and let Λ : A →H be a linear map with dense range for which (Λ( a), Λ(b)) = ω(b∗a), for all a,b ∈A. Then we
call (H, Λ) a GNS pair associated to ω. As is well known, such a pair always exists and is essentially unique.
Ifϕ is a left Haar integral on an aqg ( A, ∆), and ( H, Λ) is an associated GNS pair, then it can be shown that
there is a unique ∗-homomorphism π : A →B(H) such that π(a)Λ(b) = Λ( ab), for all a,b ∈A. Moreover, π is
faithful and non-degenerate. We let Ar denote the norm closure of π(A) in B(H). Thus, Ar is a non-degenerate
C*-subalgebra of B(H). There exists a unique non-degenerate ∗-homomorphism ∆ r :Ar →M (Ar ⊗Ar) such
that, for all a ∈A and all x ∈A ⊗A, we have ∆ r(π(a))(π ⊗π)(x) = (π ⊗π)(∆(a)x) and (π ⊗π)(x)∆ r(π(a)) =
(π ⊗π)(x∆( a)).
Deﬁne a linear map ˆΛ : ˆA →H by setting ˆΛ(ˆa) = Λ( a), for all a ∈ A. Since ˆψ(ˆb∗ˆa) = ϕ(b∗a) = (Λ( a), Λ(b)),
for alla,b ∈A, it follows that (H, ˆΛ) is a GNS-pair associated to ˆψ. It can be shown that it is unitarily equivalent
to the GNS-pair for a left Haar integral ˆ ϕ of ( ˆA, ˆ∆). Hence, we can use ( H, ˆΛ) to deﬁne a representation of the
analytic extension ( ˆAr, ˆ∆ r) of ( ˆA, ˆ∆) on the space H. There is a unique ∗-homomorphism ˆπr : ˆA →B(H) such
that ˆπr(a)ˆΛ(b) = ˆΛ(ab), for all a,b ∈ ˆA. Moreover, ˆπ is faithful and non-degenerate. Let ˆAr be the norm closure
of ˆπr(A) in B(H), so ˆAr is a non-degenerate C*-subalgebra of B(H). There exist a unique ∗-homomorphism
ˆ∆ r : ˆAr → M ( ˆAr ⊗ ˆAr) such that, for all a ∈ ˆA and x ∈ ˆA ⊗ ˆA, ˆ∆ r(ˆπ(a))(ˆπ ⊗ ˆπ)(x) = (ˆπ ⊗ ˆπ)( ˆ∆( a)x) and
(ˆπ ⊗ ˆπ)(x) ˆ∆ r(ˆπ(a)) = (ˆπ ⊗ ˆπ)(x ˆ∆( a)).
