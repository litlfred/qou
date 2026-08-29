---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-025-511-sphericity-of-pivotalization
section_title: "Sphericity of pivotalization"
section_number: 5.11
pages: 22-24
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in pa rtic- ular, the theory of weak Hopf algebras), we prove a number of g eneral results about fusion categories in"
---
have a positive characteristic, diﬀerent from 2.
LetA be a quasitriangular weak Hopf algebra, i.e., such that Rep( A) is a braided
monoidal category. Let R ∈ (A ⊗A)∆(1) be the R-matrix of A. It was shown in
ON FUSION CATEGORIES 23
[NTV] that the Drinfeld element u = S(R(2))R(1) is invertible, satisﬁes S2(h) =
uhu−1 for all h in A, and
(28) ∆( u−1) = R21R(u−1 ⊗u−1).
Furthermore, the element uS(u)−1 is group-like and implements S4 via the adjoint
action.
Observe that for any group-like elementη ∈G(A∗) the elementgη = R(1)⟨η, R(2) ⟩
is group-like in A and the map η ↦→gη is a group homomorphism from G(A∗) to
G(Aop).
Recall that distingusihed elments of A andA∗ were deﬁned in Section 4.2. In the
next Lemma we extend a result of Radford [R2] relating the distingu ished elements
and uS(u)−1.
Lemma 5.12. Leta ∈A andα ∈A∗ be a pair of distinguished group-like elements
chosen as in Section 4.2. Then gαa =S(u)u−1.
Proof. Letℓ ∈A be a non-degenerate integral from which a andα are constructed.
It follows from [N, Section 5] that
ℓ(2) ⊗ℓ(1) = ℓ(1) ⊗S2(ℓ(2))a−1
ℓ(1)h ⊗ℓ(2) = ℓ(1) ⊗ℓ(2)S(h↼α ), h ∈A.
Using these identities and properties of integrals and R-matrices we compute
ℓ(2)S(R(2) ↼α )R(1) ⊗ℓ(1) = ℓ(2)R(1) ⊗ℓ(1)R(2)
= R(1)ℓ(1) ⊗ R(2)ℓ(2)
= R(1)S(R(2))ℓ(1) ⊗ℓ(2)
= R(1)S(R(2))S2(ℓ(2))a−1 ⊗ℓ(1),
whence S(R(2) ↼ α)R(1) = R(1)S(R(2))a−1 = S(u)a−1 by non-degeneracy of ℓ.
On the other hand, from the axioms of R-matrix we have S(R(2) ↼ α)R(1) =
S(R(2))R(1)gα =ugα, which completes the proof. □
Recall [NTV, Section 7] that a central ν ∈A is a ribbon element if ν =S(ν) and
∆( ν) = R21R(ν ⊗ν). A quasitriangular weak Hopf algebra A has a ribbon element
if and only if Rep( A) is a ribbon category.
Corollary 5.13. Suppose thatA is a unimodular quasitriangular weak Hopf algebra
and that α is gauged to be ǫ. If g ∈A is a group-like element such that g2 = a−1
and S2(h) = ghg −1 for all h ∈A then ν =u−1g is a ribbon element of A.
Proof. In this case we have gα = 1. Since both u andg implementS2, the element
ν is central. It follows from Equation (28) that ∆( ν) = R21R(ν ⊗ν). Finally,
S(ν) = S(u)−1g−1 =u−1g =ν by Lemma 5.12. □
Recall that in Remark 3.1, it was shown that to every fusion categor y C one can
associate a twice bigger fusion category ˜C, which has a canonical pivotal structure.
Proposition 5.14. If dim C ⁄= 0 then the canonical pivotal stucture of the category
˜C is in fact a spherical structure.
Proof. Let us realize ˜C as the representation category of a regular weak Hopf algebra
A. In this case, the pivotal structure of ˜C is deﬁned by a grouplike element g ∈A,
such that g2 =a−1, where a is the distinguished group-like element of A. Assume
24 PA VEL ETINGOF, DMITRI NIKSHYCH, AND VIKTOR OSTRIK
that the distinguished group-like element α ∈ A∗ is gauged to be ǫ. Consider the
Drinfeld center Z( ˜C), i.e., the representation category of the Drinfeld double D(A).
One can check that a is also the distinguished grouplike element for D(A). Since
g is a grouplike element such that gxg −1 =S2(x) for x ∈D(A), and g2 =a−1, it
follows from Corollary 5.13 that D(A) is ribbon, hence, Z( ˜C) is ribbon.
Thus, we have dim(V ) = dim(V ∗) inZ( ˜C) [K]. Hence, the same holds in ˜C (i.e., ˜C
is spherical). Indeed, let I : ˜C → Z( ˜C) be the induction functor deﬁned in subsection
5.8. Then by Proposition 5.4, for any V ∈ ˜C, I(V ) = ⊕X∈Irr ( ˜C)X ⊗V ⊗X ∗ as an
object of ˜C. Hence, dim I(V ) = dim V dim ˜C. On the other hand, I(V )∗ = I(V ∗),
which implies the statement. □
Corollary 5.15. In any pivotal fusion category C over C, the dimension of a simple
object is a positive number times a root of unity.
Proof. Consider the category ˜C. It has two pivotal structures b1,b 2 : V → V ∗∗.
Namely,b1 comes from C andb2 is the canonical pivotal structure. By Proposition
5.14, b2 is spherical. On the other hand, b−1
2 ◦b1 is a tensor endomorphism of the
identity functor, which obviously acts by roots of unity on simple obj ects. This
implies the statement. □
