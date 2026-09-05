---
doc_id: arxiv-math-0006057v2
doc_title: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS"
section_id: sec-047-91-a-galois-correspondence-the-following-simple
section_title: "A Galois correspondence. The following simple observation gives a natural"
section_number: 9.1
pages: 37-38
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
doc_brief: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS — W e give a survey of the theory of ﬁnite quantum groupoids (wea k Hopf algebras), including foundations of the theory and app lications to ﬁnite"
---
passage from arbitrary ﬁnite depth subfactors to depth 2 subfa ctors.
Proposition 9.1.1. For all k ≥ 0 the inclusion N ⊂ Mk has depth d + 1, where
d is the smallest positive integer ≥ n−1
k+1 . In particular, N ⊂ Mi has depth 2 for
all i ≥n − 2, i.e., any ﬁnite depth subfactor is an intermediate subfact or of some
depth 2 inclusion.
Proof. Note that dim Z(N ′ ∩Mi) = dimZ(N ′ ∩Mi+2) for all i ≥n − 2. By [PP2],
the tower of basic construction for N ⊂Mk is
N ⊂Mk ⊂M2k+1 ⊂M3k+2 ⊂ · · · ,
therefore, the depth of this inclusion is equal to d + 1, where d is the smallest
positive integer such that d(k + 1) − 1 ≥n − 2.
This result means that N ⊂M can be realized as an intermediate subfactor of
a crossed product inclusion N ⊂N>⊳B for some quantum groupoid B :
N ⊂M ⊂N>⊳B.
Recall that in the case of a Kac algebra action there is a Galois corres pondence
between intermediate von Neumann subalgebras of N ⊂ N>⊳B and left coideal
∗-subalgebras of B [ILP],[E1]. Thus, it is natural to ask about a quantum groupoid
analogue of this correspondence.
A unital ∗-subalgebra I ⊂ B such that ∆( I) ⊂ B ⊗I (resp. ∆( I) ⊂ I ⊗B)
is said to be a left (resp. right) coideal ∗-subalgebra. The set ℓ(B) of left coideal
∗-subalgebras is a lattice under the usual operations:
I1 ∧I2 =I1 ∩I2, I 1 ∨I2 = (I1 ∪I2)′′
for all I1,I 2 ∈ ℓ(B). The smallest element of ℓ(B) is Bt and the greatest element
is B. I ∈ℓ(B) is said to be connected if Z(I) ∩Bs = C.
To justify this deﬁnition, note that if I =B, then this is precisely the deﬁnition
of a connected quantum groupoid, and if I =Bt, then this deﬁnition is equivalent
to ˆB being connected ([N1], 3.10, 3.11, [BNSz], 2.4).
On the other hand, the set ℓ(M1 ⊂M2) of intermediate von Neumann subalge-
bras of M1 ⊂M2 also forms a lattice under the operations
K1 ∧K2 =K1 ∩K2, K 1 ∨K2 = (K1 ∪K2)′′
for all K1,K 2 ∈ ℓ(M1 ⊂ M2). The smallest element of this lattice is M1 and the
greatest element is M2.
Given a left (resp. right) action of B on a von Neumann algebra N , we will
denote (by an abuse of notation)
N>⊳I = span{[x ⊗b] |x ∈N, b∈I} ⊂ N>⊳B.
The next theorem establishes a Galois correspondence, i.e., a lattice isomorphism
betweenℓ(M1 ⊂M2) and ℓ(B).
Theorem 9.1.2. Let N ⊂ M ⊂ M1 ⊂ M2 ⊂ · · · be the tower constructed from a
depth 2 subfactor N ⊂M , B = M ′ ∩M2 be the corresponding quantum groupoid,
and θ be the isomorphism between M1>⊳B and M2 (Proposition 8.3.3). Then
φ : ℓ(M1 ⊂M2) →ℓ(B) : K ↦→θ−1(M ′ ∩K) ⊂B
ψ : ℓ(B) →ℓ(M1 ⊂M2) : I ↦→θ(M1>⊳I) ⊂M2.
deﬁne isomorphisms between ℓ(M1 ⊂M2) and ℓ(B) inverse to each other.
38 DMITRI NIKSHYCH AND LEONID V AINERMAN
Proof. First, let us check that φ and ψ are indeed maps between the speciﬁed
lattices. It follows from the deﬁnition of the crossed product that M1>⊳I is a von
Neumann subalgebra of M1>⊳B, therefore θ(M1>⊳I) is a von Neumann subalgebra
of M2 =θ(M1>⊳B), so ψ is a map to ℓ(M1 ⊂M2). To show that φ maps to ℓ(B),
let us show that the annihilator ( M ′ ∩K)0 ⊂ ˆB is a left ideal in ˆB.
For all x ∈A, y∈ (M ′ ∩K)0, and b ∈M ′ ∩K we have
⟨xy, b⟩ = λ−2τ (xye2e1wb) = λ−2τ (ye2e1wbx)
= λ−3τ (ye2e1EM ′ (e1wbx)) = ⟨y, λ−1EM ′ (e1wbx) ⟩,
and it remains to show that EM ′ (e1wbx) ∈M ′ ∩K. By ([GHJ], 4.2.7), the square
K ⊂ M2
∪ ∪
M ′ ∩K ⊂ M ′ ∩M2
is commuting, so EM ′ (K) ⊂M ′ ∩K. Since e1wbx ∈K, then xy ∈ (M ′ ∩K)0, i.e.,
(M ′ ∩K)0 is a left ideal and φ(K) = θ−1(M ′ ∩K) is a left coideal ∗-subalgebra.
Clearly, φ and ψ preserve ∧ and ∨, moreover φ(M1) = Bt, φ(M2) = B and
ψ(Bt) = M1, ψ(B) = M2, therefore they are morphisms of lattices.
To see that they are inverses for each other, we ﬁrst observe th at the condition
ψ ◦φ = id is equivalent to M1(M ′ ∩K) = K, and the latter follows from applying
the conditional expectation EK to M1(M ′ ∩M2) = M1B = M2. The condition
φ ◦ψ = id translates into θ(I) = M ′ ∩θ(M1>⊳I). If b ∈I, x∈M =M B
1 , then
θ(b)x = θ([1 ⊗b][x ⊗ 1]) = θ([(b(1)⊲x ) ⊗b(2)])
= θ([x(1(2)⊲ 1) ⊗ε(1(1)b(1))b(2)]) = θ([x ⊗b]) = xθ(b),
i.e.,θ(I) commutes with M . Conversely, if x ∈M ′ ∩θ(M1>⊳I) ⊂B, then x =θ(y)
for some y ∈ (M1>⊳I) ∩B =I, therefore x ∈θ(I).
Corollary 9.1.3. ([NV3], 4.5)
(i) K =M>⊳I is a factor iﬀ Z(I) ∩Bs = C.
(ii) The inclusion M1 ⊂K =M1>⊳I is irreducible iﬀ Bs ∩I = C.
