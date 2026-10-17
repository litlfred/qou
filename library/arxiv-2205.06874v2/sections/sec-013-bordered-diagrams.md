---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defects based on spherical fusion categories"
section_id: sec-013-bordered-diagrams
section_title: "Bordered diagrams"
section_number: null
pages: 18-19
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
toc_source: outline
doc_brief: "State sum models with defects based on spherical fusion categories — We define a Turaev-Viro-Barrett-Westbury state sum model of triangulated 3-manifolds with surface, line and point defects."
---
Bordered diagrams
Using the diagrammatic calculus from the previous sections, we define a generalisation of 2-category diagrams
for Cat, in which boundary segments and endpoints of lines at the boundary are also labeled with categorical
data. We also allow multiple lines to end in a common point on a boundary.
18
Definition 2.8. Let D be a 2-category diagram for Cat. A bordered diagram D′ for D is a diagram
obtained by labeling boundary segments and endpoints of lines at the boundary of D as follows:
• each boundary segment with an object of the adjacent category in D,
• an endpoint of lines labeled with functors F1, ..., Fn, from right to left, between a segment labeled by
a ∈ObA on the right and a segment labeled by b ∈ObB on the left with a morphism α : b →Fn · · · F1(a)
if it is on the top and with a morphism α : Fn · · · F1(a) →b if it is on the bottom of D.
b
a
F3 F2 F1
A
B
α
α : b →F3F2F1(a)
b
a
F3 F2 F1
A
B
α
α : F3F2F1(a) →b
Definition 2.9. Let D be a 2-category diagram that represents a natural transformation ν : F ⇒G and D′
a bordered diagram for D labeled with objects n ∈ObN on the left and m ∈ObM on the right.
The evaluation of D′ is the morphism ev(D′) = b ◦νm ◦t : n →n, where t : n →F(m) and b : G(m) →n
are morphisms assigned to the top and bottom of D′ as follows:
• take the image of each morphism at the top or bottom of D under the composite of all functors labeling
endpoints of lines to its left,
• compose the resulting morphisms from the left to the right at the top and from the right to the left at
the bottom of D.
The evaluation of a bordered diagram D′ for a 2-category diagram D is represented diagrammatically by
cutting its boundary square on the left-hand side and straightening its boundary to a vertical line. The
naturality condition (45) allows one to move vertices of D freely with respect to boundary vertices.
Example 2.10. A bordered diagram D′ for the diagram D in (30) and its evaluation are given by
m
p
p′
n
q
F
G
H
K
L
ρ
σ
M
P
Q
N
α
β
γ
δ
ϵ
n
α
ρ
F
p
m
β
σ
K
δ
H
γ
L
p′
ϵ
G
q
n
(47)
with morphisms α : n →F(p), β : p →K(m), γ : L(m) →p′, δ : H(p′) →q and ϵ : G(q) →n.
Its evaluation is the morphism b ◦νm ◦t : n →n, where ν = (ρL) ◦(Fσ) : FK ⇒GHL is the natural
transformation represented by D, t = F(β) ◦α : n →FK(m) and b = ϵ ◦(Gδ) ◦(GHγ) : GHL(m) →n. By
(45), this coincides with the morphism represented by the diagram on the right, which reads
n
α−→F(p)
F (β)
−−−→FK(m)
F (σm)
−−−−→FL(m)
γ−→F(p′)
ρp′
−−→GH(p′)
G(δ)
−−−→G(q)
ϵ−→n.
