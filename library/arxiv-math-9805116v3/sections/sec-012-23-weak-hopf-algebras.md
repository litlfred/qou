---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras"
section_id: sec-012-23-weak-hopf-algebras
section_title: "Weak Hopf algebras"
section_number: 2.3
pages: 9-12
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
doc_brief: "Weak Hopf Algebras — We give an introduction to the theory of weak Hopf algebras pr oposed recently as a coassociative alternative of weak quasi-Hopf algebras."
---
In this Subsection we will show how the existence of an antipo de relates ⊓L, AL with ⊓R, AR
and derive the expected properties of S that have been axioms in earlier formulations. The two
most important results will be invertibility of the antipod e and separability of the algebras AL
and AR. Let us start with the question of uniqueness of the antipode .
Lemma 2.8 The unit, the counit, and the antipode, if exist, are unique. I.e. if
(A,µ,u, ∆ ,ε,S ) and (A,µ,u ′, ∆ ,ε ′,S ′) are both weak Hopf algebras then u′ = u, ε′ = ε,
and S′ =S.
Proof: The uniqueness of the unit and the counit are obvious. There fore ⊓L and ⊓R are common
in these two WHA-s. In order to prove S′ =S introduce the convolution product
(f ⋄g)(x) := f (x(1))g(x(2)) , x ∈A (2.22)
on functions f,g ∈ HomK(A,A ). This is an associative operation in terms of which the
antipode axioms take the form
id ⋄S = ⊓L, S ⋄ id ⋄S =S, S ⋄ id = ⊓R .
NowS′ satisﬁes the same equations with the same ⊓L, ⊓R, therefore
S′ =S′ ⋄ id ⋄S′ =S′ ⋄ ⊓L =S′ ⋄ id ⋄S = ⊓R ⋄S =S ⋄ id ⋄S =S .
Q.e.d.
As a preparation for the Theorem below notice that the deﬁnit ions (2.1) have counterparts
involving the antipode:
⊓L(x) = ε(S(x)1(1))1(2) (2.23a) ⊓R(x) = 1 (1)ε(1(2)S(x)) (2 .23b)
As a matter of fact
⊓L(x) = ε(1(1) ⊓L (x))1(2) =ε(⊓L(x)1(1))1(2) =ε(x(1)S(x(2))1(1))1(2) =
= ε(⊓R(x(1))S(x(2))1(1))1(2) =ε(S(x(1))x(2)S(x(3))1(1))1(2) =
= ε(S(x)1(1))1(2)
where in the subsequent equations (2.1), (2.10), (A.8a), (2 .2b), (A.8b), and ﬁnally (A.9) have
been used. Eqn(2.23b) can be proven analogously. As the dual s of (2.23a-b) we have automat-
ically the identities
⊓L(x) = S(1(1))ε(1(2)x) (2 .24a) ⊓R(x) = ε(x1(1))S(1(2)). (2.24b)
9
Lemma 2.9 In a WHA A the following identities hold:
⊓L ◦S = ⊓L ◦ ⊓R = S ◦ ⊓R (2.25a)
⊓R ◦S = ⊓R ◦ ⊓L = S ◦ ⊓L (2.25b)
Proof: It is suﬃcient to prove the ﬁrst equalities in (2.25a) and (2 .25b) because the second ones
then follow by duality.
⊓L ◦S(x) = ε(1(1)S(x))1(2) =ε(1(1)S(x(1))x(2)S(x(3)))1(2) =
= ε(1(1)S(x(1)) ⊓L (x(2)))1(2) =ε(1(1)S(x(1))x(2))1(2)
= ⊓L ◦ ⊓R(x).
In a similar way one can verify ⊓R ◦S = ⊓R ◦ ⊓L. Q.e.d.
The above Lemma implies that S(AR) ⊂ AL and S(AL) ⊂ AR. On the other hand
Eqns(2.24a-b) say that AL ⊂ S(AR) and AR ⊂ S(AL). Therefore the antipode maps AL
ontoAR bijectively and maps AR ontoAL bijectively.
Theorem 2.10 Let A be a WHA. Then the antipode is antimultiplicative and anti co multi-
plicative,
S(xy) = S(y)S(x) x,y ∈A , (2.26)
S(x)(1) ⊗S(x)(2) = S(x(2)) ⊗S(x(1)) x ∈A , (2.27)
and the restrictions S|AL and S|AR are bijections such that
S(AL) = AR , S (AR) = AL . (2.28)
The unit and the counit are S-invariant,
S(1) = 1 , (2.29a) ε ◦S = ε . (2.29b)
FurthermoreS:A →A is invertible.
Proof: We have already shown (2.28). (2.27) is the dual of (2.26) an d (2.29a) is the dual of
(2.29b).
S(xy) = S(x(1)y(1))x(2)y(2)S(x(3)y(3)) = S(x(1)y(1)) ⊓L (x(2) ⊓L (y(2))) =
= S(x(1)y(1))x(2) ⊓L (y(2))S(x(3)) = ⊓R(⊓R(x(1))y(1))S(y(2))S(x(2)) =
= S(y(1)) ⊓R (x(1))y(2)S(y(3))S(x(3)) = S(y(1))y(2)S(y(3))S(x(1))x(2)S(x(3)) =
= S(y)S(x) .
Next we prove (2.29b).
ε(S(x)) = ε(S(x(1))x(2)S(x(3))) = ε(S(x(1)) ⊓L (x(2))) = ε(S(x(1))x(2)) = ε(⊓R(x)) =
= ε(x) .
In order to prove invertibility of S notice that the descending chain A ⊃S(A) ⊃S2(A) ⊃...
of WHAs all contain 1 by (2.29a). This implies the existence o f n ∈IN such that
1 ∈ Sn+1(A) = Sn(A) ⊂ Sn−1(A) .
10
We want to show that this implies Sn(A) = Sn−1(A). Replacing A bySn−1(A) it is therefore
enough to prove invertibility of S under the additional assumption S2(A) = S(A), implying
KerS ∩ S(A) = 0 .
In this case let ¯S :=S|S(A), then ¯S:S(A) →S(A) is bijective and
PS := ¯S−1 ◦S : A →S(A)
is a multiplicative idempotent satisfying
PS(xS(y)) = PS(x)S(y), x,y ∈A .
By (2.28)AL,R ⊂S(A). Now taking into account the identity x =x(1)S(x(2))x(3), which follows
directly from axioms (A.8a) and (A.4), then using also PS(1) = 1 we have
PS(x) = PS(x(1)S(x(2))x(3)) = PS (x(1))S(x(2))x(3) =PS(x(1)S(x(2)))x(3) =
= PS(1)x(1)S(x(2))x(3) =x,
so KerPS = KerS = 0. Q.e.d.
We are now able to derive (versions of) the original antipode axioms of [2, 20]:
x(1) ⊗x(2)S(x(3)) = 1 (1)x ⊗ 1(2) (2.30a)
S(x(1))x(2) ⊗x(3) = 1 (1) ⊗x1(2) (2.30b)
x(1) ⊗S(x(2))x(3) = x1(1) ⊗S(1(2)) (2.30c)
x(1)S(x(2)) ⊗x(3) = S(1(1)) ⊗ 1(2)x (2.30d)
The ﬁrst two are just rewritings of the bialgebra identities (2.8a-b). The second two are more
delicate.
x(1) ⊗S(x(2))x(3) = x(1) ⊗ε(x(2)1(1))S(1(2)) = x(1)1(1′) ⊗ε(x(2)1(2′)1(1))S(1(2)) =
= x(1)1(1)ε(x(2)1(2)) ⊗S(1(3)) = x1(1) ⊗S(1(2))
x(1)S(x(2)) ⊗x(3) = S(1(1))ε(1(2)x(1)) ⊗x(2) =S(1(1))ε(1(2)1(1′)x(1)) ⊗ 1(2′)x(2) =
= S(1(1)) ⊗ε(1(2)x(1))1(3)x(2) =S(1(1)) ⊗ 1(2)x
The following Proposition also holds, if A is just a WBA, see [14].
Proposition 2.11 Let A be a WHA over K. Then AL and AR are separable K-algebras, in
particular, they are semisimple.
Proof: Recall that an algebra A is separable if and only if there exists a q ∈ A ⊗A such
that (x ⊗ 1)q = q(1 ⊗x) holds for all x ∈ A and furthermore µ(q) = 1, where µ denotes the
multiplication map of A [18] . Such a q will be called a separable idempotent2. So, our proof
will consist of showing that qL =S(1(1)) ⊗ 1(2) ∈AL ⊗AL andqR = 1(1) ⊗S(1(2)) ∈AR ⊗AR
are separable idempotents of AL and AR, respectively. In fact we will prove the somewhat
more general identities
x(1)yR ⊗x(2) = x(1) ⊗x(2)S(yR) (2.31a)
x(1) ⊗yLx(2) = S(yL)x(1) ⊗x(2) (2.31b)
2In fact q is an idempotent only if considered as an element of A ⊗ Aop.
11
valid for all x ∈A andyL ∈AL, yR ∈AR. Pairing the LHS of (2.31a) with ϕ ⊗ψ, we obtain
⟨ϕ ⊗ψ,LHS ⟩ = ⟨ϕ(yR⇀ ˆ1),x (1)⟩⟨ψ,x (2)⟩= ⟨ϕ,x (1)⟩⟨(S(yR)⇀ ˆ1)ψ,x (2)⟩=
= ⟨ϕ ⊗ψ,RHS ⟩.
The proof of (2.31b) is simply the mirror image of the above ar gument. Q.e.d.
