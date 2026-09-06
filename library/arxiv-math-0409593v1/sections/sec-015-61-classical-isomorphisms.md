---
doc_id: arxiv-math-0409593v1
doc_title: "CATEGORIFICATION OF THE BRAID GROUPS RAPHAËL ROUQUIER 1. Introduction Actions of braid groups on triangulated categories are quite widesp read. They arise for instance in represent"
section_id: sec-015-61-classical-isomorphisms
section_title: "Classical isomorphisms"
section_number: 6.1
pages: 15-21
source_pdf: 0409593v1.pdf
source_sha256: ad965f5c80838824
doc_brief: "CATEGORIFICATION OF THE BRAID GROUPS RAPHAËL ROUQUIER 1. Introduction Actions of braid groups on triangulated categories are quite widesp read. They arise for instance in representation theory, for co"
---
16 RAPHA ¨EL ROUQUIER
6.1.1. We consider here
• schemes of ﬁnite type over a ﬁeld of characteristic p ≥ 0 and the derived category of
constructible sheaves of Λ-modules, where Λ is a torsion ring with to rsion prime to p or
Λ is a Qℓ-algebra, for l prime to p
or
• locally compact topological spaces of ﬁnite soft c-dimension and the derived category of
constructible sheaves of C-vector spaces.
We will quote results pertaining to either of the two settings above, depending on the con-
venience of references. The maps involved will be concatenations o f canonical isomorphisms.
We denote a derived functor with the same notation as the original f unctor : we write ⊗ for
⊗L, f! for Rf!, etc...
6.1.2. Let f : Y → X and g : Z → Y be two morphisms. There are canonical isomorphisms
[KaScha, 2.6.6 and 2.3.9]
(f g)!
∼
→ f!g! and ( f g)∗ ∼
→ g∗f ∗.
These isomorphisms satisfy a cocycle property (cf [De1, Th´ eor` e me 5.1.8] for the case ( −)!) :
Lemma 6.1. Consider X3
w
− →X2
v
− →X1
u
− →X0. Then, the following diagrams are commu-
tative
w∗v∗u∗ /d47/d47
/d15/d15
w∗(uv)∗
/d15/d15
u!v!w! /d47/d47
/d15/d15
(uv)!w!
/d15/d15
(vw)∗u∗ /d47/d47 (uvw)∗ u!(vw)! /d47/d47 (uvw)!
We will take the liberty to identify the functors v∗u∗ and ( uv)∗ through the canonical iso-
morphism.
There are canonical isomorphisms [KaScha, 2.6.18]
f ∗(−1 ⊗ −2)
∼
→ (f ∗−1) ⊗ (f ∗−2) and ( −1 ⊗ −2) ⊗ −3
∼
→ − 1 ⊗ (−2 ⊗ −3)
We identify the bifunctors f ∗(−1 ⊗ −2) and ( f ∗−1) ⊗ (f ∗−2) through the canonical isomor-
phism. Given Ai ∈ Db(X), i ∈ { 1, 2, 3}, we identify ( A1 ⊗ A2) ⊗ A3 with A1 ⊗ (A2 ⊗ A3) and
we denote this object by A1 ⊗ A2 ⊗ A3.
Let X ′
f ′
/d15/d15
g′
/d47/d47 X
f
/d15/d15
S′
g
/d47/d47 S
be a cartesian square. Then, there is the canonical base change is omor-
phism [KaScha, 2.6.20] :
g∗f!
∼
→ f ′
! g′∗.
We have a canonical isomorphism [KaScha, 2.6.19]
−1 ⊗ (f!−2)
∼
→ f!(f ∗ −1 ⊗−2).
6.2. Kernel transforms.
CATEGORIFICATION OF THE BRAID GROUPS 17
6.2.1. Let us deﬁne a 2-category K.
• The 0-arrows are the varieties.
• 1-arrows : Hom( X, Y ) is the family of ( K, U) where U is a variety over Y × X and
K ∈ Db(U).
• 2-arrows : Hom(( K, U), (K ′, U ′)) is the set of ( φ, f) where f : U
∼
→ U ′ is an isomorphism
of ( Y × X)-varieties and φ : K
∼
→ f ∗K ′.
We deﬁne the composition of 1-arrows. Consider the following diagra m where the square is
cartesian
(2) V ×Y U
β
/d122/d122/d118 /d118 /d118 /d118 /d118 /d118 /d118 /d118 /d118 α
/d36/d36/d72/d72/d72/d72/d72/d72/d72/d72/d72
V
p4
/d127/d127/d126 /d126 /d126 /d126 /d126 /d126 /d126 p3
/d36/d36/d73/d73/d73/d73/d73/d73/d73/d73/d73/d73 U
p2
/d122/d122/d117 /d117 /d117 /d117 /d117 /d117 /d117 /d117 /d117 /d117 p1
/d32/d32/d64/d64/d64/d64/d64/d64/d64
Z Y X
Let K ∈ Db(U) and L ∈ Db(V ). We put L⊠ K = β∗L ⊗ α∗K. The composition ( L, V )(K, U)
is deﬁned to be ( L⊠ K, V ×Y U).
Let us consider now the diagram with all squares cartesian
W ×Z V ×Y U
b
/d118/d118/d110 /d110 /d110 /d110 /d110 /d110 /d110 /d110 /d110 /d110 /d110 /d110 a
/d40/d40/d80/d80/d80/d80/d80/d80/d80/d80/d80/d80/d80/d80
W ×Z V
δ
/d122/d122/d117 /d117 /d117 /d117 /d117 /d117 /d117 /d117 /d117 γ
/d40/d40/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81 V ×Y U
β
/d118/d118/d109 /d109 /d109 /d109 /d109 /d109 /d109 /d109 /d109 /d109 /d109 /d109 /d109 /d109 α
/d36/d36/d72/d72/d72/d72/d72/d72/d72/d72/d72
W
p6
/d126/d126/d125 /d125 /d125 /d125 /d125 /d125 /d125 /d125 p5
/d36/d36/d74/d74/d74/d74/d74/d74/d74/d74/d74/d74 V
p4
/d118/d118/d109 /d109 /d109 /d109 /d109 /d109 /d109 /d109 /d109 /d109 /d109 /d109 /d109 /d109 /d109 /d109 /d109
p3
/d40/d40/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81/d81 U
p2
/d122/d122/d117 /d117 /d117 /d117 /d117 /d117 /d117 /d117 /d117 /d117 p1
/d32/d32/d64/d64/d64/d64/d64/d64/d64
T Z Y X
and take M ∈ Db(W ). We have
(M⊠ L)⊠ K = b∗(δ∗M ⊗ γ∗L) ⊗ (αa)∗K
∼
→ (δb)∗M ⊗ a∗(β∗L ⊗ α∗K) = M⊠ (L⊠ K).
This provides the associativity isomorphisms for K. With our conventions, we will write M⊠
L⊠ K for the objects in the isomorphism above. It is straightforward to check that K is indeed
a 2-category.
6.2.2. We put Φ K = Φ p2,p1
K = p2!(K ⊗ p∗
1−) : Db(X) → Db(Y ).
Let cL,K : Φ LΦ K
∼
→ Φ L⊠K be deﬁned as the composition
p4!(L ⊗ p∗
3p2!(K ⊗ p∗
1−)) → p4!(L ⊗ β!α∗(K ⊗ p∗
1−))
→ p4!β!(β∗L ⊗ α∗(K ⊗ p∗
1−))
→ (p4β)!((β∗L ⊗ α∗K) ⊗ α∗p∗
1−)
→ (p4β)!((β∗L ⊗ α∗K) ⊗ (p1α)∗−).
18 RAPHA ¨EL ROUQUIER
Let ( φ, f) ∈ HomK((K, U), (K ′, U ′)). We have a commutative diagram
U
p2
/d7/d7/d14 /d14 /d14 /d14 /d14 /d14 /d14 /d14 /d14 /d14 /d14 /d14 /d14 /d14 /d14
p1
/d24/d24/d48/d48/d48/d48/d48/d48/d48/d48/d48/d48/d48/d48/d48/d48/d48
f ∼
/d15/d15
U ′
p′
2/d126/d126/d125 /d125 /d125 /d125 /d125 /d125 /d125
p′
1 /d32/d32/d65/d65/d65/d65/d65/d65/d65/d65
Y X
and we deﬁne Φ( φ, f) as the composition
p2!(K ⊗ p∗
1−)
∼
→ p′
2!f!(f ∗K ′ ⊗ f ∗p
′∗
1 −)
∼
→ p′
2!(K ′ ⊗ p
′∗
1 −).
Theorem 6.2. Φ is a 2-functor from K to the 2-category of triangulated categories.
We have cM ⊠L,K ◦ (cM,LΦ K) = cM,L⊠K ◦ (Φ M cL,K), i.e., the following diagram commutes :
Φ M Φ LΦ K /d47/d47
/d15/d15
Φ M ⊠LΦ K
/d15/d15
Φ M Φ L⊠K /d47/d47 Φ M ⊠L⊠K
6.2.3. The next two Lemmas deal with composition of base change isom orphisms.
For the ﬁrst Lemma, see [De1, Lemme 5.2.5] :
Lemma 6.3. Let X2
f2 /d47/d47
h2
/d15/d15
X1
f1 /d47/d47
h1
/d15/d15
X
h
/d15/d15
S2 g2
/d47/d47 S1 g1
/d47/d47 S
be a diagram with all squares cartesian. Then, the
following diagram commutes
(g1g2)∗h! /d47/d47
/d15/d15
h2!(f1f2)∗
g∗
2g∗
1h! /d47/d47 g∗
2h1!f ∗
1 /d47/d47 h2!f ∗
2 f ∗
1
/d79/d79
The second Lemma is [De1, Lemme 5.2.4] :
CATEGORIFICATION OF THE BRAID GROUPS 19
Lemma 6.4. Let X ′
2
f ′
2
/d15/d15
g2 /d47/d47 X2
f2
/d15/d15
X ′
1
f ′
1
/d15/d15
g1 /d47/d47 X1
f1
/d15/d15
S′
g
/d47/d47 S
be a diagram with all squares cartesian. Let A ∈ Db(S′).
Then, the following diagram commutes
A ⊗ g∗(f1f2)!−
/d15/d15
/d47/d47 A ⊗ (f ′
1f ′
2)!g∗
2− /d47/d47 (f ′
1f ′
2)!((f ′
1f ′
2)∗A ⊗ g∗
2−)
A ⊗ g∗f1!f2!−
/d15/d15
f ′
1!f ′
2!(f ′
2
∗f ′
1
∗A ⊗ g∗
2−)
/d79/d79
A ⊗ f ′
1!g∗
1f2!− /d47/d47 f ′
1!(f ′
1
∗A ⊗ g∗
1f2!−) /d47/d47 f ′
1!(f ′
1
∗A ⊗ f ′
2!g∗
2−)
/d79/d79
Lemma 6.5. Let f : Y → X and A, B ∈ Db(X) and C ∈ Db(Y ). Then, the following diagram
commutes
A ⊗ B ⊗ f!C /d47/d47
/d15/d15
f!(f ∗(A ⊗ B) ⊗ C)
/d15/d15
A ⊗ f!(f ∗B ⊗ C) /d47/d47 f!(f ∗A ⊗ f ∗B ⊗ C)
Proof. The corresponding statement for f! replaced by f∗ is easy, the key point is that the
composition f ∗ f ∗η
− − →f ∗f∗f ∗ εf ∗
− − →f ∗ is the identity of f ∗, where η and ε are the unit and counit
of the adjoint pair ( f ∗, f∗). The Lemma follows easily from this (in the algebraic case, we
have only to check in addition the trivial case where f is an open immersion thanks to the
transitivity of Lemma 6.4, whereas in the topological case we use the embedding f!C ⊂ f∗C
for C injective). □
Lemma 6.6. Let X ′
f ′
/d15/d15
g′
/d47/d47 X
f
/d15/d15
S′
g
/d47/d47 S
be a cartesian square. Let A ∈ Db(S) and B ∈ Db(X). Then,
the following diagram commutes
g∗A ⊗ g∗f!B /d47/d47
/d15/d15
g∗A ⊗ f ′
! g′∗B /d47/d47 f ′
! (f ′∗g∗A ⊗ g′∗B) /d47/d47 f ′
! (g′∗f ∗A ⊗ g′∗B)
/d15/d15
g∗(A ⊗ f!B) /d47/d47 g∗f!(f ∗A ⊗ B) /d47/d47 f ′
! g′∗(f ∗A ⊗ B)
20 RAPHA ¨EL ROUQUIER
Proof. As in the previous Lemma, one reduces to proving the analog of the L emma with ? !
replaced by ? ∗. This follows then from the easily checked commutativity of the two d iagrams
f ′∗g∗f∗ /d47/d47
/d15/d15
f ′∗f ′
∗g′∗
/d15/d15
g∗ /d47/d47
/d15/d15
g∗f∗f ∗
/d15/d15
g′∗f ∗f∗ /d47/d47 g′∗ f ′
∗f ′∗g∗ /d47/d47 f ′
∗g′∗f ∗
where we have used the units and counits of the adjoint pairs ( f ∗, f∗) and ( f ′∗, f ′
∗). □
Proof of the Theorem. We will show the commutativity of the following diagram
Φ p6,p5
M Φ p4β,p1α
L⊠K
ζ
/d15/d15
cM,L ⊠K
/d41/d41/d83/d83/d83/d83/d83/d83/d83/d83/d83/d83/d83/d83/d83/d83/d83
Φ M Φ LΦ K
Φ M cL,K
/d53/d53/d107/d107/d107/d107/d107/d107/d107/d107/d107/d107/d107/d107/d107/d107/d107
cM,L Φ K /d41/d41/d83/d83/d83/d83/d83/d83/d83/d83/d83/d83/d83/d83/d83/d83/d83 Φ p6δ,γ
δ∗M Φ β,p1α
L⊠K
cδ ∗M,L ⊠K /d47/d47 Φ M ⊠L⊠K
Φ p6δ,p3γ
M ⊠L Φ p2,p1
K
ξ
/d79/d79
cM ⊠L,K
/d53/d53/d107/d107/d107/d107/d107/d107/d107/d107/d107/d107/d107/d107/d107/d107/d107
where ζ is the composition
p6! (M ⊗ p∗
5(p4β)!(β∗L ⊗ α∗K ⊗ (p1α)∗−)) → p6! (M ⊗ p∗
5p4!β!(β∗L ⊗ α∗K ⊗ (p1α)∗−))
→ p6! (M ⊗ δ!γ∗β!(β∗L ⊗ α∗K ⊗ (p1α)∗−))
→ p6!δ! (δ∗M ⊗ γ∗β!(β∗L ⊗ α∗K ⊗ (p1α)∗−))
→ (p6δ)! (δ∗M ⊗ γ∗β!(β∗L ⊗ α∗K ⊗ (p1α)∗−))
and ξ the composition
(p6δ)! (δ∗M ⊗ γ∗L ⊗ (p3γ)∗p2!(K ⊗ p∗
1−)) → (p6δ)! (δ∗M ⊗ γ∗L ⊗ γ∗p∗
3p2!(K ⊗ p∗
1−))
→ (p6δ)! (δ∗M ⊗ γ∗(L ⊗ p∗
3p2!(K ⊗ p∗
1−)))
→ (p6δ)! (δ∗M ⊗ γ∗(L ⊗ β!α∗(K ⊗ p∗
1−)))
→ (p6δ)! (δ∗M ⊗ γ∗(L ⊗ β!(α∗K ⊗ α∗p∗
1−)))
→ (p6δ)! (δ∗M ⊗ γ∗(L ⊗ β!(α∗K ⊗ (p1α)∗−)))
→ (p6δ)! (δ∗M ⊗ γ∗β!(β∗L ⊗ α∗K ⊗ (p1α)∗−))
Let u and v be the compositions
u : p6!(M ⊗ p∗
5p4!−) → p6!(M ⊗ δ!γ∗−) → p6!δ!(δ∗M ⊗ γ∗−) → (p6δ)!(δ∗M ⊗ γ∗−)
and
v : L⊗p∗
3p2!(K⊗p∗
1−) → L⊗β!α∗(K⊗p∗
1−) → β!(β∗L⊗α∗(K⊗p∗
1−)) → β!(β∗L⊗α∗K⊗(p1α)∗−).
Then, one has trivially
ζ(Φ M cL,K) = u(L ⊗ p∗
3p2!(K ⊗ p∗
1−)) ◦ p6!(M ⊗ p∗
5p4!v) = ξ(cM,LΦ K).
CATEGORIFICATION OF THE BRAID GROUPS 21
The equality cM,L⊠K = cδ∗M,L⊠Kζ follows from Lemma 6.4 applied to g = p5, g1 = γ, g2 = a,
f1 = p4, f2 = β, f ′
1 = δ, f ′
2 = b and A = M and from Lemma 6.1 applied to u = p6, v = δ and
w = b.
The equality cM ⊠L,K = cδ∗M,L⊠Kξ follows from Lemma 6.3 applied to f1 = α, f2 = a, g1 = p3,
g2 = γ, h = p2, h1 = β and h2 = b, from Lemma 6.5 applied to f = b, A = δ∗M, B = γ∗L and
C = (αa)∗(K ⊗ p∗
1−) and from Lemma 6.6 applied to f = β, g = γ, f ′ = b, g′ = a, A = L and
B = α∗(K ⊗ p∗
1−). □
