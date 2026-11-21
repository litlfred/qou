---
doc_id: arxiv-0707.3799v3
doc_title: "Equivariant Satake category and Kostant-Whittaker reduction"
section_id: sec-017-45-transitivity-for-a-pair-of-levi-subgroups
section_title: "Transitivity for a pair of Levi subgroups"
section_number: 4.5
pages: 17-19
source_pdf: 0707.3799v3.pdf
source_sha256: 0b29cbced7939f72
toc_source: inferred
doc_brief: "Equivariant Satake category and Kostant-Whittaker reduction — 24 sections: Front matter; Introduction; Notation and statements of the res"
---
algΞL : gr(πL, Id, Id)∗ϕ(V ) ∼
−→(Id, πL, Id)∗ϕL(V |ˇL). In the RHS we have the restriction
of O(ˇt∗/WL ×ˇt∗/WL ×A1)-module ϕL(V |ˇL) to O(ˇt∗/WL ×ˇt∗/W ×A1). To save a bit of
notation in what follows we will write simply
algΞL : gr(πL, Id, Id)∗ϕ(V ) ∼
−→ϕL(V |ˇL).
If
ˇT
⊂
ˇL′
⊂
ˇL
is
another
Levi
subgroup,
then
we
denote
by
πL
L′
the
projection
from
ˇt∗/WL′
to
ˇt∗/WL.
Note
that
the
filtration
F •
L′
on
(πL′, Id, Id)∗ϕ(V )
=
(πL
L′, Id, Id)∗(πL, Id, Id)∗ϕ(V )
is
a
refinement
of
the
fil-
tration
(πL
L′, Id, Id)∗F •
L,
and
hence
induces
a
canonical
filtration
F L•
L′
on
(πL
L′, Id, Id)∗grF •
L(πL, Id, Id)∗ϕ(V ).
The isomorphism (πL
L′, Id, Id)∗algΞL carries the
filtration F L•
L′
to the filtration F •
L′ on (πL
L′, Id, Id)∗ϕL(V |ˇL).
We have a canonical
isomorphism
algΞL
L′
:
grF •
L′(πL
L′, Id, Id)∗ϕL(V |ˇL) ∼
−→ϕL′(V |ˇL′).
We consider the
composition
(6)
grF •
L′(πL′, Id, Id)∗ϕ(V )
grF L•
L′ (πL
L′,Id,Id)∗algΞL
−−−−−−−−−−−−−−−→grF •
L′(πL
L′, Id, Id)∗ϕL(V |ˇL)
algΞL
L′
−−−−→ϕL′(V |ˇL′)
Then we have
Lemma 8. algΞL
L′ ◦grF L•
L′ (πL
L′, Id, Id)∗algΞL =
algΞL′.
□
4.6. Tensor
structure
on
Kostant
functor. Recall
that
according
to
the proof of Lemma 5,
for V
∈
Rep( ˇG), we have a canonical isomorphism
ϕ(V ) ⊗O(ˇt∗/W×A1) W−
ℏ
∼
−→V ⊗W−
ℏ.
Thus,
for
V1, V2
∈
Rep( ˇG),
we
have
ϕ(V1)⊗O(ˇt∗/W×A1)ϕ(V2)⊗O(ˇt∗/W×A1)W−
ℏ
∼
−→ϕ(V1)⊗O(ˇt∗/W×A1)(V2⊗W−
ℏ) ∼
−→(V1⊗V2)⊗
W−
ℏ
∼
←−ϕ(V1 ⊗V2) ⊗O(ˇt∗/W×A1) W−
ℏ. Composing (and inverting) these isomorphisms
we obtain ϕ(V1 ⊗V2) ⊗O(ˇt∗/W×A1) W−
ℏ
∼
−→ϕ(V1) ⊗O(ˇt∗/W×A1) ϕ(V2) ⊗O(ˇt∗/W×A1) W−
ℏ,
18
ROMAN BEZRUKAVNIKOV AND MICHAEL FINKELBERG
and thus
algωV1,V2 : ϕ(V1 ⊗V2) ∼
−→ϕ(V1) ⊗O(ˇt∗/W×A1) ϕ(V2) =: ϕ(V1) ⋆ϕ(V2).
According to Lemma 6 (cf. also Lemma 7), we have a canonical isomorphism algΞV =
algΞT,V : gr(π, Id, Id)∗ϕ(V ) ∼
−→(Id, π, Id)∗ϕT (V | ˇT ). In the RHS we have the restriction
of O(ˇt∗×ˇt∗× A1)-module ϕT (V | ˇT ) to O(ˇt∗× (ˇt∗/W) × A1). To save a bit of notation in
what follows we will write simply algΞV : gr(π, Id, Id)∗ϕ(V ) ∼
−→ϕT (V | ˇT ). It follows that
after tensoring with k(ˇt∗×A1) (over the first and third factors in O(ˇt∗/W ×ˇt∗/W ×A1))
we have a canonical isomorphism
algΞgen
V
: ϕ(V ) ⊗O(ˇt∗/W×A1) k(ˇt∗× A1) = gr(π, Id, Id)∗ϕ(V ) ⊗O(ˇt∗×A1) k(ˇt∗× A1) ∼
−→
∼
−→ϕT (V | ˇT ) ⊗O(ˇt∗×A1) k(ˇt∗× A1) =
M
λ

