---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-008-9-weak-hopf-algebras
section_title: "Weak Hopf algebras"
section_number: 9
pages: 74-79
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
doc_brief: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem — We construct, for every complex simple Lie algebra g and every positive integer level k, a unitary modular"
---
9. Weak Hopf algebras
Hopf algebras are characterised among quasi-Hopf algebras by the property of having
trivial associator [47]. This characterization gives insight into the cohomological interpretation of quasi-Hopf algebras, in that it leads to the notion of a 3-coboundary associator.
In this section we develop a weak analogue of the notion of Hopf algebra among weak
quasi-Hopf algebras. The corresponding special subclass will be termed weak Hopf algebras. We shall see that there is no strictly coassociative weak example. We shall construct
examples later on.
Definition 9.1. Let A be a weak quasi bialgebra with associator Φ and coproduct ∆. We
shall call Φ a 3-coboundary associator if there is a twist F ∈ A ⊗ A such that
Φ = 1 ⊗ ∆(F
−1
)I ⊗ F
−1F ⊗ I∆ ⊗ 1(F), (9.1)
Φ
−1 = ∆ ⊗ 1(F−1
)F
−1 ⊗ II ⊗ F1 ⊗ ∆(F). (9.2)
If A is a quasi bialgebra and F is an invertible twist then only one equation suffices
among (9.1) and (9.2), and Def. 9.1 reduces to the corresponding notion of a 3-coboundary
associator. We next introduce weak Hopf algebras.
Let A be an algebra with a coproduct ∆ and a counit ε. To shorten some formulas, we
set:
P = ∆(I),
P3 = ∆ ⊗ 1(P), Q3 = 1 ⊗ ∆(P),
P4 = ∆ ⊗ 1 ⊗ 1(P3), Q4 = 1 ⊗ 1 ⊗ ∆(Q3)
Assume that the coproduct satisfies the following intertwining relations, espressing coassociativity in a weak sense. For a ∈ A,
Q3∆ ⊗ 1 ◦ ∆(a) = 1 ⊗ ∆ ◦ ∆(a)P3, (9.3)
P31 ⊗ ∆ ◦ ∆(a) = ∆ ⊗ 1 ◦ ∆(a)Q3. (9.4)

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 75
Proposition 9.2. The element Φ := Q3P3 satisfies Def. 6.2 d), with partial inverse
Φ
−1 = P3Q3 if and only if
P3Q3P3 = P3, Q3P3Q3 = Q3, (9.5)
Q41 ⊗ ∆ ⊗ 1(I ⊗ P P ⊗ I)P4 = Q4∆ ⊗ ∆(P)P4. (9.6)
Proof. Relations (9.5) correspond obviously to (6.3), and (9.3) to (6.4). We explicit the
cocycle condition (6.5). We have I ⊗ P3 = 1 ⊗ ∆ ⊗ 1(I ⊗ P) and I ⊗ P Q3 = Q3, and
similarly Q ⊗ IP3 = P3. This implies, taking into account (9.3) and (9.4),
I ⊗ Φ1 ⊗ ∆ ⊗ 1(Φ)Φ ⊗ I = I ⊗ Q3P31 ⊗ ∆ ⊗ 1(Q3P3)Q3P3 ⊗ I =
I ⊗ Q31 ⊗ ∆ ⊗ 1(Q3P3)P3 ⊗ I = I ⊗ Q31 ⊗ ∆ ⊗ 1(Q3)1 ⊗ ∆ ⊗ 1(P3)P3 ⊗ I =
I ⊗ Q31 ⊗ ∆ ⊗ 1(1 ⊗ ∆(P)1 ⊗ ∆ ⊗ 1(∆ ⊗ 1(P))P3 ⊗ I = Q4I ⊗ P3Q3 ⊗ IP4 =
Q41 ⊗ ∆ ⊗ 1(I ⊗ P P ⊗ I)P4.
On the other hand,
1 ⊗ 1 ⊗ ∆(Φ)∆ ⊗ 1 ⊗ 1(Φ) = 1 ⊗ 1 ⊗ ∆(Q3P3)∆ ⊗ 1 ⊗ 1(Q3P3) =
Q4∆ ⊗ ∆(P)P4.
Finally, the normalisation condition relation (6.6) is an immediate consequence of the
counit axioms (6.2). □
Remark 9.3. The cocycle relation (9.6) can alternatively be written as
Q41 ⊗ ∆ ⊗ 1(Q3P3)P4 = Q4∆ ⊗ ∆(P)P4.
Indeed, the computations in the last proof show that
Q41 ⊗ ∆ ⊗ 1(I ⊗ P) = I ⊗ Q31 ⊗ ∆ ⊗ 1(Q3),
(and a similar identity involving P4 and P3) hence multiplying on the left by Q4, this term
also equals Q41 ⊗ ∆ ⊗ 1(Q3).
Definition 9.4. An algebra A with coproduct ∆ and counit ε for which the projections
P, Pj, Qj, j = 3, 4, satisfy the requirements of the previous proposition is a weak quasibialgebra with associator Φ = Q3P3 and will be called a be called a weak bialgebra.
Proposition 9.5. If a weak bialgebra A admits an antipode (S, α, β) in the sense of weak
quasi-Hopf algebras then α, β are invertible and β = α
−1
. Hence ad(α
−1
)S is the unique
strong antipode of A.
Proof. A computation shows that if (6.7) holds for (S, α, β) where S is an antiautomorphism of A, then equations (6.8) for the associator Φ = Q3P3 reduce to βα = I and
αβ = I. The last statement follows from Prop. 6.11 a) □
Definition 9.6. A weak bialgebra with a (unique) strong antipode, will be called a weak
Hopf algebra.

