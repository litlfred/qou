---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras"
section_id: sec-018-33-restrictions-on-the-algebraic-structure
section_title: "Restrictions on the algebraic structure"
section_number: 3.3
pages: 21-22
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
doc_brief: "Weak Hopf Algebras — We give an introduction to the theory of weak Hopf algebras pr oposed recently as a coassociative alternative of weak quasi-Hopf algebras."
---
The existence of a weak Hopf structure on the K-algebraA involves certain restrictions on the
algebra A, just like in case of Hopf algebras. In this subsection we sho w that any WHA A is
quasi-Frobenius, i.e. self-injective. The notions of semi simple and separable algebras coincide
within the class of WHAs. Moreover, we prove an analogue of Ma schke’s Theorem which claims
that A is semisimple if and only if it has normalized left integrals .
Theorem 3.11 Every weak Hopf algebra over a ﬁeld K is a quasi-Frobenius algebra.
Proof: By Theorem 61.2 of [4] it is suﬃcient to prove that the left re gular A-module AA is
injective. By the Nagao–Nakayama theorem injectivity of a l eftA-module is equivalent to that
it is a direct sum of K-duals of principal indecomposable right A-modules. Since ˆAA is the
K-dual of AA, we need to show that ˆAA is a direct sum of principal indecomposable right A-
modules, i.e. that ˆAA is projective. This in turn is a consequence of the Fundament al Theorem
of WHM-s.
As a matter of fact we have the right A-module isomorphisms
ˆAA ∼= IL( ˆA) ⊗
AL
AA ∼=P (IL( ˆA) ⊗
K
AA) (3.28)
the ﬁrst of which is the consequence of the Fundamental Theor em of the right WHM ˆA
ˆAA, the
second of which is a rather simple property of the amalgamate d tensor product with respect
to the separable algebra AL. In order to explain the projection P here we make a digression.
Lemma 3.12 Deﬁne the map P : IL( ˆA) ⊗
K
A → IL( ˆA) ⊗
K
A by
P (λ ⊗x) := S2(1(1))⇀λ ⊗ 1(2)x . (3.29)
Then P ◦P = P and Ker P coincides with Ker π of the canonical projection π from the free
right A module IL( ˆA) ⊗
K
AA onto IL( ˆA) ⊗
ALAA. Therefore
P (IL( ˆA) ⊗
K
AA)
π|ImP
− → IL( ˆA) ⊗
AL
AA (3.30)
is an isomorphism of right A-modules.
Proof: The kernel of the canonical projection is
Kerπ = Span K {(λ ⊗xLy) − (S(xL)⇀λ ⊗x) | λ ⊗y ∈ IL( ˆA) ⊗A, xL ∈AL } (3.31)
If∑
i(λi ⊗xi) ∈ Kerπ then obviously ∑
iS2(1(1))⇀λi ⊗ 1(2)xi = 0, therefore Ker π ⊂ KerP .
Now assume ∑ λi ⊗xi ∈ KerP . Then
∑
i
λi ⊗xi =
∑
i
λi ⊗S(1(1))1(2)xi =
∑
i
[λi ⊗S(1(1))(1(2)xi) −S2(1(1))⇀λi ⊗ 1(2)xi] ∈ Kerπ
This proves Ker π = Ker P . That P is a projection and a right A-module map is trivial to
verify. Therefore π|ImP is an A-module isomorphism. Q.e.d.
21
Back to the Proof of Theorem 3.11 : In virtue of the above Lemma the amalgamated tensor
product IL( ˆA) ⊗
AL
AA is the direct summand of a free A-module, hence projective. By Equation
3.28 this is isomorphic to ˆAA. This proves projectivity of ˆAA, hence injectivity of AA. Q.e.d.
The equivalence of (c) and (d) of the next Theorem provides a w eak Hopf version of Maschke’s
Theorem known for Hopf algebras as well [9]. Below we denote εR(x) := x⇀ ˆ1.
Theorem 3.13 The following conditions on a WHA A over K are equivalent:
a) A is semisimple.
b) In the category of left A-modules the following exact sequence is split
0 − →KerεR − →AA εR
− →A ˆAR − →0
c) There exists a normalized left integral l ∈A.
d) A is a separable K-algebra.
Proof: (a ⇒c): If A is semisimple, then Ker ⊓L ≡ KerεR being a a left ideal there exists
p =p2 ∈A such that Ker ⊓L =Ap, whence l = 1 −p is a normalized left integral by Lemma
3.2.e.
(b⇔c): Let F ∈ Hom (A ˆAR, AA) be such that εR ◦F = id . Then xF (ˆ1) = F (x⇀ ˆ1) =
⊓L(x)F (ˆ1), for x ∈A, therefore F (ˆ1) ∈ IL(A). Moreover, ˆ1 = εR(F (ˆ1)) = F (ˆ1)⇀ ˆ1 implying
⊓L(F (ˆ1)) = 1. Conversely, if l ∈ I L is a normalized left integral then F ∈ Hom (A ˆAR,AA)
given by F (εR(x)) := xl satisﬁes εR ◦F = id .
(c⇒d): Let l be a normalized left integral. Then q =l(1) ⊗S(l(2)) is a separating idempotent
for A. As a matter of fact µ(q) = 1 follows from the normalization ⊓L(l) = 1 while ( x ⊗ 1)q =
q(1 ⊗x) is precisely the left integral property of Lemma 3.2.b.
(d⇒a): This is a standard result [18]. Q.e.d.
