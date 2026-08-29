---
doc_id: arxiv-math-0111205v1
doc_title: "From Subfactors to Categories and Topology II"
section_id: sec-038-1-c-that-is-equivalent-to-z1c-as-a-tensor-catego
section_title: "(C) that is equivalent to Z1(C) as a tensor category. Given an isomorphism"
section_number: 1
pages: 42-44
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
doc_brief: "From Subfactors to Categories and Topology II — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
s : X → Y in a W ∗-category we can use polar decomposition [17] to obtain a uni tary
morphism ˜s : X → Y . But we cannot construct a unitary half-braiding in this way since
it is not clear that the unitaries eX (Z), Z ∈ C can be chosen such that naturality (3.1) and
the braid relation (3.2) hold. Therefore a global approach i s needed, which we develop
using our machinery from Section 4.
Let C be a ∗-category with conjugates, simple unit and ﬁnitely many sim ple objects. All
dimensions d(X) are positive, and we choose the square roots of the latter an d of dim C to
be positive. Reconsidering the constructions of Section 4 w e now choose the bases {tkα
ij } in
HomC(Xk, XiXj) to be orthonormal, i.e. t′kα
ij = tkα
ij
∗, and similarly v′
i = v∗
i . Then v′ = v∗
and w′ = w∗, such that the considerations of [38, Subsection 5.3] apply . We thus obtain
a ∗-bicategory E∗ ⊂ E which is equivalent to E. The considerations in Sections 4 and 5
of this paper remain essentially unchanged except for repla cing ε(X), ε(X) by standard
solutions rX , rX of the conjugate equations [31] everywhere.
Lemma 6.3 Let C be a ∗-category. Let (X, eX ) ∈ Z 1(C) and F (X, eX ) = ( J (X ⊠1)J, pX ).
Then the idempotent pX ∈ EndE (J (X ⊠ 1)J) satisﬁes pX = p#
X iﬀ eX (Z) is unitary for
all Z.
Proof. We recall from Proposition 4.5 that pX is given by
pX = λ−1∑
i
vi ⊗ idX⊠1 ◦ eX (Xi) ⊠ idXop
i
◦ idX⊠1 ⊗ v′
i.
42
In view of the deﬁnition [38, Subsection 5.3] of the involuti on # on End E (J(X ⊠ 1)J) ≡
HomA(J (X ⊠ 1)J Q, QJ (X ⊠ 1)J) we have
p#
X = λ−1∑
i
Q X ⊠ 1
☛ ✟r∗
vi
ˆXi
e∗
i
ˆXi
v∗
i
r
✡ ✠
X ⊠ 1 Q
where e∗
i ≡ eX (Xi)∗ ⊠ idXop
i
and r = w ◦ v : 1 → Q2. In view of (4.3) it is clear that there
are uniquely determined ˆri : 1 → ˆXı ⊗ ˆXi, i ∈ Γ such that
r =
∑
i
vı ⊗ vi ◦ ˆri.
Using id Q ⊗ r∗ ◦ r ⊗ idQ = id Q one easily shows
id ˆXi
⊗ ˆr∗
i ◦ ˆrı ⊗ id ˆXi
= id ˆXi
.
(This amounts to the identiﬁcation ˆri = ˆrı which is possible since all the self-conjugate
ˆXi, i ∈ Γ are orthogonal.) Thus
v∗
i ⊗ idQ ◦ r = id ˆXi
⊗ vı ◦ ˆrı, idQ ⊗ v∗
i ◦ r = vı ⊗ id ˆXi
◦ ˆri,
and we obtain
p#
X = λ−1∑
i
Q X ⊠ 1
☛ ✟ˆr∗
ı
v∗
ı
ˆXi
e∗
i
ˆXi
vı
ˆri
✡ ✠
X ⊠ 1 Q
This equals pX iﬀ
idXıX ⊗ r∗
i ◦ idXı ⊗ eX (Xi)∗ ⊗ idXı ◦ ri ⊗ idXX ı = eX (Xı) ∀i ∈ Γ .
Considering Lemma 3.8, this is the case iﬀ eX(Xi)∗ = eX(Xi)−1 for all i ∈ Γ. In view of
Lemma 3.3 and the fact that the xα
i occurring in its proof are automatically isometries,
this is equivalent to unitarity of eX(Z) for all Z. ■
43
Theorem 6.4 Let C be a tensor ∗-category with simple unit, ﬁnitely many simple objects,
conjugates, direct sums and subobjects. Then Z ∗