76 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Remark 9.7. The first examples of weak quasi-Hopf algebras appeared in the physics
literature, in the work by Mack and Schomerus [125], who were motivated by the need of
constructing a quantum analogue of a global gauge group for certain models of algebraic
quantum field theories in low dimensions. They started with a nonsemisimple category
of representations of Uq(sl2) at roots of unity and indicated how to construct a such an
algebra [124, 125]. In a previous work [25], Mack-Schomerus construction was studied in
detail in the more general case of Uq(slN ), and it was shown that these are indeed weak
Hopf algebras in the sense of this section.
We next state, without proof, a few simple properties of weak Hopf algebras (and in fact
already of weak quasi-Hopf algebras) useful to construct new examples from given ones.
Proposition 9.8. Let A be a weak Hopf algebra.
(a) (tensor products) If B is another weak Hopf algebra then the natural weak quasiHopf structure on the tensor product algebra A⊗B is a weak Hopf algebra structure.
(b) (subalgebras) let C be a unital subalgebra of A which is invariant under coproduct
and antipode. Then C is a weak Hopf algebra with the restricted structure and there
is a natural inclusion of rigid tensor categories Rep(A) → Rep(B).
(c) (quotients) If D is a weak Hopf algebra related to A via an algebra epimorphism
A → D compatible with coproduct and antipode then there is an inclusion Rep(C) →
Rep(A) as a full rigid tensor subcategory.
Proposition 9.9. Let A and B be weak Hopf algebras, and let α : A → B an algebra
isomorphism which intertwines the corresponding coproducts and antipodes. Then α is
automatically an isomorphism of weak quasi-Hopf algebras.
Semisimple bialgebras are described via Tannaka-Krein duality by semisimple tensor
categories endowed with a tensor functor to Vec. This characterization extends to weak
bialgebras, and is based on the simple observation that they have a weak tensor furgetful
functor.
Theorem 9.10. Let C be a semisimple (rigid) tensor category with finite dimensional
morphism spaces and F : C → Vec a faithful weak quasi-tensor functor (taking an object
and a dual to spaces with the same dimension). Then A = Nat0(F) is a weak bialgebra
(weak Hopf algebra) if and only if F is a weak tensor functor.
Proof. Let A = Nat0(F) be a weak bialgebra. The forgetful functor of A is weak tensor and
this implies that the same holds for F since it is monoidally isomorphic to the composition
of a tensor equivalence with the forgetful functor. Conversely, if F is weak tensor then the
associator Φ of A and its inverse Φ−1 are derived from (4.6) and (4.7), and a computation
shows that Φ = 1 ⊗ ∆(∆(I))∆ ⊗ 1(∆(I)), Φ−1 = ∆ ⊗ 1(∆(I))1 ⊗ ∆(∆(I)), that is A is a
weak bialgebra. For the last assertion note that the equality requirement on the dimensions
of an object and a dual are automatically satisfied in our case, thanks to Cor. 5.9. Hence
Theorem 7.6 guaranties that A has an antipode.
□

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 77
It follows that the constructions of Prop. 9.8 have a description in terms of pairs of
abstract tensor categories endowed with a weak tensor functor. In particular, the following
will turn out useful to construct new weak Hopf algebras from given examples, see Sect.
32.
Corollary 9.11. Let C be a fusion category endowed with a weak tensor functor to Vec.
Under Tannaka-Krein correspondence, full fusion subcategories D ⊂ C endowed with the
restricted functor correspond to quotient weak Hopf algebras of A = Nat0(F).
The class of weak Hopf is not invariant under general twists, but we next see that it is
so under a suitable subclass of twists, that play the role of 2-cocycles in our framework.
Definition 9.12. Let A be a weak bialgebra. A twist F ∈ A ⊗ A is called a 2-cocycle of
A if it satisfies the following equations,
1 ⊗ ∆(F
−1
)I ⊗ F
−1F ⊗ I∆ ⊗ 1(F) = Q3P3, (9.7)
∆ ⊗ 1(F
−1
)F
−1 ⊗ II ⊗ F1 ⊗ ∆(F) = P3Q3. (9.8)
Note that P3 and P
F
3
:= ∆F ⊗ 1(F F −1) are respectively domain and range for F ⊗
I∆ ⊗ 1(F), and the partial inverse of this element is ∆ ⊗ 1(F
−1
)F
−1 ⊗ 1, and similarly for
I ⊗ F1 ⊗ ∆(F). The 2-cocycle equations can equivalently be written in the following form
Q
F
3 F ⊗ I∆ ⊗ 1(F) = I ⊗ F1 ⊗ ∆(F)P3,
P
F
3
I ⊗ F1 ⊗ ∆(F) = F ⊗ I∆ ⊗ 1(F)Q3,
with QF
3
:= 1 ⊗ ∆F (F F −1), as well as in a form which emphasises a categorical feature,
ΦF F ⊗ I∆ ⊗ 1(F) = I ⊗ F1 ⊗ ∆(F)Φ,
Φ
−1
F
I ⊗ F1 ⊗ ∆(F) = F ⊗ I∆ ⊗ 1(F)Φ−1.
This last form also shows that the notion of a 2-cocycle has an extension to weak quasiHopf algebras which in turn extends the corresponding notion for quasi-Hopf algebras, see,
e.g., [105].
Proposition 9.13. Let A be a weak quasi-bialgebra with coproduct ∆ and associator Φ, and
let F ∈ A ⊗ A be a twist. Then AF is a weak bialgebra if and only if Φ is the 3 coboundary
associator defined by F as in (9.1), (9.2). In particular, if A is a weak bialgebra, AF is a
weak bialgebra as well if and only if F is a 2-cocycle.
Proof. We already know that AF is a weak quasi-bialgebra with coproduct ∆F (a) =
F ∆(a)F
−1 and associator ΦF = I ⊗ F1 ⊗ ∆(F)Φ∆ ⊗ 1(F−1
)F
−1 ⊗ I. We have Φ−1
F =
F ⊗ I∆ ⊗ 1(F)Φ−11 ⊗ ∆(F
−1
)I ⊗ F
−1
. Hence for AF to be a weak bialgebra it suffices
that the associator and its inverse satisfy ΦF = QF
3 P
F
3
, Φ−1
F = P
F
3 QF3
. A simple computation shows that these equations are equivalent to the equations in the statement. If in
particular A is a weak bialgebra as well, these equations reduce to the 2-cocycle equations
(9.7), (9.8). □

