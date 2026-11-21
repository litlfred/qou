---
doc_id: arxiv-hep-th-0610241v1
doc_title: "Gravity and the standard model with neutrino mixing"
section_id: sec-002-21-the-left-right-symmetric-algebra
section_title: "The left-right symmetric algebra"
section_number: 2.1
pages: 5-7
source_pdf: hep-th-0610241.pdf
source_sha256: 6a71ab6f6459c070
toc_source: inferred
doc_brief: "Gravity and the standard model with neutrino mixing — We present an eﬀective uniﬁed theory based on noncommutative geometry for the standard model with neutrino mixing, minimally coupled to gravity."
---
The main input for the model we are going to describe is the choice of a ﬁnite dimensional
involutive algebra of the form
ALR = C ⊕HL ⊕HR ⊕M3(C).
(2.1)
This is the direct sum of the matrix algebras MN(C) for N = 1, 3 with two copies of the
algebra H of quaternions, where the indices L, R are just for book-keeping. We refer to (2.1)
as the “left-right symmetric algebra” [10].
By construction ALR is an involutive algebra, with involution
(λ, qL, qR, m)∗= (¯λ, ¯qL, ¯qR, m∗),
(2.2)
where q 7→¯q denotes the involution of the algebra of quaternions. The algebra ALR admits
a natural subalgebra C ⊕M3(C), corresponding to integer spin, which is an algebra over C.
The subalgebra HL ⊕HR, corresponding to half-integer spin, is an algebra over R.
2.2. The bimodule MF .
Let M be a bimodule over an involutive algebra A.
For u ∈A unitary, i.e. such that
uu∗= u∗u = 1, one deﬁnes Ad(u) by Ad(u)ξ = uξu∗, ∀ξ ∈M.
Deﬁnition 2.1. Let M be an ALR-bimodule. Then M is odd iﬀthe adjoint action of s =
(1, −1, −1, 1) fulﬁlls Ad(s) = −1.
Let A0
LR denote the opposite algebra of ALR.
Lemma 2.2. An odd bimodule M is a representation of the reduction B = (ALR ⊗R A0
LR)p
of ALR ⊗R A0
LR by the projection p = 1
2 (1 −s ⊗s0). This subalgebra is an algebra over C.
Proof. The result follows directly from the action of s = (1, −1, −1, 1) in Deﬁnition 2.1.
6
CHAMSEDDINE, CONNES, AND MARCOLLI
Since B = (ALR ⊗R A0
LR)p is an algebra over C, we restrict to consider complex representa-
tions.
Deﬁnition 2.3. One deﬁnes the contragredient bimodule of a bimodule M as the complex
conjugate space
M0 = {¯ξ ; ξ ∈M} ,
a ¯ξ b = b∗ξ a∗,
∀a , b ∈ALR.
(2.3)
The algebras MN(C) and H are isomorphic to their opposite algebras (by m 7→mt for matrices
and q 7→¯q for quaternions. We use this antiisomorphism to obtain a representation π0 of the
opposite algebra from a representation π .
We follow the physicists convention to denote an irreducible representation by its dimension
in boldface. So, for instance, 30 denotes the 3-dimensional irreducible representation of the
opposite algebra M3(C).
Proposition 2.4. Let MF be the direct sum of all inequivalent irreducible odd ALR-bimodules.
• The dimension of the complex vector space MF is 32.
• The ALR-bimodule MF = E ⊕E0 is the direct sum of the bimodule
E = 2L ⊗10 ⊕2R ⊗10 ⊕2L ⊗30 ⊕2R ⊗30
(2.4)
with its contragredient E0.
• The ALR-bimodule MF is isomorphic to the contragredient bimodule M0
F by the anti-
linear isometry JF given by
JF (ξ, ¯η) = (η, ¯ξ) ,
∀ξ , η ∈E
(2.5)
• One has
J2 = 1 ,
ξ b = Jb∗J ξ ,
∀ξ ∈MF , b ∈ALR
(2.6)
Proof. The ﬁrst two statements follow from the structure of the algebra B described in the
following lemma.
Lemma 2.5. The algebra B = (ALR ⊗R A0
LR)p is the direct sum of 4 copies of the algebra
M2(C) ⊕M6(C).
The sum of irreducible representations of B has dimension 32 and is given by
2L ⊗10 ⊕2R ⊗10 ⊕2L ⊗30 ⊕2R ⊗30 ⊕1 ⊗20
L ⊕1 ⊗20
R ⊕3 ⊗20
L ⊕3 ⊗20
R
(2.7)
Proof. By construction one has
B = (HL ⊕HR) ⊗R (C ⊕M3(C))0 ⊕(C ⊕M3(C)) ⊗R (HL ⊕HR)0
Thus the ﬁrst result follows from the isomorphism:
H ⊗R C = M2(C) ,
H ⊗R M3(C) = M6(C)
The complex algebra MN(C) admits only one irreducible representation and the latter has
dimension N. Thus the sum of the irreducible representations of B is given by (2.7). The
dimension of the sum of irreducible representations is 4 × 2 + 4 × 6 = 32.
To end the proof of Proposition 2.4 notice that by construction MF is the direct sum E ⊕E0
of the bimodule (2.4) with its contragredient, and that the map (2.5) gives the required
antilinear isometry. Note moreover that one has (2.6) using (2.3).
GRAVITY AND THE STANDARD MODEL WITH NEUTRINO MIXING
