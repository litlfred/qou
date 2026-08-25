---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-003-24-the-multiplicative-unitary
section_title: "The multiplicative unitary"
section_number: 2.4
pages: 13-15
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS represe ntation of the quantum plane A and its dual"
---
Multiplicative unitaries are fundamental to the theory of quantum g roups in the
setting of C∗-algebras and von Neumann algebras, and to generalization of Pon-
tryagin duality. In particular, a multiplicative unitary encodes all the structure
maps of a quantum group and its dual. A very good exposition is given in [40].
First let us deﬁne the leg notation.
Deﬁnition 2.16. LetH be a Hilbert space and W ∈ B(H⊗H ) be a bounded
operator. Then we deﬁne Wij∈B (H⊗k) by letting W acts on the factors at the
positioni,j . In particular, the operators W12,W 23,W 13∈B (H⊗H⊗H ) are given
by the formulas
T12 :=T⊗Id H, T 23 :=Id H⊗T, (2.27)
T13 := Σ 12T23Σ 12 = Σ 23T12Σ 23, (2.28)
where Σ∈B (H⊗H ) denotes the ﬂip f⊗g↦→g⊗f .
Deﬁnition 2.17. LetH be a Hilbert space. A unitary operator W∈B (H⊗H ) is
called a multiplicative unitary if it satisﬁes the pentagon equation
W23W12 =W12W13W23, (2.29)
where the leg notation is used.
Given a GNS representation ( H,π, Λ) of a locally compact quantum group A,
we can deﬁne a unitary operator
W ∗(Λ(a)⊗ Λ(b)) = (Λ ⊗ Λ)(∆( b)(a⊗ 1)). (2.30)
It is known that W is a multiplicative unitary [24, Thm 3.16, Thm 3.18], and
the coproduct on A deﬁning it can be recovered from W :
Proposition 2.18. Letx∈A֒B (H) as operator. Then
W ∗(1⊗x)W = ∆( x) (2.31)
as operators on H⊗H .
13
Proof. Forx,f,g ∈A , we have x· Λ(f ) = Λ( xf ), hence
W ∗((1⊗x)· (Λ(f )⊗ Λ(g))) = W ∗(Λ(f )⊗ Λ(xg))
= (Λ ⊗ Λ)(∆( xg)(f⊗ 1))
= (Λ ⊗ Λ)(∆( x)∆( g)(f⊗ 1))
= ∆( x)· (Λ⊗ Λ)(∆( g)(f⊗ 1))
= ∆( x)W ∗(f⊗g).
As a motivation, let us consider an example involving classical group:
Example 2.19. [40, Ex 7.1.4][45] Let G be a locally compact group with right Haar
measureλ. Then the operator
(Wf )(x,y ) := f (xy,y ) (2.32)
is a multiplicative unitary in B(L2(G,λ )⊗L2(G,λ )) =B(L2(G×G,λ×λ)). The
pentagon equation for W is equivalent to the associativity of the multiplication in
G. Indeed, for f∈L2(G×G×G,λ×λ×λ)≃L2(G,λ )⊗3 and x,y,z ∈G, we have
(W23W12f )(x,y,z ) = f (x(yz),yz,z ),
(W12W13W23f )(x,y,z ) = f ((xy)z,yz,z ).
An important property of W is that it encodes the information of the dual
quantum group ˆA. By deﬁnition, ˆA is the closure of the linear span of
{(ω⊗ 1)W :ω∈B (H)∗}⊂B (H), (2.33)
and we actually have
W∈M (A⊗ ˆA), (2.34)
where M stands for the multiplier algebra.
Similarly, the multiplicative unitary for the dual ˆA is given by ˆW :=W ∗
21, hence
it is known from the Pontryagin duality that ˆW ∈ M ( ˆA⊗A ) as well. From the
pentagon equation, we then obtain:
Corollary 2.20. As an element W∈M (A⊗ ˆA), together with the pentagon equa-
tion, we have
(∆ ⊗ 1)W =W13W23, (2.35)
(1⊗ ˆ∆) W =W13W12. (2.36)
Finally let us deﬁne the notion of “manageability” introduced by Woron owicz
[45, 46] that describes a class of well-behaved multiplicative unitary. It is shown
that any manageable multiplicative unitary gives rise to a quantum gro up on the
C∗-algebraic level.
14
Deﬁnition 2.21. A multiplicative unitary W is manageable if there exists a positive
self-adjoint operator Q acting on H and a unitary operator ~W acting on H⊗H
such that ker(Q) ={0},
(Q⊗Q)W =W (Q⊗Q), (2.37)
and
⟨x⊗u,W (z⊗y)⟩H⊗H = (z⊗Qu,~W (x⊗Q−1y)⟩H⊗H (2.38)
for any x,z∈H,y∈D(Q−1),u∈D(Q).
HereH denote the complex conjugate of H, so that the map x∈H−→ x∈H
is an anti-unitary map. The inner product on H is given by ⟨x,y⟩H :=⟨y,x⟩H.
