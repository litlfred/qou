---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras"
section_id: sec-017-32-weak-hopf-modules
section_title: "Weak Hopf modules"
section_number: 3.2
pages: 16-21
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
doc_brief: "Weak Hopf Algebras — We give an introduction to the theory of weak Hopf algebras pr oposed recently as a coassociative alternative of weak quasi-Hopf algebras."
---
Let A be a WHA. Recall that a left A-module is a K-linear space M carrying a left action of
the algebra A, denoted by x ∈ A,m ∈ M ↦→x ·m. A right A-module is a left module M of
the opposite algebra Aop with action denoted by x ∈A,m ∈M ↦→m ·x. Since A is unital, all
modules are assumed to be non-degenerate, i.e. 1 acts as the i dentity. The left A-module M is
called faithful if x ·m = 0, ∀m ∈M implies x = 0.
16
The A-modules know nothing about the coalgebra structure of A. The left A-comodules
M in turn are the comodules of the coalgebra A and carry no information about the algebra
structure of A. The left coaction is denoted by m ↦→m−1 ⊗m0 ∈A ⊗M . One deﬁnes the right
A-comodules analogously and denotes the coaction as m ↦→m0 ⊗m1 ∈M ⊗A.
Because of the ﬁnite dimensionality of A there is a one-to-one correspondence between left
(right)A-coactions on M and right (left) ˆA-actions on M given by
m ·ϕ = ⟨ϕ,m −1⟩m0 , m −1 ⊗m0 =
∑
i
bi ⊗m ·βi (3.5)
ϕ ·m = m0⟨ϕ,m 1⟩, m 0 ⊗m1 =
∑
i
βi ·m ⊗bi . (3.6)
Here {bi} denotes an arbitrary basis of A and {βi} is its dual basis: ⟨βi,bj⟩=δij. There are 8
basic examples of A modules with the target space M being either A itself or its dual ˆA. These
are the following.
AA :: x ·y =xy, A A :: y ·x =yx
AA :: x ·y =yS(x), A A :: y ·x =S(x)y
A ˆA :: x ·ϕ =x⇀ϕ, ˆAA :: ϕ ·x =ϕ↼x
A ˆA :: x ·ϕ =ϕ↼S (x), ˆAA :: ϕ ·x =S(x)⇀ϕ
where the Sweedler arrow notation (2.14) has been used. They all are faithful and non-
degenerate due to the existence of a unit and a counit. To each of the A-modules in the above
list there is a corresponding ˆA-comodule denoted by the same symbol. This identiﬁcation is
justiﬁed also by the fact that N ⊂M is an A-submodule if and only if it is an ˆA-subcomodule.
By analogy with our deﬁnition of left integrals, the space of invariants of a left A-module
M is deﬁned to be the subspace
InvM := {m ∈M |x ·m = ⊓L(x) ·m, ∀x ∈A } (3.7)
By the same methods as in Lemma 3.3, Inv M is linearly isomorphic to Hom ( A ˆAR,AM ) via
InvM = {f (ˆ1) |f ∈ Hom (A ˆAR,AM )}. (3.8)
By duality, we deﬁne the coinvariants of a right A-comodule M as
CoinvM := {m ∈M |m0 ⊗m1 =m0 ⊗ ⊓L(m1)} (3.9)
Thus, m ∈ CoinvM ⇔ m0 ⊗m1 ∈ M ⊗AL and for a left A-module M , the invariants
InvM ⊂ M coincide with Coinv M ⊂ M considered as an ˆA-comodule. Similarly, for a right
A-module (left A-comodule) M the invariants (coinvariants) are
InvM = {m ∈M |m ·x =m · ⊓R(x), ∀x ∈A } (3.10)
CoinvM = {m ∈M |m−1 ⊗m0 = ⊓R(m−1) ⊗m0}. (3.11)
Notice that the (co)invariants do not form a sub(co)module, even not an AL/R-submodule.
Scholium 3.5 The invariants of the left (right) regular A-module are precisely the left (right)
integrals of A:
InvAA = IL(A) , InvAA = IR(A) .
The invariants of A ˆA and ˆAA, on the other hand, yield the left and right subalgebras, res pec-
tively:
InvA ˆA = ˆAL , Inv ˆAA = ˆAR .
17
Investigating the structure of the mixed modules ˆA
ˆAA and A ˆA ˆA, that incorporate the whole
bialgebra structure of A, one arrives to a weak generalization of the notion of Hopf mo dules
[1, 19].
Deﬁnition 3.6 A right weak Hopf module (right WHM) over A is a right A moduleM which
is also a right A-comodule such that the compatibility relation
(m ·x)0 ⊗ (m ·x)1 = m0 ·x(1) ⊗m1x(2) (3.12)
holds for x ∈A, m ∈M .
Lemma 3.7 LetM be a right WHM over A. Then for all m ∈M
i) m0 · ⊓R(m1) = m
ii) CoinvM = {m ∈M |m0 ⊗m1 =m · 1(1) ⊗ 1(2)} and CoinvM is a right AL submodule.
iii) E(m) := m0 ·S(m1) provides a projection E :M → CoinvM .
Proof: i) Let M be a right WHM over A. Since
m0ε(m1x) = m0 · 1(1)ε(m11(2)x) = m0 · 1(1)ε(m11(2))ε(1(3)x) = m · 1(1)ε(1(2)x) (3.13)
for all x ∈A, we have m0 ⊗ ˆ1↼m 1 =m · 1(1) ⊗ ˆ1↼ 1(2), so that
m0 · ⊓R(m1) = m0 · [(ˆ1↼m 1)⇀ 1] = m · 1(1)[(ˆ1↼ 1(2))⇀ 1] = m · 1(1) ⊓R (1(2)) = m. (3.14)
ii) The inclusion ⊃ follows from (2.4). Conversely, if m ∈ CoinvM then m0 ⊗m1 ∈M ⊗AL,
implying by (2.3a), (2.10) and (3.13)
m0 ⊗m1 =m0 ⊗ε(m11(1))1(2) =m · 1(1) ⊗ε(1(2)1(1′))1(2′) =m · 1(1) ⊗ 1(2).
Also ∆( AL) ⊂A ⊗AL and therefore Coinv M is a right AL-submodule.
iii) To check that n :=m0 ·S(m1) is a coinvariant for all m ∈M we compute
n0 ⊗n1 = ( m0 ⊗m1)(·(S(m2)(1) ⊗S(m2)(2)) =
= m0 ·S(m3) ⊗m1S(m2) = m0 ·S(1(2)m1) ⊗S(1(1)) =
= n · 1(1) ⊗ 1(2).
Since for n ∈ CoinvM we haven0 ·S(n1) = n · 1(1)S(1(2)) = n,E is a projection onto Coinv M .
Q.e.d.
Example 3.8 The right weak Hopf module ˆA
ˆAA
As a linear space the module is the dual WHA ˆA. The right action and coaction are
ϕ ·x :=S(x)⇀ϕ, ϕ 0 ⊗ϕ1 :=
∑
i
βiϕ ⊗bi . (3.15)
Clearly, the right A-coaction is dual to the left ˆA-multiplication and therefore counital and
right-coassociative. The compatibility condition (3.12) can be seen as follows.
(ϕ ·x)0 ⊗ (ϕ ·x)1 =
∑
i
βi(S(x)⇀ϕ ) ⊗bi =
18
=
∑
i
βi
[
S(x(1))⇀x (2)S(x(3))⇀ϕ
]
⊗bi =
=
∑
i
βi
[
S(x(1))⇀ (x(2)⇀ ˆ1)ϕ
]
⊗bi =
=
∑
i
βi
[
S(x(2))x(3)⇀ ˆ1
][
S(x(1))⇀ϕ
]
⊗bi =
=
∑
i
[
S(x(2))x(3)⇀βi
][
S(x(1))⇀ϕ
]
⊗bi =
=
∑
i
S(x(1))⇀
[
(x(2)⇀βi)ϕ
]
⊗bi =
=
∑
i
S(x(1))⇀ (βiϕ) ⊗bix(2) =
= ϕ0 ·x(1) ⊗ϕ1x(2) .
The A-coinvariants of this WHM coincide with the ˆA-invariants of the dual left regular ˆA-
module ˆA
ˆA and therefore with the space of left integrals in ˆA by Scholium 3.5,
Coinv ( ˆA
ˆAA) = IL( ˆA). (3.16)
The Fundamental Theorem of Hopf modules generalizes to the w eak case as follows.
Theorem 3.9 Let A be a WHA, M be a right WHM over A and let N = Coinv M denote
the set of coinvariants of M . Since N is a right AL submodule, one can form the AL-module
tensor product N ⊗
AL
A and make it into a right WHM by the deﬁnitions
(n ⊗a) ·x := n ⊗ax (3.17a)
(n ⊗a)0 ⊗ (n ⊗a)1 := ( n ⊗a(1)) ⊗a(2) (3.17b)
wherea,x ∈A,n ∈N . Then the map
α : N ⊗
AL
A → M , n ⊗x ↦→n ·x (3.18)
is an isomorphism of right WHM-s.
Recall that an isomorphism of WHM-s is just a module isomorphism which is a comodule
isomorphism at the same time.
Proof: That α is a module map and comodule map is easy to verify. To construc t the
inverse deﬁne
β : M → N ⊗
AL
A
β(m) = m0 ·S(m1) ⊗m2 ≡ E(m0) ⊗m1 . (3.19)
Then β is obviously a comodule map. We show that it is also a module ma p.
β(m ·x) = m0 ·x(1)S(m1x(2)) ⊗m2x(3) =
= m0 · ⊓L(x(1))S(m1) ⊗ m2x(2) =
= m0 ·S(m11(1)) ⊗ m21(2)x =
= β(m) ·x
19
We are left with showing that on the one hand
β ◦α(n ⊗x) = β(n ·x) = β(n) ·x =n · 1(1)S(1(2)) ⊗ 1(3)x =
= n ⊗ 1(1)S(1(2))1(3)x =
= n ⊗x
and on the other hand
α ◦β(m) = m0 ·S(m1)m2 = m
where in the last equality Lemma 3.7i) has been used. Q.e.d.
Applying this Theorem to the WHM of Example 3.8 we obtain the r ight WHM isomorphism
ˆA
ˆAA ∼= IL( ˆA) ⊗
AL ˆAAA . (3.20)
Corollary 3.10 In any WHA A the space of left integrals IL(A) = S(IR(A)) is non-zero and
IL( ˆA) is the dual of IR(A) with respect to the restriction of the canonical pairing. Mo reover,
choosing a basis {λa} in IL( ˆA) and taking its dual basis {ra} in IR(A), we have
ˆ1 =
∑
a
S(ra)⇀λa (3.21)
1 =
∑
a
ra↼ ˆS(λa) (3.22)
Proof: IL( ˆA) ⁄= 0 follows from (3.20). By inspecting the form of the project ion E :M →N in
Example 3.8 we get a projection L:A → IL(A) onto the left integrals,
L(x) =
∑
i
ˆS2(βi)⇀ (bix) . (3.23)
Therefore the projection to the right integrals is
R(x) = S ◦L ◦S−1(x) =
∑
i
(xbi)↼ ˆS2(βi) . (3.24)
Similar expressions deﬁne the projections ˆL and ˆR to the dual integrals. Now it is easy to
check that
⟨ˆL(ϕ),x ⟩ = ⟨ϕ,R (x)⟩ (3.25)
proving the non-degeneracy of the restriction of the canoni cal pairing to IL( ˆA) × IR(A).
The dual bases satisfy ⟨λa,rb⟩=δab therefore
⟨λa, xS(ra)⟩ = ⟨ˆL(βi), xS(bi)⟩= ⟨S2(bj)⇀βjβi, xS(bi)⟩= ⟨βk,xS ◦ ⊓R(bk)⟩=(3.26)
= ⟨1(2)⇀ ˆ1,xS (1(1))⟩ (3.27)
where in the last step we used (2.19b). This proves (3.21). (3 .22) is the twisted version in Aop
cop.
Q.e.d.
20