O(Γλ) ⊗O(ˇt∗×A1) k(ˇt∗× A1)

⊗λV
Now we have a canonical isomorphism O(Γµ) ⋆O(Γν) := O(Γµ) ⊗O(ˇt∗×A1) O(Γν) =
O(Γµ+ν). Hence we get a canonical isomorphism algΞgen
V1 ⋆algΞgen
V2 :
(ϕ(V1)⋆ϕ(V2))⊗O(ˇt∗/W×A1)k(ˇt∗×A1) ∼
−→
M
µ+ν=λ

O(Γλ) ⊗O(ˇt∗×A1) k(ˇt∗× A1)

⊗µV1⊗νV2 =
=
M
λ

O(Γλ) ⊗O(ˇt∗×A1) k(ˇt∗× A1)

⊗λ(V1 ⊗V2)
We want to compare it with
algΞgen
V1⊗V2 : ϕ(V1⊗V2)⊗O(ˇt∗/W×A1)k(ˇt∗×A1) ∼
−→
M
λ

O(Γλ) ⊗O(ˇt∗×A1) k(ˇt∗× A1)

⊗λ(V1⊗V2)
Proposition 2.
algΞgen
V1⊗V2 = ( algΞgen
V1 ⋆algΞgen
V2 ) ◦algωV1,V2.
Proof : We consider the generic universal Verma module Mgen
ℏ
(−ρ) = Uℏ⊗Uℏ(ˇb)k(ˇt∗×
A1)(−ρ), and k(ˇt∗× A1)(−ρ) is a Uℏ(ˇb)-module which factors through the Uℏ(ˇt) =
O(ˇt∗×A1)-module where t ∈ˇt acts by multiplication by t−ℏρ(t). It is well known that
EndUℏ(Mgen
ℏ
(−ρ)) = k(ˇt∗×A1), and the category B of Uℏ(ˇn)-integrable Uℏ⊗k(ˇt∗×A1)-
modules is semisimple, and any simple object is isomorphic to Mgen
ℏ
(−ρ). In particular,
B is equivalent to the category of k(ˇt∗× A1)-modules.
For V ∈Rep( ˇG) we put φgen(V ) := φ(V ) ⊗O(ˇt∗×A1) k(ˇt∗× A1) = grφ(V ) ⊗O(ˇt∗×A1)
k(ˇt∗×A1). This is the restriction of a k(ˇt∗×A1)⊗O(ˇt∗)-module to k(ˇt∗×A1)⊗O(ˇt∗/W),
but we will view it as a k(ˇt∗× A1) ⊗O(ˇt∗)-module.
Arguing like in the proof of Lemma 5, we obtain a canonical isomorphism
φgen(V ) ⊗k(ˇt∗×A1) Mgen
ℏ
(−ρ) ∼
−→V ⊗Mgen
ℏ
(−ρ). This gives rise to the tensor structure
on the functor φgen:
φgen(V1 ⊗V2) ∼
−→φgen(V1) ⋆φgen(V2).
Clearly, the identification algΞgen
V
: φgen(V ) ∼
−→L
λ

O(Γλ) ⊗O(ˇt∗×A1) k(ˇt∗× A1)

⊗λV
commutes with the obvious tensor structure in the RHS.
On the other hand, arguing like in the proof of Lemma 5, we obtain a canonical
isomorphism φgen(V ) ∼
−→(Mgen
ℏ
(−ρ) ⊗V ⊗W−
ℏ) ⊗Uℏk[ℏ] which implies that the tensor
EQUIVARIANT SATAKE CATEGORY AND KOSTANT-WHITTAKER REDUCTION
19
structures on ϕ and φgen are compatible as well.
This completes the proof of the
proposition.
□
