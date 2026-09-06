---
doc_id: arxiv-math-9804005v3
doc_title: "RINGS WITH AUSLANDER DUALIZING COMPLEXES"
section_id: sec-044-3-let-p1-pm-be-the-minimal-prime-ideals-of-a-the
section_title: "Let p1,... , pm be the minimal prime ideals of A. Then ( ∏"
section_number: 3
pages: 24-25
source_pdf: 9804005v3.pdf
source_sha256: 62d069533bb97a00
doc_brief: "RINGS WITH AUSLANDER DUALIZING COMPLEXES — A ring with an Auslander dualizing complex is a generalizati on of an Auslander-Gorenstein ring."
---
i pi)n = 0 for some
n, and we can use parts 1 and 2.
Proposition 4.19. Let A → B be a ﬁnite homomorphism of connected graded
algebras, and assume B ∼= A ⊕L as graded A-bimodules. If B has a balanced
dualizing complex then so does A.
Proof. Let M be a ﬁnitely generated graded A-module. Then by Lemma 4.15 we
get
RΓ mB (B ⊗AM ) ∼= RΓ mA(B ⊗AM ) ∼= RΓ mAM ⊕ RΓ mA(L ⊗AM ).
By Theorem 4.5 and Lemma 4.4 applied to B, we see that the graded B-module
HiRΓ mB (B ⊗AM ) is right bounded, and vanishes for large i. Hence the same is
true for the A-module HiRΓ mAM . Now apply Theorem 4.6.
We do not know if the under the assumptions of the proposition abov e the
Auslander property can be transferred from B to A. However as shown to us by
Van den Bergh this is true in a special case:
RINGS WITH AUSLANDER DUALIZING COMPLEXES 25
Proposition 4.20. Let G be a ﬁnite group of order prime to chark, acting on B
by graded k-algebra automorphisms, and let A := BG be the ﬁxed ring. If B is
graded Auslander then so is A.
Proof. Given a ﬁnitely generated graded A-module M and a graded A◦-submodule
N ⊂ Extq
A(M,RA) we want to prove that Ext p
A◦ (N,RA) = 0 for all p < q. Let
L := {b ∈ B |∑
g∈Gg(b) = 0 }, so B = A ⊕L. We have isomorphisms of graded
A◦-modules
Extq
A(M,RA) ⊕ Extq
A(L ⊗AM,RA) ∼=
Extq
A(B ⊗AM,RA) ∼= Extq
B(B ⊗AM,RB)
that respect the G-action. Note that G acts trivially on Ext q
A(M,RA). Consider
the graded B◦-module N ·B ⊂ Extq
B(B ⊗AM,RB). Clearly N ·B = N +N ·L.
But if
n =
∑
i
nili ∈N ∩ (N ·L)
with ni ∈N and li ∈L, then
n = |G|−1∑
g∈G
g
( ∑
i
nili
)
=
∑
i
ni · |G|−1∑
g∈G
g(li) = 0.
We conclude that N ·B =N ⊕N ·L as graded A◦-modules. Therefore
Extp
A◦ (N,RA) ⊕ Extp
A◦(N ·L,RA) ∼=
Extp
A◦ (N ·B,RA) ∼= Extp
B◦ (N ·B,RB) = 0.
