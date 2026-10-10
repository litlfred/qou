---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-010-11-involution-and-c-structure
section_title: "Ω-involution and C*-structure"
section_number: 11
pages: 86-91
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
---
11. Ω-involution and C
∗
-structure
In this section we introduce a ∗-involution ∗: A → A to a weak quasi-Hopf algebra. In
the usual approach, among the compatibility conditions with the weak quasi-Hopf algebra
stucture, one requires for example that the involution and the coproduct commute. We
shall relax these compatibility conditions via the introduction of a twist Ω which is part of
the axioms of the involutive structure. There are several reasons to study such structures.
On one hand, unlike the ordinary approach, the more general notion is invariant under
Drinfeld twist operation A → AF . Another motivation for us arises from considering
natural examples, which include the Drinfeld-Jimbo quantum groups Uq(g) for the values
of the deformation parameter q with |q| = 1. Finally, as we shall see more precisely in
Sect. 13, Ω-involutions of weak quasi-Hopf algebras describe unitary structures in fusion
categories and intervene in the study of tensor ∗-equivalences.
Definition 11.1. A weak quasi bialgebra A will be called Ω-involutive if it is endowed
with a ∗-involution ∗: A → A making it into a ∗-algebra and a selfadjoint twist Ω ∈ A ⊗ A
such that A˜ = AΩ, with A˜ the adjoint weak quasi bialgebra defined in (10.8). Explicitly,
this means that Ω ∈ A ⊗ A is a partially invertible element satisfying
Ω
∗ = Ω, (11.1)
D(Ω) = ∆(I), R(Ω) = ∆(I)
∗
, (11.2)
∆(a
∗
) = Ω−1∆(a)
∗Ω, a ∈ A, (11.3)
ε ⊗ 1(Ω) = I = 1 ⊗ ε(Ω) (11.4)
Φ
∗−1 = I ⊗ Ω1 ⊗ ∆(Ω)Φ∆ ⊗ 1(Ω−1
)Ω−1 ⊗ I (11.5)
A unitary weak quasi bialgebra is an Ω-involutive weak quasi bialgebra such that A is
a C
∗
-algebra and Ω is positive in A ⊗ A. Note that Ω−1is also automatically positive.
Corresponding Hopf versions assume the existence of an antipode S. Note that in general
we require no compatibility assumption with the involution.
The most important relations are the intertwining property with the coproduct (11.3)
and the compatibility relation (11.5) between (∗, Ω) and the associator.
The notion of Ω-involution for a semisimple weak quasi-Hopf algebra is the most general
involutive structure that gives rise to a tensor ∗-category structure on the category of finite
dimensional representations of A. For example, we shall see that every fusion tensor ∗-
category (C
∗
-category) arises from a semisimple Ω-involutive (unitary) weak quasi-Hopf
algebra. We next recall several well known and important special notions.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 87
Remark 11.2. a) A is a Hopf ∗-bialgebra precisely when ∆(I) = I ⊗ I and Ω = I ⊗ I,
Φ = I ⊗I ⊗I. These structures are widely studied when A is a C
∗
-algebra in the operator
algebraic approach to quantum groups see e.g. [141], [168]. b) When A is a bialgebra
(∆(I) = I ⊗ I, Φ = I ⊗ I ⊗ I) (11.1) and (11.2) say that Ω is a selfadjoint invertible
element. Note that in this case (11.5) says that Ω is a 2-cocycle in the usual sense for
Hopf algebras. In the next proposition we discuss an extension of this property to weak
bialgebras. c) If A is as in b) and A is a C
∗
-algebra with Ω positive then the twisted
algebra AF , with F = Ω1/2is a quasi C
∗
-bialgebra in the sense of a). We shall shortly
consider an extension of the notion of triviality of Ω in the weak quasi bialgebras which is
the algebraic counterpart of the notion of unitary weak quasi-tensor functor of Def. 4.19.
d) When A is a quasi-bialgebra (that is ∆(I) = I ⊗ I and Φ non-trivial) we recover the
notion introduced by Gould and Lekatsas [72].
Example 11.3. The Hopf algebras Uq(g) for |q| = 1 considered by Wenzl in [185] are
for us important examples of Ω-involutive Hopf algebras with a non-trivial selfadjoint 2-
cocycle Ω in the sense of part b) of the previous remark. We shall discuss these examples
in Section 32. In this case, Ω is canonically induced by the R-matrix1. Furthermore, in
Sections 28, 30, 32 we shall construct new examples of semisimple Ω-involutive or unitary
weak Hopf algebras associated to Uq(g) for q a suitable root of unity, corresponding to the
associated unitary fusion categories.
We next extend the 2-cocycle property of Ω from bialgebras to weak bialgebras.
Proposition 11.4. If (∗, Ω) makes a weak bialgebra (A, ∆, ε, Φ = Q3P3) Ω-involutive then
Ω is a 2-cocycle.
Proof. By definition Φ = Q3P3 is an associator with Φ−1 = P3Q3, see Sect. 9. Then
(A, ∆˜ , ε, Φ) is a weak Hopf algebra as well since ˜
Φ = ( ˜ Q3P3)
∗−1 = (Q3P3)−1∗
= (P3Q3)
∗ = Q∗
3P
∗
3 = 1 ⊗ ∆( ˜ ∆( ˜ I))∆˜ ⊗ 1(∆( ˜ I))
and similarly Φ˜ −1 = ∆˜ ⊗ 1(∆( ˜ I))1 ⊗ ∆( ˜ ∆( ˜ I)). By (11.5) and Prop. 9.13 we see that Ω is
a 2-cocycle. □
Definition 11.5. Let A be a discrete algebra in the sense of Def. 6.17. A positive ∗-
involution on A is a ∗-involution such that A can be completed to a C
∗
-algebra. We
may then identify A with an algebraic direct sum of matrix subalgebras with the usual
∗
-involution. An Ω-involutive structure on A is defined as in the unital case but Ω is
here allowed to be a (selfadjoint) element in M(A ⊗ A). A unitary discrete weak quasiHopf algebra is defined by further requiring that Ω has positive components in the matrix
1To be precise, the Ω-involution of Uq(g) is not comprised in Def. 11.1. This is due to the fact that
the R-matrix lies in a suitable topological completion of Uq(g) ⊗ Uq(g). However, when we consider the
category of finite dimensional representations of Uq(g), this inconvenience is not source of complications
in that it gives rise to a braided tensor category, as explained in [161]. It follows that the associated Ω also
lies in the completed algebra. Similarly to the R-matrix case, in this paper we will consider applications
of the notion of Ω-involution to categories of finite dimensional representations, see Sect. 12–23, and we
shall refrain from giving a more general definition of Ω-involution.