78 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Remark 9.14. If A is a quasi-Hopf algebra, equations (9.7) and (9.8) are precisely the
cohomological equations which characterise a cohomologically trivial associator. Quite
interestingly, these equations are meaningful for weak quasi-Hopf algebras with the weak
counterparts of associator and twist, with no extra requirement on F. The previous proposition shows that weak bialgebras arise naturally when one tries to solve them for a given
associator Φ of a weak quasi-bialgebra A. This gives a cohomological motivation for regarding the associator of a weak Hopf algebra as trivial.
The following corollary extends to weak Hopf algebras a property known for Hopf algebras, see, e.g., [174].
Corollary 9.15. Let A be a weak Hopf algebra and F ∈ A ⊗ A a 2-cocycle. Then the
element uF = m ◦ S ⊗ 1(F
−1
) is invertible and u
−1
F = m ◦ 1 ⊗ S(F).
Proof. The twisted weak quasi-bialgebra AF is a weak bialgebra thanks to Prop. 9.13. If
S is the strong antipode of A then AF has weak quasi-Hopf algebra antipode (S, αF , βF )
where αF = m ◦ S ⊗ 1(F
−1
), βF = m ◦ 1 ⊗ S(F), by (6.11). Hence we can apply Prop. 9.5
to AF and deduce that αF and βF are inverses of one another. □
Proposition 9.16. If F is a 2-cocycle of A and G is a 2-cocycle of AF then GF is a
2-cocycle of A.
We introduce two examples of 2-cocycles that will be useful.
Proposition 9.17. Let v ∈ A be an invertible element with ε(v) = 1 and F ∈ A ⊗ A a
2-cocycle, then Fv := v ⊗ vF∆(v
−1
) is a 2-cocycle as well.
Proof. Obviously F
−1
v = ∆(v)F
−1
v
−1 ⊗ v−1
. A computation shows that the left hand side
of (9.7) equals
1 ⊗ ∆ ◦ ∆(v)1 ⊗ ∆(F
−1
)I ⊗ F
−1F ⊗ I∆ ⊗ 1(F)∆ ⊗ 1 ◦ ∆(v−1
) =
1 ⊗ ∆ ◦ ∆(v)Q3P3∆ ⊗ 1 ◦ ∆(v
−1
) =
1 ⊗ ∆ ◦ ∆(v)1 ⊗ ∆ ◦ ∆(v
−1
)Q3P3 = Q3P3.
Relation (9.8) for Fv can be proved in a similar way.
□
Proposition 9.18. Let E ∈ A ⊗ A be an idempotent satisfying
ε ⊗ 1(E) = 1 ⊗ ε(E) = I,
EP2E = E, P2EP2 = P2.
Then F = EP2 defines a trivial twist with D(F) = P2, R(F) = E and F
−1 = P2E. It is a
2-cocycle if and only if the following additional relations hold,
Q31 ⊗ ∆(E)I ⊗ EE ⊗ 1∆ ⊗ 1(E)P3 = Q3P3,
P3∆ ⊗ I(E)E ⊗ II ⊗ E1 ⊗ ∆(E)Q3 = P3Q3.
We omit the proof as it follows from a simple computation.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 79
