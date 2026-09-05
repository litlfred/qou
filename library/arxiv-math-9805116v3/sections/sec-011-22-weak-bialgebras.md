---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras"
section_id: sec-011-22-weak-bialgebras
section_title: "Weak bialgebras"
section_number: 2.2
pages: 6-9
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
doc_brief: "Weak Hopf Algebras — We give an introduction to the theory of weak Hopf algebras pr oposed recently as a coassociative alternative of weak quasi-Hopf algebras."
---
In a WBA deﬁne the maps ⊓L, ⊓R:A →A by the formulae
⊓L (x) := ε(1(1)x)1(2) , ⊓R(x) := 1 (1)ε(x1(2)) (2.1)
and introduce the notation AL := ⊓L(A),AR := ⊓R(A) for their images. The analogue objects
in the dual bialgebra ˆA will be denoted by ˆ⊓L, ˆ⊓R, ˆAL, and ˆAR, respectively.
Substituting y = 1 in Axiom (A.6b) one obtains immediately the identities
ε(x ⊓L (y)) = ε(xy) (2 .2a) ε(⊓R(x)y) = ε(xy) (2 .2b)
⊓L ◦ ⊓L = ⊓L (2.3a) ⊓R ◦ ⊓R = ⊓R (2.3b)
As a ﬁrst application of the duality principle take 1 the duals of Eqns(2.2a-b),
1(1) ⊗ ⊓L(1(2)) = 1 (1) ⊗ 1(2) = ⊓R(1(1)) ⊗ 1(2) .
Then these are identities in any WBA. It follows that
∆(1) ∈ AR ⊗ AL . (2.4)
Lemma 2.2 The counit deﬁnes a non-degenerate bilinear form
xL ∈AL,yR ∈AR ↦→ε(yRxL) ∈K .
HenceAL ∼=AR as K-spaces.
Proof:
ε(yRxL) = 0 ∀yR ∈AR =⇒ xL =ε(1(1)xL)1(2) = 0
ε(yRxL) = 0 ∀xL ∈AL =⇒ yR = 1(1)ε(yR1(2)) = 0
where we used (2.4). Q.e.d.
Returning to Eqns(2.2a-b) and substituting them into the de ﬁnitions (2.1) one obtains
⊓L(x ⊓L (y)) = ⊓L(xy) (2 .5a) ⊓R(⊓R(x)y) = ⊓R(xy) (2 .5b)
The duals of (2.5a-b),
∆( AL) ⊂A ⊗AL (2.6a) ∆( AR) ⊂AR ⊗A (2.6b)
tell us that AL and AR are left, respectively right coideals in the coalgebra A. Using Axiom
(A.7b) we can obtain explicit expressions for these coprodu cts
∆( xL) = ε(1(1)xL)1(2) ⊗ 1(3) =ε(1(1′ )xL)1(1)1(2′) ⊗ 1(2) = 1 (1)xL ⊗ 1(2) (2.7a)
∆( xR) = 1 (1) ⊗ 1(2)ε(xR1(3)) = 1 (1) ⊗ 1(1′)1(2)ε(xR1(2′)) = 1 (1) ⊗xR1(2) (2.7b)
where xL and xR are meant to denote arbitrary elements of AL, resp. AR.
1In taking the transpose of a statement with ⊓L/R use the fact that in a WBA
⟨ϕ, ⊓L(x)⟩= ⟨ˆ1(1) ⊗ ˆ1(2), 1(1) ⊗ x⟩⟨ϕ, 1(2)⟩= ⟨ˆ⊓L(ϕ), x⟩ and similarly ⟨ϕ, ⊓R(x)⟩= ⟨ˆ⊓R(ϕ), x⟩.
6
Lemma 2.3 For all x ∈A we have the identities
x(1) ⊗ ⊓L(x(2)) = 1 (1)x ⊗ 1(2) (2.8a)
⊓R(x(1)) ⊗x(2) = 1 (1) ⊗x1(2) (2.8b)
Proof: Using Axiom (A.7b) one obtains
x(1) ⊗ε(1(1)x(2))1(2) = 1 (1′)x(1)ε(1(1)1(2′)x(2)) ⊗ 1(2) = 1(1)x(1)ε(1(2)x(2)) ⊗ 1(3) =
= 1 (1)x ⊗ 1(2)
1(1)ε(x(1)1(2)) ⊗x(2) = 1 (1) ⊗ε(x(1)1(1′)1(2))x(2)1(2′) = 1(1) ⊗ε(x(1)1(2))x(2)1(3) =
= 1 (1) ⊗x1(2)
Q.e.d.
As a consequence we obtain the dual statements
x ⊓L (y) = ε(x(1)y)x(2) (2.9a) ⊓R(x)y =y(1)ε(xy(2)) . (2.9b)
Proposition 2.4 LetA be a WBA. Then AL and AR are subalgebras of A containing 1 and
xLyR = yRxL for all xL ∈AL and yR ∈AR . (2.10)
Proof: Eqns(2.8a-b) imply the relations
1(1)1(1′) ⊗ 1(2) ⊗ 1(2′) = 1 (1) ⊗ ⊓L(1(2)) ⊗ 1(3) (2.11a)
1(1) ⊗ 1(1′) ⊗ 1(2)1(2′) = 1 (1) ⊗ ⊓R(1(2)) ⊗ 1(3) (2.11b)
Now either Axiom (A.7a) or (A.7b) show that on the RHS of (2.11 a) the ﬁrst tensor factor
belongs to AR and on the RHS of (2.11b) the last factor belongs to AL. This is suﬃcient for
AR, respectively AL to be closed under multiplication. Hence they are algebras. Obviously
1 ∈AL ∩AR since ⊓L(1) = 1 = ⊓R(1). In order to see commutativity of left and right elements
just compare Axioms (A.7a) and (A.7b). Q.e.d.
As the duals of the statements that AL andAR are subalgebras we obtain that Ker ⊓L and
Ker ⊓R are coideals of the coalgebra A, i.e.
∆(Ker ⊓C) ⊂ A ⊗ Ker ⊓C + Ker ⊓C ⊗A , (2.12)
ε(Ker ⊓C) = 0 , C =L,R .
On the other hand, being the annihilator of the left coideal ˆAL, Ker ⊓L is a left ideal of the
algebra A and similarly, Ker ⊓R is a right ideal.
Lemma 2.5 Consider AL and A as left AL-modules by left multiplication. Then ⊓L: A →AL
is a left AL-module map. Analogously, ⊓R:A → AR is a right AR-module map. That is to
say
⊓L (⊓L(x)y) = ⊓L(x) ⊓L (y) (2.13a)
⊓R(x ⊓R (y)) = ⊓R(x) ⊓R (y) (2.13b)
hold true for all x,y ∈A.
7
Proof: At ﬁrst use the deﬁnition of ⊓L/R, then Eqn(2.2a-b), and ﬁnally Eqn(2.7a-b):
⊓L(⊓L(x)y) = ε(1(1) ⊓L (x)y)1(2) =ε(1(1) ⊓L (x) ⊓L (y))1(2) = ⊓L(x) ⊓L (y)
⊓R(x ⊓R (y)) = 1 (1)ε(x ⊓R (y)1(2)) = 1 (1)ε(⊓R(x) ⊓R (y)1(2)) = ⊓R(x) ⊓R (y)
Q.e.d.
Our next assertion about WBA-s establishes a canonical isom orphism between the left
(right) subalgebra of A and the right (left) subalgebra of ˆA. Since the existence of a common
non-trivial subalgebra of A and ˆA for Hopf algebras is by far not typical, this result is the ﬁrs t
hint towards the fundamental role AL and AR will play in the theory of WHAs.
In order to formulate the statement we introduce the Sweedle r arrow notation
x⇀ϕ :=ϕ(1)⟨ϕ(2),x ⟩, ϕ↼x := ⟨ϕ(1),x ⟩ϕ(2) . (2.14)
Since A is the dual WBA of ˆA, the Sweedler arrows ϕ⇀x and x↼ϕ are also deﬁned.
Lemma 2.6 The map κL
A:xL ↦→(xL⇀ ˆ1) is an algebra isomorphism from AL onto ˆAR. The
map κR
A:xR ↦→(ˆ1 ↼ xR) is an algebra isomorphism from AR onto ˆAL. Furthermore, the
restriction of the canonical pairing to ˆAL ×AL, ˆAR ×AR, ˆAL ×AR, or to ˆAR ×AL is non-
degenerate.
Proof: Using Eqns(2.11a-b) and the deﬁning properties ⟨ϕ↼x,y ⟩ = ⟨ϕ,xy ⟩,. . . etc. of the
Sweedler arrows one can easily verify that
(xL⇀ ˆ1)(yL⇀ ˆ1) = ˆ1(1)ˆ1(1′)⟨ˆ1(2),xL⟩⟨ˆ1(2′),yL⟩= ˆ1(1)⟨ˆ1(2),xL⟩⟨ˆ1(3),yL⟩=
= xLyL⇀ ˆ1 (2.15)
(ˆ1↼xR)(ˆ1↼yR) = ⟨ˆ1(1),xR⟩⟨ˆ1(1′ ),yL⟩ˆ1(2)ˆ1(2′) = ⟨ˆ1(1),xR⟩⟨ˆ1(2),yR⟩ˆ1(3)
= ˆ1↼xRyR (2.16)
(ˆ1↼xR)⇀ 1 = 1 (1)⟨ˆ1↼xR, 1(2)⟩= 1(1)ε(xR1(2)) = xR (2.17)
1↼ (xL⇀ ˆ1) = ⟨1(1),xL⇀ ˆ1⟩1(2) =ε(1(1)xL)1(2) =xL (2.18)
ThusκL
A (κR
A) is an algebra map with inverse κR
ˆA (κL
ˆA). As for the non-degeneracy
⟨ϕR,xL⟩= 0 ∀ϕR =⇒ xL = ⟨ˆ1,xL1(1))1(2) = ⟨1(1)⇀ ˆ1,xL⟩1(2) = 0
⟨ϕL,xL⟩= 0 ∀ϕL =⇒ xL = ⟨ˆ1, 1(1)xL⟩1(2) = ⟨ˆ1↼ 1(1),xL⟩1(2) = 0
and the transpose of these prove the claim. Q.e.d.
If {bi} is a K-basis of A and {βi} ⊂ ˆA is its dual basis, ⟨βi,bj⟩=δij, then
∑
i
⊓L(bi) ⊗βi =
∑
i
bi ⊗ ˆ⊓L(βi) = 1 ↼ ˆ1(1) ⊗ ˆ1(2) (2.19a)
∑
i
⊓R(bi) ⊗βi =
∑
i
bi ⊗ ˆ⊓R(βi) = 1 (1) ⊗ 1(2)⇀ ˆ1 (2.19b)
This can be easily seen by pairing both hand sides of any of the se equations with ϕ ⊗x and
apply the deﬁnitions (2.1).
The four arrow identities of the next Scholium will be freque ntly used in later computations.
8
Scholium 2.7 LetA be a WBA. Then for all ϕ ∈ ˆA, xL ∈AL, and xR ∈AR
xL⇀ϕ = ( xL⇀ ˆ1)ϕ (2.20a)
ϕ↼xR = ϕ(ˆ1↼xR) . (2.20b)
ϕ↼xL = ( ˆ1↼xL)ϕ (2.21a)
xR⇀ϕ = ϕ(xR⇀ ˆ1) . (2.21b)
