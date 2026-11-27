---
doc_id: arxiv-1507.06276v2
doc_title: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS"
section_id: sec-034-81-choosing
section_title: "Choosing"
section_number: 8.1
pages: 42-43
source_pdf: 1507.06276v2.pdf
source_sha256: f552aa5de7125b23
toc_source: outline
doc_brief: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS — Let g be a symmetrizable Kac-Moody algebra and let Uq(g) de- note the corresponding quantized enveloping algebra."
---
the function γ : I → K(q1/d) given by (7.7). Extend the function γ to a group
homomorphism γ :P → K(q1/d)×. Depending on the choice of coeﬃcients c ∈ C ,
it may be necessary to replace K(q1/d) by a ﬁnite extension to do this. We will
illustrate the situation and comment on the ﬁeld extension in Subsect ion 8.4.
For any λ ∈P write
λ+ = λ + Θ(λ)
2 , ˜λ = λ − Θ(λ)
2 .
Observe that both ( λ+,λ +) and ( ˜λ, ˜λ) are contained in 1
2d Z for all λ ∈ P . Recall
from Section 2.1 that ̟∨
i for i ∈I denote the fundamental coweights. Now deﬁne
a function ξ :P → K(q1/d)× by
ξ(λ) = γ(λ)q−(λ+,λ+)+∑
k∈I ( ˜αk, ˜αk)λ(̟∨
k ).(8.1)
Remark 8.1. A priori one only has −(λ+,λ +) + ∑
k∈I (˜αk, ˜αk)λ(̟∨
k ) ∈ 1
2d Z.
However, for all g of ﬁnite type one can show by direct calculation that
−(λ+,λ +) +
∑
k∈I
(˜αk, ˜αk)λ(̟∨
k ) ∈ 1
d Z for all λ ∈P .(8.2)
To this end it is useful to reformulate the above condition as
−(˜λ, ˜λ) +
∑
k∈I
(˜αk, ˜αk)λ(̟∨
k ) ∈ 1
d Z for all λ ∈P .
and to work with the weight lattice P (Σ) of the restricted root system Σ of the
symmetric pair (g, k). The relation between P (Σ) and P is discussed in detail in
[Let08, Section 2] . We expect (8.2) also to hold for inﬁnite dimensional g. If it
does not hold, then the deﬁnition of ξ requires an extension of K(q1/d) also for the
q-power to lie in the ﬁeld.
UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS 43
We claim that ξ satisﬁes the recursion (7.8).
Lemma 8.2. The function ξ :P → K(q1/d)× deﬁned by (8.1) satisﬁes the relation
ξ(µ +ν) = ξ(µ)ξ(ν)q−(µ+Θ( µ),ν)(8.3)
for all µ,ν ∈P . In particular, ξ satisﬁes the recursion (7.8).
Proof. For any µ,ν ∈P one calculates
ξ(µ +ν) = γ(µ +ν)q−((µ+ν)+,(µ+ν)+)+∑
k∈I ( ˜αk, ˜αk)(µ+ν)(̟∨
k )
=γ(µ)γ(ν)q−(µ+,µ+)−(ν+,ν+)−(µ,ν)−(Θ( µ),ν)+∑
k∈I ( ˜αk, ˜αk)(µ+ν)(̟∨
k )
=ξ(µ)ξ(ν)q−(µ+Θ( µ),ν)
which proves (8.3). Choosing ν =αi one now obtains
ξ(µ +αi)
(8.3)
= ξ(µ)ξ(αi)q−(µ+Θ( µ),αi)
(8.1)
= ξ(µ)γ(i)q−(α+
i ,α+
i )+( ˜αi, ˜αi)−(µ,αi+Θ( αi))
As (α+
i ,α +
i ) − (˜αi, ˜αi) = ( αi, Θ(αi)) the above formula implies that ξ satisﬁes
recursion (7.8). □
