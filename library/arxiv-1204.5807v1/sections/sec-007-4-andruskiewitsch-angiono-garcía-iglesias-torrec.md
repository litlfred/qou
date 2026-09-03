---
doc_id: arxiv-1204.5807v1
doc_title: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES"
section_id: sec-007-4-andruskiewitsch-angiono-garcía-iglesias-torrec
section_title: "ANDRUSKIEWITSCH, ANGIONO, GARCÍA IGLESIAS, TORRECILLAS , V AY"
section_number: 4
pages: 4-4
source_pdf: 1204.5807v1.pdf
source_sha256: 4bf4f73b0c152b19
doc_brief: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES — This is a survey on spherical Hopf algebras. We give criteria to decide when a Hopf algebra is spherical and collect exampl es."
---
Assume that H0 is a Hopf subalgebra of H. In this case, another funda-
mental invariant of H is the inﬁnitesimal braiding , a Yetter-Drinfeld module
V overH0, see [AS2]. We shall consider two particular cases:
• The Hopf algebra H is pointed if H0 = kG(H).
• The Hopf algebra H is copointed if H0 = kG for a ﬁnite group G.
Recall that x ∈ H is (g, 1) skew-primitive when ∆( x) = x⊗1 + g⊗x;
necessarily, g ∈ G(H). If H is generated as an algebra by group-like and
skew-primitive elements, then it is pointed.
We shall need the description of Yetter-Drinfeld modules over kG, G a
ﬁnite group; these are G-graded vector spaces M = ⊕g∈GMg provided with a
G-module structure such that g ·Mt =Mgtg− 1 for anyg,t ∈G. The category
kG
kGYD of Yetter-Drinfeld modules over G is semisimple and its irreducible
objects are parameterized by pairs (O,ρ ), where O is a conjugacy class of G
and ρ ∈ IrrCG(g), g ∈ O ﬁxed. We describe the corresponding irreducible
Yetter-Drinfeld module M (O,ρ ). Let g1 =g, . . . , gm be a numeration of O
and let xi ∈G such that xigx −1
i =gi for all 1 ≤i ≤m. Then
M (O,ρ ) = Ind G
CG(g)V = ⊕1≤i≤mxi ⊗V.
Letxiv :=xi ⊗v ∈M (O,ρ ), 1 ≤i ≤m,v ∈V . The Yetter-Drinfeld module
M (O,ρ ) is a braided vector space with braiding given by
(1.1) c(xiv ⊗xjw) = gi · (xjw) ⊗xiv =xhρ(γ)(w) ⊗xiv
for any 1 ≤i,j ≤m, v,w ∈V , where gixj =xhγ for unique h, 1 ≤h ≤m,
and γ ∈CG(g). Now the categories kG
kGYD and kG
kGYD are tensor equivalent,
so that a similar description of the objects of the latter hol ds, see e. g. [A V1].
The following notion is appropriate to describe all braided vector spaces
arising as Yetter-Drinfeld modules over some ﬁnite abelian group. A braided
vector space (V,c ) is of diagonal type if there exist qij ∈ k× and a basis
{xi}i∈I of V such that c(xi⊗xj) = qijxj⊗xi, for each pair i,j ∈I. In such
case, we say that i,j ∈I are connected if there exist ik ∈I, k = 0, 1,...,n ,
such that i0 = i, in = j, and qik− 1,ikqik,ik− 1 ⁄= 1 , 1 ≤ k ≤ n. It establishes
an equivalence relation on I. The equivalence classes are called connected
components, and V is connected if it has a unique component.
When H = kΓ , where Γ is a ﬁnite abelian group, each V ∈ H
HYD is a
braided vector space of diagonal type. Indeed, V = ⊕g∈Γ ,χ∈ˆΓV χ
g , where
Vg = {v ∈ V | δ(v) = g ⊗v}, V χ = {v ∈ V | g ·v = χ(g)v for all g ∈ Γ },
V χ
g = V χ ∩Vg. Note that c(x ⊗y) = χ(g)y ⊗x, for each x ∈ Vg, g ∈ Γ ,
y ∈V χ,χ ∈ ˆΓ . On the other hand, we can realize every braided vector space
of diagonal type as a Yetter-Drinfeld module over the group a lgebra of an
appropriate abelian group.
