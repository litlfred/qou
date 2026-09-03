---
doc_id: arxiv-math-0111205v1
doc_title: "From Subfactors to Categories and Topology II"
section_id: sec-015-33-semisimplicity-of-z1c
section_title: "Semisimplicity of Z1(C)"
section_number: 3.3
pages: 13-14
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
doc_brief: "From Subfactors to Categories and Topology II — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
Lemma 3.10 Let C be semisimple spherical with simple unit. We assume that the re are
only ﬁnitely many simple objects and that dim C ⁄= 0. Let (X, eX ), (Y, eY ) ∈ Z 1(C). Then
the map EX,Y : HomC(X, Y ) → HomC(X, Y ) deﬁned by
EX,Y (t) = (dim C)−1∑
i∈Γ
di
ε(Xi) Y
☛ ✟
❆❆
✁
✁
✁
❆❆eY (Xi)
Xi
✎
✍
☞
✌
t
Xi
eX (Xi)
❆❆
✁
✁
✁
❆❆
✡ ✠
X ε (Xi)
is a projection onto Hom Z1(C)((X, eX ), (Y, eY )) ⊂ HomC(X, Y ). Here {Xi, i ∈ Γ } is a
basis of simple objects and we abbreviate di = d(Xi). The family of maps EX,Y is a
conditional expectation in the sense that
EX,T (c ◦ b ◦ a) = c ◦ EY,Z (b) ◦ a (3.12)
if a ∈ HomZ1(C)((X, eX ), (Y, eY )), b ∈ HomC(Y, Z), c ∈ HomZ1(C)((Z, eZ ), (T, eT )).
Proof. We compute
dim C · idZ ⊗ EX,Y (t) ◦ eX(Z) =
∑
i∈Γ
di
Z Y
ε(Xi)
☛ ✟
❆❆
✁
✁
✁
❆❆
Xi
✎
✍
☞
✌
t
Xi
❆❆
✁
✁
✁
❆❆
✡ ✠ε(Xi)
❆❆
✁
✁
✁
❆❆X Z
=
∑
i
∑
j,α
di
Z Y ☛ ✟
Xj
✡ ✠ ❆❆
✁
✁
✁
❆❆
p′j,α
i ☛ ✟
✎
✍
☞
✌
t
Xi
❆❆
✁
✁
✁
❆❆
✡ ✠
❆❆
✁
✁
✁
❆❆X Z
13
=
∑
i
∑
j,α
di
Z Y ☛ ✟
Xj
✡ ✠ ❆❆
✁
✁
✁
❆❆
❆❆
✎
✍
☞
✌
t
❆❆
❆❆
✁
✁
✁
❆❆ Xi
✁✁ ☛ ✟
✡ ✠
X Z
=
∑
i,j,α
didj
d(Z)
Z Y
q′α
i,j ☛ ✟
Xj
❆❆
✁
✁
✁
❆❆✎
✍
☞
✌
t
Xi
❆❆
✁
✁
✁
❆❆
✡ ✠qα
i,j
X Z
=
∑
j
∑
i,α
dj
Z Y☛ ✟
✡ ✠
✁✁
❆❆
✁
✁
✁
❆❆
Xj❆❆
✎
✍
☞
✌
t
❆❆
Xi
❆❆
✁
✁
✁
❆❆ ☛ ✟r′iα
j
✡ ✠
X Z
=
∑
j
∑
i,α
dj
Z Y
❆❆
✁
✁
✁
❆❆
☛ ✟
❆❆
✁
✁
✁
❆❆
Xj
✎
✍
☞
✌
t
✡ ✠
Xi
❆❆
✁
✁
✁
❆❆ ☛ ✟
✡ ✠
X Z
=
∑
i
dj
Z Y
❆❆
✁
✁
✁
❆❆
☛ ✟
❆❆
✁
✁
✁
❆❆
Xj
✎
✍
☞
✌
t
Xj
❆❆
✁
✁
✁
❆❆
✡ ✠
X Z
= dim C · eY (Z) ◦ EX,Y (t) ⊗ idZ
Here {pj,α
i , α = 1, . . . , N Xj
Z,Xi} is, for every j ∈ Γ, a basis in Hom C(Xj, ZXi) with dual basis
{p′j,α
i } such that p′j,α
i ◦ pk,β
i = δj,kδαβ idXj and id ZX i =∑
j,α pj,α
i ◦ p′j,α
i . We used the fact
that eX (·), eY (·) are half-braidings, i.e. natural w.r.t. the second argume nt. Furthermore,
the basis {qα
i,j} in Hom C(Z, Xj Xı) and its dual basis are normalized such that trZ(q′β
i,j ◦
qα
i,j) = d(Z)δαβ . We used that a basis together with its dual can be replaced by another
one provided the normalizations are the same.
Since the above computation holds for all Z ∈ C we conclude that EX,Y (t) is in
HomZ1(C)((X, eX ), (Y, eY )). The property (3.12) for morphisms a, c in Z1(C) is obvious
since by (3.5) a, c can be pulled through the half braidings, changing the subsc ript of the
conditional expectation E appropriately. In order to show that EX,Y is idempotent it
thus suﬃces to show EX,X (idX ) = id X, which follows from the deﬁnition of dim C. ■
Remark 3.11 1. Since the conditional expectations depend also on the hal f braidings
we should in principle denote them E(X,eX ),(Y,eY ). We stick to EX,Y in order to keep the
formulae simple.
