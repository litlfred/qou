---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-036-810-cyclotomicity-of-dimension-functions
section_title: "Cyclotomicity of dimension functions"
section_number: 8.10
pages: 41-42
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in pa rtic- ular, the theory of weak Hopf algebras), we prove a number of g eneral results about fusion categories in"
---
induces a homomorphism of rings F :K(Z(C)) →K(C). It is clear that the image
of this map is contained in the center Z(K(C)) of the ring K(C).
Lemma 8.49. The map K(Z(C)) ⊗ Q →Z(K(C)) ⊗ Q is surjective.
Proof. Recall that I : C → Z(C) denotes the induction functor, that is the left
adjoint to the forgetful functor Z(C) → C . We will denote the induced map K(C) →
K(Z(C)) by the same letter. Let bi be the basis of K(C). We have by Proposition
5.4 F (I(x)) = ∑
ibixb∗
i for any x ∈K(C). In particular for x ∈Z(K(C)) we have
F (I(x)) = x ∑
ibib∗
i . Finally note that the operator of multiplication by the element∑
ibib∗
i ∈Z(K(C)) is a self-adjoint positive deﬁnite operator K(C) →K(C) (with
respect to the usual scalar product deﬁned by ( bi,b ∗
j ) = δij) and hence invertible.
The Lemma is proved. □
Remark 8.50. In the special case C = Rep(H) for some Hopf algebra H Lemma
8.49 was proved in [KSZ] 6.3.
Theorem 8.51. Let C be a fusion category over C and let L be an irreducible
representation of K(C). There exists a root of unity ξ such that for any object X
of C one has Tr ([X],L ) ∈ Z[ξ].
Proof. First of all we can assume without loss of generality that the catego ry C
is spherical. Indeed as explained in Proposition 5.14 we can construct a spheri-
cal fusion category ˜C which projects onto C; moreover the map K( ˜C) → K(C) is
surjective and the simple objects of ˜C map to the simple objects of C.
42 PA VEL ETINGOF, DMITRI NIKSHYCH, AND VIKTOR OSTRIK
Now let C be spherical and let bi be the basis of K(C). The element eL =∑
i Tr(bi,L )b∗
i is proportional to a primitive central idempotent in K(C), see e.g.
[L] 19.2 (b). By Lemma 8.49 there exists a primitive central idempoten t ˜eL ∈
K(Z(C)) such that eL is proportional to F (˜eL). The element ˜eL can expressed in
terms of S−matrix of the category Z(C), see e.g. [BaKi]. By Theorem 10.1 there
exists a root of unity ξ such that the entries of S−matrix lie in Q(ξ) and thus
˜eL ∈K(Z(C)) ⊗ Q(ξ). Hence eL is proportional to some element of K(C) ⊗ Q(ξ).
Now the coeﬃcient of b0 = 1 ∈K(C) in eL equals to dim(L) ∈ Q(ξ) and is nonzero.
Hence eL ∈ K(C) ⊗ Q(ξ) and Tr( bi,L ) ∈ Q(ξ). Obviously the number Tr( bi,L )
is an algebraic integer and the ring of integers in Q(ξ) is Z[ξ]. The Theorem is
proved. □
Remark 8.52. Again in the case when C = Rep(H) for some Hopf algebra H
Theorem 8.51 is proved in [KSZ] 6.3.
Corollary 8.53. Any irreducible representation of K(C) is deﬁned over some
cyclotomic ﬁeld. In particular for any homomorphism φ : K(C) → C we have
φ(bi) ∈ Q[ξ] for some root of unity ξ.
Proof. Let Qab be the ﬁeld of all cyclotomic numbers. We already proved that
K(C) ⊗ Qab decomposes into direct sum of simple algebras (such decomposition
is the same as the decomposition of 1 ∈ K(C) into the sum of primitive central
idempotents). Now it is well known that the Brauer group of Qab is trivial. The
result follows. □
Corollary 8.54. Let C be a fusion category over C. There exists a root of unity ξ
such that for any object X of C one has FPdim(X) ∈ Z[ξ].
