---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg"
section_id: sec-017-gluing-identities-for-polygon-diagrams
section_title: "Gluing identities for polygon diagrams"
section_number: null
pages: 26-28
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
doc_brief: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg — We define a"
---
We consider the pivotal 2-categoryBimodθ(C,D) for spherical fusion categoriesC,D. We fix setsIC, ID and
IM of representatives of the isomorphism classes of simple objects inC,D and in each bimodule categoryM.
For each objectx inC,D orM and each simple objecti in the set of representatives, we choose projection
morphisms pα
xi :x→i and inclusion morphismsjα
xi :i→x that satisfy (53).
Then we can glue and cut polygon diagrams by summing over the simple objects at their boundary segments
and over bases of the morphism spaces at their boundary vertices.
Theorem 3.1. The cyclic evaluations of the polygon diagrams forBimodθ(C,D) satisfy:
1. Gluing sides: for all objectsm∈IM, n∈IN
∑
α
m
n
F α
M
N
m
n
Fα
M
N
=
m
n
F
M
N
(66)
2. Gluing around a vertex:for all objectsm∈IM
∑
n,α dim(n) n
m
m
F
F
α
α
M
M
N = m
F
MN
(67)
3. Gluing a 2-gon:for all objectsm,n∈IM, x∈ ObC or x∈ ObD and all morphismsϕ :x→x
∑
m,n,α dim(m) dim(n)
x
x
α
α
ϕMm n = dim(M) ϕ
x
x
(68)
26
4. Inserting a diagram forC orD:
for all objectsi∈IC, x∈ ObC or i∈ID, x∈ ObD and morphismsϕ :i→x and ψ :x→i
∑
α
i
x
α
i
i
x
ϕ
α
=
i
x
ϕ
∑
α
x
i
α
i
i
x
α
ψ
=
x
i
ψ
(69)
Here, the polygon diagrams on each side of a equation stand for the product of their cyclic evaluations. It
is assumed that all parts of the diagrams that are not drawn coincide on the left-hand side and right-hand
side and that the object and morphism labels occur nowhere else in the diagrams. The vertex labelα stands
for the chosen projection and inclusion morphisms. The summations are over simple objects in the sets of
representatives and over bases of the morphism spaces. The functorF in (66) and (67) may be a composite
functor consisting of several lines or an action functorc▷− or−◁d.
Proof. Identity (66) follows from(56). The data at the boundaries and in the interiors of the first and second
diagram in(66) that is not drawn combines into morphismsµ :n→F (m) and ν :F (m)→n, respectively.
The diagram on the right-hand side of(66) is then given by the trace ofν◦µ. Equation (56) implies that
the cyclic evaluations on the left-hand side and right-hand side of (66) are given by
∑
α
n
n
F m
µ
α
n
n
F m
α
ν
(60)
=
n
n
F m
µ
ν
The proof of(69) is analogous. The only difference is that it uses the traces ofC orD. Identity(67) is a direct
consequence of the second identity in(53), depicted in(60). In this case, the contributions of the diagram in
the interior and the boundary morphisms that are not drawn combine into a morphismρ :F (m)→F (m) in
both diagrams. The cyclic evaluations of the left-hand side and right-hand side of (67) are then given by
∑
n,α dim(n)
m
m
n
m
F
F
F
ρ
α
α
(60)
=
m
m
F
F
ρ
Finally, to prove identity (68), we compute with the definition ofdim(n) and dimM
∑
m,n,α dim(m)
dim(n)
n
m
m
x
x
ϕ
α
α
(48)
=
∑
m,n,α dim(m)
dim(n)
m
x
x
x
ϕ
α
α
n
n
(60)
=
∑
n dim(n) n
x
x
ϕ (49)
= dimM
x
x
ϕ
27
Note that the first three identities in Theorem 3.1 are precisely the elementary transformations for polygon
presentations of surface groups, see for instance the books by Lee [L, Ch. 6] and by Seifert and Threlfall
[ST, Ch. 6.38 and 6.40]. Identity(66) corresponds to the cutting and pasting operation, identity(67) to the
folding and unfolding operation and identity(68) to the special case of the folding operation forS2. Identity
(69) describes the insertion of data from spherical categories into polygon diagrams.