88 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
subalgebras. It follows that the same holds for Ω−1. In the particular case where A is a
weak Hopf algebra, we shall refer to A as a unitary discrete weak Hopf algebra.
Unless otherwise stated, involutions of discrete algebras will be assumed positive. This
will hold for most part of this paper. We next describe the Ω-involutions on a simple class
of discrete algebras.
Example 11.6. We consider the bialgebra Cω(G) of complex valued functions of a finite
group G with the usual coproduct and associator given by a T-valued 3-cocycle ω, see
Ex. 7.12. A natural unitary structure is given by the C
∗
-structure of Cω(G) and Ω = I.
More generally, a general Ω-involution for Cω(G) over the same C
∗
-algebra is given by
a normalized 2-cocycle Ω(g, h) with values in R
×, that is a function satisfying Ω(1, g) =
Ω(g, 1) = 1 and Ω(g, h)Ω(gh, k) = Ω(h, k)Ω(g, hk) for all g, h, k ∈ G. The corresponding
quasi-Hopf algebra is unitary if and only of Ω(g, h) > 0 for all g, h ∈ G. This is not always
the case, an example is given by G = Z2 Ω(g, g) = −1 with g the group generator.
In the next sections we shall see examples of unitary discrete weak quasi-Hopf algebras
arising from unitary tensor categories, Sect. 13, and quantum groups Sects. 28, 30, 32.
Moreover we shall discuss conditions which guarantee unitarity, see Theorem 26.2. In the
following proposition we show that the fact that A˜ and AΩ have the same counit is a
redundant assumption.
Proposition 11.7. The counit ε of a weak quasi-bialgebra A is unique. If A is a weak
quasi-Hopf algebra with antipode S the counit satisfies ε ◦ S = ε. If A is an Ω-involutive
weak quasi-bialgebra then ε(a
∗
) = ε(a), for every a ∈ A.
Proof. The first two statements can be proved in the same way as for quasi-bialgebras,
namely the first follows from (6.2) while the second from applying the counit to one of the
equations (6.7). For the last statement it suffices to show that εe(a) := ε(a
∗
) is a counit.
For example,
(1 ⊗ εe)(∆(a)) = a(1)εe(a(2)) =
(a
∗
(1)ε(a
∗
(2)))∗ = (1 ⊗ ε(∆(a)
∗
))∗ =
(1 ⊗ ε(Ω∆(a
∗
)Ω−1))∗ = (1 ⊗ ε(∆(a
∗
)))∗ = a.
□
Proposition 11.8. a) Let A be an Ω-involutive weak quasi-bialgebra and F ∈ A ⊗ A
a twist (Def. 6.8). Then AF is an ΩF -involutive weak quasi-bialgebra with the same
involution as A and
ΩF := F
−1∗
ΩF
−1
, (ΩF )
−1
:= FΩ
−1F∗
(11.6)
b) If A is a discrete pre-C
∗
-algebra and Ω is positive in M(A ⊗ A) then ΩF is positive
as well.
We discuss a useful application of the twist of the unitary structure.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 89
Definition 11.9. Let A be a weak quasi bialgebra with a ∗-involution. An Ω-involution
compatible with ∗ on A is called trivial if it is given by Ω = ∆(I)
∗∆(I) and Ω−1 =
∆(I)∆(I)
∗
. Thus Ω is a trivial twist. We shall call it strongly trivial if in addition ∆(I) is
selfadjoint, that is equivalent to require that commutes ∆ commutes with the ∗-involution
as in the usual ∗-bialgebra theory. In this case, ∆(I) is a selfadjoint projection.
With a strongly trivial involution, ∆ commutes with ∗ and the associator Φ satisfies
Φ
∗ = Φ−1
. The above notions of (strong) triviality has the same motivation as that of and
are related to those of (strongly) unitary weak quasi tensor functor discussed before Def.
4.19.
Remark 11.10. a) As in the case of weak quasitensor structures, when A is a weak quasi
bialgebra with a ∗-involution and a trivial Ω-involution compatible with ∗then T = ∆(I)
is a twist with left inverse T
−1 = ∆(I)∆(I)∗
(or T
′ = ∆(I)∗∆(I) with T′−1 = ∆(I)) giving
a new wqh AT (AT′) with strongly trivial involution. b) When A is a discrete unitary weak
quasi-bialgebra with a trivial Ω-involution then this involution is automatically strongly
trivial. This follows from the fact that we are in a C
∗
-setting, Prop. 4.21 and the following
Tannaka-Krein duality, Theorem 13.5.
Example 11.11. We have the following generalization of the construction in Remark c)
in 11.2. Let A be a unitary discrete weak quasi bialgebra with an Ω-involution given by
Ω ∈ M(A ⊗ A). We may consider T = Ω1/2 defined via continuous functional calculus in
each full matrix subalgebra of M(A⊗A). This element satisfies the properties T ∆(I) = T,
∆(I)
∗T = T, and ω ⊗ 1(T) = 1 ⊗ ω(T) = 1, so we may regard T as an element of A
with the same domain ∆(I) as Ω. Applying the same construction to Ω−1, we construct
T
′ = (Ω−1
)
1/2 ∈ M(A ⊗ A) with range ∆(I).
Corollary 11.12. Let A be a discrete unitary weak quasi bialgebra defined by Ω and
assume that (Ω−1)
1/2Ω1/2 = ∆(I). Let us regard T = Ω1/2 as a twist with left inverse
T
−1 = (Ω−1
)
1/2
. Then the twisted Ω-involution of AT is trivial, and therefore strongly
trivial.
Proof. By part b) of Prop. 11.8, ΩT = ∆T (I)
∗∆T (I) and Ω−1
T = ∆T (I)∆T (I)
∗
. Strong
triviality follows again from the fact that we are in a C
∗
-setting, Prop. 4.21 and TannakaKrein duality Theorem 13.5. □
We shall refer to AΩ1/2 as the unitarization of A. We next introduce a deformation of an
Ω-involution on a given weak bialgebra that may be thought of as analogous to the twist
operation for the weak quasi bialgebra structure.
Definition 11.13. Let A be an Ω-involutive weak quasi bialgebra A defined by (∗, Ω). A
twist for the involutive structure is an invertible selfadjoint t ∈ A such that ε(t) = 1. If A
is discrete in the sense of Def. 11.5 we allow t ∈ M(A).
Proposition 11.14. A twist t of an involution (
∗
, Ω) gives rise to another involutive
structure on the same weak quasi bialgebra via
a
†
:= t
−1
a
∗
t, Ωt:= t
−1 ⊗ t−1Ω∆(t).

