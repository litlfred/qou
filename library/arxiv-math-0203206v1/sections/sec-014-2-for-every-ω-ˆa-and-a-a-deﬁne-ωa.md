---
doc_id: arxiv-math-0203206v1
doc_title: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories"
section_id: sec-014-2-for-every-ω-ˆa-and-a-a-deﬁne-ωa
section_title: "For every ω ∈ ˆA and a ∈A, deﬁne ω∗(a) ="
section_number: 2
pages: 8-9
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
doc_brief: "Representations of Algebraic Quantum Groups and Reconstruction Theorems for Tensor Categories — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups"
---
ω(S(a)∗).
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
satisﬁes the equation (θ ⊗θ)∆ = ˆ
ˆ∆ θ.
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
