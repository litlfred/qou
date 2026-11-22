---
doc_id: arxiv-1707.00196v3
doc_title: "Yang-Baxter representations of the inﬁnite symmetric group"
section_id: sec-009-51-r-matrices-and-k-theory
section_title: "R-matrices and K-theory"
section_number: 5.1
pages: 22-25
source_pdf: 1707.00196v3.pdf
source_sha256: 9908b71521275b17
toc_source: outline
doc_brief: "Yang-Baxter representations of the inﬁnite symmetric group — Every unitary involutive solution of the quantum Yang-Baxter equation (R- matrix) deﬁnes an extremal character and a representation of the"
---
R-matrices and K-theory
In this section we extend the previously deﬁned ρR to a ∗-homomorphism of C∗-
algebras, ρR : C∗S∞→E∞, where E∞is the C∗-algebraic counterpart of the alge-
bra E from Section 3. On K-theory the map ρR will induce a ring homomorphism
ρR∗: K0(C∗S∞) →Z[1
d] with d = dim(V ). The equivalence relation introduced in
Def. 1.1 will then translate into the approximate unitary equivalence of the corre-
sponding ∗-homomorphisms. In fact, when the invariant ρR∗is composed with the
canonical inclusion Z[1
d] ⊂R it is an indecomposable ﬁnite trace on K0(C∗S∞) in
the sense of Kerov and Vershik and we recover [34, Thm. 2.3] from the Yang-Baxter
equation. For the basic facts about UHF-algebras that we use we refer the reader to
[42].
Let R ∈R0(V ), let d = dim(V ) and denote the associated unitary representation
of Sn by ρ(n)
R . We obtain the following sequence of ∗-homomorphisms, which we will
continue to denote ρ(n)
R :
ρ(n)
R : C∗Sn = C[Sn] →End(V ⊗n)
Let E∞be the C∗-algebra obtained as the inﬁnite tensor product of the algebras
End(V ), i.e. as the C∗-algebraic inductive limit
E∞= lim
−→
n
End(V ⊗n)
taken over the maps sending T to T ⊗idV . This is an inﬁnite UHF-algebra with
K0(E∞) ∼= Z[1
d] and K1(E∞) ∼= 0. The algebra E∞has a unique trace that restricts to
the normalized trace on End(V ⊗n). It induces an explicit isomorphism τ∗: K0(E∞) →
Z[1
d] as follows: Let p, q ∈MN(E∞) be projections. Then
τ∗([p] −[q]) = (TrN ⊗τ)(p) −(TrN ⊗τ)(q) ,
where TrN ⊗τ : MN(E∞) = MN(C) ⊗E∞→C is induced by the non-normalized
trace TrN tensored with τ. This is in fact a ring isomorphism. To understand the
ring structure on K0(E∞), note that E∞is strongly self-absorbing [43, Ex. 1.14]. In
particular, there is an isomorphism ψ: E∞⊗E∞→E∞and any two such isomorphisms
22
are homotopic. Let pi ∈MNi(E∞) for i ∈{1, 2} be projections and let [pi] ∈K0(E∞)
be the corresponding K-theory classes. Let ψ′ : MN1(E∞) ⊗MN2(E∞) →MN1N2(E∞)
be the isomorphism induced by ψ. Then we have [p1] · [p2] = [ψ′(p1 ⊗p2)]. It follows
from the uniqueness of the normalized trace on E∞that
(TrN1 ⊗τ) ⊗(TrN2 ⊗τ) = (TrN1N2 ⊗τ) ◦ψ′ ,
which implies τ∗([p1] · [p2]) = τ∗([p1]) · τ∗([p2]).
Note that E∞⊂E with E as in Section 3. The inductive limit of the representations
ρ(n)
R : C∗Sn →End(V ⊗n) provides us with a ∗-homomorphism
ρR : C∗S∞→E∞.
(5.1)
The K-theory of C∗S∞was studied by Kerov and Vershik in [34]. In particular,
they obtained that K0(C∗S∞) is isomorphic to a quotient of the ring of symmetric
functions. As an abelian group it is therefore spanned by projections pλ ∈K0(C∗S∞),
that are labeled by partitions λ = [λ1, . . . , λk] of natural numbers n ∈N. The map
ρR induces a group homomorphism
ρR∗: K0(C∗S∞) →K0(E∞)
(5.2)
in K-theory.
Using the ring isomorphism induced by the unique trace on E∞we
will identify K0(E∞) with Z[1
d]. The following lemma shows that ρR∗remembers the
equivalence class of R.
Lemma 5.1. Let λ be a partition of n ∈N. We will identify λ with the corresponding
irreducible representation of Sn. On the projection pλ ∈C∗S∞associated to λ the
value of ρR∗is given by
ρR∗([pλ]) = 1
dn ⟨λ, ρ(n)
R ⟩,
where ⟨λ, µ⟩denotes the multiplicity of the irreducible representation λ in the repre-
sentation µ.
Proof. We have ρR∗([pλ]) = τ(ρR(pλ)). Let τn : End(V ⊗n) →C be the normalized
trace. Since pλ ∈C∗Sn ⊂C∗S∞and the inclusion End(V ⊗n) →E∞preserves the
normalized trace, we obtain
τ(ρR(pλ)) = τn(ρ(n)
R (pλ)) = 1
dn TrV ⊗n(ρ(n)
R (pλ)) .
Let VR = V ⊗n be the representation space of ρ(n)
R . The decomposition into its irre-
ducible components gives
VR ∼=
M
µ∈Irrep(Sn)
homC∗Sn(Vµ, VR) ⊗Vµ ,
where the action on the left is via ρ(n)
R
and on the right acts only on the second tensor
factor Vµ via µ. Observe that pλVµ is zero for λ̸ = µ and 1-dimensional for λ = µ.
Hence,
TrV ⊗n(ρ(n)
R (pλ)) = dim(ρ(n)
R (pλ)VR) = dim(homC∗Sn(Vλ, VR) ⊗pλVλ)
= dim(homC∗Sn(Vλ, VR)) = ⟨λ, ρ(n)
R ⟩.
23
From this we obtain two useful additional characterizations of the equivalence
relation from Def. 1.1, one of them K-theoretic, the other one C∗-algebraic. For the
second one we need the following equivalence relation [42, Def. 1.1.15]:
Deﬁnition 5.2. Let ϕ, ψ: A →B be ∗-homomorphisms between separable unital C∗-
algebras A and B.
We call them approximately unitarily equivalent if there is a
sequence of unitaries un ∈B with the property that for all a ∈A we have
lim
n→∞∥ϕ(a) −un ψ(a) u∗
n∥= 0 .
We denote this by ϕ ≈u ψ.
Theorem 5.3. Let R, S ∈R0(V ). The following are equivalent:
i) R ∼S,
ii) ρR∗= ρS∗,
iii) ρR ≈u ρS.
Proof. The equivalence of i) and ii) is a consequence of Lemma 5.1 and the fact that
ρ(n)
R and ρ(n)
S
are unitarily equivalent if and only if the multiplicities of their irreducible
subrepresentations agree.
To see that ii) and iii) are equivalent, note that the C∗-algebras C∗S∞and E∞
are both AF-algebras. The statement then follows from [42, Prop. 1.3.4].
The K-group K0(C∗S∞) is in fact a ring: Let λ be a partition of n ∈N and let
µ be a partition of m ∈N. Denote by pλ, pµ ∈C∗S∞the associated projections.
Let ιn,m : C∗Sn ⊗C∗Sm →C∗Sn+m be the ∗-homomorphism induced by the inclusion
Sn×Sm →Sn+m, where Sn permutes the ﬁrst n elements and Sm the last m elements.
The product [pλ] · [pµ] is then deﬁned to be the class of the projection ιn,m(pλ ⊗pµ) ∈
C∗Sn+m ⊂C∗S∞in K0(C∗S∞). With respect to this ring structure we make the
following observation:
Proposition 5.4. Let R ∈R0(V ). Then the associated K-theory invariant
ρR∗: K0(C∗S∞) →Z[1
d]
is a ring homomorphism.
Proof. Let λ, µ be partitions of n, m ∈N respectively. Let pλ ∈C∗Sn, pµ ∈C∗Sm
be the corresponding projections. Since the representations ρ(n)
R
arise from the same
R-matrix, we have ρ(n+m)
R
◦ιn,m = ρ(n)
R ⊗ρ(m)
R . Hence, we obtain
ρR∗([pλ] · [pλ]) = [ρ(n+m)
R
◦ιn,m(pλ ⊗pµ)] = [ρ(n)
R (pλ) ⊗ρ(m)
R (pµ)]
and after application of the isomorphism τ∗: K0(E∞) →Z[1
d] induced by the trace:
τ∗(ρR∗([pλ] · [pλ])) = τn+m(ρ(n)
R (pλ) ⊗ρ(m)
R (pµ))
= τn(ρ(n)
R (pλ)) τm(ρ(m)
R (pµ)) = τ∗(ρR∗([pλ])) · τ∗(ρR∗([pµ]))
where τr : End(V ⊗r) →C denotes the (normalized) trace on the matrix algebra and
we used that the inclusion End(V ⊗r) ⊂E∞is trace preserving.
Finite traces on K0(C∗S∞) have been studied by Kerov and Vershik in [34] and
ρR∗can be seen as a reﬁnement of such a trace taking values in Z[1
d]. In particular, we
recover the multiplicativity proven in [34, Thm. 2.3] in Prop. 5.4. From the point of
view of C∗-algebras it is remarkable that we obtain a ring homomorphism on K-theory
that is induced by a ∗-homomorphism.
24