90 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
If A is a C
∗
-algebra under ∗, or else if A is discrete, and (
∗
, Ω) is a positive involution,
then the same holds for A with respect to (
†
, Ωt) for any positive twist t.
Proof. The proof of the first statement follows from routine computations. For example,
Ω
†
t = Ωt
follows from (11.3). We show the second statement. If ∥a∥ denotes a C
∗
-norm of
A compatible with ∗then ∥a∥t:= ∥t
1/2at−1/2∥ is another C∗
-norm on A compatible with
†
. (Note that the original and the deformed norms are equivalent, hence completeness of
one is equivalent to completeness of the other.) Furthermore if Ω is positive with respect
to the original involution, the element Ξ := t
−1/2 ⊗ t−1/2Ω1/2∆(t1/2
) satisfies Ξ†Ξ = Ωt, so
Ωtis positive with the †-involution of A ⊗ A.
□
In the discrete case, any other involution making A into a pre-C
∗
-algebra is of the kind
a
† = t−1a∗
t, with t determined up to a normalized central positive element of M(A). This
implies e the following useful result.
Corollary 11.15. If a discrete weak quasi bialgebra A can be made unitary with respect to
an assigned pre-C
∗
-algebra involution of A, the same is true for any other such involution.
As for twists of bialgebra structures, twists of involutive structures admit a categorical
interpretation, that will be discussed in Prop. 13.1. The next results exploit the relations
between antipode and Ω-involution.
Proposition 11.16. Let (S, α, β) be an antipode of an Ω-involutive weak quasi-Hopf algebra. There is an invertible ω ∈ A such that
S(a) = ωS−1(a
∗
)
∗ω−1
, a ∈ A, (11.7)
S
−1
(β)
∗ = ω−1αΩ, S−1
(α)
∗ = βΩω (11.8)
uniquely determined by (11.7) and one of (11.8). In particular when S is a strong antipode
then
ω = m(S ⊗ 1(Ω−1)), ω−1 = m(1 ⊗ S(Ω)). (11.9)
Proof. The adjoint weak quasi-bialgebra A˜ defined in (10.8) has antipode (S, ˜ α, ˜ β˜) with
S˜(a) := S
−1
(a
∗
)
∗
, ˜α := S
−1
(β)
∗
, β˜ := S
−1
(α)
∗
. On the other hand, A˜ = AΩ, and therefore
it also admits (SΩ, αΩ, βΩ) as an antipode by Prop. 6.9. The first statement follows from
Prop. 6.10 and the last from a computation and (6.11). □
Corollary 11.17. The following are equivalent for an antipode (S, α, β),
a) S commutes with ∗,
b) S
−1
commutes with ∗,
c) S
2
(a) = ωaω−1, a ∈ A.
If these conditions hold then ω
∗ω and S(ω)ω are central.
We study the dependence of the element ω introduced in Prop. 11.16 on twisting.
Proposition 11.18. Let A be an Ω-involutive weak quasi-Hopf algebra with antipode
(S, α, β) and involutive structure (∗, Ω) and associated element ω as in Prop. 11.16.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 91
a) Let (Ad(u)S, uα, βu−1) be another antipode of A. The corresponding element is
given by ωu = uωS−1(u)
∗
.
b) Let F ∈ A⊗A be a twist and consider the weak quasi-Hopf algebra AF with antipode
(S, αF , βF ) and involutive structure (∗, ΩF ). Then the corresponding element is
given by ωF = ω.
Proof. a) follows from a computation. b) By the uniqueness stated in Prop. 11.16 we
only need to verify that S
−1
(βF )
∗ = ω−1
(αF )ΩF
. The claim follows in a straightforward
way from a computation based on (11.7) and the first relation in (11.8) which takes into
account the definition of αF , βF in (6.11) and of ΩF in (11.6).
□
Definition 11.19. An Ω-involutive weak quasi-Hopf algebra is called of Kac type if it
admits a (unique) strong antipode satisfying one of the equivalent conditions stated in
Cor. 11.17. We shall also refer to the antipode as being of Kac type.
The definition is motivated by the fact that if A is in turn a Hopf ∗–algebra in the usual
sense (Ω = I) then ω = I, and Cor. 11.17 reduces to the well known characterisation of
Hopf ∗–algebras of Kac type.
Proposition 11.20. Let A be a Hopf algebra such that
∆
op(a)∗ = ∆(a∗
), a ∈ A.
(e.g. A is Ω-involutive and satisfies ∆op(a) = Ω∆(a)Ω−1for a ∈ A). Then A is of Kac
type.
Proof. Since A is a Hopf algebra, it admits a unique strong antipode, denoted S. Furthermore, our assumptions imply ∆(a
∗
) = ∆op(a)
∗
for a ∈ A. It follows that the antiautomorphism S˜(a) := S(a
∗
)
∗
is another Hopf algebra antipode of A, as
(m ◦ (1 ⊗ S˜) ◦ ∆)(a) = a(1)S˜(a(2)) = (S(a
∗
(2))a
∗
(1))
∗ = (11.10)
[m ◦ (S ⊗ 1)(∆op(a)
∗
)]∗ = [m ◦ (S ⊗ 1)(∆(a
∗
))]∗ = (11.11)
(ε(a
∗
)I)
∗ = ε(a)I. (11.12)
Hence S˜ = S by uniqueness.
□
Wenzl shows in [185] that the assumptions of Prop. 11.20 are satisfied by the quantum
groups Uq(g) for |q| = 1, cf. also Sect. 32. We shall extend Prop. 11.20 to weak Hopf
algebras endowed with a ∗-involution and a strong antipode in Sect. 28, see Prop. 28.7.
