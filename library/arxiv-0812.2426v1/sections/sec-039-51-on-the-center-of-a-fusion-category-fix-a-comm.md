---
doc_id: arxiv-0812.2426v1
doc_title: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS"
section_id: sec-039-51-on-the-center-of-a-fusion-category-fix-a-comm
section_title: "On the center of a fusion category. Fix a commutative ring k. Let C"
section_number: 5.1
pages: 16-17
source_pdf: 0812.2426v1.pdf
source_sha256: df1eb953bc2c6c63
doc_brief: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS — A theorem of M¨ uger asserts that the center Z(C) of a spherical k-linear category C is a modular category if k is an algebraically closed ﬁeld"
---
be a fusion category over k (see Section 1.8). Then the trivial Hopf monad 1 C is
centralizable. Its centralizer Z =Z1C is:
Z(X) =
⨁
i∈I
∨Vi ⊗X ⊗Vi,
with associated dinatural transformation iX,Y : ∨Y ⊗X ⊗Y →Z(X) given by:
iX,Y =
∑
i∈I
1≤α ≤N i
Y
∨qi,α
Y ⊗ idX ⊗pi,α
Y .
The double of 1 C isD1C =Z ◦ 1C =Z. Hence Z is a quasitriangular Hopf monad
and Z(C) ∼
=Z- C as braided categories. Furthermore, if C is spherical, then Z is a
ribbon Hopf monad (and so Z(C) is ribbon).
The structural morphisms of Z can be described only in terms of the category C,
that is, only using the p,q ’s (see Section 1.8), the duality morphisms, and the
sovereign structure φX : X → ∨∨X. They are depicted in Figure 7. The dotted
lines in the ﬁgure represent id V0 = id
/BD
and can be removed without changing
the morphisms. We depicted them in order to remember which factor of Z(X) is
concerned. To simplify the reading, we denote AVi1 ⊗···⊗Vin byAi1,...,i n forA =pi,α ,
qi,α , or N i.
Using the Maschke theorem for Hopf monad’s which characterize se misimplicity
(see [BV07, Theorem 6.5]), we have:
CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INV ARIANTS 17
Z2(X,Y ) =
∑
i∈I
PSfrag replacements
ViVi
ViX
X
Y
Y
∨Vi
∨Vi
∨Vi
, Z0 =
∑
i∈I
PSfrag replacements
Vi
X
Y
∨Vi
Vi
∨Vi
,
µX =
∑
i,j,k ∈I
1≤α ≤N k
i,j
PSfrag replacements
Vi
X
Y
∨Vi
Vi
∨Vi
Vi Vj
Vk
∨Vk
∨Vj
∨Vi X
X
∨qk,α
i,j pk,α
i,j
, ηX =
PSfrag replacements
Vi
X
Y
∨Vi
Vi
∨Vi
Vi
Vj
Vk
∨Vk
∨Vj
∨Vi
X
∨qk,α
i,j
pk,α
i,j
V0X
X
∨V0
,
sl
X =
∑
i∈I
PSfrag replacements
Vi
X
Y
∨Vi
Vi
∨Vi
Vi
Vj
Vk
∨Vk
∨Vj
∨Vi
X
∨qk,α
i,j
pk,α
i,j
V0
X
∨V0
∨∨Vi V∨ i
∨V∨ i
∨Vi
∨X
∨X
, sr
X =
∑
i∈I
PSfrag replacements
Vi
X
Y
∨Vi
Vi
∨Vi
Vi
Vj
Vk
∨Vk
∨Vj
∨Vi
X
∨qk,α
i,j
pk,α
i,j
V0
X
∨V0
∨∨Vi
V∨ i
∨V∨ i
∨Vi
∨X
Vi Vi∨∨Vi∨ V ∨
i X ∨
X ∨
,
RX,Y =
∑
i∈I
1≤α ≤N i
Y
PSfrag replacements
Vi
X
Y
∨Vi
Vi
∨Vi
Vi
Vj
Vk
∨Vk
∨Vj
∨Vi
X
∨qk,α
i,j
pk,α
i,j
V0
X
∨V0
∨∨Vi
V∨ i
∨V∨ i
∨Vi
∨X
Vi
Vi∨
∨Vi∨
V ∨
i
X ∨
ViV0
∨V0
∨Vi X
X Y
Y
pi
Yqi
Y , θX =
∑
i∈I
1≤α ≤N i
X
PSfrag replacements
Vi
X
Y
∨Vi
Vi
∨Vi
Vi
Vj
Vk
∨Vk
∨Vj
∨Vi
X
∨qk,α
i,j
pk,α
i,j
V0
X
∨V0
∨∨Vi
V∨ i
∨V∨ i
∨Vi
∨X
Vi
Vi∨
∨Vi∨
V ∨
i
X ∨
Vi
V0
∨V0
∨Vi
X
Y
pi
Y
qi
Y
V∨ i
∨V∨ i
X
X
pi
X
qi
X
φVi
.
Figure 7. Structural morphisms of Z
Proposition 5.1. [BV09] Let C be a spherical fusion category. Then the (ribbon)
Hopf monad Z is semisimple if and only if dim C is invertible.
Since Z(C) ∼
=Z- C, a direct consequence of Proposition 5.1 is then:
Corollary 5.2. Let C be a spherical fusion category over an algebraic closed ﬁeld .
Assume dim C is invertible. Then Z(C) is a ribbon fusion category.
