---
doc_id: arxiv-1004.1533v3
doc_title: "TURAEV-VIRO INV ARIANTS AS AN EXTENDED TQFT"
section_id: sec-011-7-extended-combinatorial-surfaces
section_title: "Extended combinatorial surfaces"
section_number: 7
pages: 24-27
source_pdf: 1004.1533v3.pdf
source_sha256: 95c1544431e6bf37
doc_brief: "TURAEV-VIRO INV ARIANTS AS AN EXTENDED TQFT — In this paper we show how one can extend Turaev-Viro invarian ts, deﬁned for an arbitrary spherical fusion category C, to 3-manifolds with cor- ners."
---
We begin by generalizing the deﬁnition of a polytope decomposition to e xtended
surfaces.
TURAEV-VIRO INV ARIANTS AS AN EXTENDED TQFT 25
Deﬁnition 7.1. A combinatorial extended surface N is a an extended surface N
together with a polytope decomposition such that
(1) The interior of each embedded disk is one of the 2-cells of the poly tope
decomposition.
(2) Each marked point Pα on the boundary of an embedded disk is a vertex
(0-cell) of the polytope decomposition.
We can now deﬁne the state space for such a surface. Let N be a combinatorial
extended surface, and Yα,α ∈ D(N ), — a coloring of N . Let l be a labeling of
edges of N . Then we deﬁne the state space
H(N, {Yα },l ) =
⨂
C
H(C,l )
where the product is over all 2-cells of N (including the embedded disks) and
H(C,l ) =
{
⟨Yα,l (e1),l (e2),...,l (en)⟩ C =Dα – an embedded disk
⟨l(e1),l (e2),...,l (en)⟩ C – an ordinary 2-cell of N
where e1,e 2,... are edges of C traveled counterclockwise; for the embedded disks,
we also require that we start with the marked point Pα ; for ordinary 2-cells of N
the choice of starting point is not important.
As usual, we now deﬁne
(7.1) H(N, {Yα }) =
⨁
l
H(N, {Yα },l )
where the sum is taken over all equivalence classes of simple labellings l of edges of
N .
Note that so deﬁned state space is functorial in Yα and functorial under home-
omorphism of extended surfaces; it is also immediate from the deﬁnit ion that one
has a canonical isomorphism
H(N,Y ∗
α ) = H(N,Y α )∗.
Example 7.2. Let N be the sphere with n embedded disks and the cell decompo-
sition shown in Figure 24. Then
Figure 24. n-punctured sphere
26 BENJAMIN BALSAM AND ALEXANDER KIRILLOV, JR.
H(N,Y 1,...,Y n)
=
⨁
X1,...,X n,U 1,...,U n∈Irr(C)
⟨X1,U 1,X ∗
1,...,X n,U n,X ∗
n⟩ ⊗ ⟨U ∗
1,Y 1⟩ ⊗ · · · ⊗ ⟨U ∗
n,Y n⟩
≃
⨁
X1,...,X n∈Irr(C)
⟨X1,Y 1,X ∗
1,...,X n,Y n,X ∗
n⟩.
where the last isomorphism is given by direct sum of rescaled composit ions (1.10).
The ﬁrst main result of this paper is the gluing axiom for the so deﬁned state
space.
Theorem 7.3. Let N be a combinatorial extended surface and Da,D b — two
distinct embedded disks. Let N ′ be the extended surface obtained by removing the
disks Da, Db and connecting the resulting boundary circles with a cylind er with
the polytope decomposition consisting of a single 2-cell an d a single 1-cell as shown
below:
Figure 25. Gluing of extended surfaces. To help visualize the
cylinder, it is colored light gray.
Thus, the set D′ of embedded disks of N ′ is D′ =D(N ) \ {a,b }
Then one has a natural isomorphism
H(N ′, {Yα }α ∈D′) =
⨁
Z∈Irr(Z(C))
H(N, {Yα }α ∈D′,Z,Z ∗)
where objects Z,Z ∗ are assigned to embedded disks Da,D b.
Proof. For a given labeling l of edges of N , let
H0(l) =
⨂
C
H(C,l )
where the product is taken over all 2-cells of N (including the embedded disks)
except Da, Db. Then
H(N, {Yα },Z,Z ∗,l ) = H0(l) ⊗ ⟨Z,A ⟩ ⊗ ⟨Z ∗,B ⟩
whereA =l(e1) ⊗l(e2) · · · ⊗l(en), where e1,e 2,... are edges of Da traveled coun-
terclockwise starting with the marked point Pa, and similarly for B.
TURAEV-VIRO INV ARIANTS AS AN EXTENDED TQFT 27
On the other hand, for a given labeling l′ of edges of N ′, we have
H(N ′, {Yα },l ′) = H0(l) ⊗ ⟨A ⊗l(e) ⊗B ⊗l(e)∗⟩
where l is the restriction of labeling l′ to edges of N , and e is the added edge
connecting marked points Pa, Pb.
Thus, the theorem immediately follows from the following lemma.
Lemma 7.4. For any A,B ∈ Obj C, the map
(7.2)
⨁
Z∈Irr(Z(C))
⟨Z,A ⟩ ⊗ ⟨Z ∗,B ⟩ →
⨁
X∈Irr(C)
⟨A,X,B,X ∗⟩
ϕ ⊗ψ ↦→
⨁
X∈Irr(C)
√dX
√dZ
D ϕ ψ
A B
Z
X
is an an isomorphism.
(The factor √dX
√dZ/ D is introduced to make this isomorphism agree with
pairing (1.6).)
Proof. By Theorem 2.3, we have
⨁
X∈Irr(C)
⟨A ⊗X ⊗B ⊗X ∗⟩ =
⨁
X
HomC(A∗,X ⊗B ⊗X ∗)
= Hom C(A∗,FI (B)) = Hom Z(C)(I(A∗),I (B))
On the other hand,
⨁
Z∈Irr(Z(C))
⟨Z,A ⟩ ⊗ ⟨Z ∗,B ⟩ =
⨁
Z
HomC(Z ∗,A ) ⊗ HomC(Z,B )
=
⨁
Z
HomZ(C)(Z ∗,I (A)) ⊗ HomZ(C)(Z,I (B))
=
⨁
Z
HomZ(C)(I(A)∗,Z ) ⊗ HomZ(C)(Z,I (B))
= Hom Z(C)(I(A)∗,I (B))
(using semisimplicity of Z(C)). □
This completes the proof of the lemma and thus the theorem. □
