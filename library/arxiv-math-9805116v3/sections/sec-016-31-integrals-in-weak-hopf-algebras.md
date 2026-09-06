---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras"
section_id: sec-016-31-integrals-in-weak-hopf-algebras
section_title: "Integrals in weak Hopf algebras"
section_number: 3.1
pages: 14-16
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
doc_brief: "Weak Hopf Algebras — We give an introduction to the theory of weak Hopf algebras pr oposed recently as a coassociative alternative of weak quasi-Hopf algebras."
---
The following deﬁnition provides the weak Hopf generalizat ion of the well known notion of
integrals in a Hopf algebra [19].
Deﬁnition 3.1 A left (right) integral in a weak Hopf algebra A is an element l ∈ A (r ∈ A)
satisfying
xl = ⊓L(x)l
(
rx = r ⊓R (x)
)
(3.1)
for all x ∈A. The space of left (right) integrals in A is denoted by IL(A) ( IR(A)). Elements
of I := IL(A) ∩ IR(A) are called two-sided integrals. A left or right integral in A is called
non-degenerate if it deﬁnes a non-degenerate functional on ˆA. l ∈ IL(A) is called normalized
if ⊓L(l) = 1 , r ∈ IR(A) is called normalized if ⊓R(r) = 1 .
Some equivalent formulations of left (right) integrals are gathered in the next
Lemma 3.2 Let A be a weak Hopf algebra. Then the following statements for an e lement
l ∈A are equivalent:
a) l ∈ IL(A)
b) l(1) ⊗xl(2) =S(x)l(1) ⊗l(2) for all x ∈A
c) l⇀ ˆA ⊂ ˆAL
d) (ϕ↼x )⇀l =S(x)(ϕ⇀l ) for all ϕ ∈ ˆA and x ∈A
e) (Ker⊓L)l = 0
f ) S(l) ∈ IR(A)
14
Proof: a) ⇒ b): Using (2.30b) and (2.7a) we have l(1) ⊗xl(2) = [ S(x(1)) ⊗ 1]∆( x(2)l) =
[S(x(1))x(2)S(x(3)) ⊗ 1]∆( l) = S(x)l(1) ⊗ l(2). b) ⇒ a): xl = x(1)l(1)ε(x(2)l(2)) =
x(1)S(x(2))l(1)ε(l(2)) = ⊓L(x)l. a) ⇔ c): For an l ∈A the equation ⟨l⇀ϕ,x ⟩= ⟨ˆ⊓L(l⇀ϕ ),x ⟩
is clearly equivalent to the equation ⟨ϕ,xl ⟩= ⟨ϕ, ⊓L(x)l⟩. b) ⇔ d): By pairing the 2nd tensor
factor of b) with an arbitraryϕ ∈ ˆA. a) ⇒ e): is obvious. e) ⇒ a): xl = [x−⊓L(x)]l+⊓L(x)l =
⊓L(x)l. f ) ⇔ a): This follows by applying S to (3.1). Q.e.d.
Deﬁnition 3.1 as well as Lemma 3.2 provide rather technical c haracterizations of integrals.
The next argument sheds some light on their real nature. Cons ider the left A-module map
εR from the left regular A-module to the trivial A-module given by acting with the trivial
representation on the cyclic vector ˆ1:
εR : AA → A ˆAR
x ↦→(x⇀ ˆ1) . (3.2)
The existence of this (non-zero) map shows that Hom ( AA, A ˆAR) is non-zero. However, there
is in general no guarantee that Hom ( A ˆAR, AA) is non-zero. Left integrals are precisely the
objects that label the possible homomorphisms of the latter type.
Lemma 3.3 Left integrals l in A are in one-to-one correspondence with left A-module homo-
morphisms f : A ˆAR → AA. The correspondence is given by f ↦→f (ˆ1) ∈ IL. What is more the
above map provides an isomorphism IL
A ∼= Hom (A ˆAR, AA) of right A-modules. In other words
IL
A is isomorphic to the A-dual of the trivial left A-module.
Proof: If f ∈ Hom (A ˆAR, AA) then xf (ˆ1) = f (x⇀ ˆ1) = f (⊓L(x)⇀ ˆ1) = ⊓L(x)f (ˆ1), hence
f (ˆ1) ∈ IL. This is obviously a right A-module map. It is invertible since for l ∈ IL the map
fl: ˆAR →A, fl(ϕR) := (1↼ϕR)l is a left A-module map and satisﬁes fl(ˆ1) = l. Q.e.d.
The identiﬁcation of IL with Hom (A ˆAR, AA) yields an A-valued bilinear form A ˆAR ×IL
A →
A given by evaluation, ( ϕR,l ) ↦→fl(ϕR). Replacing A ˆAR with AAL using the isomorphism of
Lemma 2.12 we obtain that this bilinear form is nothing but mu ltiplication in A
AAL × I L
A → AAA , (xL,l ) ↦→xLl (3.3)
and it is an A-A bimodule map. We claim that (3.3) is a non-degenerate biline ar form. From
one side, xLl = 0 ∀xL ∈ AL ⇒ l = 0, this is trivial. From the other side we will be able to
prove this after having established that WHAs are quasi-Fro benius algebras in Thm. 3.11. As
a matter of fact by Theorem 61.2 of [4] the left annihilator of the right annihilator of the left
ideal Ker ⊓L is Ker ⊓L itself. Now by Lemma 3.2.e) the right annihilator of Ker ⊓L is just IL.
ThusxLl = 0 ∀l ∈ IL ⇒ xL = 0 follows.
Now we turn to an other characterization of left integrals th at is related to conditional
expectations. Notice at ﬁrst that if λ ∈ I L( ˆA) then the map Eλ:x ↦→λ⇀x is an AL-AL-
bimodule map from A intoAL commuting with the right ˆA-action on A. In fact, all such maps
arise from a left integral, as the following Lemma shows.
Lemma 3.4 The left integrals λ ∈ I L( ˆA) are in one-to-one correspondence with right ˆA-
module maps E ∈ Hom (A ˆA,AL
ˆA) via
λ ↦→Eλ
E ↦→ε ◦E .
15
Proof: If λ is a left integral then Eλ is a right ˆA-module map and maps into AL by Lemma
3.2.c).
Now let E ∈ Hom (A ˆA,AL
ˆA). Then
E(x) = ε(1(1)E(x))1(2) =ε ◦E(S−1(1(1))x)1(2)
where we used the fact that a right ˆA-module map is an AL-AL-bimodule map by (2.20b) and
(2.21a). Hence
E(x) = ε ◦E(x(3))x(1)S(x(2)) = ⊓L(λ⇀x )
where λ :=ε ◦E. It remained to show that λ is a left integral.
⟨ϕλ,x ⟩=ε(E(x↼ϕ )) = ε(E(x)↼ϕ ) = ⟨ˆ⊓L(ϕ)λ,x ⟩
which proves the claim. Q.e.d.
The characterization of left integrals λ as ”conditional expectations” Eλ provides a link to
the theory of inclusions and ”Jones extensions” [15].
The properties of the normalized and the non-degenerate lef t integrals will be discussed in
later Subsections. Here we only remark that λ is non-degenerate iﬀ Eλ is non-degenerate and
λ is normalized iﬀ Eλ is unital.
There are two twisting operations A ↦→Aop andA ↦→Acop that produce WHAs from WHAs.
In the ﬁrst one the multiplication µ is replaced with opposite multiplication µop(x,y ) = µ(y,x )
while in the second the coproduct is replaced by ∆ op(x) = x(2) ⊗x(1). In both cases the
antipode is replaced by S−1. The left and right subalgebras /integrals and the dual WHAs of
the resulting four twisted versions of a WHA A are related to those of A as follows.
⊓L ⊓R AL AR IL IR ˆA
A =A(µ, ∆ ,S ) ⊓L ⊓R AL AR IL IR ˆA
Aop =A(µop, ∆ ,S −1) S−1 ◦ ⊓R S−1 ◦ ⊓L AL AR IR IL ˆAcop
Acop =A(µ, ∆ op,S −1) S−1 ◦ ⊓L S−1 ◦ ⊓R AR AL IL IR ˆAop
Aop
cop =A(µop, ∆ op,S ) ⊓R ⊓L AR AL IR IL ˆAop
cop
As an application of the table we give here the twisted versio ns of the identity of Lemma
3.2.d):
(ϕ↼x )⇀l = S(x)(ϕ⇀l ) (3.4a)
(x⇀ϕ )⇀r = ( ϕ⇀r )S−1(x) (3.4b)
l↼ (ϕ↼x ) = S−1(x)(l↼ϕ ) (3.4c)
r↼ (x⇀ϕ ) = ( r↼ϕ )S(x) (3.4d)
for all x ∈A, ϕ ∈ ˆA, l ∈ IL, and r ∈ IR.
